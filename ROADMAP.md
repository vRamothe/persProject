# ScienceLycée — Roadmap & Improvement Ideas

## Learning Experience

1. **Spaced repetition / revision mode** — Track which questions a student got wrong and resurface them later. A "Révisions" section that prioritizes weak areas would massively improve retention.
2. **Lesson bookmarks / notes** — Let students highlight or annotate parts of a lesson. Simple `UserNote(user, lecon, texte, position)` model.
3. **Progress dashboard with analytics** — Show students a chart of their scores over time, strongest/weakest subjects, streak tracking (days in a row). Motivational.
4. **Timed quizzes** — Add an optional timer to simulate exam conditions (bac prep). A `duree_limite` field on Quiz.
5. **Difficulty levels on questions** — Tag questions as facile/moyen/difficile. The chapter quiz could then guarantee a balanced mix.

## Content & Engagement

6. **Interactive exercises** — Beyond QCM: drag-and-drop ordering, fill-in-the-blank in equations, matching columns. Could be done with Alpine.js `x-data` blocks and a new question type.
7. **Instant feedback on wrong answers** — Instead of showing all corrections at the end, show instant feedback per question (configurable).
8. **Glossary / formula sheet** — Auto-extracted from lesson content. A searchable reference page per matière.

## Technical / Infrastructure

9. **Bind-mount source code in dev** — Right now every code change requires a full Docker image rebuild (~2+ min). Adding `volumes: - ./backend:/app` in `docker-compose.yml` (dev only) with gunicorn `--reload` would give instant hot-reload.
10. **Add a `.dockerignore`** — The 120s+ context transfer during builds suggests large files are being sent. Ignoring `__pycache__`, `.git`, `node_modules`, `mediafiles` would cut build time dramatically.
11. **Full-text search** — Let students search across all lessons. PostgreSQL's `SearchVector` + `SearchRank` is built into Django, no extra dependency needed.
12. **PDF export of lessons** — Students often want offline access. `weasyprint` can render Markdown HTML to PDF.

## Social / Gamification

13. **Leaderboard** — Anonymous or opt-in ranking per classe/niveau. Competitive students love this.
14. **Badges / achievements** — "First quiz passed", "10-day streak", "Perfect chapter score". Simple model + display.
15. **Teacher notifications** — Email or in-app alerts when a student is struggling (e.g., 3+ failed attempts on a chapter quiz).

## Top 3 Priorities

- **#9 + #10** — Dev workflow (saves minutes on every single change)
- **#1** — Spaced repetition (single biggest pedagogical improvement)
- **#3** — Progress dashboard (gives students motivation and visibility)
