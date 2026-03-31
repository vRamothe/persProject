# ScienceLycée — Codebase Reference
_Compact reference for AI agents. Read this instead of re-reading source files._

---

## 1. Models

### 1.1 `users.CustomUser` (extends `AbstractBaseUser`, `PermissionsMixin`)

| Field | Type | Constraints |
|-------|------|-------------|
| `email` | `EmailField` | unique, `USERNAME_FIELD` |
| `prenom` | `CharField(100)` | required |
| `nom` | `CharField(100)` | required |
| `role` | `CharField(10)` | choices=`RoleChoices`, default=`eleve` |
| `niveau` | `CharField(20)` | choices=`NiveauChoices`, blank, null |
| `is_active` | `BooleanField` | default=True |
| `is_staff` | `BooleanField` | default=False |
| `date_joined` | `DateTimeField` | auto_now_add |
| `updated_at` | `DateTimeField` | auto_now |

Properties: `nom_complet`, `initiales`, `is_admin`, `is_eleve`

Manager: `CustomUserManager` — `REQUIRED_FIELDS = ["prenom", "nom"]`

### 1.2 `users.ConnexionLog`

| Field | Type | Constraints |
|-------|------|-------------|
| `user` | `FK → CustomUser` | on_delete=CASCADE, related_name=`connexions` |
| `timestamp` | `DateTimeField` | auto_now_add |
| `ip` | `GenericIPAddressField` | null, blank |

### 1.3 Choices (users)

```python
NiveauChoices: seconde | premiere | terminale
RoleChoices:   admin | eleve
```

### 1.4 `courses.Matiere`

| Field | Type | Constraints |
|-------|------|-------------|
| `nom` | `CharField(50)` | choices=`MatiereChoices`, unique |
| `slug` | `SlugField(60)` | unique, blank (auto from `nom`) |
| `description` | `TextField` | blank |
| `created_at` | `DateTimeField` | auto_now_add |

Properties: `couleurs` (from `MATIERE_COULEURS`), `icone_svg`

### 1.5 `courses.Chapitre`

| Field | Type | Constraints |
|-------|------|-------------|
| `matiere` | `FK → Matiere` | on_delete=CASCADE, related_name=`chapitres` |
| `niveau` | `CharField(20)` | choices=`NiveauChoices` |
| `titre` | `CharField(255)` | |
| `slug` | `SlugField(255)` | blank (auto from `titre`) |
| `description` | `TextField` | blank |
| `ordre` | `PositiveIntegerField` | default=1 |
| `score_minimum_deblocage` | `FloatField` | default=60.0 |
| `created_at` | `DateTimeField` | auto_now_add |
| `updated_at` | `DateTimeField` | auto_now |

`unique_together`: `[matiere, niveau, ordre]`, `[matiere, niveau, slug]`

### 1.6 `courses.Lecon`

| Field | Type | Constraints |
|-------|------|-------------|
| `chapitre` | `FK → Chapitre` | on_delete=CASCADE, related_name=`lecons` |
| `titre` | `CharField(255)` | |
| `slug` | `SlugField(255)` | blank (auto from `titre`) |
| `contenu` | `TextField` | Markdown with LaTeX ($...$) |
| `ordre` | `PositiveIntegerField` | default=1 |
| `duree_estimee` | `PositiveIntegerField` | default=15 (minutes) |
| `gratuit` | `BooleanField` | default=False |
| `video_youtube_url` | `URLField` | blank, default="" |
| `video_fichier` | `FileField` | upload_to=`lecons/videos/`, blank, default="" |
| `created_at` | `DateTimeField` | auto_now_add |
| `updated_at` | `DateTimeField` | auto_now |

`unique_together`: `[chapitre, ordre]`, `[chapitre, slug]`

Properties: `has_quiz`
Methods: `get_lecon_precedente()`, `get_lecon_suivante()`

### 1.7 `courses.Quiz`

| Field | Type | Constraints |
|-------|------|-------------|
| `lecon` | `OneToOneField → Lecon` | on_delete=CASCADE, related_name=`quiz` |
| `titre` | `CharField(255)` | |
| `score_minimum` | `FloatField` | default=60.0 |
| `created_at` | `DateTimeField` | auto_now_add |

