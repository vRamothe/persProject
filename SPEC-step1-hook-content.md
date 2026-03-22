# SPEC — Step 1: Open "Hook" Content (SEO & Storefront)

> **Status:** ✅ Implemented — deployed and verified.

## Goal

Make the first lesson of every chapter publicly accessible (no login required) with clean, SEO-friendly slug URLs so Google can index them. This creates the "free sample" funnel that drives signups and future Stripe conversions.

---

## Design Decisions (need your input)

### Decision 1: How to mark a lesson as "free"

| Option | Pros | Cons |
|--------|------|------|
| **A) Implicit: `ordre == 1`** | Zero model change, zero admin overhead — first lesson of every chapter is automatically free | Can't make a different lesson free, can't make all lessons paid |
| **B) Explicit: `gratuit` BooleanField on `Lecon`** | Full control per lesson via Django admin | Requires a migration + manually toggling each lesson |

**Recommendation:** Option B — it's one small field but gives you total flexibility (e.g. you could make a mid-chapter lesson free as a teaser, or lock all lessons for a new chapter until content is ready).

### Decision 2: URL structure for public lessons

```
Option A:  /cours/<matiere>/<niveau>/<chapitre-slug>/<lecon-slug>/
           e.g. /cours/mathematiques/terminale/suites-numeriques/definition-et-premiers-exemples/

Option B:  /cours/<niveau>/<matiere>/<chapitre-slug>/<lecon-slug>/
           e.g. /cours/terminale/mathematiques/suites-numeriques/definition-et-premiers-exemples/
```

**Recommendation:** Option A — groups by subject first, which matches how students think ("I need math help" → "which level?" → "which chapter?").

### Decision 3: What do anonymous visitors see on non-free lessons?

| Option | Behaviour |
|--------|-----------|
| **A) Redirect to login** | Simple, current behaviour |
| **B) Show lesson title + first paragraph + CTA overlay** | Better conversion — shows what they're missing |
| **C) Show the paywall modal directly** | Aggressive but clear — matches Step 2 (visual paywall) |

**Recommendation:** Option A for now (redirect to login with a `?next=` param). Step 2 (visual paywall + Stripe) will replace this with Option C later. No point building a modal without Stripe behind it.

---

## Files Changed

### 1. `courses/models.py` — Add slugs + `gratuit` field

```python
# Matiere: add slug
slug = models.SlugField(max_length=60, unique=True, blank=True)

# Chapitre: add slug
slug = models.SlugField(max_length=255, blank=True)
# unique_together becomes [["matiere", "niveau", "ordre"], ["matiere", "niveau", "slug"]]

# Lecon: add slug + gratuit
slug = models.SlugField(max_length=255, blank=True)
gratuit = models.BooleanField(default=False, verbose_name="Leçon gratuite (accessible sans compte)")
# unique_together becomes [["chapitre", "ordre"], ["chapitre", "slug"]]
```

Auto-populate slugs in `save()` via `django.utils.text.slugify` if blank. For `Matiere`, slug = `nom` value (already slug-safe: `physique`, `chimie`, `mathematiques`).

**Migration:** One migration for the 4 new fields. A data migration to backfill slugs on existing rows using `slugify(titre)` (or `slugify(nom)` for Matiere).

### 2. `courses/urls.py` — Add public routes

```python
# New public routes (no login required):
path("<str:matiere_slug>/", views.catalogue_matiere_view, name="catalogue_matiere"),
path("<str:matiere_slug>/<str:niveau>/<slug:chapitre_slug>/<slug:lecon_slug>/",
     views.lecon_publique_view, name="lecon_publique"),
```

These go **after** the existing named routes (revisions, chapitre, lecon) to avoid conflicts. The existing `lecon/<int:pk>/` route stays for authenticated users — no breaking change.

### 3. `courses/views.py` — Two new views

#### `catalogue_matiere_view(request, matiere_slug)` — no `@login_required`

- Looks up `Matiere` by slug (404 if not found)
- Lists all niveaux and their chapters for that matière
- For each chapter: show title, description, nb lessons, and whether a free lesson exists
- Links free lessons to `lecon_publique` URL; non-free lessons show 🔒
- Template: `templates/courses/catalogue.html`

#### `lecon_publique_view(request, matiere_slug, niveau, chapitre_slug, lecon_slug)` — no `@login_required`

- Resolves the full slug chain: matiere → chapitre (filtered by niveau) → lecon
- If `lecon.gratuit` is `False` → redirect to `connexion` with `?next=` pointing to this URL
- If user is already authenticated → redirect to the existing `lecon` view (PK-based) to get the full experience with progression tracking
- Renders lesson content (Markdown → HTML with LaTeX protection, video embed) — **read-only, no progression writes**
- Template: `templates/courses/lecon_publique.html`

