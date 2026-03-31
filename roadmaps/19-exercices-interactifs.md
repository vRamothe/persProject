# 19 — Exercices Interactifs

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #23 |
| **Phase** | 4 — Learning Experience |
| **Type** | Tech |
| **LLM recommandé** | **Opus** (nécessaire — 3 nouveaux types questions, schémas JSON complexes, HTML5 DnD API, évaluation proportionnelle) |
| **Statut** | ⬜ À faire |
| **Priorité** | 19 |
| **Dépendances** | Aucune |

---

## Description

3 nouveaux types de questions interactives : glisser-déposer, texte à trous, association de colonnes. Chaque type est une extension de `TypeQuestionChoices` avec des composants Alpine.js dédiés. Évaluation côté serveur étendue dans `_evaluer_reponses()` avec score proportionnel.

## Critères d'acceptation

- Nouveaux types : `glisser_deposer`, `texte_a_trous`, `association`
- **Glisser-déposer** : ordonner/placer des éléments dans zones cibles (HTML5 Drag & Drop)
- **Texte à trous** : texte avec `___` → inputs, case-insensitive, tolérances
- **Association** : deux colonnes à relier (select par ligne)
- Utilisables dans quiz leçon, chapitre et révisions Leitner
- Évaluation 100% côté serveur, score proportionnel

## Architecture

- **Schémas JSON** dans `options` / `reponse_correcte` :
  - DnD : `items[]`, `zones[]` → mapping zone→item
  - Trous : `texte` avec `___`, `blancs` count → réponses ordonnées + tolérances par blanc
  - Association : `gauche[]`, `droite[]` → mapping gauche→droite
- **Vues** : extension `_evaluer_reponses()` avec comparateur par type
- **Templates** : composants Alpine.js inline (<50 lignes chacun) dans `quiz.html`
- **Template filter** (optionnel) : `quiz_filters.py` pour render_blanks
- **Import CSV** : extension pour nouveaux types (JSONFields existants)
- **Rendu sécurisé** : `json_script` (pas `|safe`) pour les options

## Tests

- DnD : correct full score, partial score
- Trous : correct, tolérances, case-insensitive
- Association : correct pairs, partial
- Fonctionnent dans quiz chapitre et révisions
- Import CSV nouveaux types

## Sécurité

- **A03** : `json_script` au lieu de `|safe` — pas d'injection XSS
- **A04** : évaluation serveur uniquement, JS collecte les réponses
- **A08** : validation schéma JSON à l'import CSV et admin
- Association : colonne droite mélangée côté serveur (pas côté client)

## Performance

- +0 requête SQL (options/reponse_correcte déjà chargés en JSONField)
- HTML5 DnD natif, pas de lib externe
- Composants Alpine inline (<50 lignes)

## Definition of Done

- 3 types fonctionnent dans quiz leçon/chapitre/révisions
- Score proportionnel, tolérances, case-insensitive
- DnD fonctionne desktop + mobile (touch events)
- Import CSV supporte les nouveaux types
- Tests passent, CODEBASE_REFERENCE.md à jour
