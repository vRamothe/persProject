# 23 — Accessibilité (a11y)

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #32 |
| **Phase** | 6 — Architecture & Housekeeping |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — modifications HTML/CSS, aria-labels, fieldset/legend) |
| **Statut** | ⬜ À faire |
| **Priorité** | 23 |
| **Dépendances** | Aucune |

---

## Description

4 axes : (1) aria-labels manquants sur icônes, (2) focus management après HTMX swaps, (3) quiz fieldset/legend + labels, (4) contraste couleurs WCAG AA 4.5:1. Objectif : Lighthouse Accessibility ≥ 90.

## Critères d'acceptation

- `aria-label` descriptif français sur tous les boutons d'icônes
- Focus déplacé après chaque HTMX swap (`htmx:afterSwap` + `focus()`)
- Quiz : `<fieldset>/<legend>` + `<label for="">` explicite
- Contraste ≥ 4.5:1 (placeholder `text-gray-500`, badges `opacity-50`)
- Lighthouse Accessibility ≥ 90 sur accueil, leçon, quiz, dashboard

## Architecture

- **`base.html`** : aria-labels, event listener HTMX global, `.katex` overflow
- **`quiz.html`, `quiz_chapitre.html`, `revisions.html`** : fieldset/legend, labels
- **`lecon.html`** : aria-labels panneau notes
- **Contraste** : `text-gray-400` → `text-gray-500`, `opacity-40` → `opacity-50`
- Classe `.sr-only` via Tailwind CDN

## Tests

- `test_dark_mode_toggle_has_aria_label`
- `test_hamburger_button_has_aria_label`
- `test_quiz_questions_wrapped_in_fieldset`
- `test_quiz_radio_buttons_have_labels`
- `test_htmx_afterswap_focus_script_present`

## Sécurité

- Pas d'impact — modifications purement front-end

## Performance

- +0 requête SQL, +0ms TTFB
- 1 event listener délégué sur document.body

## Definition of Done

- aria-labels complets, focus HTMX, fieldset/legend, contraste AA
- Lighthouse ≥ 90
- Aucune classe `dark:` ajoutée
- Tests passent, CODEBASE_REFERENCE.md à jour
