# Tests E2E — ScienceLycée (Playwright)

Tests end-to-end qui naviguent dans un vrai navigateur vers l'app Django tournant en local.

## Prérequis

1. **Python 3.12+** installé sur la machine hôte
2. **L'app doit tourner** via Docker Compose :
   ```bash
   docker compose up --build -d
   ```
3. Vérifier que `http://localhost/health/` répond `200`

## Installation

```bash
cd e2e
pip install -r requirements.txt
playwright install chromium
```

## Lancer les tests

### Via le script (depuis la racine du projet)

```bash
./run_e2e_tests.sh
```

### Manuellement

```bash
cd e2e
python3 -m pytest -v
```

### Lancer un fichier spécifique

```bash
cd e2e
python3 -m pytest test_smoke.py -v
python3 -m pytest test_paywall_preview.py -v
```

### Mode headed (voir le navigateur)

```bash
cd e2e
python3 -m pytest --headed -v
```

### Avec slowmo (ralentir pour debug)

```bash
cd e2e
python3 -m pytest --headed --slowmo 500 -v
```

## Credentials admin

Les credentials par défaut sont ceux créés par `seed_data` :
- **Email** : `admin@sciencelycee.fr`
- **Mot de passe** : `AdminPass123`

Pour les modifier, éditer les constantes dans `conftest.py`.

## Structure

```
e2e/
├── conftest.py              # Fixtures partagées (login admin, base_url, etc.)
├── pytest.ini               # Config pytest pour les tests E2E
├── requirements.txt         # Dépendances Python (Playwright, pytest)
├── test_smoke.py            # Smoke tests (app accessible, login, health)
├── test_paywall_preview.py  # Tests du mode preview paywall admin
└── README.md                # Ce fichier
```

## Ajouter des tests

1. Créer un fichier `test_<feature>.py` dans `e2e/`
2. Utiliser les fixtures `admin_page` (connecté admin) ou `anonymous_page` (visiteur)
3. Utiliser `base_url` pour construire les URLs
4. Suivre le pattern existant : docstrings avec criticité, classes de regroupement
