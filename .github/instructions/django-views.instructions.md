---
description: "Use when editing or creating Django views in ScienceLycée. Covers function-based views, @login_required, HTMX patterns, admin checks, preview mode, rate limiting, and quiz helpers."
applyTo: "**/views.py"
---
# Django Views — ScienceLycée Conventions

- Function-based views with `@login_required` (CBV only when clearly justified)
- Admin-only views: check `request.user.role == 'admin'` and return 403 otherwise
- Student views: filter by `request.user.niveau` (or `request.session["preview_niveau"]` if set)
- Preview mode: when `request.session.get("preview_niveau")` is set, skip all progress writes (`UserProgression`, `UserQuizResultat`, etc.)
- HTMX responses: return `HttpResponse` with HTML fragment, no full page render
- Rate limiting on quiz endpoints: call `_check_quiz_rate_limit(request.user.id)` — returns `True` if exceeded → return `HttpResponse(status=429)`
- Quiz helpers: use `_evaluer_reponses(questions, post_data)` for answer evaluation; `_enregistrer_historique_questions()` for Leitner tracking
- Chapter quiz selection: `_selectionner_questions_chapitre(chapitre)` — proportional difficulty (4 facile + 4 moyen + 2 difficile)
- Email sending: use `send_mail(subject, message, from_email, recipient_list)` from `django.core.mail`; for registration verification, use `_envoyer_email_verification(request, user)` helper; for password reset, Django's built-in `PasswordResetView` handles templates (`password_reset_email.html`, `password_reset_subject.txt`); all emails configured via Brevo SMTP (see CODEBASE_REFERENCE.md § 6 for config vars)
- Named URLs only: `{% url 'name' %}` in templates, `reverse('name')` in views
- French naming: view functions, variables, and URL names in French
- Premium access: use `_user_has_active_subscription(request.user)` from `users.views` to check subscription; admins always bypass; also returns `True` for `user.is_beta=True` (beta-testers); non-subscribers redirect to `lecon_publique` with blur
- Before reading views.py, check CODEBASE_REFERENCE.md (sections 3.1–3.4) for the current view structure
