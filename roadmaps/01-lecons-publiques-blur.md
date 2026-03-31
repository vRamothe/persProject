# 01 — Leçons Publiques avec Blur Premium

| Champ | Valeur |
|-------|--------|
| **Source** | Nouvelle tâche (remplace la logique de redirect sur les leçons premium) |
| **Phase** | 1 — Product & Proof |
| **Type** | Business |
| **LLM recommandé** | Sonnet (suffisant — CSS blur, truncation serveur, modal Alpine.js, pas de nouvelle dépendance) |
| **Statut** | ⬜ À faire |
| **Priorité** | 1 (bloquant pour #02 Paywall et #03 Stripe) |
| **Dépendances** | Aucune |
| **Bloque** | #02 Paywall Visuel, #03 Intégration Stripe |

---

## Description

Toutes les leçons — gratuites ou premium — sont accessibles publiquement via leur URL SEO-friendly (`/cours/<matiere>/<niveau>/<chapitre>/<lecon>/`). Les leçons gratuites s'affichent normalement. Les leçons premium s'affichent avec trois protections cumulatives :

1. **Truncate serveur** : seuls les ~2 000 premiers mots du Markdown sont rendus en HTML pour les non-abonnés. Le reste est coupé côté serveur avant rendu — un « inspecteur F12 » ne trouvera jamais le contenu complet dans le DOM.
2. **CSS Blur progressif** : un dégradé `filter: blur()` croissant est appliqué sur les derniers 40 % du contenu visible, avec un overlay gradient blanc→transparent qui rend la lecture impossible.
3. **`user-select: none` + `-webkit-user-select: none`** : empêche le copier-coller du texte flouté.

Un cadenas 🔒 reste affiché dans les listings (`catalogue.html`, `chapitres.html`, `accueil.html`). Au clic sur une leçon verrouillée **depuis un listing**, ou via un CTA superposé au contenu flouté, un modal Alpine.js s'affiche avec un pitch commercial incitant à créer un compte et s'abonner, les deux paliers tarifaires et un CTA vers le paiement Stripe.

**Stratégie SEO** : les ~2 000 mots envoyés dans le HTML sont indexables par Google (pas de `noindex`), ce qui donne du « jus SEO » tout en protégeant la propriété intellectuelle.

## Critères d'acceptation

### Listings (catalogue, accueil, chapitres)
- Les leçons non-`gratuit` affichent un cadenas 🔒 dans `catalogue.html`, `chapitres.html` et `accueil.html`
- Le clic sur une leçon premium dans un listing mène à la page de la leçon (plus de modal dans le listing)

### Page leçon publique (`lecon_publique_view`)
- **Plus de redirect vers `/connexion/`** pour les leçons premium → la page se charge normalement
- Le contenu Markdown est **tronqué côté serveur à ~2 000 mots** avant rendu HTML (via `_tronquer_contenu(contenu, max_mots=2000)`)
- Le HTML rendu est enveloppé dans une `<div>` avec les classes CSS de flou
- Un **overlay CTA** se superpose au bas de la zone floutée (« Débloquez cette leçon ») avec bouton ouvrant le modal
- Le badge en-tête affiche « Premium 🔒 » au lieu de « Gratuit » pour les leçons non-gratuites
- Le CTA banner en bas de page montre les paliers tarifaires au lieu du « Créer un compte »

### Modal paywall (sur la page leçon premium)
- Modal Alpine.js avec pitch incitant à créer un compte et s'abonner
- Deux paliers (Mensuel ~€19/mois, Annuel ~€119/an), CTA Stripe
- Respecte `MATIERE_COULEURS` et dark mode (overrides globaux, pas de classes `dark:`)
- Responsive : bottom-sheet sur mobile, centered modal sur desktop
- Se ferme au clic extérieur, touche Escape, ou bouton ✕

### Utilisateurs authentifiés
- Un **abonné** (à implémenter dans #03 — pour l'instant, vérification stub `user.is_premium` → `False`) voit le contenu complet sans blur
- Un **élève non-abonné** authentifié voit le même blur + CTA, mais le CTA dit « Passez à Premium » au lieu de « Créer un compte »
- Un **admin** voit toujours le contenu complet (bypass)

## Architecture

### 1. Helper de truncation serveur (`courses/utils/truncate.py`)

```python
def tronquer_contenu_markdown(contenu: str, max_mots: int = 2000) -> tuple[str, bool]:
    """
    Tronque le contenu Markdown à max_mots mots.
    Retourne (contenu_tronque, a_ete_tronque).
    Coupe sur une frontière de paragraphe pour éviter de casser le Markdown.
    """
```

- Coupe au dernier `\n\n` avant le mot `max_mots` pour préserver la structure Markdown
- Retourne un tuple `(contenu, bool)` — le bool indique si le contenu a été tronqué

### 2. Vue modifiée (`courses/views.py` — `lecon_publique_view`)

```python
def lecon_publique_view(request, matiere_slug, niveau, chapitre_slug, lecon_slug):
    # ... get_object_or_404 comme avant ...

    # SUPPRIMÉ : le redirect vers /connexion/ pour les leçons non-gratuites

    # Si leçon premium + user non-premium :
    est_premium = not lecon.gratuit
    user_a_acces = (
        request.user.is_authenticated and (
            request.user.is_admin or
            getattr(request.user, 'is_premium', False)
        )
    )

    if est_premium and not user_a_acces:
        contenu_md, a_ete_tronque = tronquer_contenu_markdown(lecon.contenu, max_mots=2000)
    else:
        contenu_md = lecon.contenu
        a_ete_tronque = False

    contenu_html = render_markdown_to_html(contenu_md, latex_to_svg=False)
    # ... video handling identique ...

    return render(request, "courses/lecon_publique.html", {
        "lecon": lecon,
        "est_premium": est_premium,
        "est_floute": est_premium and not user_a_acces,
        "a_ete_tronque": a_ete_tronque,
        "contenu_html": contenu_html,
        # ... autres contextes existants ...
    })
```

### 3. CSS Blur (`lecon_publique.html` — dans `<style>` existant)

```css
.paywall-blur-container {
    position: relative;
    overflow: hidden;
}
.paywall-blur-container .paywall-blur-content {
    user-select: none;
    -webkit-user-select: none;
}
.paywall-blur-container .paywall-blur-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60%;
    background: linear-gradient(to bottom,
        rgba(255,255,255,0) 0%,
        rgba(255,255,255,0.7) 30%,
        rgba(255,255,255,0.95) 70%,
        rgba(255,255,255,1) 100%
    );
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    pointer-events: none;
}
.paywall-blur-container .paywall-cta {
    position: absolute;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    pointer-events: auto;
}
```

Dark mode : les overrides globaux dans `base.html` (`html.dark .paywall-blur-overlay`) gèrent les couleurs du gradient (blanc → gris-900). **Aucune classe `dark:` dans le template enfant.**

### 4. Template conditionnel (`lecon_publique.html`)

```html
{% if est_floute %}
<div class="paywall-blur-container">
    <div class="paywall-blur-content prose ...">
        {{ contenu_html|safe }}
    </div>
    <div class="paywall-blur-overlay"></div>
    <div class="paywall-cta">
        <button @click="showPaywall = true" class="px-6 py-3 bg-indigo-600 text-white font-bold rounded-xl shadow-lg">
            🔓 Débloquer cette leçon
        </button>
    </div>
</div>
{% else %}
<div class="prose ...">
    {{ contenu_html|safe }}
</div>
{% endif %}
```

### 5. Modal paywall (`templates/components/_paywall_modal.html`)

- Composant Alpine.js : `x-data="{ showPaywall: false, plan: 'annuel' }"`
- `x-show="showPaywall"` + `x-transition` + `@click.away` + `@keydown.escape.window`
- Deux cards de tarification (Mensuel / Annuel), card annuelle pré-sélectionnée avec badge « -48% »
- CTA : `{% url 'checkout' %}?plan=mensuel|annuel` (câblé en #03 — en attendant, `href="#"` désactivé)
- Inclus via `{% include 'components/_paywall_modal.html' %}` dans `lecon_publique.html`

### 6. Fichiers impactés

| Fichier | Action |
|---------|--------|
| `courses/utils/truncate.py` | **Nouveau** — helper `tronquer_contenu_markdown()` |
| `courses/views.py` | **Modifié** — `lecon_publique_view` : suppression redirect, ajout truncation + contexte blur |
| `templates/courses/lecon_publique.html` | **Modifié** — section contenu conditionnelle blur/normal, CSS paywall, badge Premium |
| `templates/components/_paywall_modal.html` | **Nouveau** — modal Alpine.js avec paliers tarifaires |
| `templates/courses/catalogue.html` | **Modifié** — cadenas sur leçons premium |
| `templates/courses/accueil.html` | **Modifié** — idem cadenas |
| `templates/courses/chapitres.html` | **Modifié** — idem cadenas |
| `templates/base.html` | **Modifié** — dark mode overrides pour `.paywall-blur-overlay` |

## Tests

### Tests de truncation
- `test_tronquer_contenu_court` — contenu < 2000 mots → retourné intact, `a_ete_tronque=False`
- `test_tronquer_contenu_long` — contenu > 2000 mots → tronqué, `a_ete_tronque=True`, ≤ 2000 mots
- `test_tronquer_coupe_sur_paragraphe` — la coupure se fait sur `\n\n`, pas au milieu d'une phrase
- `test_tronquer_preserves_latex` — les blocs `$$...$$` ne sont pas coupés en deux

### Tests de vue
- `test_premium_lecon_publique_no_redirect` — GET leçon premium en anonyme → 200 (plus de redirect)
- `test_premium_lecon_publique_content_truncated` — GET leçon premium → HTML ne contient **pas** le texte au-delà des ~2000 mots (vérifier l'absence d'un mot connu situé après la coupure)
- `test_premium_lecon_publique_blur_classes_present` — asserter `paywall-blur-container` et `user-select: none` dans le HTML
- `test_premium_lecon_publique_cta_present` — asserter le bouton « Débloquer cette leçon » dans le HTML
- `test_free_lecon_publique_no_blur` — GET leçon gratuite → pas de `paywall-blur-container`, contenu complet
- `test_admin_sees_full_content` — admin authentifié → pas de blur, contenu complet même sur leçon premium
- `test_paywall_modal_markup_present` — asserter `x-data` et `showPaywall` dans le HTML

### Tests de listing
- `test_catalogue_shows_lock_icon_on_premium_lessons` — GET catalogue → cadenas 🔒 sur leçons `gratuit=False`
- `test_catalogue_no_lock_on_free_lessons` — pas de cadenas sur leçons `gratuit=True`

## Sécurité

### Anti-contournement F12 (3 niveaux cumulatifs)

| Niveau | Technique | Ce que ça bloque |
|--------|-----------|------------------|
| **1 — Serveur** | `tronquer_contenu_markdown()` coupe à ~2 000 mots **avant** rendu HTML | Le DOM ne contient jamais le contenu complet — inspecter le HTML source ne donne rien |
| **2 — CSS** | `backdrop-filter: blur(4px)` + gradient overlay | Lecture impossible visuellement, même en désactivant `user-select` |
| **3 — CSS** | `user-select: none` + `-webkit-user-select: none` | Empêche le copier-coller rapide du texte visible au-dessus du blur |

### OWASP
- **A01 (Broken Access Control)** : le contenu Markdown complet n'est **jamais** envoyé dans le HTML pour les non-abonnés. Truncation côté serveur = protection à la source. Même si un attaquant supprime le CSS blur via DevTools, il n'aura que ~2 000 mots sur potentiellement 10 000+.
- **A03 (Injection)** : le contenu HTML est rendu via `render_markdown_to_html()` (python-markdown avec extensions sûres). Le modal ne contient que du texte marketing statique.
- Le `contenu_html|safe` est sûr car produit par le pipeline Markdown contrôlé (pas d'UGC non sanitisé).

### SEO vs Protection IP
- Les ~2 000 mots envoyés sont **suffisants pour le SEO** (Google indexe typiquement les premiers ~10 000 chars).
- Le contenu exclusif (démonstrations, exercices, études de cas) est dans la 2e moitié des leçons longues — protégé par la truncation.

## Performance

- **+0 requête SQL** : le flag `gratuit` est déjà sur `Lecon`, chargé dans le queryset existant
- **Truncation** : `O(n)` sur le texte, ~0.1ms pour 10 000 mots — négligeable
- **CSS** : `backdrop-filter: blur(4px)` est GPU-accelerated sur tous les navigateurs modernes
- **Poids modal** : `_paywall_modal.html` < 3 KB — pas d'impact TTFB
- **Budget** : +0 requête SQL, +0ms TTFB perceptible

## Definition of Done

- Leçons premium accessibles publiquement (plus de redirect `/connexion/`)
- Contenu tronqué côté serveur (~2 000 mots) pour les non-abonnés
- CSS blur progressif + `user-select: none` sur la zone de contenu
- CTA « Débloquer cette leçon » superposé au contenu flouté avec modal par-dessus incitant à créer un compte et s'abonner
- Cadenas 🔒 dans les listings (catalogue, accueil, chapitres)
- Admin voit toujours le contenu complet
- Aucune classe `dark:` dans les templates enfants
- Tests passent (truncation + vue + listing)
- CODEBASE_REFERENCE.md mis à jour (section 3 — Views, section 5 — Templates)
