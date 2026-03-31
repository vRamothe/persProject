# 16 — Quiz Chronométrés

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #18 |
| **Phase** | 4 — Learning Experience |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — 1 champ modèle + Alpine.js timer + validation serveur) |
| **Statut** | ⬜ À faire |
| **Priorité** | 16 |
| **Dépendances** | Aucune |

---

## Description

Chronomètre optionnel sur les quiz. Nouveau champ `duree_limite` (minutes) sur `Quiz`. Compte à rebours Alpine.js, auto-submit à expiration. Validation serveur via `quiz_start_time` (delta ≤ duree_limite + 30s).

## Critères d'acceptation

- `Quiz.duree_limite` : PositiveIntegerField, null, blank, default=None
- Timer MM:SS en sticky en haut du formulaire quand défini
- Auto-submit à expiration via `form.submit()`
- Champ caché `quiz_start_time` (timestamp Unix)
- Serveur rejette si delta > `duree_limite * 60 + 30` (HTTP 400)
- Quiz sans `duree_limite` fonctionnent comme avant

## Architecture

- **Modèle** : `courses/models.py` → `Quiz.duree_limite`
- **Templates** : `quiz.html`, `quiz_chapitre.html` — bloc conditionnel `{% if quiz.duree_limite %}`
- **Alpine.js** : `timerCountdown(minutes)` inline
- **Vues** : `progress/views.py` — `soumettre_quiz` et `soumettre_quiz_chapitre` vérifient le delta
- **Admin** : `duree_limite` dans `QuizAdmin`

## Tests

- `test_quiz_without_timer_no_countdown_markup`
- `test_quiz_with_timer_shows_countdown`
- `test_submit_quiz_within_time_succeeds`
- `test_submit_quiz_over_time_rejected` → HTTP 400
- `test_submit_quiz_no_timer_ignores_start_time`

## Sécurité

- **A04** : validation côté serveur (pas seulement JS client)
- Marge 30s acceptable pour l'itération 1 (pas un examen officiel)

## Performance

- +0 requête SQL (duree_limite chargé avec le Quiz)
- setInterval uniquement sur page quiz

## Definition of Done

- Chronomètre affiché/absent selon `duree_limite`
- Auto-submit + validation serveur
- Quiz existants non impactés
- Tests passent, CODEBASE_REFERENCE.md à jour
