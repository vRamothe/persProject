# ScienceLycée — Roadmap & Improvement Ideas

## Learning Experience

1. **Lesson bookmarks / notes** — Let students highlight or annotate parts of a lesson. Simple `UserNote(user, lecon, texte, position)` model.
2. **Timed quizzes** — Add an optional timer to simulate exam conditions (bac prep). A `duree_limite` field on Quiz.
3. **Difficulty levels on questions** — Tag questions as facile/moyen/difficile. The chapter quiz could then guarantee a balanced mix.

## Content & Engagement

4. **Interactive exercises** — Beyond QCM: drag-and-drop ordering, fill-in-the-blank in equations, matching columns. Could be done with Alpine.js `x-data` blocks and a new question type.
5. **Instant feedback on wrong answers** — Instead of showing all corrections at the end, show instant feedback per question (configurable).
6. **Glossary / formula sheet** — Auto-extracted from lesson content. A searchable reference page per matière.

## Technical / Infrastructure

7. **Full-text search** — Let students search across all lessons. PostgreSQL's `SearchVector` + `SearchRank` is built into Django, no extra dependency needed.
8. **PDF export of lessons** — Students often want offline access. `weasyprint` can render Markdown HTML to PDF.

## Social / Gamification

9. **Leaderboard** — Anonymous or opt-in ranking per classe/niveau. Competitive students love this.
10. **Badges / achievements** — "First quiz passed", "10-day streak", "Perfect chapter score". Simple model + display.
11. **Teacher notifications** — Email or in-app alerts when a student is struggling (e.g., 3+ failed attempts on a chapter quiz).

## Completed

- ~~Bind-mount source code in dev + `.dockerignore`~~ — Bind mount, gunicorn `--reload`, `.dockerignore` added
- ~~Spaced repetition / revision mode~~ — Leitner box system with `UserQuestionHistorique` model, "Révisions" page
- ~~Progress dashboard with analytics~~ — Per-subject stats, streak tracking, score trend chart, weak areas
