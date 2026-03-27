# ScienceLycée — Workspace Instructions

## Project Overview
ScienceLycée is a French high-school e-learning platform for Physics, Chemistry, and Math (Seconde / Première / Terminale). It is a **Django 5 monolith** with server-side rendering via HTMX + Alpine.js + Tailwind CSS (CDN). No React, no DRF.

## Stack
| Layer | Technology |
|-------|------------|
| Backend | Python 3.12, Django 5.1, PostgreSQL 16 — `django-axes` (rate limiting), `weasyprint` (PDF), `sentry-sdk[django]` (monitoring), TeX Live + `dvisvgm` (LaTeX→SVG for PDF math) |
| Frontend | Tailwind CSS (CDN, `darkMode: 'class'`), HTMX 1.9, Alpine.js 3.14, Chart.js 4.4 (dashboard) |
| Math rendering | KaTeX 0.16.9 (auto-render, web) · TeX Live + dvisvgm (LaTeX→SVG, PDF export) |
| Content | Markdown rendered server-side via `python-markdown` with LaTeX protection |
| Auth | Custom `users.CustomUser` (email-based, `AUTH_USER_MODEL`) |
| Deploy | Docker Compose (dev) — `db` (postgres), `web` (gunicorn + `--reload`), `nginx` · Heroku (prod) — `heroku.yml` container deploy · Dockerfile includes `texlive-latex-base texlive-latex-recommended texlive-fonts-recommended dvisvgm` for PDF math |
| Config | `python-decouple` + `.env`, settings split: `base / development / production` |

## Django App Structure
```
backend/
  app/           # Unused scaffolding — do not add code here
  config/        # urls.py, views.py, wsgi.py, settings/{base,development,production}.py
  users/         # CustomUser, ConnexionLog, managers, forms, views, urls
  courses/       # Matiere > Chapitre > Lecon > Quiz > Question hierarchy + revision views
  progress/      # UserProgression, UserQuizResultat, UserChapitreQuizResultat, ChapitreDebloque, UserQuestionHistorique
  templates/     # All HTML — base.html + per-app subdirs
  static/        # Static assets (currently empty beyond README)
```

## Key Models
- `users.CustomUser` — email login, `role` (admin|eleve), `niveau` (seconde|premiere|terminale)
- `users.ConnexionLog` — logs each successful login (user, timestamp, ip)
- `courses.Matiere` — physique / chimie / mathematiques; has `slug` (unique, auto-populated from `nom`)
- `courses.Chapitre` — belongs to Matiere + niveau, has `ordre`, `score_minimum_deblocage`, and `slug` (auto-populated from `titre`, unique per matiere+niveau)
- `courses.Lecon` — belongs to Chapitre, `contenu` in Markdown, optional `video_youtube_url` or `video_fichier`; has `slug` (auto-populated from `titre`, unique per chapitre) and `gratuit` BooleanField (marks lesson as publicly accessible without login)
- `courses.Quiz` / `courses.Question` — QCM, Vrai/Faux, or **Texte libre** linked to a Lecon
  - `Question.type` choices: `qcm`, `vrai_faux`, `texte_libre`
  - `Question.tolerances` (JSONField, optional) — accepted alternative answers for `texte_libre`, e.g. `["azote", "N2"]`; comparison is case-insensitive
  - `Question.difficulte` — `DifficulteChoices` (FACILE/MOYEN/DIFFICILE), default MOYEN
- `progress.UserNote` — per (user, lecon) student annotation: `contenu` (max 2000 chars), `created_at`, `updated_at`; `unique_together = [("user", "lecon")]`
- `progress.UserProgression` — per (user, lecon) statut: non_commence / en_cours / termine
- `progress.UserQuizResultat` — best score, nb_tentatives, passe bool (per lesson quiz)
- `progress.UserChapitreQuizResultat` — best score, nb_tentatives, passe bool (per chapter quiz, ≥80% to pass)
- `progress.ChapitreDebloque` — unlocking mechanism (requires passing the chapter quiz at ≥80%)
- `progress.UserQuestionHistorique` — Leitner spaced-repetition tracking per (user, question): boite (1–5), prochaine_revision, nb_bonnes, nb_total

