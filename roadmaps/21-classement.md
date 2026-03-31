# 21 — Classement (Leaderboard)

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #25 |
| **Phase** | 5 — Social & Gamification |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — queryset annoté, template tableau, toggle profil) |
| **Statut** | ⬜ À faire |
| **Priorité** | 21 |
| **Dépendances** | #20 Badges (pour le score nb_badges) |

---

## Description

Classement par niveau opt-in. Score agrégé : `(nb_quiz_reussis × 10) + (nb_badges × 5)`. Top 20, ligne courante mise en surbrillance. Champ `afficher_classement` (BooleanField default=False) sur CustomUser. Recalcul paresseux (à chaque chargement).

## Critères d'acceptation

- Page `/cours/classement/<str:niveau>/` — top 20
- Chaque ligne : rang, prénom + initiale, score agrégé
- Élève connecté surligné
- Toggle dans `/profil/` pour `afficher_classement`
- Élèves opt-out exclus du queryset
- Preview mode : classement vide

## Architecture

- **Modèle** : `CustomUser` + `afficher_classement` BooleanField(default=False)
- **Vue** : `classement_view(request, niveau)` — queryset annoté `Count` + `ExpressionWrapper`
- **URL** : `classement` → `/cours/classement/<str:niveau>/`
- **Template** : `templates/courses/classement.html`
- **Formulaire** : `ProfilForm` + `afficher_classement` checkbox
- **Sidebar** : lien "🏅 Classement"

## Tests

- 200 pour élève, exclusion opt-out, ordre décroissant, surbrillance, filtre niveau, login requis, preview vide

## Sécurité

- Prénom + initiale seulement (jamais email/nom complet)
- Score calculé serveur (anti-farming via rate limit quiz)
- `afficher_classement` default=False → RGPD opt-in

## Performance

- 1 requête SQL annotée complexe (LIMIT 20) + 1 pour rang utilisateur
- Cache 60s recommandé pour >1000 élèves/niveau

## Definition of Done

- Top 20 affiché, surbrillance, opt-out respecté
- Toggle profil fonctionnel
- Dark mode, tests passent, CODEBASE_REFERENCE.md à jour
