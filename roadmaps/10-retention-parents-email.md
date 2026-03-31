# 10 — Boucle de Rétention Parents (Email Hebdo)

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #17 |
| **Phase** | 3 — Scaling Traffic |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — commande management + template email) |
| **Statut** | ⬜ À faire |
| **Priorité** | 10 |
| **Dépendances** | Aucune |

---

## Description

Implémenter un email récapitulatif hebdomadaire automatique envoyé aux élèves résumant l'activité de la semaine : leçons complétées, quiz passés, score moyen, streak actuel. Envoyé via `send_weekly_recap` planifiée via Heroku Scheduler (lundi 8h UTC). Les élèves sans activité reçoivent un message d'encouragement différencié.

## Critères d'acceptation

- Commande `python manage.py send_weekly_recap` envoie un email à chaque élève actif
- Email en français, responsive HTML + texte brut (`EmailMultiAlternatives`)
- Élèves sans activité reçoivent un message d'encouragement
- Comptes inactifs et admins exclus

## Architecture

- **Commande** : `courses/management/commands/send_weekly_recap.py`
- **Templates email** : `templates/emails/recap_hebdo.html` + `.txt`
- **Scheduling** : Heroku Scheduler, lundi 8h UTC
- **Agrégation bulk** : `annotate()` sur le queryset utilisateurs (pas de boucle)

## Tests

- `test_weekly_recap_sends_email_to_active_students` — 2 actifs + 1 inactif → `len(mail.outbox) == 2`
- `test_weekly_recap_email_contains_activity_stats` — body contient "3 leçons"
- `test_weekly_recap_inactive_student_gets_encouragement` — body contient message d'encouragement
- `test_weekly_recap_skips_admins` — aucun email à l'admin
- `test_weekly_recap_html_and_text_parts` — multipart vérifié

## Sécurité

- Pas de données sensibles dans l'email (pas de mot de passe, pas de magic link)
- **A07** : pas de lien de connexion automatique

## Performance

- ~3 requêtes SQL bulk quel que soit le nombre d'élèves
- Envoi SMTP le bottleneck (~200ms/email) — `get_connection()` réutilisé

## Definition of Done

- Commande fonctionne sans erreur
- Emails corrects, comptes inactifs/admins exclus
- Tests passent, CODEBASE_REFERENCE.md à jour
