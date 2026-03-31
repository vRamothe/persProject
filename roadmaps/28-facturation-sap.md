# 28 — Facturation SAP

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #38 |
| **Phase** | 7 — Tutorat, Calendrier & Facturation SAP |
| **Type** | Feature |
| **LLM recommandé** | Sonnet (suffisant — modèle Facture, PDF récap, envoi email) |
| **Statut** | ⬜ À faire |
| **Priorité** | 28 |
| **Dépendances** | #26 Stripe Pre-auth |

---

## Description

Génération de factures pour les séances de tutorat payées. Modèle `Facture` avec numéro séquentiel, stockage montant / TVA / total. PDF WeasyPrint récapitulatif mensuel. Envoi par email à l'élève et à l'enseignant.

## Critères d'acceptation

- Facture créée automatiquement à la capture Stripe réussie
- Numéro séquentiel : `SL-AAAAMM-XXXX` (année-mois-compteur)
- PDF : entête ScienceLycée, détails session, montant HT/TVA/TTC
- Email envoyé avec PDF en pièce jointe
- Admin : vue liste des factures avec filtres date/élève/enseignant
- Management command : `generer_factures_mensuelles` (récap mensuel)

## Architecture

- **Modèle** (`tutoring/models.py`) : `Facture` (reservation FK, numero unique, montant_ht, tva, montant_ttc, date_emission, pdf_genere bool)
- **Vues** : `facture_pdf(request, pk)` → WeasyPrint, `facture_email(request, pk)` (admin only)
- **Template PDF** : `templates/tutoring/facture_pdf.html`
- **Utilitaire** : `generer_numero_facture()` — compteur atomique F() + 1
- **Management command** : `generer_factures_mensuelles`
- **Admin** : `FactureAdmin` avec list_filter

## Tests

- Numéro séquentiel unique et formaté
- PDF valide (Content-Type application/pdf)
- Email envoyé avec pièce jointe
- Admin-only access

## Sécurité

- Factures accessibles uniquement par l'élève concerné ou admin
- Numéro séquentiel pas devinable (pas d'info dans le numéro sur l'utilisateur)
- PDF généré serveur-side (pas de template injection)

## Performance

- Génération PDF : ~200ms (WeasyPrint déjà en dépendance)
- Batch mensuel via management command (pas temps réel)

## Definition of Done

- Factures générées à la capture Stripe
- PDF correct, email envoyé, numéro séquentiel
- Admin filtrable, tests passent, CODEBASE_REFERENCE.md à jour
