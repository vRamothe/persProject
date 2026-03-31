# 26 — Synchronisation Calendrier

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #37 |
| **Phase** | 7 — Tutorat, Calendrier & Facturation SAP |
| **Type** | Feature |
| **LLM recommandé** | Sonnet (suffisant — icalendar lib, vue ICS, lien abonnement) |
| **Statut** | ⬜ À faire |
| **Priorité** | 26 |
| **Dépendances** | #24 Système de Réservation |

---

## Description

Export ICS des réservations validées pour synchronisation avec Google Calendar, Apple Calendar, Outlook. URL unique signée par utilisateur (token dans l'URL). Mise à jour automatique à chaque chargement (pas de push).

## Critères d'acceptation

- URL ICS signée par utilisateur : `/tutorat/calendrier/<token>.ics`
- Événements VEVENT pour chaque réservation validée (titre, date, durée, description)
- Lien "📅 Ajouter à mon calendrier" dans dashboard élève et enseignant
- Token régénérable depuis le profil
- Token invalidé au changement de mot de passe

## Architecture

- **Lib** : `icalendar` (ajout requirements.txt)
- **Modèle** : `calendar_token` (UUIDField, unique) sur CustomUser
- **Vue** : `calendrier_ics(request, token)` — pas de `@login_required`, auth par token
- **URL** : `calendrier_ics` → `/tutorat/calendrier/<uuid:token>.ics`
- **Template** : lien `webcal://` dans dashboards
- **Régénération** : bouton dans profil, `uuid4()` + save

## Tests

- ICS valide (Content-Type `text/calendar`)
- Contient uniquement réservations validées de l'utilisateur
- Token invalide → 404
- Token régénéré → ancien invalide

## Sécurité

- Token UUID4 (128 bits d'entropie) — non brute-forceable
- Pas de données sensibles dans les événements (pas d'email, pas de téléphone)
- Rate limiting 5 req/min (anti-scraping)
- Token régénérable pour invalidation

## Performance

- 1 requête SQL (réservations validées, date ≥ today - 30 jours)
- Cache-Control: no-store (le calendrier doit être frais)

## Definition of Done

- Export ICS valide, importable dans 3 clients majeurs
- Token signé, régénérable, sécurisé
- Tests passent, CODEBASE_REFERENCE.md à jour
