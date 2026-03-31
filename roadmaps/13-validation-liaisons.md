# 13 — Système de Validation des Liaisons

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP_ROLES.md — Phase 3 (Étapes 3.1 à 3.7) |
| **Phase** | Roles — Phase 3 |
| **Type** | Tech |
| **LLM recommandé** | **Opus** (nécessaire — HTMX fragments, select_for_update, race conditions, cache notifications, 8 vues) |
| **Statut** | ⬜ À faire |
| **Priorité** | 13 |
| **Dépendances** | #12 Inscription Multi-Rôles |
| **Bloque** | #14 Dashboards Par Rôle |

---

## Description

Permettre aux enseignants et aux élèves de gérer les demandes de liaison (valider/refuser), aux enseignants d'ajouter un élève par code, et centraliser les notifications avec badge en temps réel via HTMX polling.

## Sous-étapes

### 3.1 — Liaisons Enseignant
- Vue `liaisons_enseignant_view` (GET, liste paginée 25/page, `select_related("eleve")`)
- Vue `action_lien_enseignant_view` (POST HTMX, valider/refuser)
- Helper `valider_lien(lien, valideur, action)` dans `helpers.py` — DRY entre enseignant et élève
- `select_for_update()` + `transaction.atomic()` contre race conditions
- Fragment HTMX `_fragment_lien_enseignant.html`

### 3.2 — Liaisons Élève (demandes parent)
- Même pattern que 3.1, réutilise `valider_lien()`
- Vue `liaisons_eleve_view` + `action_lien_eleve_view`
- Fragment `_fragment_lien_eleve.html`

### 3.3 — Ajout élève par code (enseignant)
- `AjouterEleveForm` dans `forms.py`
- Vue `ajouter_eleve_view` avec `get_or_create` (anti-doublon)
- Rate limit : 10 liaisons/h par enseignant

### 3.4 — Contrainte 1 enseignant par élève
- Intégré dans `valider_lien()` — `.exclude(pk=lien.pk).exists()`
- Refus automatique + notification au demandeur

### 3.5 — Contrainte max 2 parents par élève
- Intégré dans `valider_lien()` — `.count() >= 2`

### 3.6 — Notifications + badge cloche HTMX
- `notifications_view` (GET, paginée)
- `marquer_notification_lue_view` (POST HTMX)
- `tout_marquer_lu_view` (POST bulk `update()`)
- `badge_notifications_view` (GET fragment, `hx-trigger="load, every 30s"`)
- Cache `notif_count_{user_id}` (5 min TTL) + invalidation explicite

### 3.7 — Templates
- 4 templates + 3 fragments HTMX
- Boutons Valider/Refuser avec `hx-post`, `hx-target`, `hx-swap="outerHTML"`

## Tests (20+ minimum)

- Tests accès par rôle (enseignant 200, élève 403, anonyme redirect)
- Tests validation/refus de liens + notifications créées
- Tests IDOR (enseignant valide lien d'un autre → 404)
- Tests contraintes (1 enseignant, 2 parents max)
- Tests notifications (paginée, marquer lu, IDOR, tout marquer, badge HTMX)
- Tests rate limiting

## Sécurité

- IDOR protégé par `enseignant=request.user` / `eleve=request.user` dans get_object_or_404
- Race conditions via `select_for_update()`
- CSRF protégé (meta tag dans base.html)
- Enumération : messages génériques ("Code invalide.")

## Performance

- `select_related` sur tous les querysets — pas de N+1
- Pagination 25/page
- Cache notifications (5 min TTL)
- Budget SQL : ≤5 par page liste

## Definition of Done

- 8 vues + 8 URLs fonctionnelles
- Helper `valider_lien()` DRY
- Badge cloche HTMX avec polling 30s + cache
- Contraintes enseignant/parent enforced
- Tests passent, CODEBASE_REFERENCE.md à jour