### 4. `templates/courses/catalogue.html` — new template

- Extends `base.html` using `{% block full_content %}` (no sidebar, like login page)
- Subject-coloured header (gradient matching the matière)
- Chapters listed by niveau (Seconde / Première / Terminale sections)
- Each chapter: title, description, lesson count
- Free lessons: clickable links; non-free: 🔒 with "Inscris-toi pour débloquer"
- CTA button: "Créer un compte gratuitement" → `{% url 'inscription' %}`
- No dark-mode `dark:` classes (handled globally)

### 5. `templates/courses/lecon_publique.html` — new template

- Extends `base.html` using `{% block full_content %}` (no sidebar)
- Minimal top nav bar: logo + "Connexion" / "Inscription" buttons (same style as login page)
- Rendered lesson content (same prose styling as `lecon.html`)
- Video embed if present
- No quiz section, no progress buttons, no "mark as done"
- Bottom CTA banner: "Tu veux accéder à tous les cours et quiz ? Crée ton compte !" → inscription
- SEO `<meta>` tags in `{% block extra_head %}`:
  - `<title>{{ lecon.titre }} — {{ chapitre.titre }} | ScienceLycée</title>`
  - `<meta name="description" content="...">` (first 160 chars of lesson content, stripped of Markdown)
  - `<meta name="robots" content="index, follow">`
  - Open Graph: `og:title`, `og:description`, `og:type=article`

### 6. `templates/base.html` — SEO meta default

- Add `<meta name="robots" content="noindex, nofollow">` as default in `<head>` (authenticated pages should not be indexed)
- Public templates override this via `{% block extra_head %}` with `index, follow`

### 7. `config/urls.py` — Landing page for anonymous users

- Change the root `/` handler: if user is authenticated → redirect to dashboard (current behaviour). If anonymous → redirect to a simple landing or to `/cours/mathematiques/` (the catalogue).
- Alternative: keep `/` as-is (always redirects to dashboard, which 302s to login). The SEO entry point is the catalogue URL, not `/`.

**Recommendation:** Keep `/` as-is. Google enters via catalogue/lesson URLs, not the root. Simpler, no risk of breaking anything.

### 8. `courses/admin.py` — Expose new fields

- Add `slug` and `gratuit` to the relevant `ModelAdmin` classes:
  - `MatiereAdmin`: add `slug` to `list_display`, `prepopulated_fields`
  - `ChapitreAdmin`: add `slug` to `list_display`, `prepopulated_fields`
  - `LeconAdmin`: add `slug`, `gratuit` to `list_display`, `list_filter`, `prepopulated_fields`

### 9. Data migration — backfill slugs + mark first lessons as free

- For each `Matiere`: `slug = nom` (already slug-safe)
- For each `Chapitre`: `slug = slugify(titre)`, deduplicate within (matiere, niveau) if needed
- For each `Lecon`: `slug = slugify(titre)`, deduplicate within chapitre if needed
- For each chapter's first lesson (`ordre == 1`): set `gratuit = True`

---

## What This Does NOT Include (deferred to later steps)

- **Paywall modal** — Step 2, depends on Stripe
- **Stripe integration** — Step 3
- **Sitemap** — Step 15, quick add-on after public URLs exist
- **Landing page redesign** — not in scope; the catalogue + free lessons ARE the landing page for SEO

---

## New URL Map (additions only)

```
/cours/physique/                           → catalogue_matiere (public)
/cours/chimie/                             → catalogue_matiere (public)
/cours/mathematiques/                      → catalogue_matiere (public)
/cours/mathematiques/terminale/suites-numeriques/definition-et-exemples/
                                           → lecon_publique (public, if gratuit=True)
```

Existing authenticated routes unchanged:
```
/cours/                                    → matieres (login required)
/cours/lecon/42/                           → lecon (login required)
```

---

## Checklist Before Shipping

- [x] All existing authenticated routes still work (no regression)
- [x] Free lesson renders correctly for anonymous visitors (Markdown, LaTeX, video)
- [x] Non-free lesson redirects to login
- [x] Authenticated user on public URL gets redirected to the PK-based view
- [x] Slugs auto-generated on save for new models
- [x] Existing data backfilled with slugs
- [x] `gratuit` togglable in Django admin
- [x] `<meta robots>` correct: `noindex` on authenticated pages, `index` on public pages
- [x] Dark mode works on public pages (global CSS handles it)
- [x] No progression writes for anonymous visitors

---

## Next: Step 2 — Visual Paywall

Premium lessons stay visible with a 🔒 icon. On click → modal paywall ("Unlock the full Bac program") with pricing tiers — not a login redirect. This replaces the current Step 1 behaviour of redirecting non-free lessons to the login page.
