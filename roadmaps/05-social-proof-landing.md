# 05 — Social Proof sur Landing Page

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #8 |
| **Phase** | 2 — Acquisition & First Revenue |
| **Type** | Business |
| **LLM recommandé** | Sonnet (suffisant — template Tailwind simple) |
| **Statut** | ⬜ À faire |
| **Priorité** | 5 |
| **Dépendances** | #04 Beta Test (pour les témoignages) |

---

## Description

Ajouter une section de témoignages sur la page d'accueil publique (`accueil.html`) pour établir la confiance avec les visiteurs. Les témoignages proviennent des beta testeurs (#04) et sont affichés sous forme de cards avec citation, prénom, niveau et matière préférée. Un badge de confiance "Conçu par un enseignant certifié local" est affiché en bonne place. Les témoignages sont codés en dur dans le template (pas de modèle dédié) pour cette première itération.

## Critères d'acceptation

- La page d'accueil (`/`) affiche une section "Ce qu'en disent nos élèves" avec 3-5 témoignages
- Chaque témoignage card contient : citation (2-3 phrases), prénom + initiale du nom, niveau
- Un badge de confiance "Conçu par un enseignant certifié — Grasse (06)" est visible
- La section est responsive (1 colonne mobile, 2-3 colonnes desktop)
- Le dark mode fonctionne via les overrides globaux existants

## Architecture

- **Template modifié** : `templates/courses/accueil.html` — nouvelle `<section>` entre le contenu du catalogue et le footer
- **Pas de nouveau modèle** : témoignages codés en dur (itération 1) avec `<blockquote>` Tailwind
- **Fichiers impactés** : `templates/courses/accueil.html` uniquement

## Tests

- `test_accueil_contains_testimonials_section` — GET `/` (anon) → asserter `id="temoignages"` ou "Ce qu'en disent"
- `test_accueil_contains_trust_badge` — GET `/` → asserter "enseignant certifié"
- `test_accueil_testimonials_responsive_classes` — asserter `md:grid-cols-2` ou `lg:grid-cols-3`

## Sécurité

- Contenu statique — aucun risque XSS

## Performance

- +0 requête SQL, +0 appel externe. Impact TTFB : négligeable.

## Definition of Done

- Section témoignages visible sur la page d'accueil publique
- Badge de confiance affiché
- Responsive + dark mode validés
- Tests passent, CODEBASE_REFERENCE.md à jour
