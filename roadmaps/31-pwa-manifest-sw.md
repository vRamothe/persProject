# 31 — PWA : Manifest & Service Worker

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #41 |
| **Phase** | 9 — Progressive Web App (PWA) |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — manifest.json, SW basique cache-first, balises meta) |
| **Statut** | ⬜ À faire |
| **Priorité** | 31 |
| **Dépendances** | Aucune |

---

## Description

Transformer ScienceLycée en PWA installable : manifest.json avec icônes, service worker avec stratégie cache-first pour les assets statiques + network-first pour les pages Django. Bouton "Installer l'app" visible sur mobile.

## Critères d'acceptation

- `manifest.json` servi depuis `/manifest.json` (vue Django ou staticfile)
- Icônes 192x192 et 512x512 (PNG)
- `<link rel="manifest">` dans `base.html`
- `<meta name="theme-color">` (bleu-600)
- Service worker `sw.js` enregistré
- Cache-first : CSS CDN (Tailwind, HTMX, Alpine, KaTeX), icônes
- Network-first : pages HTML Django
- Stale-while-revalidate : manifest, fonts
- Bouton "Installer" via `beforeinstallprompt` event (Alpine.js)
- Lighthouse PWA : installable

## Architecture

- **`static/manifest.json`** ou **vue** : name, short_name, icons, start_url, display standalone, theme_color, background_color
- **`static/sw.js`** : event listeners install/fetch/activate, cache versioning `CACHE_V1`
- **`base.html`** : `<link rel="manifest">`, `<meta name="theme-color">`, script enregistrement SW
- **Icônes** : `static/icons/icon-192.png`, `static/icons/icon-512.png`
- **Alpine install prompt** : `x-data="installPrompt()"` dans `base.html`

## Tests

- `manifest.json` accessible et JSON valide
- `sw.js` accessible et JavaScript valide
- `base.html` contient `<link rel="manifest">`
- Lighthouse PWA installable

## Sécurité

- SW scope limité à `/` (pas d'accès cross-origin)
- Cache versioning pour invalidation
- Pas de données sensibles dans le cache (uniquement assets publics)

## Performance

- Cache-first assets : -200ms sur repeat visits
- SW install : ~50KB, one-time
- Network-first pages : latence identique, fallback offline page

## Definition of Done

- PWA installable sur Chrome/Edge/Safari mobile
- Service worker cache fonctionnel
- Bouton install visible mobile
- Lighthouse PWA pass, tests passent, CODEBASE_REFERENCE.md à jour
