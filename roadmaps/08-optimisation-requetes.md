# 08 — Optimisation des Requêtes SQL

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #14 |
| **Phase** | 2 — Acquisition & First Revenue |
| **Type** | Tech |
| **LLM recommandé** | **Opus** (nécessaire — refactoring complexe de querysets annotés, Subquery, EXPLAIN ANALYZE) |
| **Statut** | ⬜ À faire |
| **Priorité** | 8 |
| **Dépendances** | Aucune |

---

## Description

Le dashboard élève (`_dashboard_eleve` dans `users/views.py`) contient un N+1 critique dans la boucle `for matiere in matieres:` qui exécute 3 requêtes par matière (~9 supplémentaires pour 3 matières). Le calcul du streak fait 2 requêtes séparées. Total : ~18-22 requêtes SQL. L'objectif est de descendre sous 10 requêtes via annotations bulk (`annotate()`, `Subquery`, `Count` conditionnel).

## Critères d'acceptation

- La boucle per-matière remplacée par un queryset annoté unique (1-2 requêtes au lieu de ~9)
- Le calcul du streak est consolidé
- `matieres_view` : les appels `chapitres_qs.exists()` dans la boucle admin éliminés
- Dashboard élève ≤10 requêtes SQL totales (mesuré via `assertNumQueries`)
- Aucune régression fonctionnelle

## Architecture

- **Fichier principal** : `backend/users/views.py` — refactoring de `_dashboard_eleve()`
- **Pattern per-matière** : queryset annoté avec `Count` conditionnel + `Avg`
  ```python
  matieres_stats = Matiere.objects.annotate(
      total_lecons=Count("chapitres__lecons", filter=Q(chapitres__niveau=user.niveau)),
      done=Count("chapitres__lecons__progressions", filter=Q(...statut="termine"...)),
      score_moyen=Avg("chapitres__lecons__quiz__resultats__score", filter=Q(...user=user)),
  ).filter(total_lecons__gt=0)
  ```
- **Streak** : combiner progressions et connexions via `union()` ou fusion Python des deux sets
- **`matieres_view`** : supprimer le guard `if chapitres_qs.exists()` (prefetch couvre déjà)
- **Fichiers impactés** : `backend/users/views.py`, `backend/courses/views.py`

## Tests

- `test_dashboard_eleve_num_queries` — `assertNumQueries` ≤10
- `test_dashboard_eleve_data_unchanged_after_optimization` — snapshot comparison des valeurs context
- `test_matieres_view_num_queries_student` — ≤5 requêtes
- `test_matieres_view_num_queries_admin` — ≤8 requêtes
- `test_dashboard_eleve_empty_state` — aucune progression → pas de division par zéro

## Sécurité

- Pas d'impact direct — s'assurer que les annotations filtrent par `user=request.user`

## Performance

- **Avant** : ~18-22 requêtes SQL
- **Après** : ≤10 requêtes SQL
- Indexes existants (`unique_together` sur progressions/résultats) suffisants
- Vérifier via `EXPLAIN ANALYZE`

## Definition of Done

- ≤10 requêtes SQL (vérifié par test)
- Données identiques avant/après
- Tests `assertNumQueries` en place
- CODEBASE_REFERENCE.md à jour
