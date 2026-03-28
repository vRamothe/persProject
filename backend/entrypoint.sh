#!/bin/sh
set -e

# If a command is provided (e.g. Heroku process command), run it directly.
if [ "$#" -gt 0 ]; then
    exec "$@"
fi

echo ">> Application des migrations..."
python manage.py migrate --noinput

echo ">> Chargement des données initiales (terminale + admin)..."
python manage.py seed_data

echo ">> Chargement du contenu seconde..."
python manage.py seed_physique_seconde
python manage.py seed_chimie_seconde
python manage.py seed_maths_seconde

echo ">> Chargement du contenu première..."
python manage.py seed_physique_premiere
python manage.py seed_chimie_premiere
python manage.py seed_maths_premiere

echo ">> Chargement des compléments terminale..."
python manage.py seed_chimie_orga_terminale

echo ">> Complétion des quiz (20 QCM par quiz)..."
python manage.py pad_quiz_questions

echo ">> Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --clear

echo ">> Démarrage de Gunicorn..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 3 \
    --timeout 60 \
    --reload \
    --access-logfile - \
    --error-logfile -
