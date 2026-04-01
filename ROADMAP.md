# ScienceLycée — Unified Roadmap

> **Core rule:** No new "nice-to-have" features until Stripe is live and the first real sale is processed.

---

## Phase 1 — Product & Proof (Weeks 1–2)

*Goal: make the app sellable and prove demand with real users.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 1 | ~~**Open "hook" content (SEO & storefront)**~~ | Business | Sonnet | ✅ |
| 2 | ~~**Visual paywall**~~ | Business | Sonnet | ✅ |
| 3 | **Stripe integration** | Business | **Opus** | ⬜ |
| 4 | ~~**Password reset flow**~~ | Tech | Sonnet | ✅ |
| 5 | ~~**Custom error pages (404, 500)**~~ | Tech | Sonnet | ✅ |
| 6 | ~~**Automated tests + CI**~~ | Tech | Sonnet | ✅ |

---

### #2 — Visual paywall

**Description** : Les leçons premium (non `gratuit`) doivent rester visibles dans le catalogue public et les listings de chapitres, mais afficher un cadenas 🔒 signalant un contenu réservé aux abonnés. Au clic sur une leçon verrouillée, un modal Alpine.js s'affiche avec un pitch commercial ("Débloquez tout le programme Bac"), les deux paliers tarifaires (mensuel/annuel) et un CTA vers le paiement Stripe. L'objectif est de convertir les visiteurs en abonnés sans les rediriger vers une simple page de login. Le modal doit respecter le système de couleurs par matière et le dark mode global via les CSS overrides existants dans `base.html`.