Method: `get_total_points()`

### 1.8 `courses.Question`

| Field | Type | Constraints |
|-------|------|-------------|
| `quiz` | `FK → Quiz` | on_delete=CASCADE, related_name=`questions` |
| `texte` | `TextField` | |
| `type` | `CharField(20)` | choices=`TypeQuestionChoices`, default=`qcm` |
| `options` | `JSONField` | null, blank — `["Opt A", "Opt B", ...]` for QCM |
| `reponse_correcte` | `CharField(500)` | QCM: 0-index; V/F: `vrai`/`faux`; Texte: actual answer |
| `tolerances` | `JSONField` | null, blank — alt answers for texte_libre only |
| `explication` | `TextField` | blank |
| `difficulte` | `CharField(20)` | choices=`DifficulteChoices`, default=`moyen` |
| `points` | `PositiveIntegerField` | default=1 |
| `ordre` | `PositiveIntegerField` | default=1 |

### 1.9 Choices (courses)

```python
MatiereChoices:       physique | chimie | mathematiques
NiveauChoices:        seconde | premiere | terminale
TypeQuestionChoices:  qcm | vrai_faux | texte_libre
DifficulteChoices:    facile | moyen | difficile
```

### 1.10 `progress.UserProgression`

| Field | Type | Constraints |
|-------|------|-------------|
| `user` | `FK → AUTH_USER_MODEL` | on_delete=CASCADE, related_name=`progressions` |
| `lecon` | `FK → courses.Lecon` | on_delete=CASCADE, related_name=`progressions` |
| `statut` | `CharField(20)` | choices=`StatutLeconChoices`, default=`non_commence` |
| `derniere_activite` | `DateTimeField` | auto_now |
| `termine_le` | `DateTimeField` | null, blank |

`unique_together`: `[user, lecon]`

### 1.11 `progress.UserQuizResultat`

| Field | Type | Constraints |
|-------|------|-------------|
| `user` | `FK → AUTH_USER_MODEL` | on_delete=CASCADE, related_name=`quiz_resultats` |
| `quiz` | `FK → courses.Quiz` | on_delete=CASCADE, related_name=`resultats` |
| `score` | `FloatField` | default=0.0 (best %) |
| `nb_tentatives` | `PositiveIntegerField` | default=0 |
| `passe` | `BooleanField` | default=False |
| `reponses` | `JSONField` | null, blank |
| `premiere_tentative` | `DateTimeField` | auto_now_add |
| `derniere_tentative` | `DateTimeField` | auto_now |

`unique_together`: `[user, quiz]`

### 1.12 `progress.ChapitreDebloque`

| Field | Type | Constraints |
|-------|------|-------------|
| `user` | `FK → AUTH_USER_MODEL` | on_delete=CASCADE, related_name=`chapitres_debloques` |
| `chapitre` | `FK → courses.Chapitre` | on_delete=CASCADE, related_name=`deblocages` |
| `debloque_le` | `DateTimeField` | auto_now_add |

`unique_together`: `[user, chapitre]`

### 1.13 `progress.UserChapitreQuizResultat`

| Field | Type | Constraints |
|-------|------|-------------|
| `user` | `FK → AUTH_USER_MODEL` | on_delete=CASCADE, related_name=`chapitre_quiz_resultats` |
| `chapitre` | `FK → courses.Chapitre` | on_delete=CASCADE, related_name=`quiz_resultats` |
| `score` | `FloatField` | default=0.0 (best %) |
| `nb_tentatives` | `PositiveIntegerField` | default=0 |
| `passe` | `BooleanField` | default=False |
| `reponses` | `JSONField` | null, blank |
| `premiere_tentative` | `DateTimeField` | auto_now_add |
| `derniere_tentative` | `DateTimeField` | auto_now |

`unique_together`: `[user, chapitre]`

### 1.14 `progress.UserQuestionHistorique`

| Field | Type | Constraints |
|-------|------|-------------|
| `user` | `FK → AUTH_USER_MODEL` | on_delete=CASCADE, related_name=`question_historiques` |
| `question` | `FK → courses.Question` | on_delete=CASCADE, related_name=`historiques` |
| `boite` | `PositiveSmallIntegerField` | default=1 (Leitner box 1–5) |
| `prochaine_revision` | `DateField` | |
| `derniere_reponse_correcte` | `BooleanField` | default=False |
| `nb_bonnes` | `PositiveIntegerField` | default=0 |
| `nb_total` | `PositiveIntegerField` | default=0 |
| `mis_a_jour_le` | `DateTimeField` | auto_now |

