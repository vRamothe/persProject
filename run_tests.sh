#!/bin/bash

echo "=================================================="
echo "🧪 Lancement de la suite de tests ScienceLycée"
echo "=================================================="

# On lance pytest avec l'option --self-contained-html pour que le CSS/JS
# soit inclus directement dans le fichier unique. Le plugin est dans requirements.txt.
docker compose run --rm --user root --entrypoint pytest web -v --html=test_report.html --self-contained-html

echo "=================================================="
echo "✅ Tests terminés !"
echo "📊 Le rapport est disponible ici : backend/test_report.html"
echo "🌐 Double-clique dessus pour l'ouvrir dans ton navigateur."
echo "=================================================="
