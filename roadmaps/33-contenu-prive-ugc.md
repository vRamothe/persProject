# 33 — Contenu Privé / UGC (Enseignant)

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #44 |
| **Phase** | 10 — Scale & Autonomy |
| **Type** | Feature |
| **LLM recommandé** | **Opus** (nécessaire — modèle de permissions, workflow modération, Markdown preview, securité anti-XSS UGC) |
| **Statut** | ⬜ À faire |
| **Priorité** | 33 |
| **Dépendances** | Aucune |

---

## Description

Les enseignants peuvent créer du contenu privé (leçons + quiz) visible uniquement par leurs élèves liés. Workflow : brouillon → soumission → modération admin → publication privée. Markdown editor avec preview live.

## Critères d'acceptation

- Enseignant crée une leçon privée (Markdown) avec preview live
- Leçon privée visible uniquement par l'enseignant et ses élèves liés
- Quiz attachable à la leçon privée
- Workflow : brouillon → soumis → validé/rejeté par admin
- Admin voit la queue de modération
- Leçon publiée accessible via URL unique signée
- Dashboard enseignant : "Mes contenus" avec statuts

## Architecture

- **Modèles** : `LeconPrivee` (auteur FK, chapitre FK nullable, contenu Markdown, statut choices, slug unique) + `QuizPrive` + `QuestionPrivee`
- **Vues** : `creer_lecon_privee`, `modifier_lecon_privee`, `soumettre_moderation`, `moderer_lecon` (admin)
- **URLs** : `/enseignant/contenu/`, `/enseignant/contenu/<slug>/`, `/admin-tools/moderation/`
- **Templates** : formulaire Markdown avec Alpine.js preview via `marked.js` (CDN)
- **Visibilité** : `LeconPrivee.objects.filter(auteur__in=mes_enseignants, statut='valide')`
- **Admin** : file de modération (list_filter statut, date_soumission)

## Tests

- Enseignant crée contenu brouillon (201)
- Élève non lié ne voit pas le contenu (404)
- Élève lié voit le contenu validé
- Admin modère : valide → contenu visible, rejete → invisible
- Contenu soumis sans Markdown dangereux (pas de script tags)

## Sécurité

- **A03 XSS** : Markdown rendu côté serveur via `python-markdown` + `bleach` (sanitizer)
- **A01 Broken Access** : visibilité stricte auteur + élèves liés + admin
- **A04** : seul l'auteur peut modifier son contenu (pas un autre enseignant)
- Preview client côté Alpine = cosmétique, le rendu final est serveur
- Pas de `|safe` sur le contenu brut

## Performance

- Preview live : côté client (pas d'appel serveur)
- Modération : queryset paginé (20/page)
- Contenu privé : 1 requête filtrée

## Definition of Done

- Workflow complet brouillon → modération → publication
- Visibilité stricte, XSS protégé
- Dashboard enseignant + admin modération
- Tests passent, CODEBASE_REFERENCE.md à jour