`unique_together`: `[user, question]`
Method: `enregistrer_reponse(correcte)` — moves box up/down + sets next revision date

### 1.15 `progress.UserNote`

| Field | Type | Constraints |
|-------|------|-------------|
| `user` | `FK → AUTH_USER_MODEL` | on_delete=CASCADE, related_name=`notes` |
| `lecon` | `FK → courses.Lecon` | on_delete=CASCADE, related_name=`notes` |
| `contenu` | `TextField` | blank, max_length=2000 |
| `created_at` | `DateTimeField` | auto_now_add |
| `updated_at` | `DateTimeField` | auto_now |

`unique_together`: `[user, lecon]`

### 1.16 Constants

```python
StatutLeconChoices: non_commence | en_cours | termine
LEITNER_INTERVALLES = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}  # days
```

---

## 2. URLs

### 2.1 `config/urls.py` (root)

| Name | Pattern | View | Notes |
|------|---------|------|-------|
| `home` | `/` | `_home_view` | Auth → `tableau_de_bord`; anon → `accueil_view` |
| — | `/django-admin/` | Django admin | |
| — | `/` | include `users.urls` | |
| — | `/cours/` | include `courses.urls` | |
| — | `/progression/` | include `progress.urls` | |
| `django.contrib.sitemaps.views.sitemap` | `/sitemap.xml` | sitemap | CatalogueSitemap + LeconPubliqueSitemap |
| `health` | `/health/` | `config.views.health_view` | GET, no auth |

Handlers: `handler404` → `config.views.custom_404`, `handler500` → `config.views.custom_500`

### 2.2 `users/urls.py`

| Name | Full Pattern | View | Methods |
|------|-------------|------|---------|
| `connexion` | `/connexion/` | `ConnexionView` | GET, POST |
| `inscription` | `/inscription/` | `InscriptionView` | GET, POST |
| `inscription_confirmation` | `/inscription/confirmation/` | `inscription_confirmation_view` | GET |
| `verifier_email` | `/verifier-email/<str:token>/` | `verifier_email_view` | GET |
| `deconnexion` | `/deconnexion/` | `deconnexion_view` | GET |
| `tableau_de_bord` | `/tableau-de-bord/` | `TableauDeBordView` | GET |
| `profil` | `/profil/` | `ProfilView` | GET, POST |
| `password_reset` | `/mot-de-passe-oublie/` | `PasswordResetView` | GET, POST |
| `password_reset_done` | `/mot-de-passe-oublie/envoye/` | `PasswordResetDoneView` | GET |
| `password_reset_confirm` | `/reinitialiser/<uidb64>/<token>/` | `PasswordResetConfirmView` | GET, POST |
| `password_reset_complete` | `/reinitialiser/termine/` | `PasswordResetCompleteView` | GET |
| `admin_utilisateurs` | `/admin-panel/utilisateurs/` | `admin_utilisateurs` | GET |
| `admin_toggle_actif` | `/admin-panel/utilisateurs/<int:user_id>/toggle/` | `admin_toggle_actif` | POST |
| `admin_eleve_detail` | `/admin-panel/utilisateurs/<int:user_id>/` | `admin_eleve_detail` | GET |
| `admin_toggle_chapitre` | `/admin-panel/utilisateurs/<int:user_id>/chapitre/<int:chapitre_id>/toggle/` | `admin_toggle_chapitre` | POST |
| `exit_preview` | `/admin-panel/preview/exit/` | `exit_preview_view` | GET |
| `preview_niveau` | `/admin-panel/preview/<str:niveau>/` | `preview_niveau_view` | GET |
| `admin_analytics` | `/admin-panel/analytics/` | `admin_analytics_view` | GET |
| `admin_test_report` | `/admin-panel/rapport-tests/` | `admin_test_report_view` | GET |
| `admin_serve_report` | `/admin-panel/rapport-tests/raw/` | `admin_serve_test_report` | GET |

