# 21 — Badges / Récompenses

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #25 |
| **Phase** | 5 — Social & Gamification |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — 2 modèles simples, helper vérification, template section) |
| **Statut** | ⬜ À faire |
| **Priorité** | 21 |
| **Dépendances** | Aucune |

---

## Description

Système de badges : `Badge` (catalogue, 8 initiaux) + `UserBadge` (M2M horodatée). Attribution automatique via helper appelé depuis les vues existantes (pas de signals). Affichage dashboard élève (obtenus dorés, verrouillés grisés).

## Critères d'acceptation

- 8 badges seeded : premier_quiz, streak_10, score_parfait_lecon, score_parfait_chapitre, chapitre_complete, matiere_complete, revisions_assidu (50 questions), explorateur (3 matières)
- Attribution automatique au moment pertinent
- unique_together sur UserBadge — jamais en double
- Dashboard affiche obtenus + verrouillés (grisés `opacity-40`)
- Pas d'écriture en mode preview

## Architecture

- **Modèles** (`progress/models.py`) : `Badge` (code slug unique, nom, description, icone, categorie) + `UserBadge` (user FK, badge FK, obtenu_le)
- **Helper** : `_verifier_et_attribuer_badges(user, contexte)` — vérifie conditions, `get_or_create`
- **Appelé depuis** : `soumettre_quiz`, `soumettre_quiz_chapitre`, `_dashboard_eleve`
- **Seed** : `seed_badges.py` — 8 badges idempotent (`update_or_create`)
- **Template** : `dashboard/eleve.html` section "🏆 Mes badges"
- **Admin** : `BadgeAdmin`, `UserBadgeAdmin`

## Tests

- Badge attribué au premier quiz réussi, pas dupliqué au 2e
- Score parfait badge à 100%, pas à 99%
- Streak 10 → badge
- Dashboard affiche obtenus et grisés

## Sécurité

- UserBadge filtré par `user=request.user`
- Attribution serveur uniquement — pas d'endpoint auto-attribution
- `unique_together` empêche doublons même en race condition

## Performance

- `_verifier_et_attribuer_badges` : +1-2 requêtes SQL par appel
- Conditionnel : uniquement si quiz réussi
- Seed : 8 `update_or_create`

## Definition of Done

- 8 badges seeded et visibles admin
- Attribution automatique correcte
- Dashboard affichage obtenus/grisés
- Mode preview respecté
- Tests passent, CODEBASE_REFERENCE.md à jour
