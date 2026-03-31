# 34 — Analytics Granulaires (Temps passé)

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #45 |
| **Phase** | 10 — Scale & Autonomy |
| **Type** | Tech |
| **LLM recommandé** | Sonnet (suffisant — modèle TempsLecon, beacon/HTMX heartbeat, aggrégation Chart.js) |
| **Statut** | ⬜ À faire |
| **Priorité** | 34 |
| **Dépendances** | Aucune |

---

## Description

Tracking du temps passé par leçon : heartbeat toutes les 30s (beacon API ou XHR), stockage en base, agrégation par jour/semaine/mois pour le dashboard. Graphiques temps par matière et temps par jour.

## Critères d'acceptation

- Heartbeat toutes les 30s quand l'onglet est actif (`visibilitychange`)
- Endpoint `/cours/lecon/<int:pk>/heartbeat/` — incrémente +30s
- Modèle `TempsLecon` (user, lecon, date, secondes) — unique_together [user, lecon, date]
- Anti-triche : max 8h/leçon/jour, skip si inactif >5min
- Dashboard élève : graphique temps par jour (Chart.js) + total par matière
- Preview mode : pas d'écriture

## Architecture

- **Modèle** (`progress/models.py`) : `TempsLecon` (user FK, lecon FK, date, secondes IntegerField)
- **Vue** : `heartbeat_lecon(request, pk)` — POST, incrémente `F('secondes') + 30`, anti-triche check
- **URL** : `heartbeat_lecon` → `/cours/lecon/<int:pk>/heartbeat/`
- **JS** (`lecon.html`) : `setInterval` 30s + `document.visibilityState` check + `navigator.sendBeacon` fallback
- **Dashboard** : agrégation `TempsLecon.objects.filter(user=).values('date').annotate(total=Sum('secondes'))`
- **Chart.js** : ligne temps quotidien (7 derniers jours) + barres par matière

## Tests

- Heartbeat incrémente +30s
- Max 8h/jour respecté (28800s)
- Onglet inactif → pas d'incrément
- Dashboard affiche les totaux corrects
- Preview mode skip écriture

## Sécurité

- Heartbeat authentifié (`@login_required`)
- Anti-gaming : max 8h/jour, skip si dernière activité >5min
- Pas de tracking precise (résolution 30s, pas de mouse tracking)
- RGPD : données agrégées, pas de screenshots ou keylogging

## Performance

- 1 `update_or_create` par heartbeat (30s interval = 2/min)
- `F('secondes') + 30` atomique (pas de read-modify-write)
- Index sur (user, date)
- Dashboard : 1 agrégation SQL

## Definition of Done

- Heartbeat + stockage + anti-triche
- Dashboard graphiques temps
- Onglet inactif respecté
- Tests passent, CODEBASE_REFERENCE.md à jour
