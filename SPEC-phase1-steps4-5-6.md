# SPEC — Phase 1, Steps 4–6

> **Status:** ✅ Implemented — 33 tests passing, all features deployed.

---

## Step 4 — Password Reset Flow

### Goal

Students who forget their password are currently locked out. Add Django's built-in password reset views with styled French templates so users can reset via email.

### Design Decisions

#### Decision 1: Email backend

| Environment | Backend | Why |
|-------------|---------|-----|
| **Development** | `django.core.mail.backends.console.EmailBackend` | Emails printed to `docker compose logs web` — no SMTP needed locally |
| **Production (Heroku)** | `django.core.mail.backends.smtp.SMTPBackend` via a transactional email service | Real delivery required |

**Recommendation:** Use console backend in `development.py`, SMTP in `production.py`. For the actual email service, the cheapest options are:
- **Brevo (ex-Sendinblue)** — 300 emails/day free forever, SMTP relay, no credit card
- **Mailgun** — 100 emails/day free on Flex plan

I'll configure production.py to read `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL` from `.env` via `python-decouple`. You can fill those in when you choose a provider — zero code change needed.

#### Decision 2: URL prefix

| Option | URLs |
|--------|------|
| **A) Under `/` (flat)** | `/mot-de-passe-oublie/`, `/mot-de-passe-oublie/envoye/`, `/reinitialiser/<uidb64>/<token>/`, `/reinitialiser/termine/` |
| **B) Under `/compte/`** | `/compte/mot-de-passe-oublie/`, etc. |

**Recommendation:** Option A — keeps URLs short and matches the existing flat structure (`/connexion/`, `/inscription/`). All four routes live in `users/urls.py`.

#### Decision 3: Rate limiting on reset requests

The built-in `PasswordResetView` doesn't send an email if the address isn't found (no user enumeration), but an attacker could still spam the endpoint. Options:

| Option | Detail |
|--------|--------|
| **A) Skip for now** | Low traffic, low risk at this stage |
| **B) Add `django-ratelimit` decorator** | Extra dependency, overkill right now |

**Recommendation:** Option A — Step 11 (Phase 2) adds rate limiting globally. No point adding a one-off decorator now.

---

### Files Changed

#### 1. `config/settings/development.py` — console email backend

```python
# Email — print to console in dev
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "ScienceLycée <noreply@sciencelycee.fr>"
```

#### 2. `config/settings/production.py` — SMTP email backend

```python
# Email — transactional SMTP (Brevo, Mailgun, etc.)
EMAIL_BACKEND = "django.core.mail.backends.smtp.SMTPBackend"
EMAIL_HOST = config("EMAIL_HOST", default="smtp-relay.brevo.com")
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="ScienceLycée <noreply@sciencelycee.fr>")
```

#### 3. `users/urls.py` — 4 new routes

```python
from django.contrib.auth import views as auth_views

# Add to urlpatterns:
path("mot-de-passe-oublie/", auth_views.PasswordResetView.as_view(
    template_name="registration/password_reset.html",
    email_template_name="registration/password_reset_email.html",
    subject_template_name="registration/password_reset_subject.txt",
    success_url=reverse_lazy("password_reset_done"),
), name="password_reset"),

path("mot-de-passe-oublie/envoye/", auth_views.PasswordResetDoneView.as_view(
    template_name="registration/password_reset_done.html",
), name="password_reset_done"),

path("reinitialiser/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
    template_name="registration/password_reset_confirm.html",
    success_url=reverse_lazy("password_reset_complete"),
), name="password_reset_confirm"),

path("reinitialiser/termine/", auth_views.PasswordResetCompleteView.as_view(
    template_name="registration/password_reset_complete.html",
), name="password_reset_complete"),
```

#### 4. Templates — 4 new + 1 email + 1 subject

All extend `base.html` with `{% block full_content %}` (no sidebar, like login/register).
Same visual style as `login.html` (centered card, ⚗️ logo, subject-gradient accents).

| File | Purpose |
|------|---------|
| `templates/registration/password_reset.html` | Form: "Enter your email to reset your password" — one email field + submit button |
| `templates/registration/password_reset_done.html` | Confirmation: "If an account exists with that email, we've sent a reset link." (no user enumeration) |
| `templates/registration/password_reset_confirm.html` | Form: "Enter your new password" — two password fields + submit, validates with Django password validators |
| `templates/registration/password_reset_complete.html` | Success: "Your password has been reset. You can now log in." + link to `/connexion/` |
| `templates/registration/password_reset_email.html` | Plain-text email body (French) with the reset link |
| `templates/registration/password_reset_subject.txt` | Subject line: `ScienceLycée — Réinitialisation de votre mot de passe` |

#### 5. `templates/registration/login.html` — add "Forgot password?" link

Add a "Mot de passe oublié ?" link below the password field, pointing to `{% url 'password_reset' %}`.

---

### New URL Map (additions only)

```
/mot-de-passe-oublie/                      → password_reset
/mot-de-passe-oublie/envoye/               → password_reset_done
/reinitialiser/<uidb64>/<token>/           → password_reset_confirm
/reinitialiser/termine/                     → password_reset_complete
```