### 2.3 `courses/urls.py` (prefix: `/cours/`)

| Name | Full Pattern | View | Methods |
|------|-------------|------|---------|
| `matieres` | `/cours/` | `matieres_view` | GET |
| `revisions` | `/cours/revisions/` | `revisions_view` | GET |
| `soumettre_revisions` | `/cours/revisions/soumettre/` | `soumettre_revisions` | POST |
| `chapitre` | `/cours/chapitre/<int:chapitre_pk>/` | `chapitre_view` | GET |
| `quiz_chapitre` | `/cours/chapitre/<int:chapitre_pk>/quiz/` | `quiz_chapitre_view` | GET |
| `lecon` | `/cours/lecon/<int:lecon_pk>/` | `lecon_view` | GET |
| `quiz` | `/cours/lecon/<int:lecon_pk>/quiz/` | `quiz_view` | GET |
| `lecon_pdf` | `/cours/lecon/<int:lecon_pk>/pdf/` | `lecon_pdf_view` | GET |
| `recherche` | `/cours/recherche/` | `recherche_view` | GET |
| `catalogue_matiere` | `/cours/<slug:matiere_slug>/` | `catalogue_matiere_view` | GET (public) |
| `lecon_publique` | `/cours/<slug:matiere_slug>/<str:niveau>/<slug:chapitre_slug>/<slug:lecon_slug>/` | `lecon_publique_view` | GET (public) |

### 2.4 `progress/urls.py` (prefix: `/progression/`)

| Name | Full Pattern | View | Methods |
|------|-------------|------|---------|
| `terminer_lecon` | `/progression/terminer/<int:lecon_pk>/` | `terminer_lecon` | POST |
| `soumettre_quiz` | `/progression/quiz/<int:lecon_pk>/soumettre/` | `soumettre_quiz` | POST |
| `soumettre_quiz_chapitre` | `/progression/quiz-chapitre/<int:chapitre_pk>/soumettre/` | `soumettre_quiz_chapitre` | POST |
| `sauvegarder_note` | `/progression/note/<int:lecon_pk>/sauvegarder/` | `sauvegarder_note` | POST |

---

## 3. Views

### 3.1 `config/views.py`

| View | Decorators | Purpose |
|------|-----------|---------|
| `custom_404` | — | Renders `404.html` |
| `custom_500` | — | Renders `500.html` (self-contained) |
| `health_view` | — | Returns `{"status":"ok"}`, no auth, no DB |

### 3.2 `users/views.py`

| View | Decorators | Purpose | Key Logic |
|------|-----------|---------|-----------|
| `ConnexionView` (CBV) | — | Login page | Redirects if auth; logs `ConnexionLog` with IP on success |
| `InscriptionView` (CBV) | — | Registration page | Sets `is_active=False`; unlocks 1st chapters; sends email verification |
| `deconnexion_view` | — | Logout | Redirects to `connexion` |
| `TableauDeBordView` (CBV) | `@login_required` | Dashboard router | Admin → `_dashboard_admin`; Eleve → `_dashboard_eleve` |
| `_dashboard_eleve` | — (private) | Student dashboard | Per-subject stats, streak, 30-day score Chart.js, revisions CTA, weak chapters (<70%) |
| `_dashboard_admin` | — (private) | Admin dashboard | nb_eleves, nb_chapitres, nb_lecons, eleves_par_niveau, derniers_inscrits |
| `ProfilView` (CBV) | `@login_required` | Profile + password edit | Handles `action=profil` and `action=mot_de_passe` |
| `admin_utilisateurs` | `@login_required` | Admin: list students | Filters: niveau, search (nom/prenom/email), actif; batch progression calc |
| `admin_toggle_actif` | `@login_required` | Admin: activate/deactivate student | POST only |
| `admin_eleve_detail` | `@login_required` | Admin: student detail | Progression, chapitres, connexion chart, cumulative progression chart |
| `admin_toggle_chapitre` | `@login_required` | Admin: lock/unlock a chapter for student | POST only; creates/deletes `ChapitreDebloque` |
| `preview_niveau_view` | `@login_required` | Admin: enter preview mode | Sets `session["preview_niveau"]`; valid values: `seconde`, `premiere`, `terminale` |
| `exit_preview_view` | `@login_required` | Admin: exit preview mode | Pops `session["preview_niveau"]` |
| `inscription_confirmation_view` | — | Post-registration confirmation page | |
| `verifier_email_view` | — | Email verification link handler | `signing.loads(token, salt="email-verification", max_age=86400)`; activates user + auto-login |
| `admin_analytics_view` | `@login_required` | Admin: analytics dashboard | Weak questions (<40%), lesson completion %, chapter quiz pass rates |
| `admin_test_report_view` | `@login_required` | Admin: test report iframe wrapper | Parses `test_report.html` for stats |
| `admin_serve_test_report` | `@login_required` | Admin: serves raw test_report.html | For iframe src |

