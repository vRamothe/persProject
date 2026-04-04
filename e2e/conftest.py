"""
Fixtures partagées pour les tests E2E Playwright.
L'app doit tourner en local via docker compose avant de lancer les tests.

Credentials admin lus depuis le fichier .env à la racine du projet
(FIRST_ADMIN_EMAIL / FIRST_ADMIN_PASSWORD), identiques à ceux de seed_data.
"""
import logging
import os
import re

import pytest
from decouple import Config, RepositoryEnv
from playwright.sync_api import Page

# ─── Hook de logging structuré (même format que backend/conftest.py) ───

logger = logging.getLogger("test_info")
logger.setLevel(logging.INFO)

_FIELD_PATTERNS = {
    "teste": re.compile(r"Teste\s*:\s*(.+)", re.IGNORECASE),
    "raison": re.compile(r"Raison\s*:\s*(.+)", re.IGNORECASE),
    "features": re.compile(r"Features?\s*:\s*(.+)", re.IGNORECASE),
    "criticite": re.compile(r"Criticit[ée]\s*:\s*(.+)", re.IGNORECASE),
}

_SEPARATOR = "═" * 63


def _parse_structured_docstring(docstring):
    """Extrait les champs structurés d'une docstring."""
    fields = {}
    for key, pattern in _FIELD_PATTERNS.items():
        match = pattern.search(docstring)
        if match:
            fields[key] = match.group(1).strip()
    return fields


def pytest_runtest_setup(item):
    """Log les informations structurées du test avant son exécution."""
    try:
        cls = item.cls
        class_name = cls.__name__ if cls else None
        test_name = item.name
        display_name = f"{class_name}.{test_name}" if class_name else test_name

        docstring = item.function.__doc__

        lines = [_SEPARATOR, f"🧪 TEST: {display_name}"]

        if docstring:
            fields = _parse_structured_docstring(docstring)
            if fields:
                lines.append(f"📋 Teste: {fields.get('teste', 'Non documenté')}")
                if "raison" in fields:
                    lines.append(f"❓ Raison: {fields['raison']}")
                if "features" in fields:
                    lines.append(f"🔗 Features: {fields['features']}")
                if "criticite" in fields:
                    lines.append(f"⚠️  Criticité: {fields['criticite']}")
            else:
                raw = docstring.strip().split("\n")[0].strip()
                lines.append(f"📋 Teste: {raw}")
        else:
            lines.append("📋 Teste: Non documenté")

        lines.append(_SEPARATOR)
        logger.info("\n".join(lines))

    except Exception:
        pass

# Lire le .env à la racine du projet (un niveau au-dessus de e2e/)
_env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
_config = Config(RepositoryEnv(_env_path))

ADMIN_EMAIL = _config("FIRST_ADMIN_EMAIL")
ADMIN_PASSWORD = _config("FIRST_ADMIN_PASSWORD")
BASE_URL = _config("E2E_BASE_URL", default="http://localhost")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def admin_credentials():
    """Retourne les credentials admin (depuis .env)."""
    return {"email": ADMIN_EMAIL, "password": ADMIN_PASSWORD}


@pytest.fixture
def admin_page(page: Page, base_url, admin_credentials):
    """Page connectée en tant qu'admin."""
    page.goto(f"{base_url}/connexion/")
    page.fill('input[name="username"]', admin_credentials["email"])
    page.fill('input[name="password"]', admin_credentials["password"])
    page.click('button[type="submit"]')
    # Attend la redirection vers le tableau de bord
    page.wait_for_url("**/tableau-de-bord/")
    return page


@pytest.fixture
def anonymous_page(page: Page, base_url):
    """Page non connectée (visiteur anonyme)."""
    return page
