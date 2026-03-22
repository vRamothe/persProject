#!/usr/bin/env bash
set -euo pipefail

# Sync local courses data to Heroku
# Usage: ./scripts/sync_courses_to_heroku.sh <heroku-app-name>
#   e.g. ./scripts/sync_courses_to_heroku.sh sciencelycee
# reminder: app name is kogito could be kogito-<env> (e.g. kogito-prod, kogito-staging) in the future when we have multiple envs
APP_NAME="${1:-}"
DUMP_FILE="courses_dump.json"

if [[ -z "$APP_NAME" ]]; then
  echo "Usage: $0 <heroku-app-name>"
  exit 1
fi

echo "==> Exporting courses from local database..."
docker compose exec -T web python manage.py dumpdata courses --indent 2 > "$DUMP_FILE"
echo "    Created $DUMP_FILE ($(wc -l < "$DUMP_FILE") lines)"

echo "==> Committing dump file temporarily..."
git add "$DUMP_FILE"
git commit -m "temp: add courses dump for Heroku import"

echo "==> Pushing to Heroku ($APP_NAME)..."
git push heroku main

echo "==> Loading data on Heroku..."
heroku run python manage.py loaddata "$DUMP_FILE" --app "$APP_NAME"

echo "==> Cleaning up dump file from repo..."
git rm "$DUMP_FILE"
git commit -m "temp: remove courses dump"
git push heroku main

echo "==> Done! Courses synced to $APP_NAME."