## Chapter Unlock Flow
1. Student completes all lessons in a chapter
2. Chapter quiz becomes available — 10 questions selected by `_selectionner_questions_chapitre()` in `courses/views.py` (proportional difficulty: 4 facile + 4 moyen + 2 difficile; falls back to available pool if smaller)
3. Student must score ≥80% on the chapter quiz to unlock the next chapter
4. `_verifier_deblocage_chapitre_suivant()` in `progress/views.py` checks for a passing `UserChapitreQuizResultat`

## Spaced Repetition (Leitner System)
- Every quiz answer (lesson quiz, chapter quiz, revision quiz) creates/updates a `UserQuestionHistorique`
- 5 boxes with intervals: `{1: 1d, 2: 3d, 3: 7d, 4: 14d, 5: 30d}`
- Correct → box+1 (max 5); Wrong → box=1
- "Révisions" page (`revisions_view` in `courses/views.py`) shows due questions, Leitner stats, and a revision quiz form
- Helper: `_enregistrer_historique_questions()` in `progress/views.py`

## Student Dashboard
- Per-subject progress bars (lessons done / total, average score)
- Streak counter (consecutive days with activity from progressions + connexion logs)
- 30-day score trend chart (Chart.js, inline JS)
- Revision CTA with count of due questions
- Weak chapters section (avg score < 70%)

## Colour System (per subject)
```python
MATIERE_COULEURS = {
  "physique":      blue-600 family
  "chimie":        emerald-600 family
  "mathematiques": purple-600 family
}
```
Always respect this mapping when adding UI for subject-specific elements.

## Template Rules
- All pages extend `base.html`
- Authenticated pages use `{% block content %}` + `{% block page_title %}`
- Non-authenticated pages use `{% block full_content %}` (full page, no sidebar)
- Public SEO pages (catalogue, free lessons) use `{% block full_content %}` + `{% block extra_head %}` to set `<meta name="robots" content="index, follow">` (base.html defaults to `noindex, nofollow`)
- **Never** add dark-mode Tailwind classes in child templates — dark mode is handled globally in `base.html` via `html.dark { }` CSS overrides
- Dark mode toggle (sun/moon button) lives in the top-right of the header; theme is persisted in `localStorage`; the `<html>` tag gets/loses the `dark` class; initialisation script in `<head>` prevents flash-of-unstyled-content

## Admin Preview Mode
Admins can simulate the exact student view for any level without creating dummy accounts:
- Entry points: dashboard card + sidebar section in `base.html`
- Views: `preview_niveau_view(request, niveau)` and `exit_preview_view(request)` in `users/views.py`
- URLs: `preview_niveau` (str:niveau) and `exit_preview` in `users/urls.py`
- Session key: `request.session["preview_niveau"]` — `"seconde"` | `"premiere"` | `"terminale"` | absent
- `matieres_view` and `lecon_view` in `courses/views.py` already respect this session key
- A yellow banner is shown on every page while preview is active; progress writes are skipped in preview mode

