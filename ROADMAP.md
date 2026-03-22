# ScienceLycée — Unified Roadmap

> **Core rule:** No new "nice-to-have" features until Stripe is live and the first real sale is processed.

---

## Phase 1 — Product & Proof (Weeks 1–2)

*Goal: make the app sellable and prove demand with real users.*

| # | Task | Type | Detail |
|---|------|------|--------|
| 1 | **Open "hook" content (SEO & storefront)** | Business | Remove `@login_required` on the first lesson of every chapter. Add slug-based, SEO-friendly URLs so Googlebot can index free content. |
| 2 | **Visual paywall** | Business | Premium lessons stay visible with a 🔒 icon. On click → modal paywall ("Unlock the full Bac program") with pricing tiers — not a login redirect. |
| 3 | **Stripe integration** | Business | Stripe Checkout Sessions or Elements in Django. Two tiers: Monthly (~€19/mo) and Annual (~€119/yr). Webhook to activate/deactivate subscriptions. |
| 4 | **Password reset flow** | Tech | No reset exists — students are locked out. Add Django's built-in `PasswordResetView` flow with email sending. |
| 5 | **Custom error pages (404, 500)** | Tech | No custom templates — users see Django's default page. Add branded error pages. |
| 6 | **Automated tests + CI** | Tech | Zero tests exist. Add model tests (Leitner, chapter unlock), view tests (access control, quiz scoring, preview mode), GitHub Actions pipeline. |

## Phase 2 — Acquisition & First Revenue (Weeks 3–4)

*Goal: get paying users and build trust.*

| # | Task | Type | Detail |
|---|------|------|--------|
| 7 | **Beta test with current students** | Business | Create free accounts for private tutoring students. Onboard parents for feedback and bug hunting. |
| 8 | **Social proof on landing page** | Business | Collect written testimonials from beta students/parents. Display with trust badge ("Designed by a certified local teacher"). |
| 9 | **"Hybrid Bac Sprint" upsell** | Business | High-margin package (~€89/month): unlimited app access + 1h/month 1-on-1 video coaching to review analytics and target weak points. |
| 10 | **Local marketing (Grasse & 06)** | Business | Flyers with QR code to a high-value free lesson. Distribute at Tocqueville, Amiral de Grasse. Post in local Facebook parent groups. |
| 11 | **Rate limiting on login & quiz** | Tech | No throttling on `ConnexionView.post` or `soumettre_quiz`. Add `django-axes` or rate-limit decorator against brute-force/spam. |
| 12 | **Email verification on signup** | Tech | Anyone can register with a fake email. Add token-based verification to prevent dummy accounts. |
| 13 | **Query optimization** | Tech | `_dashboard_eleve` has N+1 per matière; `matieres_view` N+1 on progressions. Use `Prefetch`, `annotate()`, `select_related`. |

## Phase 3 — Scaling Traffic (Month 2+)

*Goal: grow organic reach and reduce churn.*

| # | Task | Type | Detail |
|---|------|------|--------|
| 14 | **Snackable social content** | Business | 60-second TikTok/IG Shorts solving classic exam problems. App link in bio. |
| 15 | **Technical SEO (sitemaps)** | Tech | `django.contrib.sitemaps` → dynamic `sitemap.xml` with all free lessons. Submit to Google Search Console. |
| 16 | **Parent retention loop** | Business | Automated weekly email (or dashboard view) for parents summarizing the student's activity ("Leo completed 15 exercises this week"). |
| 17 | **Mobile responsiveness audit** | Tech | Sidebar is desktop-first; quiz forms with math equations overflow on phones. Focused mobile pass needed. |

## Phase 4 — Learning Experience Improvements

*Goal: make the product stickier and more effective.*

| # | Task | Type | Detail |
|---|------|------|--------|
| 18 | **Timed quizzes** | Feature | Optional timer to simulate bac exam conditions. `duree_limite` field on Quiz. |
| 19 | **Instant feedback on wrong answers** | Feature | Show correction per question immediately instead of all at the end (configurable). |
| 20 | **Difficulty levels on questions** | Feature | Tag questions facile/moyen/difficile. Chapter quiz guarantees balanced mix. |
| 21 | **Lesson bookmarks / notes** | Feature | `UserNote(user, lecon, texte, position)` model for student annotations. |
| 22 | **Glossary / formula sheet** | Feature | Searchable reference page per matière, auto-extracted from lesson content. |
| 23 | **Interactive exercises** | Feature | Drag-and-drop, fill-in-the-blank, matching columns via Alpine.js `x-data` + new question type. |

## Phase 5 — Social / Gamification

| # | Task | Type | Detail |
|---|------|------|--------|
| 24 | **Badges / achievements** | Feature | "First quiz passed", "10-day streak", "Perfect chapter score". Simple model + display. |
| 25 | **Leaderboard** | Feature | Anonymous or opt-in ranking per classe/niveau. |
| 26 | **Teacher notifications** | Feature | Email or in-app alert when a student struggles (3+ failed attempts on a chapter quiz). |

## Phase 6 — Architecture & Housekeeping

| # | Task | Type | Detail |
|---|------|------|--------|
| 27 | **DRY quiz submission logic** | Refactor | `soumettre_quiz` and `soumettre_quiz_chapitre` share ~80% code. Extract `_evaluer_reponses()`. |
| 28 | **Content admin UX — bulk import** | Tool | CSV/JSON bulk import for questions (with tolerances, options). |
| 29 | **Admin content analytics** | Feature | Question success rates, lesson drop-off rates — helps improve content quality. |
| 30 | **Full-text search** | Feature | PostgreSQL `SearchVector` + `SearchRank`, built into Django. |
| 31 | **PDF export of lessons** | Feature | Offline access via `weasyprint` rendering Markdown HTML to PDF. |
| 32 | **Accessibility (a11y)** | Tech | `aria-label`, focus management after HTMX swaps, `<fieldset>`/`<legend>` on quiz radios. |
| 33 | **Logging & monitoring** | Infra | Structured logging, Sentry, `/health/` endpoint. |
| 34 | **Database backups** | Infra | Schedule automated Postgres backups (Heroku `pg:backups:schedule` or equivalent). |

---

## Completed

- ~~Bind-mount source code in dev + `.dockerignore`~~ — Bind mount, gunicorn `--reload`, `.dockerignore` added
- ~~Spaced repetition / revision mode~~ — Leitner box system with `UserQuestionHistorique` model, "Révisions" page
- ~~Progress dashboard with analytics~~ — Per-subject stats, streak tracking, score trend chart, weak areas
