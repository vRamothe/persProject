# ScienceLycée — Unified Roadmap

> **Core rule:** No new "nice-to-have" features until Stripe is live and the first real sale is processed.

---

## Phase 1 — Product & Proof (Weeks 1–2)

*Goal: make the app sellable and prove demand with real users.*

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 1 | ~~**Open "hook" content (SEO & storefront)**~~ ✅ | Business | Sonnet | Slug-based public URLs (`/cours/<matiere>/`, `/cours/<matiere>/<niveau>/<chapitre>/<lecon>/`), `gratuit` BooleanField, catalogue + public lesson templates, SEO meta, data migration. |
| 2 | **Visual paywall** | Business | Sonnet | Premium lessons stay visible with a 🔒 icon. On click → modal paywall ("Unlock the full Bac program") with pricing tiers — not a login redirect. |
| 3 | **Stripe integration** | Business | **Opus** | Stripe Checkout Sessions or Elements in Django. Two tiers: Monthly (~€19/mo) and Annual (~€119/yr). Webhook to activate/deactivate subscriptions. |
| 4 | ~~**Password reset flow**~~ ✅ | Tech | Sonnet | Django built-in `PasswordResetView` flow with French templates, console backend (dev), SMTP/Brevo (prod), "Mot de passe oublié ?" link on login page. |
| 5 | ~~**Custom error pages (404, 500)**~~ ✅ | Tech | Sonnet | Branded 404 (extends base.html) and 500 (self-contained, no DB) templates. `handler404`/`handler500` in config/urls.py. |
| 6 | ~~**Automated tests + CI**~~ ✅ | Tech | Sonnet | 33 pytest tests (access control, quiz scoring, chapter unlock, Leitner, slugs, public pages). GitHub Actions CI with PostgreSQL service. |

## Phase 2 — Acquisition & First Revenue (Weeks 3–4)

*Goal: get paying users and build trust.*

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 7 | **Beta test with current students** | Business | — | Create free accounts for private tutoring students. Onboard parents for feedback and bug hunting. |
| 8 | **Social proof on landing page** | Business | Sonnet | Collect written testimonials from beta students/parents. Display with trust badge ("Designed by a certified local teacher"). |
| 9 | **"Hybrid Bac Sprint" upsell** | Business | — | High-margin package (~€89/month): unlimited app access + 1h/month 1-on-1 video coaching to review analytics and target weak points. |
| 10 | **Local marketing (Grasse & 06)** | Business | — | Flyers with QR code to a high-value free lesson. Distribute at Tocqueville, Amiral de Grasse. Post in local Facebook parent groups. |
| 11 | ~~**Rate limiting on login & quiz**~~ ✅ | Tech | Sonnet | `django-axes` on `ConnexionView.post`; cache-based 30 req/min on `soumettre_quiz` + `soumettre_revisions` via `_check_quiz_rate_limit()`. Returns 429. |
| 12 | ~~**Email verification on signup**~~ ✅ | Tech | Sonnet | `is_active=False` on register; signed token (`django.core.signing`); `verifier_email_view` activates + auto-logins; 24h expiry. |
| 13 | **Query optimization** | Tech | **Opus** | `_dashboard_eleve` has N+1 per matière; `matieres_view` N+1 on progressions. Use `Prefetch`, `annotate()`, `select_related`. |

## Phase 3 — Scaling Traffic (Month 2+)

*Goal: grow organic reach and reduce churn.*

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 14 | **Snackable social content** | Business | — | 60-second TikTok/IG Shorts solving classic exam problems. App link in bio. |
| 15 | ~~**Technical SEO (sitemaps)**~~ ✅ | Tech | Sonnet | `CatalogueSitemap` + `LeconPubliqueSitemap` (gratuit=True only) in `courses/sitemaps.py`. `/sitemap.xml` registered in `config/urls.py`. |
| 16 | **Parent retention loop** | Business | Sonnet | Automated weekly email (or dashboard view) for parents summarizing the student's activity ("Leo completed 15 exercises this week"). |
| 17 | **Mobile responsiveness audit** | Tech | Sonnet | Sidebar is desktop-first; quiz forms with math equations overflow on phones. Focused mobile pass needed. |

## Phase 4 — Learning Experience Improvements

