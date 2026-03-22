# ScienceLycée — Roadmap & Improvement Ideas

## Priority 1 — Critical

1. **Automated tests + CI** — Zero tests exist. Add model tests (Leitner transitions, chapter unlock logic), view tests (access control, quiz scoring, preview mode), and a GitHub Actions pipeline to run them on every push.
2. **Query optimization** — `_dashboard_eleve` runs 5+ queries per matière in a loop; `matieres_view` has N+1 on progressions. Use `Prefetch`, `annotate()`, and `select_related` before real content (135+ chapters) makes pages slow.
3. **Password reset flow** — No password reset exists. Students who forget their password are locked out. Add Django's built-in `PasswordResetView` flow with email sending.

## Priority 2 — Security & UX

4. **Rate limiting on login & quiz submission** — No throttling on `ConnexionView.post` or `soumettre_quiz`. Add `django-axes` or a simple rate-limit decorator to prevent brute-force and spam.
5. **Custom error pages (404, 500)** — No custom error templates. Users see Django's default ugly page or a stack trace if DEBUG leaks.
6. **Email verification on signup** — Anyone can register with a fake email. Add a token-based email verification to prevent dummy accounts.

## Priority 3 — Learning Experience

7. **Lesson bookmarks / notes** — Let students highlight or annotate parts of a lesson. Simple `UserNote(user, lecon, texte, position)` model.
8. **Timed quizzes** — Add an optional timer to simulate exam conditions (bac prep). A `duree_limite` field on Quiz.
9. **Difficulty levels on questions** — Tag questions as facile/moyen/difficile. The chapter quiz could then guarantee a balanced mix.
10. **Instant feedback on wrong answers** — Instead of showing all corrections at the end, show instant feedback per question (configurable).

## Priority 4 — Content & Engagement

11. **Interactive exercises** — Beyond QCM: drag-and-drop ordering, fill-in-the-blank in equations, matching columns. Alpine.js `x-data` blocks + new question type.
12. **Glossary / formula sheet** — Auto-extracted from lesson content. A searchable reference page per matière.
13. **Full-text search** — PostgreSQL `SearchVector` + `SearchRank`, built into Django, no extra dependency needed.
14. **PDF export of lessons** — Offline access via `weasyprint` rendering Markdown HTML to PDF.

## Priority 5 — Social / Gamification

15. **Leaderboard** — Anonymous or opt-in ranking per classe/niveau.
16. **Badges / achievements** — "First quiz passed", "10-day streak", "Perfect chapter score". Simple model + display.
17. **Teacher notifications** — Email or in-app alerts when a student is struggling (3+ failed attempts on a chapter quiz).

## Priority 6 — Architecture / Housekeeping

18. **Mobile responsiveness audit** — Sidebar is desktop-first; quiz forms with math equations likely overflow on phones. Focused mobile pass needed.
19. **Content admin UX — bulk import** — CSV/JSON bulk import for questions (with tolerances, options) to speed up real bac-prep content entry.
20. **Admin content analytics** — Which questions have the lowest success rate? Which lessons have the highest drop-off? Helps improve content quality.
21. **Accessibility (a11y)** — Add `aria-label` on interactive elements, focus management after HTMX swaps, proper `<fieldset>`/`<legend>` on quiz radio buttons.
22. **DRY quiz submission logic** — `soumettre_quiz` and `soumettre_quiz_chapitre` share ~80% identical code. Extract a shared `_evaluer_reponses()` helper.
23. **Logging & monitoring** — Add structured logging, Sentry integration, and a `/health/` endpoint for production visibility.
24. **Database backups** — Schedule automated Postgres backups (Heroku `pg:backups:schedule` or equivalent).

## Completed

- ~~Bind-mount source code in dev + `.dockerignore`~~ — Bind mount, gunicorn `--reload`, `.dockerignore` added
- ~~Spaced repetition / revision mode~~ — Leitner box system with `UserQuestionHistorique` model, "Révisions" page
- ~~Progress dashboard with analytics~~ — Per-subject stats, streak tracking, score trend chart, weak areas