Private helpers: `_envoyer_email_verification(request, user)`, `_debloquer_premiers_chapitres(user)`

### 3.3 `courses/views.py`

| View | Decorators | Purpose | Key Logic |
|------|-----------|---------|-----------|
| `matieres_view` | `@login_required` | List subjects + chapters | Respects `preview_niveau` session; admin sees all niveaux; student filtered by niveau |
| `chapitre_view` | `@login_required` | Chapter detail: list lessons | Checks niveau + unlock; shows chapter quiz CTA if all lessons done |
| `lecon_view` | `@login_required` | Display lesson (Markdown→HTML) | Auto-marks `en_cours`; skips writes in preview; renders video (YouTube/file); injects note |
| `quiz_view` | `@login_required` | Display quiz | Random sample of 5 from all questions; hidden `question_ids` field |
| `quiz_chapitre_view` | `@login_required` | Display chapter quiz | `_selectionner_questions_chapitre()`: 4 facile + 4 moyen + 2 difficile (10 total) |
| `revisions_view` | `@login_required` | Spaced repetition quiz | Leitner: due questions (≤today), ordered by box asc, max 10 |
| `soumettre_revisions` | `@login_required` | Submit revision answers | Rate-limited; IDOR check on niveau; updates Leitner boxes |
| `catalogue_matiere_view` | — (public) | Public subject catalogue | Lists chapters by niveau with lesson list; shows `gratuit` badge |
| `lecon_publique_view` | — (public) | Public free lesson view | Non-free → redirect to login; authenticated → redirect to PK view |
| `accueil_view` | — (public) | Homepage for anon users | All matières + chapitres + leçons with gratuit flag |
| `recherche_view` | `@login_required` | Full-text search | PostgreSQL `SearchVector` on titre (A) + contenu (B); min 2 chars; max 20 results |
| `lecon_pdf_view` | `@login_required` | PDF export | WeasyPrint; LaTeX→SVG via `render_markdown_to_html(latex_to_svg=True)` |

Private helpers: `_selectionner_questions_chapitre(chapitre, nb_total=10)`, `_extraire_youtube_id(url)`, `_generer_video_html(lecon, youtube_id)`

### 3.4 `progress/views.py`

| View | Decorators | Purpose | Key Logic |
|------|-----------|---------|-----------|
| `terminer_lecon` | `@require_POST`, `@login_required` | Mark no-quiz lesson as done | Sets `TERMINE` + checks chapter unlock; HTMX: returns `HX-Redirect` |
| `soumettre_quiz` | `@require_POST`, `@login_required` | Submit lesson quiz answers | Rate-limited (30/min); uses `_evaluer_reponses()`; keeps best score; Leitner update; unlocks next chapter if pass |
| `soumettre_quiz_chapitre` | `@require_POST`, `@login_required` | Submit chapter quiz answers | Rate-limited; score_minimum=80%; uses `_evaluer_reponses()`; Leitner update; unlocks next chapter |
| `sauvegarder_note` | `@require_POST`, `@login_required` | HTMX auto-save lesson note | `update_or_create`; max 2000 chars; returns green checkmark HTML |

Private helpers: `_check_quiz_rate_limit(user_id)` (30 req/min, cache-based), `_evaluer_reponses(questions, post_data)`, `_comparer_texte_libre(reponse, question)`, `_verifier_deblocage_chapitre_suivant(user, chapitre)`, `_enregistrer_historique_questions(user, corrections)`

---

## 4. Forms

