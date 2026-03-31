# 17 — Feedback Immédiat Quiz

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #19 |
| **Phase** | 4 — Learning Experience |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — HTMX partials + Alpine.js navigation question par question) |
| **Statut** | ⬜ À faire |
| **Priorité** | 17 |
| **Dépendances** | Aucune (compatible avec #16) |

---

## Description

Mode question-par-question avec correction immédiate via HTMX. Nouveau champ `feedback_immediat` (BooleanField) sur `Quiz`. Chaque question évaluée individuellement, correction + explication affichées, score cumulé en temps réel. Incompatible avec chronomètre (#16) — si les deux actifs, chronomètre prioritaire.

## Critères d'acceptation

- `Quiz.feedback_immediat` : BooleanField, default=False
- Mode feedback : une question à la fois, bouton "Valider"
- Évaluation HTMX → correction affichée sous la question
- Score cumulé visible, bouton "Suivante"
- Réponses stockées en session (pas en hidden fields)
- Résultat final enregistré normalement

## Architecture

- **Nouveau endpoint HTMX** : `evaluer_question_unique(request, question_pk)` — POST, retourne partial `_feedback_question.html`
- **Nouvelle vue** : `finaliser_quiz_feedback(request, lecon_pk)` — POST, calcule score final depuis session
- **Templates** : `quiz.html` conditionnel + `_feedback_question.html` (nouveau)
- **Alpine.js** : `currentIndex`, `score`, `total` pour navigation

## Tests

- `test_quiz_classic_mode_no_feedback_markup`
- `test_quiz_feedback_mode_shows_single_question`
- `test_evaluer_question_returns_correction`
- `test_evaluer_question_wrong_answer`
- `test_finaliser_quiz_feedback_saves_resultat`
- `test_feedback_mode_ignored_when_timer_active`

## Sécurité

- **A01** : vérifier que la question est accessible à l'élève (niveau, chapitre débloqué)
- Réponses en session côté serveur — non modifiables par l'élève
- IDOR : question appartient bien au quiz de l'élève
- Rate limiting existant s'applique

## Performance

- N requêtes HTMX (1/question) mais chacune très légère (~5ms)
- Budget par question : +1-2 requêtes SQL

## Definition of Done

- Mode feedback question par question fonctionnel
- Score cumulé en temps réel
- Résultat final identique au mode classique
- Chronomètre prioritaire si les deux actifs
- Tests passent, CODEBASE_REFERENCE.md à jour
