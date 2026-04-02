"""
Hook pytest pour logger des informations structurées avant chaque test.
Parse la docstring du test pour extraire: Teste, Raison, Features, Criticité.
"""

import logging
import re

logger = logging.getLogger("test_info")
logger.setLevel(logging.INFO)

# Patterns pour extraire les champs structurés des docstrings
_FIELD_PATTERNS = {
    "teste": re.compile(r"Teste\s*:\s*(.+)", re.IGNORECASE),
    "raison": re.compile(r"Raison\s*:\s*(.+)", re.IGNORECASE),
    "features": re.compile(r"Features?\s*:\s*(.+)", re.IGNORECASE),
    "criticite": re.compile(r"Criticit[ée]\s*:\s*(.+)", re.IGNORECASE),
}

_SEPARATOR = "═" * 63


def _parse_structured_docstring(docstring):
    """Extrait les champs structurés d'une docstring. Retourne un dict (peut être vide)."""
    fields = {}
    for key, pattern in _FIELD_PATTERNS.items():
        match = pattern.search(docstring)
        if match:
            fields[key] = match.group(1).strip()
    return fields


def pytest_runtest_setup(item):
    """Log les informations structurées du test avant son exécution."""
    try:
        # Nom de la classe (ou module si pas de classe)
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
                # Docstring brute (première ligne non-vide)
                raw = docstring.strip().split("\n")[0].strip()
                lines.append(f"📋 Teste: {raw}")
        else:
            lines.append("📋 Teste: Non documenté")

        lines.append(_SEPARATOR)
        logger.info("\n".join(lines))

    except Exception:
        # Ne jamais crasher le test à cause du hook de logging
        pass
