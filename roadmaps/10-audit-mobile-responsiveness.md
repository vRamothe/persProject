# 10 — Audit Mobile Responsiveness

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #17 |
| **Phase** | 3 — Scaling Traffic |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — HTML/CSS/Alpine.js uniquement) |
| **Statut** | ⬜ À faire |
| **Priorité** | 10 |
| **Dépendances** | Aucune |

---

## Description

La sidebar et certains composants (quiz KaTeX, tableaux Markdown, modal paywall) ne sont pas optimisés pour mobile (<768px). Corrections : sidebar hamburger/overlay, overflow KaTeX, formulaires quiz au pouce (≥44px), modal paywall full-screen. Aucune modification backend.

## Critères d'acceptation

- Sidebar cachée par défaut sur mobile, accessible via bouton hamburger (Alpine.js)
- Équations KaTeX ne provoquent pas de scroll horizontal (`overflow-x: auto`)
- Formulaires quiz utilisables au pouce (≥44px, espacement suffisant)
- Modal paywall full-screen sur mobile
- Tableaux larges wrappés dans `div.overflow-x-auto`
- Validé sur iPhone SE 375px, iPhone 14 390px, Pixel 7 412px

## Architecture

- **`base.html`** : sidebar `hidden md:block`, hamburger `md:hidden`, Alpine.js toggle + backdrop
- **`lecon.html`** : wrapper `overflow-x-auto` autour du contenu Markdown
- **`quiz.html` + `quiz_chapitre.html`** : `min-h-[44px]`, `py-3` sur radio buttons
- **`_paywall_modal.html`** : `w-full h-full md:max-w-lg md:h-auto`
- **KaTeX CSS** : `.katex-display { overflow-x: auto; max-width: 100%; }`
- **Hamburger** : SVG inline (3 barres / ✕)

## Tests

- `test_base_template_contains_hamburger_button` — `aria-label` "menu" + `md:hidden`
- `test_sidebar_has_responsive_hidden_class` — `hidden md:block`
- `test_lecon_template_has_overflow_wrapper` — `overflow-x-auto`
- `test_quiz_radio_buttons_have_sufficient_padding` — `min-h-` ou `py-3`

## Sécurité

- Pas d'impact — modifications purement CSS/HTML/Alpine.js

## Performance

- +0 requête SQL, JS Alpine minimal (<10 lignes)

## Definition of Done

- Sidebar responsive, KaTeX ne casse plus le layout mobile, quiz confortables au pouce
- Testé sur 3 viewports via Chrome DevTools
- Aucune classe `dark:` ajoutée
- CODEBASE_REFERENCE.md à jour