## URL Map
```
/                                          → home (public accueil for anon, redirect to tableau_de_bord for auth)
/health/                                   → health_check (JSON {"status":"ok"}, no login required)
/sitemap.xml                               → sitemap (public, catalogue + free lessons)
/connexion/                                → connexion
/inscription/                              → inscription
/inscription/confirmation/                 → inscription_confirmation
/verifier-email/<str:token>/               → verifier_email (activates account from signed token)
/deconnexion/                              → deconnexion
/tableau-de-bord/                          → tableau_de_bord
/profil/                                   → profil
/mot-de-passe-oublie/                      → password_reset
/mot-de-passe-oublie/envoye/               → password_reset_done
/reinitialiser/<uidb64>/<token>/           → password_reset_confirm
/reinitialiser/termine/                    → password_reset_complete
/admin-panel/utilisateurs/                 → admin_utilisateurs
/admin-panel/utilisateurs/<id>/            → admin_eleve_detail
/admin-panel/utilisateurs/<id>/toggle/     → admin_toggle_actif
/admin-panel/utilisateurs/<id>/chapitre/<id>/toggle/ → admin_toggle_chapitre
/admin-panel/preview/<niveau>/             → preview_niveau
/admin-panel/preview/exit/                 → exit_preview
/admin-panel/analytics/                    → admin_analytics (admin only)
/cours/                                    → matieres
/cours/recherche/                          → recherche (login required; PostgreSQL full-text)
/cours/revisions/                          → revisions
/cours/revisions/soumettre/                → soumettre_revisions
/cours/chapitre/<pk>/                      → chapitre
/cours/chapitre/<pk>/quiz/                 → quiz_chapitre
/cours/lecon/<pk>/                         → lecon
/cours/lecon/<pk>/quiz/                    → quiz
/cours/lecon/<pk>/pdf/                     → lecon_pdf (WeasyPrint, login required)
/cours/<matiere_slug>/                     → catalogue_matiere (public, no login)
/cours/<matiere_slug>/<niveau>/<chapitre_slug>/<lecon_slug>/
                                           → lecon_publique (public if gratuit=True, else redirect to login)
/progression/terminer/<pk>/                → terminer_lecon
/progression/quiz/<pk>/soumettre/          → soumettre_quiz
/progression/quiz-chapitre/<pk>/soumettre/ → soumettre_quiz_chapitre
/progression/note/<lecon_pk>/sauvegarder/  → sauvegarder_note (HTMX POST, upsert UserNote)
```

## Error Pages
- `handler404` → `config.views.custom_404` renders `templates/404.html` (extends `base.html`)
- `handler500` → `config.views.custom_500` renders `templates/500.html` (self-contained, no DB or template inheritance)

## Password Reset
Uses Django's built-in `PasswordResetView` flow with French templates in `templates/registration/`. Console email backend in dev, Brevo SMTP in production. Settings in `config/settings/development.py` and `production.py`.

## Testing
- **Stack**: `pytest` 8.3 + `pytest-django` 4.9, config in `backend/pytest.ini`; 80 tests
- **Test files**: `users/tests.py`, `courses/tests.py`, `progress/tests.py`
- **Run locally**: `docker compose run --rm --entrypoint pytest web -v --tb=short`
- **CI**: GitHub Actions (`.github/workflows/ci.yml`) — runs on push/PR to `main` with PostgreSQL 16 service container
- **⚠️ Important**: always use `client.force_login(user)` in tests — `client.login(email=, password=)` fails with `AxesBackendRequestParameterRequired` because `django-axes` requires a request object in `authenticate()`

## Dev Workflow
```bash
# Start everything (bind-mount + gunicorn --reload for hot reloading)
docker compose up --build -d

# Check logs
docker compose logs -f web

# Run management commands (bypassing entrypoint)
docker compose run --rm --entrypoint python web manage.py <command>

# Generate migrations (mount volume so files persist)
docker compose run --rm --user root -v $(pwd)/backend:/app --entrypoint python web manage.py makemigrations

# Shell
docker compose exec web python manage.py shell
```

## Seed Data
Full curriculum content is seeded via dedicated management commands per subject and level:

| Command | Matière | Niveau | Chapitres | Leçons | Questions |
|---------|---------|--------|-----------|--------|-----------|
| `seed_chimie_seconde` | chimie | seconde | 11 | 22 | 440 |
| `seed_physique_seconde` | physique | seconde | 8 | 16 | 320 |
| `seed_maths_seconde` | mathematiques | seconde | 13 | 26 | 520 |
| `seed_chimie_premiere` | chimie | premiere | 10 | 21 | 420 |
| `seed_physique_premiere` | physique | premiere | 9 | 18 | 360 |
| `seed_maths_premiere` | mathematiques | premiere | 9 | 25 | 500 |
| `seed_data` (imports `seed_content.py`) | all | terminale | 42 | 152 | 548 |

`seed_data` also creates the admin user from `.env` (`FIRST_ADMIN_EMAIL` / `FIRST_ADMIN_PASSWORD`) and basic Matière records.

