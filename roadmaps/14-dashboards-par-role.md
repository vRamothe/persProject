# 14 — Dashboards Par Rôle

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP_ROLES.md — Phase 4 (Étapes 4.1 à 4.6) |
| **Phase** | Roles — Phase 4 |
| **Type** | Tech |
| **LLM recommandé** | **Opus** (nécessaire — 4 dashboards, fiche élève complète, TruncDate, Chart.js, helpers, context processor) |
| **Statut** | ⬜ À faire |
| **Priorité** | 14 |
| **Dépendances** | #13 Validation Liaisons |
| **Bloque** | #15 Messagerie Interne |

---

## Description

Router le tableau de bord par rôle et créer les dashboards enseignant + parent, la fiche élève complète, adapter le dashboard élève avec ses relations, et conditionner la sidebar.

## Sous-étapes

### 4.1 — Router le tableau de bord
- `TableauDeBordView.get()` dispatch vers 4 branches (admin/enseignant/parent/eleve)

### 4.2 — Dashboard Enseignant
- `_dashboard_enseignant(request)` : stats classe, tableau élèves, graphique 30j (Chart.js)
- Helper `_calculs_stats_classe(enseignant)` dans `helpers.py`
- Données : demandes en attente, messages non lus, progression moyenne, score moyen
- Tableau élèves : nom, niveau, progression %, score moyen, dernière connexion, streak

### 4.3 — Dashboard Parent
- `_dashboard_parent(request)` : carte par enfant (max 2), détails expandable (Alpine.js)
- Notes par matière (couleurs bleu/emerald/violet), points forts/faibles, graphique 30j
- Max 2 enfants → budget ≤12 requêtes SQL

### 4.4 — Fiche Élève Complète
- `fiche_eleve_view(request, eleve_id)` — 7 sections
- Helper `peut_voir_eleve(user, eleve)` : admin=True, enseignant lié=True, parent lié=True, sinon=False
- Sections : Identité, Relations, Heatmap 90j, Scores/matière, Points forts, Points faibles (Leitner box=1), Progression/matière
- Budget : ≤8 requêtes SQL

### 4.5 — Adaptation Dashboard Élève
- Ajouter au contexte : enseignant lié, parents liés, code identifiant (bouton copier), badge notifications

### 4.6 — Sidebar Conditionnelle
- `base.html` : liens conditionnels `{% if user.is_eleve %}` / `{% if user.is_enseignant %}` / etc.
- Context processor `notifications_context()` : compteur cache 5 min

## Tests (25+ minimum)

- Routage dashboard (4 tests template)
- Accès fiche élève (7 tests : admin/enseignant lié/parent lié/non lié/élève/anonyme/mauvais rôle)
- Helper `peut_voir_eleve` (5 tests)
- Données affichées (4 tests états vides/pleins)
- Sidebar conditionnelle (4 tests liens par rôle)
- IDOR (2 tests)

## Sécurité

- `peut_voir_eleve()` vérifie lien validé — IDOR impossible
- Pas d'emails affichés dans les fiches
- `get_object_or_404` avec `role=ELEVE` → 404 pour non-élèves

## Performance

- Dashboard enseignant : ≤12 requêtes SQL
- Dashboard parent : ≤12 requêtes (max 2 enfants)
- Fiche élève : ≤8 requêtes SQL
- Context processor : cache 5 min sur COUNT notifications

## Definition of Done

- 4 dashboards fonctionnels + fiche élève 7 sections
- Sidebar conditionnelle par rôle
- Context processor notifications
- Heatmap + Chart.js fonctionnels
- Tests passent, CODEBASE_REFERENCE.md à jour
