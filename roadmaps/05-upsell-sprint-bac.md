# 05 — Offre "Sprint Bac" Upsell

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #9 |
| **Phase** | 2 — Acquisition & First Revenue |
| **Type** | Business (non-technique) |
| **LLM recommandé** | Aucun (tâche humaine — pricing & Stripe dashboard) |
| **Statut** | ⬜ À faire |
| **Priorité** | 5 |
| **Dépendances** | #02 Stripe (pour le price_id) |

---

## Description

Définir et formaliser une offre premium "Sprint Bac" combinant l'accès illimité à l'application et 1h/mois de coaching individuel en visio pour analyser les analytics de l'élève et cibler ses points faibles. Cette offre est un package business (~€89/mois) proposé sur la landing page et dans le modal paywall (#01). Pas de développement logiciel — uniquement la définition du produit et de son intégration tarifaire dans l'offre Stripe.

## Critères d'acceptation

- Le pricing est finalisé (tarif mensuel et éventuellement trimestriel)
- Le descriptif produit est rédigé (proposition de valeur, ce qui est inclus, ce qui ne l'est pas)
- Le plan est créé dans le dashboard Stripe (mode test) avec un `price_id` prêt à être intégré
- Le positionnement par rapport aux deux paliers existants (Mensuel/Annuel) est clair

## Definition of Done

- Document de pricing finalisé
- Produit + Price créés dans Stripe (test mode)
- Le `price_id` est documenté dans `.env.example` (`STRIPE_PRICE_SPRINT`)
- Le descriptif est prêt pour insertion dans le modal paywall
