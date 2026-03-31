# 28 — Tuteur IA Socratique

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #39 |
| **Phase** | 8 — Intelligence Artificielle |
| **Type** | Feature |
| **LLM recommandé** | **Opus** (nécessaire — intégration API OpenAI/Anthropic, prompt engineering, gestion du contexte de conversation, sécurité anti-jailbreak) |
| **Statut** | ⬜ À faire |
| **Priorité** | 28 |
| **Dépendances** | Aucune |

---

## Description

Chat IA intégré dans la page leçon : l'élève pose des questions sur le contenu, l'IA répond en mode socratique (guide par des questions, ne donne pas directement la réponse). Contexte : contenu de la leçon. Historique de conversation par session.

## Critères d'acceptation

- Bouton "🤖 Poser une question" dans `lecon.html`
- Chat overlay / sidebar (Alpine.js `x-show`)
- Réponses en mode socratique (prompt system : "Guide l'élève par des questions, ne donne jamais la réponse directement")
- Contexte = contenu Markdown de la leçon (pas de retrieval external)
- Historique par session (sessionStorage ou modèle léger)
- Rate limiting : 20 messages / élève / heure
- Fallback gracieux si API indisponible

## Architecture

- **Settings** : `AI_PROVIDER` (openai/anthropic), `AI_API_KEY`, `AI_MODEL`
- **Vue** : `chat_ia(request, lecon_pk)` — POST HTMX, retourne HTML du message
- **URL** : `/cours/lecon/<int:pk>/chat/`
- **Prompt system** : stocké dans `courses/utils/ai_prompts.py` (pas dans la vue)
- **Template** : composant Alpine.js dans `lecon.html` — messages scrollables, input + bouton envoyer
- **Modèle optionnel** : `ConversationIA` (user, lecon, messages JSON, created_at) — TTL 24h
- **Anti-jailbreak** : sanitization du message, longueur max 500 chars, refus de répondre hors sujet

## Tests

- Réponse 200 avec message HTML
- Rate limiting déclenché après 20 messages
- Message trop long → 400
- Leçon inexistante → 404
- Preview mode : chat fonctionnel (read-only, pas d'écriture convo)

## Sécurité

- **A03 Injection** : message sanitisé avant envoi à l'API, réponse échappée avant rendu
- **Anti-jailbreak** : prompt system non modifiable par l'utilisateur, instructions fermes
- **A04 IDOR** : vérifie que l'élève a accès à la leçon (chapitre débloqué)
- **A05** : clé API jamais exposée côté client
- Rate limiting sévère pour éviter l'abus de l'API (coûts)
- Pas de PII envoyé à l'API (pseudo anonyme dans le prompt)

## Performance

- Appel API réseau : 500ms-3s selon le modèle
- Streaming recommandé (SSE) pour UX fluide
- Contexte limité au contenu de la leçon (~2000 tokens max)

## Definition of Done

- Chat fonctionnel mode socratique
- Rate limiting, anti-jailbreak, sanitization
- Historique session, fallback erreur
- Tests passent, CODEBASE_REFERENCE.md à jour
