# 11 — Modèles de Données Multi-Rôles

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP_ROLES.md — Phase 1 (Étapes 1.1 à 1.6) |
| **Phase** | Roles — Phase 1 |
| **Type** | Tech |
| **LLM recommandé** | **Opus** (nécessaire — 5 nouveaux modèles, override save(), migration 3 étapes, contraintes complexes) |
| **Statut** | ⬜ À faire |
| **Priorité** | 11 |
| **Dépendances** | Aucune |
| **Bloque** | #12 Inscription Multi-rôles, #13 Validation Liaisons, #14 Dashboards Par Rôle |

---

## Description

Poser les fondations du système multi-rôles en étendant le modèle utilisateur et en créant les modèles de liaison, notification et messagerie. Aucune vue ni template — uniquement modèles, migrations et tests unitaires.

## Sous-étapes

### 1.1 — Étendre `RoleChoices`
- Ajouter `enseignant` et `parent` aux choices
- Propriétés `is_enseignant`, `is_parent` sur `CustomUser`

### 1.2 — Ajouter `code_identifiant`
- `CharField(8)`, unique, auto-généré via `_generer_code_identifiant()`
- Préfixes : ELV, ENS, PAR, ADM
- `secrets.token_hex(3)[:5].upper()` (5 retries)
- Override `save()` — génère au premier save uniquement

### 1.3 — Modèles de liaison
- `StatutLienChoices` : en_attente, valide, refuse
- `LienEnseignantEleve` : FK enseignant + FK élève, unique_together, index (eleve, statut)
- `LienParentEleve` : FK parent + FK élève, unique_together, index (eleve, statut)
- `clean()` : max 1 enseignant validé, max 2 parents validés par élève
- `limit_choices_to` sur les FK

### 1.4 — Modèle `Notification`
- `TypeNotificationChoices` : demande_liaison, liaison_validee, liaison_refusee, nouveau_message, systeme
- Champs : destinataire FK, type, titre, contenu, lue, lien, cree_le
- Index composite `(destinataire, lue, -cree_le)`, ordering `-cree_le`

### 1.5 — Modèles Messagerie
- `Conversation` : M2M participants, ordering `-mis_a_jour_le`
- `Message` : FK conversation, FK auteur, contenu (max 2000), lu, envoye_le
- Index `(conversation, -envoye_le)` et `(conversation, lu)`

### 1.6 — Migrations (3 étapes)
1. Migration 1 : ajout champs + nouveaux modèles (code_identifiant null=True)
2. Migration 2 : data migration backfill code_identifiant (`bulk_update`)
3. Migration 3 : `AlterField` → null=False, unique=True

## Tests (12+ minimum)

- `test_creation_user_eleve_code_identifiant_prefixe_ELV`
- `test_creation_user_enseignant_code_identifiant_prefixe_ENS`
- `test_creation_user_parent_code_identifiant_prefixe_PAR`
- `test_creation_user_admin_code_identifiant_prefixe_ADM`
- `test_code_identifiant_unique_entre_utilisateurs`
- `test_code_identifiant_collision_retry`
- `test_lien_enseignant_eleve_unique_together` → IntegrityError
- `test_lien_parent_eleve_unique_together` → IntegrityError
- `test_max_2_parents_valides_par_eleve` → ValidationError
- `test_notification_ordering_par_cree_le_desc`
- `test_message_contenu_max_2000_caracteres` → ValidationError
- `test_statut_lien_defaut_en_attente`

## Sécurité

- `secrets.token_hex()` (CSPRNG) pour les codes
- Codes non sensibles (partageables)
- `limit_choices_to` protège l'admin

## Performance

- `db_index=True` sur `code_identifiant` et `statut`
- Index composites pour les lookups fréquents

## Definition of Done

- Tous les modèles créés et testés
- 3 migrations exécutables (base vide + peuplée)
- Rollback fonctionnel
- CODEBASE_REFERENCE.md mis à jour