| Form | Parent | Fields | Validation Notes |
|------|--------|--------|------------------|
| `ConnexionForm` | `AuthenticationForm` | `username` (email), `password` | Custom error messages (French) |
| `InscriptionForm` | `ModelForm(CustomUser)` | `prenom`, `nom`, `email`, `niveau`, `password1`, `password2` | Password: ≥8 chars + 1 uppercase + 1 digit; email uniqueness (lowercase); niveau required; saves as `role=eleve` + `is_active` left to view |
| `ProfilForm` | `ModelForm(CustomUser)` | `prenom`, `nom`, `email`, `niveau` | Standard ModelForm |
| `MotDePasseForm` | `forms.Form` | `ancien`, `nouveau1`, `nouveau2` | Match check; ≥8 chars; old password verified in view |

All widgets use Tailwind classes: `w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent`

---

## 5. Templates

### 5.1 Root

| Template | Description |
|----------|-------------|
| `base.html` | Master layout: sidebar, header, dark mode toggle + global CSS overrides, KaTeX, HTMX, Alpine.js, Tailwind CDN |
| `404.html` | Custom 404 page (extends `base.html`) |
| `500.html` | Custom 500 page (self-contained HTML, no extends) |

### 5.2 `components/`

| Template | Description |
|----------|-------------|
| `nav_item.html` | Reusable sidebar nav item |

### 5.3 `courses/`

| Template | Description |
|----------|-------------|
| `_chapitre_card.html` | Partial: chapter card component |
| `accueil.html` | Public homepage (all subjects/chapters) |
| `catalogue.html` | Public subject catalogue page |
| `chapitres.html` | Chapter detail: lesson list + chapter quiz CTA |
| `lecon.html` | Lesson view (Markdown content + video + notes + quiz link) |
| `lecon_pdf.html` | PDF-specific layout for WeasyPrint |
| `lecon_publique.html` | Public free lesson (read-only, no progression) |
| `matieres.html` | Subjects list with chapters per niveau |
| `quiz.html` | Quiz form (QCM / Vrai-Faux / Texte libre) |
| `quiz_chapitre.html` | Chapter quiz form |
| `quiz_resultat.html` | Lesson quiz results page |
| `quiz_chapitre_resultat.html` | Chapter quiz results page |
| `recherche.html` | Full-text search UI + results |
| `revisions.html` | Spaced repetition quiz + Leitner box display |
| `revisions_resultat.html` | Spaced repetition results |

### 5.4 `dashboard/`

| Template | Description |
|----------|-------------|
| `admin.html` | Admin dashboard (stats, derniers inscrits) |
| `admin_analytics.html` | Admin analytics (weak questions, completion, pass rates) |
| `admin_eleve_detail.html` | Admin: single student detail with charts |
| `admin_test_report.html` | Admin: test report iframe wrapper |
| `admin_users.html` | Admin: student management list |
| `eleve.html` | Student dashboard (per-subject progress, streak, Chart.js trend, revisions) |

### 5.5 `registration/`

| Template | Description |
|----------|-------------|
| `login.html` | Login page |
| `register.html` | Registration page |
| `inscription_confirmation.html` | Post-registration email verification notice |
| `email_verification_invalid.html` | Bad/expired verification token |
| `password_reset.html` | Password reset request form |
| `password_reset_done.html` | Password reset email sent confirmation |
| `password_reset_confirm.html` | New password form (from email link) |
| `password_reset_complete.html` | Password reset success |
| `password_reset_email.html` | Password reset email body |
| `password_reset_subject.txt` | Password reset email subject |

### 5.6 `users/`

| Template | Description |
|----------|-------------|
| `profile.html` | User profile + password change |

---

## 6. Settings Summary (`config/settings/base.py`)

