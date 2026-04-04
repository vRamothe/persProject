#!/bin/bash
set -e

echo "=================================================="
echo "🌐 Tests E2E ScienceLycée (Playwright)"
echo "=================================================="

VENV_DIR="e2e/.venv"

# Vérifier que l'app tourne
echo "🔍 Vérification que l'app est accessible sur http://localhost..."
if ! curl -s -o /dev/null -w "%{http_code}" http://localhost/health/ | grep -q "200"; then
    echo "❌ L'app n'est pas accessible sur http://localhost"
    echo "   Lance d'abord : docker compose up --build -d"
    exit 1
fi
echo "✅ L'app est accessible"

# Créer le venv si nécessaire
if [ ! -f "$VENV_DIR/bin/activate" ]; then
    # Nettoyer un éventuel venv cassé
    rm -rf "$VENV_DIR"
    echo "📦 Création du virtualenv E2E..."

    # Vérifier que le module venv est disponible
    if ! python3 -c "import venv; import ensurepip" 2>/dev/null; then
        echo "⚠️  Le module python3-venv n'est pas installé."
        echo "   Installation automatique..."
        sudo apt update -qq && sudo apt install -y python3-venv 2>/dev/null || {
            PYTHON_VERSION=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
            echo "❌ Impossible d'installer python3-venv automatiquement."
            echo "   Lance manuellement : sudo apt install python3.${PYTHON_VERSION##*.}-venv python3-venv"
            exit 1
        }
    fi

    python3 -m venv "$VENV_DIR" || {
        echo "❌ Échec de la création du virtualenv."
        echo "   Essaie : sudo apt install python3-full"
        exit 1
    }
fi

# Activer le venv
source "$VENV_DIR/bin/activate"

# Installer les dépendances pip si Playwright n'est pas installé
if ! python3 -c "import playwright" 2>/dev/null; then
    echo "📦 Installation des dépendances E2E..."
    python3 -m pip install --upgrade pip -q
    python3 -m pip install -r e2e/requirements.txt -q
    echo "🌐 Installation du navigateur Chromium..."
    python3 -m playwright install chromium
fi

# Installer les dépendances système si manquantes (une seule fois)
DEPS_MARKER="$VENV_DIR/.deps-installed"
if [ ! -f "$DEPS_MARKER" ]; then
    echo "🔧 Installation des dépendances système pour Chromium..."
    # Utiliser le chemin absolu du playwright du venv (sudo reset PATH)
    PLAYWRIGHT_BIN="$(cd "$(dirname "$0")" && pwd)/$VENV_DIR/bin/playwright"
    if sudo "$PLAYWRIGHT_BIN" install-deps chromium; then
        touch "$DEPS_MARKER"
    else
        echo "⚠️  Échec de l'installation automatique des deps système."
        echo "   Lance manuellement :"
        echo "     sudo $PLAYWRIGHT_BIN install-deps chromium"
        echo "   Ou :"
        echo "     sudo apt-get install libasound2t64"
        exit 1
    fi
fi

echo ""
echo "🚀 Lancement des tests E2E..."
cd e2e && python3 -m pytest -v --html=e2e_test_report.html --self-contained-html "$@"
EXIT_CODE=$?

# Copier le rapport dans backend/ à côté du rapport unitaire
if [ -f e2e_test_report.html ]; then
    cp e2e_test_report.html ../backend/e2e_test_report.html
fi

deactivate 2>/dev/null

echo ""
echo "=================================================="
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Tous les tests E2E sont passés !"
    echo "📊 Rapport E2E : backend/e2e_test_report.html"
else
    echo "❌ Certains tests E2E ont échoué."
    echo "📊 Rapport E2E : backend/e2e_test_report.html"
fi
echo "=================================================="
exit $EXIT_CODE
