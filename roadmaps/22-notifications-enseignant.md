# 22 — Notifications Enseignant (Élèves en Difficulté)

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #26 |
| **Phase** | 5 — Social & Gamification |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — modèle simple, helper dans soumettre_quiz, email, panneau admin) |
| **Statut** | ⬜ À faire |
| **Priorité** | 22 |
| **Dépendances** | Aucune |

---

## Description

Notification admin/enseignant quand un élève échoue 3+ fois au quiz d'un chapitre sans réussir. Email envoyé une seule fois par (élève, chapitre). Panneau "⚠️ Élèves en difficulté" sur dashboard admin. Résolution quand l'élève réussit.

## Critères d'acceptation

- Notification après 3+ échecs consécutifs sans réussite
- Email aux admins actifs (1 seule fois par couple élève-chapitre)
- Résolution automatique quand l'élève réussit
- Dashboard admin : panneau non résolues (top 20)
- Mode preview ne déclenche pas de notifications

## Architecture

- **Modèle** (`progress/models.py`) : `Notification` (user FK, chapitre FK, type, nb_tentatives, meilleur_score, resolue, envoyee, unique_together)
- **Helpers** : `_verifier_difficulte_eleve(user, chapitre)` et `_resoudre_notification(user, chapitre)` dans `progress/views.py`
- **Vue modifiée** : `_dashboard_admin` charge les non résolues
- **Templates email** : `notification_difficulte.html` + `.txt`
- **Admin** : `NotificationAdmin`

## Tests

- Notification créée après 3 échecs, pas avant 3
- Email envoyé aux admins, pas dupliqué au 4e échec
- Résolution à la réussite
- Dashboard admin affiche les non résolues
- Preview mode skip

## Sécurité

- Données scolaires — accès restreint aux admins (RGPD)
- Anti-spam : email 1 seule fois via `envoyee=False` guard
- `unique_together` anti-doublons DB

## Performance

- +1 `get_or_create` dans `soumettre_quiz_chapitre` (quand passe=False)
- +1 requête dashboard admin (LIMIT 20 + select_related)

## Definition of Done

- Notification + email après 3+ échecs
- 1 seule notification par (élève, chapitre)
- Résolution automatique
- Panneau admin, preview respecté
- Tests passent, CODEBASE_REFERENCE.md à jour