| Setting | Value |
|---------|-------|
| `AUTH_USER_MODEL` | `users.CustomUser` |
| `LOGIN_URL` | `connexion` |
| `LOGIN_REDIRECT_URL` | `tableau_de_bord` |
| `LOGOUT_REDIRECT_URL` | `connexion` |
| `SESSION_COOKIE_AGE` | 1209600 (2 weeks) |
| `LANGUAGE_CODE` | `fr-fr` |
| `TIME_ZONE` | `Europe/Paris` |
| `DEFAULT_AUTO_FIELD` | `BigAutoField` |
| `STATICFILES_STORAGE` | `whitenoise.storage.CompressedManifestStaticFilesStorage` |
| `STATIC_URL` | `/static/` |
| `MEDIA_URL` | `/media/` |
| `ROOT_URLCONF` | `config.urls` |
| `AXES_FAILURE_LIMIT` | 5 |
| `AXES_COOLOFF_TIME` | 1 (hour) |
| `AXES_RESET_ON_SUCCESS` | True |
| `AXES_BEHIND_REVERSE_PROXY` | True |
| `INSTALLED_APPS` | django defaults + `django_htmx`, `axes`, `users`, `courses`, `progress`, `django.contrib.sitemaps`, `django.contrib.postgres` |
| `AUTHENTICATION_BACKENDS` | `AxesStandaloneBackend`, `ModelBackend` |
| `MIDDLEWARE` (order) | SecurityMiddleware → WhiteNoise → Session → Common → Csrf → Auth → Axes → Messages → XFrame → Htmx |
| Context processors | default 4 + `users.context_processors.test_report_status` |
| Password validators | UserAttributeSimilarity, MinLength(8), Common, Numeric |
| Admin credentials | `FIRST_ADMIN_EMAIL`, `FIRST_ADMIN_PASSWORD` (from `.env`) |
| DB config | `DATABASE_URL` env var → `dj_database_url`; fallback: individual `POSTGRES_*` env vars |
| Logging | Console handler, WARNING root, INFO for `courses`/`progress`/`users` |

---

## 7. Management Commands

| Command | File | Purpose |
|---------|------|---------|
| `seed_data` | `seed_data.py` | Idempotent: creates admin + sample Matière/Chapitre/Lecon (Terminale) |
| `seed_content` | `seed_content.py` | Seed content (Terminale base) |
| `seed_content_new` | `seed_content_new.py` | Additional Terminale content |
| `seed_content_tail` | `seed_content_tail.py` | Terminale tail content |
| `seed_chimie_seconde` | `seed_chimie_seconde.py` | Chimie Seconde chapters + lessons + quizzes |
| `seed_physique_seconde` | `seed_physique_seconde.py` | Physique Seconde chapters + lessons + quizzes |
| `seed_maths_seconde` | `seed_maths_seconde.py` | Maths Seconde chapters + lessons + quizzes |
| `seed_chimie_premiere` | `seed_chimie_premiere.py` | Chimie Première chapters + lessons + quizzes |
| `seed_physique_premiere` | `seed_physique_premiere.py` | Physique Première chapters + lessons + quizzes |
| `seed_maths_premiere` | `seed_maths_premiere.py` | Maths Première chapters + lessons + quizzes |
| `seed_chimie_orga_terminale` | `seed_chimie_orga_terminale.py` | Chimie orga Terminale content |
| `pad_quiz_questions` | `pad_quiz_questions.py` | Pads quizzes to ensure minimum question count |
| `import_questions` | `import_questions.py` | CSV import: columns `quiz_lecon_slug`, `texte`, `type`, `reponse_correcte`, `options`, `tolerances`, `difficulte`; supports `--dry-run` |

---

## 8. Key Patterns

### 8.1 Colour System (`MATIERE_COULEURS`)

```python
MATIERE_COULEURS = {
    "physique": {
        "bg": "bg-blue-600",
        "light": "bg-blue-50",
        "text": "text-blue-600",
        "border": "border-blue-200",
        "hex": "#2563eb",
    },
    "chimie": {
        "bg": "bg-emerald-600",
        "light": "bg-emerald-50",
        "text": "text-emerald-600",
        "border": "border-emerald-200",
        "hex": "#059669",
    },
    "mathematiques": {
        "bg": "bg-purple-600",
        "light": "bg-purple-50",
        "text": "text-purple-600",
        "border": "border-purple-200",
        "hex": "#7c3aed",
    },
}
```

Icons: physique=⚛, chimie=🧪, mathematiques=∑

### 8.2 Preview Mode