*Goal: make the product stickier and more effective.*

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 18 | **Timed quizzes** | Feature | Sonnet | Optional timer to simulate bac exam conditions. `duree_limite` field on Quiz. |
| 19 | **Instant feedback on wrong answers** | Feature | Sonnet | Show correction per question immediately instead of all at the end (configurable). |
| 20 | ~~**Difficulty levels on questions**~~ ✅ | Feature | Sonnet | `DifficulteChoices` (FACILE/MOYEN/DIFFICILE) + `Question.difficulte` field (default MOYEN). `_selectionner_questions_chapitre()` guarantees 4 facile + 4 moyen + 2 difficile per chapter quiz. |
| 21 | ~~**Lesson bookmarks / notes**~~ ✅ | Feature | Sonnet | `UserNote(user, lecon, contenu, created_at, updated_at)` model; HTMX auto-save panel in `lecon.html`; `sauvegarder_note` view with upsert. |
| 22 | **Glossary / formula sheet** | Feature | Sonnet | Searchable reference page per matière, auto-extracted from lesson content. |
| 23 | **Interactive exercises** | Feature | **Opus** | Drag-and-drop, fill-in-the-blank, matching columns via Alpine.js `x-data` + new question type. |

## Phase 5 — Social / Gamification

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 24 | **Badges / achievements** | Feature | Sonnet | "First quiz passed", "10-day streak", "Perfect chapter score". Simple model + display. |
| 25 | **Leaderboard** | Feature | Sonnet | Anonymous or opt-in ranking per classe/niveau. |
| 26 | **Teacher notifications** | Feature | Sonnet | Email or in-app alert when a student struggles (3+ failed attempts on a chapter quiz). |

## Phase 6 — Architecture & Housekeeping

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 27 | ~~**DRY quiz submission logic**~~ ✅ | Refactor | Opus | `_evaluer_reponses(questions, post_data)` + `_check_quiz_rate_limit(user_id)` extracted; used by `soumettre_quiz`, `soumettre_quiz_chapitre`, `soumettre_revisions`. |
| 28 | ~~**Content admin UX — bulk import**~~ ✅ | Tool | Sonnet | `import_questions` management command; CSV with `quiz_lecon_slug`, `texte`, `type`, `reponse_correcte`, `options` (JSON), `tolerances` (JSON), `difficulte`; `--dry-run` flag. |
| 29 | ~~**Admin content analytics**~~ ✅ | Feature | Sonnet | `admin_analytics_view` at `/admin-panel/analytics/`; weak questions (<40% success), lesson completion %, chapter quiz pass rates. |
| 30 | ~~**Full-text search**~~ ✅ | Feature | Sonnet | `recherche_view` at `/cours/recherche/`; PostgreSQL `SearchVector` + `SearchRank` on `Lecon.titre` + `contenu`; niveau-filtered for students; top 20 results. |
| 31 | ~~**PDF export of lessons**~~ ✅ | Feature | Sonnet | `lecon_pdf_view` at `/cours/lecon/<pk>/pdf/`; LaTeX→DVI→dvisvgm→SVG pipeline for native-quality math rendering; WeasyPrint renders `lecon_pdf.html` with inline SVG equations. |
| 32 | **Accessibility (a11y)** | Tech | **Opus** | `aria-label`, focus management after HTMX swaps, `<fieldset>`/`<legend>` on quiz radios. |
| 33 | ~~**Logging & monitoring**~~ ✅ | Infra | Sonnet | Full Django `LOGGING` dict in `base.py`; Sentry (`sentry-sdk[django]`) init in `production.py` via `SENTRY_DSN` env var; `health_view` at `/health/` returns `{"status":"ok"}`. |
| 34 | ~~**Database backups**~~ ✅ | Infra | Sonnet | `heroku pg:backups:schedule DATABASE_URL --at '02:00 UTC'`; restore with `heroku pg:backups:restore`. No code changes needed. |

