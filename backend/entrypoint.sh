#!/bin/sh
set -e

# If a command is provided (e.g. Heroku process command), run it directly.
if [ "$#" -gt 0 ]; then
    exec "$@"
fi

echo ">> Application des migrations..."
python manage.py migrate --noinput

echo ">> Chargement des données initiales..."
python manage.py seed_data

echo ">> Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --clear

echo ">> Démarrage de Gunicorn..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 3 \
    --timeout 60 \
    --access-logfile - \
    --error-logfile -