- **Entry**: admin hits `/admin-panel/preview/<niveau>/` → `session["preview_niveau"]` = `seconde|premiere|terminale`
- **Exit**: `/admin-panel/preview/exit/` → pops session key
- **Effect**: `matieres_view` and `lecon_view` filter by `preview_niveau` instead of `user.niveau`; `lecon_view` skips progression writes when preview is active
- **Banner**: yellow notice shown in `base.html` when session key is set

### 8.3 Quiz Evaluation (`_evaluer_reponses`)

1. For each question, compare `post_data[f"question_{question.id}"]` with `question.reponse_correcte` (case-insensitive)
2. If QCM: compare index string. If texte_libre and initial match fails: call `_comparer_texte_libre()`
3. `_comparer_texte_libre`: normalized lowercase+strip comparison against `reponse_correcte` + all `tolerances[]`
4. Returns `(corrections[], points_obtenus, total_points)`
5. Lesson quiz needs `score >= quiz.score_minimum` (default 60%)
6. Chapter quiz needs `score >= 80%`

### 8.4 Chapter Unlock Logic (`_verifier_deblocage_chapitre_suivant`)

1. Check `UserChapitreQuizResultat.passe=True` for current chapter
2. If passed → find next chapter with same `matiere`, `niveau`, `ordre+1`
3. Create `ChapitreDebloque` for next chapter
4. First chapters (ordre=1) auto-unlocked at registration via `_debloquer_premiers_chapitres()`

### 8.5 Leitner Spaced Repetition

- 5 boxes: `{1: 1d, 2: 3d, 3: 7d, 4: 14d, 5: 30d}`
- Correct answer → box+1 (max 5). Wrong answer → box 1
- `prochaine_revision = today + LEITNER_INTERVALLES[new_box]`
- `_enregistrer_historique_questions(user, corrections)` — called by `soumettre_quiz`, `soumettre_quiz_chapitre`, `soumettre_revisions`
- `revisions_view` selects due questions (`prochaine_revision <= today`), ordered by box asc, max 10
- Mastered = box ≥ 4

### 8.6 Rate Limiting

- **Login**: `django-axes` — `AXES_FAILURE_LIMIT=5`, `AXES_COOLOFF_TIME=1h`
- **Quiz submissions**: `_check_quiz_rate_limit(user_id)` — cache key `quiz_rate_{user_id}`, 30 req/min (60s TTL); returns HTTP 429 when exceeded
- Applied to: `soumettre_quiz`, `soumettre_quiz_chapitre`, `soumettre_revisions`

### 8.7 Context Processor

| Processor | Location | Purpose |
|-----------|----------|---------|
| `test_report_status` | `users/context_processors.py` | Injects test report stats (passed/failed/error/total/status) for admins only |

Parses `backend/test_report.html`; status: `green` (0 failures), `orange` (1-3 failures), `red` (>3 failures or errors)

### 8.8 Email Verification Flow

1. `InscriptionView.post()` → `user.is_active = False` → `_envoyer_email_verification()`
2. Token: `signing.dumps(user.pk, salt="email-verification")`
3. Link: `/verifier-email/<token>/` → `verifier_email_view`
4. Validates with `signing.loads(token, salt="email-verification", max_age=86400)` (24h)
5. Success: activates user + auto-login. Failure: HTTP 400 with reason (`expiré` or `invalide`)

### 8.9 Sitemaps

| Sitemap | Location | Content |
|---------|----------|---------|
| `CatalogueSitemap` | `courses/sitemaps.py` | All matières catalogue pages |
| `LeconPubliqueSitemap` | `courses/sitemaps.py` | Only lessons with `gratuit=True` |

### 8.10 PDF Export

1. `lecon_pdf_view` → `render_markdown_to_html(lecon.contenu, latex_to_svg=True)`
2. LaTeX equations compiled via `texlive` → DVI → `dvisvgm` → inline SVG
3. Rendered with `courses/lecon_pdf.html` template
4. `WeasyPrint` generates final PDF
5. Helpers in `courses/utils/latex_parser.py`: `proteger_latex()`, `restaurer_latex()`

### 8.11 Full-Text Search

- PostgreSQL `SearchVector("titre", weight="A") + SearchVector("contenu", weight="B")`, config=`french`
- Min query length: 2 chars; max results: 20
- Students filtered by `chapitre__niveau=user.niveau`; admins see all
