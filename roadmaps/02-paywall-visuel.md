# 02 — Paywall Visuel

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #2 |
| **Phase** | 1 — Product & Proof |
| **Type** | Business |
| **LLM recommandé** | Sonnet (suffisant) |
| **Statut** | ⬜ À faire |
| **Priorité** | 2 (bloquant pour Stripe) |
| **Dépendances** | Aucune |
| **Bloque** | #03 Integration Stripe |

---

## Description

Les leçons premium (non `gratuit`) doivent rester visibles dans le catalogue public et les listings de chapitres, mais afficher un cadenas 🔒 signalant un contenu réservé aux abonnés. Au clic sur une leçon verrouillée, un modal Alpine.js s'affiche avec un pitch commercial ("Débloquez tout le programme Bac"), les deux paliers tarifaires (mensuel/annuel) et un CTA vers le paiement Stripe. L'objectif est de convertir les visiteurs en abonnés sans les rediriger vers une simple page de login. Le modal doit respecter le système de couleurs par matière et le dark mode global via les CSS overrides existants dans `base.html`.

## Critères d'acceptation

- Les leçons non-`gratuit` affichent un cadenas 🔒 dans `catalogue.html`, `chapitres.html` et `accueil.html`
- Le clic sur une leçon verrouillée ouvre un modal Alpine.js (pas de redirection vers `/connexion/`)
- Le modal affiche les deux paliers tarifaires (Mensuel ~€19/mois, Annuel ~€119/an) avec un CTA pointant vers la Stripe Checkout Session (cf. #03)
- Le modal respecte le design system (couleurs par matière via `MATIERE_COULEURS`, dark mode via les overrides globaux)
- Sur mobile, le modal est responsive (full-screen ou bottom-sheet selon la taille d'écran)

## Architecture

- **Nouveau template partiel** : `templates/components/_paywall_modal.html` — composant Alpine.js (`x-data="{ showPaywall: false, plan: 'mensuel' }"`) inclus via `{% include %}` dans les templates concernés
- **Templates modifiés** : `catalogue.html`, `accueil.html`, `lecon_publique.html` — ajout conditionnel du cadenas (`{% if not lecon.gratuit %}🔒{% endif %}`) et du `@click` Alpine qui ouvre le modal
- **Pas de nouveau modèle** : le flag `Lecon.gratuit` existe déjà ; le modal est purement front-end
- **Patterns** : le modal utilise `x-show`, `x-transition` et `@click.away="showPaywall = false"` pour une UX fluide. Les URLs des CTA (`{% url 'checkout' %}?plan=mensuel`) seront câblées une fois #03 implémenté. En attendant, un lien `#` avec `disabled` suffit.
- **Fichiers impactés** : `templates/components/_paywall_modal.html` (nouveau), `templates/courses/catalogue.html`, `templates/courses/accueil.html`, `templates/courses/lecon_publique.html`

## Tests

- `test_catalogue_shows_lock_icon_on_premium_lessons` — GET `/cours/<matiere_slug>/`, asserter que le HTML contient `🔒` pour chaque leçon où `gratuit=False`
- `test_catalogue_no_lock_on_free_lessons` — même page, asserter l'absence de cadenas pour les leçons `gratuit=True`
- `test_paywall_modal_markup_present` — asserter que le HTML de la page contient `x-data` et `showPaywall` (le composant Alpine est bien inclus)
- `test_premium_lesson_public_view_still_blocks_content` — GET `/cours/<matiere>/<niveau>/<chapitre>/<lecon>/` sur une leçon `gratuit=False` → redirect vers login (le serveur ne livre pas le contenu)

## Sécurité

- **OWASP A01 (Broken Access Control)** : le contenu Markdown de la leçon premium n'est **jamais** inclus dans le HTML de la page catalogue — le serveur ne l'envoie pas, le cadenas est la seule chose affichée. `lecon_publique_view` continue de rediriger les leçons non-gratuites vers le login.
- Le modal ne contient aucune donnée sensible (uniquement du texte marketing et des prix).

## Performance

- Le partial `_paywall_modal.html` pèse < 2 KB — aucun impact mesurable sur le TTFB
- Pas de requête SQL ajoutée : le flag `gratuit` est déjà chargé dans les querysets existants des vues catalogue/accueil
- Budget : +0 requête SQL par page

## Definition of Done

- Les cadenas s'affichent correctement sur les trois templates de listing (catalogue, accueil, leçon publique)
- Le modal s'ouvre au clic, affiche les paliers, et se ferme au clic extérieur ou bouton ✕
- Le dark mode fonctionne (pas de classes `dark:` dans les templates enfants — uniquement les overrides CSS globaux)
- Tests passent
- CODEBASE_REFERENCE.md mis à jour (section 5 — Templates)
