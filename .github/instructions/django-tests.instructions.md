---
description: "Use when writing or editing pytest tests for ScienceLycée. Covers force_login requirement, fixture patterns, and test file locations."
applyTo: "**/tests.py"
---
# Django Tests — ScienceLycée Conventions

- Stack: `pytest` 8.3 + `pytest-django` 4.9, config in `backend/pytest.ini`
- Test files: `users/tests.py`, `courses/tests.py`, `progress/tests.py`
- **CRITICAL**: Always use `client.force_login(user)` — never `client.login(email=, password=)` (django-axes raises `AxesBackendRequestParameterRequired`)
- Fixtures: use `@pytest.fixture` for `admin_user` (role=admin), `eleve_user` (role=eleve, niveau=seconde), `matiere`, `chapitre`, `lecon`, `quiz`, `question`
- Factory pattern: create minimal test objects inline; use `Matiere.objects.create(nom="physique")` etc.
- Assertions: check HTTP status codes, template used (`assertTemplateUsed` equivalent), redirect targets, and DB state
- Quiz tests: test all question types (qcm, vrai_faux, texte_libre), tolerances, rate limiting
- Chapter unlock: test ≥80% pass threshold, `ChapitreDebloque` creation, next chapter access
- Admin views: test `role == 'admin'` gate (403 for eleve)
- Preview mode: test that progress is NOT written when `session["preview_niveau"]` is set
- Run: `docker compose run --rm --entrypoint pytest web -v --tb=short`
