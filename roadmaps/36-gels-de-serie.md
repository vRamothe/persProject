# 36 — Gels de Série (Streak Freeze)

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #47 |
| **Phase** | 10 — Scale & Autonomy |
| **Type** | Feature |
| **LLM recommandé** | Sonnet (suffisant — modèle léger, vérification dans helper streak existant) |
| **Statut** | ⬜ À faire |
| **Priorité** | 36 |
| **Dépendances** | Série de connexion déjà implémentée (ConnexionLog) |

---

## Description

Gels de série : l'élève peut "geler" un jour manqué pour ne pas casser sa série de connexion. Max 1 gel actif, rechargeable après 7 jours de série consécutifs. Visuel dans le dashboard (icône givre).

## Critères d'acceptation

- Champ `gel_serie_disponible` (BooleanField default=False) sur CustomUser
- Automatiquement accordé après 7 jours de série consécutifs
- Bouton "🧊 Activer le gel" dans le dashboard — consomme le gel
- Lors du calcul de la série, un jour gelé ne casse pas la chaîne
- Max 1 gel actif (pas d'accumulation)
- Dashboard : indicateur gel disponible / gel actif / gel consommé
- Pas de gel en mode preview

## Architecture

- **Modèle** : `CustomUser` + `gel_serie_disponible` BooleanField + `dernier_gel_utilise` DateField nullable
- **Helper** : modifier `_calculer_serie(user)` dans `progress/views.py` — check si `dernier_gel_utilise` = jour manqué
- **Vue** : `activer_gel(request)` — POST, set `gel_serie_disponible=False`, `dernier_gel_utilise=today`
- **URL** : `/progression/activer-gel/`
- **Dashboard** : icône givre si disponible, icône utilisée si actif, grisé sinon
- **Attribution** : dans `_dashboard_eleve`, si serie >= 7 et `gel_serie_disponible=False` et pas de gel récent → `gel_serie_disponible=True`

## Tests

- Gel disponible après 7 jours consécutifs
- Gel consommé → série préservée malgré 1 jour manqué
- 2 jours manqués → série cassée (1 seul gel)
- Gel rechargé après 7 jours post-utilisation
- Preview mode skip écriture

## Sécurité

- `@login_required` + `@require_POST` sur activer_gel
- `request.user` uniquement (pas d'IDOR)
- Anti-spam : rate limiting 3 req/min

## Performance

- +1 condition dans `_calculer_serie` (déjà O(n) sur ConnexionLog)
- +0 requête SQL supplémentaire (champs sur CustomUser)

## Definition of Done

- Gel accordé, activé, consommé, rechargé
- Série préservée avec gel
- Dashboard visuel (givre)
- Tests passent, CODEBASE_REFERENCE.md à jour
