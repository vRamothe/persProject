# 29 — Génération Dynamique de Questions

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #40 |
| **Phase** | 8 — Intelligence Artificielle |
| **Type** | Feature |
| **LLM recommandé** | **Opus** (nécessaire — génération IA structurée, validation schéma JSON, queue asynchrone, modération) |
| **Statut** | ⬜ À faire |
| **Priorité** | 29 |
| **Dépendances** | #28 Tuteur IA |

---

## Description

Génération automatique de questions de quiz par IA à partir du contenu d'une leçon. L'admin déclenche la génération, les questions sont créées en statut "brouillon" pour modération. Types supportés : QCM, vrai/faux, texte libre. L'IA respecte le niveau scolaire et la difficulté.

## Critères d'acceptation

- Bouton "🤖 Générer des questions" dans l'admin du quiz
- Paramètres : nb questions, types souhaités, difficulté
- Questions générées en statut brouillon (pas publiées directement)
- Format : JSON structuré parsé → objets Question
- Admin valide/modifie/supprime avant publication
- Prompt inclut le contenu de la leçon + le niveau scolaire

## Architecture

- **Vue admin** : `generer_questions_ia(request, quiz_pk)` — admin only
- **URL** : `/admin-tools/generer-questions/<int:pk>/`
- **Prompt** : `courses/utils/ai_prompts.py` — template avec leçon, niveau, nb, types, difficulté
- **Parsing** : JSON structuré → `Question.objects.create(statut='brouillon', ...)`
- **Modèle** : `Question` + champ `statut` (brouillon/publie) ou `est_brouillon` BooleanField
- **Template** : formulaire de paramètres + résultat avec preview des questions générées
- **Validation** : schéma JSON strict (jsonschema lib) — type, enonce, options, reponse_correcte

## Tests

- Génération crée N questions en brouillon
- Questions brouillon non visibles dans les quiz élèves
- JSON invalide → erreur gracieuse
- Admin-only access
- Prompt contient le bon contenu et niveau

## Sécurité

- **A01** : admin-only (`is_staff` ou `role == 'admin'`)
- **A03** : contenu généré sanitisé avant stockage (pas de HTML/JS)
- Réponses IA validées par schéma JSON strict
- Clé API protégée (côté serveur uniquement)
- Rate limiting : 5 générations / admin / heure

## Performance

- Génération : 3-10s (async recommandé)
- Batch : 5-20 questions par appel
- Parsing JSON + validation + bulk_create

## Definition of Done

- Génération fonctionnelle en brouillon
- Modération admin avant publication
- Validation schéma JSON, sanitization
- Tests passent, CODEBASE_REFERENCE.md à jour
