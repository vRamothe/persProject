# ScienceLycée — Workspace Instructions

## Project Overview
ScienceLycée is a French high-school e-learning platform for Physics, Chemistry, and Math (Seconde / Première / Terminale). It is a **Django 5 monolith** with server-side rendering via HTMX + Alpine.js + Tailwind CSS (CDN). No React, no DRF.

## Stack
| Layer | Technology |
|-------|------------|
| Backend | Python 3.12, Django 5.1, PostgreSQL 16 |
| Frontend | Tailwind CSS (CDN, `darkMode: 'class'`), HTMX 1.9, Alpine.js 3.14 |
| Math rendering | KaTeX (auto-render) |
| Content | Markdown rendered server-side via `python-markdown` |
| Auth | Custom `users.CustomUser` (email-based, `AUTH_USER_MODEL`) |
| Deploy | Docker Compose — `db` (postgres), `web` (gunicorn), `nginx` |
| Config | `python-decouple` + `.env`, settings split: `base / development / production` |

## Django App Structure
```
backend/
  app/           # Unused scaffolding — do not add code here
  config/        # urls.py, wsgi.py, settings/{base,development,production}.py
  users/         # CustomUser model, managers, forms, views, urls
  courses/       # Matiere > Chapitre > Lecon > Quiz > Question hierarchy
  progress/      # UserProgression, UserQuizResultat, ChapitreDebloque
  templates/     # All HTML — base.html + per-app subdirs
  static/        # Static assets (currently empty beyond README)
```

## Key Models
- `users.CustomUser` — email login, `role` (admin|eleve), `niveau` (seconde|premiere|terminale)
- `courses.Matiere` — physique / chimie / mathematiques
- `courses.Chapitre` — belongs to Matiere + niveau, has `ordre` and `score_minimum_deblocage`
- `courses.Lecon` — belongs to Chapitre, `contenu` in Markdown
- `courses.Quiz` / `courses.Question` — QCM, Vrai/Faux, or **Texte libre** linked to a Lecon
  - `Question.type` choices: `qcm`, `vrai_faux`, `texte_libre`
  - `Question.tolerances` (JSONField, optional) — accepted alternative answers for `texte_libre`, e.g. `["azote", "N2"]`; comparison is case-insensitive
- `progress.UserProgression` — per (user, lecon) statut: non_commence / en_cours / termine
- `progress.UserQuizResultat` — best score, nb_tentatives, passe bool
- `progress.ChapitreDebloque` — unlocking mechanism

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

## Codebase Reference
`CODEBASE_REFERENCE.md` at the project root contains a compact summary of all models, URLs, views, forms, templates, settings, management commands, and key patterns. **All agents must read this file first** before reading source files. After any code change, the corresponding section must be updated.

## Dev Workflow
```bash
# Start everything
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
`python manage.py seed_data` — idempotent, creates admin + sample Matière/Chapitre/Lecon content. Extend via `courses/management/commands/seed_content.py`.

Admin credentials from `.env`: `FIRST_ADMIN_EMAIL` / `FIRST_ADMIN_PASSWORD`.

## Paywall / Premium Lessons
- `Lecon.gratuit` (`BooleanField`, default=`False`) — determines if a lesson is fully public or premium
- Premium lessons on public URLs show truncated content (~2000 words) + CSS blur overlay + paywall modal
- Server-side truncation via `courses/utils/truncate.py` → `tronquer_contenu_markdown(contenu, max_mots=2000)`
- CSS classes: `.paywall-blur-container`, `.paywall-blur-content`, `.paywall-blur-overlay`, `.paywall-cta` — defined in `lecon_publique.html`
- Dark mode override: `html.dark .paywall-blur-overlay` in `base.html` (no `dark:` classes in child templates)
- Paywall modal: `templates/components/_paywall_modal.html` — Alpine.js, included via `{% include %}` in `lecon_publique.html`
- Access check: `user_a_acces = request.user.is_admin or getattr(request.user, 'is_premium', False)` — `is_premium` is a stub (always `False`) until Stripe integration
- Listings (`catalogue.html`, `accueil.html`): premium lessons show 🔒 cadenas + "Premium" badge as clickable links

## Conventions
- Views are function-based with `@login_required`; use CBV only when there is a clear reason
- URLs are named — always use `{% url 'name' %}` in templates
- French variable names in models/views is intentional and expected — keep consistency
- Forms render with custom widgets defined in `users/forms.py` (Tailwind classes baked in)
- No JavaScript files — all JS lives inline in templates or in Alpine.js `x-data` blocks
- Migrations: always run `makemigrations` before `migrate`; never edit migration files manually unless fixing a squash
