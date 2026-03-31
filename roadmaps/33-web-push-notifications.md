# 33 — Web Push Notifications

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #43 |
| **Phase** | 9 — Progressive Web App (PWA) |
| **Type** | Feature |
| **LLM recommandé** | **Opus** (nécessaire — VAPID keys, PushSubscription, pywebpush, SW push handler, permission flow) |
| **Statut** | ⬜ À faire |
| **Priorité** | 33 |
| **Dépendances** | #31 PWA Manifest & SW |

---

## Description

Notifications push via Web Push API (VAPID). L'élève reçoit des rappels de révision, des notifications de nouveaux chapitres disponibles, et des alertes quand un enseignant valide sa réservation. Permission demandée une seule fois, opt-out dans le profil.

## Critères d'acceptation

- VAPID keypair générée (management command)
- Endpoint `/api/push/subscribe/` — stocke la subscription
- Endpoint `/api/push/unsubscribe/` — supprime
- Envoi via `pywebpush` depuis le serveur
- Types : rappel_revision, nouveau_chapitre, reservation_validee
- SW `push` event handler avec notification display
- Préférences utilisateur (BooleanField par type)
- Permission demandée via Alpine.js (`Notification.requestPermission()`)

## Architecture

- **Settings** : `VAPID_PUBLIC_KEY`, `VAPID_PRIVATE_KEY`, `VAPID_CLAIMS_EMAIL`
- **Modèle** : `PushSubscription` (user FK, endpoint, p256dh, auth, created_at)
- **Lib** : `pywebpush` (ajout requirements.txt)
- **Vues** : `push_subscribe`, `push_unsubscribe` (POST HTMX)
- **Helper** : `envoyer_push(user, titre, corps, url)` — itère sur subscriptions user
- **SW** : `self.addEventListener('push', ...)` → `self.registration.showNotification()`
- **Management command** : `generer_vapid_keys`
- **Alpine** : composant `pushPermission()` dans `base.html`

## Tests

- Subscribe → PushSubscription créée
- Unsubscribe → PushSubscription supprimée
- Double subscribe → update (pas doublon)
- envoyer_push avec 0 subscriptions → no-op
- Push endpoint non accessible sans login

## Sécurité

- VAPID private key en env var uniquement
- Subscription liée à user (pas d'envoi à des users arbitraires)
- Pas de PII dans les notifications (titre + lien uniquement)
- `@login_required` sur subscribe/unsubscribe
- Rate limiting : 3 push / user / heure

## Performance

- `pywebpush` : ~100ms par push
- Batch envoi : `ThreadPoolExecutor` pour >10 users
- Subscription cleanup : supprimer si `WebPushException(410 Gone)`

## Definition of Done

- Push fonctionnel sur Chrome/Edge/Firefox
- 3 types de notifications
- Opt-in/opt-out, préférences profil
- Tests passent, CODEBASE_REFERENCE.md à jour
