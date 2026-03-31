# 25 — Stripe Pre-auth / Capture

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #36 |
| **Phase** | 7 — Tutorat, Calendrier & Facturation SAP |
| **Type** | Feature |
| **LLM recommandé** | **Opus** (nécessaire — Stripe PaymentIntent confirm+capture, webhooks, annulation/remboursement, sécurité PCI) |
| **Statut** | ⬜ À faire |
| **Priorité** | 25 |
| **Dépendances** | #24 Système de Réservation (le modèle Reservation) |

---

## Description

Paiement Stripe pour les sessions de tutorat : pre-autorisation à la réservation, capture automatique après la session confirmée, annulation du PaymentIntent si annulé >24h. Webhooks pour gérer les cas asynchrones.

## Critères d'acceptation

- Stripe Checkout / PaymentIntent en mode `capture_method=manual`
- Pre-auth au moment de la réservation
- Capture automatique 1h après fin de session validée (management command ou Celery)
- Annulation du PI si réservation annulée >24h avant
- Refund partiel si annulation <24h avec circonstances exceptionnelles (admin)
- Webhook `payment_intent.succeeded`, `payment_intent.payment_failed`, `charge.refunded`
- `stripe_payment_intent_id` stocké sur Reservation

## Architecture

- **Settings** : `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` via `.env`
- **Vues** : `creer_paiement(request, reservation_id)` → Stripe Checkout session, `stripe_webhook(request)` → `@csrf_exempt` + signature verification
- **Management command** : `capture_paiements_en_attente` — capture les PI dont session terminée depuis 1h
- **Modèle** : champ `stripe_payment_intent_id` (déjà prévu sur Reservation), + `paiement_statut` choices
- **URLs** : `/tutorat/paiement/<int:pk>/`, `/tutorat/webhook/stripe/`

## Tests

- Paiement créé avec capture_method=manual
- Webhook signature invalide → 400
- Webhook payment_intent.succeeded → paiement_statut mis à jour
- Capture command fonctionne pour sessions terminées
- Annulation → cancel du PI

## Sécurité

- **PCI** : jamais de numéro de carte côté serveur (Stripe Elements/Checkout)
- Webhook vérifié par signature `stripe.Webhook.construct_event()`
- `@csrf_exempt` uniquement sur webhook, avec vérification signature
- `STRIPE_SECRET_KEY` jamais en clair, toujours via env var
- `select_for_update()` avant capture pour éviter double-capture

## Performance

- Appels Stripe réseau (+200-500ms) — asynchrone via webhooks
- Capture batch via management command (pas blocking)
- Pas de polling client

## Definition of Done

- Pre-auth à la réservation, capture post-session
- Annulation/refund fonctionnels
- Webhooks sécurisés et idempotents
- Tests passent, CODEBASE_REFERENCE.md à jour
