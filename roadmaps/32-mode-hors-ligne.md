# 32 — Mode Hors-Ligne

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #42 |
| **Phase** | 9 — Progressive Web App (PWA) |
| **Type** | Feature |
| **LLM recommandé** | Sonnet (suffisant — extension SW, IndexedDB via idb-keyval, sync queue) |
| **Statut** | ⬜ À faire |
| **Priorité** | 32 |
| **Dépendances** | #31 PWA Manifest & SW |

---

## Description

Extension du service worker pour permettre la lecture des leçons hors-ligne. Les leçons visitées sont mises en cache automatiquement. Une page `/offline/` sert de fallback quand aucune page n'est en cache. Les quiz soumis hors-ligne sont mis en queue et synchronisés au retour de la connexion.

## Critères d'acceptation

- Leçons visitées automatiquement cachées (HTML + KaTeX CSS)
- Page `/offline/` avec liste des leçons disponibles en cache
- Quiz : réponses stockées en IndexedDB, sync au `online` event
- Indicateur visuel "Mode hors-ligne" dans le header
- Cache limité à 50 leçons (LRU eviction)
- Pas de données sensibles dans le cache

## Architecture

- **`sw.js`** : stratégie CacheFirst pour `/cours/lecon/*`, fallback `/offline/`
- **IndexedDB** : `idb-keyval` (CDN) pour queue de quiz soumissions
- **`base.html`** : Alpine.js composant `onlineStatus()` — écoute `online/offline` events
- **Template** : `templates/offline.html` — liste des leçons en cache via `caches.keys()`
- **Vue** : `offline_view(request)` — retourne la page (aussi cachée par SW)
- **Sync** : `navigator.serviceWorker.addEventListener('message')` pour trigger sync

## Tests

- Page `/offline/` accessible (200)
- `sw.js` contient le handler fetch pour `/cours/lecon/`
- Pas de données utilisateur dans le cache (vérifier absence de noms/emails)

## Sécurité

- Cache : contenu public uniquement (leçons), pas de tokens/sessions
- Sync queue : validation côté serveur au moment du replay
- IndexedDB : données non sensibles (réponses quiz uniquement)

## Performance

- Cache : ~50KB par leçon (HTML pré-rendu)
- 50 leçons max = ~2.5MB
- LRU eviction automatique

## Definition of Done

- Leçons lisibles hors-ligne
- Quiz queue + sync automatique
- Fallback offline page
- Tests passent, CODEBASE_REFERENCE.md à jour
