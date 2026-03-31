# 15 — Messagerie Interne

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP_ROLES.md — Phase 5 (Étapes 5.1 à 5.2+) |
| **Phase** | Roles — Phase 5 |
| **Type** | Tech |
| **LLM recommandé** | **Opus** (nécessaire — helper contacts autorisés, HTMX polling, strip_tags, rate limiting, email notification) |
| **Statut** | ⬜ À faire |
| **Priorité** | 15 |
| **Dépendances** | #14 Dashboards Par Rôle |

---

## Description

Implémenter la messagerie interne entre utilisateurs liés. Les modèles `Conversation` et `Message` existent déjà (Phase 1 / #11). Ajouter les règles d'accès, les vues, les templates HTMX et les notifications de message.

## Sous-étapes

### 5.1 — Helper `contacts_autorises(user)`
- Admin : tous sauf lui-même
- Enseignant : ses élèves liés validés + parents de ses élèves
- Parent : enseignants de ses enfants
- Élève : ses enseignants liés validés
- Retourne un QuerySet (chaînable)

### 5.2 — Vues Messagerie
- `liste_conversations_view` — annotate `dernier_message_date`, `non_lus`
- `nouvelle_conversation_view` — sélection destinataire dans `contacts_autorises()`
- `conversation_detail_view` — messages paginés 50/page, envoi POST HTMX
- `nouveaux_messages_view` — fragment HTMX polling 5s

### Règles d'accès

| Rôle | Peut contacter |
|------|----------------|
| Admin | Tous |
| Enseignant | Élèves liés + leurs parents |
| Parent | Enseignants de ses enfants |
| Élève | Ses enseignants |

## Tests

- Tests helper `contacts_autorises` par rôle (4 tests)
- Tests vues (accès, IDOR, envoi message, polling)
- Tests rate limiting (30 msg/h)
- Tests `strip_tags()` sur contenu

## Sécurité

- `strip_tags()` + `escape()` sur le contenu — double protection XSS
- Vérification participant dans chaque vue
- Rate limit 30 msg/h par utilisateur
- Pas de pièces jointes (MVP)

## Performance

- `prefetch_related("messages__auteur", "participants")` sur conversations
- Polling 5s = 12 req/min max par utilisateur
- Cache `msg_count_{user_id}` pour badge non lus
- Pagination 50 messages/page

## Definition of Done

- Helper `contacts_autorises()` implémenté et testé
- 4 vues messagerie + HTMX polling
- Rate limiting + sanitization
- Tests passent, CODEBASE_REFERENCE.md à jour