**Quiz format**: 20 questions per quiz in individual seed files (8 QCM facile + 6 QCM moyen + 3 vrai_faux moyen + 3 texte_libre difficile). Terminale quizzes in `seed_content.py` have 2-3 questions per quiz.

**Total**: 280 quizzes, 3108 questions across 280 lessons.

## Conventions
- Views are function-based with `@login_required`; use CBV only when there is a clear reason
- URLs are named — always use `{% url 'name' %}` in templates
- French variable names in models/views is intentional and expected — keep consistency
- Forms render with custom widgets defined in `users/forms.py` (Tailwind classes baked in)
- No JavaScript files — all JS lives inline in templates or in Alpine.js `x-data` blocks
- Migrations: always run `makemigrations` before `migrate`; never edit migration files manually unless fixing a squash

## Rate Limiting
- Login: `django-axes` (AXES_FAILURE_LIMIT=5, AXES_COOLOFF_TIME=0.5h, AXES_LOCKOUT_CALLABLE configured)
- Quiz endpoints: cache-based `_check_quiz_rate_limit(user_id)` — 30 requests/min; returns HTTP 429 if exceeded
- Middleware: `axes.middleware.AxesMiddleware` in MIDDLEWARE; backend: `axes.backends.AxesStandaloneBackend`

## Email Verification
- New users are created with `is_active=False`
- `_envoyer_email_verification(request, user)` signs the user PK with `django.core.signing` (salt=`email-verification`, max_age=86400)
- `verifier_email_view` validates the token, sets `is_active=True`, logs in the user
- Tampered/expired tokens return HTTP 400 and render `registration/email_verification_invalid.html`

## Admin Analytics
- `admin_analytics_view` at `/admin-panel/analytics/` (admin-only, `is_admin` check)
- Context: `weak_questions` (list of dicts with `question_id`, `texte`, `lecon`, `taux`), `lecon_completion` (dict by lecon PK), `chapitre_pass_rate` (dict by chapitre PK)
- Template: `templates/dashboard/admin_analytics.html` — uses `item.texte` and `item.question_id` (NOT `item.question.texte`)

## Content Import
- `python manage.py import_questions <csv_file>` — columns: `quiz_lecon_slug`, `texte`, `type`, `reponse_correcte`, `options` (JSON), `tolerances` (JSON), `explication`, `points`, `ordre`, `difficulte`
- `--dry-run` flag: validates without writing to DB
- Rows with missing `reponse_correcte` or unknown `quiz_lecon_slug` are skipped with a warning

## PDF Export & LaTeX Rendering
- `lecon_pdf_view` at `/cours/lecon/<pk>/pdf/` — login required
- **Pipeline**: Markdown content → `_proteger_latex()` (replaces `$$...$$` and `$...$` with placeholders) → `python-markdown` → `_restaurer_latex_svg()` (compiles equations via LaTeX engine + dvisvgm, embeds inline SVG) → WeasyPrint renders HTML→PDF
- **LaTeX compilation**: `_compiler_equations_latex()` generates a single `.tex` file (all equations, one per `\newpage`), runs `latex -interaction=nonstopmode` → DVI, then `dvisvgm --no-fonts --exact-bbox` → one SVG per page with `<path>` glyphs (no font dependency)
- **SVG cleanup**: `_nettoyer_svg(svg, prefix)` strips XML prologue/comments, prefixes all `id`/`href` attributes with `eq{n}-` to avoid WeasyPrint "Anchor defined twice" collisions
- **Dockerfile packages**: `texlive-latex-base`, `texlive-latex-recommended`, `texlive-fonts-recommended`, `dvisvgm`, `fonts-stix`
- **Pinned deps**: `weasyprint==62.3`, `pydyf==0.11.0` (0.12.x breaks WeasyPrint's `super().transform()`)
- **Template**: `lecon_pdf.html` — CSS classes `.math-inline` (inline SVG, `vertical-align: middle`) and `.math-block` (centred display equations)

## Self-Update Rule
When you make changes that affect the project structure, models, URL routes, features, or conventions documented in this file or in `.github/agents/implementer.agent.md`, **update both files** to reflect the new state before finishing your task. Keep these files as the single source of truth for the project.