## Phase 7 — Tutorat, Calendrier & Facturation SAP

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 35 | **Système de Réservation** | Feature | Opus | Demande de cours avec double-validation (enseignant + élève/parent) obligatoire pour créer l'événement. États : `En attente`, `Validé`, `Annulé`. |
| 36 | **Stripe Pre-auth & Capture** | Business | Opus | Paiement par carte requis à la réservation (`capture_method: 'manual'`). Le débit réel (Capture) n'a lieu qu'après la double-validation. |
| 37 | **Sync Calendrier** | Feature | Sonnet | Génération de flux `.ics` dynamiques (ou API OAuth) compatibles Google Agenda, Apple Calendar, Outlook. |
| 38 | **Facturation SAP (Défiscalisation)** | Business | Sonnet | PDF généré via WeasyPrint avec mentions légales "Service à la Personne" (50% crédit d'impôt). Envoi auto par email (Parent, Élève, Enseignant). |

## Phase 8 — Intelligence Artificielle & Adaptive Learning

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 39 | **Tuteur IA "Socratique"** | Feature | Opus | Chatbot contextuel (OpenAI/Anthropic) sur les quiz échoués. Guide l'élève sans donner la réponse. Modèle `AIAssistanceLog`. |
| 40 | **Génération dynamique de questions** | Feature | Opus | Variations générées par IA des énoncés (chiffres, prénoms variables) stockées comme variantes dans `QuestionVariant` (Système Leitner résilient). |

## Phase 9 — PWA, Offline & Mobile Experience

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 41 | **Progressive Web App (PWA)** | Tech | Sonnet | `manifest.json` et Service Worker (`sw.js`). Rendre l'app installable (A2HS) sur iOS/Android. |
| 42 | **Mode Hors-Ligne (Offline)** | Tech | Sonnet | Mise en cache (Cache API) via Service Worker des leçons textuelles et SVGs LaTeX pour lecture hors connexion. |
| 43 | **Web Push Notifications** | Feature | Sonnet | Implémentation de clés VAPID pour l'envoi de notifications push (rappels de révisions Leitner) sur mobile et bureau. |

## Phase 10 — UGC Enseignants, Analytics & Performance

| # | Task | Type | LLM | Detail |
|---|------|------|-----|--------|
| 44 | **Création de contenu privé (UGC)** | Feature | Opus | Espace Prof pour créer leçons/quiz personnalisés. Visibles uniquement par les élèves liés. |
| 45 | **Analytics Granulaires (Temps)** | Feature | Sonnet | Tracking JS du temps passé par question, envoyé via HTMX/Beacon et agrégé pour le dashboard enseignant. |
| 46 | **Cache Redis (LaTeX/MD)** | Tech | Opus | Implémentation de `django-redis`. Mise en cache des rendus lourds HTML/SVG des leçons. |
| 47 | **Gels de série (Streak Freezes)** | Feature | Sonnet | Économie virtuelle (points gagnés aux quiz) pour acheter un droit à l'erreur sur les streaks. Modèle `UserInventory`. |

---

## 🏗 Architectural & Quality Standards (Phases 8-10)

### 1. Intelligence Artificielle (Phase 8)
- **Architecture** : Isoler la logique LLM dans un service dédié (ex: `ai_tutor/services.py`). Ne pas bloquer le thread web principal : utiliser `Celery` ou un worker asynchrone pour la génération dynamique de questions par lots.
- **Tests** : Mocker systématiquement les appels API externes avec `responses` ou `unittest.mock`. Les tests CI ne doivent jamais faire de vrais appels OpenAI/Anthropic.
- **Sécurité & Qualité** : Ne jamais faire confiance à l'output d'un LLM. Mettre en place un parseur strict (Pydantic) pour s'assurer du format des questions générées. Rate limiting strict (OWASP) pour éviter l'explosion des coûts d'API (ex: max 5 appels Tuteur IA / heure / élève).

### 2. PWA & Offline (Phase 9)
- **Architecture** : Le fichier `sw.js` (Service Worker) doit être servi à la racine `/sw.js` (via une configuration URL spécifique de Django) pour avoir la portée (scope) sur tout le site.
- **Tests** : L'utilisation de Service Workers ne peut pas être testée via de simples requêtes HTTP Django (pytest). Des tests End-to-End (E2E) via Playwright ou Cypress seront nécessaires pour valider le comportement hors-ligne.
- **Sécurité & Qualité** : Stratégie de cache claire. Utiliser "Stale-While-Revalidate" pour les assets statiques (CSS/JS) et "Network-First" pour les soumissions de quiz. Prévoir une logique de file d'attente (IndexedDB) pour les réponses aux quiz soumises hors-ligne.

### 3. UGC Enseignants & Cache Redis (Phase 10)
- **Architecture** : Extension des modèles `Lecon` et `Quiz` avec une ForeignKey `auteur` (nullable pour le contenu officiel de l'admin) et un boolean `is_private`.
- **Sécurité Critique (OWASP A03)** : L'utilisation de la librairie `bleach` est **obligatoire** sur TOUT le contenu Markdown saisi par les enseignants avant l'enregistrement en base de données pour neutraliser tout risque d'attaque XSS (cross-site scripting).
- **Tests & Cache** : Mettre en place des tests d'invalidation de cache. Lorsqu'une leçon est mise à jour (via un signal `post_save`), le fragment en cache (Redis) doit être systématiquement purgé pour éviter de servir du contenu obsolète.

---

## Completed

- ~~Bind-mount source code in dev + `.dockerignore`~~ — Bind mount, gunicorn `--reload`, `.dockerignore` added
- ~~Spaced repetition / revision mode~~ — Leitner box system with `UserQuestionHistorique` model, "Révisions" page
- ~~Progress dashboard with analytics~~ — Per-subject stats, streak tracking, score trend chart, weak areas
- ~~Open "hook" content (SEO & storefront)~~ — Public catalogue & free lessons with slug URLs, `gratuit` field, SEO meta tags, data migration for slugs
- ~~Rate limiting~~ (#11) — `django-axes` on login; cache-based 30 req/min on quiz endpoints
- ~~Email verification~~ (#12) — `is_active=False` on register; signed token; 24h expiry; auto-login on verification
- ~~Technical SEO / sitemaps~~ (#15) — `CatalogueSitemap` + `LeconPubliqueSitemap`; `/sitemap.xml`
- ~~Difficulty levels~~ (#20) — `Question.difficulte` field; balanced chapter quiz (4/4/2) via `_selectionner_questions_chapitre()`
- ~~Lesson notes~~ (#21) — `UserNote` model; HTMX auto-save in lesson view
- ~~DRY quiz logic~~ (#27) — `_evaluer_reponses()` + `_check_quiz_rate_limit()` helpers
- ~~Bulk import~~ (#28) — `import_questions` management command (CSV + `--dry-run`)
- ~~Admin analytics~~ (#29) — weak questions, lesson completion, chapter quiz pass rates
- ~~Full-text search~~ (#30) — PostgreSQL `SearchVector` + `SearchRank` at `/cours/recherche/`
- ~~PDF export~~ (#31) — WeasyPrint at `/cours/lecon/<pk>/pdf/` with LaTeX→SVG math rendering (TeX Live + dvisvgm)
- ~~Logging & monitoring~~ (#33) — Django `LOGGING`, Sentry (prod), `/health/` endpoint
- ~~Database backups~~ (#34) — Heroku `pg:backups:schedule`
- ~~Full curriculum content seeding~~ — All 9 seed commands covering 3 subjects × 3 levels with complete chapter+lesson+quiz content: 283 quizzes, 3168 questions across 283 lessons. Bug fixes: `'choix'→'options'` (61q), text `reponse_correcte`→index (59q), missing `difficulte` added (268q). Commands: `seed_chimie_seconde` (11ch), `seed_physique_seconde` (8ch), `seed_maths_seconde` (13ch), `seed_chimie_premiere` (10ch), `seed_physique_premiere` (9ch), `seed_maths_premiere` (9ch), `seed_data`+`seed_content` (Terminale: 42ch).
- ~~Registration bug fixes~~ — (1) `_envoyer_email_verification()` wrapped in try/except to prevent 500 on SMTP failure, (2) `InscriptionForm.save()` now assigns `user.niveau` from form data (was NULL → students saw no courses)
- ~~Heroku static files fix~~ — `collectstatic` moved from release phase (ephemeral dyno) to Dockerfile build stage; Django admin CSS/JS now correctly served in production
- ~~Seed pipeline fix~~ — Added all 6 seconde/première seed commands to `heroku-release.sh` and `entrypoint.sh`; emptied stale seconde/première stubs from `seed_content.py`; switched 5 seed commands from `get_or_create` to `update_or_create` with explicit `slug` to prevent UniqueViolation on `(matiere, niveau, slug)`
- ~~Chimie organique terminale (Ch.13)~~ — New `seed_chimie_orga_terminale` command: 3 leçons (représentations, nomenclature IUPAC, isomérie), 60 questions. Based on Chapitre_21 curriculum documents.