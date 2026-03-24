---
description: "Deploy ScienceLycée to Heroku production"
agent: "Heroku Deploy"
argument-hint: "What to deploy: 'full deploy', 'update env vars', 'diagnose failed release', 'rollback'"
---
Deploy or manage the Heroku production environment for ScienceLycée.

Context:
- Container deploy via `heroku.yml`
- Release phase runs `heroku-release.sh` (migrate + collectstatic)
- Required env vars: SECRET_KEY, DATABASE_URL, SENTRY_DSN, BREVO_SMTP_*, FIRST_ADMIN_EMAIL/PASSWORD
