#!/bin/sh
set -eu

echo ">> Python version"
python --version

echo ">> Django checks"
python manage.py check --deploy --fail-level WARNING

echo ">> Applying migrations"
python manage.py migrate --noinput --verbosity 2

echo ">> Loading seed data"
python manage.py seed_data

echo ">> Collecting static files"
python manage.py collectstatic --noinput --clear --verbosity 2

echo ">> Release phase completed"