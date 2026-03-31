# 03 — Intégration Stripe

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #3 |
| **Phase** | 1 — Product & Proof |
| **Type** | Business |
| **LLM recommandé** | **Opus** (nécessaire — logique paiement complexe, webhooks, sécurité PCI) |
| **Statut** | ⬜ À faire |
| **Priorité** | 3 (première vente = validation business) |
| **Dépendances** | #02 Paywall Visuel (pour les CTA) |
| **Bloque** | Toutes les features de monétisation |

---

## Description

Intégrer Stripe comme système de paiement pour les abonnements premium. Deux paliers seront proposés : Mensuel (~€19/mois) et Annuel (~€119/an). L'implémentation utilise Stripe Checkout Sessions pour rediriger l'utilisateur vers la page de paiement hébergée par Stripe, puis un webhook `checkout.session.completed` active l'abonnement côté Django. Un nouveau modèle `Abonnement` stocke l'état de la souscription de chaque utilisateur (`stripe_customer_id`, `stripe_subscription_id`, statut actif/annulé/expiré). Le Stripe Customer Portal permettra à l'utilisateur de gérer son abonnement (annulation, changement de plan). Un helper `_user_has_active_subscription(user)` sera appelé dans les vues protégées (`lecon_view`, `quiz_view`, `lecon_publique_view`) pour vérifier l'accès premium côté serveur.

## Critères d'acceptation

- L'utilisateur authentifié peut souscrire un abonnement mensuel ou annuel via Stripe Checkout
- Le webhook `checkout.session.completed` crée/active l'`Abonnement` en base
- Le webhook `customer.subscription.deleted` / `customer.subscription.updated` désactive l'abonnement
- Les leçons non-`gratuit` ne sont accessibles qu'aux utilisateurs avec un abonnement actif, ou aux admins
- L'utilisateur peut gérer/annuler son abonnement via le Stripe Customer Portal (accessible depuis son profil)
- Le mode test Stripe (`STRIPE_SECRET_KEY=sk_test_...`) fonctionne en développement avec les webhooks CLI (`stripe listen`)

## Architecture

- **Nouveau modèle** (`users/models.py`) :
  ```
  Abonnement
  ├── user                    OneToOne → CustomUser (on_delete=CASCADE, related_name='abonnement')
  ├── stripe_customer_id      CharField(255)
  ├── stripe_subscription_id  CharField(255), blank
  ├── plan                    CharField(20) choices=[mensuel, annuel]
  ├── statut                  CharField(20) choices=[actif, annule, expire]
  ├── date_debut              DateTimeField
  ├── date_fin                DateTimeField(null, blank)
  ├── created_at              DateTimeField(auto_now_add)
  ├── updated_at              DateTimeField(auto_now)
  ```
- **Nouvelles vues** (`users/views.py`) :
  - `creer_checkout_session(request)` — POST, `@login_required` ; appelle `stripe.checkout.Session.create()` ; redirige vers `session.url`
  - `stripe_webhook(request)` — POST, `@csrf_exempt` ; vérifie la signature via `stripe.Webhook.construct_event()` ; traite checkout.session.completed, customer.subscription.updated, customer.subscription.deleted
  - `portail_client(request)` — GET, `@login_required` ; crée session Customer Portal et redirige
  - `checkout_success(request)` / `checkout_cancel(request)` — pages de confirmation/annulation
- **Nouvelles URLs** : `checkout` (POST), `stripe-webhook` (POST), `portail-abonnement` (GET), `checkout-success` (GET), `checkout-cancel` (GET)
- **Helper** : `_user_has_active_subscription(user)` — `Abonnement.objects.filter(user=user, statut='actif').exists()`
- **Settings** : `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, `STRIPE_WEBHOOK_SECRET`, `STRIPE_PRICE_MONTHLY`, `STRIPE_PRICE_ANNUAL`
- **Package** : `stripe` ajouté à `requirements.txt`
- **Transaction** : le webhook utilise `transaction.atomic()` pour l'écriture
- **Idempotence** : `update_or_create` sur `stripe_subscription_id`

## Tests

- `test_creer_checkout_session_redirects_to_stripe` — mock `stripe.checkout.Session.create` → asserter redirect 303
- `test_webhook_checkout_completed_creates_abonnement` — POST webhook signé → asserter `Abonnement(statut='actif')` créé
- `test_webhook_subscription_deleted_deactivates` — POST → asserter `statut == 'annule'`
- `test_webhook_rejects_invalid_signature` — asserter HTTP 400
- `test_webhook_idempotent_on_duplicate_event` — 2 envois → 1 seul `Abonnement`
- `test_premium_lesson_requires_active_subscription` — user sans abonnement → redirect/403
- `test_premium_lesson_accessible_with_active_subscription` — user avec abonnement actif → HTTP 200
- `test_admin_bypasses_subscription_check` — admin sans abonnement → HTTP 200
- `test_portail_client_redirects_to_stripe` — mock → asserter redirect

## Sécurité

- **A01** : accès vérifié côté serveur dans chaque vue via `_user_has_active_subscription()`
- **A02** : clés Stripe dans `.env` uniquement, jamais dans le code
- **A08** : signature webhook vérifiée via `stripe.Webhook.construct_event()`
- **CSRF** : webhook `@csrf_exempt` mais protégé par signature
- **PCI-DSS** : aucun numéro de carte ne transite par notre serveur — Stripe Checkout hébergé
- **Replay protection** : signature + idempotence `update_or_create`

## Performance

- `_user_has_active_subscription(user)` = 1 requête SQL (`EXISTS`) — budget +1 par page protégée
- Index sur `(user_id, statut)` dans le modèle `Abonnement`
- Appels Stripe API (~200-500ms) uniquement sur actions ponctuelles, pas en navigation

## Definition of Done

- Les deux paliers fonctionnent end-to-end en mode test Stripe
- Webhooks activent/désactivent avec idempotence et vérification de signature
- Accès premium vérifié côté serveur (admins exemptés)
- Customer Portal accessible depuis le profil
- Variables Stripe documentées dans `.env.example`
- Tests passent (Stripe mocké), CODEBASE_REFERENCE.md à jour