---

## Step 5 — Custom Error Pages (404, 500)

### Goal

Replace Django's default white-text error pages with branded, helpful pages that match the app's visual identity and guide users back to useful content.

### Design Decisions

#### Decision 1: Template style

| Option | Detail |
|--------|--------|
| **A) Minimal — centred card** | Same layout as login/register (centred ⚗️ + message + CTA button). Simple, consistent. |
| **B) Full branded page** | Custom illustration, animated elements, more work. |

**Recommendation:** Option A — matches existing public page style, takes 10 minutes to build, and does the job.

#### Decision 2: 500 page constraints

The 500 template **must not** use template tags that require database access (no `{% url %}`, no context processors that query the DB) because the 500 handler fires when the app is broken. We'll hardcode the `/` and `/connexion/` links.

#### Decision 3: DEBUG=False testing

Custom error pages only render when `DEBUG=False`. We'll add a note on how to test locally (temporarily set `DEBUG=False` in `development.py`, or use the test URLs from django-debug-toolbar if installed).

---

### Files Changed

#### 1. `templates/404.html` — Page not found

- Extends `base.html` using `{% block full_content %}`
- Centred card with ⚗️ icon
- **Title:** "Page introuvable"
- **Message:** "La page que tu cherches n'existe pas ou a été déplacée."
- **CTA buttons:**
  - "Retour à l'accueil" → `{% url 'home' %}`
  - "Voir les cours" → `{% url 'catalogue_matiere' matiere_slug='mathematiques' %}` (or just `/cours/mathematiques/`)
- Appropriate tone (friendly, tutoring, "tu")

#### 2. `templates/500.html` — Server error

- **Does NOT extend `base.html`** — fully self-contained HTML (database may be down)
- Inline Tailwind via CDN `<script>` tag (same one as `base.html`)
- Centred card with ⚗️ icon
- **Title:** "Erreur serveur"
- **Message:** "Oups, quelque chose s'est mal passé de notre côté. Réessaie dans quelques instants."
- **CTA:** "Retour à l'accueil" → hardcoded `/`
- No `{% url %}` tags, no DB queries, no template inheritance

#### 3. `config/urls.py` — Register handlers

```python
handler404 = "config.views.custom_404"
handler500 = "config.views.custom_500"
```

#### 4. `config/views.py` — Custom handler functions (new file)

```python
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, "404.html", status=404)

def custom_500(request):
    return render(request, "500.html", status=500)
```

Using a thin view function (instead of a string path to the template) gives us flexibility to add logging later if needed.

---

## Step 6 — Automated Tests + CI

### Goal

Go from zero tests to a meaningful safety net covering the most critical business logic. Set up GitHub Actions so every push and PR runs the test suite automatically.

### Design Decisions

#### Decision 1: Test scope (what to test first)

We can't test everything at once. Priority is business-critical logic that, if broken, would lose users or money:

| Priority | Area | Tests |
|----------|------|-------|
| **P0 — Critical** | Access control | Anonymous can't access authenticated views; eleve can't access admin views; admin can access everything |
| **P0 — Critical** | Quiz scoring | QCM, Vrai/Faux, Texte libre (with tolerances + case insensitivity) |
| **P0 — Critical** | Chapter unlock | ≥80% required, < 80% blocked; `ChapitreDebloque` created on pass |
| **P1 — Important** | Leitner box progression | Correct → box+1; Wrong → box=1; prochaine_revision calculation |
| **P1 — Important** | Slug generation | Auto-slug on save, uniqueness within scope |
| **P1 — Important** | Public pages | Catalogue accessible without login; free lesson accessible; non-free lesson redirects |
| **P2 — Nice to have** | Preview mode | Session key set → eleve view; no progress written; exit clears session |
| **P2 — Nice to have** | Dashboard stats | Streak calculation, per-subject progress |

**Recommendation:** Implement P0 and P1 now. P2 can come later.

#### Decision 2: Test framework

| Option | Pros | Cons |
|--------|------|------|
| **A) Django's `TestCase` + `unittest`** | Zero dependencies, built-in, what Django docs recommend | Verbose assertions |
| **B) `pytest` + `pytest-django`** | Better assertions, fixtures, parametrize, less boilerplate | Extra dependency |

**Recommendation:** Option B — `pytest-django` is industry standard, makes tests shorter and more readable. Add `pytest` + `pytest-django` to `requirements.txt`.

#### Decision 3: Test database

Django's test runner creates a temporary test database automatically. No special config needed — it uses the same `DATABASES` setting but creates a `test_<dbname>` database. In Docker, the `db` container handles this. In CI (GitHub Actions), we'll spin up a PostgreSQL service container.

#### Decision 4: CI platform

GitHub Actions — the repo is already on GitHub, free for public repos, generous minutes for private repos.

---

### Files Changed

#### 1. `requirements.txt` — Add test dependencies

```
pytest==8.3.4
pytest-django==4.9.0
```

