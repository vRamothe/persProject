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

echo ">> Loading seed data (terminale + admin)"
python manage.py seed_data

echo ">> Loading seconde content"
python manage.py seed_physique_seconde
python manage.py seed_chimie_seconde
python manage.py seed_maths_seconde

echo ">> Loading première content"
python manage.py seed_physique_premiere
python manage.py seed_chimie_premiere
python manage.py seed_maths_premiere

echo ">> Loading terminale extras"
python manage.py seed_chimie_orga_terminale

echo ">> Release phase completed"