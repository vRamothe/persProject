# Roadmap ScienceLycée — Index

Ce dossier contient **37 fiches features** extraites de `ROADMAP.md` et `ROADMAP_ROLES.md`, classées par priorité d'implémentation.

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
| 01 | [Leçons Publiques avec Blur Premium](01-lecons-publiques-blur.md) | 1 — Product & Proof | Sonnet | ⬜ |
| 02 | [Paywall Visuel](02-paywall-visuel.md) | 1 — Product & Proof | Sonnet | ⬜ |
| 03 | [Intégration Stripe](03-integration-stripe.md) | 1 — Product & Proof | **Opus** | ⬜ |
| 04 | [Bêta Test Élèves](04-beta-test-eleves.md) | 1 — Product & Proof | Sonnet | ⬜ |
| 05 | [Social Proof Landing](05-social-proof-landing.md) | 1 — Product & Proof | Sonnet | ⬜ |
| 06 | [Upsell Sprint Bac](06-upsell-sprint-bac.md) | 2 — Monétisation | Sonnet | ⬜ |
| 07 | [Marketing Local](07-marketing-local.md) | 3 — Acquisition | Sonnet | ⬜ |
| 08 | [Optimisation Requêtes SQL](08-optimisation-requetes.md) | 3 — Acquisition | Sonnet | ⬜ |
| 09 | [Contenu Social Snackable](09-contenu-social-snackable.md) | 3 — Acquisition | Sonnet | ⬜ |
| 10 | [Rétention Parents Email](10-retention-parents-email.md) | 3 — Acquisition | Sonnet | ⬜ |
| 11 | [Audit Mobile Responsiveness](11-audit-mobile-responsiveness.md) | 3 — Acquisition | Sonnet | ⬜ |
| 12 | [Modèles de Données Multi-Rôles](12-modeles-donnees-multi-roles.md) | Rôles 1 — Data Models | **Opus** | ⬜ |
| 13 | [Inscription Multi-Rôles](13-inscription-multi-roles.md) | Rôles 2 — Registration | **Opus** | ⬜ |
| 14 | [Validation Liaisons](14-validation-liaisons.md) | Rôles 3 — Liaison | **Opus** | ⬜ |
| 15 | [Dashboards par Rôle](15-dashboards-par-role.md) | Rôles 4 — Dashboards | **Opus** | ⬜ |
| 16 | [Messagerie Interne](16-messagerie-interne.md) | Rôles 5 — Messaging | **Opus** | ⬜ |
| 17 | [Quiz Chronométrés](17-quiz-chronometres.md) | 4 — Learning Experience | Sonnet | ⬜ |
| 18 | [Feedback Immédiat](18-feedback-immediat.md) | 4 — Learning Experience | Sonnet | ⬜ |
| 19 | [Glossaire & Fiches Formules](19-glossaire-fiches-formules.md) | 4 — Learning Experience | Sonnet | ⬜ |
| 20 | [Exercices Interactifs](20-exercices-interactifs.md) | 4 — Learning Experience | **Opus** | ⬜ |
| 21 | [Badges / Récompenses](21-badges-recompenses.md) | 5 — Gamification | Sonnet | ⬜ |
| 22 | [Classement](22-classement.md) | 5 — Gamification | Sonnet | ⬜ |
| 23 | [Notifications Enseignant](23-notifications-enseignant.md) | 5 — Gamification | Sonnet | ⬜ |
| 24 | [Accessibilité](24-accessibilite.md) | 6 — Architecture | Sonnet | ⬜ |
| 25 | [Système de Réservation](25-systeme-reservation.md) | 7 — Tutorat | **Opus** | ⬜ |
| 26 | [Stripe Pre-auth / Capture](26-stripe-preauth-capture.md) | 7 — Tutorat | **Opus** | ⬜ |
| 27 | [Sync Calendrier](27-sync-calendrier.md) | 7 — Tutorat | Sonnet | ⬜ |
| 28 | [Facturation SAP](28-facturation-sap.md) | 7 — Tutorat | Sonnet | ⬜ |
| 29 | [Tuteur IA Socratique](29-tuteur-ia-socratique.md) | 8 — IA | **Opus** | ⬜ |
| 30 | [Génération Questions](30-generation-dynamique-questions.md) | 8 — IA | **Opus** | ⬜ |
| 31 | [PWA Manifest & SW](31-pwa-manifest-sw.md) | 9 — PWA | Sonnet | ⬜ |
| 32 | [Mode Hors-Ligne](32-mode-hors-ligne.md) | 9 — PWA | Sonnet | ⬜ |
| 33 | [Web Push Notifications](33-web-push-notifications.md) | 9 — PWA | **Opus** | ⬜ |
| 34 | [Contenu Privé / UGC](34-contenu-prive-ugc.md) | 10 — Scale | **Opus** | ⬜ |
| 35 | [Analytics Granulaires](35-analytics-granulaires-temps.md) | 10 — Scale | Sonnet | ⬜ |
| 36 | [Cache Redis](36-cache-redis.md) | 10 — Scale | Sonnet | ⬜ |
| 37 | [Gels de Série](37-gels-de-serie.md) | 10 — Scale | Sonnet | ⬜ |

---

## Répartition LLM

- **Opus requis** : 13 features (03, 12, 13, 14, 15, 16, 20, 25, 26, 29, 30, 33, 34)
- **Sonnet suffisant** : 24 features

## Par phase

| Phase | Features | Nb |
|-------|----------|----|
| 1 — Product & Proof | 01, 02, 03, 04, 05 | 5 |
| 2 — Monétisation | 06 | 1 |
| 3 — Acquisition | 07, 08, 09, 10, 11 | 5 |
| Rôles 1-3 | 12, 13, 14 | 3 |
| Rôles 4-5 | 15, 16 | 2 |
| 4 — Learning Experience | 17, 18, 19, 20 | 4 |
| 5 — Gamification | 21, 22, 23 | 3 |
| 6 — Architecture | 24 | 1 |
| 7 — Tutorat | 25, 26, 27, 28 | 4 |
| 8 — IA | 29, 30 | 2 |
| 9 — PWA | 31, 32, 33 | 3 |
| 10 — Scale | 34, 35, 36, 37 | 4 |
