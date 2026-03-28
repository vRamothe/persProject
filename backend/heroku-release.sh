#!/bin/sh
set -eu

echo ">> Python version"
python --version

if [ -z "${DATABASE_URL:-}" ]; then
	echo ">> DATABASE_URL is not set yet. Skipping DB-dependent release tasks."
	echo ">> This release is allowed so Heroku can apply config vars/addons."
	exit 0
fi

echo ">> Django checks"
python manage.py check --deploy

echo ">> Applying migrations"
python manage.py migrate --noinput --verbosity 2

echo ">> Loading seed data"
python manage.py seed_data

echo ">> Release phase completed"