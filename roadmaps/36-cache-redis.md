# 36 — Cache Redis

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #46 |
| **Phase** | 10 — Scale & Autonomy |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — django-redis config, @cache_page, invalidation signals) |
| **Statut** | ⬜ À faire |
| **Priorité** | 36 |
| **Dépendances** | Aucune |

---

## Description

Cache Redis pour les vues les plus sollicitées : catalogue public, chapitres, leçons publiques. Invalidation automatique quand un contenu est modifié. Session backend Redis (remplacement DB sessions).

## Critères d'acceptation

- Redis ajouté à docker-compose.yml (service `redis`)
- `django-redis` configuré comme CACHES default
- `@cache_page(300)` sur `catalogue_view`, `lecon_publique_view`
- Invalidation : signal `post_save` sur Lecon/Chapitre → `cache.delete_pattern('*lecon*')`
- Sessions backend : `django.contrib.sessions.backends.cache`
- Heroku : `REDIS_URL` via Redis addon
- Fallback : `LocMemCache` si `REDIS_URL` absente

## Architecture

- **docker-compose.yml** : service `redis:7-alpine`, lien vers `web`
- **Settings** : `CACHES = {'default': django_redis.cache.RedisCache}` si `REDIS_URL`
- **Décorateurs** : `@cache_page(300)` sur vues publiques, `@vary_on_cookie` pour authentifiées
- **Signals** : `courses/signals.py` — `post_save` Lecon, Chapitre → invalidation
- **Requirements** : `django-redis`
- **Heroku** : `REDIS_URL` auto-set par Heroku Redis addon

## Tests

- Cache hit : 2e requête plus rapide (mock cache)
- Invalidation : modification leçon → cache vidé
- Sessions persistent via Redis
- Fallback LocMemCache si pas de Redis

## Sécurité

- Redis non exposé publiquement (Docker réseau interne, Heroku private URL)
- Pas de données sensibles dans le cache (vues publiques uniquement)
- `@vary_on_cookie` pour vues authentifiées (pas de cache cross-user)

## Performance

- Pages publiques : TTFB ~5ms au lieu de ~50ms
- Redis : <1ms latence locale
- Session read : ~0.5ms au lieu de ~5ms (DB)

## Definition of Done

- Redis en Docker + Heroku
- Cache sur vues publiques + invalidation
- Sessions Redis, fallback LocMemCache
- Tests passent, CODEBASE_REFERENCE.md à jour