#### 2. `backend/pytest.ini` — pytest configuration

```ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings.development
python_files = tests.py test_*.py *_tests.py
python_classes = Test*
python_functions = test_*
```

#### 3. `backend/users/tests.py` — User & access control tests

```
Tests:
- test_connexion_page_accessible_anonymous
- test_inscription_creates_eleve
- test_dashboard_redirects_anonymous_to_login
- test_admin_panel_forbidden_for_eleve
- test_admin_panel_accessible_for_admin
- test_profil_requires_login
```

#### 4. `backend/courses/tests.py` — Course, slug & public page tests

```
Tests:
- test_matiere_slug_auto_generated
- test_chapitre_slug_auto_generated
- test_lecon_slug_auto_generated
- test_slug_unique_within_scope
- test_catalogue_accessible_anonymous
- test_free_lesson_accessible_anonymous
- test_non_free_lesson_redirects_to_login
- test_authenticated_user_redirected_to_pk_view
```

#### 5. `backend/progress/tests.py` — Quiz, unlock & Leitner tests

```
Tests:
— Quiz scoring:
  - test_qcm_correct_answer_scores
  - test_qcm_wrong_answer_zero
  - test_vrai_faux_scoring
  - test_texte_libre_exact_match
  - test_texte_libre_tolerance_match
  - test_texte_libre_case_insensitive

— Chapter unlock:
  - test_chapitre_quiz_pass_at_80_percent
  - test_chapitre_quiz_fail_below_80_percent
  - test_passing_creates_chapitre_debloque
  - test_next_chapter_accessible_after_unlock

— Leitner:
  - test_correct_answer_moves_box_up
  - test_wrong_answer_resets_to_box_1
  - test_max_box_is_5
  - test_prochaine_revision_calculated_correctly
```

#### 6. `.github/workflows/ci.yml` — GitHub Actions pipeline

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_DB: test_sciencelycee
          POSTGRES_USER: sciencelycee
          POSTGRES_PASSWORD: sciencelycee_secret
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    env:
      DJANGO_SETTINGS_MODULE: config.settings.development
      DATABASE_URL: postgres://sciencelycee:sciencelycee_secret@localhost:5432/test_sciencelycee
      SECRET_KEY: ci-test-secret-key

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        working-directory: backend
        run: pip install -r requirements.txt

      - name: Run tests
        working-directory: backend
        run: pytest -v --tb=short
```

---

### What to run locally

```bash
# Run tests in Docker
docker compose run --rm --entrypoint pytest web -v --tb=short

# Or if you have a local Python env
cd backend && pytest -v
```

---

## What This Does NOT Include (deferred)

- **Rate limiting on reset endpoint** — Step 11 (Phase 2) handles rate limiting globally
- **Email verification on signup** — Step 12 (Phase 2), separate feature
- **P2 tests (preview mode, dashboard stats)** — will be added incrementally as features evolve
- **Coverage reporting / badge** — nice-to-have, can be added to CI later with `pytest-cov`

---

## Implementation Checklist

### Step 4 — Password Reset
- [ ] Add `EMAIL_BACKEND` + `DEFAULT_FROM_EMAIL` to `development.py`
- [ ] Add SMTP settings to `production.py` (reads from `.env`)
- [ ] Add 4 password reset URL patterns to `users/urls.py`
- [ ] Create `templates/registration/password_reset.html`
- [ ] Create `templates/registration/password_reset_done.html`
- [ ] Create `templates/registration/password_reset_confirm.html`
- [ ] Create `templates/registration/password_reset_complete.html`
- [ ] Create `templates/registration/password_reset_email.html`
- [ ] Create `templates/registration/password_reset_subject.txt`
- [ ] Add "Mot de passe oublié ?" link to `login.html`
- [ ] Test locally: trigger reset, check console output for email, follow link, change password, log in

### Step 5 — Custom Error Pages
- [ ] Create `templates/404.html`
- [ ] Create `templates/500.html` (self-contained, no DB)
- [ ] Create `config/views.py` with `custom_404` and `custom_500`
- [ ] Register `handler404` and `handler500` in `config/urls.py`
- [ ] Test with `DEBUG=False` locally

### Step 6 — Automated Tests + CI
- [ ] Add `pytest` + `pytest-django` to `requirements.txt`
- [ ] Create `backend/pytest.ini`
- [ ] Create `users/tests.py` — access control tests
- [ ] Create `courses/tests.py` — slug + public page tests
- [ ] Create `progress/tests.py` — quiz scoring + chapter unlock + Leitner tests
- [ ] Create `.github/workflows/ci.yml`
- [ ] Run tests locally via Docker — all green
- [ ] Push and verify GitHub Actions passes

---

## New URL Map (additions only)

```
/mot-de-passe-oublie/                      → password_reset
/mot-de-passe-oublie/envoye/               → password_reset_done
/reinitialiser/<uidb64>/<token>/           → password_reset_confirm
/reinitialiser/termine/                     → password_reset_complete
```

No new URLs for Steps 5–6 (error handlers are implicit; tests don't add routes).
