# 18 — Glossaire / Fiches de Formules

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #22 |
| **Phase** | 4 — Learning Experience |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — modèle simple, vue, template Alpine.js, commande management) |
| **Statut** | ⬜ À faire |
| **Priorité** | 18 |
| **Dépendances** | Aucune |

---

## Description

Page de référence consultable par matière avec termes clés, définitions et formules LaTeX. Modèle `EntreeGlossaire` avec extraction automatique depuis le Markdown des leçons. Admin valide les entrées. Recherche Alpine.js côté client + filtre par chapitre. KaTeX pour les formules.

## Critères d'acceptation

- `EntreeGlossaire` : terme, définition, formule LaTeX, matière FK, chapitre FK, leçon source FK, validée bool
- Page `/cours/glossaire/<slug:matiere_slug>/` avec entrées groupées par chapitre
- Recherche côté client (Alpine.js `x-show`) sur terme + définition
- Filtre par chapitre (dropdown ou tabs)
- Formules rendues via KaTeX
- Commande `extraire_glossaire` parse `**terme**` et `$...$` dans les leçons

## Architecture

- **Modèle** (`courses/models.py`) : `EntreeGlossaire` avec `unique_together [matiere, terme]`
- **Vue** : `glossaire_view(request, matiere_slug)` — `@login_required`, filter validée=True
- **URL** : `glossaire` → `/cours/glossaire/<slug:matiere_slug>/`
- **Template** : `templates/courses/glossaire.html` — Alpine.js `x-data="{ search: '', chapitre: 'all' }"`
- **Commande** : `extraire_glossaire.py` — parse leçons, crée entrées `validee=False`
- **Admin** : `EntreeGlossaireAdmin` avec action batch "Valider"
- **Sidebar** : lien "📖 Glossaire"

## Tests

- `test_glossaire_page_returns_200`
- `test_glossaire_excludes_non_validated`
- `test_glossaire_groups_by_chapitre`
- `test_glossaire_search_markup_present`
- `test_extraire_glossaire_creates_candidates`
- `test_glossaire_requires_login`

## Sécurité

- `@login_required`, entrées auto-escaped, KaTeX sandboxé

## Performance

- 1 requête SQL (filter + select_related)
- Filtrage côté client — 0 requête supplémentaire
- Index `(matiere_id, validee)`

## Definition of Done

- Glossaire fonctionnel avec KaTeX
- Commande extraction, admin validation
- Lien sidebar
- Tests passent, CODEBASE_REFERENCE.md à jour
