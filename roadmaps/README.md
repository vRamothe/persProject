# Roadmap ScienceLycée — Index

Ce dossier contient **36 fiches features** extraites de `ROADMAP.md` et `ROADMAP_ROLES.md`, classées par priorité d'implémentation.

## Légende

| Symbole | Signification |
|---------|---------------|
| ⬜ | À faire |
| 🔧 | En cours |
| ✅ | Terminé |
| **Opus** | Nécessite Claude Opus (complexité élevée) |
| Sonnet | Claude Sonnet suffit |

---

## Vue d'ensemble

| # | Feature | Phase | LLM | Statut |
|---|---------|-------|-----|--------|
| 01 | [Paywall Visuel](01-paywall-visuel.md) | 2 — Monétisation | Sonnet | ⬜ |
| 02 | [Stripe Paiement](02-stripe-paiement.md) | 2 — Monétisation | **Opus** | ⬜ |
| 03 | [Social Media Content](03-social-media-content.md) | 3 — Acquisition | Sonnet | ⬜ |
| 04 | [Optimisation Requêtes SQL](04-optimisation-requetes-sql.md) | 3 — Acquisition | Sonnet | ⬜ |
| 05 | [Rétention Parents](05-retention-parents.md) | 3 — Acquisition | Sonnet | ⬜ |
| 06 | [Responsive Mobile](06-responsive-mobile.md) | 3 — Acquisition | Sonnet | ⬜ |
| 07 | [Modèles de Données Rôles](07-modeles-donnees-roles.md) | Rôles 1 — Data Models | **Opus** | ⬜ |
| 08 | [Inscription Multi-Rôle](08-inscription-multi-role.md) | Rôles 2 — Registration | **Opus** | ⬜ |
| 09 | [Inscription Enseignant](09-inscription-enseignant.md) | Rôles 2 — Registration | Sonnet | ⬜ |
| 10 | [Inscription Parent](10-inscription-parent.md) | Rôles 2 — Registration | Sonnet | ⬜ |
| 11 | [Recherche Liaison Élève](11-recherche-liaison-eleve.md) | Rôles 3 — Validation | Sonnet | ⬜ |
| 12 | [Validation Liaison](12-validation-liaison.md) | Rôles 3 — Validation | Sonnet | ⬜ |
| 13 | [Validation Liaisons](13-validation-liaisons.md) | Rôles 3 — Liaison | **Opus** | ⬜ |
| 14 | [Dashboards par Rôle](14-dashboards-par-role.md) | Rôles 4 — Dashboards | **Opus** | ⬜ |
| 15 | [Messagerie Interne](15-messagerie-interne.md) | Rôles 5 — Messaging | **Opus** | ⬜ |
| 16 | [Quiz Chronométrés](16-quiz-chronometres.md) | 4 — Learning Experience | Sonnet | ⬜ |
| 17 | [Feedback Immédiat](17-feedback-immediat.md) | 4 — Learning Experience | Sonnet | ⬜ |
| 18 | [Glossaire & Fiches Formules](18-glossaire-fiches-formules.md) | 4 — Learning Experience | Sonnet | ⬜ |
| 19 | [Exercices Interactifs](19-exercices-interactifs.md) | 4 — Learning Experience | **Opus** | ⬜ |
| 20 | [Badges / Récompenses](20-badges-recompenses.md) | 5 — Gamification | Sonnet | ⬜ |
| 21 | [Classement](21-classement.md) | 5 — Gamification | Sonnet | ⬜ |
| 22 | [Notifications Enseignant](22-notifications-enseignant.md) | 5 — Gamification | Sonnet | ⬜ |
| 23 | [Accessibilité](23-accessibilite.md) | 6 — Architecture | Sonnet | ⬜ |
| 24 | [Système de Réservation](24-systeme-reservation.md) | 7 — Tutorat | **Opus** | ⬜ |
| 25 | [Stripe Pre-auth / Capture](25-stripe-preauth-capture.md) | 7 — Tutorat | **Opus** | ⬜ |
| 26 | [Sync Calendrier](26-sync-calendrier.md) | 7 — Tutorat | Sonnet | ⬜ |
| 27 | [Facturation SAP](27-facturation-sap.md) | 7 — Tutorat | Sonnet | ⬜ |
| 28 | [Tuteur IA Socratique](28-tuteur-ia-socratique.md) | 8 — IA | **Opus** | ⬜ |
| 29 | [Génération Questions](29-generation-dynamique-questions.md) | 8 — IA | **Opus** | ⬜ |
| 30 | [PWA Manifest & SW](30-pwa-manifest-sw.md) | 9 — PWA | Sonnet | ⬜ |
| 31 | [Mode Hors-Ligne](31-mode-hors-ligne.md) | 9 — PWA | Sonnet | ⬜ |
| 32 | [Web Push Notifications](32-web-push-notifications.md) | 9 — PWA | **Opus** | ⬜ |
| 33 | [Contenu Privé / UGC](33-contenu-prive-ugc.md) | 10 — Scale | **Opus** | ⬜ |
| 34 | [Analytics Granulaires](34-analytics-granulaires-temps.md) | 10 — Scale | Sonnet | ⬜ |
| 35 | [Cache Redis](35-cache-redis.md) | 10 — Scale | Sonnet | ⬜ |
| 36 | [Gels de Série](36-gels-de-serie.md) | 10 — Scale | Sonnet | ⬜ |

---

## Répartition LLM

- **Opus requis** : 13 features (01, 02, 07, 08, 13, 14, 15, 19, 24, 25, 28, 29, 32, 33)
- **Sonnet suffisant** : 23 features

## Par phase

| Phase | Features | Nb |
|-------|----------|----|
| 2 — Monétisation | 01, 02 | 2 |
| 3 — Acquisition | 03, 04, 05, 06 | 4 |
| Rôles 1-3 | 07, 08, 09, 10, 11, 12, 13 | 7 |
| Rôles 4-5 | 14, 15 | 2 |
| 4 — Learning Experience | 16, 17, 18, 19 | 4 |
| 5 — Gamification | 20, 21, 22 | 3 |
| 6 — Architecture | 23 | 1 |
| 7 — Tutorat | 24, 25, 26, 27 | 4 |
| 8 — IA | 28, 29 | 2 |
| 9 — PWA | 30, 31, 32 | 3 |
| 10 — Scale | 33, 34, 35, 36 | 4 |
