# 25 — Système de Réservation (Tutorat)

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #36 |
| **Phase** | 7 — Tutorat, Calendrier & Facturation SAP |
| **Type** | Feature |
| **LLM recommandé** | **Opus** (nécessaire — nouvelle app Django, 2 modèles, double validation, annulation 24h, select_for_update, emails) |
| **Statut** | ⬜ À faire |
| **Priorité** | 25 |
| **Dépendances** | Aucune |
| **Bloque** | #26 Stripe Pre-auth, #27 Sync Calendrier, #28 Facturation SAP |

---

## Description

Nouvelle app `tutoring/` : disponibilités enseignant → réservation élève → double validation → confirmation email. États : en_attente → valide | annule. Annulation possible >24h avant le créneau. Dashboards admin et élève enrichis.

## Critères d'acceptation

- Enseignant crée/modifie/supprime des créneaux récurrents
- Élève voit calendrier hebdomadaire, réserve un créneau
- Réservation en_attente → enseignant valide/refuse → emails
- Annulation bloquée si <24h (HTTP 403)
- Dashboards admin (réservations en attente + à venir) et élève (confirmées + historique)
- Créneaux réservés invisibles pour les autres élèves

## Architecture

- **App** : `tutoring/` (models, views, urls, admin)
- **Modèles** :
  - `DisponibiliteEnseignant` : enseignant FK, jour_semaine, heure_debut, heure_fin, duree_seance, actif
  - `Reservation` : eleve FK, enseignant FK, date, heure_debut, heure_fin, statut, stripe_payment_intent_id, unique_together [enseignant, date, heure_debut]
- **Vues** : disponibilites, reserver (POST HTMX), valider, annuler, mes_reservations
- **URLs** : préfixe `/tutorat/`
- **Templates** : disponibilites.html, reservations.html, mes_reservations.html
- **Emails** : réservation nouvelle/validée/annulée (.html + .txt)
- **Anti race condition** : `select_for_update()` dans la vue de réservation

## Tests

- Élève réserve créneau libre → en_attente
- Double booking empêché
- Enseignant valide → statut valide + email
- Annulation bloquée <24h, autorisée >24h
- Élève ne peut pas valider
- Créneau annulé redevient disponible

## Sécurité

- **A01** : vérification `reservation.eleve == request.user or is_admin`
- **A04** : `unique_together` + `select_for_update()` anti double-booking
- Rate limiting 10 req/min sur réservation
- Transitions d'état contrôlées

## Performance

- disponibilites : 2 requêtes SQL
- reserver : 1 `select_for_update` + 1 `create` + email
- Dashboard : +1 requête (LIMIT 10, select_related)
- Index `(enseignant, date)` sur Reservation

## Definition of Done

- Créneaux gérables, réservation → double validation
- Annulation avec contrainte 24h
- Anti double-booking (base + race condition)
- Dashboards enrichis, emails envoyés
- Preview respecté, tests passent, CODEBASE_REFERENCE.md à jour
