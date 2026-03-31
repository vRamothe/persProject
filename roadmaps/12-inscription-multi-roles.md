# 12 — Inscription Multi-Rôles

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP_ROLES.md — Phase 2 (Étapes 2.1 à 2.4) |
| **Phase** | Roles — Phase 2 |
| **Type** | Tech |
| **LLM recommandé** | **Opus** (nécessaire — 3 formulaires, helpers, rate limiting, transaction.atomic, 4 templates, backward compat) |
| **Statut** | ⬜ À faire |
| **Priorité** | 12 |
| **Dépendances** | #11 Modèles Multi-Rôles |
| **Bloque** | #13 Validation Liaisons |

---

## Description

Remplacer le formulaire d'inscription unique par un système en 2 étapes : choix du rôle → formulaire spécialisé par rôle. Chaque rôle a sa propre logique de création de compte, de liaison optionnelle (code enseignant / code élève), et de vérification email.

## Sous-étapes

### 2.1 — Formulaires
- `InscriptionEleveForm` : prenom, nom, email, niveau, passwords, code_enseignant (optionnel)
- `InscriptionEnseignantForm` : prenom, nom, email, passwords (pas de niveau, pas de code)
- `InscriptionParentForm` : prenom, nom, email, passwords, code_eleve (obligatoire)
- Validation codes : messages génériques anti-énumération ("Code invalide ou inactif.")
- `save()` met `is_active=False` et le bon rôle

### 2.2 — Helpers et Vues
- `users/helpers.py` (nouveau) : `_creer_lien_enseignant(eleve, code)`, `_creer_lien_parent(parent, code)`
- `choix_role_view`, `inscription_eleve_view`, `inscription_enseignant_view`, `inscription_parent_view`
- `transaction.atomic()` dans chaque vue POST
- Rate limiting : 5 tentatives/h/IP sur POST avec code
- `_get_client_ip(request)` helper

### 2.3 — Templates
- `choix_role.html` : 3 cartes (Élève/Enseignant/Parent), `{% block full_content %}`
- `register_eleve.html`, `register_enseignant.html`, `register_parent.html`
- Dark mode toggle + anti-flash, `noindex,nofollow`

### 2.4 — URLs
- `/inscription/choix/`, `/inscription/eleve/`, `/inscription/enseignant/`, `/inscription/parent/`
- Ancien `/inscription/` → redirect 301 vers `/inscription/choix/`

## Tests (18+ minimum)

- Tests GET 200 pour chaque page
- Tests POST avec/sans code, codes invalides, email dupliqué
- Tests `is_active=False`, `_debloquer_premiers_chapitres`, email vérification
- Tests backward compat redirect 301
- Tests rate limiting 429

## Sécurité

- Enumération : message unique "Code invalide ou inactif."
- Rate limit 5/h/IP sur codes
- `strip()` + `lower()` email, `strip()` + `upper()` codes
- Token email signé (existant) : 24h expiry
- `transaction.atomic()` empêche états incohérents

## Performance

- Lookup code_identifiant : O(1) via index unique
- Rate limit via cache mémoire — aucune requête DB

## Definition of Done

- Les 3 formulaires créés avec validation
- Helpers dans `users/helpers.py`
- 4 vues + 4 templates + 4 URLs
- Redirect 301 backward compat
- Migration vers `users/tests/` avec conftest
- Tests passent, CODEBASE_REFERENCE.md à jour