🎯 **Critères d'acceptation**
- Les leçons non-`gratuit` affichent un cadenas 🔒 dans `catalogue.html`, `chapitres.html` et `accueil.html`
- Le clic sur une leçon verrouillée ouvre un modal Alpine.js (pas de redirection vers `/connexion/`)
- Le modal affiche les deux paliers tarifaires (Mensuel ~€19/mois, Annuel ~€119/an) avec un CTA pointant vers la Stripe Checkout Session (cf. #3)
- Le modal respecte le design system (couleurs par matière via `MATIERE_COULEURS`, dark mode via les overrides globaux)
- Sur mobile, le modal est responsive (full-screen ou bottom-sheet selon la taille d'écran)

🏗 **Architecture**
- **Nouveau template partiel** : `templates/components/_paywall_modal.html` — composant Alpine.js (`x-data="{ showPaywall: false, plan: 'mensuel' }"`) inclus via `{% include %}` dans les templates concernés
- **Templates modifiés** : `catalogue.html`, `accueil.html`, `lecon_publique.html` — ajout conditionnel du cadenas (`{% if not lecon.gratuit %}🔒{% endif %}`) et du `@click` Alpine qui ouvre le modal
- **Pas de nouveau modèle** : le flag `Lecon.gratuit` existe déjà ; le modal est purement front-end
- **Patterns** : le modal utilise `x-show`, `x-transition` et `@click.away="showPaywall = false"` pour une UX fluide. Les URLs des CTA (`{% url 'checkout' %}?plan=mensuel`) seront câblées une fois #3 implémenté. En attendant, un lien `#` avec `disabled` suffit.
- **Fichiers impactés** : `templates/components/_paywall_modal.html` (nouveau), `templates/courses/catalogue.html`, `templates/courses/accueil.html`, `templates/courses/lecon_publique.html`

🧪 **Tests**
- `test_catalogue_shows_lock_icon_on_premium_lessons` — GET `/cours/<matiere_slug>/`, asserter que le HTML contient `🔒` pour chaque leçon où `gratuit=False`
- `test_catalogue_no_lock_on_free_lessons` — même page, asserter l'absence de cadenas pour les leçons `gratuit=True`
- `test_paywall_modal_markup_present` — asserter que le HTML de la page contient `x-data` et `showPaywall` (le composant Alpine est bien inclus)
- `test_premium_lesson_public_view_still_blocks_content` — GET `/cours/<matiere>/<niveau>/<chapitre>/<lecon>/` sur une leçon `gratuit=False` → redirect vers login (le serveur ne livre pas le contenu)

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : le contenu Markdown de la leçon premium n'est **jamais** inclus dans le HTML de la page catalogue — le serveur ne l'envoie pas, le cadenas est la seule chose affichée. `lecon_publique_view` continue de rediriger les leçons non-gratuites vers le login.
- Le modal ne contient aucune donnée sensible (uniquement du texte marketing et des prix).

⚡ **Performance**
- Le partial `_paywall_modal.html` pèse < 2 KB — aucun impact mesurable sur le TTFB
- Pas de requête SQL ajoutée : le flag `gratuit` est déjà chargé dans les querysets existants des vues catalogue/accueil
- Budget : +0 requête SQL par page

✅ **Definition of Done**
- Les cadenas s'affichent correctement sur les trois templates de listing (catalogue, accueil, leçon publique)
- Le modal s'ouvre au clic, affiche les paliers, et se ferme au clic extérieur ou bouton ✕
- Le dark mode fonctionne (pas de classes `dark:` dans les templates enfants — uniquement les overrides CSS globaux)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (section 5 — Templates)

---

### #3 — Stripe integration

**Description** : Intégrer Stripe comme système de paiement pour les abonnements premium. Deux paliers seront proposés : Mensuel (~€19/mois) et Annuel (~€119/an). L'implémentation utilise Stripe Checkout Sessions pour rediriger l'utilisateur vers la page de paiement hébergée par Stripe, puis un webhook `checkout.session.completed` active l'abonnement côté Django. Un nouveau modèle `Abonnement` stocke l'état de la souscription de chaque utilisateur (`stripe_customer_id`, `stripe_subscription_id`, statut actif/annulé/expiré). Le Stripe Customer Portal permettra à l'utilisateur de gérer son abonnement (annulation, changement de plan). Un helper `_user_has_active_subscription(user)` sera appelé dans les vues protégées (`lecon_view`, `quiz_view`, `lecon_publique_view`) pour vérifier l'accès premium côté serveur.

🎯 **Critères d'acceptation**
- L'utilisateur authentifié peut souscrire un abonnement mensuel ou annuel via Stripe Checkout
- Le webhook `checkout.session.completed` crée/active l'`Abonnement` en base
- Le webhook `customer.subscription.deleted` / `customer.subscription.updated` désactive l'abonnement
- Les leçons non-`gratuit` ne sont accessibles qu'aux utilisateurs avec un abonnement actif, ou aux admins
- L'utilisateur peut gérer/annuler son abonnement via le Stripe Customer Portal (accessible depuis son profil)
- Le mode test Stripe (`STRIPE_SECRET_KEY=sk_test_...`) fonctionne en développement avec les webhooks CLI (`stripe listen`)

🏗 **Architecture**
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
  - `creer_checkout_session(request)` — POST, `@login_required` ; appelle `stripe.checkout.Session.create()` avec le `price_id` correspondant au plan ; redirige vers `session.url`
  - `stripe_webhook(request)` — POST, `@csrf_exempt` ; vérifie la signature via `stripe.Webhook.construct_event(payload, sig, STRIPE_WEBHOOK_SECRET)` ; traite `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`
  - `portail_client(request)` — GET, `@login_required` ; crée une session Customer Portal et redirige
  - `checkout_success(request)` — GET, page de confirmation post-paiement
  - `checkout_cancel(request)` — GET, page d'annulation
- **Nouvelles URLs** (`users/urls.py`) : `checkout` (POST), `stripe-webhook` (POST), `portail-abonnement` (GET), `checkout-success` (GET), `checkout-cancel` (GET)
- **Helper** : `_user_has_active_subscription(user)` dans `users/views.py` — `Abonnement.objects.filter(user=user, statut='actif').exists()` ; appelé dans `lecon_view`, `quiz_view`, `lecon_publique_view` pour gate l'accès premium
- **Settings** (`config/settings/base.py`) : `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, `STRIPE_WEBHOOK_SECRET`, `STRIPE_PRICE_MONTHLY`, `STRIPE_PRICE_ANNUAL` — tous lus via `decouple.config()`
- **Package** : `stripe` ajouté à `requirements.txt`
- **Templates** : `templates/users/checkout_success.html`, `templates/users/checkout_cancel.html` ; mise à jour de `templates/users/profile.html` (lien vers le portail) et `templates/components/_paywall_modal.html` (CTA avec `{% url 'checkout' %}`)
- **Transaction** : le webhook utilise `transaction.atomic()` pour l'écriture de `Abonnement` afin d'éviter les race conditions en cas de retry Stripe
- **Idempotence** : le webhook gère les événements dupliqués (Stripe peut renvoyer le même event) via `update_or_create` sur `stripe_subscription_id`

🧪 **Tests**
- `test_creer_checkout_session_redirects_to_stripe` — mock `stripe.checkout.Session.create` pour retourner une URL fictive ; POST `/checkout/` → asserter redirect 303 vers l'URL Stripe
- `test_webhook_checkout_completed_creates_abonnement` — POST `/stripe-webhook/` avec payload signé simulé (`checkout.session.completed`) → asserter `Abonnement.objects.filter(user=user, statut='actif').exists()`
- `test_webhook_subscription_deleted_deactivates` — POST avec payload `customer.subscription.deleted` → asserter `Abonnement.statut == 'annule'`
- `test_webhook_rejects_invalid_signature` — POST avec un header `Stripe-Signature` invalide → asserter HTTP 400
- `test_webhook_idempotent_on_duplicate_event` — envoyer deux fois le même `checkout.session.completed` → asserter qu'un seul `Abonnement` existe (pas de doublon)
- `test_premium_lesson_requires_active_subscription` — user authentifié sans `Abonnement` → GET `/cours/lecon/<pk>/` sur leçon `gratuit=False` → redirect ou HTTP 403
- `test_premium_lesson_accessible_with_active_subscription` — user avec `Abonnement(statut='actif')` → GET → HTTP 200
- `test_admin_bypasses_subscription_check` — admin sans abonnement → GET leçon premium → HTTP 200
- `test_portail_client_redirects_to_stripe` — mock `stripe.billing_portal.Session.create` → asserter redirect

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : l'accès premium est vérifié **côté serveur** dans chaque vue (`_user_has_active_subscription()`), jamais uniquement côté client
- **OWASP A02 (Cryptographic Failures)** : les clés Stripe (`STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`) restent exclusivement dans les variables d'environnement (`.env`), jamais dans le code source ou les templates
- **OWASP A08 (Software and Data Integrity)** : chaque requête webhook est validée via `stripe.Webhook.construct_event()` avant tout traitement — rejet immédiat (HTTP 400) si la signature est invalide
- **CSRF** : le webhook est `@csrf_exempt` car Stripe ne peut pas envoyer de CSRF token, mais il est protégé par la vérification de signature
- **PCI-DSS** : aucun numéro de carte ne transite par notre serveur — tout passe par Stripe Checkout (hosted page)
- **Replay protection** : combiner signature + idempotence (`update_or_create` sur `stripe_subscription_id`) neutralise les replays

⚡ **Performance**
- `_user_has_active_subscription(user)` = 1 requête SQL (`EXISTS` sur `Abonnement`) — budget +1 requête par page protégée
- **Index** : index sur `(user_id, statut)` dans le modèle `Abonnement` pour rendre le `EXISTS` instantané
- **Cache session** (optimisation optionnelle) : stocker `request.session['has_subscription'] = True/False` lors du login et du webhook → 0 requête SQL supplémentaire en régime normal. Invalidation : le webhook met à jour la session via `SessionStore` si l'utilisateur a une session active
- Les appels Stripe API (`Session.create`, `billing_portal.Session.create`) sont synchrones (~200-500ms) mais n'interviennent que sur des actions utilisateur ponctuelles (clic CTA), pas sur chaque page load
- Budget global : +0 (avec cache session) ou +1 (sans cache) requête SQL par page protégée

✅ **Definition of Done**
- Les deux paliers (mensuel/annuel) fonctionnent end-to-end en mode test Stripe (Checkout → webhook → `Abonnement` actif)
- Les webhooks activent/désactivent correctement l'`Abonnement` avec idempotence et vérification de signature
- L'accès aux leçons premium est vérifié côté serveur (admins exemptés)
- Le Customer Portal est accessible depuis le profil utilisateur
- Variables d'environnement Stripe documentées dans `.env.example`
- Tests passent (tous les appels Stripe mockés)
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2, 3, 5, 6)

---

## Phase 2 — Acquisition & First Revenue (Weeks 3–4)

*Goal: get paying users and build trust.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 7 | **Beta test with current students** | Business | — | ⬜ |
| 8 | **Social proof on landing page** | Business | Sonnet | ⬜ |
| 9 | **"Hybrid Bac Sprint" upsell** | Business | — | ⬜ |
| 10 | **Local marketing (Grasse & 06)** | Business | — | ⬜ |
| 11 | ~~**Rate limiting on login & quiz**~~ | Tech | Sonnet | ✅ |
| 12 | ~~**Email verification on signup**~~ | Tech | Sonnet | ✅ |
| 13 | **Query optimization** | Tech | **Opus** | ⬜ |

---

### #7 — Beta test with current students

**Description** : Créer des comptes gratuits (avec abonnement offert ou flag `beta`) pour les élèves actuels en cours particuliers. Embarquer les parents dans le processus pour récolter du feedback structuré (bugs, UX, contenu) et obtenir les premiers témoignages utilisables pour la landing page (#8).

🎯 **Critères d'acceptation**
- 5-10 comptes beta créés et actifs avec des élèves réels (niveaux seconde/première/terminale)
- Chaque beta testeur a complété au moins 3 leçons et 2 quiz
- Un formulaire de feedback structuré est distribué (Google Forms ou équivalent) couvrant : navigation, compréhension des leçons, difficulté des quiz, bugs rencontrés
- Au moins 3 retours écrits exploitables (parents ou élèves) collectés
- Les bugs critiques identifiés sont triés et priorisés dans le backlog

✅ **Definition of Done**
- Comptes beta créés et documentés (emails, niveaux)
- Feedback collecté et synthétisé dans un document récapitulatif
- Bugs critiques enregistrés comme issues
- Au moins 2 témoignages exploitables pour la landing page (#8)

---

### #8 — Social proof on landing page

**Description** : Ajouter une section de témoignages sur la page d'accueil publique (`accueil.html`) pour établir la confiance avec les visiteurs. Les témoignages proviennent des beta testeurs (#7) et sont affichés sous forme de cards avec citation, prénom, niveau et matière préférée. Un badge de confiance "Conçu par un enseignant certifié local" est affiché en bonne place. Les témoignages sont codés en dur dans le template (pas de modèle dédié) pour cette première itération — un modèle `Temoignage` pourra être ajouté ultérieurement si nécessaire.

🎯 **Critères d'acceptation**
- La page d'accueil (`/`) affiche une section "Ce qu'en disent nos élèves" avec 3-5 témoignages
- Chaque témoignage card contient : citation (2-3 phrases), prénom + initiale du nom, niveau (Seconde/Première/Terminale)
- Un badge de confiance "Conçu par un enseignant certifié — Grasse (06)" est visible au-dessus ou en-dessous des témoignages
- La section est responsive (1 colonne mobile, 2-3 colonnes desktop)
- Le dark mode fonctionne via les overrides globaux existants

🏗 **Architecture**
- **Template modifié** : `templates/courses/accueil.html` — nouvelle `<section>` entre le contenu du catalogue et le footer
- **Pas de nouveau modèle** : témoignages codés en dur dans le template (itération 1) avec des `<blockquote>` stylisés en Tailwind
- **Fichiers impactés** : `templates/courses/accueil.html` uniquement

🧪 **Tests**
- `test_accueil_contains_testimonials_section` — GET `/` (anon) → asserter la présence de `id="temoignages"` ou "Ce qu'en disent"
- `test_accueil_contains_trust_badge` — GET `/` → asserter la présence de "enseignant certifié"
- `test_accueil_testimonials_responsive_classes` — asserter la présence de classes Tailwind responsive (`md:grid-cols-2` ou `lg:grid-cols-3`)

🔒 **Sécurité**
- Les témoignages sont du contenu statique dans le template — aucun risque XSS (pas d'input utilisateur)

⚡ **Performance**
- Contenu statique : +0 requête SQL, +0 appel externe
- Impact TTFB : négligeable (quelques KB de HTML en plus)

✅ **Definition of Done**
- La section témoignages est visible sur la page d'accueil publique
- Le badge de confiance est affiché
- Responsive validé (mobile + desktop)
- Dark mode fonctionne sans classes `dark:` dans le template enfant
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (section 5.3 — description `accueil.html`)

---

### #9 — "Hybrid Bac Sprint" upsell

**Description** : Définir et formaliser une offre premium "Sprint Bac" combinant l'accès illimité à l'application et 1h/mois de coaching individuel en visio pour analyser les analytics de l'élève et cibler ses points faibles. Cette offre est un package business (~€89/mois) proposé sur la landing page et dans le modal paywall (#2). Pas de développement logiciel — uniquement la définition du produit et de son intégration tarifaire dans l'offre Stripe.

🎯 **Critères d'acceptation**
- Le pricing est finalisé (tarif mensuel et éventuellement trimestriel)
- Le descriptif produit est rédigé (proposition de valeur, ce qui est inclus, ce qui ne l'est pas)
- Le plan est créé dans le dashboard Stripe (mode test) avec un `price_id` prêt à être intégré
- Le positionnement par rapport aux deux paliers existants (Mensuel/Annuel) est clair

✅ **Definition of Done**
- Document de pricing finalisé
- Produit + Price créés dans Stripe (test mode)
- Le `price_id` est documenté dans `.env.example` (`STRIPE_PRICE_SPRINT`)
- Le descriptif est prêt pour insertion dans le modal paywall

---

### #10 — Local marketing (Grasse & 06)

**Description** : Stratégie d'acquisition locale ciblant les lycées de Grasse et des Alpes-Maritimes. Créer des supports marketing physiques (flyers avec QR code pointant vers une leçon gratuite à haute valeur) et numériques (posts dans les groupes Facebook de parents d'élèves locaux). L'objectif est de générer les premières inscriptions organiques hors du cercle de cours particuliers.

🎯 **Critères d'acceptation**
- Flyer (format A5 ou carte de visite) conçu avec : nom de l'app, QR code vers une leçon gratuite spécifique, proposition de valeur en 1 phrase, mentions légales
- Le QR code pointe vers une URL publique trackable (ex : `/cours/physique/seconde/mouvement/description-mouvement/?utm_source=flyer`)
- 50+ flyers distribués à Tocqueville et Amiral de Grasse
- Au moins 2 posts publiés dans des groupes Facebook parents locaux (06/Grasse)
- Tracking : les paramètres UTM sont reconnus par l'analytics (Google Analytics ou Plausible)

✅ **Definition of Done**
- Flyer finalisé et imprimé
- Distribution effectuée dans au moins 2 établissements
- Posts Facebook publiés
- QR code fonctionnel pointant vers une leçon gratuite pertinente
- Métriques accessibles (inscriptions attribuées à la source `flyer`)

---

### #13 — Query optimization

**Description** : Le dashboard élève (`_dashboard_eleve` dans `users/views.py`) contient un N+1 critique dans la boucle `for matiere in matieres:` qui exécute 3 requêtes par matière (count leçons, count progressions, aggregate scores) — soit ~9 requêtes supplémentaires pour 3 matières. De plus, le calcul du streak fait 2 requêtes séparées (dates progressions + dates connexions). Au total, le dashboard élève effectue environ 18-22 requêtes SQL. L'objectif est de remplacer ces boucles par des annotations bulk (`annotate()`, `Subquery`, `Count` conditionnel) et de vérifier que `matieres_view` n'a pas de N+1 résiduels. Le dashboard élève doit descendre sous les 10 requêtes SQL totales.

🎯 **Critères d'acceptation**
- La boucle per-matière dans `_dashboard_eleve` est remplacée par un queryset annoté unique (1-2 requêtes au lieu de ~9)
- Le calcul du streak est consolidé (fusion `union()` ou single query au lieu de 2 requêtes séparées)
- `matieres_view` : les appels `chapitres_qs.exists()` dans la boucle admin sont éliminés (le prefetch couvre déjà le cas)
- Le dashboard élève s'exécute en ≤10 requêtes SQL totales (mesuré via `assertNumQueries` dans les tests)
- Aucune régression fonctionnelle — les données affichées sont identiques avant/après

🏗 **Architecture**
- **Fichier principal** : `backend/users/views.py` — refactoring de `_dashboard_eleve()`
- **Pattern per-matière** : remplacer la boucle par un queryset annoté :
  ```python
  matieres_stats = (
      Matiere.objects.annotate(
          total_lecons=Count(
              "chapitres__lecons",
              filter=Q(chapitres__niveau=user.niveau),
          ),
          done=Count(
              "chapitres__lecons__progressions",
              filter=Q(
                  chapitres__lecons__progressions__user=user,
                  chapitres__lecons__progressions__statut="termine",
                  chapitres__niveau=user.niveau,
              ),
          ),
          score_moyen=Avg(
              "chapitres__lecons__quiz__resultats__score",
              filter=Q(chapitres__lecons__quiz__resultats__user=user),
          ),
      ).filter(total_lecons__gt=0)
  )
  ```
  → 1 requête SQL au lieu de ~9
- **Streak** : combiner progressions et connexions via `values_list("date", flat=True).union()` pour une seule passe Python, ou fusionner les deux `set()` existants après deux requêtes bulk (déjà fait — optimisation marginale)
- **`matieres_view`** : dans le chemin admin (`is_admin_browse`), supprimer le guard `if chapitres_qs.exists()` — les chapitres sont déjà prefetchés via `prefetch_related("chapitres__lecons")`, donc itérer sans guard n'ajoute aucune requête
- **Fichiers impactés** : `backend/users/views.py` (principal), `backend/courses/views.py` (matieres_view — ajustement mineur)

🧪 **Tests**
- `test_dashboard_eleve_num_queries` — utiliser `django_assert_num_queries` (ou `assertNumQueries`) pour vérifier ≤10 requêtes SQL sur `_dashboard_eleve()`
- `test_dashboard_eleve_data_unchanged_after_optimization` — comparer les valeurs du context dict (`matieres_stats`, `streak`, `score_moyen`, `progression_globale`) via un snapshot ou des assertions directes — s'assurer de l'absence de régression
- `test_matieres_view_num_queries_student` — asserter ≤5 requêtes SQL pour un élève
- `test_matieres_view_num_queries_admin` — asserter ≤8 requêtes SQL pour un admin (browse all niveaux)
- `test_dashboard_eleve_empty_state` — un élève sans aucune progression → pas de division par zéro, streak=0, listes vides sans erreur

🔒 **Sécurité**
- Pas d'impact sécurité direct — refactoring de requêtes internes uniquement
- **OWASP A01** : s'assurer que les annotations filtrent toujours par `user=request.user` pour éviter toute fuite de données entre utilisateurs

⚡ **Performance**
- **Avant** : `_dashboard_eleve` ≈ 18-22 requêtes SQL (3 stats globales + 9 per-matière + 2 streak + 2 trend + 2 revisions + weak areas)
- **Après cible** : ≤10 requêtes SQL totales
- **Indexes existants** : `UserProgression(user, lecon)` UNIQUE + `UserQuizResultat(user, quiz)` UNIQUE — déjà couverts par les `unique_together`, suffisants pour les `Count`/`Avg` annotés
- **Vérification** : exécuter `EXPLAIN ANALYZE` sur la requête annotée Matière pour confirmer l'utilisation des index
- `matieres_view` est déjà bien optimisé avec `prefetch_related("chapitres__lecons")` — gain marginal attendu (élimination de `exists()` dans la boucle admin)

✅ **Definition of Done**
- `_dashboard_eleve` s'exécute en ≤10 requêtes SQL (vérifié par test)
- Les données affichées sont identiques avant/après (aucune régression)
- `matieres_view` : pas de N+1 résiduel dans la boucle admin
- Tests de nombre de requêtes (`assertNumQueries`) en place
- CODEBASE_REFERENCE.md mis à jour (section 3.2 — `_dashboard_eleve` key logic)

---

## Phase 3 — Scaling Traffic (Month 2+)

*Goal: grow organic reach and reduce churn.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 14 | **Snackable social content** | Business | — | ⬜ |
| 15 | ~~**Technical SEO (sitemaps)**~~ | Tech | Sonnet | ✅ |
| 16 | **Parent retention loop** | Business | Sonnet | ⬜ |
| 17 | **Mobile responsiveness audit** | Tech | Sonnet | ⬜ |

---

### #14 — Snackable social content

**Description** : Créer des vidéos courtes (60 secondes) au format TikTok / Instagram Reels résolvant des problèmes classiques d'examen (Bac). Chaque vidéo montre la résolution pas à pas d'un exercice avec un hook accrocheur dans les 3 premières secondes. Le lien vers l'application est dans la bio. L'objectif est de générer du trafic organique vers le catalogue public.

🎯 **Critères d'acceptation**
- 5 vidéos courtes (≤60s) produites, couvrant au moins 2 matières (physique/chimie/maths)
- Chaque vidéo a un hook dans les 3 premières secondes
- Le CTA de fin pointe vers l'application (lien en bio)
- Les vidéos sont publiées sur TikTok et Instagram Reels
- Le profil TikTok/Instagram contient le lien vers la homepage

✅ **Definition of Done**
- 5 vidéos publiées sur TikTok + Instagram
- Profils renseignés avec lien vers l'app
- Premières métriques de vues disponibles (>100 vues cumulées dans la première semaine)

---

### #16 — Parent retention loop

**Description** : Implémenter un email récapitulatif hebdomadaire automatique envoyé aux élèves (et ultérieurement aux parents) résumant l'activité de la semaine : nombre de leçons complétées, quiz passés, score moyen, streak actuel, et un encouragement personnalisé. L'email est généré par une commande management Django (`send_weekly_recap`) planifiée via Heroku Scheduler (chaque lundi 8h UTC). Le contenu est rendu via un template Django HTML+texte et envoyé via le backend email configuré (console en dev, Brevo SMTP en prod). Les élèves sans activité reçoivent un message d'encouragement différencié pour les réengager.

🎯 **Critères d'acceptation**
- La commande `python manage.py send_weekly_recap` envoie un email récapitulatif à chaque élève actif
- L'email contient : prénom de l'élève, nombre de leçons complétées cette semaine, quiz passés, score moyen, streak actuel
- L'email est en français, responsive (HTML), et lisible en texte brut (multipart `EmailMultiAlternatives`)
- Les élèves sans activité dans la semaine reçoivent un email d'encouragement ("Tu n'as pas encore étudié cette semaine — reprends ton élan !")
- L'email n'est pas envoyé aux comptes inactifs (`is_active=False`) ni aux admins

🏗 **Architecture**
- **Nouvelle commande** : `courses/management/commands/send_weekly_recap.py`
  - Queryset : `CustomUser.objects.filter(role='eleve', is_active=True)`
  - Stats agrégées en bulk via `annotate()` : `UserProgression.filter(derniere_activite__gte=lundi_dernier)` + `UserQuizResultat.filter(derniere_tentative__gte=lundi_dernier)`
  - Envoi : `EmailMultiAlternatives` avec template HTML + fallback texte brut
- **Templates email** : `templates/emails/recap_hebdo.html` (HTML responsive) + `templates/emails/recap_hebdo.txt` (texte brut)
- **Scheduling** : Heroku Scheduler addon, commande `python manage.py send_weekly_recap`, fréquence hebdomadaire (lundi 8h UTC)
- **Opt-out** (itération 2) : BooleanField `email_recap` sur `CustomUser` (default=True) — non requis pour l'itération 1 mais le filtre est prévu dans le queryset (`filter(email_recap=True)` si le champ existe)
- **Fichiers impactés** : `courses/management/commands/send_weekly_recap.py` (nouveau), `templates/emails/recap_hebdo.html` (nouveau), `templates/emails/recap_hebdo.txt` (nouveau)

🧪 **Tests**
- `test_weekly_recap_sends_email_to_active_students` — créer 2 élèves actifs + 1 inactif → lancer la commande → asserter `len(mail.outbox) == 2`
- `test_weekly_recap_email_contains_activity_stats` — élève avec 3 leçons terminées cette semaine → asserter que le body contient "3 leçons"
- `test_weekly_recap_inactive_student_gets_encouragement` — élève actif mais 0 activité → asserter que le body contient le message d'encouragement
- `test_weekly_recap_skips_admins` — créer un admin → asserter qu'aucun email ne lui est envoyé
- `test_weekly_recap_html_and_text_parts` — asserter que chaque email a bien un `content_subtype='html'` et une alternative texte brut

🔒 **Sécurité**
- Ne pas inclure de données sensibles dans l'email (pas de mot de passe, pas de token de login automatique)
- Le lien dans l'email pointe vers le dashboard (`{% url 'tableau_de_bord' %}`) avec l'URL absolue du site — pas de lien de connexion automatique
- **OWASP A07 (Identification and Authentication Failures)** : ne pas inclure de "magic link" dans les emails récapitulatifs

⚡ **Performance**
- **Agrégation bulk** : pré-charger toutes les stats en 2-3 requêtes annotées sur le queryset utilisateurs (pas de boucle avec requêtes individuelles) → budget ~3 requêtes SQL totales quel que soit le nombre d'élèves
- L'envoi SMTP (Brevo) est le bottleneck (~200ms/email). Pour N > 100 élèves, utiliser `send_mass_mail()` ou `django.core.mail.get_connection()` avec une seule connexion SMTP réutilisée
- La commande est exécutée hors du chemin critique (scheduler, pas de page web) — pas d'impact sur le TTFB

✅ **Definition of Done**
- La commande `send_weekly_recap` s'exécute sans erreur et envoie les emails
- Les emails sont en français, responsives, et contiennent les stats correctes
- Les comptes inactifs et les admins sont exclus
- Tests passent (avec `django.core.mail.outbox`)
- La commande est documentée dans CODEBASE_REFERENCE.md (section 7 — Management Commands)

---

### #17 — Mobile responsiveness audit

**Description** : La sidebar de navigation et certains composants (formulaires quiz avec équations KaTeX, tableaux dans le contenu Markdown des leçons, modal paywall) ne sont pas optimisés pour les écrans mobiles (<768px). Un audit ciblé est nécessaire pour corriger les problèmes critiques : sidebar en mode hamburger/overlay sur mobile, overflow horizontal des équations mathématiques, formulaires quiz utilisables au pouce, et modal paywall full-screen. L'audit ne touche que le HTML/CSS (Tailwind classes) et le JavaScript Alpine.js pour le toggle sidebar — aucune modification backend.

🎯 **Critères d'acceptation**
- La sidebar est cachée par défaut sur mobile et accessible via un bouton hamburger (toggle Alpine.js)
- Les équations KaTeX ne provoquent pas de scroll horizontal — elles wrappent ou scrollent dans un conteneur dédié (`overflow-x: auto`)
- Les formulaires quiz (radio buttons, champs texte) sont utilisables au pouce (taille de cible ≥ 44px, espacement suffisant)
- Le modal paywall (#2) s'affiche en full-screen sur mobile
- La page de leçon (contenu Markdown) ne déborde pas horizontalement — les tableaux larges sont wrappés dans un `div.overflow-x-auto`
- Validation sur Chrome DevTools (iPhone SE 375px, iPhone 14 390px, Pixel 7 412px) et au moins 1 vrai device

🏗 **Architecture**
- **Template principal** : `templates/base.html` — refactoring de la sidebar :
  - Desktop : sidebar visible par défaut (`hidden md:block`)
  - Mobile : bouton hamburger (`md:hidden`) avec `x-data="{ sidebarOpen: false }"`, sidebar en overlay avec `x-show="sidebarOpen"` + backdrop semi-transparent + `@click.away="sidebarOpen = false"`
- **Templates impactés** :
  - `templates/base.html` — sidebar responsibe + bouton hamburger
  - `templates/courses/lecon.html` — wrapper `overflow-x-auto` autour du contenu Markdown rendu (pour équations et tableaux)
  - `templates/courses/quiz.html` + `quiz_chapitre.html` — padding et taille des radio buttons/labels (`min-h-[44px]`, `py-3`)
  - `templates/components/_paywall_modal.html` — classes responsives (`w-full h-full md:max-w-lg md:h-auto`)
- **KaTeX overflow** : ajouter `.katex-display { overflow-x: auto; max-width: 100%; }` dans les overrides CSS globaux de `base.html` (même `<style>` que les overrides `html.dark {}`)
- **Pas de modification backend** — uniquement HTML/CSS/Alpine.js
- **Pattern hamburger** : SVG inline (3 barres / ✕) — pas de bibliothèque d'icônes externe

🧪 **Tests**
- `test_base_template_contains_hamburger_button` — asserter la présence d'un élément avec `aria-label` contenant "menu" et la classe `md:hidden`
- `test_sidebar_has_responsive_hidden_class` — asserter que la sidebar contient `hidden md:block` ou équivalent
- `test_lecon_template_has_overflow_wrapper` — GET `/cours/lecon/<pk>/` → asserter la présence de `overflow-x-auto` dans le HTML rendu
- `test_quiz_radio_buttons_have_sufficient_padding` — asserter la présence de `min-h-` ou `py-3` sur les labels radio des quiz

🔒 **Sécurité**
- Pas d'impact sécurité — modifications purement CSS/HTML/Alpine.js front-end
- S'assurer que le toggle sidebar ne brise pas le `@login_required` ni n'expose de liens non autorisés

⚡ **Performance**
- Aucune requête SQL ajoutée
- Le JavaScript Alpine.js pour le toggle sidebar est minimal (< 10 lignes) — aucun impact sur le TTI
- Les wrappers `overflow-x-auto` n'ajoutent aucun poids réseau
- Le backdrop overlay utilise une transition CSS (pas de JS animation) — rendu GPU-accéléré

✅ **Definition of Done**
- La sidebar est responsive (hamburger sur mobile, fixe sur desktop)
- Les équations KaTeX ne cassent pas le layout mobile
- Les formulaires quiz sont confortables au pouce (≥44px touch target)
- Le modal paywall est full-screen sur mobile
- Testé sur 3 viewports (iPhone SE 375px, iPhone 14 390px, Pixel 7 412px) via Chrome DevTools
- Tests passent
- Aucune classe `dark:` ajoutée dans les templates enfants
- CODEBASE_REFERENCE.md mis à jour (section 5.1 — `base.html` mention hamburger mobile)

## Phase 4 — Learning Experience Improvements (Month 3+)

*Goal: make learning more engaging, interactive, and effective.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 18 | **Timed quizzes** | Tech | Sonnet | ⬜ |
| 19 | **Instant feedback** | Tech | Sonnet | ⬜ |
| 20 | ~~**Difficulty levels**~~ | Tech | Sonnet | ✅ |
| 21 | ~~**Lesson notes**~~ | Tech | Sonnet | ✅ |
| 22 | **Glossary / formula sheet** | Tech | Sonnet | ⬜ |
| 23 | **Interactive exercises** | Tech | **Opus** | ⬜ |

---

### #18 — Timed quizzes

**Description** : Ajouter un chronomètre optionnel aux quiz de leçon et de chapitre. Un nouveau champ `duree_limite` (en minutes) sur le modèle `Quiz` permet à l'auteur de définir un temps imparti. Quand `duree_limite` est renseigné (> 0), un compte à rebours JavaScript s'affiche en haut du formulaire. À expiration, le formulaire est auto-soumis via HTMX ou un `form.submit()` classique. Les réponses non remplies comptent comme fausses. Le chronomètre est purement côté client — le serveur enregistre l'heure de début dans un champ caché pour permettre une validation anti-triche basique (rejet si le delta dépasse `duree_limite + 30s` de marge).

🎯 **Critères d'acceptation**
- Le modèle `Quiz` possède un champ `duree_limite` (`PositiveIntegerField`, null, blank, default=None) exprimé en minutes
- Quand `duree_limite` est défini, le template quiz affiche un compte à rebours (MM:SS) en position sticky en haut du formulaire
- À expiration du timer, le formulaire est automatiquement soumis
- Le champ caché `quiz_start_time` (timestamp Unix) est inclus dans le formulaire ; le serveur rejette les soumissions dont le delta dépasse `duree_limite * 60 + 30` secondes (HTTP 400 avec message "Temps écoulé")
- Les quiz sans `duree_limite` (null) fonctionnent exactement comme avant (pas de chronomètre)

🏗 **Architecture**
- **Modèle modifié** : `courses/models.py` — `Quiz` reçoit `duree_limite = models.PositiveIntegerField(null=True, blank=True, verbose_name="Durée limite (min)", help_text="Laisser vide pour un quiz sans chronomètre.")`
- **Templates modifiés** :
  - `templates/courses/quiz.html` — bloc conditionnel `{% if quiz.duree_limite %}` : barre sticky avec compte à rebours Alpine.js (`x-data="timerCountdown({{ quiz.duree_limite }})"`) + champ caché `<input type="hidden" name="quiz_start_time" :value="startTime">`
  - `templates/courses/quiz_chapitre.html` — même bloc conditionnel
- **Alpine.js component** (inline dans le template) :
  ```js
  function timerCountdown(minutes) {
    return {
      remaining: minutes * 60,
      startTime: Math.floor(Date.now() / 1000),
      interval: null,
      get display() { return `${Math.floor(this.remaining/60)}:${String(this.remaining%60).padStart(2,'0')}`; },
      init() {
        this.interval = setInterval(() => {
          this.remaining--;
          if (this.remaining <= 0) { clearInterval(this.interval); this.$refs.quizForm.submit(); }
        }, 1000);
      }
    }
  }
  ```
- **Vues modifiées** :
  - `progress/views.py` — `soumettre_quiz` et `soumettre_quiz_chapitre` : si `quiz.duree_limite`, extraire `quiz_start_time` du POST, calculer le delta, rejeter si > `duree_limite * 60 + 30`
- **Admin** : `courses/admin.py` — ajouter `duree_limite` à `QuizAdmin.fields` ou `list_display`
- **Fichiers impactés** : `courses/models.py`, `courses/admin.py`, `templates/courses/quiz.html`, `templates/courses/quiz_chapitre.html`, `progress/views.py`

🧪 **Tests**
- `test_quiz_without_timer_no_countdown_markup` — créer un Quiz sans `duree_limite` → GET `/cours/lecon/<pk>/quiz/` → asserter l'absence de `timerCountdown` dans le HTML
- `test_quiz_with_timer_shows_countdown` — créer un Quiz avec `duree_limite=10` → GET → asserter la présence de `timerCountdown(10)` et de `quiz_start_time` dans le HTML
- `test_submit_quiz_within_time_succeeds` — POST avec `quiz_start_time` = maintenant − 300s, `duree_limite=10` → HTTP 200 (résultat normal)
- `test_submit_quiz_over_time_rejected` — POST avec `quiz_start_time` = maintenant − 700s, `duree_limite=10` → HTTP 400
- `test_submit_quiz_no_timer_ignores_start_time` — Quiz sans `duree_limite` → POST sans `quiz_start_time` → résultat normal

🔒 **Sécurité**
- **OWASP A04 (Insecure Design)** : le chronomètre est côté client uniquement pour l'UX — la validation du temps est faite **côté serveur** via le delta `quiz_start_time`. Un élève qui altère le JS ne pourra pas contourner la limite de temps.
- **Anti-tamper** : `quiz_start_time` est un timestamp envoyé par le client. Un élève pourrait le falsifier pour gagner du temps. Pour l'itération 1, la marge de 30 secondes + le caractère non-certificatif (pas un examen officiel) rendent ce risque acceptable. Itération 2 : stocker le `start_time` côté serveur (session ou cache) pour une validation incontournable.
- **Pas de données sensibles** exposées — le `duree_limite` est public (visible dans le HTML).

⚡ **Performance**
- +0 requête SQL : `duree_limite` est chargé avec le Quiz existant (`select_related` ou accès direct)
- Le `setInterval` JS tourne uniquement sur la page quiz — aucun impact sur les autres pages
- La validation serveur ajoute ~0ms (comparaison de timestamps, pas de requête)
- Budget : +0 requête SQL par page

✅ **Definition of Done**
- Le chronomètre s'affiche pour les quiz avec `duree_limite` et pas pour les autres
- L'auto-submit fonctionne à expiration
- Le serveur rejette les soumissions hors délai
- Les quiz existants (sans `duree_limite`) ne sont pas impactés
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1.7, 3.4, 5.3)

---

### #19 — Instant feedback

**Description** : Ajouter un mode de feedback immédiat aux quiz. Un nouveau champ `feedback_immediat` (`BooleanField`, default=False) sur le modèle `Quiz` permet d'activer ce mode. Quand il est actif, chaque question est évaluée individuellement dès que l'élève soumet sa réponse (via HTMX), et la correction (bonne/mauvaise réponse + explication) s'affiche immédiatement sous la question avant de passer à la suivante. Le quiz se déroule alors question par question (pas de formulaire global), avec un score cumulé affiché en temps réel. À la fin, le résultat global est affiché comme d'habitude. Ce mode est incompatible avec le chronomètre global (#18) — si les deux sont activés, `feedback_immediat` est ignoré et le mode classique (chronomètre) prend le dessus.

🎯 **Critères d'acceptation**
- Le modèle `Quiz` possède un champ `feedback_immediat` (`BooleanField`, default=False)
- Quand `feedback_immediat=True`, le quiz affiche une question à la fois avec un bouton "Valider"
- Au clic sur "Valider", la réponse est évaluée côté serveur via un endpoint HTMX dédié et le résultat (correcte/incorrecte + explication) s'affiche sous la question
- Un bouton "Question suivante" apparaît après validation pour passer à la question suivante
- Le score cumulé (ex. "3/5 correctes") est visible en permanence
- À la dernière question, un bouton "Voir le résultat" soumet le résultat final

🏗 **Architecture**
- **Modèle modifié** : `courses/models.py` — `Quiz` reçoit `feedback_immediat = models.BooleanField(default=False, verbose_name="Feedback immédiat", help_text="Affiche la correction après chaque question au lieu d'attendre la fin.")`
- **Nouvelle vue HTMX** : `progress/views.py` — `evaluer_question_unique(request, question_pk)` :
  - `@require_POST`, `@login_required`
  - Récupère la question, évalue la réponse via `_evaluer_reponses([question], request.POST)`
  - Retourne un partial HTML (`_feedback_question.html`) avec le résultat + explication
  - Stocke la réponse en session (`request.session[f'quiz_{quiz_id}_reponses']`) pour le résultat final
- **Nouvelle vue** : `progress/views.py` — `finaliser_quiz_feedback(request, lecon_pk)` :
  - POST, `@login_required`
  - Récupère les réponses accumulées en session, calcule le score final, enregistre `UserQuizResultat` + Leitner
  - Redirige vers `quiz_resultat.html`
- **Nouvelles URLs** (`progress/urls.py`) :
  - `evaluer_question` : `/progression/question/<int:question_pk>/evaluer/` (POST, HTMX)
  - `finaliser_quiz_feedback` : `/progression/quiz/<int:lecon_pk>/finaliser/` (POST)
- **Nouveau template partial** : `templates/courses/_feedback_question.html` — résultat d'une question (icône ✓/✗, explication, bouton "Question suivante")
- **Template modifié** : `templates/courses/quiz.html` — bloc conditionnel `{% if quiz.feedback_immediat and not quiz.duree_limite %}` :
  - Alpine.js `x-data="{ currentIndex: 0, score: 0, total: {{ questions|length }} }"` pour gérer la navigation question par question
  - Chaque question dans un `<div x-show="currentIndex === {{ forloop.counter0 }}">`
  - Bouton "Valider" → `hx-post="{% url 'evaluer_question' question.pk %}"` → `hx-target="#feedback-{{ question.pk }}"`
  - Après validation, bouton "Suivante" incrémente `currentIndex`
- **Admin** : `courses/admin.py` — ajouter `feedback_immediat` à `QuizAdmin`
- **Fichiers impactés** : `courses/models.py`, `courses/admin.py`, `progress/views.py`, `progress/urls.py`, `templates/courses/quiz.html`, `templates/courses/_feedback_question.html` (nouveau)

🧪 **Tests**
- `test_quiz_classic_mode_no_feedback_markup` — Quiz avec `feedback_immediat=False` → GET quiz page → asserter l'absence de `evaluer_question` dans le HTML
- `test_quiz_feedback_mode_shows_single_question` — Quiz avec `feedback_immediat=True` → GET → asserter `x-show="currentIndex === 0"` dans le HTML
- `test_evaluer_question_returns_correction` — POST `/progression/question/<pk>/evaluer/` avec bonne réponse → asserter HTTP 200, HTML contient "Bonne réponse" ou `✓`
- `test_evaluer_question_wrong_answer` — POST avec mauvaise réponse → asserter HTML contient la bonne réponse + explication
- `test_finaliser_quiz_feedback_saves_resultat` — accumuler des réponses en session puis POST `/progression/quiz/<pk>/finaliser/` → asserter `UserQuizResultat` créé avec le bon score
- `test_feedback_mode_ignored_when_timer_active` — Quiz avec `feedback_immediat=True` ET `duree_limite=10` → GET → asserter le mode classique (formulaire global, chronomètre visible)

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : `evaluer_question_unique` vérifie que `question.quiz.lecon` est accessible à l'utilisateur (niveau compatible, chapitre débloqué) — pas de réponse sur une question hors périmètre
- **OWASP A04 (Insecure Design)** : les réponses sont stockées en session côté serveur (pas en hidden fields côté client) — l'élève ne peut pas modifier ses réponses précédentes
- **IDOR** : vérifier que la question appartient bien à un quiz auquel l'élève a accès
- Rate limiting : `_check_quiz_rate_limit` s'applique à `evaluer_question_unique` (chaque validation compte comme 1 requête)

⚡ **Performance**
- `evaluer_question_unique` fait 1 requête (fetch la question avec `select_related('quiz__lecon__chapitre')`) + évaluation en mémoire → très léger
- Les réponses en session (~100 octets par question) sont négligeables
- Le mode feedback ajoute N requêtes HTMX (1 par question) au lieu de 1 soumission globale, mais chaque requête est très légère (~5ms)
- Budget par question évaluée : +1-2 requêtes SQL

✅ **Definition of Done**
- Le mode feedback affiche une question à la fois et montre la correction immédiatement
- Le score cumulé est visible en temps réel
- Le résultat final est enregistré correctement (identique au mode classique)
- Les quiz classiques (sans `feedback_immediat`) ne sont pas impactés
- Le chronomètre (#18) prend le dessus si les deux options sont activées
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1.7, 2.4, 3.4, 5.2, 5.3)

---

### #20 — ~~Difficulty levels~~ ✅

---

### #21 — ~~Lesson notes~~ ✅

---

### #22 — Glossary / formula sheet

**Description** : Créer une page de référence consultable par matière, regroupant les termes clés, définitions et formules essentielles extraits automatiquement du contenu Markdown des leçons. Un nouveau modèle `EntreeGlossaire` stocke chaque entrée (terme, définition, formule LaTeX optionnelle, leçon source). Une commande management `extraire_glossaire` parse les leçons et génère des entrées candidates. Les enseignants (admins) valident/éditent les entrées via l'admin Django. Côté élève, une page de recherche interactive par matière (avec filtre par chapitre et recherche textuelle Alpine.js côté client) affiche les entrées avec rendu KaTeX pour les formules. Cette page sert de "fiche de révision" rapide consultable pendant les exercices.

🎯 **Critères d'acceptation**
- Le modèle `EntreeGlossaire` stocke : terme, définition, formule LaTeX (optionnel), matière, chapitre (optionnel), leçon source
- La page `/cours/glossaire/<slug:matiere_slug>/` affiche toutes les entrées de la matière, groupées par chapitre
- Un champ de recherche Alpine.js filtre les entrées côté client en temps réel (sur terme + définition)
- Un filtre par chapitre (dropdown ou tabs) permet de restreindre les résultats
- Les formules LaTeX sont rendues via KaTeX (déjà chargé globalement dans `base.html`)
- La commande `python manage.py extraire_glossaire` parse les leçons et génère des entrées candidates (non-validées)

🏗 **Architecture**
- **Nouveau modèle** (`courses/models.py`) :
  ```
  EntreeGlossaire
  ├── matiere          FK → Matiere (on_delete=CASCADE, related_name='glossaire')
  ├── chapitre         FK → Chapitre (on_delete=SET_NULL, null, blank, related_name='glossaire')
  ├── lecon_source     FK → Lecon (on_delete=SET_NULL, null, blank)
  ├── terme            CharField(200)
  ├── definition       TextField
  ├── formule_latex    CharField(500, blank)  — ex: "$F = ma$"
  ├── validee          BooleanField(default=False)
  ├── created_at       DateTimeField(auto_now_add)
  ├── updated_at       DateTimeField(auto_now)
  ```
  `unique_together`: `[matiere, terme]`
  `ordering`: `['terme']`
- **Nouvelle vue** (`courses/views.py`) :
  - `glossaire_view(request, matiere_slug)` — `@login_required` ; filtre `EntreeGlossaire.objects.filter(matiere__slug=matiere_slug, validee=True)` avec `select_related('chapitre')` ; regroupe par chapitre pour le template
- **Nouvelle URL** (`courses/urls.py`) : `glossaire` → `/cours/glossaire/<slug:matiere_slug>/`
- **Nouveau template** : `templates/courses/glossaire.html` — page avec barre de recherche Alpine.js (`x-data="{ search: '', chapitre: 'all' }"`), cards d'entrées filtrables côté client via `x-show="..."`
- **Commande management** : `courses/management/commands/extraire_glossaire.py` — itère sur les leçons, extrait les termes en gras (`**terme**`) et les blocs formule (`$...$`), crée des `EntreeGlossaire(validee=False)` comme candidates
- **Admin** : `courses/admin.py` — `EntreeGlossaireAdmin` avec `list_display`, `list_filter(matiere, validee, chapitre)`, `search_fields(terme, definition)`, action batch "Valider les entrées sélectionnées"
- **Navigation** : ajout d'un lien "📖 Glossaire" dans la sidebar de `base.html` (sous "Révisions"), visible pour les élèves
- **Fichiers impactés** : `courses/models.py`, `courses/admin.py`, `courses/views.py`, `courses/urls.py`, `templates/courses/glossaire.html` (nouveau), `templates/base.html` (sidebar), `courses/management/commands/extraire_glossaire.py` (nouveau)

🧪 **Tests**
- `test_glossaire_page_returns_200` — créer une matière + une `EntreeGlossaire(validee=True)` → GET `/cours/glossaire/physique/` → HTTP 200
- `test_glossaire_excludes_non_validated` — créer une entrée `validee=False` → GET → asserter que le terme n'apparaît pas dans le HTML
- `test_glossaire_groups_by_chapitre` — créer 2 entrées dans 2 chapitres différents → asserter que les deux noms de chapitre apparaissent dans le HTML
- `test_glossaire_search_markup_present` — asserter la présence de `x-data` et du champ de recherche dans le HTML
- `test_extraire_glossaire_creates_candidates` — créer une leçon avec `**Énergie cinétique**` dans le contenu → lancer la commande → asserter `EntreeGlossaire.objects.filter(terme="Énergie cinétique", validee=False).exists()`
- `test_glossaire_requires_login` — GET `/cours/glossaire/physique/` sans login → redirect vers connexion

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : `@login_required` sur la vue glossaire ; les entrées sont filtrées par matière uniquement (pas de données utilisateur sensibles)
- **OWASP A03 (Injection)** : les termes et définitions sont rendus via `{{ entry.definition }}` dans le template Django (auto-escaped) ; les formules LaTeX sont rendues par KaTeX (sandboxé, pas d'exécution JS arbitraire)
- La commande `extraire_glossaire` est read-only sur les leçons et write-only sur le glossaire — pas de risque d'altération du contenu pédagogique

⚡ **Performance**
- La vue glossaire fait 1 requête SQL (`filter + select_related`) — les entrées sont peu nombreuses (~50-200 par matière)
- Le filtrage est entièrement côté client (Alpine.js `x-show`) — 0 requête supplémentaire lors de la recherche
- KaTeX est déjà chargé globalement — pas de téléchargement additionnel
- Index BTree sur `(matiere_id, validee)` pour la requête principale
- Budget : +1 requête SQL par chargement de page

✅ **Definition of Done**
- La page glossaire affiche les entrées validées, groupées par chapitre, avec rendu KaTeX
- La recherche et le filtre par chapitre fonctionnent côté client
- La commande `extraire_glossaire` génère des candidates depuis le Markdown
- L'admin permet la validation des entrées
- Le lien glossaire est visible dans la sidebar
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2.3, 3.3, 5.3, 7)

---

### #23 — Interactive exercises

**Description** : Étendre le système de quiz avec de nouveaux types de questions interactives : glisser-déposer (drag-and-drop), texte à trous (fill-in-the-blank), et association de colonnes (matching). Ces types permettent des exercices plus engageants que le QCM classique, notamment pour les formules de chimie, les unités physiques et les définitions mathématiques. Chaque nouveau type est implémenté comme une extension de `TypeQuestionChoices` et rendu via des composants Alpine.js dédiés dans les templates quiz. L'évaluation côté serveur est étendue dans `_evaluer_reponses()` avec un comparateur par type. La structure de données utilise le `JSONField` existant (`options` et `reponse_correcte`) avec des schémas JSON documentés par type.

🎯 **Critères d'acceptation**
- Trois nouveaux types de questions disponibles : `glisser_deposer`, `texte_a_trous`, `association`
- **Glisser-déposer** : l'élève ordonne ou place des éléments dans des zones cibles (ex. : ordonner les étapes d'une réaction chimique, placer les grandeurs dans la bonne formule)
- **Texte à trous** : un texte avec des blancs `___` que l'élève remplit (ex. : "La formule de l'énergie cinétique est $E_c = \frac{1}{2} \times \_\_\_ \times v^2$")
- **Association** : deux colonnes à relier (ex. : grandeur ↔ unité, terme ↔ définition)
- Chaque type est utilisable dans les quiz de leçon, les quiz de chapitre, et les révisions Leitner
- L'évaluation est faite côté serveur — le JS ne fait que collecter les réponses

🏗 **Architecture**
- **Modèle modifié** : `courses/models.py` — extension de `TypeQuestionChoices` :
  ```python
  GLISSER_DEPOSER = "glisser_deposer", "Glisser-déposer"
  TEXTE_A_TROUS = "texte_a_trous", "Texte à trous"
  ASSOCIATION = "association", "Association de colonnes"
  ```
- **Schémas JSON par type** (stockés dans `options` et `reponse_correcte`) :
  - **Glisser-déposer** :
    - `options`: `{"items": ["H₂O", "NaCl", "CO₂"], "zones": ["Eau", "Sel", "Dioxyde de carbone"]}` — `items` = éléments à placer, `zones` = cibles
    - `reponse_correcte`: `{"Eau": "H₂O", "Sel": "NaCl", "Dioxyde de carbone": "CO₂"}` — mapping zone → item
  - **Texte à trous** :
    - `options`: `{"texte": "L'accélération gravitationnelle est ___ m/s². La formule est F = ___ × g.", "blancs": 2}`
    - `reponse_correcte`: `["9.81", "m"]` — réponses ordonnées par position du blanc
    - `tolerances`: `[["9,81", "9.8"], ["M"]]` — alternatives par blanc (case-insensitive)
  - **Association** :
    - `options`: `{"gauche": ["Force", "Énergie", "Puissance"], "droite": ["Newton", "Joule", "Watt"]}` — colonnes mélangées côté client
    - `reponse_correcte`: `{"Force": "Newton", "Énergie": "Joule", "Puissance": "Watt"}`
- **Vues modifiées** : `progress/views.py` — extension de `_evaluer_reponses()` :
  - `glisser_deposer` : compare le mapping soumis (`POST[f'question_{id}_zone_{zone}']`) au `reponse_correcte` dict — score proportionnel au nombre de placements corrects
  - `texte_a_trous` : compare chaque blanc (`POST[f'question_{id}_blank_{i}']`) à `reponse_correcte[i]` + `tolerances[i]` — case-insensitive via `_comparer_texte_libre()`
  - `association` : compare les paires soumises au `reponse_correcte` dict — score proportionnel
- **Templates** — nouveaux composants Alpine.js inline dans `quiz.html` :
  - **Glisser-déposer** : `x-data="dragDrop({{ question.options|json_script:'' }})"` avec HTML5 Drag & Drop API (`@dragstart`, `@dragover.prevent`, `@drop`) ; les items sont des `<div draggable="true">`, les zones sont des `<div @drop="place($event)">` ; les `<input type="hidden">` sont mis à jour automatiquement
  - **Texte à trous** : le texte est rendu avec des `<input type="text" class="..." name="question_{{ question.pk }}_blank_{{ i }}">` à la place des `___` ; rendu via un template filter custom ou split/join dans le template
  - **Association** : deux colonnes (gauche fixe, droite draggable ou dropdown par ligne) ; `<select name="question_{{ question.pk }}_match_{{ left }}">` pour chaque élément gauche avec les options droite mélangées
- **Template filter** (optionnel) : `courses/templatetags/quiz_filters.py` — `@register.filter def render_blanks(texte, question_pk)` qui remplace `___` par des `<input>` numérotés
- **Admin** : `courses/admin.py` — le schéma JSON est documenté dans les `help_text` de `Question.options` et `Question.reponse_correcte`
- **Import CSV** : `import_questions.py` — extension pour supporter les nouveaux types (même structure du CSV, `options` et `reponse_correcte` sont déjà des JSONFields)
- **Fichiers impactés** : `courses/models.py`, `progress/views.py`, `templates/courses/quiz.html`, `templates/courses/quiz_chapitre.html`, `templates/courses/revisions.html`, `courses/templatetags/quiz_filters.py` (nouveau), `courses/management/commands/import_questions.py`

🧪 **Tests**
- `test_drag_drop_correct_placement_full_score` — créer une question `glisser_deposer` → POST avec le mapping correct → asserter score = 100%
- `test_drag_drop_partial_placement` — POST avec 2/3 placements corrects → asserter score proportionnel
- `test_fill_blank_correct_answers` — créer une question `texte_a_trous` → POST avec réponses correctes → asserter 100%
- `test_fill_blank_with_tolerances` — POST avec une tolérance acceptée (ex. "9,81" au lieu de "9.81") → asserter correct
- `test_fill_blank_case_insensitive` — POST en majuscules → asserter correct (case-insensitive)
- `test_association_correct_pairs` — créer une question `association` → POST avec les bonnes paires → 100%
- `test_association_partial_correct` — POST avec 2/3 paires correctes → score proportionnel
- `test_new_types_work_in_chapter_quiz` — créer des questions des 3 nouveaux types dans un chapitre → soumettre le quiz chapitre → asserter `UserChapitreQuizResultat` créé
- `test_new_types_work_in_revisions` — questions des nouveaux types dans le système Leitner → soumettre révisions → asserter `UserQuestionHistorique` mis à jour
- `test_import_csv_new_types` — CSV avec `type=glisser_deposer` et JSON `options`/`reponse_correcte` → asserter import réussi

🔒 **Sécurité**
- **OWASP A03 (Injection)** : les `options` et `reponse_correcte` JSON sont rendus via `{{ question.options|json_script:"" }}` (auto-escaped par Django `json_script`) — jamais via `{{ question.options|safe }}` qui permettrait l'injection XSS
- **OWASP A04 (Insecure Design)** : l'évaluation est entièrement côté serveur dans `_evaluer_reponses()` — le JS côté client collecte uniquement les réponses dans des `<input>` soumis via POST, pas d'évaluation côté client
- **OWASP A08 (Software and Data Integrity)** : les schémas JSON sont validés à l'import CSV (`import_questions`) et dans l'admin — des `options` malformées sont rejetées
- Pour les questions `association`, la colonne droite est mélangée côté serveur (pas côté client) pour éviter que l'ordre du HTML ne trahisse les bonnes réponses

⚡ **Performance**
- Les nouveaux types n'ajoutent **aucune requête SQL** : les `options` et `reponse_correcte` sont déjà chargés avec la question (JSONField)
- L'évaluation côté serveur (comparaisons de dicts/listes) est O(n) avec n < 20 items — négligeable
- Le drag-and-drop HTML5 natif n'ajoute aucune dépendance JS externe
- Les composants Alpine.js restent inline (< 50 lignes chacun) — aucun bundle JS supplémentaire
- Budget : +0 requête SQL par page

✅ **Definition of Done**
- Les 3 nouveaux types de questions fonctionnent dans les quiz de leçon, de chapitre, et les révisions
- L'évaluation côté serveur est correcte (score proportionnel, tolérances, case-insensitive)
- L'import CSV supporte les nouveaux types
- Le drag-and-drop fonctionne sur desktop et mobile (touch events)
- Les composants Alpine.js sont accessibles (labels, aria-attributes)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1.8, 1.9, 3.4, 5.3, 7)

## Phase 5 — Social & Gamification (Month 4+)

*Goal: increase engagement, retention, and social motivation through game mechanics and communication loops.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 24 | **Badges / achievements** | Tech | Sonnet | ⬜ |
| 25 | **Leaderboard** | Tech | Sonnet | ⬜ |
| 26 | **Teacher notifications** | Tech | Sonnet | ⬜ |

---

### #24 — Badges / achievements

**Description** : Implémenter un système de badges pour récompenser les accomplissements clés des élèves : premier quiz réussi, streak de 10 jours consécutifs, score parfait sur un quiz de chapitre, complétion de toutes les leçons d'une matière, etc. Le système repose sur deux modèles : `Badge` (catalogue des badges disponibles avec nom, description, icône et condition de déclenchement) et `UserBadge` (relation M2M horodatée entre un utilisateur et ses badges obtenus). L'attribution est déclenchée par des fonctions helper appelées depuis les vues existantes (`soumettre_quiz`, `soumettre_quiz_chapitre`, `_dashboard_eleve`) — pas de Django signals pour rester explicite et testable. Les badges sont affichés sur le dashboard élève (section dédiée) et sur une page profil publique optionnelle.

🎯 **Critères d'acceptation**
- Le modèle `Badge` stocke : `code` (unique slug), `nom`, `description`, `icone` (emoji ou SVG inline), `categorie` (quiz, streak, progression, chapitre)
- Le modèle `UserBadge` stocke : `user` FK, `badge` FK, `obtenu_le` datetime
- Au moins 8 badges initiaux sont seeded :
  - `premier_quiz` — "Premier quiz réussi"
  - `streak_10` — "10 jours de connexion consécutifs"
  - `score_parfait_lecon` — "100% sur un quiz de leçon"
  - `score_parfait_chapitre` — "100% sur un quiz de chapitre"
  - `chapitre_complete` — "Toutes les leçons d'un chapitre terminées"
  - `matiere_complete` — "Toutes les leçons d'une matière terminées"
  - `revisions_assidu` — "50 questions révisées via Leitner"
  - `explorateur` — "Leçons consultées dans les 3 matières"
- Les badges sont attribués automatiquement au moment pertinent (pas de vérification batch différée)
- Le dashboard élève affiche les badges obtenus avec un effet visuel (icône dorée vs grisée)
- Un badge ne peut être attribué qu'une seule fois par utilisateur (`unique_together`)

🏗 **Architecture**
- **Nouveaux modèles** (`progress/models.py`) :
  ```
  Badge
  ├── code             SlugField(50), unique
  ├── nom              CharField(100)
  ├── description      CharField(255)
  ├── icone            CharField(50)     — emoji ("🏆") ou nom d'icône SVG
  ├── categorie        CharField(30)     — choices: quiz, streak, progression, chapitre
  ├── created_at       DateTimeField(auto_now_add)

  UserBadge
  ├── user             FK → CustomUser (on_delete=CASCADE, related_name='badges_obtenus')
  ├── badge            FK → Badge (on_delete=CASCADE, related_name='attributions')
  ├── obtenu_le        DateTimeField(auto_now_add)
  unique_together: [user, badge]
  ```
- **Helper** (`progress/views.py`) :
  - `_verifier_et_attribuer_badges(user, contexte)` — fonction centrale appelée après les événements clés. `contexte` est un dict indiquant ce qui vient de se passer (`{"quiz_score": 100, "quiz_type": "lecon"}`, `{"streak": 10}`, etc.). La fonction vérifie les conditions de chaque badge et crée les `UserBadge` manquants via `get_or_create`.
  - Appelée depuis : `soumettre_quiz` (badges quiz), `soumettre_quiz_chapitre` (badges chapitre), `_dashboard_eleve` (badges streak/progression — recalcul léger)
- **Seed** : `courses/management/commands/seed_badges.py` — crée les 8 badges initiaux (idempotent via `update_or_create` sur `code`)
- **Templates modifiés** :
  - `templates/dashboard/eleve.html` — nouvelle section "🏆 Mes badges" avec grille d'icônes ; badges non obtenus affichés en grisé avec `opacity-40`
  - `templates/users/profil.html` (optionnel) — section badges publique
- **Admin** : `progress/admin.py` — `BadgeAdmin` avec `list_display(code, nom, categorie)` + `UserBadgeAdmin` avec `list_display(user, badge, obtenu_le)`, `list_filter(badge)`
- **Fichiers impactés** : `progress/models.py`, `progress/views.py`, `progress/admin.py`, `templates/dashboard/eleve.html`, `courses/management/commands/seed_badges.py` (nouveau)

🧪 **Tests**
- `test_premier_quiz_badge_attributed_on_first_quiz_pass` — élève passe son premier quiz (score ≥ score_minimum) → asserter `UserBadge.objects.filter(user=user, badge__code='premier_quiz').exists()`
- `test_badge_not_duplicated_on_second_quiz` — élève passe un 2e quiz → asserter `UserBadge.objects.filter(user=user, badge__code='premier_quiz').count() == 1`
- `test_score_parfait_badge_on_100_percent` — score = 100% sur un quiz de leçon → asserter `score_parfait_lecon` attribué
- `test_score_parfait_not_attributed_on_99_percent` — score = 99% → asserter badge PAS attribué
- `test_streak_10_badge_on_consecutive_days` — simuler 10 jours de connexion consécutifs → asserter `streak_10` attribué
- `test_dashboard_displays_obtained_badges` — élève avec 2 badges → GET dashboard → asserter que les 2 icônes de badge apparaissent dans le HTML (pas en grisé)
- `test_dashboard_displays_locked_badges_greyed` — élève avec 0 badges → GET dashboard → asserter la présence de badges avec `opacity` dans le HTML

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : `UserBadge` est filtré par `user=request.user` dans toutes les vues — un élève ne voit que ses propres badges. La page profil publique (si implémentée) n'affiche que le prénom + badges, jamais l'email ou le niveau.
- **OWASP A04 (Insecure Design)** : l'attribution est côté serveur uniquement via `_verifier_et_attribuer_badges()` — aucun endpoint ne permet à un utilisateur de s'auto-attribuer un badge.
- Les badges sont créés via seed command (admin only) — pas d'endpoint de création côté utilisateur.
- Le `unique_together` sur `UserBadge` empêche les insertions dupliquées même en cas de race condition (contrainte DB).

⚡ **Performance**
- `_verifier_et_attribuer_badges()` fait 1 requête pour charger les badges déjà obtenus (`UserBadge.filter(user=user).values_list('badge__code', flat=True)`) puis 0-N `get_or_create` pour les nouveaux (typiquement 0 en régime normal, 1 quand un badge est déclenché). Budget : +1-2 requêtes SQL par appel.
- L'appel est conditionnel : dans `soumettre_quiz`, on ne vérifie les badges que si le quiz est réussi (`passe=True`). Dans `_dashboard_eleve`, la vérification streak est faite 1x par session (guard via `request.session.get('badges_verified_today')`).
- Le seed est idempotent : 8 `update_or_create` = 8 requêtes, exécuté uniquement au déploiement.
- L'affichage dashboard ajoute +1 requête (`UserBadge.filter(user=user).select_related('badge')`) — déjà incluse dans le budget ≤10 cible de #13.

✅ **Definition of Done**
- Les 8 badges initiaux sont seeded et visibles dans l'admin
- Les badges sont attribués automatiquement au moment pertinent
- Le dashboard affiche les badges obtenus et les badges verrouillés (grisés)
- Un badge n'est jamais attribué en double
- Les badges ne sont pas écrits en mode preview (`request.session["preview_niveau"]`)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2.4, 3.4, 5.2, 7)

---

### #25 — Leaderboard

**Description** : Ajouter un classement par niveau (seconde/première/terminale) qui classe les élèves selon un score agrégé basé sur leurs quiz réussis, leur streak, et leurs badges obtenus. Le classement est opt-in : un nouveau champ `afficher_classement` (BooleanField) sur `CustomUser` permet à chaque élève de choisir de participer ou non. Les élèves qui ne participent pas n'apparaissent pas dans le classement et ne voient pas les noms des autres (uniquement les scores anonymisés). Le classement est recalculé de manière paresseuse (à chaque chargement de la page) via un queryset annoté — pas de table matérialisée pour l'itération 1. Un reset hebdomadaire optionnel (commande management) remet les scores à zéro chaque lundi pour stimuler la compétition récurrente.

🎯 **Critères d'acceptation**
- La page `/cours/classement/<str:niveau>/` affiche le top 20 des élèves pour le niveau donné
- Chaque ligne contient : rang, prénom + initiale du nom (ou "Anonyme" si opt-out), score agrégé
- Le score agrégé = somme pondérée : `(nb_quiz_reussis × 10) + (streak_actuel × 2) + (nb_badges × 5)`
- L'élève connecté voit sa propre ligne mise en surbrillance (même s'il n'est pas dans le top 20)
- Un toggle dans les paramètres utilisateur (`/profil/`) permet d'activer/désactiver `afficher_classement`
- Les élèves avec `afficher_classement=False` ne sont PAS inclus dans le queryset du classement
- Les admins en mode preview ne voient pas de classement (ou un classement vide)

🏗 **Architecture**
- **Modèle modifié** : `users/models.py` — `CustomUser` reçoit `afficher_classement = models.BooleanField(default=False, verbose_name="Participer au classement")`
- **Nouvelle vue** (`courses/views.py`) :
  - `classement_view(request, niveau)` — `@login_required`
  - Queryset :
    ```python
    classement = (
        CustomUser.objects.filter(
            role='eleve', niveau=niveau, is_active=True, afficher_classement=True
        ).annotate(
            nb_quiz_reussis=Count('quiz_resultats', filter=Q(quiz_resultats__passe=True)),
            nb_badges=Count('badges_obtenus'),
            score=ExpressionWrapper(
                F('nb_quiz_reussis') * 10 + F('nb_badges') * 5,
                output_field=IntegerField()
            ),
        ).order_by('-score')[:20]
    )
    ```
    (Le streak n'est pas stocké en DB — calculé séparément pour l'utilisateur courant uniquement, inclus dans son row)
  - Context : `classement`, `user_rank` (position de l'utilisateur courant dans le classement complet), `user_score`
- **Nouvelle URL** (`courses/urls.py`) : `classement` → `/cours/classement/<str:niveau>/`
- **Nouveau template** : `templates/courses/classement.html` — tableau avec rangs, avatars (initiales), scores ; ligne de l'utilisateur courant en surbrillance (couleur matière ou jaune)
- **Formulaire modifié** : `users/forms.py` — ajouter `afficher_classement` au formulaire de profil (checkbox)
- **Commande management** (optionnelle) : `courses/management/commands/reset_classement.py` — remet les scores hebdomadaires à zéro (si une table `ClassementHebdo` est ajoutée ultérieurement — hors scope itération 1)
- **Navigation** : lien "🏅 Classement" dans la sidebar de `base.html` (visible pour les élèves)
- **Fichiers impactés** : `users/models.py`, `users/forms.py`, `courses/views.py`, `courses/urls.py`, `templates/courses/classement.html` (nouveau), `templates/base.html` (sidebar)

🧪 **Tests**
- `test_classement_returns_200_for_student` — élève de niveau seconde → GET `/cours/classement/seconde/` → HTTP 200
- `test_classement_excludes_opt_out_students` — créer 2 élèves, 1 avec `afficher_classement=False` → GET → asserter que seul l'élève opt-in apparaît dans le context `classement`
- `test_classement_ordered_by_score_descending` — 3 élèves avec des scores différents → asserter l'ordre décroissant dans le context
- `test_classement_shows_current_user_highlighted` — GET → asserter la présence de la classe CSS de surbrillance pour l'utilisateur courant dans le HTML
- `test_classement_filters_by_niveau` — élèves de niveaux différents → GET `/cours/classement/seconde/` → asserter que seuls les élèves `niveau=seconde` apparaissent
- `test_classement_requires_login` — GET sans login → redirect vers connexion
- `test_classement_preview_mode_empty` — admin en mode preview → GET → asserter classement vide ou message informatif

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : le classement n'affiche que le prénom + initiale du nom de famille (jamais l'email, le nom complet, ni le niveau de détail de progression). Les élèves opt-out sont totalement exclus du queryset — leur existence n'est pas déductible.
- **OWASP A04 (Insecure Design)** : le score est calculé côté serveur via `annotate()` — aucun moyen pour un utilisateur de gonfler son score artificiellement sans réellement passer des quiz. Le rate limiting existant sur les quiz empêche le farming.
- **Vérification de niveau** : un élève `seconde` ne peut consulter que le classement `seconde` (ou tous les niveaux en tant que visiteur ? — restreindre à son propre niveau pour éviter la comparaison inter-niveaux non pertinente).
- **Privacy** : le BooleanField `afficher_classement` respecte le RGPD — consentement explicite nécessaire (default=False = opt-in).

⚡ **Performance**
- Le queryset annoté fait 1 requête SQL complexe avec `COUNT` + `ExpressionWrapper` — PostgreSQL l'optimise via les index existants sur `UserQuizResultat(user, quiz)` UNIQUE et `UserBadge(user, badge)` UNIQUE.
- Le LIMIT 20 (`.[:20]`) évite de charger tous les étudiants.
- Le calcul du rang de l'utilisateur courant nécessite 1 requête supplémentaire (`COUNT(*) WHERE score > user_score`).
- Budget : +2 requêtes SQL par chargement de page.
- Pour un volume > 1000 élèves par niveau : envisager un cache (60s TTL) sur le classement via `cache.get_or_set('classement_{niveau}', queryset, 60)`.

✅ **Definition of Done**
- La page classement affiche le top 20 avec scores et rangs
- L'utilisateur courant est mis en surbrillance
- Les élèves opt-out ne sont pas visibles
- Le toggle `afficher_classement` fonctionne dans le profil
- Le classement respecte le dark mode (overrides globaux)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1.1, 2.3, 3.3, 4, 5.3)

---

### #26 — Teacher notifications

**Description** : Implémenter un système de notifications à destination de l'admin/enseignant quand un élève est en difficulté, définie par 3+ tentatives échouées sur un quiz de chapitre sans jamais atteindre le score minimum. La notification est envoyée par email (et optionnellement affichée dans un panneau in-app sur le dashboard admin). Le système utilise une table `Notification` pour éviter les doublons (on ne notifie qu'une fois par couple élève-chapitre tant que l'élève n'a pas réussi). La vérification est déclenchée dans `soumettre_quiz_chapitre` après chaque tentative échouée. L'email est envoyé via le backend email configuré (console en dev, Brevo SMTP en prod).

🎯 **Critères d'acceptation**
- Quand un élève échoue 3 fois ou plus au quiz d'un même chapitre sans jamais réussir, une notification est envoyée à tous les admins actifs
- L'email contient : prénom de l'élève, nom du chapitre, matière, niveau, nombre de tentatives, meilleur score atteint
- La notification n'est envoyée qu'une seule fois par couple (élève, chapitre) tant que l'élève ne réussit pas le quiz
- Si l'élève réussit finalement, la notification est marquée comme résolue (`resolue=True`)
- Le dashboard admin affiche un panneau "⚠️ Élèves en difficulté" avec la liste des notifications non résolues
- Les notifications résolues disparaissent du panneau (mais restent en base pour l'historique)

🏗 **Architecture**
- **Nouveau modèle** (`progress/models.py`) :
  ```
  Notification
  ├── user             FK → CustomUser (on_delete=CASCADE, related_name='notifications_difficulte')
  ├── chapitre         FK → Chapitre (on_delete=CASCADE, related_name='notifications')
  ├── type             CharField(30)      — choices: difficulte_chapitre (extensible)
  ├── nb_tentatives    PositiveIntegerField
  ├── meilleur_score   FloatField
  ├── resolue          BooleanField(default=False)
  ├── envoyee          BooleanField(default=False)
  ├── created_at       DateTimeField(auto_now_add)
  ├── updated_at       DateTimeField(auto_now)
  unique_together: [user, chapitre, type]
  ```
- **Helper** (`progress/views.py`) :
  - `_verifier_difficulte_eleve(user, chapitre)` — appelée dans `soumettre_quiz_chapitre` quand `passe=False` :
    1. Vérifie `UserChapitreQuizResultat.nb_tentatives >= 3` et `passe=False`
    2. `Notification.objects.get_or_create(user=user, chapitre=chapitre, type='difficulte_chapitre', defaults={...})`
    3. Si la notification est nouvelle (`created=True`) ou n'a pas encore été envoyée (`envoyee=False`), envoie l'email
    4. Met à jour `nb_tentatives` et `meilleur_score` sur la notification existante
  - `_resoudre_notification(user, chapitre)` — appelée dans `soumettre_quiz_chapitre` quand `passe=True` : met `resolue=True` sur la notification existante (si elle existe)
- **Email** : `EmailMultiAlternatives` avec template `templates/emails/notification_difficulte.html` + `.txt`
  - Destinataires : `CustomUser.objects.filter(role='admin', is_active=True).values_list('email', flat=True)`
- **Vue modifiée** : `users/views.py` — `_dashboard_admin` charge les notifications non résolues :
  ```python
  notifications_difficulte = (
      Notification.objects.filter(resolue=False, type='difficulte_chapitre')
      .select_related('user', 'chapitre__matiere')
      .order_by('-created_at')[:20]
  )
  ```
- **Template modifié** : `templates/dashboard/admin.html` — nouvelle section "⚠️ Élèves en difficulté" avec liste des notifications (prénom élève, chapitre, tentatives, score)
- **Admin** : `progress/admin.py` — `NotificationAdmin` avec `list_display(user, chapitre, type, nb_tentatives, resolue)`, `list_filter(resolue, type)`
- **Fichiers impactés** : `progress/models.py`, `progress/views.py`, `progress/admin.py`, `users/views.py`, `templates/dashboard/admin.html`, `templates/emails/notification_difficulte.html` (nouveau), `templates/emails/notification_difficulte.txt` (nouveau)

🧪 **Tests**
- `test_notification_created_after_3_failed_attempts` — élève échoue 3 fois au quiz chapitre → asserter `Notification.objects.filter(user=user, chapitre=chapitre, resolue=False).exists()`
- `test_notification_not_created_before_3_attempts` — élève échoue 2 fois → asserter `Notification.objects.filter(user=user, chapitre=chapitre).count() == 0`
- `test_notification_email_sent_to_admins` — 3e échec → asserter `len(mail.outbox) == 1` et que le destinataire est l'admin
- `test_notification_not_duplicated_on_4th_attempt` — 4e échec → asserter toujours 1 seule notification en base, `len(mail.outbox)` n'augmente pas
- `test_notification_resolved_on_success` — élève réussit après 3+ échecs → asserter `Notification.objects.get(...).resolue == True`
- `test_admin_dashboard_shows_unresolved_notifications` — créer une notification non résolue → GET dashboard admin → asserter la présence du prénom de l'élève et du nom du chapitre dans le HTML
- `test_notification_skipped_in_preview_mode` — admin en mode preview échoue un quiz chapitre → asserter aucune notification créée

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : le panneau "Élèves en difficulté" n'est visible que sur le dashboard admin — `_dashboard_admin` est protégé par le check `user.is_admin`. Les élèves ne voient jamais les notifications des autres.
- **OWASP A07 (Identification Failures)** : l'email de notification ne contient pas de lien de connexion automatique — l'admin doit se connecter manuellement pour voir les détails.
- **Privacy / RGPD** : les notifications contiennent des données scolaires (tentatives, scores) d'un élève. L'accès est restreint aux admins (enseignants) qui ont une relation pédagogique légitime. Pas de partage avec des tiers.
- **Anti-spam** : l'email n'est envoyé qu'une seule fois par (élève, chapitre) via le guard `envoyee=False` — pas de flood même si l'élève fait 50 tentatives.
- Le `unique_together` sur `Notification` empêche les doublons en base même en cas de requêtes concurrentes.

⚡ **Performance**
- `_verifier_difficulte_eleve` fait 1 `get_or_create` (1 requête SQL) + 1 `send_mail` (asynchrone côté SMTP, ~200ms bloquant). L'email est le bottleneck — acceptable car il ne se produit qu'une seule fois par (élève, chapitre).
- Le dashboard admin : 1 requête SQL pour les notifications non résolues (LIMIT 20 + `select_related`).
- Index recommandé : `(resolue, type)` sur `Notification` pour le filtre du dashboard admin.
- Budget : +1 requête SQL dans `soumettre_quiz_chapitre` (uniquement quand `passe=False`), +1 requête SQL sur le dashboard admin.

✅ **Definition of Done**
- La notification est créée et l'email envoyé après 3+ échecs non suivis de réussite
- L'email est envoyé une seule fois par (élève, chapitre)
- La notification est résolue quand l'élève réussit
- Le dashboard admin affiche les notifications non résolues
- Le mode preview ne déclenche pas de notifications
- Tests passent (avec `django.core.mail.outbox`)
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2.4, 3.2, 3.4, 5.2)

---

## Phase 6 — Architecture & Housekeeping (Month 5+)

*Goal: improve code quality, developer experience, and accessibility.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 27 | ~~**Completed**~~ | Tech | — | ✅ |
| 28 | ~~**Completed**~~ | Tech | — | ✅ |
| 29 | ~~**Completed**~~ | Tech | — | ✅ |
| 30 | ~~**Completed**~~ | Tech | — | ✅ |
| 31 | ~~**Completed**~~ | Tech | — | ✅ |
| 32 | **Accessibility (a11y)** | Tech | Sonnet | ⬜ |
| 33 | ~~**Completed**~~ | Tech | — | ✅ |
| 34 | ~~**Completed**~~ | Tech | — | ✅ |

---

### #32 — Accessibility (a11y)

**Description** : Le site présente plusieurs lacunes d'accessibilité qui nuisent à l'expérience des utilisateurs en situation de handicap et impactent le score Lighthouse Accessibility. Les problèmes identifiés couvrent quatre axes : (1) **aria-labels manquants** — les icônes interactives (sidebar, dark mode toggle, hamburger menu) et les boutons sans texte n'ont pas de label accessible ; (2) **focus management après HTMX swaps** — quand un partiel est injecté via HTMX (résultat quiz, sauvegarde note), le focus n'est pas déplacé vers le nouveau contenu, forçant les utilisateurs clavier/lecteur d'écran à naviguer depuis le début ; (3) **quiz radio buttons** — les groupes de réponses ne sont pas encapsulés dans des `<fieldset>/<legend>`, les radios n'ont pas de `role` explicite, et le lien sémantique question↔réponses est absent ; (4) **contraste des couleurs** — certaines combinaisons (texte sur fond matière, placeholders, badges grisés) ne respectent pas le ratio WCAG 2.1 AA minimum de 4.5:1.

🎯 **Critères d'acceptation**
- Tous les éléments interactifs sans texte visible ont un `aria-label` descriptif en français
- Les boutons d'icônes (dark mode toggle, hamburger, close modals) ont un `aria-label` et un `role="button"` si pas déjà des `<button>`
- Après chaque swap HTMX, le focus est déplacé vers le contenu injecté via `htmx:afterSwap` event listener + `element.focus()` (ou `tabindex="-1"` + `focus()` sur le conteneur)
- Les groupes de réponses quiz (QCM, vrai/faux) sont encapsulés dans `<fieldset>` avec `<legend>` reprenant le texte de la question
- Chaque radio/checkbox a un `<label for="">` explicite lié par `id`
- Le ratio de contraste est ≥ 4.5:1 pour tout texte normal et ≥ 3:1 pour les textes larges (≥18px bold), vérifié avec axe DevTools ou Lighthouse
- Le score Lighthouse Accessibility est ≥ 90 sur les pages : accueil, leçon, quiz, dashboard

🏗 **Architecture**
- **Template principal** (`templates/base.html`) :
  - Ajouter `aria-label="Basculer le thème sombre"` sur le bouton dark mode (header + floating)
  - Ajouter `aria-label="Ouvrir le menu de navigation"` / `aria-label="Fermer le menu"` sur le hamburger
  - Ajouter `aria-label` sur les liens de la sidebar qui n'ont que des icônes
  - Événement HTMX global : `<script>document.body.addEventListener('htmx:afterSwap', function(e) { e.detail.target.setAttribute('tabindex', '-1'); e.detail.target.focus(); });</script>`
- **Templates quiz** (`templates/courses/quiz.html`, `quiz_chapitre.html`, `revisions.html`) :
  - Wrapping : `<fieldset><legend class="sr-only">{{ question.texte }}</legend>...radios...</fieldset>` pour chaque question
  - Chaque `<input type="radio" id="q{{ question.pk }}_opt{{ forloop.counter0 }}">` avec `<label for="q{{ question.pk }}_opt{{ forloop.counter0 }}">`
  - Même pattern pour vrai/faux et texte libre (`<label for="">`)
- **Templates leçon** (`templates/courses/lecon.html`) :
  - `aria-label` sur le panneau notes et ses contrôles
  - `role="tabpanel"` si des tabs sont présents (leçon / notes)
- **Contraste couleurs** — ajustements CSS dans `base.html` :
  - Texte placeholder : passer de `text-gray-400` à `text-gray-500` (contrast ratio 4.6:1 sur fond blanc)
  - Badges grisés (#24) : utiliser `opacity-50` au lieu de `opacity-40` pour maintenir le contraste
  - Vérifier les couleurs matière (blue-600, emerald-600, purple-600) sur fond blanc — déjà AA compliant
  - En dark mode : vérifier les couleurs de texte sur fond `gray-800`/`gray-900`
- **Classe utilitaire** : `.sr-only` (screen-reader only) — déjà disponible via Tailwind CDN (`sr-only` class)
- **Fichiers impactés** : `templates/base.html`, `templates/courses/quiz.html`, `templates/courses/quiz_chapitre.html`, `templates/courses/revisions.html`, `templates/courses/lecon.html`, `templates/courses/lecon_publique.html`

🧪 **Tests**
- `test_dark_mode_toggle_has_aria_label` — GET any authenticated page → asserter la présence de `aria-label` contenant "thème" ou "theme" sur le bouton toggle
- `test_hamburger_button_has_aria_label` — GET any page → asserter la présence de `aria-label` contenant "menu" sur le bouton hamburger
- `test_quiz_questions_wrapped_in_fieldset` — GET `/cours/lecon/<pk>/quiz/` → asserter la présence de `<fieldset>` et `<legend>` dans le HTML
- `test_quiz_radio_buttons_have_labels` — asserter que chaque `<input type="radio">` a un attribut `id` et qu'un `<label for="...">` correspondant existe
- `test_htmx_afterswap_focus_script_present` — GET any authenticated page → asserter la présence de `htmx:afterSwap` dans le HTML inline script
- `test_lighthouse_accessibility_score` (manual/CI — via `lighthouse-ci`) — score ≥ 90 sur accueil, leçon, quiz, dashboard

🔒 **Sécurité**
- Pas d'impact sécurité direct — modifications purement HTML/CSS/accessibilité.
- Les `aria-label` et `<label>` n'exposent aucune donnée sensible.
- Le `tabindex="-1"` + `focus()` après HTMX swap ne contourne aucun mécanisme de sécurité — il ne rend accessible que le contenu déjà visible à l'écran.

⚡ **Performance**
- Zéro requête SQL ajoutée — modifications purement front-end (HTML attributs + 1 event listener JS).
- L'event listener `htmx:afterSwap` est un seul listener délégué sur `document.body` — aucun impact mesurable sur le TTI.
- Les `<fieldset>/<legend>` ajoutent ~200 octets par page quiz — négligeable.
- Le remplacement de `opacity-40` par `opacity-50` n'a aucun coût de rendu.
- Budget : +0 requête SQL, +0ms TTFB.

✅ **Definition of Done**
- Tous les boutons d'icônes ont un `aria-label` descriptif
- Le focus est déplacé vers le contenu injecté après chaque HTMX swap
- Les quiz utilisent `<fieldset>/<legend>` et tous les radios ont des `<label for="">`
- Le ratio de contraste est ≥ 4.5:1 sur tout le texte (vérifié avec axe DevTools)
- Lighthouse Accessibility ≥ 90 sur les 4 pages clés
- Aucune classe `dark:` ajoutée dans les templates enfants
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 5.1, 5.3, 8)

---

## Phase 7 — Tutorat, Calendrier & Facturation SAP (Month 6+)

*Goal: enable paid tutoring sessions with a full booking→payment→calendar→invoice pipeline.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 35 | **Système de Réservation** | Feature | Opus | ⬜ |
| 36 | **Stripe Pre-auth & Capture** | Feature | Opus | ⬜ |
| 37 | **Sync Calendrier** | Feature | Sonnet | ⬜ |
| 38 | **Facturation SAP** | Feature | Sonnet | ⬜ |

---

### #35 — Système de Réservation

**Description** : Créer une app `tutoring/` dédiée au tutorat individuel. Un enseignant (admin) publie ses créneaux de disponibilité hebdomadaires via un formulaire (jour, heure début, heure fin, durée par séance). Un élève (ou son parent) peut réserver un créneau. Le processus suit une **double-validation** : l'élève soumet une demande → l'enseignant confirme ou refuse → si confirmé, l'élève/parent reçoit un email de confirmation avec le lien de paiement (cf. #36). Les réservations passent par les états `en_attente` → `valide` | `annule`. L'annulation est possible par les deux parties jusqu'à 24h avant le créneau, avec remboursement automatique via Stripe (cf. #36). Le dashboard admin affiche les réservations à venir et en attente ; le dashboard élève affiche ses réservations confirmées et passées.

🎯 **Critères d'acceptation**
- L'enseignant peut créer/modifier/supprimer des créneaux de disponibilité récurrents (jour de la semaine + plage horaire)
- L'élève voit les créneaux disponibles sur une vue calendrier hebdomadaire et peut en réserver un
- La réservation passe par l'état `en_attente` jusqu'à validation par l'enseignant
- L'enseignant reçoit un email à chaque nouvelle demande ; l'élève reçoit un email à chaque changement d'état
- L'annulation est bloquée si le créneau est dans moins de 24h (HTTP 403 + message explicatif)
- Le dashboard admin affiche les réservations en attente (avec boutons Valider/Refuser) et les réservations à venir
- Le dashboard élève affiche les réservations confirmées (avec bouton Annuler si > 24h) et l'historique
- Les créneaux déjà réservés ne sont plus visibles pour les autres élèves

🏗 **Architecture**
- **Nouvelle app** : `tutoring/` avec `models.py`, `views.py`, `urls.py`, `admin.py`
- **Modèles** (`tutoring/models.py`) :
  ```
  DisponibiliteEnseignant
  ├── enseignant      FK → CustomUser (limit_choices_to={'role': 'admin'})
  ├── jour_semaine    IntegerField (0=lundi..6=dimanche)
  ├── heure_debut     TimeField
  ├── heure_fin       TimeField
  ├── duree_seance    DurationField (default=timedelta(hours=1))
  ├── actif           BooleanField(default=True)

  Reservation
  ├── eleve           FK → CustomUser (on_delete=CASCADE, related_name='reservations')
  ├── enseignant      FK → CustomUser (on_delete=CASCADE, related_name='reservations_enseignant')
  ├── date            DateField
  ├── heure_debut     TimeField
  ├── heure_fin       TimeField
  ├── statut          CharField — choices: en_attente / valide / annule / termine
  ├── motif_annulation TextField(blank=True)
  ├── stripe_payment_intent_id  CharField(max_length=255, blank=True)
  ├── created_at      DateTimeField(auto_now_add)
  ├── updated_at      DateTimeField(auto_now)
  unique_together: [enseignant, date, heure_debut]
  ```
- **Vues** (`tutoring/views.py`) :
  - `disponibilites_view(request)` — affiche le calendrier hebdomadaire avec créneaux libres (GET)
  - `reserver_view(request, pk)` — crée une `Reservation(statut='en_attente')` (POST, HTMX)
  - `valider_reservation_view(request, pk)` — enseignant valide → `statut='valide'` + email (POST, admin only)
  - `annuler_reservation_view(request, pk)` — annulation par élève ou enseignant si > 24h (POST)
  - `mes_reservations_view(request)` — liste des réservations de l'élève connecté
- **URLs** : préfixe `/tutorat/`, noms : `disponibilites`, `reserver`, `valider_reservation`, `annuler_reservation`, `mes_reservations`
- **Templates** : `templates/tutoring/disponibilites.html`, `reservations.html`, `mes_reservations.html`
- **Emails** : `templates/emails/reservation_nouvelle.html`, `reservation_validee.html`, `reservation_annulee.html` (+ `.txt`)
- **Fichiers impactés** : `tutoring/` (nouveau), `config/urls.py` (include), `templates/base.html` (sidebar link), `templates/dashboard/eleve.html` (section réservations), `templates/dashboard/admin.html` (section réservations en attente)

🧪 **Tests**
- `test_eleve_can_book_available_slot` — POST sur un créneau libre → `Reservation` créée avec `statut='en_attente'`
- `test_double_booking_prevented` — 2e élève tente de réserver le même créneau → HTTP 409 ou message d'erreur
- `test_enseignant_can_validate_reservation` — admin POST sur `valider_reservation` → `statut='valide'` + email envoyé
- `test_annulation_blocked_within_24h` — tentative d'annulation d'un créneau dans < 24h → HTTP 403
- `test_annulation_allowed_beyond_24h` — annulation d'un créneau dans > 24h → `statut='annule'`
- `test_eleve_cannot_validate_reservation` — élève POST sur `valider_reservation` → HTTP 403
- `test_cancelled_slot_becomes_available_again` — après annulation, le créneau réapparaît dans `disponibilites_view`

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : seuls les admins peuvent valider/refuser ; seul le propriétaire (élève ou enseignant lié) peut annuler. Vérification `reservation.eleve == request.user or request.user.is_admin` dans chaque vue.
- **OWASP A04 (Insecure Design)** : le `unique_together` sur `[enseignant, date, heure_debut]` empêche les double réservations au niveau base. En plus, un `select_for_update()` dans la vue de réservation prévient les race conditions.
- **OWASP A08 (Data Integrity)** : les transitions d'état sont contrôlées — `en_attente` → `valide` | `annule` uniquement. Pas de transition directe vers `termine` par les utilisateurs.
- **Rate limiting** : la vue `reserver_view` est protégée par le même pattern cache-based (10 req/min par élève) pour éviter le spam de réservations.

⚡ **Performance**
- `disponibilites_view` : 2 requêtes SQL (disponibilités enseignant + réservations existantes pour la semaine affichée).
- `reserver_view` : 1 `select_for_update` + 1 `create` (2 requêtes + 1 email).
- Dashboard : +1 requête SQL pour les réservations en attente/à venir (LIMIT 10, `select_related`).
- Index recommandé : `(enseignant, date)` sur `Reservation` pour les lookups calendrier.
- Budget : +2 requêtes SQL max par page impactée.

✅ **Definition of Done**
- Les créneaux de disponibilité sont gérables par l'enseignant
- L'élève peut réserver un créneau → statut `en_attente`
- L'enseignant peut valider/refuser → emails envoyés
- L'annulation fonctionne avec la contrainte des 24h
- Pas de double réservation possible (ni en base ni en race condition)
- Les dashboards admin et élève affichent les réservations
- Le mode preview est respecté (pas de réservation créée)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2, 3, 5)

---

### #36 — Stripe Pre-auth & Capture

**Description** : Intégrer Stripe pour le paiement des séances de tutorat avec un flux **pre-autorisation + capture différée**. Quand l'enseignant valide une réservation (#35), un `PaymentIntent` est créé avec `capture_method='manual'` et le lien de paiement est envoyé à l'élève/parent par email. Le montant est bloqué sur la carte mais pas débité. La capture effective (débit) est déclenchée automatiquement lorsque la séance passe en statut `termine` (après la date/heure du créneau) ou manuellement par l'enseignant. En cas d'annulation dans les délais (> 24h), le `PaymentIntent` est annulé (libération de la pre-auth). Ce flux protège l'élève (pas de débit avant la séance) et l'enseignant (garantie de paiement).

🎯 **Critères d'acceptation**
- Quand l'enseignant valide une réservation, un `PaymentIntent` Stripe est créé avec `capture_method='manual'` et le montant correspondant au tarif de la séance
- L'élève reçoit un email contenant un lien vers une page de paiement (Stripe Checkout Session en mode `payment` liée au `PaymentIntent`)
- Après paiement réussi, le `PaymentIntent` passe en `requires_capture` et la `Reservation.stripe_payment_intent_id` est mise à jour
- La capture est déclenchée automatiquement par une commande de gestion (`capture_sessions_terminees`) exécutée via cron/Heroku Scheduler après la fin du créneau
- En cas d'annulation (> 24h), le `PaymentIntent` est annulé via `stripe.PaymentIntent.cancel()` → remboursement automatique
- Le webhook Stripe (`checkout.session.completed`, `payment_intent.canceled`) met à jour le statut de la réservation
- Le dashboard admin affiche le statut de paiement (en attente / autorisé / capturé / annulé)

🏗 **Architecture**
- **Dépendance** : `stripe` (PyPI) ajouté à `requirements.txt`
- **Settings** (`config/settings/base.py`) :
  ```python
  STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY', default='')
  STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY', default='')
  STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET', default='')
  STRIPE_TUTORING_PRICE = config('STRIPE_TUTORING_PRICE', default=5000, cast=int)  # centimes
  ```
- **Vues** (`tutoring/views.py`) :
  - `creer_checkout_session(request, reservation_pk)` — crée `PaymentIntent` + `CheckoutSession`, redirige vers Stripe
  - `stripe_webhook(request)` — endpoint POST, vérifie la signature Stripe, dispatch selon `event.type`
  - `checkout_success(request)` — page de confirmation après paiement
  - `checkout_cancel(request)` — page d'annulation/retour
- **Management command** : `tutoring/management/commands/capture_sessions_terminees.py` — parcourt les `Reservation(statut='valide', heure_fin__lt=now)` dont le `PaymentIntent` est en `requires_capture`, appelle `stripe.PaymentIntent.capture()`
- **Modèle modifié** : `Reservation` — ajout de `stripe_checkout_session_id` (CharField), `paiement_statut` (CharField: `en_attente` / `autorise` / `capture` / `annule`)
- **URLs** : `/tutorat/checkout/<pk>/`, `/tutorat/webhook/`, `/tutorat/checkout/success/`, `/tutorat/checkout/cancel/`
- **Templates** : `templates/tutoring/checkout_success.html`, `checkout_cancel.html`
- **Fichiers impactés** : `tutoring/models.py`, `tutoring/views.py`, `tutoring/urls.py`, `config/settings/base.py`, `requirements.txt`, `tutoring/management/commands/capture_sessions_terminees.py` (nouveau)

🧪 **Tests**
- `test_checkout_session_created_on_validation` — valider une réservation → asserter `stripe.PaymentIntent.create` appelé avec `capture_method='manual'` (mock Stripe)
- `test_webhook_checkout_completed_updates_reservation` — POST webhook avec `checkout.session.completed` → asserter `paiement_statut='autorise'`
- `test_webhook_signature_verification` — POST webhook avec signature invalide → HTTP 400
- `test_annulation_cancels_payment_intent` — annuler une réservation autorisée → asserter `stripe.PaymentIntent.cancel` appelé (mock)
- `test_capture_command_captures_terminated_sessions` — réservation `valide` avec `heure_fin` passée → commande `capture_sessions_terminees` → asserter `stripe.PaymentIntent.capture` appelé
- `test_capture_command_skips_already_captured` — réservation déjà `capture` → commande ne fait rien

🔒 **Sécurité**
- **OWASP A02 (Cryptographic Failures)** : `STRIPE_SECRET_KEY` et `STRIPE_WEBHOOK_SECRET` stockés exclusivement dans les variables d'environnement, jamais en dur dans le code. `.env` est dans `.gitignore`.
- **OWASP A04 (Insecure Design)** : le webhook vérifie la signature Stripe via `stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_SECRET)` — pas de traitement sans signature valide.
- **OWASP A08 (Data Integrity)** : la vue `creer_checkout_session` est protégée par `@login_required` et vérifie `reservation.eleve == request.user`. L'enseignant ne peut pas payer à la place de l'élève.
- **CSRF** : le webhook Stripe est exempté de CSRF (`@csrf_exempt`) car authentifié par signature cryptographique.
- **Idempotence** : le webhook utilise `event.id` comme clé d'idempotence pour éviter les double-traitements.

⚡ **Performance**
- Les appels Stripe sont des I/O réseau (~200-500ms). Ils sont effectués uniquement sur les actions utilisateur (validation, annulation) et via la commande planifiée — jamais sur les pages de navigation.
- Le webhook est un endpoint léger : 1 vérification de signature + 1 UPDATE SQL.
- La commande `capture_sessions_terminees` est exécutée toutes les heures — elle traite un batch de `Reservation` (typiquement < 10 par exécution).
- Budget : 0 requête SQL ajoutée sur les pages existantes ; les coûts sont isolés dans les flux de paiement.

✅ **Definition of Done**
- Le flux pre-auth → capture fonctionne de bout en bout (Stripe test mode)
- Le webhook met à jour les statuts de réservation et de paiement
- L'annulation libère la pre-auth via `PaymentIntent.cancel()`
- La commande de capture automatique fonctionne pour les séances passées
- Les clés Stripe sont dans les variables d'environnement uniquement
- Le dashboard affiche les statuts de paiement
- Tests passent (avec Stripe mocké)
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2, 3, 6, 7)

---

### #37 — Sync Calendrier

**Description** : Permettre aux élèves et aux enseignants de synchroniser leurs réservations de tutorat confirmées avec leurs calendriers personnels. Le système génère des flux `.ics` dynamiques (iCalendar RFC 5545) personnalisés par utilisateur, accessibles via une URL signée unique. Des boutons "Ajouter à Google Calendar", "Ajouter à Apple Calendar" et "Ajouter à Outlook" sont affichés sur la page de confirmation de réservation et dans la vue `mes_reservations`. Le flux `.ics` se met à jour automatiquement quand des réservations sont ajoutées, modifiées ou annulées — les applications calendrier qui supportent la souscription (Apple Calendar, Outlook) reflètent les changements sans action de l'utilisateur.

🎯 **Critères d'acceptation**
- Chaque utilisateur (élève et enseignant) dispose d'une URL `.ics` unique et signée contenant toutes ses réservations confirmées et à venir
- L'URL `.ics` est accessible sans authentification (signée via token HMAC) mais ne révèle pas l'identité de l'utilisateur dans l'URL elle-même
- Les boutons "Google Calendar", "Apple Calendar", "Outlook" sont affichés à côté de chaque réservation confirmée et sur la page `mes_reservations`
- Le lien Google Calendar ouvre `calendar.google.com/calendar/r/eventedit?...` avec les paramètres pré-remplis (titre, date, heure, description)
- Le lien Apple/Outlook déclenche le téléchargement d'un fichier `.ics` pour l'événement individuel
- Le flux `.ics` de souscription inclut les réservations des 3 prochains mois et se met à jour dynamiquement
- Les réservations annulées apparaissent avec `STATUS:CANCELLED` dans le flux `.ics`

🏗 **Architecture**
- **Dépendance** : `icalendar` (PyPI) ajouté à `requirements.txt`
- **Modèle modifié** : `CustomUser` — ajout de `calendrier_token` (UUIDField, default=uuid4, unique) pour l'URL signée
- **Vues** (`tutoring/views.py`) :
  - `flux_ics_view(request, token)` — génère le flux `.ics` complet pour l'utilisateur identifié par `token` (pas de `@login_required`, authentifié par UUID)
  - `evenement_ics_view(request, reservation_pk)` — génère un `.ics` pour une seule réservation (téléchargement, `@login_required`)
- **Helper** (`tutoring/utils.py`) :
  - `generer_url_google_calendar(reservation)` — construit l'URL `calendar.google.com/calendar/r/eventedit?text=...&dates=...&details=...`
  - `generer_evenement_ical(reservation)` — retourne un objet `icalendar.Event` à partir d'une `Reservation`
- **URLs** : `/tutorat/calendrier/<uuid:token>.ics`, `/tutorat/calendrier/evenement/<pk>.ics`
- **Templates modifiés** : `templates/tutoring/mes_reservations.html` — boutons calendrier avec icônes SVG ; `templates/tutoring/checkout_success.html` — même boutons
- **Fichiers impactés** : `tutoring/views.py`, `tutoring/urls.py`, `tutoring/utils.py` (nouveau), `users/models.py`, `requirements.txt`, `templates/tutoring/mes_reservations.html`, `templates/tutoring/checkout_success.html`

🧪 **Tests**
- `test_ics_feed_returns_valid_icalendar` — GET `flux_ics_view` avec token valide → response `Content-Type: text/calendar` + contenu parseable par `icalendar.Calendar.from_ical()`
- `test_ics_feed_contains_confirmed_reservations` — utilisateur avec 2 réservations confirmées → asserter 2 `VEVENT` dans le flux
- `test_ics_feed_excludes_other_users_reservations` — le flux d'un utilisateur ne contient pas les réservations des autres
- `test_ics_feed_invalid_token_returns_404` — GET avec token UUID inexistant → HTTP 404
- `test_google_calendar_url_correctly_formatted` — asserter que l'URL générée contient les bons paramètres (`text`, `dates` au format `YYYYMMDDTHHmmSSZ`, `details`)
- `test_cancelled_reservation_has_cancelled_status_in_ics` — réservation annulée → `STATUS:CANCELLED` dans le `VEVENT`

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : le flux `.ics` est protégé par un UUID v4 aléatoire (122 bits d'entropie) — non devinable par brute force. L'URL ne contient ni le `pk` ni l'email de l'utilisateur.
- **OWASP A04 (Insecure Design)** : l'URL `.ics` est en lecture seule — aucune action de modification n'est possible via ce endpoint.
- **OWASP A07 (Identification Failures)** : si un token est compromis, l'utilisateur peut le régénérer via un bouton dans ses paramètres (reset du `calendrier_token`).
- Le contenu du `.ics` ne contient pas d'informations sensibles au-delà du nom de l'enseignant et de la date/heure du créneau — pas de données financières, pas d'adresse email exposée.

⚡ **Performance**
- `flux_ics_view` : 1 requête SQL (`Reservation.objects.filter(eleve|enseignant=user, date__gte=today-7d, date__lte=today+90d).select_related()`). Cacheable 5 min via `@cache_page(300)` ou `Cache-Control: max-age=300`.
- `evenement_ics_view` : 1 requête SQL (get_object_or_404).
- La génération `.ics` est CPU-négligeable (sérialisation texte simple).
- Budget : +1 requête SQL par accès au flux.

✅ **Definition of Done**
- Le flux `.ics` dynamique est accessible via URL signée (UUID)
- Les boutons Google/Apple/Outlook sont affichés sur les pages de réservation
- Le flux se met à jour automatiquement (ajouts, annulations)
- Le token est régénérable par l'utilisateur
- Les réservations annulées apparaissent comme `CANCELLED` dans le flux
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1.4, 2, 3, 5)

---

### #38 — Facturation SAP

**Description** : Générer des factures PDF conformes aux obligations légales SAP (Service à la Personne) pour chaque séance de tutorat terminée et payée. La facture inclut les mentions obligatoires : numéro de facture séquentiel, date, identité du prestataire (SIREN, agrément SAP), identité du client, nature de la prestation ("Soutien scolaire à domicile — cours particulier"), durée, montant TTC, mention "TVA non applicable — article 293 B du CGI" (si applicable), et la mention SAP spécifique pour le crédit d'impôt ("Attestation fiscale annuelle fournie sur demande"). La facture est générée via WeasyPrint (déjà utilisé pour les PDF de leçons) et envoyée par email à 3 parties : l'élève/parent, l'enseignant, et une copie archivée pour l'admin.

🎯 **Critères d'acceptation**
- Une facture PDF est générée automatiquement quand une réservation passe en statut `termine` et que le paiement est capturé
- La facture contient toutes les mentions légales SAP obligatoires (numéro séquentiel, SIREN, mentions TVA, mention crédit d'impôt)
- Le numéro de facture suit un format séquentiel sans trou : `SAP-YYYY-NNNN` (ex: `SAP-2026-0001`)
- La facture est envoyée par email à l'élève (ou parent si mineur), à l'enseignant, et à une adresse d'archive admin
- La facture PDF est stockée sur le système de fichiers (media) et accessible via le dashboard admin
- L'enseignant peut télécharger ses factures émises depuis son dashboard
- Une vue "Attestation fiscale annuelle" génère un récapitulatif PDF par client pour la déclaration d'impôts

🏗 **Architecture**
- **Modèle** (`tutoring/models.py`) :
  ```
  Facture
  ├── reservation     OneToOneField → Reservation (on_delete=PROTECT)
  ├── numero          CharField(max_length=20, unique=True)  — format SAP-YYYY-NNNN
  ├── date_emission   DateField(auto_now_add)
  ├── montant_ttc     DecimalField(max_digits=8, decimal_places=2)
  ├── fichier_pdf     FileField(upload_to='factures/%Y/%m/')
  ├── envoyee         BooleanField(default=False)
  ├── created_at      DateTimeField(auto_now_add)
  ```
- **Settings** (`config/settings/base.py`) :
  ```python
  SAP_SIREN = config('SAP_SIREN', default='')
  SAP_AGREMENT = config('SAP_AGREMENT', default='')
  SAP_NOM_PRESTATAIRE = config('SAP_NOM_PRESTATAIRE', default='')
  SAP_ADRESSE = config('SAP_ADRESSE', default='')
  SAP_EMAIL_ARCHIVE = config('SAP_EMAIL_ARCHIVE', default='')
  ```
- **Helper** (`tutoring/factures.py`) :
  - `generer_numero_facture()` — `SAP-{year}-{Facture.objects.filter(date_emission__year=year).count() + 1:04d}` avec `select_for_update` pour éviter les doublons
  - `generer_facture_pdf(reservation)` — rend le template `facture_sap.html` via WeasyPrint, sauvegarde dans `Facture.fichier_pdf`
  - `envoyer_facture_email(facture)` — `EmailMultiAlternatives` avec PDF en pièce jointe à 3 destinataires
  - `generer_attestation_annuelle(client, annee)` — PDF récapitulatif annuel pour le crédit d'impôt
- **Vues** (`tutoring/views.py`) :
  - `telecharger_facture_view(request, pk)` — sert le PDF de la facture (`@login_required`, accès limité au propriétaire/admin)
  - `attestation_annuelle_view(request, user_pk, annee)` — génère et sert l'attestation fiscale (admin uniquement)
  - `liste_factures_view(request)` — liste des factures pour l'enseignant/admin
- **Template** : `templates/tutoring/facture_sap.html` — template PDF WeasyPrint avec mise en page professionnelle (en-tête prestataire, mentions légales en pied, tableau prestation)
- **Intégration** : la commande `capture_sessions_terminees` (#36) appelle `generer_facture_pdf` + `envoyer_facture_email` après chaque capture réussie
- **URLs** : `/tutorat/facture/<pk>/`, `/tutorat/factures/`, `/tutorat/attestation/<user_pk>/<annee>/`
- **Fichiers impactés** : `tutoring/models.py`, `tutoring/factures.py` (nouveau), `tutoring/views.py`, `tutoring/urls.py`, `config/settings/base.py`, `templates/tutoring/facture_sap.html` (nouveau), `templates/tutoring/attestation_annuelle.html` (nouveau), `tutoring/management/commands/capture_sessions_terminees.py`

🧪 **Tests**
- `test_facture_generated_on_capture` — capture d'un paiement → asserter `Facture.objects.filter(reservation=reservation).exists()` et `fichier_pdf` non vide
- `test_facture_numero_sequential` — générer 3 factures → numéros `SAP-2026-0001`, `SAP-2026-0002`, `SAP-2026-0003`
- `test_facture_contains_mandatory_sap_mentions` — lire le PDF généré (ou le HTML source) → asserter la présence de SIREN, mention TVA, mention crédit d'impôt
- `test_facture_email_sent_to_three_parties` — capture → asserter `len(mail.outbox) == 1` avec 3 destinataires (to + cc)
- `test_telecharger_facture_forbidden_for_other_user` — élève A tente de télécharger la facture d'élève B → HTTP 403
- `test_attestation_annuelle_admin_only` — élève tente d'accéder à l'attestation → HTTP 403
- `test_facture_numero_no_gaps_on_concurrent_creation` — 2 factures créées simultanément → numéros consécutifs sans trou (test avec `select_for_update`)

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : `telecharger_facture_view` vérifie `facture.reservation.eleve == request.user or request.user.is_admin`. L'attestation annuelle est réservée aux admins.
- **OWASP A02 (Cryptographic Failures)** : les factures PDF sont stockées dans `MEDIA_ROOT/factures/` avec des noms de fichiers non prédictibles (UUID ou hash). Le `MEDIA_URL` n'est pas directement servi par nginx sans auth en production (servies via la vue Django).
- **OWASP A04 (Insecure Design)** : le numéro de facture est généré avec `select_for_update` pour garantir la séquentialité même sous charge concurrente — obligation légale de continuité de numérotation.
- **Données personnelles (RGPD)** : les factures contiennent nom, adresse et données de paiement du client. L'accès est strictement limité aux parties concernées.

⚡ **Performance**
- La génération PDF via WeasyPrint est CPU-intensive (~500ms-1s par facture). Elle est effectuée uniquement lors de la capture (commande planifiée, hors requête utilisateur) — pas d'impact sur le TTFB des pages.
- Le téléchargement de facture est un simple `FileResponse` (1 requête SQL + lecture fichier).
- L'attestation annuelle est générée à la demande (rare, ~1-2 fois/an par client) — pas besoin de cache.
- `generer_numero_facture` utilise `select_for_update` qui prend un lock de ligne — acceptable car la contention est très faible (quelques factures/jour).
- Budget : 0 requête SQL ajoutée sur les pages existantes ; coûts isolés dans le flux facturation.

✅ **Definition of Done**
- Les factures PDF sont générées automatiquement après capture Stripe
- Les numéros de facture sont séquentiels et sans trou
- Toutes les mentions légales SAP obligatoires sont présentes
- L'email est envoyé aux 3 parties (élève, enseignant, archive)
- Le téléchargement est protégé par contrôle d'accès
- L'attestation fiscale annuelle est disponible pour les admins
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2, 3, 5, 6, 7)

---

## Phase 8 — Intelligence Artificielle & Adaptive Learning (Month 7+)

*Goal: leverage AI to provide personalized tutoring and dynamic content generation.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 39 | **Tuteur IA "Socratique"** | Feature | Opus | ⬜ |
| 40 | **Génération dynamique de questions** | Feature | Opus | ⬜ |

---

### #39 — Tuteur IA "Socratique"

**Description** : Implémenter un chatbot IA contextuel accessible depuis la page résultat d'un quiz échoué. Quand un élève échoue à une question, il peut cliquer sur "Aide-moi à comprendre" pour ouvrir un panneau de conversation avec un tuteur IA qui adopte une approche **socratique** : il guide l'élève vers la réponse par des questions intermédiaires, des indices progressifs et des reformulations, sans jamais donner la réponse directement. Le tuteur a accès au contexte complet : la question posée, la mauvaise réponse de l'élève, la bonne réponse, et le contenu de la leçon associée. Chaque interaction est journalisée dans un modèle `AIAssistanceLog` pour analyse (taux d'utilisation, sujets difficiles, amélioration post-aide). L'intégration se fait via l'API OpenAI (ou compatible) avec un system prompt soigneusement conçu pour maintenir la posture socratique et le niveau pédagogique adapté (seconde/première/terminale).

🎯 **Critères d'acceptation**
- Un bouton "Aide-moi à comprendre 🤖" apparaît à côté de chaque question échouée sur `quiz_resultat.html`, `quiz_chapitre_resultat.html` et `revisions_resultat.html`
- Le clic ouvre un panneau de chat (Alpine.js) en bas de la page ou en modal, avec un historique de conversation
- Le premier message du tuteur IA est un indice contextuel basé sur l'erreur de l'élève (pas une réponse générique)
- Le tuteur ne donne **jamais** la réponse directement — il pose des questions intermédiaires, donne des indices progressifs, et félicite quand l'élève approche de la bonne réponse
- L'élève peut envoyer jusqu'à 10 messages par question (anti-abus)
- Chaque conversation est enregistrée dans `AIAssistanceLog` avec le nombre de messages, la question concernée, et si l'élève a exprimé avoir compris
- Le panneau respecte le dark mode et le système de couleurs par matière
- L'IA adapte son vocabulaire au niveau de l'élève (seconde vs terminale)

🏗 **Architecture**
- **Dépendance** : `openai` (PyPI) ajouté à `requirements.txt`
- **Settings** (`config/settings/base.py`) :
  ```python
  OPENAI_API_KEY = config('OPENAI_API_KEY', default='')
  OPENAI_MODEL = config('OPENAI_MODEL', default='gpt-4o-mini')
  AI_MAX_MESSAGES_PAR_QUESTION = 10
  ```
- **Modèle** (`progress/models.py`) :
  ```
  AIAssistanceLog
  ├── user            FK → CustomUser (on_delete=CASCADE, related_name='ai_logs')
  ├── question        FK → Question (on_delete=CASCADE, related_name='ai_logs')
  ├── messages        JSONField  — liste de {role, content, timestamp}
  ├── nb_messages     PositiveIntegerField(default=0)
  ├── compris         NullBooleanField  — feedback élève (True/False/None si pas répondu)
  ├── created_at      DateTimeField(auto_now_add)
  ├── updated_at      DateTimeField(auto_now)
  unique_together: [user, question]  — 1 conversation par (élève, question)
  ```
- **Vues** (`progress/views.py`) :
  - `tuteur_ia_view(request, question_pk)` — POST HTMX, reçoit le message de l'élève, appelle l'API OpenAI avec le contexte, retourne la réponse du tuteur en HTML partiel
  - `tuteur_ia_feedback(request, question_pk)` — POST HTMX, enregistre le feedback `compris` (True/False)
- **System prompt** (dans `progress/ai_prompts.py`) :
  ```
  Tu es un tuteur de {matiere} pour un élève de {niveau} dans le système éducatif français.
  L'élève a échoué à cette question : "{question.texte}"
  Sa réponse était : "{reponse_eleve}"
  La bonne réponse est : "{question.reponse_correcte}"
  Contenu de la leçon associée (pour contexte) : "{lecon.contenu[:2000]}"

  RÈGLES STRICTES :
  1. Ne donne JAMAIS la réponse directement
  2. Pose des questions intermédiaires pour guider la réflexion
  3. Donne des indices progressifs (du plus vague au plus précis)
  4. Utilise un vocabulaire adapté au niveau {niveau}
  5. Félicite les progrès, encourage la persévérance
  6. Si l'élève demande directement la réponse, refuse poliment et reformule un indice
  7. Reste dans le domaine de {matiere} — refuse poliment les questions hors-sujet
  ```
- **Frontend** (Alpine.js dans les templates résultat) :
  - Composant `x-data="tuteurIA(questionPk)"` avec `messages[]`, `input`, `loading`, `open`
  - Envoi via `fetch()` vers `tuteur_ia_view` (POST, CSRF token)
  - Affichage streaming ou réponse complète selon la latence
- **URLs** : `/progression/tuteur-ia/<question_pk>/`, `/progression/tuteur-ia/<question_pk>/feedback/`
- **Templates modifiés** : `quiz_resultat.html`, `quiz_chapitre_resultat.html`, `revisions_resultat.html` — ajout du bouton + composant chat
- **Fichiers impactés** : `progress/models.py`, `progress/views.py`, `progress/ai_prompts.py` (nouveau), `progress/urls.py`, `config/settings/base.py`, `requirements.txt`, `templates/courses/quiz_resultat.html`, `quiz_chapitre_resultat.html`, `revisions_resultat.html`

🧪 **Tests**
- `test_tuteur_ia_returns_response` — POST avec message → asserter HTTP 200 et contenu HTML non vide (mock OpenAI)
- `test_tuteur_ia_creates_log` — premier message → asserter `AIAssistanceLog.objects.filter(user=user, question=question).exists()`
- `test_tuteur_ia_max_messages_enforced` — envoyer 11 messages → le 11e retourne HTTP 429 avec message "Limite atteinte"
- `test_tuteur_ia_requires_login` — POST sans auth → HTTP 302 redirect vers login
- `test_tuteur_ia_feedback_records_compris` — POST feedback `compris=true` → asserter `AIAssistanceLog.objects.get(...).compris == True`
- `test_tuteur_ia_system_prompt_contains_question_context` — mock OpenAI, capturer les messages envoyés → asserter que le system prompt contient le texte de la question et la réponse de l'élève
- `test_tuteur_ia_skipped_in_preview_mode` — admin en preview → POST tuteur IA → HTTP 403 ou réponse sans log créé

🔒 **Sécurité**
- **OWASP A02 (Cryptographic Failures)** : `OPENAI_API_KEY` stockée exclusivement dans les variables d'environnement. Jamais exposée côté client — les appels API sont faits côté serveur uniquement.
- **OWASP A03 (Injection)** : le message de l'élève est inclus dans le prompt comme contenu utilisateur (`role: user`) et non dans le system prompt — l'API OpenAI traite les rôles séparément. Le contenu est nettoyé (`bleach.clean()` ou `strip_tags()`) avant inclusion pour éviter toute injection HTML dans la réponse affichée.
- **OWASP A04 (Insecure Design)** : le system prompt interdit explicitement de donner la réponse. En defense-in-depth, la réponse de l'IA est post-traitée pour détecter la présence de `question.reponse_correcte` en clair — si trouvée, la réponse est remplacée par un message générique d'encouragement.
- **Anti-abus** : limite de 10 messages par (élève, question) + rate limiting global (réutilisation de `_check_quiz_rate_limit` adapté à 20 req/min).
- **Coûts** : le modèle `gpt-4o-mini` est choisi pour son rapport coût/performance. Le `max_tokens` de la réponse est capé à 300 tokens pour limiter les coûts.

⚡ **Performance**
- L'appel API OpenAI est le bottleneck (~500ms-2s). Il est effectué uniquement sur action explicite de l'élève (clic + envoi de message), pas sur le chargement de page.
- `tuteur_ia_view` : 1 `get_or_create` sur `AIAssistanceLog` + 1 appel API + 1 `save()` = 2 requêtes SQL + 1 I/O réseau.
- Le contexte envoyé à l'API est limité : question + réponse + 2000 premiers caractères de la leçon — maîtrise des coûts tokens.
- Le composant Alpine.js est lazy-loaded (le HTML du chat n'est injecté qu'au premier clic).
- Budget : 0 requête SQL ajoutée sur le chargement initial des pages résultat ; coûts isolés dans les interactions chat.

✅ **Definition of Done**
- Le bouton "Aide-moi à comprendre" est visible sur les 3 pages résultat pour les questions échouées
- Le chatbot guide l'élève sans donner la réponse
- La conversation est enregistrée dans `AIAssistanceLog`
- La limite de 10 messages est respectée
- Le feedback (compris/pas compris) est enregistré
- Le mode preview ne crée pas de logs
- Le dark mode et les couleurs matière sont respectés
- Tests passent (avec OpenAI mocké)
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2.4, 3.2, 5.3, 6, 8)

---

### #40 — Génération dynamique de questions

**Description** : Utiliser l'IA pour générer des variations des questions existantes afin de fournir un contenu toujours renouvelé aux élèves qui refont les quiz. Au lieu de toujours présenter les mêmes questions, le système génère des variantes (reformulations, changements de valeurs numériques, contextes différents) qui testent la même compétence. Les variantes sont générées à l'avance (batch) ou à la demande, validées par un contrôle qualité automatique (cohérence réponse/question, format correct), et stockées dans un modèle `QuestionVariant`. L'enseignant peut approuver/rejeter les variantes depuis l'admin. Le quiz pioche aléatoirement parmi les variantes approuvées de chaque question originale pour offrir une expérience unique à chaque tentative.

🎯 **Critères d'acceptation**
- Pour chaque question originale, le système peut générer 3 à 5 variantes via l'API OpenAI
- Les variantes préservent : le type de question (QCM/vrai_faux/texte_libre), la difficulté, la compétence testée, et la structure (même nombre d'options pour un QCM)
- Les variantes QCM ont des options plausibles (pas de distracteurs absurdes) et une seule réponse correcte
- Les variantes numériques changent les valeurs mais maintiennent la cohérence mathématique (ex: si la question demande une vitesse = distance/temps, les nouvelles valeurs donnent un résultat correct)
- Chaque variante a un statut : `generee` → `approuvee` | `rejetee` (validation enseignant)
- Seules les variantes `approuvee` sont utilisées dans les quiz
- Le quiz pioche aléatoirement parmi la question originale et ses variantes approuvées
- Une commande de gestion `generer_variantes` parcourt les questions sans variantes et en génère
- L'admin peut voir, approuver, rejeter et supprimer les variantes depuis l'interface admin Django

🏗 **Architecture**
- **Modèle** (`courses/models.py`) :
  ```
  QuestionVariant
  ├── question_originale  FK → Question (on_delete=CASCADE, related_name='variantes')
  ├── texte               TextField
  ├── reponse_correcte    CharField(max_length=500)
  ├── options             JSONField(blank=True, null=True)  — pour QCM
  ├── tolerances          JSONField(blank=True, null=True)  — pour texte_libre
  ├── statut              CharField — choices: generee / approuvee / rejetee
  ├── score_qualite       FloatField(null=True)  — score auto-évaluation (0-1)
  ├── metadata_generation JSONField  — {model, prompt_version, generated_at}
  ├── created_at          DateTimeField(auto_now_add)
  ```
- **Helper** (`courses/ai_generation.py`) :
  - `generer_variantes_question(question, nb=3)` — appelle l'API OpenAI avec un prompt structuré, retourne une liste de `QuestionVariant` non sauvegardées
  - `_construire_prompt_generation(question)` — construit le prompt selon le type de question (QCM vs vrai_faux vs texte_libre) avec des exemples few-shot
  - `_valider_variante(question_originale, variante_data)` — contrôle qualité automatique :
    - QCM : vérifie que `reponse_correcte` est dans `options`, que le nombre d'options est identique
    - Texte libre : vérifie que la réponse n'est pas vide
    - Vrai/faux : vérifie que la réponse est "Vrai" ou "Faux"
    - Score de qualité basé sur la diversité lexicale (ratio mots différents vs question originale)
  - `_parser_reponse_ia(response_text, question_type)` — parse la réponse JSON structurée de l'IA
- **Management command** : `courses/management/commands/generer_variantes.py` :
  - `--quiz <quiz_pk>` : génère des variantes pour toutes les questions d'un quiz
  - `--all` : génère des variantes pour toutes les questions qui en ont < 3
  - `--dry-run` : affiche les variantes sans les sauvegarder
  - Utilise un batch de 5 questions par appel API pour optimiser les coûts
- **Modification quiz** (`courses/views.py` et `progress/views.py`) :
  - `_selectionner_questions_quiz(quiz)` (nouveau helper) — pour chaque question du quiz, pioche aléatoirement entre la question originale et ses variantes approuvées (`random.choice([question] + list(variantes))`)
  - Intégré dans `quiz_view`, `quiz_chapitre_view` (via `_selectionner_questions_chapitre`), et `revisions_view`
  - Le template quiz doit gérer les deux cas : question originale (objet `Question`) et variante (objet `QuestionVariant`) — un template tag ou une propriété unifiée simplifie cela
- **Admin** (`courses/admin.py`) :
  - `QuestionVariantAdmin` avec `list_display(question_originale, texte[:80], statut, score_qualite)`, `list_filter(statut, question_originale__quiz__lecon__chapitre__matiere)`, actions batch `approuver_variantes` et `rejeter_variantes`
  - Inline `QuestionVariantInline` sur `QuestionAdmin` pour voir les variantes d'une question
- **URLs** : pas de nouvelles URLs publiques — la génération passe par la commande de gestion et l'admin Django
- **Fichiers impactés** : `courses/models.py`, `courses/ai_generation.py` (nouveau), `courses/admin.py`, `courses/views.py`, `progress/views.py`, `courses/management/commands/generer_variantes.py` (nouveau), `requirements.txt` (si `openai` pas déjà ajouté par #39), `templates/courses/quiz.html` (adaptation pour QuestionVariant)

🧪 **Tests**
- `test_generer_variantes_creates_variants` — appeler `generer_variantes_question(question_qcm)` (mock OpenAI) → asserter 3 `QuestionVariant` créées avec `statut='generee'`
- `test_variante_qcm_has_correct_answer_in_options` — variante QCM générée → asserter `variante.reponse_correcte in variante.options`
- `test_variante_vrai_faux_valid_response` — variante vrai/faux → asserter `variante.reponse_correcte in ['Vrai', 'Faux']`
- `test_validation_rejects_invalid_qcm` — variante QCM dont `reponse_correcte` n'est pas dans `options` → score_qualite = 0, non sauvegardée
- `test_quiz_view_uses_approved_variants` — question avec 2 variantes approuvées → GET quiz multiple fois → asserter que les textes affichés varient (statistiquement)
- `test_quiz_view_ignores_rejected_variants` — question avec 1 variante rejetée → asserter que le texte de la variante rejetée n'apparaît jamais
- `test_generer_variantes_command_dry_run` — `call_command('generer_variantes', '--all', '--dry-run')` → asserter 0 `QuestionVariant` en base
- `test_evaluer_reponses_works_with_variants` — soumettre un quiz avec une variante → asserter que `_evaluer_reponses` évalue correctement avec `variante.reponse_correcte`

🔒 **Sécurité**
- **OWASP A02 (Cryptographic Failures)** : `OPENAI_API_KEY` (partagée avec #39) stockée dans les variables d'environnement uniquement.
- **OWASP A03 (Injection)** : les variantes générées par l'IA sont stockées en base et servies comme du contenu statique — pas d'exécution dynamique. Le texte des variantes est échappé par le template engine Django (`{{ variante.texte }}` auto-escape).
- **OWASP A04 (Insecure Design)** : le workflow `generee → approuvee` impose une validation humaine avant qu'une variante soit utilisée en quiz. Aucune variante n'est servie sans approbation explicite de l'enseignant.
- **Intégrité pédagogique** : le contrôle qualité automatique (`_valider_variante`) filtre les variantes incohérentes avant même la review humaine. Le `score_qualite` aide à prioriser la review.
- **Coûts** : la génération batch est contrôlée via la commande de gestion (pas de génération automatique à chaque quiz). Le `max_tokens` est capé et le prompt est optimisé pour minimiser les tokens.

⚡ **Performance**
- La génération de variantes est un processus batch (commande de gestion), jamais en temps réel pendant un quiz — 0 impact sur le TTFB.
- La sélection de variantes dans `_selectionner_questions_quiz` : +1 requête SQL (`QuestionVariant.objects.filter(question_originale__in=questions, statut='approuvee')`) groupée, puis `random.choice` en Python — négligeable.
- L'admin `QuestionVariantAdmin` : pagination standard Django (25/page), `select_related('question_originale')`.
- La commande `generer_variantes --all` fait ~N/5 appels API (batch de 5) — pour 200 questions, ~40 appels, ~2-3 min.
- Index recommandé : `(question_originale, statut)` sur `QuestionVariant` pour le filtre quiz.
- Budget : +1 requête SQL groupée dans les vues quiz (amortie sur toutes les questions du quiz).

✅ **Definition of Done**
- La commande `generer_variantes` génère des variantes valides pour les 3 types de questions
- Le contrôle qualité automatique filtre les variantes incohérentes
- L'admin peut approuver/rejeter les variantes individuellement ou en batch
- Les quiz piochent aléatoirement parmi question originale + variantes approuvées
- `_evaluer_reponses` fonctionne correctement avec les variantes
- Le `--dry-run` n'écrit rien en base
- Tests passent (avec OpenAI mocké)
- CODEBASE_REFERENCE.md mis à jour (sections 1, 3, 7, 8)

---

## Phase 9 — PWA, Offline & Mobile Experience (Month 8+)

*Goal: make ScienceLycée installable, usable offline, and push revision reminders via web notifications.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 41 | **PWA — manifest.json + Service Worker** | Tech | Sonnet | ⬜ |
| 42 | **Mode hors-ligne** | Tech | Sonnet | ⬜ |
| 43 | **Web Push Notifications** | Tech | Opus | ⬜ |

---

### #41 — PWA — manifest.json + Service Worker

**Description** : Transformer ScienceLycée en Progressive Web App installable sur iOS et Android. Ajouter un `manifest.json` correctement configuré (nom, icônes 192×512, `start_url`, `display: standalone`, `theme_color` bleu ScienceLycée, `background_color` blanc) et enregistrer un Service Worker (`sw.js`) minimal à la racine du site. Le Service Worker gère le pré-cache de l'app shell (HTML squelette, Tailwind CDN, Alpine.js, HTMX, KaTeX) et implémente une stratégie *Stale-While-Revalidate* pour les assets statiques. Un bandeau "Installer l'application" (A2HS) s'affiche une seule fois pour les visiteurs éligibles (navigateurs supportant `beforeinstallprompt` sur Android ; instruction manuelle pour iOS Safari). L'installation est trackée via un événement `appinstalled`.

🎯 **Critères d'acceptation**
- `manifest.json` est servi à `/manifest.json` avec les icônes 192px et 512px
- Le `<link rel="manifest">` est présent dans `base.html`
- `sw.js` est enregistré depuis `base.html` et contrôle la page au second chargement
- L'app shell (HTML squelette + CDN assets) est pré-cachée à l'installation du SW
- Un bandeau A2HS s'affiche une seule fois (flag `localStorage`) sur les navigateurs compatibles
- Lighthouse PWA score ≥ 90

🏗 **Architecture**
- **Nouveau fichier** : `static/manifest.json` — déclaration PWA standard ; servi via `{% static 'manifest.json' %}` ou route Django dédiée si nécessaire
- **Nouveau fichier** : `static/sw.js` — Service Worker ; enregistré via `<script>` dans `base.html` ; scope `/`
- **Nouveaux fichiers** : `static/icons/icon-192.png`, `static/icons/icon-512.png` — icônes PWA
- **Template modifié** : `base.html` — ajout `<link rel="manifest">`, `<meta name="theme-color">`, script d'enregistrement SW, bandeau A2HS Alpine.js (`x-data="{ showInstall: false }"`)
- **Stratégie de cache** : *Cache-first* pour les icônes/fonts, *Stale-While-Revalidate* pour CDN assets (Tailwind, Alpine, HTMX, KaTeX), *Network-first* pour les pages HTML
- **Fichiers impactés** : `static/manifest.json` (nouveau), `static/sw.js` (nouveau), `static/icons/` (nouveau), `templates/base.html`

🧪 **Tests**
- `test_manifest_json_served` — GET `/static/manifest.json` → status 200, `content-type: application/manifest+json`, contient `"name": "ScienceLycée"`
- `test_manifest_icons_exist` — asserter que les fichiers `icon-192.png` et `icon-512.png` existent dans `static/icons/`
- `test_base_html_has_manifest_link` — GET `/` → HTML contient `<link rel="manifest"`
- `test_sw_js_served_at_root_scope` — GET `/sw.js` (ou `/static/sw.js`) → status 200, contient `self.addEventListener('install'`
- `test_a2hs_banner_markup_present` — GET page authentifiée → HTML contient `showInstall` (composant Alpine A2HS)

🔒 **Sécurité**
- **OWASP A05 (Security Misconfiguration)** : `sw.js` doit être servi avec `Content-Type: application/javascript` et `Service-Worker-Allowed: /` header si le fichier est dans `/static/`. Le scope du SW est limité à `/` — pas d'interception de requêtes cross-origin.
- **OWASP A07 (XSS)** : le SW ne modifie jamais le contenu des réponses cachées — il sert les réponses telles quelles. Aucune injection possible via le cache.
- Le `manifest.json` ne contient aucune donnée sensible.

⚡ **Performance**
- Le pré-cache de l'app shell (~200 KB total : HTML squelette + CDN refs) accélère les navigations suivantes de ~30-50% (pas de re-téléchargement réseau).
- Le SW n'intercepte que les requêtes `same-origin` + les CDN connues — aucun ralentissement sur les requêtes tierces.
- Le bandeau A2HS est purement Alpine.js côté client — 0 requête serveur.
- Budget : +0 requête SQL ; +~5 KB de JS (enregistrement SW + bandeau).

✅ **Definition of Done**
- `manifest.json` et `sw.js` sont déployés et fonctionnels
- L'app est installable via A2HS sur Android Chrome et via instructions manuelles sur iOS Safari
- Lighthouse PWA ≥ 90
- L'app shell est servie depuis le cache au second chargement (vérifiable dans DevTools > Application > Cache Storage)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour

---

### #42 — Mode hors-ligne

**Description** : Permettre aux élèves de consulter les leçons déjà visitées même sans connexion internet. Le Service Worker (installé en #41) est étendu avec une stratégie de cache intelligente : les pages de leçons textuelles (HTML rendu + SVGs LaTeX inline) sont cachées dans un cache dédié `scienlycee-lessons-v1` lors de la première visite. Les assets critiques (Tailwind CDN, Alpine.js, HTMX, KaTeX) sont pré-cachés à l'installation. Les soumissions de quiz utilisent une stratégie *Network-first* avec fallback qui affiche un message "Reconnecte-toi pour soumettre" au lieu de crasher. Une page offline dédiée (`offline.html`) est affichée pour les pages non cachées. Un indicateur de statut réseau (online/offline) est affiché dans le header via Alpine.js (`navigator.onLine`).

🎯 **Critères d'acceptation**
- Les leçons visitées sont consultables hors-ligne (texte + SVGs LaTeX)
- Les assets CDN (Tailwind, Alpine, HTMX, KaTeX) sont disponibles hors-ligne après la première visite
- Les soumissions de quiz hors-ligne affichent un message d'erreur gracieux (pas de crash)
- Une page `offline.html` s'affiche pour les pages non cachées
- Un badge "Hors-ligne" apparaît dans le header quand `navigator.onLine === false`
- Le cache est versionné (`scienlycee-lessons-v1`) et les anciens caches sont nettoyés à l'activation

🏗 **Architecture**
- **Fichier modifié** : `static/sw.js` — extension du SW de #41 avec :
  - Cache `scienlycee-static-v1` : pré-cache à l'installation (app shell + CDN assets)
  - Cache `scienlycee-lessons-v1` : cache dynamique des pages `/cours/lecon/` visitées (stratégie *Network-first*, fallback cache)
  - Cache `scienlycee-images-v1` : SVGs LaTeX et images (stratégie *Cache-first*)
  - Stratégie *Network-only* pour les POST (soumissions quiz) — pas de cache des mutations
  - Fallback `offline.html` pour les navigations non cachées
  - Nettoyage des anciens caches dans l'événement `activate`
- **Nouveau template** : `templates/offline.html` — page self-contained (pas de `{% extends %}`) avec CSS inline, message "Vous êtes hors-ligne", et bouton "Réessayer" (`location.reload()`)
- **Template modifié** : `base.html` — ajout d'un badge Alpine.js `x-data="{ online: navigator.onLine }"` avec listeners `@online.window` / `@offline.window`
- **Template modifié** : `templates/courses/quiz.html` — le formulaire de soumission vérifie `navigator.onLine` avant le POST et affiche un message si hors-ligne
- **Fichiers impactés** : `static/sw.js`, `templates/offline.html` (nouveau), `templates/base.html`, `templates/courses/quiz.html`

🧪 **Tests**
- `test_offline_page_served` — GET `/offline.html` (ou route dédiée) → status 200, contient "hors-ligne"
- `test_offline_page_self_contained` — le HTML de `offline.html` ne dépend d'aucun `{% extends %}` ni `{% static %}` — tout est inline
- `test_sw_caches_lesson_pages` — (E2E Playwright) visiter une leçon, passer offline, recharger → contenu affiché
- `test_sw_shows_offline_page_for_uncached` — (E2E Playwright) passer offline, naviguer vers une page non visitée → `offline.html` affiché
- `test_quiz_submission_offline_shows_message` — (E2E Playwright) passer offline, soumettre quiz → message "Reconnecte-toi" affiché (pas d'erreur réseau brute)
- `test_online_offline_badge` — (E2E Playwright) vérifier que le badge "Hors-ligne" apparaît/disparaît selon l'état réseau

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : le SW ne cache que les pages où l'utilisateur est déjà authentifié et autorisé — il ne contourne pas les contrôles d'accès serveur. Si le token de session expire, la prochaine requête réseau redirigera vers le login.
- **OWASP A04 (Insecure Design)** : les soumissions de quiz sont strictement *Network-only* — pas de replay hors-ligne, pas de mise en file d'attente. Cela évite les problèmes de cohérence et de triche.
- **Données cachées** : le cache contient du HTML rendu (pas de données brutes JSON). Si l'appareil est partagé, un autre utilisateur pourrait voir le contenu caché. Mitigation : le cache est purgé au logout (appel `caches.delete()` dans le handler de déconnexion).

⚡ **Performance**
- Le cache des leçons évite les re-téléchargements réseau pour les pages déjà visitées — gain de ~100-300ms par navigation (LTE/3G).
- La stratégie *Cache-first* pour les SVGs LaTeX est particulièrement bénéfique car ces fichiers sont statiques et souvent volumineux.
- Taille maximale du cache leçons : ~50 MB (quota navigateur standard). Au-delà, les entrées les plus anciennes sont évictées (LRU).
- Le badge online/offline est purement Alpine.js côté client — 0 requête serveur, 0 impact TTFB.
- Budget : +0 requête SQL ; +~2 KB de JS (listeners réseau).

✅ **Definition of Done**
- Les leçons visitées sont consultables hors-ligne avec leur contenu complet (texte + SVGs)
- Les CDN assets fonctionnent hors-ligne
- La page `offline.html` s'affiche pour les pages non cachées
- Les soumissions de quiz hors-ligne affichent un message gracieux
- Le badge online/offline fonctionne
- Le cache est nettoyé au logout
- Tests E2E passent (Playwright)
- CODEBASE_REFERENCE.md mis à jour

---

### #43 — Web Push Notifications

**Description** : Implémenter les Web Push Notifications pour envoyer des rappels de révision Leitner aux élèves. L'élève peut activer les notifications depuis son dashboard via un bouton "Activer les rappels 🔔". L'abonnement push est stocké côté serveur dans un modèle `PushSubscription` lié au `CustomUser`. Un worker Celery (ou commande de gestion cron) vérifie quotidiennement quels élèves ont des cartes Leitner dues (`prochaine_revision ≤ now()` dans `UserQuestionHistorique`) et leur envoie une notification push "Tu as X cartes à réviser aujourd'hui !". Les clés VAPID sont générées une seule fois et stockées dans les variables d'environnement. La librairie `pywebpush` gère l'envoi des notifications. L'élève peut désactiver les notifications à tout moment.

🎯 **Critères d'acceptation**
- Un bouton "Activer les rappels 🔔" est affiché sur le dashboard élève
- Le clic déclenche la demande de permission du navigateur (`Notification.requestPermission()`)
- Si l'élève accepte, l'abonnement push (`PushSubscription`) est envoyé au serveur et stocké en base
- Le serveur envoie une notification push quotidienne aux élèves ayant des cartes Leitner dues
- La notification contient le nombre de cartes à réviser et un lien vers `/cours/revisions/`
- L'élève peut désactiver les notifications (suppression de la `PushSubscription` en base)
- Les notifications fonctionnent sur Chrome (Desktop + Android) et Firefox

🏗 **Architecture**
- **Nouveau modèle** (`users/models.py`) :
  ```
  PushSubscription
  ├── user                FK → CustomUser (on_delete=CASCADE, related_name='push_subscriptions')
  ├── endpoint            URLField(max_length=500)
  ├── p256dh              CharField(max_length=200)  # clé publique client
  ├── auth                CharField(max_length=100)  # secret d'authentification
  ├── created_at          DateTimeField(auto_now_add)
  ├── unique_together     [("user", "endpoint")]
  ```
- **Nouvelles vues** (`users/views.py`) :
  - `sauvegarder_push_subscription(request)` — POST, `@login_required`, JSON body ; crée ou met à jour la `PushSubscription`
  - `supprimer_push_subscription(request)` — POST, `@login_required`, JSON body ; supprime la subscription
- **Nouvelles URLs** (`users/urls.py`) : `push-subscribe` (POST), `push-unsubscribe` (POST)
- **Nouvelle commande de gestion** : `courses/management/commands/envoyer_rappels_push.py` — itère les élèves avec des cartes Leitner dues, envoie les notifications via `pywebpush`, gère les erreurs (subscription expirée → suppression)
- **Settings** (`config/settings/base.py`) : `VAPID_PUBLIC_KEY`, `VAPID_PRIVATE_KEY`, `VAPID_CLAIMS_EMAIL` — lus via `decouple.config()`
- **Package** : `pywebpush` ajouté à `requirements.txt`
- **Template modifié** : `templates/dashboard/eleve.html` — bouton Alpine.js pour activer/désactiver les notifications push, avec logique JS d'abonnement/désabonnement (`navigator.serviceWorker.ready.then(reg => reg.pushManager.subscribe(...))`)
- **Fichier modifié** : `static/sw.js` — ajout du listener `push` pour afficher la notification et `notificationclick` pour ouvrir `/cours/revisions/`
- **Fichiers impactés** : `users/models.py`, `users/views.py`, `users/urls.py`, `config/settings/base.py`, `requirements.txt`, `templates/dashboard/eleve.html`, `static/sw.js`, `courses/management/commands/envoyer_rappels_push.py` (nouveau)

🧪 **Tests**
- `test_sauvegarder_push_subscription` — POST JSON valide → status 201, `PushSubscription` créée en base avec les bonnes clés
- `test_sauvegarder_push_subscription_duplicate` — POST même endpoint 2 fois → 1 seule `PushSubscription` (upsert)
- `test_supprimer_push_subscription` — POST endpoint existant → `PushSubscription` supprimée, status 200
- `test_push_subscription_requires_auth` — POST sans authentification → redirect login
- `test_envoyer_rappels_push_sends_notifications` — créer 2 élèves avec cartes Leitner dues + `PushSubscription` ; mock `pywebpush.webpush` ; `call_command('envoyer_rappels_push')` → asserter 2 appels `webpush`
- `test_envoyer_rappels_push_cleans_expired` — mock `webpush` raise `WebPushException(410)` → `PushSubscription` supprimée en base
- `test_envoyer_rappels_push_skips_no_cards_due` — élève avec cartes Leitner non dues → 0 appel `webpush`

🔒 **Sécurité**
- **OWASP A02 (Cryptographic Failures)** : les clés VAPID (`VAPID_PRIVATE_KEY`) sont stockées uniquement dans les variables d'environnement, jamais en base ni en code.
- **OWASP A01 (Broken Access Control)** : les vues `sauvegarder_push_subscription` et `supprimer_push_subscription` sont `@login_required` et filtrent par `request.user` — un utilisateur ne peut pas modifier les subscriptions d'un autre.
- **OWASP A07 (XSS)** : le contenu de la notification est généré côté serveur (texte statique + compteur) — aucune donnée utilisateur dans le body de la notification.
- **Anti-spam** : la commande `envoyer_rappels_push` est conçue pour être exécutée 1×/jour via cron. Pas de mécanisme d'envoi depuis les vues (pas de spam possible par un utilisateur).
- **Consentement** : les notifications ne sont envoyées qu'aux élèves ayant explicitement activé les push (opt-in).

⚡ **Performance**
- La commande `envoyer_rappels_push` fait 1 requête SQL pour récupérer les élèves avec cartes dues (`UserQuestionHistorique.objects.filter(prochaine_revision__lte=now).values('user').distinct()`) + 1 requête pour leurs subscriptions. Total : 2 requêtes SQL quel que soit le nombre d'élèves.
- Les appels `webpush` sont I/O-bound (HTTP vers les push services). Pour un déploiement > 1000 élèves, envisager un pool de threads ou Celery.
- L'abonnement push (JS côté client) est une opération one-shot — pas d'impact sur les navigations suivantes.
- Budget : +2 requêtes SQL (commande cron) ; +0 en navigation normale.

✅ **Definition of Done**
- Le bouton d'activation fonctionne (permission demandée, subscription envoyée au serveur)
- Les notifications push sont reçues sur Chrome et Firefox
- La commande `envoyer_rappels_push` envoie aux élèves avec cartes Leitner dues
- Les subscriptions expirées sont nettoyées automatiquement
- L'élève peut désactiver les notifications
- Tests passent (avec `webpush` mocké)
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2, 3, 7)

---

## Phase 10 — UGC Enseignants, Analytics & Performance (Month 9+)

*Goal: empower teachers with content creation tools, add granular time analytics, and optimize platform performance with caching.*

| # | Task | Type | LLM | Status |
|---|------|------|-----|--------|
| 44 | **Création contenu privé UGC** | Feature | Opus | ⬜ |
| 45 | **Analytics granulaires temps** | Feature | Sonnet | ⬜ |
| 46 | **Cache Redis** | Tech | Sonnet | ⬜ |
| 47 | **Gels de série (streak freezes)** | Feature | Sonnet | ⬜ |

---

### #44 — Création contenu privé UGC

**Description** : Ajouter un espace dédié aux enseignants pour créer du contenu pédagogique personnalisé (leçons et quiz) visible uniquement par leurs élèves liés. Un nouveau rôle `enseignant` est ajouté au `CustomUser.role` (en plus de `admin` et `eleve`). L'enseignant peut créer des `Lecon` et `Quiz` marqués comme privés (`visibilite='prive'`, `auteur=request.user`). Les élèves sont liés à un enseignant via un modèle `ClasseVirtuelle` (l'enseignant partage un code d'invitation alphanumérique que les élèves saisissent). Le contenu privé apparaît dans une section dédiée du catalogue de l'élève ("Contenu de mon professeur") et n'est pas indexé par les moteurs de recherche. L'enseignant dispose d'un dashboard simplifié avec stats de consultation de son contenu.

🎯 **Critères d'acceptation**
- L'enseignant peut créer des leçons Markdown avec prévisualisation live (split-pane Alpine.js)
- L'enseignant peut créer des quiz (QCM, Vrai/Faux, Texte libre) associés à ses leçons
- Le contenu privé est visible uniquement par les élèves de la `ClasseVirtuelle` de l'enseignant
- L'enseignant peut générer/régénérer un code d'invitation pour sa classe virtuelle
- L'élève peut rejoindre une classe virtuelle via un code d'invitation (max 1 classe active)
- Le contenu UGC n'apparaît pas dans le catalogue public ni dans les sitemaps
- L'enseignant voit des stats basiques : nombre de consultations par leçon, scores moyens par quiz

🏗 **Architecture**
- **Modification modèle** (`users/models.py`) : ajout `'enseignant'` aux choices de `CustomUser.role`
- **Nouveaux modèles** (`courses/models.py`) :
  ```
  ClasseVirtuelle
  ├── enseignant       FK → CustomUser (limit_choices_to={'role': 'enseignant'}, on_delete=CASCADE)
  ├── nom              CharField(200)
  ├── code_invitation  CharField(8), unique, auto-généré (secrets.token_urlsafe(6))
  ├── created_at       DateTimeField(auto_now_add)

  # Modèle M2M explicite
  MembreClasse
  ├── classe           FK → ClasseVirtuelle (on_delete=CASCADE)
  ├── eleve            FK → CustomUser (limit_choices_to={'role': 'eleve'}, on_delete=CASCADE)
  ├── date_adhesion    DateTimeField(auto_now_add)
  ├── unique_together  [("classe", "eleve")]
  ```
- **Modification modèle** (`courses/models.py`) : ajout sur `Lecon` :
  - `visibilite` : `CharField(10)` choices `['public', 'prive']`, default `'public'`
  - `auteur` : `FK → CustomUser (null=True, blank=True, on_delete=SET_NULL)`
- **Nouvelles vues** (`courses/views.py`) :
  - `espace_enseignant_view(request)` — dashboard enseignant, liste du contenu créé + stats
  - `creer_lecon_ugc(request)` — formulaire de création de leçon avec prévisualisation Markdown
  - `creer_quiz_ugc(request)` — formulaire de création de quiz multi-questions
  - `rejoindre_classe(request)` — POST, formulaire avec code d'invitation
  - `generer_code_invitation(request, classe_id)` — POST, régénère le code
- **Nouvelles URLs** (`courses/urls.py`) : `espace-enseignant`, `creer-lecon`, `creer-quiz`, `rejoindre-classe`, `generer-code`
- **Nouveaux templates** : `templates/courses/espace_enseignant.html`, `templates/courses/creer_lecon.html`, `templates/courses/creer_quiz.html`, `templates/courses/rejoindre_classe.html`
- **Templates modifiés** : `templates/courses/chapitres.html` — section "Contenu de mon professeur" conditionnelle
- **Sanitization** : `bleach.clean()` appliqué sur le Markdown des leçons UGC avant stockage (whitelist de tags HTML autorisés)
- **Fichiers impactés** : `users/models.py`, `courses/models.py`, `courses/views.py`, `courses/urls.py`, `courses/forms.py` (nouveau ou modifié), 4 nouveaux templates, `requirements.txt` (`bleach`)

🧪 **Tests**
- `test_enseignant_can_create_lecon` — POST avec rôle `enseignant` → `Lecon` créée avec `visibilite='prive'` et `auteur=enseignant`
- `test_eleve_cannot_create_lecon` — POST avec rôle `eleve` → redirect ou 403
- `test_eleve_sees_private_content_of_their_teacher` — élève membre d'une `ClasseVirtuelle` → voit les leçons privées de cet enseignant
- `test_eleve_does_not_see_other_teachers_content` — élève non membre → ne voit pas le contenu privé
- `test_private_lecon_not_in_catalogue` — GET catalogue public → les leçons `prive` sont absentes
- `test_rejoindre_classe_with_valid_code` — POST code valide → `MembreClasse` créé
- `test_rejoindre_classe_with_invalid_code` — POST code invalide → erreur 404 ou message
- `test_ugc_lecon_bleach_sanitized` — créer une leçon avec `<script>alert('xss')</script>` dans le contenu → asserter que le `<script>` est supprimé en base
- `test_enseignant_dashboard_shows_stats` — enseignant avec 2 leçons → dashboard affiche les compteurs

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : toutes les vues UGC vérifient `request.user.role == 'enseignant'`. Le contenu privé est filtré par `MembreClasse.objects.filter(eleve=request.user, classe__enseignant=lecon.auteur).exists()` — jamais de fuite de contenu.
- **OWASP A03 (Injection / XSS)** : le contenu Markdown UGC est sanitisé via `bleach.clean()` avec une whitelist stricte de tags (`p, h1-h6, ul, ol, li, strong, em, code, pre, blockquote, a, img, table, thead, tbody, tr, th, td`). Les attributs sont limités (`href` pour `a`, `src/alt` pour `img`). Le JavaScript est entièrement supprimé.
- **OWASP A04 (Insecure Design)** : le code d'invitation est généré via `secrets.token_urlsafe(6)` (8 caractères, 48 bits d'entropie) — suffisant pour un code partagé verbalement. L'enseignant peut le régénérer à tout moment.
- **CSRF** : toutes les vues POST utilisent `@csrf_protect` (comportement par défaut Django) — les formulaires incluent `{% csrf_token %}`.

⚡ **Performance**
- Les leçons privées sont filtrées en SQL (`visibilite='prive', auteur__in=enseignants_de_mes_classes`) — 2-3 requêtes SQL max pour l'affichage du catalogue élève avec section UGC.
- Le dashboard enseignant utilise des agrégations SQL (`Count`, `Avg`) — pas de boucle Python.
- Le `bleach.clean()` est appelé une seule fois au `save()`, pas à chaque affichage — 0 impact sur le TTFB de lecture.
- Budget : +2-3 requêtes SQL pour les élèves ayant un enseignant ; +0 pour les autres ; +1 agrégation pour le dashboard enseignant.

✅ **Definition of Done**
- L'enseignant peut créer leçons et quiz privés avec prévisualisation
- Les élèves de sa classe voient le contenu dans une section dédiée
- Le contenu privé est invisible dans le catalogue public et les sitemaps
- Le code d'invitation fonctionne (rejoindre + régénérer)
- Le contenu UGC est sanitisé (pas de XSS)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2, 3, 4, 5)

---

### #45 — Analytics granulaires temps

**Description** : Ajouter un tracking JavaScript non intrusif du temps passé par question dans les quiz et par section dans les leçons. Les données sont envoyées au serveur via des requêtes HTMX `hx-trigger="visibilitychange"` (ou `beforeunload`) et stockées dans un modèle `TempsInteraction`. Un dashboard enseignant (et admin) agrège ces données pour identifier les questions/sections où les élèves passent le plus de temps (potentiels points de difficulté). Les graphiques utilisent Chart.js (déjà disponible via CDN pour le dashboard élève). Le tracking respecte la vie privée : pas de données personnelles au-delà de l'identifiant utilisateur, pas de tracking tiers, conformité RGPD.

🎯 **Critères d'acceptation**
- Le temps passé par question est enregistré (precision : seconde) pendant les quiz
- Le temps passé sur une page de leçon est enregistré (entrée/sortie)
- Le dashboard enseignant affiche un graphique "temps moyen par question" pour chaque quiz
- Le dashboard admin affiche les questions avec le temps moyen le plus élevé (points de difficulté)
- Les données sont agrégées (pas de logs individuels visibles sauf pour l'admin)
- Le tracking cesse si l'onglet est en arrière-plan (`visibilitychange`)

🏗 **Architecture**
- **Nouveau modèle** (`progress/models.py`) :
  ```
  TempsInteraction
  ├── user              FK → CustomUser (on_delete=CASCADE)
  ├── content_type      CharField(20) choices=['question', 'lecon']
  ├── object_id         PositiveIntegerField  # PK de la question ou lecon
  ├── duree_secondes    PositiveIntegerField
  ├── created_at        DateTimeField(auto_now_add)
  ├── index             (user, content_type, object_id)
  ```
- **Nouvelle vue** (`progress/views.py`) :
  - `enregistrer_temps(request)` — POST, `@login_required`, JSON body `{ content_type, object_id, duree_secondes }` ; crée ou incrémente le `TempsInteraction` ; valide `duree_secondes ≤ 3600` (cap anti-abus)
- **Nouvelle URL** (`progress/urls.py`) : `enregistrer-temps` (POST)
- **JavaScript inline** (dans `quiz.html` et `lecon.html`) :
  - Timer Alpine.js par question : `x-data="{ start: Date.now() }"` ; au changement de question, calcule le delta et l'envoie via `fetch()` au serveur
  - Timer de page pour les leçons : `visibilitychange` listener ; envoie le delta au serveur quand l'onglet perd le focus ou se ferme
- **Dashboard** : extension de `admin_analytics_view` et `espace_enseignant_view` (si #44 implémenté) avec graphiques Chart.js "temps moyen par question"
- **Fichiers impactés** : `progress/models.py`, `progress/views.py`, `progress/urls.py`, `templates/courses/quiz.html`, `templates/courses/lecon.html`, `templates/dashboard/admin_analytics.html`

🧪 **Tests**
- `test_enregistrer_temps_question` — POST JSON `{ content_type: 'question', object_id: 1, duree_secondes: 45 }` → status 201, `TempsInteraction` créée
- `test_enregistrer_temps_cap_3600` — POST `duree_secondes: 9999` → asserter que la valeur stockée est cappée à 3600
- `test_enregistrer_temps_requires_auth` — POST sans authentification → redirect login
- `test_enregistrer_temps_invalid_content_type` — POST `content_type: 'invalid'` → status 400
- `test_analytics_shows_avg_time` — créer 3 `TempsInteraction` pour une question → dashboard admin affiche la moyenne
- `test_temps_interaction_preview_mode_skipped` — en mode preview admin → POST ne crée pas de `TempsInteraction`

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : `enregistrer_temps` est `@login_required` et associe toujours au `request.user` — pas de paramètre `user_id` dans le body.
- **OWASP A04 (Insecure Design)** : le cap à 3600 secondes empêche l'inflation des données. Le `content_type` est validé contre les choices autorisés. L'`object_id` est vérifié en base (la question/leçon doit exister).
- **RGPD** : les données sont agrégées pour l'affichage. L'élève ne voit pas le tracking d'autrui. Le dashboard enseignant ne montre que des moyennes par question, pas par élève.
- **Rate limiting** : la vue accepte max 1 requête/seconde par utilisateur (debounce côté JS, validation côté serveur via cache key `temps_{user_id}`).

⚡ **Performance**
- Les requêtes de tracking sont des POST légers (~100 bytes JSON) — envoyés en arrière-plan via `fetch()` sans bloquer l'UI.
- L'agrégation dashboard utilise `Avg('duree_secondes')` avec `GROUP BY` — 1 requête SQL, pas de boucle Python.
- L'index `(user, content_type, object_id)` garantit des lookups rapides.
- Le debounce JS (1 req/sec max) limite la charge serveur côté client.
- Budget : +1 requête SQL par changement de question (en écriture) ; +1 agrégation pour le dashboard.

✅ **Definition of Done**
- Le temps par question est tracké pendant les quiz
- Le temps par leçon est tracké
- Le dashboard admin/enseignant affiche les agrégations
- Le tracking respecte la vie privée (RGPD compliant)
- Le cap anti-abus fonctionne (3600s max, debounce)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1, 2, 3)

---

### #46 — Cache Redis

**Description** : Intégrer Redis comme backend de cache Django via `django-redis` pour accélérer les rendus les plus coûteux. Les cibles principales sont : (1) les pages de leçons rendues (`Lecon.contenu` Markdown → HTML, incluant les SVGs LaTeX) — cachées par `cache.set(f'lecon_html_{lecon.pk}', rendered, timeout=3600)` ; (2) les résultats d'agrégation du dashboard (stats élève, analytics admin) — cachés 5 minutes ; (3) le catalogue public (liste des matières/chapitres/leçons par niveau) — caché 10 minutes. Le cache est invalidé au `save()` des modèles concernés via un signal `post_save`. L'instance Redis est ajoutée au `docker-compose.yml` en dev et configurée via `REDIS_URL` en production (Heroku Redis).

🎯 **Critères d'acceptation**
- `django-redis` est configuré comme `CACHES['default']` dans `base.py`
- Les pages de leçons sont servies depuis le cache Redis au second chargement (vérifiable via header `X-Cache: HIT` ou logs)
- Le dashboard élève et le dashboard analytics sont cachés 5 minutes
- Le catalogue public est caché 10 minutes
- Le cache d'une leçon est invalidé quand la `Lecon` est sauvegardée (`post_save`)
- Le cache du catalogue est invalidé quand un `Chapitre` ou une `Lecon` est ajouté/modifié
- `docker-compose.yml` inclut un service `redis`
- En production, `REDIS_URL` est lu via `decouple.config()`

🏗 **Architecture**
- **Settings** (`config/settings/base.py`) :
  ```python
  CACHES = {
      'default': {
          'BACKEND': 'django_redis.cache.RedisCache',
          'LOCATION': config('REDIS_URL', default='redis://redis:6379/0'),
          'OPTIONS': { 'CLIENT_CLASS': 'django_redis.client.DefaultClient' },
          'TIMEOUT': 300,
      }
  }
  ```
- **Vues modifiées** :
  - `lecon_view` : `cache.get(f'lecon_html_{lecon.pk}')` avant le rendu Markdown ; `cache.set()` après
  - `lecon_publique_view` : idem
  - `_dashboard_eleve` : `cache.get(f'dashboard_{user.pk}')` ; timeout 300s
  - `admin_analytics_view` : `cache.get('admin_analytics')` ; timeout 300s
  - `catalogue_matiere_view` : `cache.get(f'catalogue_{matiere.slug}_{niveau}')` ; timeout 600s
- **Signaux** (`courses/signals.py`, nouveau) :
  - `post_save` sur `Lecon` → `cache.delete(f'lecon_html_{instance.pk}')`
  - `post_save` sur `Chapitre` / `Lecon` → `cache.delete_pattern('catalogue_*')` (via `django-redis` native)
- **Docker** (`docker-compose.yml`) : ajout service `redis` (image `redis:7-alpine`)
- **Package** : `django-redis` ajouté à `requirements.txt`
- **Fichiers impactés** : `config/settings/base.py`, `courses/views.py`, `users/views.py`, `courses/signals.py` (nouveau), `courses/apps.py` (connect signals), `docker-compose.yml`, `requirements.txt`

🧪 **Tests**
- `test_lecon_view_cache_hit` — GET leçon 2 fois → la 2e fois, `cache.get()` retourne le HTML (mock cache pour vérifier)
- `test_lecon_save_invalidates_cache` — `cache.set('lecon_html_1', 'old')` ; `lecon.save()` → `cache.get('lecon_html_1')` retourne `None`
- `test_catalogue_cache_invalidated_on_new_lecon` — `cache.set('catalogue_physique_seconde', 'old')` ; créer nouvelle `Lecon` → cache catalogue invalidé
- `test_dashboard_cache_timeout` — vérifier que le cache dashboard est configuré avec timeout 300s
- `test_redis_fallback_if_unavailable` — si Redis est down, les vues fonctionnent toujours (pas de crash, juste pas de cache)

🔒 **Sécurité**
- **OWASP A05 (Security Misconfiguration)** : Redis en production (Heroku Redis) utilise TLS par défaut. En dev, Redis est sur le réseau Docker interne (pas exposé). Le `REDIS_URL` est stocké dans les variables d'environnement.
- **OWASP A01 (Broken Access Control)** : le cache des leçons est keyed par PK (pas par URL) — un changement de permissions (leçon rendue gratuite/premium) invalide correctement le cache via le signal `post_save`. Le cache du dashboard est keyed par `user.pk` — pas de fuite cross-user.
- **Cache poisoning** : les clés de cache sont construites côté serveur (pas de paramètre utilisateur dans la clé) — pas d'injection possible.

⚡ **Performance**
- Le rendu Markdown + LaTeX→SVG est l'opération la plus coûteuse (~200-500ms pour une leçon complexe). Le cache Redis réduit le TTFB à ~5-10ms pour les leçons déjà rendues.
- Le dashboard élève avec agrégations SQL (~50-100ms) est réduit à ~5ms via cache.
- Le catalogue public (~30-50ms) est réduit à ~5ms.
- Redis en mémoire : une leçon cachée ≈ 50-200 KB (HTML + SVGs inline). Pour 500 leçons → ~100 MB de RAM Redis — largement dans les limites.
- Le `delete_pattern('catalogue_*')` de `django-redis` utilise `SCAN` (non bloquant) — pas de lock Redis.
- Budget : -1 à -5 requêtes SQL par page (en cas de cache hit) ; +~100 MB RAM Redis.

✅ **Definition of Done**
- Redis est configuré en dev (Docker) et en prod (Heroku Redis)
- Les leçons, le dashboard et le catalogue sont cachés avec les TTL appropriés
- Les signaux invalident le cache au `save()` des modèles
- Les vues fonctionnent même si Redis est indisponible (graceful degradation)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 3, 6, 8)

---

### #47 — Gels de série (streak freezes)

**Description** : Introduire un système de "gels de série" (streak freezes) pour la gamification. Quand un élève manque un jour de connexion/activité, un gel est automatiquement consommé pour préserver sa série de jours consécutifs (streak) affichée sur le dashboard. Les gels sont obtenus gratuitement : 1 gel offert par semaine (dimanche), ou 1 gel bonus en atteignant un jalon de série (7, 30, 100 jours). Un nouveau modèle `UserInventory` stocke le nombre de gels disponibles et le nombre de gels utilisés. Le dashboard affiche le nombre de gels restants avec une icône ❄️. La consommation du gel est automatique lors du calcul de la série (dans la vue dashboard, quand un "trou" de 1 jour est détecté).

🎯 **Critères d'acceptation**
- L'élève reçoit 1 gel gratuit par semaine (dimanche, via commande de gestion ou signal)
- L'élève reçoit 1 gel bonus aux jalons de série : 7, 30, 100, 365 jours
- Quand l'élève manque 1 jour et a un gel disponible, le gel est consommé et la série est préservée
- Quand l'élève manque 1 jour sans gel, la série est réinitialisée à 0
- Le dashboard affiche le nombre de gels restants (❄️ × N)
- L'historique des gels (obtenus/consommés) est visible dans le profil de l'élève
- Max 5 gels stockables simultanément

🏗 **Architecture**
- **Nouveau modèle** (`progress/models.py`) :
  ```
  UserInventory
  ├── user              OneToOne → CustomUser (on_delete=CASCADE, related_name='inventaire')
  ├── streak_freezes    PositiveIntegerField(default=0)  # gels disponibles (max 5)
  ├── freezes_utilises  PositiveIntegerField(default=0)  # total gels consommés (historique)
  ├── dernier_gel_hebdo DateField(null, blank)  # date du dernier gel offert (anti-doublon)
  ├── created_at        DateTimeField(auto_now_add)
  ├── updated_at        DateTimeField(auto_now)
  ```
- **Logique de série modifiée** (`users/views.py`, `_dashboard_eleve`) :
  - Le calcul de streak existant vérifie si un jour a été manqué
  - Si oui et `inventaire.streak_freezes > 0` : décrémenter `streak_freezes`, incrémenter `freezes_utilises`, préserver le streak
  - Si oui et `streak_freezes == 0` : reset streak à 0
  - Jalons : après le calcul, si streak ∈ {7, 30, 100, 365} et pas déjà reçu → ajouter 1 gel (cap à 5)
- **Nouvelle commande de gestion** : `progress/management/commands/distribuer_gels.py` — exécutée 1×/semaine (dimanche) ; pour chaque élève avec `dernier_gel_hebdo` < today et `streak_freezes < 5` → incrémenter + mettre à jour `dernier_gel_hebdo`
- **Template modifié** : `templates/dashboard/eleve.html` — ajout section "❄️ Gels de série : N/5" avec description
- **Fichiers impactés** : `progress/models.py`, `users/views.py`, `templates/dashboard/eleve.html`, `progress/management/commands/distribuer_gels.py` (nouveau)

🧪 **Tests**
- `test_streak_freeze_consumed_on_missed_day` — élève avec streak=5 et 1 freeze, manque 1 jour → streak préservé, freezes=0
- `test_streak_reset_without_freeze` — élève avec streak=5 et 0 freeze, manque 1 jour → streak=0
- `test_streak_freeze_cap_at_5` — élève avec 5 freezes → `distribuer_gels` ne donne pas de 6e
- `test_milestone_bonus_freeze_at_7_days` — streak atteint 7 → inventaire gagne 1 freeze
- `test_milestone_bonus_not_given_twice` — streak à 7 puis revient à 7 après reset → pas de double bonus (basé sur un flag ou `dernier_jalon_atteint`)
- `test_distribuer_gels_weekly` — `call_command('distribuer_gels')` → chaque élève éligible gagne 1 freeze
- `test_distribuer_gels_idempotent_same_week` — appeler 2 fois dans la même semaine → 1 seul gel distribué (grâce à `dernier_gel_hebdo`)

🔒 **Sécurité**
- **OWASP A01 (Broken Access Control)** : le `UserInventory` est toujours accédé via `request.user.inventaire` — pas de paramètre `user_id` dans les URLs. L'élève ne peut pas modifier son inventaire directement.
- **OWASP A04 (Insecure Design)** : le cap à 5 gels est enforced en base (`min(streak_freezes + 1, 5)` dans le code). La distribution hebdomadaire est idempotente grâce au `dernier_gel_hebdo`.
- **Intégrité** : la consommation de gel est atomique (dans une transaction `select_for_update` pour éviter les race conditions en cas de double requête).

⚡ **Performance**
- Le calcul de streak + freeze est fait 1 seule fois au chargement du dashboard — +1 requête SQL (`UserInventory.objects.get_or_create(user=user)`).
- La commande `distribuer_gels` est un `UPDATE` bulk — 1 requête SQL pour tous les élèves éligibles.
- Le `select_for_update` sur `UserInventory` est de courte durée (< 1ms) — pas de contention.
- Budget : +1 requête SQL au dashboard ; +0 en navigation normale.

✅ **Definition of Done**
- Les gels sont distribués hebdomadairement et aux jalons de série
- Le gel est consommé automatiquement quand un jour est manqué
- Le cap à 5 gels fonctionne
- Le dashboard affiche les gels restants
- La distribution est idempotente
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (sections 1, 3, 7)

---

### 🏗 Architectural & Quality Standards (Phases 8–10)

#### 1. Intelligence Artificielle (Phase 8)

- **Isolation** : toute logique LLM est isolée dans `courses/ai_generation.py` et `courses/ai_tuteur.py` — les vues n'appellent que des fonctions wrapper. Cela permet de changer de provider (OpenAI → Anthropic → local) sans modifier les vues.
- **Async** : les appels API sont I/O-bound. Pour le tuteur (#39), les réponses sont streamées via SSE. Pour la génération (#40), les appels sont batch (commande de gestion) — pas de Celery requis initialement, mais le code est structuré pour migrer facilement vers des tasks Celery si le volume l'exige.
- **Tests** : **tous les tests mockent les appels API** (`unittest.mock.patch`) — aucun appel réel à OpenAI en CI. Les fixtures contiennent des réponses types pour chaque scénario (tuteur socratique, génération QCM, génération vrai/faux, génération texte libre).
- **Parsing** : les réponses JSON de l'IA sont validées via un parseur strict (Pydantic ou `json.loads` + validation manuelle) — jamais d'`eval()` ou d'exécution dynamique.
- **Rate limit** : les appels API sont cappés côté serveur (max 10 messages/question pour le tuteur, batch de 5 pour la génération) — anti-abus + contrôle des coûts.

#### 2. PWA & Offline (Phase 9)

- **Service Worker scope** : `sw.js` est servi à la racine (`/sw.js`) pour avoir le scope maximal. Si servi depuis `/static/sw.js`, le header `Service-Worker-Allowed: /` est requis.
- **Stratégies de cache** :
  - *Stale-While-Revalidate* : assets CDN (Tailwind, Alpine, HTMX, KaTeX) — sert le cache immédiatement, met à jour en arrière-plan
  - *Network-first* : pages HTML (leçons, quiz) — toujours tenter le réseau, fallback cache
  - *Cache-first* : images et SVGs LaTeX — statiques, pas besoin de revalidation
  - *Network-only* : POST (soumissions quiz, tracking temps) — pas de cache des mutations
- **Tests E2E** : les scénarios offline sont testés via Playwright avec `page.context.setOffline(true)`. Les tests unitaires Django ne couvrent pas le SW (code JS).
- **Versioning** : les caches sont nommés avec un suffixe version (`scienlycee-static-v1`). Le passage à `v2` dans le SW déclenche le nettoyage de `v1` dans l'événement `activate`.

#### 3. UGC & Cache Redis (Phase 10)

- **FK auteur** : `Lecon.auteur` est nullable (`SET_NULL`) — les leçons officielles (admin) ont `auteur=None`. Seules les leçons UGC (enseignant) ont un auteur. Ce champ sert de discriminant pour filtrer le contenu privé.
- **Sanitization XSS** : tout contenu UGC (Markdown enseignant) passe par `bleach.clean()` **avant stockage** — pas à chaque affichage. La whitelist de tags est restrictive (pas de `<script>`, `<iframe>`, `<style>`, `<form>`). Les attributs sont limités par tag.
- **Cache Redis — invalidation** : les signaux `post_save` sur `Lecon` et `Chapitre` invalident les clés concernées. Le pattern `cache.delete_pattern('catalogue_*')` (natif `django-redis`) utilise `SCAN` (non bloquant). En cas de doute, préférer l'invalidation agressive (supprimer trop plutôt que servir du stale).
- **Cache Redis — graceful degradation** : si Redis est indisponible, les vues fonctionnent normalement (pas de cache, requêtes SQL directes). Ceci est garanti par des `try/except` autour des appels `cache.get/set` ou par le fallback `DummyCache` en dev.
- **Tests invalidation** : chaque signal d'invalidation a un test dédié qui vérifie que `cache.get()` retourne `None` après le `save()` du modèle.

---

## Summary

| Phase | Tasks | Focus |
|-------|-------|-------|
| 1 | #1–#6 | Product & Proof — SEO hook, paywall, Stripe, password reset, error pages, CI |
| 2 | #7–#12 | Acquisition & First Revenue — landing page, analytics, social sharing, rate limiting, email verification |
| 3 | #13–#17 | Scaling Traffic — blog, partnerships, technical SEO, performance, referral |
| 4 | #18–#23 | Learning Experience — timed quizzes, instant feedback, difficulty, notes, glossary, interactive exercises |
| 5 | #24–#26 | Social & Gamification — leaderboard, study groups, badges |
| 6 | #27–#34 | Architecture & Housekeeping — completed infra & content tasks |
| 7 | #35–#38 | Tutorat, Calendrier & Facturation SAP — tutoring sessions, calendar, SAP billing |
| 8 | #39–#40 | Intelligence Artificielle — AI Socratic tutor, dynamic question generation |
| 9 | #41–#43 | PWA & Mobile — manifest/SW, offline mode, web push notifications |
| 10 | #44–#47 | UGC, Analytics & Performance — teacher content, time tracking, Redis cache, streak freezes |

**Total: 47 tasks across 10 phases.**

---

## Completed

- ~~Bind-mount source code in dev + `.dockerignore`~~
- ~~`CustomUser` model with email login~~
- ~~Matiere / Chapitre / Lecon / Quiz / Question hierarchy~~
- ~~Seed data management command (`seed_data`)~~
- ~~Admin preview mode (simulate student view per level)~~
- ~~Dark mode toggle (sun/moon) with `localStorage` persistence~~
- ~~Spaced repetition (Leitner 5-box system)~~
- ~~Chapter quiz with proportional difficulty selection~~
- ~~DRY quiz helpers (`_evaluer_reponses`, `_check_quiz_rate_limit`)~~
- ~~Password reset flow (Django built-in, French templates)~~
- ~~Custom error pages (404 extends base, 500 self-contained)~~
- ~~Automated tests (pytest 8.3, 208 tests) + CI (GitHub Actions)~~
- ~~Rate limiting (django-axes login + cache-based quiz)~~
- ~~Email verification on signup (signed tokens, 24h expiry)~~
- ~~Technical SEO (sitemaps for catalogue + free lessons)~~
- ~~Difficulty levels (`DifficulteChoices`: FACILE / MOYEN / DIFFICILE)~~
- ~~Lesson notes (`UserNote`, HTMX auto-save)~~
- ~~Open "hook" content (SEO & storefront — public catalogue, free lessons)~~
- ~~Full-text search (PostgreSQL `SearchVector` + `SearchRank`)~~
- ~~PDF export (LaTeX → DVI → dvisvgm → SVG, WeasyPrint)~~
- ~~Admin analytics (weak questions, completion %, pass rates)~~
- ~~CSV import (`import_questions` management command)~~
- ~~Health check endpoint (`/health/`)~~
- ~~Logging & Sentry integration~~
- ~~Student dashboard (progress bars, streak, Chart.js trend, revision CTA)~~
- ~~Seed physique seconde (Ch.1–Ch.8)~~
- ~~Seed chimie seconde (Ch.1–Ch.6)~~
- ~~Seed maths seconde (Ch.1–Ch.10)~~
- ~~Seed physique première (Ch.1–Ch.10)~~
- ~~Seed chimie première (Ch.1–Ch.8)~~
- ~~Seed maths première (Ch.1–Ch.12)~~
- ~~Chimie organique terminale (Ch.13)~~
