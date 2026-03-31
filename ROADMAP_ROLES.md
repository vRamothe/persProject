# Roadmap — Système multi-rôles (Élève · Enseignant · Parent)

## Vue d'ensemble

Extension du système utilisateur de ScienceLycée pour supporter 4 rôles :
- **Admin** — inchangé, supervise tout
- **Élève** — apprend, peut valider les demandes de liaison parent
- **Enseignant** — suit ses élèves, communique avec élèves et parents
- **Parent** — suit ses enfants, communique avec les enseignants

### Règles métier fondamentales

| Rôle | Création de compte | Liaison requise | Validation par |
|------|-------------------|-----------------|----------------|
| Élève | Seul OU avec code enseignant | Non obligatoire | Enseignant (si code fourni) |
| Enseignant | Seul | Non obligatoire | Email (vérification classique) |
| Parent | Avec code élève uniquement | Obligatoire | Élève |

### Règle d'attribution par défaut

> **Tout élève sans enseignant lié est considéré comme « élève de l'administrateur ».**
> L'admin les voit dans son panel comme s'il était leur enseignant. Dès qu'un enseignant valide un lien avec cet élève, l'élève sort du pool admin et apparaît dans le panel de son enseignant.
>
> Un élève peut avoir **un seul enseignant** lié (validé) à la fois.
> Un élève peut avoir **au maximum 2 parents** liés (validés).

### Flux de validation

```
Élève s'inscrit avec code enseignant :
  Élève → compte inactif → email vérifié → compte actif MAIS lien "en attente"
  → Enseignant reçoit notification → approuve/refuse → lien validé

Élève s'inscrit seul :
  Élève → compte inactif → email vérifié → compte actif
  (Aucune autre validation requise, l'élève est rattaché à l'admin par défaut)

Parent s'inscrit avec code élève :
  Parent → compte inactif → email vérifié → compte actif MAIS lien "en attente"
  → Élève reçoit notification → approuve/refuse → lien validé

Enseignant s'inscrit seul :
  Enseignant → compte inactif → email vérifié → compte actif
```

---

## Standards transversaux

### Convention de qualité de code

Chaque étape d'implémentation doit respecter :

- **Nommage** : fonctions, variables et URL en français (convention existante)
- **FBV** : vues function-based avec `@login_required` sauf raison claire pour CBV
- **DRY** : extraire les helpers dès la deuxième utilisation (ex: vérification de lien validé)
- **Single Responsibility** : une vue = une action. Pas de vue qui fait à la fois création + validation + notification
- **Imports** : groupés par stdlib / Django / app locale, séparés par une ligne vide
- **Pas de logique métier dans les templates** : tout calcul dans la vue, le template affiche uniquement
- **Pas de dark: classes dans les templates enfants** (convention existante)
- **Docstrings** : une ligne pour chaque nouvelle vue et chaque nouveau modèle

### Convention d'architecture

Organisation des fichiers et séparation des responsabilités :

- **Fichiers helpers** : créer `helpers.py` dans une app dès qu'un helper est réutilisé par ≥ 2 vues ou par une autre app (ex: `users/helpers.py` → `peut_voir_eleve()`, `contacts_autorises()`). Le fichier ne contient que des fonctions pures ou des fonctions recevant des objets Django — jamais d'accès à `request`
- **Fichiers services** : créer `services.py` dans une app quand une action métier implique plusieurs modèles ou effets de bord (ex: `users/services.py` → `creer_lien_et_notifier()`). Un service peut accéder à `request` si nécessaire pour le contexte (email, session)
- **Seuil pour une nouvelle app Django** : ≥ 3 modèles propres + vues dédiées + templates propres. En dessous, ajouter dans une app existante. Exception : messagerie (`messaging/`) car domaine clairement distinct
- **Transactions** : `transaction.atomic()` obligatoire pour toute opération groupée (création compte + lien + notification, envoi message + notification, validation lien + notification). Pattern :
  ```python
  from django.db import transaction

  with transaction.atomic():
      lien = LienEnseignantEleve.objects.create(...)
      Notification.objects.create(...)
  ```
- **Signaux Django** : éviter sauf pour le découplage inter-apps strict (ex: `progress` réagit à un événement `courses`). Préférer les appels explicites dans les services. Justification obligatoire en commentaire si un signal est utilisé

### Convention de tests

- **`client.force_login(user)`** systématiquement (django-axes interdit `client.login()`)
- **Structure des fichiers test** : migrer vers un dossier `tests/` par app avec `conftest.py` + fichiers par domaine :
  ```
  users/
    tests/
      __init__.py
      conftest.py           # fixtures partagées pour l'app
      test_inscription.py
      test_liaisons.py
      test_dashboard.py
      test_notifications.py
  ```
- **Fixtures réutilisables dans `conftest.py`** : `eleve`, `admin_user`, `enseignant`, `parent_user`, `lien_enseignant_eleve_valide`, `lien_parent_eleve_valide`. Chaque fixture crée l'objet minimal nécessaire. Les fixtures de lien dépendent des fixtures utilisateur
- **Nommage des tests** : `test_{action}_{scenario}_{resultat_attendu}` — exemples :
  - `test_inscription_eleve_code_invalide_erreur_formulaire`
  - `test_valider_lien_enseignant_deja_lie_refuse`
  - `test_fiche_eleve_parent_non_lie_403`
- **Ratio minimum par vue** : chaque vue doit avoir au minimum 3 tests :
  1. Accès anonyme → redirect vers login
  2. Accès rôle interdit → 403
  3. Accès rôle autorisé → 200 (ou 302 si redirect attendu)
- **Assertion sur l'état DB** : chaque test de modification de données doit vérifier l'état de la base après l'action (`assert Model.objects.filter(...).exists()`, `assert obj.statut == "valide"`, etc.)
- **Tests IDOR obligatoires** : toute vue accédant aux données d'un autre utilisateur doit avoir un test vérifiant qu'un utilisateur non autorisé reçoit 403 (ex: enseignant A tente de voir la fiche d'un élève de l'enseignant B)
- **Pattern HTMX** : les tests de vues HTMX vérifient le fragment HTML retourné, pas un redirect
- **Fichiers existants** : `users/tests.py` pour les vues users, `courses/tests/test_courses.py` pour les cours. Migrer vers la structure `tests/` à partir de la Phase 2

### Convention de sécurité

- **OWASP Top 10** vérifié à chaque phase
- **Broken Access Control** (#1) : chaque vue vérifie le rôle ET le lien validé
- **Injection** (#3) : pas de `|safe` sur des données utilisateur, `escape()` systématique
- **IDOR** : tout accès à une ressource par ID doit vérifier que l'utilisateur a le droit
- **Enumeration** : messages d'erreur génériques pour les codes invalides
- **CSRF** : toutes les actions POST via formulaire ou HTMX (déjà couvert par Django + meta CSRF)
- **Rate limiting** : sur tout endpoint de création (inscription, liaison, message)

### Convention de performance

- **Budgets de requêtes SQL par type de page** :
  - Page liste (matières, chapitres, élèves) : **5 requêtes max**
  - Page détail (leçon, fiche élève, conversation) : **8 requêtes max**
  - Dashboard (élève, enseignant, parent, admin) : **12 requêtes max**
  - Vérifier avec `django.test.utils.override_settings(DEBUG=True)` + `len(connection.queries)` dans les tests de performance
- **`select_related` / `prefetch_related`** : obligatoire pour tout FK ou M2M accédé dans un template ou une boucle. Exemples :
  - `LienEnseignantEleve.objects.select_related("enseignant", "eleve")` pour les pages de liaisons
  - `Conversation.objects.prefetch_related("messages__auteur")` pour l'inbox
- **Pagination** : 25 éléments par page sauf :
  - Conversations : 50 messages par page (derniers messages d'abord)
  - Notifications : 25 par page
- **Cache** : compteurs de notifications non lues et compteurs de messages non lus stockés en cache (`django.core.cache`). Invalidation à chaque écriture (création notification, envoi message, marquage lu). Clé : `notif_count_{user_id}`, `msg_count_{user_id}`
- **Indexes** : ajouter `db_index=True` sur les champs utilisés dans les filtres fréquents
- **Bulk operations** : `bulk_create()` pour les seeds, pas de boucle `save()` unitaire

### Convention de migration

Règles pour toute création ou modification de migration :

- **Ordre pour un nouveau champ obligatoire + unique** :
  1. Migration 1 : ajouter le champ en `null=True, blank=True` (sans unique)
  2. Migration 2 (data migration) : remplir les valeurs pour les lignes existantes
  3. Migration 3 : `AlterField` → `null=False, unique=True`
- **Réversibilité** : toute migration doit être réversible. Pas de `RunPython` sans `reverse_code`. Minimum acceptable : `reverse_code=migrations.RunPython.noop` avec commentaire justificatif
- **Bulk operations dans les data migrations** : utiliser `bulk_update()` / `bulk_create()` pour traiter les données existantes. Pas de boucle `.save()` unitaire dans une data migration
- **Jamais d'édition manuelle** de migration existante sauf pour corriger un squash. Générer une nouvelle migration à la place
- **Nommage** : laisser Django auto-nommer (`XXXX_auto_...`). Renommer uniquement les data migrations manuelles en `XXXX_descriptif` (ex: `0003_backfill_code_identifiant`)

### Convention de documentation

- **Docstring d'une ligne** pour toute nouvelle vue et tout nouveau modèle. Format : `"""Verbe + objet."""` (ex: `"""Liste les liaisons en attente pour l'enseignant."""`)
- **Mise à jour obligatoire de `CODEBASE_REFERENCE.md`** après tout changement de code :
  - Nouveau modèle ou champ → section 1 (Models)
  - Nouvelle URL → section 2 (URLs)
  - Nouvelle vue → section 3 (Views)
  - Nouveau formulaire → section 4 (Forms)
  - Nouveau template → section 5 (Templates)
  - Changement settings → section 6 (Settings)
  - Nouvelle commande → section 7 (Management Commands)
  - Nouveau pattern → section 8 (Key Patterns)
- **Pas de commentaires inline** sauf logique complexe nécessitant une explication (regex, algorithme, workaround). Un commentaire inline doit expliquer le *pourquoi*, jamais le *quoi*
- **`ROADMAP_ROLES.md`** : mis à jour à la fin de chaque phase pour refléter l'état réel (cocher les étapes terminées, noter les écarts avec le plan initial)

---

## Phase 1 — Modèles de données

> **Objectif** : poser les fondations du système multi-rôles en étendant le modèle utilisateur et en créant les modèles de liaison, notification et messagerie. Aucune vue, aucun template, aucun formulaire dans cette phase — uniquement les modèles, migrations et tests unitaires.

### Décisions d'architecture (Phase 1)

| Décision | Justification |
|----------|---------------|
| Tous les nouveaux modèles dans `users/models.py` | Moins de 3 modèles de messagerie (Conversation + Message = 2) → en dessous du seuil pour créer une app `messaging/`. On regroupe tout ce qui touche aux rôles et aux relations dans `users/`. Si la messagerie grossit en Phase 5+, on migrera vers une app dédiée |
| `_generer_code_identifiant()` est une méthode privée du modèle `CustomUser` | La logique de génération est intrinsèque à l'entité utilisateur : préfixe basé sur le rôle, unicité. Aucun signal `post_save` car c'est de la logique interne au modèle, pas du découplage inter-apps |
| `save()` overridé pour la génération auto | Le code doit être généré au premier `save()` uniquement. Un signal serait superflu et masquerait une logique métier simple. On vérifie `if not self.code_identifiant` pour ne pas écraser un code existant |
| `Notification` et `Message` dans `users/` | Notifications et messages sont centrés sur les utilisateurs et leurs relations. Pas de domaine métier distinct tant qu'on n'a pas de routage complexe, de pièces jointes, ou de threads |
| `StatutLienChoices` partagé entre les deux modèles de lien | Un seul enum pour `LienEnseignantEleve` et `LienParentEleve` — mêmes transitions d'état (en_attente → valide/refuse) |

---

### Étape 1.1 — Étendre `RoleChoices` avec `enseignant` et `parent`

**Modification** : `users/models.py` → `RoleChoices`

```python
class RoleChoices(models.TextChoices):
    ADMIN = "admin", "Administrateur"
    ELEVE = "eleve", "Élève"
    ENSEIGNANT = "enseignant", "Enseignant"
    PARENT = "parent", "Parent"
```

**Ajouts sur `CustomUser`** :

```python
@property
def is_enseignant(self):
    return self.role == RoleChoices.ENSEIGNANT

@property
def is_parent(self):
    return self.role == RoleChoices.PARENT
```

> **Impact** : le champ `role` utilise `max_length=10` — `"enseignant"` fait 10 caractères, ça passe. Si on ajoutait un rôle plus long à l'avenir, il faudrait migrer le max_length.

#### 🎯 Critères d'acceptation

- `RoleChoices` contient exactement 4 valeurs : `admin`, `eleve`, `enseignant`, `parent`
- `CustomUser(role="enseignant").is_enseignant` retourne `True`
- `CustomUser(role="parent").is_parent` retourne `True`
- `is_eleve`, `is_admin` continuent de fonctionner sans régression
- Les 208 tests existants passent toujours (aucune régression)

#### 🔒 Sécurité

- Aucun risque — c'est un ajout de choices, pas de données sensibles exposées

#### ⚡ Performance

- Aucun index impacté, aucune requête modifiée

#### ✅ Definition of Done

- [ ] `RoleChoices` contient les 4 valeurs
- [ ] Propriétés `is_enseignant` et `is_parent` ajoutées à `CustomUser`
- [ ] Tests existants passent (0 échec)
- [ ] `CODEBASE_REFERENCE.md` section 1.1 et 1.3 mises à jour

---

### Étape 1.2 — Ajouter `code_identifiant` sur `CustomUser`

**Modification** : `users/models.py` → `CustomUser`

```python
import secrets

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # ... champs existants ...

    code_identifiant = models.CharField(
        max_length=8,
        unique=True,
        blank=True,
        null=True,      # null=True pour la migration en 3 étapes (existants)
        verbose_name="Code d'identification",
        db_index=True,
    )

    PREFIXES_ROLE = {
        RoleChoices.ELEVE: "ELV",
        RoleChoices.ENSEIGNANT: "ENS",
        RoleChoices.PARENT: "PAR",
        RoleChoices.ADMIN: "ADM",
    }

    def _generer_code_identifiant(self):
        """Génère un code unique : préfixe rôle (3 car) + 5 hex aléatoires."""
        prefixe = self.PREFIXES_ROLE.get(self.role, "ELV")
        for _ in range(5):
            code = prefixe + secrets.token_hex(3)[:5].upper()  # 3+5 = 8 car
            if not CustomUser.objects.filter(code_identifiant=code).exists():
                return code
        raise RuntimeError(
            f"Impossible de générer un code_identifiant unique après 5 tentatives "
            f"pour le rôle {self.role}"
        )

    def save(self, *args, **kwargs):
        if not self.code_identifiant:
            self.code_identifiant = self._generer_code_identifiant()
        super().save(*args, **kwargs)
```

> **`secrets.token_hex(3)`** produit 6 caractères hex. On en prend 5 → 16^5 = 1 048 576 combinaisons par préfixe. Largement suffisant pour une plateforme scolaire. Si on atteint un taux de collision élevé, on augmentera la longueur.

#### 🎯 Critères d'acceptation

- Un `code_identifiant` est généré automatiquement lors du premier `save()` si absent
- Le préfixe correspond au rôle : `ELV` pour élève, `ENS` pour enseignant, `PAR` pour parent, `ADM` pour admin
- Le code fait exactement 8 caractères (3 préfixe + 5 hex uppercase)
- En cas de collision, un nouveau code est généré (max 5 retries)
- Après 5 collisions consécutives, une `RuntimeError` est levée
- Un `save()` sur un utilisateur existant ne change pas son code
- Le champ est `unique=True` et `db_index=True`

#### 🏗 Architecture

- `_generer_code_identifiant()` est une méthode privée (préfixe `_`) car elle ne doit pas être appelée depuis l'extérieur
- On override `save()` plutôt que d'utiliser un signal `post_save` : la génération est de la logique interne au modèle, pas un effet de bord inter-apps
- `secrets.token_hex()` au lieu de `random.choice()` pour la sécurité cryptographique, même si le code n'est pas un secret à proprement parler — c'est la convention du projet

#### 🔒 Sécurité

- `secrets.token_hex()` (CSPRNG) — pas de `random` standard
- Le code ne contient aucune information sensible (pas de PII, pas de date)
- Le code est public (partageable) — il sert d'identifiant de liaison, pas d'authentification
- Protection contre l'énumération : les vues (Phase 2+) retourneront des messages génériques si un code est invalide

#### ⚡ Performance

- `db_index=True` sur `code_identifiant` — recherche O(log n) pour les lookups par code
- La boucle de retry (max 5) ne fait des requêtes supplémentaires qu'en cas de collision, événement statistiquement rare (probabilité < 0.001% avec < 10 000 utilisateurs)

#### ✅ Definition of Done

- [ ] Champ `code_identifiant` ajouté avec `unique=True`, `db_index=True`
- [ ] `_generer_code_identifiant()` implémenté avec retry (5 max)
- [ ] `save()` overridé — génère le code au premier save uniquement
- [ ] Migration en 3 étapes créée (null=True → backfill → null=False, unique=True)
- [ ] `CODEBASE_REFERENCE.md` section 1.1 mise à jour

---

### Étape 1.3 — Modèles de liaison : `LienEnseignantEleve` et `LienParentEleve`

**Ajout** : `users/models.py`

```python
class StatutLienChoices(models.TextChoices):
    EN_ATTENTE = "en_attente", "En attente"
    VALIDE = "valide", "Validé"
    REFUSE = "refuse", "Refusé"


class LienEnseignantEleve(models.Model):
    """Liaison entre un enseignant et un élève, avec validation."""
    enseignant = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="liens_eleves",
        limit_choices_to={"role": RoleChoices.ENSEIGNANT},
        verbose_name="Enseignant",
    )
    eleve = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="liens_enseignants",
        limit_choices_to={"role": RoleChoices.ELEVE},
        verbose_name="Élève",
    )
    statut = models.CharField(
        max_length=15,
        choices=StatutLienChoices.choices,
        default=StatutLienChoices.EN_ATTENTE,
        db_index=True,
        verbose_name="Statut",
    )
    cree_le = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    mis_a_jour_le = models.DateTimeField(auto_now=True, verbose_name="Mis à jour le")

    class Meta:
        verbose_name = "Lien enseignant-élève"
        verbose_name_plural = "Liens enseignant-élève"
        unique_together = [("enseignant", "eleve")]
        indexes = [
            models.Index(fields=["eleve", "statut"], name="idx_lien_ens_eleve_statut"),
        ]

    def __str__(self):
        return f"{self.enseignant.nom_complet} → {self.eleve.nom_complet} ({self.statut})"


class LienParentEleve(models.Model):
    """Liaison entre un parent et un élève, avec validation."""
    parent = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="liens_enfants",
        limit_choices_to={"role": RoleChoices.PARENT},
        verbose_name="Parent",
    )
    eleve = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="liens_parents",
        limit_choices_to={"role": RoleChoices.ELEVE},
        verbose_name="Élève",
    )
    statut = models.CharField(
        max_length=15,
        choices=StatutLienChoices.choices,
        default=StatutLienChoices.EN_ATTENTE,
        db_index=True,
        verbose_name="Statut",
    )
    cree_le = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    mis_a_jour_le = models.DateTimeField(auto_now=True, verbose_name="Mis à jour le")

    class Meta:
        verbose_name = "Lien parent-élève"
        verbose_name_plural = "Liens parent-élève"
        unique_together = [("parent", "eleve")]
        indexes = [
            models.Index(fields=["eleve", "statut"], name="idx_lien_par_eleve_statut"),
        ]

    def __str__(self):
        return f"{self.parent.nom_complet} → {self.eleve.nom_complet} ({self.statut})"
```

> **Règle métier** : un élève peut avoir **1 seul enseignant validé** et **max 2 parents validés**. Le `unique_together` sur `(enseignant, eleve)` et `(parent, eleve)` empêche les doublons de paires. La limite « 1 enseignant validé » et « 2 parents validés » est vérifiée côté applicatif dans `clean()` et dans les services (Phase 2).

#### 🎯 Critères d'acceptation

- `LienEnseignantEleve` et `LienParentEleve` sont créés avec `statut` par défaut `en_attente`
- `unique_together` empêche la création de deux liens entre le même enseignant/parent et le même élève
- `limit_choices_to` restreint les FK au bon rôle (protection admin Django)
- Un élève ne peut avoir qu'un seul `LienEnseignantEleve` avec `statut="valide"` — vérifié par `clean()` sur le modèle
- Un élève ne peut avoir que 2 `LienParentEleve` avec `statut="valide"` — vérifié par `clean()` sur le modèle
- Les indexes composites `(eleve, statut)` existent pour optimiser les requêtes fréquentes

#### 🏗 Architecture

- `StatutLienChoices` est partagé entre les deux modèles de lien pour éviter la duplication
- `limit_choices_to` protège uniquement l'interface admin Django — la vérification du rôle doit aussi être faite dans les vues/services (Phase 2)
- Index composite `(eleve, statut)` car la requête la plus fréquente sera : « quels liens validés pour cet élève ? » (dashboards, vérifications d'accès)
- `clean()` lèvera `ValidationError` si les contraintes de nombre sont violées. Les services appelleront `full_clean()` avant `save()` dans un `transaction.atomic()`

#### 🔒 Sécurité

- `limit_choices_to` empêche la création de liens incohérents via l'admin Django
- Les vérifications de rôle devront être dupliquées dans les vues (Phase 2) — l'admin n'est pas le seul point d'entrée
- IDOR : les vues (Phase 2+) vérifieront que l'utilisateur courant est bien une partie du lien

#### ⚡ Performance

- `db_index=True` sur `statut` des deux modèles
- Index composite `(eleve, statut)` pour les lookups fréquents
- `select_related("enseignant", "eleve")` et `select_related("parent", "eleve")` dans les vues (Phase 2+)

#### ✅ Definition of Done

- [ ] `StatutLienChoices` créé avec 3 valeurs
- [ ] `LienEnseignantEleve` créé avec FK, statut, unique_together, index composite
- [ ] `LienParentEleve` créé avec FK, statut, unique_together, index composite
- [ ] `clean()` implémenté sur les deux modèles pour les limites de nombre
- [ ] `CODEBASE_REFERENCE.md` sections 1.x mises à jour pour les nouveaux modèles

---

### Étape 1.4 — Modèle `Notification`

**Ajout** : `users/models.py`

```python
class TypeNotificationChoices(models.TextChoices):
    DEMANDE_LIAISON = "demande_liaison", "Demande de liaison"
    LIAISON_VALIDEE = "liaison_validee", "Liaison validée"
    LIAISON_REFUSEE = "liaison_refusee", "Liaison refusée"
    NOUVEAU_MESSAGE = "nouveau_message", "Nouveau message"
    SYSTEME = "systeme", "Notification système"


class Notification(models.Model):
    """Notification envoyée à un utilisateur (liaison, message, système)."""
    destinataire = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name="Destinataire",
    )
    type = models.CharField(
        max_length=20,
        choices=TypeNotificationChoices.choices,
        verbose_name="Type",
    )
    titre = models.CharField(max_length=255, verbose_name="Titre")
    contenu = models.TextField(blank=True, verbose_name="Contenu")
    lue = models.BooleanField(default=False, db_index=True, verbose_name="Lue")
    lien = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Lien associé",
    )
    cree_le = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ["-cree_le"]
        indexes = [
            models.Index(
                fields=["destinataire", "lue", "-cree_le"],
                name="idx_notif_dest_lue_date",
            ),
        ]

    def __str__(self):
        return f"[{self.type}] {self.titre} → {self.destinataire.nom_complet}"
```

#### 🎯 Critères d'acceptation

- `Notification` est créée avec `lue=False` par défaut
- L'ordering par défaut est `-cree_le` (plus récentes en premier)
- `TypeNotificationChoices` contient exactement 5 types : `demande_liaison`, `liaison_validee`, `liaison_refusee`, `nouveau_message`, `systeme`
- Le `lien` est optionnel (blank=True) — utilisé pour rediriger vers la page pertinente
- L'index composite `(destinataire, lue, -cree_le)` existe

#### 🏗 Architecture

- Pas de modèle `Expediteur` — on ne stocke que le destinataire. L'expéditeur est implicite (le système, l'utilisateur qui a initié l'action). Si on a besoin de l'émetteur dans le futur, on ajoutera un champ `FK → CustomUser` nullable
- `TypeNotificationChoices` est un enum séparé pour faciliter le dispatch côté template (icône, couleur par type)
- `lien` est un `CharField(500)` et non un `URLField` car il stockera des chemins relatifs Django (`/cours/matieres/`, `/utilisateurs/liaisons/`) et non des URLs absolues

#### 🔒 Sécurité

- `contenu` sera nettoyé avec `strip_tags()` avant insertion dans les services (Phase 2+) — pas de HTML dans les notifications
- `lien` ne doit contenir que des URLs relatives internes — les services valideront avec `django.urls.resolve()` ou un préfixe `/`
- Pas d'injection possible via `titre` car rendu échappé dans les templates (comportement Django par défaut)

#### ⚡ Performance

- `db_index=True` sur `lue` — filtre le plus fréquent (badges non lus)
- Index composite `(destinataire, lue, -cree_le)` pour la requête principale : « notifications non lues de cet utilisateur, triées par date »
- Cache `notif_count_{user_id}` prévu en Phase 3 (vues) pour éviter le `COUNT(*)` à chaque page

#### ✅ Definition of Done

- [ ] Modèle `Notification` créé avec tous les champs
- [ ] `TypeNotificationChoices` créé avec 5 types
- [ ] Index composite `(destinataire, lue, -cree_le)` ajouté
- [ ] Ordering par défaut `-cree_le` configuré
- [ ] `CODEBASE_REFERENCE.md` mis à jour avec le nouveau modèle

---

### Étape 1.5 — Modèles de messagerie : `Conversation` et `Message`

**Ajout** : `users/models.py`

```python
class Conversation(models.Model):
    """Conversation entre deux ou plusieurs utilisateurs."""
    participants = models.ManyToManyField(
        CustomUser,
        related_name="conversations",
        verbose_name="Participants",
    )
    cree_le = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    mis_a_jour_le = models.DateTimeField(auto_now=True, verbose_name="Mis à jour le")

    class Meta:
        verbose_name = "Conversation"
        verbose_name_plural = "Conversations"
        ordering = ["-mis_a_jour_le"]

    def __str__(self):
        noms = ", ".join(p.nom_complet for p in self.participants.all()[:3])
        return f"Conversation: {noms}"


class Message(models.Model):
    """Message dans une conversation."""
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="Conversation",
    )
    auteur = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="messages_envoyes",
        verbose_name="Auteur",
    )
    contenu = models.TextField(
        max_length=2000,
        verbose_name="Contenu",
    )
    envoye_le = models.DateTimeField(auto_now_add=True, verbose_name="Envoyé le")
    lu = models.BooleanField(default=False, verbose_name="Lu")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["envoye_le"]
        indexes = [
            models.Index(
                fields=["conversation", "-envoye_le"],
                name="idx_msg_conv_date",
            ),
            models.Index(
                fields=["conversation", "lu"],
                name="idx_msg_conv_lu",
            ),
        ]

    def __str__(self):
        return f"{self.auteur.nom_complet}: {self.contenu[:50]}"
```

> **Choix M2M pour participants** : Une conversation est entre N participants (typiquement 2, mais extensible à un groupe parent+enseignant). Le M2M est géré par Django sans table intermédiaire explicite — suffisant pour le volume attendu.

#### 🎯 Critères d'acceptation

- `Conversation` stocke les participants via M2M
- `Conversation` est ordonnée par `-mis_a_jour_le` (dernière activité en premier)
- `Message.contenu` a une limite de 2000 caractères (`max_length=2000`)
- `Message` est ordonné par `envoye_le` (chronologique)
- `Message.lu` est `False` par défaut
- L'envoi d'un message met à jour `Conversation.mis_a_jour_le` (via `auto_now` au `save()` de la conversation dans le service)
- Les indexes composites `(conversation, -envoye_le)` et `(conversation, lu)` existent

#### 🏗 Architecture

- `Conversation` ne contient pas le contenu du dernier message — il sera récupéré par `messages.order_by("-envoye_le").first()` avec `select_related("auteur")`
- `Message.lu` est un booléen simple (pas de tracking par participant). Suffisant pour les conversations 1:1 du MVP. Si on passe à N participants, il faudrait une table `MessageLu(message, user, lu_le)` — migration prévue en Phase 5+ si nécessaire
- Le `max_length=2000` sur `TextField` est une validation Django, pas une contrainte DB (PostgreSQL `TEXT` n'a pas de limite native). La validation se fera dans le formulaire et dans `clean()`
- La mise à jour de `Conversation.mis_a_jour_le` lors de l'envoi d'un message sera faite explicitement dans le service (`conversation.save()`) — pas par un signal

#### 🔒 Sécurité

- `contenu` sera nettoyé avec `strip_tags()` dans le service d'envoi (Phase 5) — pas de HTML dans les messages
- Les vues (Phase 5) vérifieront que l'auteur est bien un participant de la conversation
- Pas de pièces jointes dans le MVP — réduit la surface d'attaque (pas de risque de téléchargement malveillant)

#### ⚡ Performance

- Index composite `(conversation, -envoye_le)` pour paginer les messages d'une conversation
- Index composite `(conversation, lu)` pour compter les messages non lus
- `prefetch_related("messages__auteur")` pour l'inbox (listing des conversations avec dernier message)
- Cache `msg_count_{user_id}` prévu en Phase 5 pour le badge de messages non lus
- Pagination : 50 messages par page dans les conversations (défini dans les standards transversaux)

#### ✅ Definition of Done

- [ ] `Conversation` créé avec M2M participants, ordering `-mis_a_jour_le`
- [ ] `Message` créé avec FK conversation, auteur, contenu max 2000, lu, envoye_le
- [ ] Index composites ajoutés (2 indexes sur `Message`)
- [ ] `CODEBASE_REFERENCE.md` mis à jour avec les deux nouveaux modèles

---

### Étape 1.6 — Migrations

**Stratégie de migration** : le champ `code_identifiant` sur `CustomUser` est `unique=True` et doit être ajouté à une table existante potentiellement peuplée. On suit la convention de migration en 3 étapes :

1. **Migration 1** (`XXXX_add_roles_code_identifiant.py`) :
   - Ajouter `enseignant` et `parent` aux choices de `role` (pas de changement de colonne DB, juste les choices)
   - Ajouter `code_identifiant` en `CharField(max_length=8, null=True, blank=True)` — pas encore unique, pas d'index
   - Créer `LienEnseignantEleve`, `LienParentEleve`, `Notification`, `Conversation`, `Message`

2. **Migration 2** (`XXXX_backfill_code_identifiant.py` — data migration) :
   - `RunPython` qui génère un `code_identifiant` pour chaque utilisateur existant
   - `reverse_code` : `RunPython.noop` (les codes ne sont pas utilisés ailleurs à ce stade, perte acceptable)
   - Utilise `bulk_update()` par batch de 500

3. **Migration 3** (`XXXX_code_identifiant_unique.py`) :
   - `AlterField` → `null=False, blank=True, unique=True, db_index=True`

```python
# Migration 2 — backfill (pseudo-code)
import secrets
from django.db import migrations

PREFIXES = {"admin": "ADM", "eleve": "ELV", "enseignant": "ENS", "parent": "PAR"}

def backfill_code_identifiant(apps, schema_editor):
    CustomUser = apps.get_model("users", "CustomUser")
    codes_existants = set()
    users_a_maj = []

    for user in CustomUser.objects.filter(code_identifiant__isnull=True).iterator():
        prefixe = PREFIXES.get(user.role, "ELV")
        for _ in range(5):
            code = prefixe + secrets.token_hex(3)[:5].upper()
            if code not in codes_existants:
                user.code_identifiant = code
                codes_existants.add(code)
                users_a_maj.append(user)
                break

    CustomUser.objects.bulk_update(users_a_maj, ["code_identifiant"], batch_size=500)


class Migration(migrations.Migration):
    dependencies = [("users", "XXXX_add_roles_code_identifiant")]
    operations = [
        migrations.RunPython(
            backfill_code_identifiant,
            reverse_code=migrations.RunPython.noop,  # Acceptable : codes non utilisés encore
        ),
    ]
```

#### 🎯 Critères d'acceptation

- Les 3 migrations s'exécutent sans erreur sur une base avec des utilisateurs existants
- Après migration, chaque utilisateur a un `code_identifiant` non-null, unique, de 8 caractères
- Les migrations sont réversibles (au minimum `noop` pour la data migration)
- Les nouveaux modèles (`LienEnseignantEleve`, `LienParentEleve`, `Notification`, `Conversation`, `Message`) sont créés avec tous les indexes et contraintes
- `python manage.py migrate` + `python manage.py migrate users zero` fonctionne sans erreur

#### ✅ Definition of Done

- [ ] 3 migrations créées et nommées conformément aux conventions
- [ ] `migrate` s'exécute sans erreur sur une base vide et une base peuplée
- [ ] Rollback testé (`migrate users <migration_précédente>`)
- [ ] Aucune migration existante modifiée

---

### 🧪 Tests — Phase 1

> **Agent responsable** : `test-writer`
> **Fichier** : `users/tests.py` (fichier existant, à compléter — la migration vers `tests/` se fera en Phase 2)
> **Nombre minimum** : 12 tests

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_creation_user_eleve_code_identifiant_prefixe_ELV` | `CustomUser.objects.create_user(email="e@t.com", prenom="A", nom="B", role="eleve", password="test1234")` | `assertEqual(user.code_identifiant[:3], "ELV")` |
| 2 | `test_creation_user_enseignant_code_identifiant_prefixe_ENS` | idem avec `role="enseignant"` | `assertEqual(user.code_identifiant[:3], "ENS")` |
| 3 | `test_creation_user_parent_code_identifiant_prefixe_PAR` | idem avec `role="parent"` | `assertEqual(user.code_identifiant[:3], "PAR")` |
| 4 | `test_creation_user_admin_code_identifiant_prefixe_ADM` | idem avec `role="admin"` | `assertEqual(user.code_identifiant[:3], "ADM")` |
| 5 | `test_code_identifiant_unique_entre_utilisateurs` | 2 users créés | `assertNotEqual(user1.code_identifiant, user2.code_identifiant)` |
| 6 | `test_code_identifiant_collision_retry_genere_nouveau_code` | Mock `secrets.token_hex` pour retourner un code existant les 4 premières fois, puis un unique | `assertEqual(user.code_identifiant[:3], "ELV")` + pas de `RuntimeError` |
| 7 | `test_lien_enseignant_eleve_unique_together` | Créer un lien, tenter de créer le même | `assertRaises(IntegrityError)` |
| 8 | `test_lien_parent_eleve_unique_together` | Créer un lien, tenter de créer le même | `assertRaises(IntegrityError)` |
| 9 | `test_max_2_parents_valides_par_eleve` | Créer 2 liens parent validés, tenter un 3e `full_clean()` | `assertRaises(ValidationError)` |
| 10 | `test_notification_ordering_par_cree_le_desc` | 3 notifications créées à des dates différentes | `assertEqual(notifs[0].cree_le, plus_recente)` |
| 11 | `test_message_contenu_max_2000_caracteres` | Message avec 2001 caractères → `full_clean()` | `assertRaises(ValidationError)` |
| 12 | `test_statut_lien_defaut_en_attente` | `LienEnseignantEleve.objects.create(enseignant=ens, eleve=elv)` | `assertEqual(lien.statut, "en_attente")` |

**Tests complémentaires recommandés** (bonus, non bloquants) :

| # | Nom du test | Assertion clé |
|---|-------------|---------------|
| 13 | `test_code_identifiant_longueur_8` | `assertEqual(len(user.code_identifiant), 8)` |
| 14 | `test_code_identifiant_non_modifie_au_second_save` | `user.save()` deux fois → code identique |
| 15 | `test_is_enseignant_property` | `assertTrue(user.is_enseignant)` pour `role="enseignant"` |
| 16 | `test_is_parent_property` | `assertTrue(user.is_parent)` pour `role="parent"` |
| 17 | `test_max_1_enseignant_valide_par_eleve` | 1 lien enseignant validé + 2e avec autre enseignant → `ValidationError` |
| 18 | `test_conversation_ordering_par_mis_a_jour_le_desc` | 2 conversations → la plus récemment modifiée est en premier |

---

### Résumé des changements par fichier — Phase 1

| Fichier | Action |
|---------|--------|
| `users/models.py` | Étendre `RoleChoices`, ajouter `code_identifiant` + `save()` override, ajouter `is_enseignant`/`is_parent`, créer `StatutLienChoices`, `LienEnseignantEleve`, `LienParentEleve`, `TypeNotificationChoices`, `Notification`, `Conversation`, `Message` |
| `users/migrations/` | 3 nouvelles migrations (ajout champs + backfill + unique constraint) |
| `users/admin.py` | Enregistrer les nouveaux modèles dans l'admin Django |
| `users/tests.py` | 12+ tests unitaires (délégué à `test-writer`) |
| `CODEBASE_REFERENCE.md` | Sections 1.1, 1.3 mises à jour + nouvelles sections pour les 5 modèles |

### Ordre d'exécution recommandé

```
1. Implementer  → Étapes 1.1 à 1.5 (modèles dans users/models.py + admin.py)
2. Migration Writer → Étape 1.6 (3 migrations)
3. Test Writer  → 12+ tests dans users/tests.py
4. Implementer  → Mise à jour CODEBASE_REFERENCE.md
```

---

## Phase 2 — Inscription et validation multi-rôles

> **Objectif** : remplacer le formulaire d'inscription unique (`InscriptionView` + `InscriptionForm`) par un système en 2 étapes : choix du rôle → formulaire spécialisé par rôle. Chaque rôle a sa propre logique de création de compte, de liaison optionnelle (code enseignant / code élève), et de vérification email. Aucune modification des modèles dans cette phase — on utilise les modèles créés en Phase 1.

### Décisions d'architecture (Phase 2)

| Décision | Justification |
|----------|---------------|
| 3 formulaires séparés plutôt qu'un formulaire dynamique | Chaque rôle a des champs et des validations différents (niveau obligatoire pour élève, code optionnel pour élève, code obligatoire pour parent, aucun code pour enseignant). Un formulaire unique avec logique conditionnelle serait fragile et difficile à tester |
| Validation du code dans `clean_code_*()` du formulaire | La validation du code (existence, préfixe, utilisateur actif) est une règle métier du formulaire, pas de la vue. Cela permet de réutiliser la validation si le formulaire est utilisé ailleurs (ex: admin) |
| Helpers `_creer_lien_enseignant()` et `_creer_lien_parent()` dans `users/helpers.py` | Extraits car réutilisés en Phase 3 (validation de liens). Les helpers sont des fonctions pures recevant des objets Django — pas d'accès à `request` |
| `transaction.atomic()` dans chaque vue POST | Création compte + lien + notification sont atomiques. Si l'email de vérification échoue, on laisse le compte créé (l'email peut être renvoyé) mais le lien doit être cohérent |
| Ancien URL `/inscription/` redirige vers `choix_role` | Backward compatibility pour les liens existants (emails, bookmarks). Redirect 301 permanent |
| Migration du dossier `tests/` dès cette phase | Conformément aux standards transversaux : `users/tests/` avec `conftest.py` + fichiers par domaine |

---

### Étape 2.1 — Formulaires d'inscription multi-rôles

**Fichiers** : `users/forms.py`

#### `InscriptionEleveForm`

```python
class InscriptionEleveForm(forms.ModelForm):
    """Formulaire d'inscription pour les élèves."""
    password1 = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")
    code_enseignant = forms.CharField(
        max_length=8,
        required=False,
        label="Code enseignant (optionnel)",
        help_text="Si un enseignant vous a donné un code, saisissez-le ici.",
    )

    class Meta:
        model = CustomUser
        fields = ["prenom", "nom", "email", "niveau"]

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Un compte avec cet email existe déjà.")
        return email

    def clean_code_enseignant(self):
        code = self.cleaned_data.get("code_enseignant", "").strip().upper()
        if not code:
            return ""
        if not code.startswith("ENS"):
            raise ValidationError("Code invalide ou inactif.")
        if not CustomUser.objects.filter(
            code_identifiant=code, role=RoleChoices.ENSEIGNANT, is_active=True
        ).exists():
            raise ValidationError("Code invalide ou inactif.")
        return code

    def clean_niveau(self):
        niveau = self.cleaned_data.get("niveau")
        if not niveau:
            raise ValidationError("Le niveau est obligatoire pour un élève.")
        return niveau

    def clean(self):
        # Validation mot de passe : identiques, ≥8 chars, 1 majuscule, 1 chiffre
        ...

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.role = RoleChoices.ELEVE
        user.is_active = False
        if commit:
            user.save()
        return user
```

#### `InscriptionEnseignantForm`

```python
class InscriptionEnseignantForm(forms.ModelForm):
    """Formulaire d'inscription pour les enseignants."""
    password1 = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")

    class Meta:
        model = CustomUser
        fields = ["prenom", "nom", "email"]
        # Pas de champ niveau — null pour les enseignants

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Un compte avec cet email existe déjà.")
        return email

    def clean(self):
        # Validation mot de passe : identiques, ≥8 chars, 1 majuscule, 1 chiffre
        ...

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.role = RoleChoices.ENSEIGNANT
        user.is_active = False
        user.niveau = None
        if commit:
            user.save()
        return user
```

#### `InscriptionParentForm`

```python
class InscriptionParentForm(forms.ModelForm):
    """Formulaire d'inscription pour les parents."""
    password1 = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")
    code_eleve = forms.CharField(
        max_length=8,
        required=True,
        label="Code élève",
        help_text="Le code d'identification de votre enfant (commence par ELV).",
    )

    class Meta:
        model = CustomUser
        fields = ["prenom", "nom", "email"]
        # Pas de champ niveau — null pour les parents

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Un compte avec cet email existe déjà.")
        return email

    def clean_code_eleve(self):
        code = self.cleaned_data.get("code_eleve", "").strip().upper()
        if not code:
            raise ValidationError("Le code élève est obligatoire.")
        if not code.startswith("ELV"):
            raise ValidationError("Code invalide ou inactif.")
        if not CustomUser.objects.filter(
            code_identifiant=code, role=RoleChoices.ELEVE, is_active=True
        ).exists():
            raise ValidationError("Code invalide ou inactif.")
        return code

    def clean(self):
        # Validation mot de passe : identiques, ≥8 chars, 1 majuscule, 1 chiffre
        ...

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.role = RoleChoices.PARENT
        user.is_active = False
        user.niveau = None
        if commit:
            user.save()
        return user
```

> **Message d'erreur anti-énumération** : `"Code invalide ou inactif."` est le message unique retourné que le code n'existe pas, que le préfixe soit mauvais, ou que l'utilisateur lié ne soit pas actif. Cela empêche un attaquant de distinguer ces cas.

> **Widgets Tailwind** : les 3 formulaires utilisent les mêmes classes widget que `InscriptionForm` existant : `w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent`.

#### 🎯 Critères d'acceptation

- `InscriptionEleveForm` a les champs : `prenom`, `nom`, `email`, `niveau`, `password1`, `password2`, `code_enseignant` (optionnel)
- `InscriptionEnseignantForm` a les champs : `prenom`, `nom`, `email`, `password1`, `password2` — pas de `niveau`
- `InscriptionParentForm` a les champs : `prenom`, `nom`, `email`, `password1`, `password2`, `code_eleve` (obligatoire)
- `clean_email()` normalise en `strip().lower()` et vérifie l'unicité sur les 3 formulaires
- `clean_code_enseignant()` : code vide → OK (optionnel) ; code ne commençant pas par `ENS` → `"Code invalide ou inactif."` ; code inexistant ou enseignant inactif → `"Code invalide ou inactif."`
- `clean_code_eleve()` : code vide → `"Le code élève est obligatoire."` ; code ne commençant pas par `ELV` → `"Code invalide ou inactif."` ; code inexistant ou élève inactif → `"Code invalide ou inactif."`
- `save()` de chaque formulaire met `is_active=False` et le bon `role`
- `save()` de `InscriptionEnseignantForm` et `InscriptionParentForm` met `niveau=None`
- Validation mot de passe identique à l'existant : ≥8 chars, 1 majuscule, 1 chiffre

#### 🏗 Architecture

- Les 3 `clean_email()` partagent la même logique — DRY via un mixin `_CleanEmailMixin` ou duplication acceptée (3 lignes, le coût d'un mixin serait supérieur au gain)
- `clean_code_enseignant()` et `clean_code_eleve()` sont dans le formulaire (pas dans la vue) : Single Responsibility — la vue orchestre, le formulaire valide
- `save(commit=True)` suit le pattern Django standard : `super().save(commit=False)` → configure les champs → `save()` si commit

#### 🔒 Sécurité

- **Enumération** : message unique `"Code invalide ou inactif."` pour toute erreur de code (préfixe, existence, activité)
- **Input sanitization** : `strip()` + `lower()` sur email, `strip()` + `upper()` sur codes dans les méthodes `clean_*()` — jamais de données non nettoyées
- **CSRF** : protégé par défaut (formulaire Django standard)
- **Password strength** : mêmes règles que `InscriptionForm` existant (≥8 chars, 1 majuscule, 1 chiffre)

#### ⚡ Performance

- Lookup `code_identifiant` : une seule requête `filter(code_identifiant=code, role=..., is_active=True).exists()` — O(1) via l'index unique `code_identifiant`
- Lookup email : `filter(email=email).exists()` — O(1) via l'index unique `email`
- Aucune requête N+1

#### ✅ Definition of Done

- [ ] `InscriptionEleveForm` créé avec `code_enseignant` optionnel + validation
- [ ] `InscriptionEnseignantForm` créé sans `niveau` ni code
- [ ] `InscriptionParentForm` créé avec `code_eleve` obligatoire + validation
- [ ] Widgets Tailwind cohérents avec les formulaires existants
- [ ] `CODEBASE_REFERENCE.md` section 4 (Forms) mise à jour

---

### Étape 2.2 — Helpers et vues d'inscription multi-rôles

**Fichiers** : `users/helpers.py` (nouveau), `users/views.py`

#### Helpers — `users/helpers.py`

```python
from users.models import CustomUser, LienEnseignantEleve, LienParentEleve, Notification
from users.models import StatutLienChoices, TypeNotificationChoices, RoleChoices


def _creer_lien_enseignant(eleve, code_enseignant):
    """Crée un LienEnseignantEleve en_attente et notifie l'enseignant."""
    enseignant = CustomUser.objects.get(
        code_identifiant=code_enseignant,
        role=RoleChoices.ENSEIGNANT,
        is_active=True,
    )
    lien = LienEnseignantEleve.objects.create(
        enseignant=enseignant,
        eleve=eleve,
        statut=StatutLienChoices.EN_ATTENTE,
    )
    Notification.objects.create(
        destinataire=enseignant,
        type=TypeNotificationChoices.DEMANDE_LIAISON,
        titre="Nouvelle demande de liaison élève",
        contenu=f"{eleve.nom_complet} souhaite rejoindre votre classe.",
        lien="/liaisons/",  # URL Phase 3
    )
    return lien


def _creer_lien_parent(parent, code_eleve):
    """Crée un LienParentEleve en_attente et notifie l'élève."""
    eleve = CustomUser.objects.get(
        code_identifiant=code_eleve,
        role=RoleChoices.ELEVE,
        is_active=True,
    )
    lien = LienParentEleve.objects.create(
        parent=parent,
        eleve=eleve,
        statut=StatutLienChoices.EN_ATTENTE,
    )
    Notification.objects.create(
        destinataire=eleve,
        type=TypeNotificationChoices.DEMANDE_LIAISON,
        titre="Demande de liaison parentale",
        contenu=f"{parent.nom_complet} souhaite se lier à votre compte en tant que parent.",
        lien="/liaisons/",  # URL Phase 3
    )
    return lien
```

> **Pourquoi `helpers.py` et pas `services.py`** : ces fonctions ne prennent pas `request` en paramètre — ce sont des fonctions pures recevant des objets Django. Elles seront appelées depuis les vues (qui gèrent `request` et `transaction.atomic()`). Si on ajoute des effets de bord liés à `request` (ex: logging IP), on les déplacera dans `services.py`.

#### Vues — `users/views.py`

```python
from django.db import transaction
from django.shortcuts import render, redirect
from django.core.cache import cache
from users.helpers import _creer_lien_enseignant, _creer_lien_parent


def choix_role_view(request):
    """Page de choix du rôle avant inscription."""
    if request.user.is_authenticated:
        return redirect("tableau_de_bord")
    return render(request, "registration/choix_role.html")


def inscription_eleve_view(request):
    """Inscription d'un élève (avec code enseignant optionnel)."""
    if request.user.is_authenticated:
        return redirect("tableau_de_bord")

    if request.method == "POST":
        form = InscriptionEleveForm(request.POST)
        if form.is_valid():
            code_enseignant = form.cleaned_data.get("code_enseignant", "")

            # Rate limit sur POST avec code (5 tentatives/h/IP)
            if code_enseignant:
                ip = _get_client_ip(request)
                cache_key = f"inscription_code_{ip}"
                attempts = cache.get(cache_key, 0)
                if attempts >= 5:
                    return render(request, "registration/register_eleve.html", {
                        "form": form,
                        "error_rate_limit": "Trop de tentatives. Réessayez dans une heure.",
                    }, status=429)
                cache.set(cache_key, attempts + 1, timeout=3600)

            with transaction.atomic():
                user = form.save()
                _debloquer_premiers_chapitres(user)
                if code_enseignant:
                    _creer_lien_enseignant(user, code_enseignant)

            _envoyer_email_verification(request, user)
            return redirect("inscription_confirmation")
    else:
        form = InscriptionEleveForm()

    return render(request, "registration/register_eleve.html", {"form": form})


def inscription_enseignant_view(request):
    """Inscription d'un enseignant."""
    if request.user.is_authenticated:
        return redirect("tableau_de_bord")

    if request.method == "POST":
        form = InscriptionEnseignantForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()

            _envoyer_email_verification(request, user)
            return redirect("inscription_confirmation")
    else:
        form = InscriptionEnseignantForm()

    return render(request, "registration/register_enseignant.html", {"form": form})


def inscription_parent_view(request):
    """Inscription d'un parent (code élève obligatoire)."""
    if request.user.is_authenticated:
        return redirect("tableau_de_bord")

    if request.method == "POST":
        form = InscriptionParentForm(request.POST)
        if form.is_valid():
            code_eleve = form.cleaned_data["code_eleve"]

            # Rate limit sur POST avec code (5 tentatives/h/IP)
            ip = _get_client_ip(request)
            cache_key = f"inscription_code_{ip}"
            attempts = cache.get(cache_key, 0)
            if attempts >= 5:
                return render(request, "registration/register_parent.html", {
                    "form": form,
                    "error_rate_limit": "Trop de tentatives. Réessayez dans une heure.",
                }, status=429)
            cache.set(cache_key, attempts + 1, timeout=3600)

            with transaction.atomic():
                user = form.save()
                _creer_lien_parent(user, code_eleve)

            _envoyer_email_verification(request, user)
            return redirect("inscription_confirmation")
    else:
        form = InscriptionParentForm()

    return render(request, "registration/register_parent.html", {"form": form})


def _get_client_ip(request):
    """Extrait l'IP du client depuis les headers (derrière reverse proxy)."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")
```

> **`_debloquer_premiers_chapitres(user)`** : helper existant dans `users/views.py`, déjà appelé dans `InscriptionView`. Réutilisé tel quel pour les élèves.
>
> **`_envoyer_email_verification(request, user)`** : helper existant dans `users/views.py`. Réutilisé pour les 3 rôles.
>
> **`_get_client_ip(request)`** : nouveau helper privé dans `users/views.py` pour extraire l'IP client derrière le reverse proxy Nginx. Utilisé pour le rate limiting par IP.
>
> **Rate limiting** : 5 tentatives/h/IP uniquement sur les POST avec code (élève avec code enseignant, parent avec code élève). Clé cache partagée `inscription_code_{ip}` — un attaquant qui essaie des codes enseignant et des codes élève consomme le même quota. Timeout 3600 secondes (1h).

#### 🎯 Critères d'acceptation

- `GET /inscription/choix/` → 200, affiche la page de choix du rôle
- `GET /inscription/choix/` pour un utilisateur authentifié → redirect vers `tableau_de_bord`
- `GET /inscription/eleve/` → 200, affiche le formulaire élève
- `POST /inscription/eleve/` avec données valides sans code → crée un `CustomUser(role="eleve", is_active=False)` + redirige vers `inscription_confirmation`
- `POST /inscription/eleve/` avec `code_enseignant="ENS-MC01"` valide → crée un `LienEnseignantEleve(statut="en_attente")` + crée une `Notification(type="demande_liaison")` pour l'enseignant
- `POST /inscription/eleve/` avec `code_enseignant="XXX12345"` → retourne le formulaire avec erreur `"Code invalide ou inactif."` sur le champ `code_enseignant`
- `POST /inscription/eleve/` avec `code_enseignant="ELV12345"` (mauvais préfixe) → retourne le formulaire avec erreur `"Code invalide ou inactif."` sur le champ `code_enseignant`
- `POST /inscription/eleve/` avec email dupliqué → retourne le formulaire avec erreur `"Un compte avec cet email existe déjà."` sur le champ `email`
- `POST /inscription/eleve/` → le compte créé a `is_active=False`
- `POST /inscription/eleve/` → les premiers chapitres sont débloqués via `_debloquer_premiers_chapitres()`
- `GET /inscription/enseignant/` → 200, affiche le formulaire enseignant
- `POST /inscription/enseignant/` avec données valides → crée un `CustomUser(role="enseignant", is_active=False, niveau=None)` + redirige vers `inscription_confirmation`
- `GET /inscription/parent/` → 200, affiche le formulaire parent
- `POST /inscription/parent/` sans `code_eleve` → retourne le formulaire avec erreur `"Le code élève est obligatoire."` sur le champ `code_eleve`
- `POST /inscription/parent/` avec `code_eleve` valide → crée un `CustomUser(role="parent", is_active=False)` + `LienParentEleve(statut="en_attente")` + `Notification(type="demande_liaison")` pour l'élève + redirige vers `inscription_confirmation`
- `POST /inscription/parent/` avec code d'un élève inactif (`is_active=False`) → retourne le formulaire avec erreur `"Code invalide ou inactif."` sur le champ `code_eleve`
- Après inscription réussie pour les 3 rôles → redirect vers `inscription_confirmation`
- Email de vérification envoyé pour les 3 rôles via `_envoyer_email_verification()`
- Rate limit : 6e POST avec code en < 1h depuis la même IP → HTTP 429 + message `"Trop de tentatives. Réessayez dans une heure."`

#### 🏗 Architecture

- `transaction.atomic()` dans chaque vue POST : création compte + lien + notification sont atomiques. Si l'email de vérification échoue après le bloc atomique, le compte existe mais n'est pas activé — l'utilisateur peut demander un renvoi (Phase future)
- `_creer_lien_enseignant()` et `_creer_lien_parent()` dans `users/helpers.py` : fonctions pures, réutilisées en Phase 3 (gestion des liaisons)
- `_debloquer_premiers_chapitres(user)` : helper existant réutilisé — uniquement pour les élèves
- `_envoyer_email_verification(request, user)` : helper existant réutilisé — pour les 3 rôles
- Rate limit par IP avec `django.core.cache` — même pattern que `_check_quiz_rate_limit()` dans `progress/views.py`, mais avec une clé et un seuil différents
- Ancien `InscriptionView` conservé temporairement avec redirect 301 vers `choix_role` (backward compat)

#### 🔒 Sécurité

- **Enumeration** : `"Code invalide ou inactif."` — message unique pour code inexistant, mauvais préfixe, ou utilisateur inactif
- **Rate limit** : 5 tentatives/h/IP sur POST avec code — empêche le brute-force sur les codes d'identification (16^5 ≈ 1M combinaisons par préfixe, mais le rate limit bloque bien avant)
- **Input sanitization** : `strip()` + `lower()` sur email, `strip()` + `upper()` sur codes — effectué dans les méthodes `clean_*()` du formulaire
- **Token email** : signé avec `signing.dumps()`, expire 24h — existant, réutilisé
- **CSRF** : protégé par défaut (Django middleware + `{% csrf_token %}` dans les templates)
- **`transaction.atomic()`** : empêche les états incohérents (compte sans lien, lien sans notification)
- **Redirect si authentifié** : les 4 vues redirigent vers `tableau_de_bord` si l'utilisateur est déjà connecté — empêche une seconde inscription

#### ⚡ Performance

- Lookup `code_identifiant` : O(1) via index unique — une seule requête `filter().exists()` dans `clean_code_*()`
- Lookup email : O(1) via index unique — une seule requête `filter(email=email).exists()` dans `clean_email()`
- `transaction.atomic()` regroupe les writes en une seule transaction — réduit les locks DB
- Pas de N+1 : une seule requête pour vérifier le code, une seule pour créer le lien, une seule pour créer la notification
- Rate limit via cache (mémoire) — aucune requête DB supplémentaire

#### ✅ Definition of Done

- [ ] `users/helpers.py` créé avec `_creer_lien_enseignant()` et `_creer_lien_parent()`
- [ ] `choix_role_view` créée — GET renvoie la page de choix
- [ ] `inscription_eleve_view` créée — GET/POST avec code optionnel + `transaction.atomic()`
- [ ] `inscription_enseignant_view` créée — GET/POST sans code + `transaction.atomic()`
- [ ] `inscription_parent_view` créée — GET/POST avec code obligatoire + `transaction.atomic()`
- [ ] Rate limit 5 tentatives/h/IP implémenté sur les POST avec code
- [ ] `_get_client_ip()` helper créé dans `users/views.py`
- [ ] `CODEBASE_REFERENCE.md` sections 3.2 (Views) et 8 (Key Patterns) mises à jour

---

### Étape 2.3 — Templates d'inscription

**Fichiers** : `templates/registration/choix_role.html`, `templates/registration/register_eleve.html`, `templates/registration/register_enseignant.html`, `templates/registration/register_parent.html`

#### `choix_role.html`

- Extends `base.html` via `{% block full_content %}` (page non authentifiée)
- 3 cartes cliquables : Élève, Enseignant, Parent
  - Chaque carte a une icône, un titre, une description courte, un lien vers le formulaire spécialisé
  - Couleurs : indigo pour élève (cohérent avec le thème existant), vert pour enseignant, orange pour parent
- Lien « Déjà un compte ? Se connecter » en bas
- Dark mode toggle (bouton flottant, comme sur `login.html` et `register.html` existants)
- Anti-flash dark mode init script (comme `login.html`)
- Meta `noindex,nofollow` (page d'inscription, pas de SEO)

#### `register_eleve.html`

- Extends `base.html` via `{% block full_content %}`
- Titre : « Inscription Élève »
- Champs : prénom, nom, email, niveau (select), mot de passe, confirmer mot de passe, code enseignant (optionnel)
- Help text sous le champ code : « Si un enseignant vous a donné un code, saisissez-le ici. »
- Affichage des erreurs de formulaire (messages en français)
- Affichage de `error_rate_limit` si présent (bandeau rouge au-dessus du formulaire)
- Bouton submit : « Créer mon compte »
- Lien retour vers `choix_role`
- Dark mode toggle + anti-flash

#### `register_enseignant.html`

- Même structure que `register_eleve.html`
- Titre : « Inscription Enseignant »
- Champs : prénom, nom, email, mot de passe, confirmer mot de passe
- Pas de champ niveau ni code
- Bouton submit : « Créer mon compte »

#### `register_parent.html`

- Même structure que `register_eleve.html`
- Titre : « Inscription Parent »
- Champs : prénom, nom, email, code élève (obligatoire), mot de passe, confirmer mot de passe
- Help text sous le champ code : « Le code d'identification de votre enfant (commence par ELV). »
- Affichage de `error_rate_limit` si présent
- Bouton submit : « Créer mon compte »

> **Règle dark mode** : les templates utilisent `{% block full_content %}` et les mêmes styles que `login.html` / `register.html`. Pas de classes `dark:` — tout est géré par les CSS overrides dans `base.html`.

#### 🎯 Critères d'acceptation

- `choix_role.html` affiche 3 cartes cliquables avec les bons liens (`inscription_eleve`, `inscription_enseignant`, `inscription_parent`)
- Chaque template de formulaire affiche les erreurs de validation par champ (messages en français)
- `error_rate_limit` s'affiche en bandeau rouge quand la variable est dans le contexte
- Les 4 templates ont le dark mode toggle fonctionnel
- Les 4 templates ont la meta `noindex,nofollow`
- Aucune classe `dark:` dans les templates enfants

#### 🏗 Architecture

- Les 4 templates étendent `base.html` via `{% block full_content %}` (convention pages non authentifiées)
- Les erreurs de formulaire sont affichées via `{{ form.field.errors }}` et `{{ form.non_field_errors }}` — pattern Django standard
- La variable `error_rate_limit` est distincte des erreurs de formulaire pour permettre un affichage différencié (bandeau vs inline)

#### 🔒 Sécurité

- `{% csrf_token %}` dans chaque formulaire
- Pas de `|safe` sur les données utilisateur — uniquement sur le contenu statique
- `noindex,nofollow` empêche l'indexation des pages d'inscription

#### ✅ Definition of Done

- [ ] `choix_role.html` créé avec 3 cartes et liens corrects
- [ ] `register_eleve.html` créé avec tous les champs + erreurs + rate limit
- [ ] `register_enseignant.html` créé avec les champs appropriés
- [ ] `register_parent.html` créé avec code élève obligatoire + erreurs + rate limit
- [ ] Dark mode toggle fonctionnel sur les 4 templates
- [ ] Aucune classe `dark:` dans les templates enfants
- [ ] `CODEBASE_REFERENCE.md` section 5.5 (registration templates) mise à jour

---

### Étape 2.4 — URLs d'inscription

**Fichier** : `users/urls.py`

```python
# Nouvelles URLs d'inscription multi-rôles
path("inscription/choix/", views.choix_role_view, name="choix_role"),
path("inscription/eleve/", views.inscription_eleve_view, name="inscription_eleve"),
path("inscription/enseignant/", views.inscription_enseignant_view, name="inscription_enseignant"),
path("inscription/parent/", views.inscription_parent_view, name="inscription_parent"),
```

**Modification de l'URL existante** :

```python
# Ancien URL — redirect permanent vers choix_role pour backward compat
path("inscription/", lambda request: redirect("choix_role", permanent=True), name="inscription"),
```

> **Backward compat** : l'URL `/inscription/` existante est conservée mais redirige en 301 vers `/inscription/choix/`. Les liens existants (emails de confirmation, bookmarks) continuent de fonctionner. Le nom `inscription` est conservé pour ne pas casser les `{% url 'inscription' %}` existants dans les templates — mais ils devront être mis à jour progressivement.

#### 🎯 Critères d'acceptation

- `GET /inscription/choix/` → 200 (page de choix du rôle)
- `GET /inscription/eleve/` → 200 (formulaire élève)
- `GET /inscription/enseignant/` → 200 (formulaire enseignant)
- `GET /inscription/parent/` → 200 (formulaire parent)
- `GET /inscription/` → 301 redirect vers `/inscription/choix/`
- Les noms d'URL `choix_role`, `inscription_eleve`, `inscription_enseignant`, `inscription_parent` sont résolvables via `{% url %}` et `reverse()`
- Le nom `inscription` redirige vers `choix_role`

#### 🏗 Architecture

- 4 nouveaux `path()` dans `users/urls.py`
- L'ancien `path("inscription/", ...)` est modifié pour être un redirect 301 → backward compat
- `name="inscription"` conservé sur le redirect pour ne pas casser les templates existants qui utilisent `{% url 'inscription' %}`

#### 🔒 Sécurité

- Aucun risque — ce sont des routes publiques (inscription)
- Les vues elles-mêmes gèrent la sécurité (vérification si authentifié, rate limit, CSRF)

#### ✅ Definition of Done

- [ ] 4 nouvelles URLs ajoutées dans `users/urls.py`
- [ ] URL `/inscription/` redirige en 301 vers `/inscription/choix/`
- [ ] `{% url 'choix_role' %}`, `{% url 'inscription_eleve' %}`, `{% url 'inscription_enseignant' %}`, `{% url 'inscription_parent' %}` résolvables
- [ ] `{% url 'inscription' %}` toujours résolvable (backward compat)
- [ ] `CODEBASE_REFERENCE.md` section 2.2 (users URLs) mise à jour
- [ ] Lien « Inscription » dans `login.html` mis à jour pour pointer vers `choix_role`

---

### 🧪 Tests — Phase 2

> **Agent responsable** : `test-writer`
> **Fichiers** : migration vers `users/tests/` — création de `users/tests/__init__.py`, `users/tests/conftest.py`, `users/tests/test_inscription.py`
> Le fichier `users/tests.py` existant est déplacé vers `users/tests/test_existants.py` (aucune modification de contenu)
> **Nombre minimum** : 18 tests

#### Fixtures — `users/tests/conftest.py`

```python
import pytest
from users.models import CustomUser, RoleChoices

@pytest.fixture
def eleve(db):
    """Élève actif avec niveau seconde."""
    return CustomUser.objects.create_user(
        email="eleve@test.com", prenom="Jean", nom="Dupont",
        password="Test1234!", role=RoleChoices.ELEVE, niveau="seconde",
    )

@pytest.fixture
def enseignant(db):
    """Enseignant actif."""
    return CustomUser.objects.create_user(
        email="prof@test.com", prenom="Marie", nom="Curie",
        password="Test1234!", role=RoleChoices.ENSEIGNANT,
    )

@pytest.fixture
def parent_user(db):
    """Parent actif."""
    return CustomUser.objects.create_user(
        email="parent@test.com", prenom="Paul", nom="Dupont",
        password="Test1234!", role=RoleChoices.PARENT,
    )

@pytest.fixture
def admin_user(db):
    """Admin actif."""
    return CustomUser.objects.create_superuser(
        email="admin@test.com", prenom="Admin", nom="Root",
        password="Test1234!",
    )
```

#### Tests — `users/tests/test_inscription.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_choix_role_get_200` | `client` (anonyme) | `response.status_code == 200` + contient "Élève", "Enseignant", "Parent" |
| 2 | `test_inscription_eleve_get_200` | `client` (anonyme) | `response.status_code == 200` + contient "Inscription Élève" |
| 3 | `test_inscription_eleve_post_sans_code_cree_compte_role_eleve` | `client` (anonyme) | `CustomUser.objects.filter(email="new@test.com", role="eleve").exists()` + `response.status_code == 302` vers `inscription_confirmation` |
| 4 | `test_inscription_eleve_post_avec_code_valide_cree_lien_en_attente` | `enseignant` | POST avec `code_enseignant=enseignant.code_identifiant` → `LienEnseignantEleve.objects.filter(eleve__email="new@test.com", enseignant=enseignant, statut="en_attente").exists()` + `Notification.objects.filter(destinataire=enseignant, type="demande_liaison").exists()` |
| 5 | `test_inscription_eleve_post_code_invalide_erreur_formulaire` | `client` (anonyme) | POST avec `code_enseignant="XXXAAAAA"` → `response.status_code == 200` + `"Code invalide ou inactif."` dans le HTML |
| 6 | `test_inscription_eleve_post_code_mauvais_prefixe_erreur_formulaire` | `eleve` | POST avec `code_enseignant=eleve.code_identifiant` (préfixe ELV) → `response.status_code == 200` + `"Code invalide ou inactif."` dans le HTML |
| 7 | `test_inscription_eleve_post_email_duplique_erreur_formulaire` | `eleve` | POST avec `email=eleve.email` → `response.status_code == 200` + `"Un compte avec cet email existe déjà."` dans le HTML |
| 8 | `test_inscription_eleve_post_is_active_false` | `client` (anonyme) | POST valide → `CustomUser.objects.get(email="new@test.com").is_active == False` |
| 9 | `test_inscription_eleve_post_premiers_chapitres_debloques` | `client` (anonyme) + chapitres seed | POST valide → `ChapitreDebloque.objects.filter(user__email="new@test.com").count() >= 1` |
| 10 | `test_inscription_enseignant_get_200` | `client` (anonyme) | `response.status_code == 200` + contient "Inscription Enseignant" |
| 11 | `test_inscription_enseignant_post_cree_compte_role_enseignant` | `client` (anonyme) | `CustomUser.objects.filter(email="prof2@test.com", role="enseignant").exists()` + redirect vers `inscription_confirmation` |
| 12 | `test_inscription_enseignant_post_niveau_null` | `client` (anonyme) | POST valide → `CustomUser.objects.get(email="prof2@test.com").niveau is None` |
| 13 | `test_inscription_parent_get_200` | `client` (anonyme) | `response.status_code == 200` + contient "Inscription Parent" |
| 14 | `test_inscription_parent_post_sans_code_erreur_formulaire` | `client` (anonyme) | POST sans `code_eleve` → `response.status_code == 200` + `"Le code élève est obligatoire."` dans le HTML |
| 15 | `test_inscription_parent_post_code_valide_cree_lien_en_attente` | `eleve` | POST avec `code_eleve=eleve.code_identifiant` → `LienParentEleve.objects.filter(parent__email="parent2@test.com", eleve=eleve, statut="en_attente").exists()` + `Notification.objects.filter(destinataire=eleve, type="demande_liaison").exists()` |
| 16 | `test_inscription_parent_post_code_eleve_inactif_erreur` | `db` | Créer un élève avec `is_active=False` → POST avec son code → `response.status_code == 200` + `"Code invalide ou inactif."` dans le HTML |
| 17 | `test_email_verification_active_compte` | `client` (anonyme) | POST inscription élève, récupérer le token signé, GET `/verifier-email/<token>/` → `CustomUser.objects.get(email="new@test.com").is_active == True` |
| 18 | `test_backward_compat_ancien_url_inscription_redirige` | `client` (anonyme) | `GET /inscription/` → `response.status_code == 301` + `response["Location"]` contient `/inscription/choix/` |

**Tests complémentaires recommandés** (bonus, non bloquants) :

| # | Nom du test | Assertion clé |
|---|-------------|---------------|
| 19 | `test_choix_role_get_authenticated_redirect` | `client.force_login(eleve)` + `GET /inscription/choix/` → 302 vers `tableau_de_bord` |
| 20 | `test_inscription_eleve_rate_limit_code_429` | 6 POST consécutifs avec code → 6e retourne 429 + `"Trop de tentatives."` dans le HTML |
| 21 | `test_inscription_parent_rate_limit_code_429` | Idem pour parent |
| 22 | `test_inscription_eleve_transaction_atomic_rollback` | Mock `_creer_lien_enseignant` pour lever une exception → vérifier que le user n'est PAS créé (rollback) |

---

### Résumé des changements par fichier — Phase 2

| Fichier | Action |
|---------|--------|
| `users/forms.py` | Ajouter `InscriptionEleveForm`, `InscriptionEnseignantForm`, `InscriptionParentForm` |
| `users/helpers.py` | **Nouveau** — `_creer_lien_enseignant()`, `_creer_lien_parent()` |
| `users/views.py` | Ajouter `choix_role_view`, `inscription_eleve_view`, `inscription_enseignant_view`, `inscription_parent_view`, `_get_client_ip()` |
| `users/urls.py` | Ajouter 4 URLs + modifier l'ancienne `/inscription/` en redirect 301 |
| `templates/registration/choix_role.html` | **Nouveau** — page de choix du rôle |
| `templates/registration/register_eleve.html` | **Nouveau** — formulaire inscription élève |
| `templates/registration/register_enseignant.html` | **Nouveau** — formulaire inscription enseignant |
| `templates/registration/register_parent.html` | **Nouveau** — formulaire inscription parent |
| `templates/registration/login.html` | Mettre à jour le lien « Inscription » → `{% url 'choix_role' %}` |
| `users/tests/__init__.py` | **Nouveau** — init du package tests |
| `users/tests/conftest.py` | **Nouveau** — fixtures `eleve`, `enseignant`, `parent_user`, `admin_user` |
| `users/tests/test_inscription.py` | **Nouveau** — 18+ tests d'inscription multi-rôles |
| `users/tests/test_existants.py` | **Déplacé** depuis `users/tests.py` (aucune modification de contenu) |
| `CODEBASE_REFERENCE.md` | Sections 2.2 (URLs), 3.2 (Views), 4 (Forms), 5.5 (Templates), 8 (Patterns) mises à jour |

### Ordre d'exécution recommandé

```
1. Implementer  → Étape 2.1 (formulaires dans users/forms.py)
2. Implementer  → Étape 2.2 (helpers.py + vues dans users/views.py)
3. Implementer  → Étape 2.3 (4 templates dans templates/registration/)
4. Implementer  → Étape 2.4 (URLs dans users/urls.py + update login.html)
5. Test Writer  → 18+ tests dans users/tests/test_inscription.py
6. Implementer  → Mise à jour CODEBASE_REFERENCE.md
```

---

## Phase 3 — Système de validation des liaisons

> **Objectif** : permettre aux enseignants et aux élèves de gérer les demandes de liaison (valider / refuser), aux enseignants d'ajouter un élève par code, et centraliser les notifications avec badge en temps réel. Cette phase utilise les modèles créés en Phase 1 et les helpers créés en Phase 2. Aucune modification de modèle dans cette phase.

### Décisions d'architecture (Phase 3)

| Décision | Justification |
|----------|---------------|
| Helper centralisé `valider_lien(lien, valideur)` dans `users/helpers.py` | La logique de validation est identique pour enseignant et élève : vérifier le statut, les contraintes de nombre, mettre à jour, notifier. DRY entre `liaisons_enseignant_view` et `liaisons_eleve_view` |
| `select_for_update()` sur le lien lors de la validation | Évite les race conditions si deux requêtes concurrentes tentent de valider/refuser le même lien simultanément. Requiert `transaction.atomic()` |
| HTMX pour les boutons Valider/Refuser | Pas de full page reload — le bouton envoie un POST, la vue retourne un fragment HTML qui remplace la ligne du lien dans la liste. UX fluide sans JS supplémentaire |
| Cache pour le compteur de notifications | `cache.set(f"notif_count_{user.id}", count, 300)` (5 min) évite un `COUNT(*)` à chaque chargement de page. Invalidation explicite à chaque création/marquage de notification |
| Fragment HTMX pour le badge cloche | `hx-get="/notifications/badge/" hx-trigger="every 30s"` retourne uniquement le span du compteur. Pas de WebSocket — suffisant pour le volume scolaire, complexité minimale |
| Rate limit 10 liaisons/heure par enseignant | Empêche le spam de demandes de liaison. Implémenté via cache comme `_check_quiz_rate_limit()` : `cache.get(f"liaison_rate_{user.id}")` |
| Pagination 25/page sur les liaisons et notifications | Conforme aux standards transversaux. `Paginator(queryset, 25)` dans chaque vue liste |

---

### Étape 3.1 — Vue gestion liaisons enseignant

**Fichiers** : `users/views.py`, `users/helpers.py`, `users/urls.py`

#### Vues

```python
@login_required
def liaisons_enseignant_view(request):
    """Liste les liaisons de l'enseignant connecté avec actions valider/refuser."""
    if request.user.role != RoleChoices.ENSEIGNANT:
        return HttpResponseForbidden()

    liaisons = (
        LienEnseignantEleve.objects
        .filter(enseignant=request.user)
        .select_related("eleve")
        .order_by("-cree_le")
    )
    paginator = Paginator(liaisons, 25)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "users/liaisons_enseignant.html", {"page_obj": page})


@login_required
@require_POST
def action_lien_enseignant_view(request, lien_id, action):
    """Valide ou refuse un lien enseignant-élève (HTMX, retourne fragment)."""
    if request.user.role != RoleChoices.ENSEIGNANT:
        return HttpResponseForbidden()

    with transaction.atomic():
        lien = get_object_or_404(
            LienEnseignantEleve.objects.select_for_update(),
            pk=lien_id,
            enseignant=request.user,
        )
        resultat = valider_lien(lien, request.user, action)

    return render(request, "users/_fragment_lien_enseignant.html", {
        "lien": lien, "resultat": resultat,
    })
```

#### Helper `valider_lien()` dans `users/helpers.py`

```python
from django.utils import timezone
from users.models import (
    LienEnseignantEleve, LienParentEleve,
    StatutLienChoices, Notification, TypeNotificationChoices,
)

def valider_lien(lien, valideur, action):
    """Valide ou refuse un lien (enseignant-élève ou parent-élève). DRY."""
    if lien.statut != StatutLienChoices.EN_ATTENTE:
        return {"ok": False, "message": "Ce lien a déjà été traité."}

    if action == "valider":
        # Contraintes de nombre
        if isinstance(lien, LienEnseignantEleve):
            if LienEnseignantEleve.objects.filter(
                eleve=lien.eleve, statut=StatutLienChoices.VALIDE,
            ).exists():
                lien.statut = StatutLienChoices.REFUSE
                lien.save()
                return {"ok": False, "message": "Cet élève a déjà un enseignant lié."}
            destinataire = lien.eleve
        elif isinstance(lien, LienParentEleve):
            if LienParentEleve.objects.filter(
                eleve=lien.eleve, statut=StatutLienChoices.VALIDE,
            ).count() >= 2:
                lien.statut = StatutLienChoices.REFUSE
                lien.save()
                return {"ok": False, "message": "Cet élève a déjà 2 parents liés."}
            destinataire = lien.eleve if hasattr(lien, "parent") else lien.enseignant

        lien.statut = StatutLienChoices.VALIDE
        lien.valide_le = timezone.now()  # Note: champ à ajouter si absent — sinon mis_a_jour_le suffit
        lien.save()

        Notification.objects.create(
            destinataire=destinataire,
            type=TypeNotificationChoices.LIAISON_VALIDEE,
            titre="Liaison validée",
            contenu=f"Votre liaison a été validée par {valideur.nom_complet}.",
            lien="/panel-enseignant/liaisons/" if isinstance(lien, LienEnseignantEleve) else "/mes-liaisons/",
        )
        _invalider_cache_notifications(destinataire.id)
        return {"ok": True, "message": "Liaison validée avec succès."}

    elif action == "refuser":
        lien.statut = StatutLienChoices.REFUSE
        lien.save()

        if isinstance(lien, LienEnseignantEleve):
            destinataire = lien.eleve
        else:
            destinataire = lien.eleve

        Notification.objects.create(
            destinataire=destinataire,
            type=TypeNotificationChoices.LIAISON_REFUSEE,
            titre="Liaison refusée",
            contenu=f"Votre liaison a été refusée par {valideur.nom_complet}.",
            lien="/panel-enseignant/liaisons/" if isinstance(lien, LienEnseignantEleve) else "/mes-liaisons/",
        )
        _invalider_cache_notifications(destinataire.id)
        return {"ok": True, "message": "Liaison refusée."}

    return {"ok": False, "message": "Action invalide."}


def _invalider_cache_notifications(user_id):
    """Invalide le cache du compteur de notifications pour un utilisateur."""
    from django.core.cache import cache
    cache.delete(f"notif_count_{user_id}")
```

#### URLs

```python
# users/urls.py (ajouts)
path("panel-enseignant/liaisons/", liaisons_enseignant_view, name="liaisons_enseignant"),
path("panel-enseignant/liaisons/<int:lien_id>/<str:action>/", action_lien_enseignant_view, name="action_lien_enseignant"),
```

#### 🎯 Critères d'acceptation

- `GET /panel-enseignant/liaisons/` avec un enseignant connecté → 200, liste paginée des liaisons
- `GET /panel-enseignant/liaisons/` avec un élève connecté → 403
- `GET /panel-enseignant/liaisons/` anonyme → redirect vers login
- `POST /panel-enseignant/liaisons/5/valider/` avec lien `statut='en_attente'` et `enseignant=request.user` → `statut='valide'`, `mis_a_jour_le=now()`, notification créée pour l'élève, fragment HTML retourné
- `POST /panel-enseignant/liaisons/5/refuser/` → `statut='refuse'`, notification créée pour l'élève
- `POST valider un lien d'un autre enseignant` → 404 (filtre `enseignant=request.user` dans `get_object_or_404`)
- `POST valider un lien déjà traité (statut != en_attente)` → fragment avec message "Ce lien a déjà été traité."
- Élève avec déjà un enseignant validé → nouveau lien automatiquement refusé, message "Cet élève a déjà un enseignant lié."
- Pagination : 25 liaisons par page, paramètre `?page=N`

#### 🏗 Architecture

- `valider_lien(lien, valideur, action)` dans `users/helpers.py` — réutilisé en 3.2 pour les liaisons parent
- `select_for_update()` sur le lien dans `transaction.atomic()` pour éviter les race conditions
- Fragment HTMX `_fragment_lien_enseignant.html` retourné après action — pas de full page reload
- `select_related("eleve")` sur le queryset pour éviter les requêtes N+1
- `_invalider_cache_notifications()` appelé après chaque création de notification

#### 🔒 Sécurité

- **Broken Access Control** : vérification `request.user.role == ENSEIGNANT` + filtre `enseignant=request.user` dans le queryset → impossible de valider le lien d'un autre enseignant (retourne 404, pas 403, pour éviter l'énumération)
- **Race condition** : `select_for_update()` empêche la double validation concurrente
- **CSRF** : protégé par `{% csrf_token %}` dans le formulaire HTMX (meta tag CSRF dans `base.html`)
- **IDOR** : le filtre `enseignant=request.user` dans `get_object_or_404` empêche l'accès aux liens d'autres enseignants

#### ⚡ Performance

- `select_related("eleve")` sur le queryset principal → 1 requête au lieu de N+1
- Pagination 25/page → requête bornée
- `select_for_update()` : verrou ligne uniquement, libéré en fin de transaction (rapide)
- Budget SQL : ≤ 5 requêtes pour la page liste (auth + count + page + CSRF)

#### ✅ Definition of Done

- [ ] Vue `liaisons_enseignant_view` (GET liste paginée) implémentée
- [ ] Vue `action_lien_enseignant_view` (POST valider/refuser) implémentée
- [ ] Helper `valider_lien()` dans `users/helpers.py` — fonctionne pour enseignant ET parent
- [ ] URLs `liaisons_enseignant` et `action_lien_enseignant` enregistrées
- [ ] Fragment HTMX `_fragment_lien_enseignant.html` créé
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 2.2, 3.2, 8 mises à jour

---

### Étape 3.2 — Vue gestion liaisons élève (demandes parent)

**Fichiers** : `users/views.py`, `users/urls.py`

#### Vues

```python
@login_required
def liaisons_eleve_view(request):
    """Liste les demandes de liaison parent pour l'élève connecté."""
    if request.user.role != RoleChoices.ELEVE:
        return HttpResponseForbidden()

    liaisons = (
        LienParentEleve.objects
        .filter(eleve=request.user)
        .select_related("parent")
        .order_by("-cree_le")
    )
    paginator = Paginator(liaisons, 25)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "users/liaisons_eleve.html", {"page_obj": page})


@login_required
@require_POST
def action_lien_eleve_view(request, lien_id, action):
    """Valide ou refuse un lien parent-élève (HTMX, retourne fragment)."""
    if request.user.role != RoleChoices.ELEVE:
        return HttpResponseForbidden()

    with transaction.atomic():
        lien = get_object_or_404(
            LienParentEleve.objects.select_for_update(),
            pk=lien_id,
            eleve=request.user,
        )
        resultat = valider_lien(lien, request.user, action)

    return render(request, "users/_fragment_lien_eleve.html", {
        "lien": lien, "resultat": resultat,
    })
```

#### URLs

```python
# users/urls.py (ajouts)
path("mes-liaisons/", liaisons_eleve_view, name="liaisons_eleve"),
path("mes-liaisons/<int:lien_id>/<str:action>/", action_lien_eleve_view, name="action_lien_eleve"),
```

#### 🎯 Critères d'acceptation

- `GET /mes-liaisons/` avec un élève connecté → 200, liste paginée des demandes parent
- `GET /mes-liaisons/` avec un enseignant connecté → 403
- `GET /mes-liaisons/` anonyme → redirect vers login
- `POST /mes-liaisons/7/valider/` avec lien `statut='en_attente'` et `eleve=request.user` → `statut='valide'`, notification créée pour le parent
- `POST /mes-liaisons/7/refuser/` → `statut='refuse'`, notification créée pour le parent
- `POST valider un lien d'un autre élève` → 404
- Élève avec déjà 2 parents validés → nouveau lien automatiquement refusé, message "Cet élève a déjà 2 parents liés."
- Réutilise le même helper `valider_lien()` que l'étape 3.1

#### 🏗 Architecture

- Réutilise `valider_lien()` de `users/helpers.py` — aucune duplication de logique
- Fragment HTMX `_fragment_lien_eleve.html` pour le retour après action
- `select_related("parent")` pour optimiser le queryset
- Même pattern `select_for_update()` + `transaction.atomic()` que 3.1

#### 🔒 Sécurité

- **IDOR** : filtre `eleve=request.user` dans `get_object_or_404` → impossible de valider le lien d'un autre élève
- **Broken Access Control** : vérification `request.user.role == ELEVE`
- **Race condition** : `select_for_update()` protège la validation concurrente

#### ⚡ Performance

- `select_related("parent")` → 1 requête au lieu de N+1
- Pagination 25/page
- Budget SQL : ≤ 5 requêtes pour la page liste

#### ✅ Definition of Done

- [ ] Vue `liaisons_eleve_view` (GET liste paginée) implémentée
- [ ] Vue `action_lien_eleve_view` (POST valider/refuser) implémentée
- [ ] URLs `liaisons_eleve` et `action_lien_eleve` enregistrées
- [ ] Fragment HTMX `_fragment_lien_eleve.html` créé
- [ ] Tests passent
- [ ] `CODEBASE_REFERENCE.md` mis à jour

---

### Étape 3.3 — Liaison initiée par l'enseignant (ajout d'élève par code)

**Fichiers** : `users/views.py`, `users/forms.py`, `users/urls.py`

#### Formulaire

```python
class AjouterEleveForm(forms.Form):
    """Formulaire pour qu'un enseignant ajoute un élève par code identifiant."""
    code_eleve = forms.CharField(
        max_length=8,
        label="Code élève",
        help_text="Saisissez le code identifiant de l'élève (ex: ELV1A2B3).",
    )

    def clean_code_eleve(self):
        code = self.cleaned_data["code_eleve"].strip().upper()
        if not code.startswith("ELV"):
            raise forms.ValidationError("Code invalide.")
        if not CustomUser.objects.filter(
            code_identifiant=code, role=RoleChoices.ELEVE, is_active=True,
        ).exists():
            raise forms.ValidationError("Code invalide.")
        return code
```

#### Vue

```python
@login_required
def ajouter_eleve_view(request):
    """Formulaire pour qu'un enseignant ajoute un élève par code identifiant."""
    if request.user.role != RoleChoices.ENSEIGNANT:
        return HttpResponseForbidden()

    if _check_liaison_rate_limit(request.user.id):
        return HttpResponse("Trop de tentatives. Réessayez plus tard.", status=429)

    if request.method == "POST":
        form = AjouterEleveForm(request.POST)
        if form.is_valid():
            eleve = CustomUser.objects.get(
                code_identifiant=form.cleaned_data["code_eleve"],
            )
            with transaction.atomic():
                lien, created = LienEnseignantEleve.objects.get_or_create(
                    enseignant=request.user,
                    eleve=eleve,
                    defaults={"statut": StatutLienChoices.EN_ATTENTE},
                )
                if created:
                    Notification.objects.create(
                        destinataire=eleve,
                        type=TypeNotificationChoices.DEMANDE_LIAISON,
                        titre="Demande de liaison enseignant",
                        contenu=f"{request.user.nom_complet} souhaite devenir votre enseignant.",
                        lien="/mes-liaisons/",
                    )
                    _invalider_cache_notifications(eleve.id)
            messages.success(request, "Demande de liaison envoyée." if created else "Une demande existe déjà pour cet élève.")
            return redirect("liaisons_enseignant")
    else:
        form = AjouterEleveForm()

    return render(request, "users/ajouter_eleve.html", {"form": form})


def _check_liaison_rate_limit(user_id):
    """Vérifie le rate limit de 10 liaisons/heure pour un enseignant."""
    from django.core.cache import cache
    key = f"liaison_rate_{user_id}"
    count = cache.get(key, 0)
    if count >= 10:
        return True
    cache.set(key, count + 1, 3600)
    return False
```

#### URL

```python
# users/urls.py (ajout)
path("panel-enseignant/ajouter-eleve/", ajouter_eleve_view, name="ajouter_eleve"),
```

#### 🎯 Critères d'acceptation

- `GET /panel-enseignant/ajouter-eleve/` avec un enseignant connecté → 200, formulaire avec champ `code_eleve`
- `GET /panel-enseignant/ajouter-eleve/` avec un élève → 403
- `POST` avec code valide d'un élève actif → `LienEnseignantEleve` créé avec `statut='en_attente'`, notification envoyée à l'élève, redirect vers `liaisons_enseignant`
- `POST` avec code invalide (mauvais préfixe, inexistant, utilisateur inactif) → formulaire ré-affiché avec erreur "Code invalide."
- `POST` avec code d'un élève déjà lié → pas de doublon (`get_or_create`), message "Une demande existe déjà pour cet élève."
- Rate limit : 11e demande en 1h → HTTP 429
- Message d'erreur générique "Code invalide." pour empêcher l'énumération de codes

#### 🏗 Architecture

- `AjouterEleveForm` dans `users/forms.py` — validation du code dans `clean_code_eleve()`
- `get_or_create()` empêche les doublons de paire (enseignant, élève) sans lever d'IntegrityError
- `_check_liaison_rate_limit()` dans `users/views.py` (pattern identique à `_check_quiz_rate_limit()`)
- `transaction.atomic()` pour création lien + notification
- `_invalider_cache_notifications()` après création de notification

#### 🔒 Sécurité

- **Énumération de codes** : message d'erreur générique "Code invalide." pour tout cas d'échec (mauvais préfixe, code inexistant, utilisateur inactif)
- **Rate limit** : 10 liaisons/heure par enseignant via cache pour empêcher le brute force de codes
- **CSRF** : formulaire standard Django avec `{% csrf_token %}`
- **Broken Access Control** : vérification `role == ENSEIGNANT`

#### ⚡ Performance

- `get_or_create()` : 1 requête (ou 2 en cas de création) — évite un SELECT + INSERT séparé
- Rate limit via cache Redis/Memcached : O(1)

#### ✅ Definition of Done

- [ ] `AjouterEleveForm` dans `users/forms.py`
- [ ] Vue `ajouter_eleve_view` (GET formulaire + POST création lien) implémentée
- [ ] `_check_liaison_rate_limit()` implémenté
- [ ] URL `ajouter_eleve` enregistrée
- [ ] Template `ajouter_eleve.html` créé
- [ ] Tests passent
- [ ] `CODEBASE_REFERENCE.md` mis à jour

---

### Étape 3.4 — Contrainte un seul enseignant par élève

**Fichiers** : `users/helpers.py` (déjà géré dans `valider_lien()`)

> Cette contrainte est intégrée dans le helper `valider_lien()` (étape 3.1). Cette étape documente la vérification et ses cas limites.

#### Logique dans `valider_lien()`

```python
# Extrait de valider_lien() — branche LienEnseignantEleve + action "valider"
if isinstance(lien, LienEnseignantEleve):
    if LienEnseignantEleve.objects.filter(
        eleve=lien.eleve,
        statut=StatutLienChoices.VALIDE,
    ).exclude(pk=lien.pk).exists():
        lien.statut = StatutLienChoices.REFUSE
        lien.save()
        Notification.objects.create(
            destinataire=lien.enseignant,
            type=TypeNotificationChoices.LIAISON_REFUSEE,
            titre="Liaison refusée automatiquement",
            contenu=f"L'élève {lien.eleve.nom_complet} a déjà un enseignant lié.",
            lien="/panel-enseignant/liaisons/",
        )
        _invalider_cache_notifications(lien.enseignant.id)
        return {"ok": False, "message": "Cet élève a déjà un enseignant lié."}
```

#### 🎯 Critères d'acceptation

- Un enseignant tente de valider un lien avec un élève qui a déjà un enseignant validé → lien automatiquement refusé (`statut='refuse'`), notification envoyée à l'enseignant demandeur, message "Cet élève a déjà un enseignant lié."
- La vérification utilise `.exclude(pk=lien.pk)` pour ne pas considérer le lien courant comme bloquant
- La vérification est effectuée à l'intérieur du `select_for_update()` + `transaction.atomic()` pour éviter les race conditions
- Un élève avec un enseignant `statut='refuse'` ou `statut='en_attente'` ne bloque PAS la validation d'un nouveau lien

#### 🏗 Architecture

- La contrainte est applicative (dans `valider_lien()`), pas un `unique_together` Django — car on a besoin de vérifier `statut='valide'` uniquement, pas la paire brute
- L'`.exclude(pk=lien.pk)` empêche un faux positif lors d'une re-validation idempotente
- La notification au demandeur refusé est créée dans la même transaction que le refus

#### 🔒 Sécurité

- **Race condition** : `select_for_update()` sur le lien + vérification dans `transaction.atomic()` → il est impossible que deux enseignants valident simultanément pour le même élève
- Le message retourné ne révèle pas l'identité de l'enseignant existant (juste "a déjà un enseignant lié")

#### ⚡ Performance

- 1 requête `EXISTS` supplémentaire lors de la validation (indexée par `(eleve, statut)`)

#### ✅ Definition of Done

- [ ] Contrainte vérifiée dans `valider_lien()` avec `.exclude(pk=lien.pk)`
- [ ] Lien automatiquement refusé si contrainte violée
- [ ] Notification envoyée à l'enseignant demandeur refusé
- [ ] Protégé par `select_for_update()` contre les race conditions
- [ ] Tests passent

---

### Étape 3.5 — Contrainte max 2 parents par élève

**Fichiers** : `users/helpers.py` (déjà géré dans `valider_lien()`)

> Même pattern que 3.4, mais pour `LienParentEleve` avec un seuil de 2.

#### Logique dans `valider_lien()`

```python
# Extrait de valider_lien() — branche LienParentEleve + action "valider"
if isinstance(lien, LienParentEleve):
    count = LienParentEleve.objects.filter(
        eleve=lien.eleve,
        statut=StatutLienChoices.VALIDE,
    ).exclude(pk=lien.pk).count()
    if count >= 2:
        lien.statut = StatutLienChoices.REFUSE
        lien.save()
        Notification.objects.create(
            destinataire=lien.parent,
            type=TypeNotificationChoices.LIAISON_REFUSEE,
            titre="Liaison refusée automatiquement",
            contenu=f"L'élève {lien.eleve.nom_complet} a déjà 2 parents liés.",
            lien="/",
        )
        _invalider_cache_notifications(lien.parent.id)
        return {"ok": False, "message": "Cet élève a déjà 2 parents liés."}
```

#### 🎯 Critères d'acceptation

- Un élève tente de valider un 3e lien parent → lien automatiquement refusé, notification envoyée au parent demandeur, message "Cet élève a déjà 2 parents liés."
- Un élève avec 1 parent validé peut valider un 2e parent sans problème
- Un élève avec 2 parents `en_attente` peut valider l'un des deux (l'autre reste en attente)
- La vérification utilise `.exclude(pk=lien.pk)` et `.count()` au lieu de `.exists()`

#### 🏗 Architecture

- Seuil `>= 2` (constante en dur dans le code). Si le seuil change, il devrait être extrait en constante modèle ou settings — mais YAGNI pour le MVP
- `.count()` au lieu de `.exists()` car on vérifie un seuil numérique, pas juste l'existence

#### 🔒 Sécurité

- Même protection `select_for_update()` + `transaction.atomic()` que 3.4
- Le message ne révèle pas l'identité des parents existants

#### ⚡ Performance

- 1 requête `COUNT` indexée par `(eleve, statut)` — négligeable

#### ✅ Definition of Done

- [ ] Contrainte `count >= 2` vérifiée dans `valider_lien()` pour `LienParentEleve`
- [ ] Lien automatiquement refusé si contrainte violée
- [ ] Notification envoyée au parent demandeur refusé
- [ ] Protégé par `select_for_update()` contre les race conditions
- [ ] Tests passent

---

### Étape 3.6 — Centre de notifications + badge cloche HTMX

**Fichiers** : `users/views.py`, `users/urls.py`, `templates/base.html`

#### Vues

```python
@login_required
def notifications_view(request):
    """Liste paginée des notifications de l'utilisateur connecté."""
    notifications = (
        Notification.objects
        .filter(destinataire=request.user)
        .order_by("-cree_le")
    )
    paginator = Paginator(notifications, 25)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "users/notifications.html", {"page_obj": page})


@login_required
@require_POST
def marquer_notification_lue_view(request, notif_id):
    """Marque une notification comme lue (HTMX, retourne fragment)."""
    notif = get_object_or_404(Notification, pk=notif_id, destinataire=request.user)
    notif.lue = True
    notif.save(update_fields=["lue"])
    _invalider_cache_notifications(request.user.id)
    return render(request, "users/_fragment_notification.html", {"notif": notif})


@login_required
@require_POST
def tout_marquer_lu_view(request):
    """Marque toutes les notifications non lues comme lues."""
    Notification.objects.filter(
        destinataire=request.user, lue=False,
    ).update(lue=True)
    _invalider_cache_notifications(request.user.id)
    return redirect("notifications")


@login_required
def badge_notifications_view(request):
    """Fragment HTMX : retourne uniquement le compteur de notifications non lues."""
    from django.core.cache import cache
    key = f"notif_count_{request.user.id}"
    count = cache.get(key)
    if count is None:
        count = Notification.objects.filter(
            destinataire=request.user, lue=False,
        ).count()
        cache.set(key, count, 300)
    return HttpResponse(f'<span class="badge-count">{count}</span>' if count > 0 else "")
```

#### URLs

```python
# users/urls.py (ajouts)
path("notifications/", notifications_view, name="notifications"),
path("notifications/<int:notif_id>/lue/", marquer_notification_lue_view, name="marquer_notification_lue"),
path("notifications/tout-lu/", tout_marquer_lu_view, name="tout_marquer_lu"),
path("notifications/badge/", badge_notifications_view, name="badge_notifications"),
```

#### Badge cloche dans `base.html`

```html
<!-- Dans le header, à côté du bouton dark mode -->
{% if user.is_authenticated %}
<a href="{% url 'notifications' %}" class="relative p-2">
    <svg><!-- icône cloche --></svg>
    <span
        hx-get="{% url 'badge_notifications' %}"
        hx-trigger="load, every 30s"
        hx-swap="innerHTML"
    ></span>
</a>
{% endif %}
```

#### 🎯 Critères d'acceptation

- `GET /notifications/` authentifié → 200, liste paginée (25/page) des notifications, les plus récentes en premier
- `GET /notifications/` anonyme → redirect vers login
- `POST /notifications/42/lue/` avec notification appartenant à l'utilisateur → `lue=True`, fragment retourné
- `POST /notifications/42/lue/` avec notification d'un autre utilisateur → 404
- `POST /notifications/tout-lu/` → toutes les notifications non lues de l'utilisateur passent à `lue=True`, redirect vers `notifications`
- `GET /notifications/badge/` → fragment HTML avec compteur (`<span class="badge-count">3</span>`) ou vide si 0
- Badge cloche dans `base.html` affiche le compteur en temps réel via `hx-trigger="load, every 30s"`
- Le compteur est mis en cache pendant 5 minutes (300s), invalidé à chaque création/marquage

#### 🏗 Architecture

- `badge_notifications_view` lit d'abord le cache, puis fallback sur `COUNT(*)` si cache vide
- `_invalider_cache_notifications()` (dans `users/helpers.py`) est appelé par : `valider_lien()`, `marquer_notification_lue_view`, `tout_marquer_lu_view`, et tout code créant une notification
- `tout_marquer_lu_view` utilise `.update(lue=True)` (1 requête bulk) et non une boucle `.save()`
- Fragment HTMX `_fragment_notification.html` pour le retour de `marquer_notification_lue_view`
- Le badge utilise `hx-swap="innerHTML"` pour remplacer uniquement le contenu du span

#### 🔒 Sécurité

- **IDOR** : filtre `destinataire=request.user` sur tous les endpoints → impossible de lire/marquer les notifications d'un autre utilisateur
- **CSRF** : toutes les actions POST protégées
- Le fragment badge ne retourne aucune donnée sensible (juste un nombre entier)

#### ⚡ Performance

- Cache `notif_count_{user_id}` (5 min TTL) — le `COUNT(*)` n'est exécuté que si le cache est vide
- `update(lue=True)` bulk pour "tout marquer lu" — 1 requête quel que soit le nombre de notifications
- `save(update_fields=["lue"])` pour le marquage unitaire — UPDATE minimal
- Le polling `every 30s` génère 2 req/min max par utilisateur connecté — acceptable pour le volume scolaire
- Index composite `(destinataire, lue, -cree_le)` (créé en Phase 1) optimise les requêtes liste et compteur

#### ✅ Definition of Done

- [ ] Vue `notifications_view` (GET liste paginée) implémentée
- [ ] Vue `marquer_notification_lue_view` (POST unitaire, HTMX) implémentée
- [ ] Vue `tout_marquer_lu_view` (POST bulk) implémentée
- [ ] Vue `badge_notifications_view` (GET fragment HTMX) implémentée
- [ ] URLs `notifications`, `marquer_notification_lue`, `tout_marquer_lu`, `badge_notifications` enregistrées
- [ ] Badge cloche intégré dans `base.html` avec `hx-trigger="load, every 30s"`
- [ ] Cache compteur notifications fonctionnel + invalidation
- [ ] Tests passent
- [ ] `CODEBASE_REFERENCE.md` mis à jour

---

### Étape 3.7 — Templates

**Fichiers** : 4 templates + 3 fragments HTMX

| Template | Description |
|----------|-------------|
| `templates/users/liaisons_enseignant.html` | Liste des liaisons enseignant avec boutons Valider/Refuser HTMX |
| `templates/users/liaisons_eleve.html` | Liste des demandes parent avec boutons Valider/Refuser HTMX |
| `templates/users/ajouter_eleve.html` | Formulaire de saisie du code élève |
| `templates/users/notifications.html` | Liste paginée des notifications avec bouton "Tout marquer lu" |
| `templates/users/_fragment_lien_enseignant.html` | Fragment HTMX : état d'un lien après action (badge statut + message) |
| `templates/users/_fragment_lien_eleve.html` | Fragment HTMX : état d'un lien parent après action |
| `templates/users/_fragment_notification.html` | Fragment HTMX : notification après marquage lu (opacité réduite, pas de bouton) |

#### Conventions templates

- Tous étendent `base.html` via `{% block content %}`
- Boutons Valider/Refuser avec `hx-post`, `hx-target` (la ligne du lien), `hx-swap="outerHTML"`
- Bouton "Tout marquer lu" est un formulaire POST standard (redirect vers la page notifications)
- Couleurs neutres (pas de couleur matière) — ces pages sont transversales
- Pagination avec `{% include "components/pagination.html" %}` (composant existant ou à créer)
- Pas de `dark:` classes — géré globalement dans `base.html`

#### 🎯 Critères d'acceptation

- `liaisons_enseignant.html` affiche : nom de l'élève, niveau, statut (badge coloré), date, boutons Valider/Refuser pour les liens `en_attente`
- `liaisons_eleve.html` affiche : nom du parent, statut, date, boutons Valider/Refuser pour les liens `en_attente`
- `ajouter_eleve.html` affiche : champ code avec aide contextuelle, bouton Soumettre
- `notifications.html` affiche : icône par type, titre, contenu, date relative, bouton marquer lu (si non lue), bouton "Tout marquer lu" en haut de page
- Les fragments HTMX remplacent la ligne sans recharger la page
- Pagination fonctionnelle sur les 3 pages de liste

#### ✅ Definition of Done

- [ ] 4 templates + 3 fragments HTMX créés
- [ ] Boutons HTMX fonctionnels (valider/refuser sans reload)
- [ ] Pagination affichée et fonctionnelle
- [ ] Responsive (mobile-first)
- [ ] Aucune classe `dark:` dans les templates (géré par `base.html`)
- [ ] Rendu vérifié visuellement

---

### 🧪 Tests — Phase 3

> **Agent responsable** : `test-writer`
> **Fichiers** : `users/tests/test_liaisons.py`, `users/tests/test_notifications.py`
> **Nombre minimum** : 20 tests

#### `users/tests/test_liaisons.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_liaisons_enseignant_get_role_enseignant_200` | `enseignant` + `client.force_login(enseignant)` | `response.status_code == 200` + template `liaisons_enseignant.html` utilisé |
| 2 | `test_liaisons_enseignant_get_role_eleve_403` | `eleve` + `client.force_login(eleve)` | `response.status_code == 403` |
| 3 | `test_liaisons_enseignant_get_role_anonyme_redirect` | `client` (anonyme) | `response.status_code == 302` + redirect contient `/connexion/` |
| 4 | `test_enseignant_valide_lien_statut_valide` | `enseignant`, `eleve`, `LienEnseignantEleve(statut="en_attente")` | POST valider → `lien.refresh_from_db()` + `lien.statut == "valide"` |
| 5 | `test_enseignant_valide_lien_notification_creee_pour_eleve` | `enseignant`, `eleve`, lien `en_attente` | POST valider → `Notification.objects.filter(destinataire=eleve, type="liaison_validee").exists()` |
| 6 | `test_enseignant_refuse_lien_statut_refuse` | `enseignant`, `eleve`, lien `en_attente` | POST refuser → `lien.refresh_from_db()` + `lien.statut == "refuse"` |
| 7 | `test_enseignant_refuse_lien_notification_creee_pour_eleve` | `enseignant`, `eleve`, lien `en_attente` | POST refuser → `Notification.objects.filter(destinataire=eleve, type="liaison_refusee").exists()` |
| 8 | `test_idor_enseignant_valide_lien_autre_enseignant_403` | `enseignant`, `enseignant2`, lien entre `enseignant2` et `eleve` | `client.force_login(enseignant)` + POST → `response.status_code == 404` |
| 9 | `test_double_validation_idempotent` | `enseignant`, lien déjà `valide` | POST valider → fragment contient "Ce lien a déjà été traité." |
| 10 | `test_eleve_valide_parent_statut_valide` | `eleve`, `parent_user`, `LienParentEleve(statut="en_attente")` | POST valider → `lien.refresh_from_db()` + `lien.statut == "valide"` |
| 11 | `test_idor_eleve_valide_lien_autre_eleve_403` | `eleve`, `eleve2`, lien entre `parent_user` et `eleve2` | `client.force_login(eleve)` + POST → `response.status_code == 404` |
| 12 | `test_ajout_eleve_par_code_enseignant_lien_en_attente` | `enseignant`, `eleve` | POST `code_eleve=eleve.code_identifiant` → `LienEnseignantEleve.objects.filter(enseignant=enseignant, eleve=eleve, statut="en_attente").exists()` |
| 13 | `test_ajout_eleve_code_invalide_erreur` | `enseignant` | POST `code_eleve="XXXZZZZZ"` → `response.status_code == 200` + "Code invalide." dans le HTML |
| 14 | `test_contrainte_un_enseignant_par_eleve_refuse_nouveau` | `enseignant`, `enseignant2`, `eleve`, lien validé entre `enseignant` et `eleve` | `enseignant2` valide un nouveau lien → `lien2.refresh_from_db()` + `lien2.statut == "refuse"` + fragment contient "Cet élève a déjà un enseignant lié." |
| 15 | `test_contrainte_max_2_parents_validation_bloquee` | `eleve`, `parent1`, `parent2`, `parent3`, 2 liens validés | `eleve` valide le 3e → `lien3.refresh_from_db()` + `lien3.statut == "refuse"` + fragment contient "Cet élève a déjà 2 parents liés." |

#### `users/tests/test_notifications.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 16 | `test_notifications_get_paginee_200` | `eleve` + 30 `Notification` créées | `response.status_code == 200` + `len(response.context["page_obj"]) == 25` |
| 17 | `test_notification_marquer_lue` | `eleve` + `Notification(lue=False)` | POST → `notif.refresh_from_db()` + `notif.lue == True` |
| 18 | `test_idor_notification_autre_utilisateur_403` | `eleve`, `enseignant`, notification pour `enseignant` | `client.force_login(eleve)` + POST → `response.status_code == 404` |
| 19 | `test_tout_marquer_lu` | `eleve` + 5 `Notification(lue=False)` | POST tout-lu → `Notification.objects.filter(destinataire=eleve, lue=False).count() == 0` |
| 20 | `test_badge_notifications_htmx_fragment` | `eleve` + 3 `Notification(lue=False)` | GET badge → `response.status_code == 200` + `"3"` dans `response.content.decode()` |

**Tests complémentaires recommandés** (bonus, non bloquants) :

| # | Nom du test | Assertion clé |
|---|-------------|---------------|
| 21 | `test_badge_notifications_zero_retourne_vide` | `eleve` + 0 notif non lues → réponse vide (pas de span) |
| 22 | `test_badge_notifications_cache_utilise` | Mock `cache.get` pour retourner 5 → réponse contient "5" sans requête DB |
| 23 | `test_ajout_eleve_rate_limit_429` | `enseignant` + 11 POST en boucle → 11e retourne `status_code == 429` |
| 24 | `test_liaisons_enseignant_pagination_page_2` | `enseignant` + 30 liaisons → `GET ?page=2` → `len(page_obj) == 5` |
| 25 | `test_notification_invalidation_cache_apres_marquage` | Mock `cache.delete` → vérifie qu'il est appelé avec `f"notif_count_{eleve.id}"` |

#### Fixtures dans `users/tests/conftest.py` (ajouts Phase 3)

```python
from users.models import LienEnseignantEleve, LienParentEleve, Notification, StatutLienChoices

@pytest.fixture
def enseignant2(db):
    """Deuxième enseignant pour tests IDOR."""
    return CustomUser.objects.create_user(
        email="prof2@test.com", prenom="Albert", nom="Einstein",
        password="Test1234!", role=RoleChoices.ENSEIGNANT,
    )

@pytest.fixture
def eleve2(db):
    """Deuxième élève pour tests IDOR."""
    return CustomUser.objects.create_user(
        email="eleve2@test.com", prenom="Pierre", nom="Martin",
        password="Test1234!", role=RoleChoices.ELEVE, niveau="seconde",
    )

@pytest.fixture
def lien_enseignant_eleve_en_attente(enseignant, eleve):
    """Lien enseignant-élève en attente."""
    return LienEnseignantEleve.objects.create(
        enseignant=enseignant, eleve=eleve, statut=StatutLienChoices.EN_ATTENTE,
    )

@pytest.fixture
def lien_enseignant_eleve_valide(enseignant, eleve):
    """Lien enseignant-élève validé."""
    return LienEnseignantEleve.objects.create(
        enseignant=enseignant, eleve=eleve, statut=StatutLienChoices.VALIDE,
    )

@pytest.fixture
def lien_parent_eleve_en_attente(parent_user, eleve):
    """Lien parent-élève en attente."""
    return LienParentEleve.objects.create(
        parent=parent_user, eleve=eleve, statut=StatutLienChoices.EN_ATTENTE,
    )
```

---

### Résumé des changements par fichier — Phase 3

| Fichier | Action |
|---------|--------|
| `users/helpers.py` | Ajouter `valider_lien()`, `_invalider_cache_notifications()` |
| `users/views.py` | Ajouter `liaisons_enseignant_view`, `action_lien_enseignant_view`, `liaisons_eleve_view`, `action_lien_eleve_view`, `ajouter_eleve_view`, `_check_liaison_rate_limit`, `notifications_view`, `marquer_notification_lue_view`, `tout_marquer_lu_view`, `badge_notifications_view` |
| `users/forms.py` | Ajouter `AjouterEleveForm` |
| `users/urls.py` | Ajouter 8 URLs : `liaisons_enseignant`, `action_lien_enseignant`, `liaisons_eleve`, `action_lien_eleve`, `ajouter_eleve`, `notifications`, `marquer_notification_lue`, `tout_marquer_lu`, `badge_notifications` |
| `templates/users/liaisons_enseignant.html` | **Nouveau** — liste liaisons enseignant avec actions HTMX |
| `templates/users/liaisons_eleve.html` | **Nouveau** — liste demandes parent avec actions HTMX |
| `templates/users/ajouter_eleve.html` | **Nouveau** — formulaire ajout élève par code |
| `templates/users/notifications.html` | **Nouveau** — centre de notifications paginé |
| `templates/users/_fragment_lien_enseignant.html` | **Nouveau** — fragment HTMX après action sur lien enseignant |
| `templates/users/_fragment_lien_eleve.html` | **Nouveau** — fragment HTMX après action sur lien parent |
| `templates/users/_fragment_notification.html` | **Nouveau** — fragment HTMX après marquage notification |
| `templates/base.html` | Ajouter badge cloche HTMX dans le header |
| `users/tests/conftest.py` | Ajouter fixtures `enseignant2`, `eleve2`, `lien_*` |
| `users/tests/test_liaisons.py` | **Nouveau** — 15 tests liaisons (délégué à `test-writer`) |
| `users/tests/test_notifications.py` | **Nouveau** — 5+ tests notifications (délégué à `test-writer`) |
| `CODEBASE_REFERENCE.md` | Sections 2.2 (URLs), 3.2 (Views), 4 (Forms), 5 (Templates), 8 (Patterns) mises à jour |

### Ordre d'exécution recommandé

```
1. Implementer  → Étape 3.1 (helper valider_lien + vue liaisons enseignant)
2. Implementer  → Étape 3.2 (vue liaisons élève — réutilise le helper)
3. Implementer  → Étape 3.3 (formulaire + vue ajout élève par code)
4. Implementer  → Étapes 3.4 + 3.5 (vérifier contraintes dans valider_lien — déjà intégrées)
5. Implementer  → Étape 3.6 (vues notifications + badge cloche + cache)
6. Implementer  → Étape 3.7 (4 templates + 3 fragments HTMX)
7. Test Writer  → 20+ tests dans users/tests/test_liaisons.py + test_notifications.py
8. Implementer  → Mise à jour CODEBASE_REFERENCE.md
```

---

## Phase 4 — Dashboards par rôle

> **Objectif** : router le tableau de bord existant par rôle et créer les dashboards spécialisés pour enseignant et parent, la fiche élève complète accessible par enseignant/parent/admin, adapter le dashboard élève avec ses relations, et mettre à jour la sidebar pour la navigation conditionnelle par rôle. Aucun nouveau modèle dans cette phase — on utilise les modèles créés en Phases 1-3.

### Décisions d'architecture (Phase 4)

| Décision | Justification |
|----------|---------------|
| Routeur dans `TableauDeBordView.get()` | Le pattern existant dispatche déjà admin → `_dashboard_admin` et sinon → `_dashboard_eleve`. On étend ce dispatch à 4 branches. Pas de nouveau CBV, on garde le même point d'entrée |
| `_dashboard_enseignant(request)` et `_dashboard_parent(request)` comme fonctions privées | Cohérent avec `_dashboard_eleve(request)` et `_dashboard_admin(request)` déjà en place dans `users/views.py` |
| Helper `peut_voir_eleve(user, eleve)` dans `users/helpers.py` | Réutilisé par la fiche élève, les dashboards, et la messagerie (Phase 5). Fonction pure : reçoit deux objets `CustomUser`, retourne `True/False`. Pas d'accès à `request` |
| Helper `_calculs_stats_classe(enseignant)` dans `users/helpers.py` | DRY : les mêmes calculs (progression moyenne, score moyen, leçons terminées) sont utilisés dans le dashboard enseignant et potentiellement dans la fiche élève. Fonction pure avec une seule requête agrégée |
| `TruncDate` + `Avg` pour graphiques 30 jours | Une seule requête SQL pour les données du graphique au lieu de 30 requêtes filtrées par jour. Utilise `django.db.models.functions.TruncDate` et `Avg` |
| Sidebar conditionnelle via `{% if user.is_enseignant %}` | Les propriétés `is_enseignant`, `is_parent`, `is_eleve`, `is_admin` existent déjà sur `CustomUser` (Phase 1). Pas de template tag custom — les conditions directes sont lisibles et suffisantes |
| Fiche élève : 3 requêtes max pour calculs lourds | Les données sont regroupées en 3 requêtes annotées : (1) progression + scores par matière, (2) heatmap connexions 90j via `TruncDate`, (3) questions Leitner box=1. Le reste (identité, relations) est déjà en mémoire via `select_related` |

---

### Étape 4.1 — Router le tableau de bord par rôle

**Fichier** : `users/views.py` → `TableauDeBordView`

```python
class TableauDeBordView(LoginRequiredMixin, View):
    """Tableau de bord routé par rôle."""

    def get(self, request):
        user = request.user
        if user.role == RoleChoices.ADMIN:
            return _dashboard_admin(request)
        elif user.role == RoleChoices.ENSEIGNANT:
            return _dashboard_enseignant(request)
        elif user.role == RoleChoices.PARENT:
            return _dashboard_parent(request)
        else:
            return _dashboard_eleve(request)
```

#### 🎯 Critères d'acceptation

- Un admin connecté → `_dashboard_admin(request)` est appelé, template `dashboard/admin.html`
- Un enseignant connecté → `_dashboard_enseignant(request)` est appelé, template `dashboard/enseignant.html`
- Un parent connecté → `_dashboard_parent(request)` est appelé, template `dashboard/parent.html`
- Un élève connecté → `_dashboard_eleve(request)` est appelé, template `dashboard/eleve.html`
- Un utilisateur anonyme → redirect vers login (assuré par `LoginRequiredMixin`)
- Le routage ne dépend que de `user.role` — pas de condition sur d'autres champs
- Le preview mode (`request.session["preview_niveau"]`) ne change pas le routage — seul le rôle compte

#### 🔒 Sécurité

- Aucun risque propre — le routage ne fait que dispatcher vers des fonctions privées
- `LoginRequiredMixin` empêche l'accès anonyme (existant)

#### ⚡ Performance

- Aucune requête supplémentaire — simple dispatch conditionnel

#### ✅ Definition of Done

- [ ] `TableauDeBordView.get()` route vers 4 branches par rôle
- [ ] Chaque branche appelle la bonne fonction `_dashboard_*`
- [ ] Tests de routage passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` section 3.2 mise à jour

---

### Étape 4.2 — Dashboard enseignant

**Fichiers** : `users/views.py`, `users/helpers.py`, `templates/dashboard/enseignant.html`

#### Helper

```python
# users/helpers.py

from django.db.models import Avg, Count, Q
from django.db.models.functions import TruncDate
from django.utils import timezone
from datetime import timedelta


def _calculs_stats_classe(enseignant):
    """Calcule les stats agrégées pour les élèves liés à un enseignant."""
    from users.models import LienEnseignantEleve, StatutLienChoices
    from progress.models import UserProgression, UserQuizResultat

    eleves_ids = list(
        LienEnseignantEleve.objects
        .filter(enseignant=enseignant, statut=StatutLienChoices.VALIDE)
        .values_list("eleve_id", flat=True)
    )

    if not eleves_ids:
        return {
            "nb_eleves": 0,
            "progression_moyenne": 0,
            "score_moyen": 0,
            "lecons_terminees_semaine": 0,
        }

    nb_eleves = len(eleves_ids)

    stats_progression = UserProgression.objects.filter(
        user_id__in=eleves_ids
    ).aggregate(
        total=Count("id"),
        terminees=Count("id", filter=Q(statut="termine")),
    )

    progression_moyenne = 0
    if stats_progression["total"]:
        progression_moyenne = round(
            stats_progression["terminees"] / stats_progression["total"] * 100
        )

    score_moyen_result = UserQuizResultat.objects.filter(
        user_id__in=eleves_ids
    ).aggregate(score_moyen=Avg("meilleur_score"))
    score_moyen = round(score_moyen_result["score_moyen"] or 0)

    il_y_a_7j = timezone.now() - timedelta(days=7)
    lecons_terminees_semaine = UserProgression.objects.filter(
        user_id__in=eleves_ids,
        statut="termine",
        mis_a_jour_le__gte=il_y_a_7j,
    ).count()

    return {
        "nb_eleves": nb_eleves,
        "progression_moyenne": progression_moyenne,
        "score_moyen": score_moyen,
        "lecons_terminees_semaine": lecons_terminees_semaine,
    }
```

#### Vue

```python
# users/views.py

def _dashboard_enseignant(request):
    """Dashboard enseignant : stats classe, tableau élèves, graphique 30j."""
    from users.models import (
        LienEnseignantEleve, StatutLienChoices,
        Notification, CustomUser,
    )
    from users.helpers import _calculs_stats_classe
    from progress.models import UserQuizResultat, UserProgression
    from django.db.models.functions import TruncDate
    from django.db.models import Avg, Count, Q

    enseignant = request.user

    # Compteurs rapides
    demandes_en_attente = LienEnseignantEleve.objects.filter(
        enseignant=enseignant, statut=StatutLienChoices.EN_ATTENTE
    ).count()
    messages_non_lus = Message.objects.filter(
        conversation__participants=enseignant, lu=False
    ).exclude(auteur=enseignant).count()

    # Stats classe agrégées (1 appel helper → 3 requêtes)
    stats_classe = _calculs_stats_classe(enseignant)

    # Tableau élèves — select_related pour nom, niveau
    eleves_lies = (
        LienEnseignantEleve.objects
        .filter(enseignant=enseignant, statut=StatutLienChoices.VALIDE)
        .select_related("eleve")
    )

    tableau_eleves = []
    eleves_ids = [l.eleve_id for l in eleves_lies]

    # Pré-charger progression et scores en bulk
    progressions = dict(
        UserProgression.objects.filter(user_id__in=eleves_ids)
        .values("user_id")
        .annotate(
            total=Count("id"),
            terminees=Count("id", filter=Q(statut="termine")),
        )
        .values_list("user_id", "total", "terminees")
        .iterator()
    ) if eleves_ids else {}

    scores = dict(
        UserQuizResultat.objects.filter(user_id__in=eleves_ids)
        .values("user_id")
        .annotate(score_moyen=Avg("meilleur_score"))
        .values_list("user_id", "score_moyen")
    ) if eleves_ids else {}

    for lien in eleves_lies:
        eleve = lien.eleve
        prog_data = progressions.get(eleve.id)
        total = prog_data[0] if prog_data else 0
        terminees = prog_data[1] if prog_data else 0
        progression_pct = round(terminees / total * 100) if total else 0

        tableau_eleves.append({
            "eleve": eleve,
            "niveau": eleve.get_niveau_display() if eleve.niveau else "—",
            "progression_pct": progression_pct,
            "score_moyen": round(scores.get(eleve.id, (0,))[0] or 0),
            "derniere_connexion": eleve.last_login,
            "streak": getattr(eleve, "streak_jours", 0),
        })

    # Graphique activité 30 jours (1 requête avec TruncDate)
    il_y_a_30j = timezone.now() - timedelta(days=30)
    activite_30j = list(
        UserProgression.objects.filter(
            user_id__in=eleves_ids,
            mis_a_jour_le__gte=il_y_a_30j,
        )
        .annotate(jour=TruncDate("mis_a_jour_le"))
        .values("jour")
        .annotate(count=Count("id"))
        .order_by("jour")
    )

    return render(request, "dashboard/enseignant.html", {
        "demandes_en_attente": demandes_en_attente,
        "messages_non_lus": messages_non_lus,
        "stats_classe": stats_classe,
        "tableau_eleves": tableau_eleves,
        "activite_30j": activite_30j,
    })
```

#### Template `dashboard/enseignant.html`

Structure du template (extends `base.html`, block `content`) :

1. **Bandeau résumé** : 4 cartes (nb élèves liés, demandes en attente avec lien, messages non lus avec lien, leçons terminées/semaine)
2. **Vue d'ensemble classe** : progression moyenne (barre), score moyen (barre)
3. **Tableau élèves** : colonnes Nom, Niveau, Progression %, Score moyen, Dernière connexion, Streak — chaque ligne cliquable → fiche élève
4. **Graphique activité 30 jours** : Chart.js bar chart avec données `activite_30j`

#### 🎯 Critères d'acceptation

- `_dashboard_enseignant(request)` retourne un rendu `dashboard/enseignant.html` avec status 200
- Le template affiche les données correctes : nb élèves liés (validés uniquement), demandes en attente, messages non lus
- Le tableau élèves contient une ligne par élève lié (statut validé) avec nom, niveau, progression %, score moyen, dernière connexion, streak
- Le graphique 30 jours affiche l'activité agrégée par jour via Chart.js
- Un enseignant sans élèves liés voit un état vide avec message d'invitation ("Aucun élève lié. Partagez votre code…")
- Un enseignant avec demandes en attente voit un badge sur la carte "Demandes"
- Chaque ligne du tableau est cliquable → redirige vers `fiche_eleve` (étape 4.4)

#### 🏗 Architecture

- `_calculs_stats_classe(enseignant)` dans `users/helpers.py` — DRY, réutilisable
- `select_related("eleve")` sur `LienEnseignantEleve` pour éviter N+1
- Progression et scores pré-chargés en bulk (2 requêtes annotées) au lieu de N requêtes par élève
- `TruncDate("mis_a_jour_le")` pour le graphique — 1 seule requête pour 30 jours d'activité
- Les compteurs `messages_non_lus` et `demandes_en_attente` sont des requêtes simples (COUNT) avec index existants

#### 🔒 Sécurité

- Seul un enseignant peut accéder à ce dashboard (routing par rôle dans 4.1)
- Le tableau ne montre que les élèves liés au `request.user` (filtre `enseignant=request.user`)
- Pas d'emails d'élèves affichés dans le tableau — seulement nom, niveau, progression, score
- Preview mode : `_dashboard_enseignant` ne sera jamais appelé en preview car le routeur utilise le rôle réel, pas le rôle simulé

#### ⚡ Performance

- Budget : **≤ 12 requêtes SQL**
  - 1 : auth/session
  - 1 : demandes en attente (COUNT)
  - 1 : messages non lus (COUNT)
  - 1 : IDs élèves liés
  - 1 : progressions agrégées par élève
  - 1 : scores agrégés par élève
  - 1 : stats classe (helper)
  - 1 : activité 30j (TruncDate)
  - ≤ 4 : overhead Django (CSRF, session save, etc.)
- `prefetch_related` / `select_related` sur tous les FK accédés
- Pas de boucle N+1 grâce au pré-chargement bulk

#### ✅ Definition of Done

- [ ] `_dashboard_enseignant(request)` implémenté dans `users/views.py`
- [ ] `_calculs_stats_classe(enseignant)` implémenté dans `users/helpers.py`
- [ ] Template `dashboard/enseignant.html` créé avec les 4 sections
- [ ] Graphique Chart.js 30j fonctionnel
- [ ] État vide géré (aucun élève lié)
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 3.2, 5, 8 mises à jour

---

### Étape 4.3 — Dashboard parent

**Fichiers** : `users/views.py`, `templates/dashboard/parent.html`

#### Vue

```python
# users/views.py

def _dashboard_parent(request):
    """Dashboard parent : carte par enfant, détails, graphique 30j, messages."""
    from users.models import LienParentEleve, StatutLienChoices, Message
    from progress.models import UserProgression, UserQuizResultat
    from courses.models import Matiere
    from django.db.models.functions import TruncDate
    from django.db.models import Avg, Count, Q

    parent = request.user

    # Messages non lus
    messages_non_lus = Message.objects.filter(
        conversation__participants=parent, lu=False
    ).exclude(auteur=parent).count()

    # Enfants liés (validés uniquement)
    liens_enfants = (
        LienParentEleve.objects
        .filter(parent=parent, statut=StatutLienChoices.VALIDE)
        .select_related("eleve")
    )

    enfants_data = []
    il_y_a_30j = timezone.now() - timedelta(days=30)

    for lien in liens_enfants:
        enfant = lien.eleve

        # Progression globale
        prog = UserProgression.objects.filter(user=enfant).aggregate(
            total=Count("id"),
            terminees=Count("id", filter=Q(statut="termine")),
        )
        progression_pct = 0
        if prog["total"]:
            progression_pct = round(prog["terminees"] / prog["total"] * 100)

        # Scores par matière
        matieres = Matiere.objects.all()
        notes_par_matiere = []
        for matiere in matieres:
            score = UserQuizResultat.objects.filter(
                user=enfant,
                quiz__lecon__chapitre__matiere=matiere,
            ).aggregate(moy=Avg("meilleur_score"))
            notes_par_matiere.append({
                "matiere": matiere.nom,
                "score": round(score["moy"] or 0),
            })

        # Points forts (>80%) et points faibles (<60%)
        chapitres_scores = (
            UserQuizResultat.objects.filter(user=enfant)
            .values("quiz__lecon__chapitre__titre")
            .annotate(moy=Avg("meilleur_score"))
        )
        points_forts = [
            c for c in chapitres_scores if (c["moy"] or 0) > 80
        ][:5]
        points_faibles = [
            c for c in chapitres_scores if (c["moy"] or 0) < 60
        ][:5]

        # Graphique 30 jours par enfant
        activite_30j = list(
            UserProgression.objects.filter(
                user=enfant,
                mis_a_jour_le__gte=il_y_a_30j,
            )
            .annotate(jour=TruncDate("mis_a_jour_le"))
            .values("jour")
            .annotate(count=Count("id"))
            .order_by("jour")
        )

        enfants_data.append({
            "enfant": enfant,
            "niveau": enfant.get_niveau_display() if enfant.niveau else "—",
            "progression_pct": progression_pct,
            "derniere_connexion": enfant.last_login,
            "streak": getattr(enfant, "streak_jours", 0),
            "score_global": round(
                UserQuizResultat.objects.filter(user=enfant)
                .aggregate(moy=Avg("meilleur_score"))["moy"] or 0
            ),
            "notes_par_matiere": notes_par_matiere,
            "points_forts": points_forts,
            "points_faibles": points_faibles,
            "activite_30j": activite_30j,
        })

    return render(request, "dashboard/parent.html", {
        "messages_non_lus": messages_non_lus,
        "enfants_data": enfants_data,
    })
```

#### Template `dashboard/parent.html`

Structure du template (extends `base.html`, block `content`) :

1. **Bandeau** : messages non lus (avec lien), nombre d'enfants liés
2. **Carte par enfant** : nom, niveau, progression globale (barre), dernière connexion, streak, score global
3. **Section détaillée par enfant** (Alpine.js toggle) :
   - Dernières connexions (date `last_login`)
   - Notes par matière (barres de couleur selon le subject colour system)
   - Points forts (top 5, score > 80%) — badge vert
   - Points faibles (top 5, score < 60%) — badge rouge
   - Graphique 30 jours (Chart.js line chart)
4. **Lien vers fiche élève** pour chaque enfant (étape 4.4)

#### 🎯 Critères d'acceptation

- `_dashboard_parent(request)` retourne un rendu `dashboard/parent.html` avec status 200
- Le template affiche une carte par enfant lié (validé uniquement)
- Chaque carte montre : nom, niveau, progression %, dernière connexion, streak, score global
- La section détaillée affiche : notes par matière (avec couleurs physique=bleu, chimie=emerald, maths=violet), points forts > 80%, points faibles < 60%, graphique 30j
- Un parent sans enfant lié voit un état vide ("Aucun enfant lié. Utilisez le code de votre enfant…")
- Le parent ne voit **jamais** les emails de ses enfants — uniquement nom, prénom, niveau
- Le parent ne voit **jamais** les données d'enfants d'autres parents
- Le badge "messages non lus" est affiché si > 0

#### 🏗 Architecture

- La boucle sur les enfants est acceptable car un parent a max 2 enfants liés (contrainte modèle Phase 1)
- Notes par matière : itération sur `Matiere.objects.all()` (3 matières) × 2 enfants max = 6 requêtes — acceptable vu la cardinalité fixe
- Points forts/faibles : agrégation par chapitre avec annotation `Avg` — une requête par enfant
- Graphique 30 jours : `TruncDate` — une requête par enfant
- Total estimé : ≤ 12 requêtes pour 2 enfants (dans le budget dashboard)

#### 🔒 Sécurité

- Seul un parent peut accéder à ce dashboard (routing par rôle dans 4.1)
- Le queryset filtre `parent=request.user, statut=VALIDE` — impossible de voir les enfants d'un autre parent
- **Pas d'emails** affichés dans le template — ni ceux des enfants, ni ceux d'autres parents
- **Pas de données croisées** : un parent ne voit que ses propres enfants, jamais les enfants d'un autre parent même s'ils partagent un enseignant
- Preview mode non applicable (un admin en preview simule un élève, pas un parent)

#### ⚡ Performance

- Budget : **≤ 12 requêtes SQL** (pour max 2 enfants)
  - 1 : auth/session
  - 1 : messages non lus (COUNT)
  - 1 : liens enfants (avec select_related)
  - Par enfant (× 2 max) :
    - 1 : progression agrégée
    - 1 : score global
    - 1 : notes par matière (3 sous-requêtes)
    - 1 : chapitres scores (points forts/faibles)
    - 1 : activité 30j (TruncDate)
- La cardinalité fixe (max 2 enfants, 3 matières) garantit que le budget est respecté

#### ✅ Definition of Done

- [ ] `_dashboard_parent(request)` implémenté dans `users/views.py`
- [ ] Template `dashboard/parent.html` créé avec carte + section détaillée par enfant
- [ ] Subject colour system respecté (bleu/emerald/violet)
- [ ] Graphiques Chart.js 30j par enfant fonctionnels
- [ ] État vide géré (aucun enfant lié)
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 3.2, 5 mises à jour

---

### Étape 4.4 — Fiche élève complète

**Fichiers** : `users/helpers.py`, `users/views.py`, `users/urls.py`, `templates/dashboard/fiche_eleve.html`

#### Helper `peut_voir_eleve`

```python
# users/helpers.py

def peut_voir_eleve(user, eleve):
    """Vérifie si user a le droit de consulter la fiche de eleve.

    Retourne True si :
    - user est admin
    - user est enseignant lié validé à eleve
    - user est parent lié validé à eleve
    Retourne False sinon.
    """
    from users.models import (
        RoleChoices, LienEnseignantEleve, LienParentEleve, StatutLienChoices,
    )

    if user.role == RoleChoices.ADMIN:
        return True

    if user.role == RoleChoices.ENSEIGNANT:
        return LienEnseignantEleve.objects.filter(
            enseignant=user, eleve=eleve, statut=StatutLienChoices.VALIDE
        ).exists()

    if user.role == RoleChoices.PARENT:
        return LienParentEleve.objects.filter(
            parent=user, eleve=eleve, statut=StatutLienChoices.VALIDE
        ).exists()

    return False
```

#### Vue

```python
# users/views.py

@login_required
def fiche_eleve_view(request, eleve_id):
    """Fiche détaillée d'un élève — accessible par admin, enseignant lié, parent lié."""
    from users.helpers import peut_voir_eleve
    from users.models import LienEnseignantEleve, LienParentEleve, StatutLienChoices
    from progress.models import (
        UserProgression, UserQuizResultat, UserQuestionHistorique,
    )
    from courses.models import Matiere
    from django.db.models import Avg, Count, Q
    from django.db.models.functions import TruncDate

    eleve = get_object_or_404(CustomUser, pk=eleve_id, role=RoleChoices.ELEVE)

    if not peut_voir_eleve(request.user, eleve):
        return HttpResponseForbidden()

    # === Section 1 : Identité ===
    identite = {
        "nom_complet": eleve.nom_complet,
        "niveau": eleve.get_niveau_display() if eleve.niveau else "—",
        "code_identifiant": eleve.code_identifiant,
        "date_inscription": eleve.date_joined,
        "derniere_connexion": eleve.last_login,
    }

    # === Section 2 : Relations ===
    enseignant_lie = (
        LienEnseignantEleve.objects
        .filter(eleve=eleve, statut=StatutLienChoices.VALIDE)
        .select_related("enseignant")
        .first()
    )
    parents_lies = (
        LienParentEleve.objects
        .filter(eleve=eleve, statut=StatutLienChoices.VALIDE)
        .select_related("parent")
    )

    # === Section 3 : Heatmap connexions 90 jours (1 requête) ===
    il_y_a_90j = timezone.now() - timedelta(days=90)
    connexions_90j = list(
        UserProgression.objects.filter(
            user=eleve,
            mis_a_jour_le__gte=il_y_a_90j,
        )
        .annotate(jour=TruncDate("mis_a_jour_le"))
        .values("jour")
        .annotate(count=Count("id"))
        .order_by("jour")
    )

    # === Section 4 : Notes et scores par matière (1 requête agrégée) ===
    matieres = Matiere.objects.all()
    scores_par_matiere = []
    for matiere in matieres:
        score = UserQuizResultat.objects.filter(
            user=eleve,
            quiz__lecon__chapitre__matiere=matiere,
        ).aggregate(moy=Avg("meilleur_score"))
        scores_par_matiere.append({
            "matiere": matiere,
            "score": round(score["moy"] or 0),
        })

    # === Section 5 : Points forts (top 5 > 80%) ===
    chapitres_scores = list(
        UserQuizResultat.objects.filter(user=eleve)
        .values(
            "quiz__lecon__chapitre__id",
            "quiz__lecon__chapitre__titre",
            "quiz__lecon__chapitre__matiere__nom",
        )
        .annotate(moy=Avg("meilleur_score"))
        .order_by("-moy")
    )
    points_forts = [c for c in chapitres_scores if (c["moy"] or 0) > 80][:5]

    # === Section 6 : Points faibles (bottom 5 < 60% + Leitner box=1) ===
    points_faibles = [c for c in chapitres_scores if (c["moy"] or 0) < 60][:5]
    questions_leitner_box1 = (
        UserQuestionHistorique.objects
        .filter(user=eleve, boite_leitner=1)
        .select_related("question")
        .order_by("-derniere_reponse_le")[:10]
    )

    # === Section 7 : Progression par matière (barres) ===
    progression_par_matiere = []
    for matiere in matieres:
        prog = UserProgression.objects.filter(
            user=eleve,
            lecon__chapitre__matiere=matiere,
        ).aggregate(
            total=Count("id"),
            terminees=Count("id", filter=Q(statut="termine")),
        )
        total = prog["total"] or 0
        terminees = prog["terminees"] or 0
        progression_par_matiere.append({
            "matiere": matiere,
            "total": total,
            "terminees": terminees,
            "pct": round(terminees / total * 100) if total else 0,
        })

    return render(request, "dashboard/fiche_eleve.html", {
        "eleve": eleve,
        "identite": identite,
        "enseignant_lie": enseignant_lie,
        "parents_lies": parents_lies,
        "connexions_90j": connexions_90j,
        "scores_par_matiere": scores_par_matiere,
        "points_forts": points_forts,
        "points_faibles": points_faibles,
        "questions_leitner_box1": questions_leitner_box1,
        "progression_par_matiere": progression_par_matiere,
    })
```

#### URL

```python
# users/urls.py (ajout)
path("fiche-eleve/<int:eleve_id>/", fiche_eleve_view, name="fiche_eleve"),
```

#### Template `dashboard/fiche_eleve.html`

Structure du template (extends `base.html`, block `content`) — **7 sections** :

1. **Identité** : nom complet, niveau, code identifiant, date inscription, dernière connexion
2. **Relations** : enseignant lié (nom, ou "Aucun — rattaché à l'administrateur"), parents liés (noms, max 2)
3. **Connexions** : heatmap 90 jours (grid CSS 7×13 colonnes, couleur par intensité via Alpine.js)
4. **Notes / Scores** : gauge Chart.js (doughnut) par matière + score numérique, couleurs selon subject colour system
5. **Points forts** : top 5 chapitres > 80% — badge vert, nom chapitre, matière, score
6. **Points faibles** : bottom 5 chapitres < 60% — badge rouge, nom chapitre, matière, score + liste questions Leitner box=1 (texte question, date dernière réponse)
7. **Progression** : barres horizontales par matière (terminées / total leçons), couleurs subject colour system

#### 🎯 Critères d'acceptation

- `GET /fiche-eleve/42/` avec un admin connecté → 200, fiche complète
- `GET /fiche-eleve/42/` avec l'enseignant lié validé à l'élève 42 → 200
- `GET /fiche-eleve/42/` avec un parent lié validé à l'élève 42 → 200
- `GET /fiche-eleve/42/` avec un enseignant **non** lié à l'élève 42 → 403
- `GET /fiche-eleve/42/` avec un parent **non** lié à l'élève 42 → 403
- `GET /fiche-eleve/42/` avec un élève connecté (même l'élève 42 lui-même) → 403
- `GET /fiche-eleve/42/` anonyme → redirect vers login
- `GET /fiche-eleve/99999/` (ID inexistant) → 404
- `GET /fiche-eleve/42/` où user 42 est un enseignant (pas un élève) → 404
- Les 7 sections sont affichées avec les bonnes données
- Le subject colour system est respecté pour les barres et gauges
- La heatmap 90j affiche les jours avec activité vs sans activité
- Les questions Leitner box=1 sont limitées à 10

#### 🏗 Architecture

- `peut_voir_eleve(user, eleve)` dans `users/helpers.py` — réutilisé par les dashboards et la messagerie (Phase 5)
- La vue effectue au maximum **8 requêtes SQL** pour les calculs lourds :
  - 1 : élève (get_object_or_404)
  - 1 : enseignant lié
  - 1 : parents liés
  - 1 : connexions 90j (TruncDate)
  - 1 : chapitres scores (agrégation pour points forts/faibles)
  - 1 : questions Leitner box=1
  - 2 : scores + progression par matière (3 itérations × 2 — cardinalité fixe)
- `get_object_or_404(CustomUser, pk=eleve_id, role=RoleChoices.ELEVE)` → retourne 404 si l'ID ne correspond pas à un élève (pas de leak d'existence d'autres rôles)
- La heatmap est rendue côté serveur en HTML/CSS (grid 7×13) avec Alpine.js pour les tooltips — pas de lib JS externe

#### 🔒 Sécurité

- **IDOR** : `peut_voir_eleve(request.user, eleve)` vérifie le lien validé — un enseignant/parent ne peut voir que les fiches de ses élèves/enfants
- **Broken Access Control** : un élève ne peut pas accéder aux fiches (même la sienne) — la fiche est réservée aux superviseurs
- **Information Disclosure** : les emails ne sont affichés nulle part dans la fiche. Les noms des parents liés à l'élève ne montrent pas les emails des autres parents. Un parent voit "Parent 1 : Mme X" et "Parent 2 : M. Y" mais pas leurs emails
- **Enumeration** : `get_object_or_404` avec filtre `role=ELEVE` → un ID d'enseignant ou parent retourne 404 (pas 403)

#### ⚡ Performance

- Budget : **≤ 8 requêtes SQL** principales (hors auth/session/CSRF overhead)
- `select_related("enseignant")` et `select_related("parent")` sur les liens
- `select_related("question")` sur les questions Leitner
- Cardinalité fixe pour les matières (3) → pas de pagination nécessaire
- Questions Leitner box=1 limitées à 10 (slice queryset)

#### ✅ Definition of Done

- [ ] `peut_voir_eleve(user, eleve)` implémenté dans `users/helpers.py`
- [ ] `fiche_eleve_view(request, eleve_id)` implémenté dans `users/views.py`
- [ ] URL `fiche_eleve` enregistrée dans `users/urls.py`
- [ ] Template `dashboard/fiche_eleve.html` créé avec les 7 sections
- [ ] Heatmap 90j fonctionnelle (CSS grid + Alpine.js tooltips)
- [ ] Gauges Chart.js par matière fonctionnelles
- [ ] Tests d'accès passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 2.2, 3.2, 5, 8 mises à jour

---

### Étape 4.5 — Adaptation dashboard élève

**Fichier** : `users/views.py` → `_dashboard_eleve(request)`, `templates/dashboard/eleve.html`

#### Modifications sur `_dashboard_eleve`

Ajouter au contexte existant :

```python
# Dans _dashboard_eleve(request), ajouter au contexte :
from users.models import (
    LienEnseignantEleve, LienParentEleve,
    StatutLienChoices, Notification,
)

eleve = request.user

# Enseignant lié
enseignant_lie = (
    LienEnseignantEleve.objects
    .filter(eleve=eleve, statut=StatutLienChoices.VALIDE)
    .select_related("enseignant")
    .first()
)

# Parents liés
parents_lies = (
    LienParentEleve.objects
    .filter(eleve=eleve, statut=StatutLienChoices.VALIDE)
    .select_related("parent")
)

# Code identifiant de l'élève (pour partager)
code_identifiant = eleve.code_identifiant

# Notifications non lues (badge)
nb_notifications = Notification.objects.filter(
    destinataire=eleve, lue=False
).count()

# Ajouter au contexte du render :
# "enseignant_lie": enseignant_lie,
# "parents_lies": parents_lies,
# "code_identifiant": code_identifiant,
# "nb_notifications": nb_notifications,
```

#### Modifications sur `templates/dashboard/eleve.html`

Ajouter 3 sections au template existant :

1. **Section "Mes enseignants"** : nom de l'enseignant lié (ou "Aucun enseignant lié — vous êtes en mode libre"). Si pas d'enseignant → suggestion "Demandez un code à votre enseignant"
2. **Section "Mes parents"** : liste des parents liés (noms uniquement, pas d'emails). Si aucun → suggestion "Partagez votre code avec vos parents"
3. **Code identifiant** : affichage du code avec bouton copier (Alpine.js `navigator.clipboard.writeText()`) + texte "Partagez ce code avec vos parents pour qu'ils puissent suivre votre progression"
4. **Badge notifications** : compteur dans le bandeau supérieur si `nb_notifications > 0`

#### 🎯 Critères d'acceptation

- Le dashboard élève existant continue de fonctionner sans régression (progress bars, streak, trend, revision CTA, weak chapters)
- La section "Mes enseignants" affiche le nom de l'enseignant lié validé, ou un message d'état vide
- La section "Mes parents" affiche les noms des parents liés validés (max 2), ou un message d'état vide
- Le code identifiant est affiché avec un bouton copier fonctionnel
- Le badge notifications affiche le nombre de notifications non lues si > 0
- Les emails de l'enseignant et des parents ne sont **jamais** affichés

#### 🏗 Architecture

- On ajoute au contexte existant de `_dashboard_eleve` — pas de refactoring du code existant
- Les 4 nouvelles requêtes sont légères (2 × EXISTS/COUNT + 1 SELECT + 1 COUNT) — restent dans le budget 12 requêtes du dashboard
- Le bouton copier utilise Alpine.js inline (pas de fichier JS externe) : `@click="navigator.clipboard.writeText('{{ code_identifiant }}')"` avec feedback visuel

#### 🔒 Sécurité

- Pas d'emails affichés — seulement les noms des enseignants/parents liés
- Le code identifiant est public par design (prévu pour être partagé) — pas d'information sensible
- Preview mode : les données de relations sont affichées **en lecture seule** — aucune écriture en preview mode

#### ⚡ Performance

- +4 requêtes sur le dashboard existant. Budget total dashboard élève estimé à ≤ 12 requêtes (existant ~8 + 4 nouvelles)
- `select_related("enseignant")` et `select_related("parent")` pour éviter N+1

#### ✅ Definition of Done

- [ ] `_dashboard_eleve(request)` mis à jour avec les 4 nouvelles variables de contexte
- [ ] Template `dashboard/eleve.html` mis à jour avec les 3 nouvelles sections + badge
- [ ] Bouton copier code identifiant fonctionnel (Alpine.js)
- [ ] Aucune régression sur le dashboard existant
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 3.2, 5 mises à jour

---

### Étape 4.6 — Adaptation sidebar `base.html`

**Fichier** : `templates/base.html`

#### Navigation conditionnelle par rôle

La sidebar actuelle affiche des liens pour les élèves et admins. On la rend conditionnelle par rôle :

```html
{# === Navigation commune (tous rôles authentifiés) === #}
<a href="{% url 'tableau_de_bord' %}">Tableau de bord</a>

{# === Navigation Élève === #}
{% if user.is_eleve %}
  <a href="{% url 'matieres' %}">Mes matières</a>
  <a href="{% url 'revisions' %}">Révisions</a>
  <a href="{% url 'liaisons_eleve' %}">Mes liaisons</a>
  <a href="{% url 'notifications' %}">
    Notifications
    {% if nb_notifications > 0 %}
      <span class="...">{{ nb_notifications }}</span>
    {% endif %}
  </a>
{% endif %}

{# === Navigation Enseignant === #}
{% if user.is_enseignant %}
  <a href="{% url 'liaisons_enseignant' %}">Mes élèves</a>
  <a href="{% url 'ajouter_eleve' %}">Ajouter un élève</a>
  <a href="{% url 'liaisons_enseignant' %}?statut=en_attente">Demandes en attente</a>
  <a href="{% url 'notifications' %}">
    Notifications
    {% if nb_notifications > 0 %}
      <span class="...">{{ nb_notifications }}</span>
    {% endif %}
  </a>
{% endif %}

{# === Navigation Parent === #}
{% if user.is_parent %}
  <a href="{% url 'tableau_de_bord' %}">Mes enfants</a>
  <a href="{% url 'notifications' %}">
    Notifications
    {% if nb_notifications > 0 %}
      <span class="...">{{ nb_notifications }}</span>
    {% endif %}
  </a>
{% endif %}

{# === Navigation Admin (inchangée) === #}
{% if user.is_admin %}
  {# ... liens admin existants ... #}
{% endif %}
```

> **Note** : le compteur `nb_notifications` doit être injecté via le context processor existant (`users/context_processors.py`) pour être disponible sur toutes les pages, pas seulement le dashboard.

#### Modification du context processor

```python
# users/context_processors.py (ajout)

def notifications_context(request):
    """Injecte le compteur de notifications non lues pour le badge sidebar."""
    if not request.user.is_authenticated:
        return {}
    from django.core.cache import cache
    from users.models import Notification

    cache_key = f"notif_count_{request.user.id}"
    count = cache.get(cache_key)
    if count is None:
        count = Notification.objects.filter(
            destinataire=request.user, lue=False
        ).count()
        cache.set(cache_key, count, 300)  # 5 min TTL
    return {"nb_notifications": count}
```

**Enregistrement** dans `config/settings/base.py` :

```python
TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    "users.context_processors.notifications_context",
]
```

#### 🎯 Critères d'acceptation

- Un élève connecté voit : Tableau de bord, Mes matières, Révisions, Mes liaisons, Notifications (avec badge)
- Un enseignant connecté voit : Tableau de bord, Mes élèves, Ajouter un élève, Demandes en attente, Notifications (avec badge)
- Un parent connecté voit : Tableau de bord, Mes enfants, Notifications (avec badge)
- Un admin connecté voit : les liens admin existants (inchangés)
- Le badge notifications affiche le compteur si > 0, rien si 0
- Le compteur est mis en cache (5 min TTL) pour éviter un COUNT à chaque page
- La sidebar est responsive (mobile : menu burger existant)
- Navigation pour un rôle ne montre **jamais** les liens d'un autre rôle

#### 🏗 Architecture

- Context processor `notifications_context` → `nb_notifications` disponible sur toutes les pages
- Cache avec TTL 5 min — invalidation explicite dans `_invalider_cache_notifications()` (déjà implémenté en Phase 3)
- Utilisation des propriétés `is_eleve`, `is_enseignant`, `is_parent`, `is_admin` directement dans le template — pas de template tag custom
- Les liens de messagerie (`{% url 'inbox' %}`) seront ajoutés en Phase 5 quand les vues existeront

#### 🔒 Sécurité

- La sidebar filtrée par rôle est une **défense en profondeur** — les vues vérifient toujours le rôle indépendamment
- Cacher un lien dans la sidebar ne remplace pas le contrôle d'accès côté vue
- Le compteur de notifications utilise le cache — en cas de cache stale, la page notifications montre le vrai compte (pas de risque de sécurité, juste un badge décalé temporairement)
- Preview mode : la sidebar montre les liens du rôle **réel** de l'admin, pas ceux de l'élève simulé (le preview affecte le contenu des pages, pas la navigation)

#### ⚡ Performance

- Le context processor fait 1 requête COUNT **uniquement** si le cache est vide (miss)
- Cache TTL 5 min → au maximum 1 requête COUNT toutes les 5 minutes par utilisateur
- Invalidation explicite lors de la création / marquage de notifications → le compteur est toujours frais après une action

#### ✅ Definition of Done

- [ ] Sidebar `base.html` mise à jour avec navigation conditionnelle par rôle
- [ ] Context processor `notifications_context` implémenté
- [ ] Context processor enregistré dans `base.py` TEMPLATES
- [ ] Cache 5 min sur le compteur de notifications
- [ ] Badge notifications visible si > 0
- [ ] Tests sidebar passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 5, 6, 8 mises à jour

---

### 🧪 Tests — Phase 4

> **Agent responsable** : `test-writer`
> **Fichiers** : `users/tests/test_dashboard.py` (nouveau), `users/tests/test_fiche_eleve.py` (nouveau), `users/tests/conftest.py` (enrichir fixtures)
> **Nombre minimum** : 25 tests

#### Tests de routage du dashboard (4 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_dashboard_routage_admin_template_admin` | `admin_user` | `assertTemplateUsed(response, "dashboard/admin.html")` |
| 2 | `test_dashboard_routage_enseignant_template_enseignant` | `enseignant` | `assertTemplateUsed(response, "dashboard/enseignant.html")` |
| 3 | `test_dashboard_routage_parent_template_parent` | `parent_user` | `assertTemplateUsed(response, "dashboard/parent.html")` |
| 4 | `test_dashboard_routage_eleve_template_eleve` | `eleve` | `assertTemplateUsed(response, "dashboard/eleve.html")` |

#### Tests d'accès fiche élève (7 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 5 | `test_fiche_eleve_acces_admin_200` | `admin_user`, `eleve` | `assertEqual(response.status_code, 200)` |
| 6 | `test_fiche_eleve_acces_enseignant_lie_200` | `enseignant`, `lien_enseignant_eleve_valide` | `assertEqual(response.status_code, 200)` |
| 7 | `test_fiche_eleve_acces_parent_lie_200` | `parent_user`, `lien_parent_eleve_valide` | `assertEqual(response.status_code, 200)` |
| 8 | `test_fiche_eleve_acces_enseignant_non_lie_403` | `enseignant2`, `eleve` | `assertEqual(response.status_code, 403)` |
| 9 | `test_fiche_eleve_acces_parent_non_lie_403` | `parent_user2`, `eleve` | `assertEqual(response.status_code, 403)` |
| 10 | `test_fiche_eleve_acces_eleve_403` | `eleve`, `eleve` (himself) | `assertEqual(response.status_code, 403)` |
| 11 | `test_fiche_eleve_acces_anonyme_redirect_login` | — | `assertEqual(response.status_code, 302)` |

#### Tests helper `peut_voir_eleve` (5 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 12 | `test_peut_voir_eleve_admin_true` | `admin_user`, `eleve` | `assertTrue(peut_voir_eleve(admin, eleve))` |
| 13 | `test_peut_voir_eleve_enseignant_lie_true` | `enseignant`, `lien_valide` | `assertTrue(peut_voir_eleve(enseignant, eleve))` |
| 14 | `test_peut_voir_eleve_parent_lie_true` | `parent_user`, `lien_valide` | `assertTrue(peut_voir_eleve(parent, eleve))` |
| 15 | `test_peut_voir_eleve_enseignant_non_lie_false` | `enseignant2`, `eleve` | `assertFalse(peut_voir_eleve(enseignant2, eleve))` |
| 16 | `test_peut_voir_eleve_eleve_false` | `eleve`, `eleve` | `assertFalse(peut_voir_eleve(eleve, eleve))` |

#### Tests données affichées (4 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 17 | `test_dashboard_enseignant_affiche_nb_eleves` | `enseignant`, `lien_valide` | `assertContains(response, "1")` (nb élèves) |
| 18 | `test_dashboard_enseignant_sans_eleves_etat_vide` | `enseignant` (sans lien) | `assertContains(response, "Aucun élève")` |
| 19 | `test_dashboard_parent_affiche_carte_enfant` | `parent_user`, `lien_valide` | `assertContains(response, eleve.nom_complet)` |
| 20 | `test_dashboard_parent_sans_enfant_etat_vide` | `parent_user` (sans lien) | `assertContains(response, "Aucun enfant")` |

#### Tests sidebar conditionnelle (4 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 21 | `test_sidebar_eleve_contient_lien_matieres` | `eleve` | `assertContains(response, "Mes matières")` |
| 22 | `test_sidebar_enseignant_contient_lien_eleves` | `enseignant` | `assertContains(response, "Mes élèves")` |
| 23 | `test_sidebar_parent_contient_lien_enfants` | `parent_user` | `assertContains(response, "Mes enfants")` |
| 24 | `test_sidebar_enseignant_ne_contient_pas_lien_matieres` | `enseignant` | `assertNotContains(response, "Mes matières")` |

#### Tests IDOR et sécurité (2 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 25 | `test_fiche_eleve_idor_enseignant_autre_eleve_403` | `enseignant`, `eleve_de_enseignant2` | `assertEqual(response.status_code, 403)` |
| 26 | `test_fiche_eleve_id_non_eleve_404` | `admin_user`, `enseignant` (ID d'un enseignant) | `assertEqual(response.status_code, 404)` |

**Fixtures à ajouter dans `conftest.py`** :

```python
@pytest.fixture
def enseignant2(db):
    return CustomUser.objects.create_user(
        email="ens2@test.com", prenom="Marie", nom="Martin",
        role="enseignant", password="test1234",
    )

@pytest.fixture
def parent_user2(db):
    return CustomUser.objects.create_user(
        email="par2@test.com", prenom="Jean", nom="Petit",
        role="parent", password="test1234",
    )

@pytest.fixture
def lien_enseignant_eleve_valide(enseignant, eleve):
    return LienEnseignantEleve.objects.create(
        enseignant=enseignant, eleve=eleve, statut="valide",
    )

@pytest.fixture
def lien_parent_eleve_valide(parent_user, eleve):
    return LienParentEleve.objects.create(
        parent=parent_user, eleve=eleve, statut="valide",
    )
```

---

### Résumé des changements par fichier — Phase 4

| Fichier | Action |
|---------|--------|
| `users/views.py` | Modifier `TableauDeBordView.get()` (routeur 4 branches), ajouter `_dashboard_enseignant`, `_dashboard_parent`, `fiche_eleve_view`, enrichir `_dashboard_eleve` |
| `users/helpers.py` | Ajouter `peut_voir_eleve()`, `_calculs_stats_classe()` |
| `users/urls.py` | Ajouter URL `fiche_eleve` |
| `users/context_processors.py` | Ajouter `notifications_context()` |
| `config/settings/base.py` | Ajouter `notifications_context` au context processors |
| `templates/dashboard/enseignant.html` | **Nouveau** — dashboard enseignant avec stats + tableau + graphique 30j |
| `templates/dashboard/parent.html` | **Nouveau** — dashboard parent avec cartes enfants + détails + graphique 30j |
| `templates/dashboard/fiche_eleve.html` | **Nouveau** — fiche élève 7 sections (identité, relations, heatmap, scores, forts, faibles, progression) |
| `templates/dashboard/eleve.html` | Enrichir avec sections enseignants/parents/code/badge |
| `templates/base.html` | Sidebar conditionnelle par rôle |
| `users/tests/conftest.py` | Ajouter fixtures `enseignant2`, `parent_user2`, `lien_*_valide` |
| `users/tests/test_dashboard.py` | **Nouveau** — 12+ tests dashboards (délégué à `test-writer`) |
| `users/tests/test_fiche_eleve.py` | **Nouveau** — 14+ tests fiche élève + helper (délégué à `test-writer`) |
| `CODEBASE_REFERENCE.md` | Sections 2.2 (URLs), 3.2 (Views), 5 (Templates), 6 (Settings), 8 (Patterns) mises à jour |

### Ordre d'exécution recommandé

```
1. Implementer  → Étape 4.1 (routeur dashboard par rôle)
2. Implementer  → Étape 4.2 (dashboard enseignant + helper stats classe)
3. Implementer  → Étape 4.3 (dashboard parent)
4. Implementer  → Étape 4.4 (fiche élève + helper peut_voir_eleve)
5. Implementer  → Étape 4.5 (adaptation dashboard élève)
6. Implementer  → Étape 4.6 (sidebar conditionnelle + context processor)
7. Test Writer  → 25+ tests dans users/tests/test_dashboard.py + test_fiche_eleve.py
8. Implementer  → Mise à jour CODEBASE_REFERENCE.md
```

---

## Phase 5 — Messagerie

> **Objectif** : implémenter la messagerie interne entre utilisateurs liés (enseignant↔élève, enseignant↔parent, admin↔tous). Les modèles `Conversation` et `Message` existent déjà (Phase 1). Cette phase ajoute les règles d'accès, les vues, les templates HTMX et les notifications de message. Aucun nouveau modèle — on utilise les modèles créés en Phase 1.

### Décisions d'architecture (Phase 5)

| Décision | Justification |
|----------|---------------|
| `contacts_autorises(user)` dans `users/helpers.py` | Fonction pure, réutilisable par les vues messagerie et potentiellement par d'autres features. Retourne un QuerySet (pas de boucle Python) pour performance et chaînabilité |
| Tout reste dans `users/` | `Conversation` + `Message` = 2 modèles, en dessous du seuil de 3 pour créer une app dédiée. Les vues messagerie accèdent aux mêmes liens (`LienEnseignantEleve`, `LienParentEleve`) que les autres vues `users/` |
| Fragment HTMX `_message_item.html` | Un seul fragment réutilisé par (1) le rendu initial de la conversation, (2) l'insertion HTMX après envoi, (3) le polling des nouveaux messages. DRY et cache-friendly |
| Polling `hx-trigger="every 5s"` plutôt que WebSocket | Simplicité d'infrastructure — pas de Channels/Redis à ajouter. 5s est un bon compromis entre réactivité et charge serveur pour le volume attendu (< 100 utilisateurs simultanés). Migration vers WebSocket possible en Phase 6+ si nécessaire |
| `strip_tags()` + `escape()` sur le contenu | Double protection XSS : `strip_tags()` supprime le HTML, `escape()` encode les caractères spéciaux restants. Appliqué dans le service avant `save()`, pas dans le template (défense en profondeur) |
| Rate limit 30 msg/h par utilisateur | Empêche le spam sans gêner l'usage normal. Implémenté via cache (`msg_rate_{user_id}`) sur le même pattern que `_check_quiz_rate_limit()` |
| Email optionnel si déconnecté > 5 min | Vérifié via `user.last_login` ou cache `last_seen_{user_id}`. Configurable par l'utilisateur en Phase 6+ (préférences). Pour le MVP, envoi systématique si déconnecté > 5 min |

---

### Étape 5.1 — Règles d'accès et helper `contacts_autorises`

**Fichier** : `users/helpers.py`

```python
from django.db.models import Q
from users.models import (
    CustomUser, RoleChoices, LienEnseignantEleve,
    LienParentEleve, StatutLienChoices,
)


def contacts_autorises(user):
    """Retourne le QuerySet des utilisateurs que `user` peut contacter."""
    if user.role == RoleChoices.ADMIN:
        return CustomUser.objects.exclude(pk=user.pk)

    if user.role == RoleChoices.ENSEIGNANT:
        # Ses élèves liés validés
        eleve_ids = LienEnseignantEleve.objects.filter(
            enseignant=user, statut=StatutLienChoices.VALIDE,
        ).values_list("eleve_id", flat=True)
        # Parents liés validés de ses élèves
        parent_ids = LienParentEleve.objects.filter(
            eleve_id__in=eleve_ids, statut=StatutLienChoices.VALIDE,
        ).values_list("parent_id", flat=True)
        return CustomUser.objects.filter(
            Q(pk__in=eleve_ids) | Q(pk__in=parent_ids)
        )

    if user.role == RoleChoices.PARENT:
        # Ses enfants liés validés
        enfant_ids = LienParentEleve.objects.filter(
            parent=user, statut=StatutLienChoices.VALIDE,
        ).values_list("eleve_id", flat=True)
        # Enseignants liés validés de ses enfants
        enseignant_ids = LienEnseignantEleve.objects.filter(
            eleve_id__in=enfant_ids, statut=StatutLienChoices.VALIDE,
        ).values_list("enseignant_id", flat=True)
        return CustomUser.objects.filter(pk__in=enseignant_ids)

    if user.role == RoleChoices.ELEVE:
        # Ses enseignants liés validés
        enseignant_ids = LienEnseignantEleve.objects.filter(
            eleve=user, statut=StatutLienChoices.VALIDE,
        ).values_list("enseignant_id", flat=True)
        return CustomUser.objects.filter(pk__in=enseignant_ids)

    return CustomUser.objects.none()
```

**Règles d'accès** :

| Rôle | Peut contacter |
|------|----------------|
| Admin | Tous les utilisateurs |
| Enseignant | Ses élèves liés validés + parents liés validés de ses élèves |
| Parent | Enseignants liés validés de ses enfants |
| Élève | Ses enseignants liés validés |

#### 🎯 Critères d'acceptation

- `contacts_autorises(enseignant)` retourne un QuerySet contenant ses élèves liés validés + parents de ses élèves liés validés
- `contacts_autorises(parent)` retourne un QuerySet contenant uniquement les enseignants de ses enfants liés validés
- `contacts_autorises(eleve)` retourne un QuerySet contenant uniquement ses enseignants liés validés
- `contacts_autorises(admin)` retourne tous les utilisateurs sauf l'admin lui-même
- Un utilisateur sans lien validé obtient un QuerySet vide (sauf admin)
- Le résultat est un QuerySet Django (pas une liste Python) — chaînable avec `.filter()`, `.count()`, etc.

#### 🏗 Architecture

- Fonction pure dans `users/helpers.py` — pas d'accès à `request`
- Utilise `values_list("x_id", flat=True)` + `Q()` pour construire le QuerySet en 2-3 requêtes SQL max (sous-requêtes IN)
- Pas de boucle Python sur les résultats
- L'admin exclut `pk=user.pk` pour éviter de se contacter lui-même

#### 🔒 Sécurité

- Seuls les liens `statut=StatutLienChoices.VALIDE` sont considérés — un lien `en_attente` ou `refuse` ne donne pas accès à la messagerie
- Un parent ne peut pas contacter un autre parent (pas dans les règles)
- Un élève ne peut pas contacter un parent (même le sien) — uniquement ses enseignants

#### ⚡ Performance

- 2-3 requêtes SQL max par appel grâce aux sous-requêtes `IN`
- Résultat chaînable — pas de matérialisation en liste

#### ✅ Definition of Done

- [ ] `contacts_autorises()` implémenté dans `users/helpers.py`
- [ ] Retourne un QuerySet (pas une liste)
- [ ] Respecte les 4 règles d'accès par rôle
- [ ] Ne retourne que les liens validés
- [ ] Tests unitaires passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` section 8 (Patterns) mise à jour

---

### Étape 5.2 — Vues messagerie

**Fichier** : `users/views.py`, `users/urls.py`

**URLs** :

| URL | Nom | Méthode | Vue |
|-----|-----|---------|-----|
| `/messages/` | `liste_conversations` | GET | `liste_conversations_view` |
| `/messages/nouveau/` | `nouvelle_conversation` | GET, POST | `nouvelle_conversation_view` |
| `/messages/<int:conversation_id>/` | `conversation_detail` | GET, POST | `conversation_detail_view` |
| `/messages/<int:conversation_id>/nouveaux/` | `nouveaux_messages` | GET | `nouveaux_messages_view` |

**Vue `liste_conversations_view`** :

```python
@login_required
def liste_conversations_view(request):
    """Liste les conversations de l'utilisateur, triées par dernier message."""
    conversations = (
        Conversation.objects.filter(participants=request.user)
        .select_related()
        .prefetch_related("messages__auteur", "participants")
        .annotate(
            dernier_message_date=Max("messages__envoye_le"),
            non_lus=Count(
                "messages",
                filter=Q(messages__lu=False) & ~Q(messages__auteur=request.user),
            ),
        )
        .order_by("-dernier_message_date")
    )
    return render(request, "users/liste_conversations.html", {
        "conversations": conversations,
    })
```

**Vue `conversation_detail_view`** :

```python
@login_required
def conversation_detail_view(request, conversation_id):
    """Affiche une conversation et permet d'envoyer un message (HTMX)."""
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    if not conversation.participants.filter(pk=request.user.pk).exists():
        return HttpResponseForbidden()

    if request.method == "POST":
        contenu = request.POST.get("contenu", "").strip()
        if not contenu:
            return HttpResponseBadRequest("Contenu vide.")
        if len(contenu) > 2000:
            return HttpResponseBadRequest("Message trop long (2000 caractères max).")
        if _check_message_rate_limit(request.user.id):
            return HttpResponse("Trop de messages envoyés. Réessayez plus tard.", status=429)

        contenu_nettoye = escape(strip_tags(contenu))
        message = Message.objects.create(
            conversation=conversation,
            auteur=request.user,
            contenu=contenu_nettoye,
        )
        conversation.save()  # Met à jour mis_a_jour_le

        # Notification pour les autres participants
        for participant in conversation.participants.exclude(pk=request.user.pk):
            Notification.objects.create(
                destinataire=participant,
                type=TypeNotificationChoices.NOUVEAU_MESSAGE,
                titre=f"Nouveau message de {request.user.nom_complet}",
                contenu=contenu_nettoye[:100],
                lien=f"/messages/{conversation.pk}/",
            )
            _envoyer_email_si_deconnecte(participant, request.user, contenu_nettoye)

        # Invalider le cache compteur non lus
        for participant in conversation.participants.exclude(pk=request.user.pk):
            cache.delete(f"msg_count_{participant.pk}")

        if request.headers.get("HX-Request"):
            return render(request, "users/_message_item.html", {"message": message})
        return redirect("conversation_detail", conversation_id=conversation.pk)

    messages_list = (
        conversation.messages
        .select_related("auteur")
        .order_by("envoye_le")
    )
    paginator = Paginator(messages_list, 50)
    page = paginator.get_page(request.GET.get("page"))

    # Marquer comme lus
    conversation.messages.filter(lu=False).exclude(
        auteur=request.user,
    ).update(lu=True)
    cache.delete(f"msg_count_{request.user.pk}")

    return render(request, "users/conversation.html", {
        "conversation": conversation,
        "messages_page": page,
    })
```

**Vue `nouvelle_conversation_view`** :

```python
@login_required
def nouvelle_conversation_view(request):
    """Formulaire pour créer une nouvelle conversation."""
    contacts = contacts_autorises(request.user)

    if request.method == "POST":
        destinataire_id = request.POST.get("destinataire")
        contenu = request.POST.get("contenu", "").strip()

        if not contenu or not destinataire_id:
            return render(request, "users/nouvelle_conversation.html", {
                "contacts": contacts,
                "erreur": "Destinataire et contenu requis.",
            })

        destinataire = get_object_or_404(CustomUser, pk=destinataire_id)
        if not contacts.filter(pk=destinataire.pk).exists():
            return HttpResponseForbidden()

        if len(contenu) > 2000:
            return render(request, "users/nouvelle_conversation.html", {
                "contacts": contacts,
                "erreur": "Message trop long (2000 caractères max).",
            })

        if _check_message_rate_limit(request.user.id):
            return HttpResponse("Trop de messages envoyés. Réessayez plus tard.", status=429)

        contenu_nettoye = escape(strip_tags(contenu))

        with transaction.atomic():
            conversation = Conversation.objects.create()
            conversation.participants.add(request.user, destinataire)
            Message.objects.create(
                conversation=conversation,
                auteur=request.user,
                contenu=contenu_nettoye,
            )
            Notification.objects.create(
                destinataire=destinataire,
                type=TypeNotificationChoices.NOUVEAU_MESSAGE,
                titre=f"Nouveau message de {request.user.nom_complet}",
                contenu=contenu_nettoye[:100],
                lien=f"/messages/{conversation.pk}/",
            )

        cache.delete(f"msg_count_{destinataire.pk}")
        _envoyer_email_si_deconnecte(destinataire, request.user, contenu_nettoye)

        return redirect("conversation_detail", conversation_id=conversation.pk)

    return render(request, "users/nouvelle_conversation.html", {
        "contacts": contacts,
    })
```

**Vue `nouveaux_messages_view`** (endpoint polling HTMX) :

```python
@login_required
def nouveaux_messages_view(request, conversation_id):
    """Retourne les nouveaux messages pour le polling HTMX."""
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    if not conversation.participants.filter(pk=request.user.pk).exists():
        return HttpResponseForbidden()

    dernier_id = request.GET.get("dernier_id", 0)
    nouveaux = (
        conversation.messages
        .filter(pk__gt=dernier_id)
        .exclude(auteur=request.user)
        .select_related("auteur")
        .order_by("envoye_le")
    )

    # Marquer comme lus
    nouveaux.filter(lu=False).update(lu=True)
    cache.delete(f"msg_count_{request.user.pk}")

    return render(request, "users/_messages_polling.html", {
        "messages": nouveaux,
    })
```

**Helper rate limit** :

```python
def _check_message_rate_limit(user_id):
    """Vérifie le rate limit de 30 messages/heure. Retourne True si limité."""
    cache_key = f"msg_rate_{user_id}"
    count = cache.get(cache_key, 0)
    if count >= 30:
        return True
    cache.set(cache_key, count + 1, timeout=3600)
    return False
```

**Helper email si déconnecté** :

```python
def _envoyer_email_si_deconnecte(destinataire, expediteur, contenu):
    """Envoie un email de notification si le destinataire est déconnecté > 5 min."""
    last_seen_key = f"last_seen_{destinataire.pk}"
    last_seen = cache.get(last_seen_key)
    if last_seen is None or (timezone.now() - last_seen).total_seconds() > 300:
        send_mail(
            subject=f"Nouveau message de {expediteur.nom_complet}",
            message=f"{expediteur.nom_complet} vous a envoyé un message :\n\n{contenu[:200]}",
            from_email=None,
            recipient_list=[destinataire.email],
            fail_silently=True,
        )
```

#### 🎯 Critères d'acceptation

- `GET /messages/` retourne la liste des conversations triées par `dernier_message_date` desc
- `GET /messages/<id>/` affiche les messages de la conversation avec pagination 50 msg/page
- `POST /messages/<id>/` avec `contenu='Bonjour'` crée un `Message` et retourne un fragment HTMX avec le message affiché (si header `HX-Request`)
- `POST /messages/<id>/` sans header HTMX redirige vers `conversation_detail`
- `GET /messages/nouveau/` affiche le formulaire avec la liste des contacts autorisés
- `POST /messages/nouveau/` crée une `Conversation` + premier `Message` + `Notification` dans une transaction atomique
- `GET /messages/<id>/nouveaux/?dernier_id=42` retourne les messages postérieurs à l'ID 42, excluant ceux de l'utilisateur courant
- Un non-participant reçoit 403 sur `conversation_detail` et `nouveaux_messages`

#### 🏗 Architecture

- Template `conversation.html` HTMX :
  - `hx-post` sur le formulaire d'envoi → insère la réponse avec `hx-swap="beforeend"` dans le conteneur de messages
  - `hx-trigger="every 5s"` sur un div invisible → appelle `nouveaux_messages_view` pour le polling
  - `hx-swap="beforeend"` pour insérer les nouveaux messages reçus
- Fragment `_message_item.html` : rendu d'un seul message (auteur, contenu, date) — réutilisé par envoi POST et polling
- Fragment `_messages_polling.html` : boucle sur les nouveaux messages, chacun rendu via `{% include "users/_message_item.html" %}`
- `strip_tags()` + `escape()` sur le contenu avant `save()` — défense en profondeur
- `transaction.atomic()` pour la création de conversation (conversation + participants + message + notification)
- `conversation.save()` après envoi de message pour mettre à jour `mis_a_jour_le` (champ `auto_now`)

#### 🔒 Sécurité

- **Vérification destinataire** : `contacts.filter(pk=destinataire.pk).exists()` — un utilisateur ne peut créer de conversation qu'avec un contact autorisé
- **IDOR conversation** : `conversation.participants.filter(pk=request.user.pk).exists()` — un non-participant reçoit 403
- **XSS** : `strip_tags()` + `escape()` sur le contenu avant `save()`. Pas de `|safe` dans les templates
- **Rate limit** : `_check_message_rate_limit()` — 30 messages/heure par utilisateur via cache
- **CSRF** : couvert par Django middleware + HTMX meta tag (existant)
- **Contenu vide / trop long** : validation explicite avant création

#### ⚡ Performance

- `select_related("auteur")` + `prefetch_related("messages")` sur les conversations
- Pagination 50 messages/page dans `conversation_detail_view`
- Cache compteur non lus `msg_count_{user_id}` — invalidé à chaque envoi/lecture
- Annotation `non_lus` dans la liste des conversations pour éviter N+1
- Endpoint polling `nouveaux_messages_view` ne récupère que les messages > `dernier_id` (incrémental)

#### ✅ Definition of Done

- [ ] 4 vues implémentées : `liste_conversations_view`, `conversation_detail_view`, `nouvelle_conversation_view`, `nouveaux_messages_view`
- [ ] 4 URLs enregistrées dans `users/urls.py`
- [ ] Helper `_check_message_rate_limit()` implémenté
- [ ] Helper `_envoyer_email_si_deconnecte()` implémenté
- [ ] Validation contenu (vide, >2000 chars, XSS)
- [ ] IDOR vérifié sur chaque vue
- [ ] Rate limit 30 msg/h fonctionnel
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 2.2 (URLs), 3.2 (Views), 8 (Patterns) mises à jour

---

### Étape 5.3 — Templates messagerie

**Fichiers** : `templates/users/liste_conversations.html`, `templates/users/conversation.html`, `templates/users/nouvelle_conversation.html`, `templates/users/_message_item.html`, `templates/users/_messages_polling.html`

**`liste_conversations.html`** :

```html
{% extends "base.html" %}
{% block page_title %}Mes messages{% endblock %}

{% block content %}
<div class="max-w-3xl mx-auto">
    <div class="flex justify-between items-center mb-6">
        <h1 class="text-2xl font-bold">Messages</h1>
        <a href="{% url 'nouvelle_conversation' %}"
           class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
            Nouveau message
        </a>
    </div>

    {% for conv in conversations %}
    <a href="{% url 'conversation_detail' conv.pk %}"
       class="block p-4 mb-2 rounded-lg border hover:bg-gray-50 transition">
        <div class="flex justify-between items-center">
            <div>
                <p class="font-semibold">
                    {% for p in conv.participants.all %}
                        {% if p.pk != request.user.pk %}{{ p.nom_complet }}{% endif %}
                    {% endfor %}
                </p>
                <p class="text-sm text-gray-500 truncate">
                    {{ conv.messages.last.contenu|truncatewords:15 }}
                </p>
            </div>
            <div class="text-right">
                <p class="text-xs text-gray-400">{{ conv.dernier_message_date|timesince }}</p>
                {% if conv.non_lus > 0 %}
                <span class="inline-block bg-red-500 text-white text-xs rounded-full px-2 py-0.5 mt-1">
                    {{ conv.non_lus }}
                </span>
                {% endif %}
            </div>
        </div>
    </a>
    {% empty %}
    <p class="text-gray-500 text-center py-8">Aucune conversation.</p>
    {% endfor %}
</div>
{% endblock %}
```

**`conversation.html`** (style chat avec HTMX) :

```html
{% extends "base.html" %}
{% block page_title %}Conversation{% endblock %}

{% block content %}
<div class="max-w-3xl mx-auto flex flex-col h-[calc(100vh-12rem)]">
    <div class="flex items-center mb-4">
        <a href="{% url 'liste_conversations' %}" class="mr-3 text-gray-500 hover:text-gray-700">←</a>
        <h1 class="text-xl font-bold">
            {% for p in conversation.participants.all %}
                {% if p.pk != request.user.pk %}{{ p.nom_complet }}{% endif %}
            {% endfor %}
        </h1>
    </div>

    <!-- Zone messages scrollable -->
    <div id="messages-container" class="flex-1 overflow-y-auto space-y-3 p-4 bg-gray-50 rounded-lg">
        {% for msg in messages_page %}
            {% include "users/_message_item.html" with message=msg %}
        {% endfor %}
    </div>

    <!-- Polling HTMX pour nouveaux messages -->
    <div hx-get="{% url 'nouveaux_messages' conversation.pk %}?dernier_id={{ messages_page.object_list.last.pk|default:0 }}"
         hx-trigger="every 5s"
         hx-target="#messages-container"
         hx-swap="beforeend">
    </div>

    <!-- Formulaire envoi -->
    <form hx-post="{% url 'conversation_detail' conversation.pk %}"
          hx-target="#messages-container"
          hx-swap="beforeend"
          hx-on::after-request="this.reset()"
          class="mt-4 flex gap-2">
        {% csrf_token %}
        <input type="text" name="contenu" placeholder="Votre message..."
               maxlength="2000" required
               class="flex-1 border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none">
        <button type="submit"
                class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700">
            Envoyer
        </button>
    </form>
</div>
{% endblock %}
```

**`_message_item.html`** (fragment HTMX) :

```html
<div class="flex {% if message.auteur == request.user %}justify-end{% else %}justify-start{% endif %}">
    <div class="max-w-xs lg:max-w-md px-4 py-2 rounded-2xl
                {% if message.auteur == request.user %}
                    bg-blue-600 text-white
                {% else %}
                    bg-white border
                {% endif %}">
        {% if message.auteur != request.user %}
        <p class="text-xs font-semibold text-gray-500 mb-1">{{ message.auteur.nom_complet }}</p>
        {% endif %}
        <p>{{ message.contenu }}</p>
        <p class="text-xs mt-1 {% if message.auteur == request.user %}text-blue-200{% else %}text-gray-400{% endif %}">
            {{ message.envoye_le|time:"H:i" }}
        </p>
    </div>
</div>
```

**`nouvelle_conversation.html`** :

```html
{% extends "base.html" %}
{% block page_title %}Nouveau message{% endblock %}

{% block content %}
<div class="max-w-xl mx-auto">
    <h1 class="text-2xl font-bold mb-6">Nouveau message</h1>

    {% if erreur %}
    <div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-4">
        {{ erreur }}
    </div>
    {% endif %}

    <form method="post" class="space-y-4">
        {% csrf_token %}
        <div>
            <label for="destinataire" class="block text-sm font-medium mb-1">Destinataire</label>
            <select name="destinataire" id="destinataire" required
                    class="w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500">
                <option value="">— Choisir —</option>
                {% for contact in contacts %}
                <option value="{{ contact.pk }}">{{ contact.nom_complet }} ({{ contact.get_role_display }})</option>
                {% endfor %}
            </select>
        </div>
        <div>
            <label for="contenu" class="block text-sm font-medium mb-1">Message</label>
            <textarea name="contenu" id="contenu" rows="4" maxlength="2000" required
                      class="w-full border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500"
                      placeholder="Écrivez votre message..."></textarea>
        </div>
        <button type="submit"
                class="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700">
            Envoyer
        </button>
    </form>
</div>
{% endblock %}
```

**`_messages_polling.html`** :

```html
{% for msg in messages %}
    {% include "users/_message_item.html" with message=msg %}
{% endfor %}
```

#### 🎯 Critères d'acceptation

- `liste_conversations.html` affiche chaque conversation avec le nom de l'interlocuteur, le dernier message tronqué, la date relative, et le badge de messages non lus
- `conversation.html` affiche les messages en style chat (bulle droite = moi, bulle gauche = interlocuteur) avec scroll automatique
- Le formulaire d'envoi utilise `hx-post` + `hx-swap="beforeend"` pour insérer le message sans rechargement
- Le polling `hx-trigger="every 5s"` récupère les nouveaux messages de l'interlocuteur
- `_message_item.html` est utilisé pour le rendu d'un message individuel (partagé entre rendu initial, envoi POST et polling)
- `nouvelle_conversation.html` affiche un `<select>` avec uniquement les contacts autorisés
- Aucun `|safe` sur les données utilisateur dans les templates

#### 🏗 Architecture

- Tous les templates dans `templates/users/` (cohérent avec les vues dans `users/views.py`)
- Fragments HTMX préfixés par `_` : `_message_item.html`, `_messages_polling.html`
- Chat bubbles avec Tailwind : bleu pour l'expéditeur (à droite), blanc avec bordure pour le destinataire (à gauche)
- Pas de `dark:` classes — dark mode géré globalement dans `base.html`

#### ✅ Definition of Done

- [ ] 5 templates créés : `liste_conversations.html`, `conversation.html`, `nouvelle_conversation.html`, `_message_item.html`, `_messages_polling.html`
- [ ] Style chat avec bulles alignées par auteur
- [ ] HTMX envoi + polling fonctionnels
- [ ] Aucun `|safe` sur les données utilisateur
- [ ] `CODEBASE_REFERENCE.md` section 5 (Templates) mise à jour

---

### Étape 5.4 — Notifications de message et intégration

**Fichier** : `users/views.py`, `users/context_processors.py`, `templates/base.html`

**Notifications** :

Chaque message envoyé crée une `Notification` de type `NOUVEAU_MESSAGE` pour les autres participants de la conversation (déjà inclus dans les vues de l'étape 5.2).

**Compteur non lus dans le header** :

Le context processor `notifications_context()` (créé en Phase 4) est enrichi pour inclure le compteur de messages non lus :

```python
def notifications_context(request):
    """Ajoute les compteurs de notifications et messages non lus au contexte."""
    if not request.user.is_authenticated:
        return {}

    # Compteur notifications non lues (existant Phase 4)
    notif_count = cache.get(f"notif_count_{request.user.pk}")
    if notif_count is None:
        notif_count = Notification.objects.filter(
            destinataire=request.user, lue=False,
        ).count()
        cache.set(f"notif_count_{request.user.pk}", notif_count, timeout=300)

    # Compteur messages non lus
    msg_count = cache.get(f"msg_count_{request.user.pk}")
    if msg_count is None:
        msg_count = Message.objects.filter(
            conversation__participants=request.user,
            lu=False,
        ).exclude(auteur=request.user).count()
        cache.set(f"msg_count_{request.user.pk}", msg_count, timeout=300)

    return {
        "notif_non_lues": notif_count,
        "msg_non_lus": msg_count,
    }
```

**Sidebar `base.html`** — ajout du lien Messages avec badge :

```html
<!-- Dans la sidebar, pour tous les rôles sauf admin -->
<a href="{% url 'liste_conversations' %}" class="...">
    Messages
    {% if msg_non_lus > 0 %}
    <span class="bg-red-500 text-white text-xs rounded-full px-2 py-0.5 ml-2">
        {{ msg_non_lus }}
    </span>
    {% endif %}
</a>
```

**Email optionnel si déconnecté** :

L'email est envoyé via `_envoyer_email_si_deconnecte()` (étape 5.2) si le destinataire n'a pas été vu depuis > 5 minutes. Le suivi `last_seen` se fait via un middleware léger ou via le context processor qui met à jour le cache à chaque requête :

```python
# Dans notifications_context() — tracking last_seen
cache.set(f"last_seen_{request.user.pk}", timezone.now(), timeout=600)
```

#### 🎯 Critères d'acceptation

- Chaque message envoyé crée une `Notification(type="nouveau_message")` pour chaque participant (hors auteur)
- Le compteur `msg_non_lus` est affiché dans la sidebar à côté du lien Messages
- Le compteur est caché (300s) et invalidé à chaque envoi/lecture
- Un email est envoyé au destinataire si déconnecté depuis plus de 5 minutes
- `last_seen_{user_id}` est mis à jour à chaque requête authentifiée via le context processor

#### 🔒 Sécurité

- `Notification.contenu` tronqué à 100 caractères (pas de fuite de message complet dans les notifications)
- `Notification.lien` utilise des chemins relatifs internes (`/messages/<id>/`)
- L'email est envoyé avec `fail_silently=True` pour ne pas bloquer l'envoi de message en cas d'erreur SMTP

#### ⚡ Performance

- Cache `msg_count_{user_id}` et `notif_count_{user_id}` avec TTL 300s
- Invalidation ciblée à chaque écriture (pas de flush global)
- `last_seen` via cache — pas de write DB à chaque requête

#### ✅ Definition of Done

- [ ] `notifications_context()` enrichi avec `msg_non_lus`
- [ ] Badge compteur dans la sidebar `base.html`
- [ ] `last_seen` tracking implémenté
- [ ] `_envoyer_email_si_deconnecte()` fonctionnel
- [ ] Invalidation cache correcte à chaque envoi/lecture
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 3.2 (Views), 5 (Templates), 8 (Patterns) mises à jour

---

### 🧪 Tests Phase 5 (16 tests)

**Fichier** : `users/tests/test_messagerie.py`

#### Tests helper `contacts_autorises` (3 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_contacts_autorises_enseignant_retourne_eleves_et_parents` | `enseignant`, `eleve`, `parent_user`, `lien_enseignant_eleve_valide`, `lien_parent_eleve_valide` | `assertIn(eleve, result)`, `assertIn(parent_user, result)` |
| 2 | `test_contacts_autorises_parent_retourne_enseignants_enfants` | `parent_user`, `eleve`, `enseignant`, `lien_parent_eleve_valide`, `lien_enseignant_eleve_valide` | `assertIn(enseignant, result)`, `assertEqual(result.count(), 1)` |
| 3 | `test_contacts_autorises_eleve_retourne_enseignants` | `eleve`, `enseignant`, `lien_enseignant_eleve_valide` | `assertIn(enseignant, result)`, `assertEqual(result.count(), 1)` |

#### Tests envoi de message — accès autorisé (3 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 4 | `test_enseignant_envoie_message_eleve_lie_ok` | `enseignant`, `eleve`, `lien_enseignant_eleve_valide`, `conversation_ens_eleve` | `assertEqual(Message.objects.count(), 1)`, `assertEqual(response.status_code, 200)` (HTMX fragment) |
| 5 | `test_parent_envoie_message_enseignant_enfant_ok` | `parent_user`, `enseignant`, `lien_parent_eleve_valide`, `lien_enseignant_eleve_valide`, `conversation_parent_ens` | `assertEqual(Message.objects.count(), 1)` |
| 6 | `test_eleve_envoie_message_enseignant_lie_ok` | `eleve`, `enseignant`, `lien_enseignant_eleve_valide`, `conversation_ens_eleve` | `assertEqual(Message.objects.count(), 1)` |

#### Tests envoi de message — accès refusé (3 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 7 | `test_parent_envoie_message_autre_parent_403` | `parent_user`, `parent_user2`, `conversation_parents` | `assertEqual(response.status_code, 403)` |
| 8 | `test_eleve_envoie_message_parent_403` | `eleve`, `parent_user` | `assertEqual(response.status_code, 403)` (via `nouvelle_conversation` POST) |
| 9 | `test_utilisateur_non_autorise_envoie_message_403` | `enseignant2` (pas lié), `eleve`, `conversation_ens2_eleve` | `assertEqual(response.status_code, 403)` |

#### Tests conversation et inbox (4 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 10 | `test_inbox_trie_par_dernier_message` | `enseignant`, 2 conversations avec messages à dates différentes | Première conversation dans la réponse = celle avec le message le plus récent |
| 11 | `test_acces_conversation_non_participant_403` | `enseignant2`, `conversation_ens_eleve` (enseignant2 non participant) | `assertEqual(response.status_code, 403)` |
| 12 | `test_message_plus_2000_caracteres_erreur` | `enseignant`, `conversation_ens_eleve` | `assertEqual(response.status_code, 400)` |
| 13 | `test_fragment_htmx_conversation_html_partiel` | `enseignant`, `conversation_ens_eleve`, header `HX-Request: true` | `assertNotContains(response, '<!DOCTYPE')`, `assertContains(response, 'Bonjour')` |

#### Tests création et notification (3 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 14 | `test_nouvelle_conversation_cree_conversation_et_message` | `enseignant`, `eleve`, `lien_enseignant_eleve_valide` | `assertEqual(Conversation.objects.count(), 1)`, `assertEqual(Message.objects.count(), 1)` |
| 15 | `test_notification_creee_a_reception_message` | `enseignant`, `eleve`, `conversation_ens_eleve` | `assertTrue(Notification.objects.filter(destinataire=eleve, type="nouveau_message").exists())` |
| 16 | `test_compteur_messages_non_lus_correct` | `eleve`, `conversation_ens_eleve` + 3 messages non lus | `assertEqual(response.context["msg_non_lus"], 3)` |

**Fixtures à ajouter dans `conftest.py`** :

```python
@pytest.fixture
def conversation_ens_eleve(enseignant, eleve):
    conv = Conversation.objects.create()
    conv.participants.add(enseignant, eleve)
    return conv

@pytest.fixture
def conversation_parent_ens(parent_user, enseignant):
    conv = Conversation.objects.create()
    conv.participants.add(parent_user, enseignant)
    return conv
```

---

### Résumé des changements par fichier — Phase 5

| Fichier | Action |
|---------|--------|
| `users/helpers.py` | Ajouter `contacts_autorises()` |
| `users/views.py` | Ajouter `liste_conversations_view`, `conversation_detail_view`, `nouvelle_conversation_view`, `nouveaux_messages_view`, `_check_message_rate_limit`, `_envoyer_email_si_deconnecte` |
| `users/urls.py` | Ajouter URLs `liste_conversations`, `nouvelle_conversation`, `conversation_detail`, `nouveaux_messages` |
| `users/context_processors.py` | Enrichir `notifications_context()` avec `msg_non_lus` + `last_seen` tracking |
| `templates/users/liste_conversations.html` | **Nouveau** — liste des conversations avec badge non lus |
| `templates/users/conversation.html` | **Nouveau** — style chat HTMX (envoi + polling 5s) |
| `templates/users/nouvelle_conversation.html` | **Nouveau** — formulaire nouvelle conversation |
| `templates/users/_message_item.html` | **Nouveau** — fragment HTMX message individuel (bulle chat) |
| `templates/users/_messages_polling.html` | **Nouveau** — fragment HTMX polling nouveaux messages |
| `templates/base.html` | Ajouter lien Messages dans la sidebar avec badge `msg_non_lus` |
| `users/tests/conftest.py` | Ajouter fixtures `conversation_ens_eleve`, `conversation_parent_ens` |
| `users/tests/test_messagerie.py` | **Nouveau** — 16 tests messagerie (délégué à `test-writer`) |
| `CODEBASE_REFERENCE.md` | Sections 2.2 (URLs), 3.2 (Views), 5 (Templates), 8 (Patterns) mises à jour |

### Ordre d'exécution recommandé

```
1. Implementer  → Étape 5.1 (helper contacts_autorises)
2. Implementer  → Étape 5.2 (vues messagerie + helpers rate limit/email)
3. Implementer  → Étape 5.3 (templates HTMX)
4. Implementer  → Étape 5.4 (notifications + compteur sidebar + last_seen)
5. Test Writer  → 16 tests dans users/tests/test_messagerie.py
6. Implementer  → Mise à jour CODEBASE_REFERENCE.md
```

---

## Phase 6 — Panel admin étendu

> **Objectif** : donner à l'administrateur une visibilité complète sur les enseignants et leurs classes, permettre la gestion forcée des liaisons (assigner/supprimer), et enrichir les compteurs du dashboard admin. L'admin doit pouvoir gérer le pool d'élèves sans enseignant et forcer des liaisons depuis le panel.

### Décisions d'architecture (Phase 6)

| Décision | Justification |
|----------|---------------|
| Toutes les vues admin dans `users/views.py` | Cohérent avec `admin_analytics_view` existant dans `users/views.py`. Le seuil de création d'app n'est pas atteint |
| Templates dans `templates/dashboard/` | Sous-répertoire existant pour les dashboards. Cohérent avec `admin_analytics.html` |
| `admin_required` helper réutilisé | Décorateur ou check inline `if not request.user.is_admin` → 403, identique aux vues admin existantes |
| Pagination 25 éléments/page | Convention projet (cf. standards transversaux) |
| Endpoints POST pour forcer/supprimer des liaisons | Actions destructrices → POST-only, CSRF protégé, admin-only |

---

### Étape 6.1 — Admin Django register

**Fichier** : `users/admin.py`

Enregistrer les modèles dans l'interface Django Admin pour permettre la gestion directe en cas de besoin :

```python
# users/admin.py (ajouts)
from users.models import (
    LienEnseignantEleve, LienParentEleve,
    Notification, Conversation, Message,
)

@admin.register(LienEnseignantEleve)
class LienEnseignantEleveAdmin(admin.ModelAdmin):
    list_display = ("enseignant", "eleve", "statut", "date_demande")
    list_filter = ("statut",)
    search_fields = ("enseignant__email", "eleve__email")
    raw_id_fields = ("enseignant", "eleve")

@admin.register(LienParentEleve)
class LienParentEleveAdmin(admin.ModelAdmin):
    list_display = ("parent", "eleve", "statut", "date_demande")
    list_filter = ("statut",)
    search_fields = ("parent__email", "eleve__email")
    raw_id_fields = ("parent", "eleve")

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("destinataire", "type", "lue", "date_creation")
    list_filter = ("type", "lue")
    search_fields = ("destinataire__email", "contenu")

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("pk", "dernier_message_date")
    filter_horizontal = ("participants",)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("auteur", "conversation", "envoye_le", "lu")
    list_filter = ("lu",)
    search_fields = ("auteur__email", "contenu")
    raw_id_fields = ("auteur", "conversation")
```

#### 🎯 Critères d'acceptation

- Les 5 modèles apparaissent dans l'interface Django Admin (`/admin/`)
- Chaque modèle a `list_display`, `list_filter`, et `search_fields` configurés
- `raw_id_fields` est utilisé sur les FK pour éviter des `<select>` lourds sur les grosses bases
- `filter_horizontal` est utilisé sur le M2M `participants` de `Conversation`

#### 🏗 Architecture

- Aucun modèle proxy, aucun inline — enregistrement simple
- Pas de `ModelAdmin` custom complexe : l'admin Django sert de filet de sécurité, le vrai panel est dans les vues custom

#### 🔒 Sécurité

- L'interface Django Admin est déjà protégée par `is_staff` / `is_superuser`
- Les `raw_id_fields` empêchent le chargement de milliers d'utilisateurs dans un `<select>`

#### ⚡ Performance

- `raw_id_fields` sur toutes les FK : évite les requêtes N+1 dans l'admin
- `search_fields` sur `email` (indexé) uniquement

#### ✅ Definition of Done

- [ ] 5 `ModelAdmin` enregistrés dans `users/admin.py`
- [ ] Chaque modèle visible et fonctionnel dans l'admin Django
- [ ] `CODEBASE_REFERENCE.md` section Admin mise à jour

---

### Étape 6.2 — `admin_enseignants_view` (tableau des enseignants)

**Fichier** : `users/views.py`, `users/urls.py`, `templates/dashboard/admin_enseignants.html`

**Vue** :

```python
@login_required
def admin_enseignants_view(request):
    """Liste les enseignants avec stats et filtres pour le panel admin."""
    if not request.user.is_admin:
        return HttpResponseForbidden()

    q = request.GET.get("q", "").strip()
    tri = request.GET.get("tri", "nom")  # nom | nb_eleves | derniere_connexion

    enseignants = CustomUser.objects.filter(
        role=RoleChoices.ENSEIGNANT,
    ).annotate(
        nb_eleves=Count(
            "liens_enseignant",
            filter=Q(liens_enseignant__statut=StatutLienChoices.VALIDE),
        ),
    )

    if q:
        enseignants = enseignants.filter(
            Q(first_name__icontains=q)
            | Q(last_name__icontains=q)
            | Q(email__icontains=q)
        )

    ordres_valides = {
        "nom": "last_name",
        "nb_eleves": "-nb_eleves",
        "derniere_connexion": "-last_login",
    }
    enseignants = enseignants.order_by(ordres_valides.get(tri, "last_name"))

    paginator = Paginator(enseignants, 25)
    page = paginator.get_page(request.GET.get("page"))

    return render(request, "dashboard/admin_enseignants.html", {
        "page_obj": page,
        "q": q,
        "tri": tri,
    })
```

#### URL

```python
# users/urls.py (ajout)
path("admin-panel/enseignants/", admin_enseignants_view, name="admin_enseignants"),
```

#### Template `dashboard/admin_enseignants.html`

Structure :

1. **Barre de recherche** : champ texte avec `hx-get` pour filtrage HTMX en temps réel
2. **Tri** : liens cliquables sur les en-têtes de colonnes (Nom, Nb élèves, Dernière connexion)
3. **Tableau** : colonnes — Nom complet, Email, Nb élèves liés (badge), Dernière connexion, Lien vers détail
4. **Pagination** : standard 25/page

#### 🎯 Critères d'acceptation

- `GET /admin-panel/enseignants/` avec admin connecté → 200, tableau des enseignants
- `GET /admin-panel/enseignants/` avec non-admin → 403
- `GET /admin-panel/enseignants/` anonyme → redirect login
- Le filtre `?q=dupont` filtre par nom, prénom ou email (icontains)
- Le tri `?tri=nb_eleves` ordonne par nombre d'élèves liés validés (décroissant)
- Le tri `?tri=derniere_connexion` ordonne par `last_login` (décroissant)
- Le tri par défaut est alphabétique par `last_name`
- La pagination affiche 25 enseignants par page
- Le compteur `nb_eleves` reflète uniquement les liens au statut `VALIDE`
- Chaque ligne a un lien vers `admin_enseignant_detail`

#### 🏗 Architecture

- `annotate(nb_eleves=Count(..., filter=Q(...)))` — une seule requête SQL pour le tableau + compteurs
- `Paginator` + `get_page()` — pattern existant dans le projet
- Tri par whitelist (`ordres_valides`) — jamais d'injection de champ via GET
- Recherche `Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(email__icontains=q)` — pas de full-text, suffisant pour un panel admin

#### 🔒 Sécurité

- **Admin-only** : `if not request.user.is_admin: return HttpResponseForbidden()`
- **Injection tri** : whitelist `ordres_valides` — un paramètre `tri` invalide fallback sur `last_name`
- **XSS** : aucun `|safe` dans le template, les données utilisateur passent par l'auto-escape Django

#### ⚡ Performance

- `annotate(Count)` en une seule requête — pas de N+1 pour le compteur d'élèves
- Pagination 25 → taille de résultat bornée
- `last_name` indexé par défaut (champ Django `AbstractUser`)

#### ✅ Definition of Done

- [ ] `admin_enseignants_view` implémenté dans `users/views.py`
- [ ] URL `admin_enseignants` enregistrée dans `users/urls.py`
- [ ] Template `dashboard/admin_enseignants.html` créé avec tableau, recherche, tri, pagination
- [ ] Annotation `nb_eleves` fonctionnelle
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 2.2 (URLs), 3.2 (Views), 5 (Templates) mises à jour

---

### Étape 6.3 — `admin_enseignant_detail_view` (stats classe)

**Fichier** : `users/views.py`, `users/urls.py`, `templates/dashboard/admin_enseignant_detail.html`

**Vue** :

```python
@login_required
def admin_enseignant_detail_view(request, enseignant_id):
    """Affiche les stats classe et le tableau des élèves d'un enseignant."""
    if not request.user.is_admin:
        return HttpResponseForbidden()

    enseignant = get_object_or_404(
        CustomUser, pk=enseignant_id, role=RoleChoices.ENSEIGNANT,
    )

    liens = LienEnseignantEleve.objects.filter(
        enseignant=enseignant,
        statut=StatutLienChoices.VALIDE,
    ).select_related("eleve")

    eleves = [lien.eleve for lien in liens]
    eleve_ids = [e.pk for e in eleves]

    # Stats classe agrégées
    from progress.models import UserProgression, UserQuizResultat
    from courses.models import Lecon

    total_lecons = Lecon.objects.count()
    progressions = UserProgression.objects.filter(
        user_id__in=eleve_ids, statut="termine",
    ).values("user_id").annotate(nb_terminees=Count("id"))
    progressions_map = {p["user_id"]: p["nb_terminees"] for p in progressions}

    quiz_resultats = UserQuizResultat.objects.filter(
        user_id__in=eleve_ids,
    ).values("user_id").annotate(score_moyen=Avg("meilleur_score"))
    scores_map = {r["user_id"]: r["score_moyen"] for r in quiz_resultats}

    eleves_data = []
    for eleve in eleves:
        eleves_data.append({
            "eleve": eleve,
            "nb_lecons_terminees": progressions_map.get(eleve.pk, 0),
            "total_lecons": total_lecons,
            "score_moyen": scores_map.get(eleve.pk, 0),
            "derniere_connexion": eleve.last_login,
        })

    stats_classe = {
        "nb_eleves": len(eleves),
        "score_moyen_classe": (
            sum(s.get("score_moyen", 0) or 0 for s in eleves_data) / len(eleves)
            if eleves else 0
        ),
        "taux_completion_moyen": (
            sum(e["nb_lecons_terminees"] for e in eleves_data)
            / (len(eleves) * total_lecons) * 100
            if eleves and total_lecons else 0
        ),
    }

    return render(request, "dashboard/admin_enseignant_detail.html", {
        "enseignant": enseignant,
        "eleves_data": eleves_data,
        "stats_classe": stats_classe,
    })
```

#### URL

```python
# users/urls.py (ajout)
path("admin-panel/enseignants/<int:enseignant_id>/", admin_enseignant_detail_view, name="admin_enseignant_detail"),
```

#### Template `dashboard/admin_enseignant_detail.html`

Structure :

1. **En-tête** : nom enseignant, email, date inscription, dernière connexion, code identifiant
2. **Carte stats classe** : nb élèves, score moyen classe (gauge), taux complétion moyen (barre)
3. **Tableau élèves** : Nom, Niveau, Leçons terminées (barre), Score moyen quiz (badge couleur), Dernière connexion, Lien fiche élève

#### 🎯 Critères d'acceptation

- `GET /admin-panel/enseignants/42/` avec admin → 200, détail de l'enseignant 42
- `GET /admin-panel/enseignants/42/` avec non-admin → 403
- `GET /admin-panel/enseignants/42/` anonyme → redirect login
- `GET /admin-panel/enseignants/99999/` → 404
- `GET /admin-panel/enseignants/42/` où user 42 est un élève (pas enseignant) → 404
- Le tableau affiche uniquement les élèves liés avec statut `VALIDE`
- `stats_classe.score_moyen_classe` est la moyenne des scores moyens quiz de chaque élève
- `stats_classe.taux_completion_moyen` est le ratio global (leçons terminées / total leçons × nb élèves)
- Chaque ligne élève a un lien vers `fiche_eleve` (Phase 4)

#### 🏗 Architecture

- `get_object_or_404(CustomUser, pk=enseignant_id, role=RoleChoices.ENSEIGNANT)` — 404 si rôle incorrect (pas de leak d'existence)
- `select_related("eleve")` sur les liens → une seule requête pour liens + élèves
- Agrégations en 2 requêtes groupées (`values("user_id").annotate(...)`) au lieu de N requêtes par élève
- Budget : **≤ 6 requêtes SQL** (enseignant + liens + progressions + quiz + total_lecons + auth overhead)

#### 🔒 Sécurité

- **Admin-only** : vérification `is_admin` en première ligne
- **Enumeration** : filtre `role=RoleChoices.ENSEIGNANT` dans le `get_object_or_404` → un ID d'élève retourne 404
- **XSS** : pas de `|safe`, auto-escape Django standard

#### ⚡ Performance

- `select_related("eleve")` sur les liens : 1 requête au lieu de N
- `values("user_id").annotate(Count/Avg)` : 2 requêtes groupées pour toutes les stats
- Pas de pagination sur les élèves d'un enseignant (cardinalité attendue < 40)

#### ✅ Definition of Done

- [ ] `admin_enseignant_detail_view` implémenté dans `users/views.py`
- [ ] URL `admin_enseignant_detail` enregistrée dans `users/urls.py`
- [ ] Template `dashboard/admin_enseignant_detail.html` créé avec en-tête, stats classe, tableau élèves
- [ ] Budget ≤ 6 requêtes SQL respecté
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 2.2, 3.2, 5 mises à jour

---

### Étape 6.4 — Pool « Élèves sans enseignant » dans le dashboard admin

**Fichier** : `users/views.py` (modification `_dashboard_admin` ou `admin_analytics_view`), `templates/dashboard/admin_eleves_orphelins.html`

**Logique** :

Un élève est « orphelin » (sans enseignant) si aucun `LienEnseignantEleve` au statut `VALIDE` n'existe pour lui. L'admin voit ces élèves comme s'il était leur enseignant par défaut.

**Vue dédiée** :

```python
@login_required
def admin_eleves_orphelins_view(request):
    """Liste les élèves sans enseignant lié (pool admin par défaut)."""
    if not request.user.is_admin:
        return HttpResponseForbidden()

    eleves_orphelins = CustomUser.objects.filter(
        role=RoleChoices.ELEVE,
    ).exclude(
        pk__in=Subquery(
            LienEnseignantEleve.objects.filter(
                statut=StatutLienChoices.VALIDE,
            ).values("eleve_id")
        ),
    ).order_by("last_name", "first_name")

    paginator = Paginator(eleves_orphelins, 25)
    page = paginator.get_page(request.GET.get("page"))

    return render(request, "dashboard/admin_eleves_orphelins.html", {
        "page_obj": page,
        "total_orphelins": paginator.count,
    })
```

**Compteur dans le dashboard admin** :

Ajouter dans `_dashboard_admin` le compteur pour affichage sur une carte :

```python
nb_orphelins = CustomUser.objects.filter(
    role=RoleChoices.ELEVE,
).exclude(
    pk__in=Subquery(
        LienEnseignantEleve.objects.filter(
            statut=StatutLienChoices.VALIDE,
        ).values("eleve_id")
    ),
).count()
```

#### URL

```python
# users/urls.py (ajout)
path("admin-panel/eleves-orphelins/", admin_eleves_orphelins_view, name="admin_eleves_orphelins"),
```

#### Template `dashboard/admin_eleves_orphelins.html`

Structure :

1. **En-tête** : titre « Élèves sans enseignant » + compteur total
2. **Tableau** : Nom, Email, Niveau, Date inscription, Dernière connexion, Bouton « Assigner un enseignant »
3. **Bouton assigner** : ouvre un modal/dropdown HTMX avec la liste des enseignants pour assigner (POST vers `admin_forcer_liaison`)
4. **Pagination** : 25/page standard

#### 🎯 Critères d'acceptation

- `GET /admin-panel/eleves-orphelins/` avec admin → 200, tableau des élèves sans enseignant validé
- `GET /admin-panel/eleves-orphelins/` avec non-admin → 403
- `GET /admin-panel/eleves-orphelins/` anonyme → redirect login
- Un élève avec un lien `VALIDE` n'apparaît PAS dans la liste
- Un élève avec un lien `EN_ATTENTE` ou `REFUSE` apparaît dans la liste (il n'a pas d'enseignant validé)
- Le compteur `total_orphelins` correspond au nombre total (pas seulement la page courante)
- Le dashboard admin affiche une carte « Élèves sans enseignant : N » avec lien vers cette vue
- Le bouton « Assigner » déclenche un formulaire POST vers `admin_forcer_liaison` (étape 6.5)

#### 🏗 Architecture

- `Subquery` + `exclude` : requête SQL efficace avec `NOT IN (SELECT eleve_id FROM ...)` — pas de boucle Python
- Le compteur dans le dashboard admin utilise la même logique `.count()` — extraire en helper si réutilisé :
  ```python
  def _get_eleves_orphelins_qs():
      """Retourne le queryset des élèves sans enseignant validé."""
      return CustomUser.objects.filter(
          role=RoleChoices.ELEVE,
      ).exclude(
          pk__in=Subquery(
              LienEnseignantEleve.objects.filter(
                  statut=StatutLienChoices.VALIDE,
              ).values("eleve_id")
          ),
      )
  ```
- Alternative plus performante avec `Exists` subquery :
  ```python
  eleves_orphelins = CustomUser.objects.filter(
      role=RoleChoices.ELEVE,
  ).annotate(
      a_enseignant=Exists(
          LienEnseignantEleve.objects.filter(
              eleve=OuterRef("pk"),
              statut=StatutLienChoices.VALIDE,
          )
      ),
  ).filter(a_enseignant=False)
  ```

#### 🔒 Sécurité

- **Admin-only** : vérification `is_admin` explicite
- **Enumeration** : la liste ne montre que les élèves, pas les enseignants/parents/admins
- **IDOR** : non applicable (pas d'accès par ID d'un autre utilisateur)

#### ⚡ Performance

- `Exists` subquery préféré à `Subquery` + `exclude` → plan d'exécution plus efficace sur PostgreSQL
- Pagination 25 → résultat borné
- `db_index=True` sur `LienEnseignantEleve.statut` si pas déjà indexé

#### ✅ Definition of Done

- [ ] `admin_eleves_orphelins_view` implémenté dans `users/views.py`
- [ ] Helper `_get_eleves_orphelins_qs()` extrait (partagé avec dashboard admin)
- [ ] URL `admin_eleves_orphelins` enregistrée dans `users/urls.py`
- [ ] Template `dashboard/admin_eleves_orphelins.html` créé avec tableau, bouton assigner, pagination
- [ ] Compteur `nb_orphelins` affiché sur une carte dans le dashboard admin
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 2.2, 3.2, 5 mises à jour

---

### Étape 6.5 — Forcer / supprimer des liaisons (endpoints admin POST)

**Fichier** : `users/views.py`, `users/urls.py`

**Deux vues POST-only** :

```python
@login_required
@require_POST
def admin_forcer_liaison_view(request):
    """Force la création d'un lien enseignant-élève validé (admin uniquement)."""
    if not request.user.is_admin:
        return HttpResponseForbidden()

    enseignant_id = request.POST.get("enseignant_id")
    eleve_id = request.POST.get("eleve_id")

    enseignant = get_object_or_404(
        CustomUser, pk=enseignant_id, role=RoleChoices.ENSEIGNANT,
    )
    eleve = get_object_or_404(
        CustomUser, pk=eleve_id, role=RoleChoices.ELEVE,
    )

    # Vérifier qu'il n'existe pas déjà un lien validé pour cet élève
    lien_existant = LienEnseignantEleve.objects.filter(
        eleve=eleve, statut=StatutLienChoices.VALIDE,
    ).first()

    if lien_existant:
        messages.error(request, f"Cet élève est déjà lié à {lien_existant.enseignant.nom_complet}.")
        return redirect("admin_eleves_orphelins")

    with transaction.atomic():
        LienEnseignantEleve.objects.update_or_create(
            enseignant=enseignant,
            eleve=eleve,
            defaults={
                "statut": StatutLienChoices.VALIDE,
                "date_validation": timezone.now(),
            },
        )
        Notification.objects.create(
            destinataire=eleve,
            type=TypeNotificationChoices.LIEN_VALIDE,
            contenu=f"L'administrateur vous a assigné à l'enseignant {enseignant.nom_complet}.",
        )
        Notification.objects.create(
            destinataire=enseignant,
            type=TypeNotificationChoices.LIEN_VALIDE,
            contenu=f"L'administrateur vous a assigné l'élève {eleve.nom_complet}.",
        )

    messages.success(request, f"{eleve.nom_complet} a été assigné à {enseignant.nom_complet}.")
    return redirect("admin_eleves_orphelins")


@login_required
@require_POST
def admin_supprimer_liaison_view(request):
    """Supprime un lien enseignant-élève (admin uniquement)."""
    if not request.user.is_admin:
        return HttpResponseForbidden()

    lien_id = request.POST.get("lien_id")
    lien = get_object_or_404(LienEnseignantEleve, pk=lien_id)

    enseignant = lien.enseignant
    eleve = lien.eleve

    with transaction.atomic():
        lien.delete()
        Notification.objects.create(
            destinataire=eleve,
            type=TypeNotificationChoices.LIEN_REFUSE,
            contenu=f"L'administrateur a supprimé votre liaison avec l'enseignant {enseignant.nom_complet}.",
        )
        Notification.objects.create(
            destinataire=enseignant,
            type=TypeNotificationChoices.LIEN_REFUSE,
            contenu=f"L'administrateur a supprimé la liaison avec l'élève {eleve.nom_complet}.",
        )

    messages.success(request, f"Liaison {enseignant.nom_complet} ↔ {eleve.nom_complet} supprimée.")
    referrer = request.POST.get("next", "admin_enseignants")
    return redirect(referrer)
```

#### URLs

```python
# users/urls.py (ajout)
path("admin-panel/forcer-liaison/", admin_forcer_liaison_view, name="admin_forcer_liaison"),
path("admin-panel/supprimer-liaison/", admin_supprimer_liaison_view, name="admin_supprimer_liaison"),
```

#### 🎯 Critères d'acceptation

- `POST /admin-panel/forcer-liaison/` avec admin + `enseignant_id` + `eleve_id` valides → crée un lien `VALIDE`, redirige vers `admin_eleves_orphelins`
- `POST /admin-panel/forcer-liaison/` si l'élève a déjà un enseignant validé → message d'erreur, pas de modification
- `POST /admin-panel/forcer-liaison/` avec non-admin → 403
- `GET /admin-panel/forcer-liaison/` → 405 (Method Not Allowed, `@require_POST`)
- `POST /admin-panel/supprimer-liaison/` avec admin + `lien_id` valide → supprime le lien, redirige
- `POST /admin-panel/supprimer-liaison/` avec `lien_id` inexistant → 404
- `POST /admin-panel/supprimer-liaison/` avec non-admin → 403
- Les deux endpoints créent des `Notification` pour l'élève ET l'enseignant concernés
- Les opérations sont dans un `transaction.atomic()`
- Le paramètre `next` dans `admin_supprimer_liaison_view` permet de revenir à la page appelante

#### 🏗 Architecture

- `@require_POST` (Django built-in) — refuse GET/PUT/DELETE → 405
- `transaction.atomic()` — le lien et les notifications sont créés/supprimés ensemble
- `update_or_create` pour `admin_forcer_liaison_view` — si un lien `EN_ATTENTE` ou `REFUSE` existe déjà, il est mis à jour vers `VALIDE` au lieu de créer un doublon
- `messages.success/error` pour le feedback utilisateur (framework messages Django existant)
- `request.POST.get("next", "admin_enseignants")` — le template peut inclure un champ hidden `next` pour contrôler la redirection après suppression

#### 🔒 Sécurité

- **Admin-only** : double vérification `is_admin` + `@require_POST`
- **CSRF** : protégé par le middleware CSRF Django (formulaire POST standard)
- **Validation des IDs** : `get_object_or_404` avec filtre `role` → pas d'assignation d'un enseignant en tant qu'élève
- **Race condition** : `transaction.atomic()` + `update_or_create` → sérialisé par la DB
- **Redirection ouverte** : `next` est un nom d'URL Django (`redirect("admin_enseignants")`), pas une URL externe — valider en whitelist si nécessaire :
  ```python
  REDIRECTS_VALIDES = {"admin_enseignants", "admin_eleves_orphelins", "admin_enseignant_detail"}
  referrer = request.POST.get("next", "admin_enseignants")
  if referrer not in REDIRECTS_VALIDES:
      referrer = "admin_enseignants"
  ```

#### ⚡ Performance

- 1 requête check `lien_existant` + 1 `update_or_create` + 2 `Notification.create` = 4 requêtes max par opération
- Pas de N+1, pas de boucle

#### ✅ Definition of Done

- [ ] `admin_forcer_liaison_view` implémenté (POST-only, admin-only)
- [ ] `admin_supprimer_liaison_view` implémenté (POST-only, admin-only)
- [ ] 2 URLs enregistrées dans `users/urls.py`
- [ ] Whitelist de redirection (`REDIRECTS_VALIDES`) implémentée
- [ ] `transaction.atomic()` sur les deux vues
- [ ] Notifications créées pour les deux parties
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 2.2, 3.2, 8 mises à jour

---

### Étape 6.6 — Compteurs étendus dashboard admin

**Fichier** : `users/views.py` (modification `_dashboard_admin`), `templates/dashboard/eleve.html` (dashboard admin)

**Ajouts au contexte du dashboard admin** :

```python
# Dans _dashboard_admin(request) — ajouts
from users.models import LienEnseignantEleve, StatutLienChoices

nb_enseignants = CustomUser.objects.filter(role=RoleChoices.ENSEIGNANT).count()
nb_parents = CustomUser.objects.filter(role=RoleChoices.PARENT).count()
nb_orphelins = _get_eleves_orphelins_qs().count()
nb_liaisons_en_attente = LienEnseignantEleve.objects.filter(
    statut=StatutLienChoices.EN_ATTENTE,
).count() + LienParentEleve.objects.filter(
    statut=StatutLienChoices.EN_ATTENTE,
).count()
nb_messages_total = Message.objects.count()
nb_messages_24h = Message.objects.filter(
    envoye_le__gte=timezone.now() - timedelta(hours=24),
).count()
```

**Nouvelles cartes dans le dashboard admin** :

| Carte | Valeur | Icône | Lien |
|-------|--------|-------|------|
| Enseignants | `nb_enseignants` | 👩‍🏫 | `admin_enseignants` |
| Parents | `nb_parents` | 👨‍👩‍👧 | — |
| Élèves sans enseignant | `nb_orphelins` | ⚠️ | `admin_eleves_orphelins` |
| Liaisons en attente | `nb_liaisons_en_attente` | ⏳ | — |
| Messages (24h) | `nb_messages_24h` / `nb_messages_total` | 💬 | — |

#### 🎯 Critères d'acceptation

- Le dashboard admin affiche les 5 nouvelles cartes avec les compteurs corrects
- Chaque compteur est calculé avec une seule requête SQL (`count()` ou `aggregate`)
- La carte « Enseignants » est cliquable et mène à `admin_enseignants`
- La carte « Élèves sans enseignant » est cliquable et mène à `admin_eleves_orphelins`
- La carte « Élèves sans enseignant » affiche un style d'alerte (bordure orange/rouge) si `nb_orphelins > 0`
- Les compteurs sont calculés en temps réel (pas de cache) car le dashboard admin est peu fréquenté

#### 🏗 Architecture

- `_get_eleves_orphelins_qs()` réutilisé (étape 6.4)
- Compteurs via `.count()` — requêtes SQL simples et rapides
- Pas de cache : le dashboard admin est consulté rarement, la fraîcheur est plus importante

#### 🔒 Sécurité

- Le dashboard admin est déjà protégé par `is_admin` — pas de changement de contrôle d'accès

#### ⚡ Performance

- 6 requêtes SQL supplémentaires (tous des `.count()`) — acceptable pour le dashboard admin (budget ≤ 12)
- Pas de N+1 : chaque compteur est une requête isolée

#### ✅ Definition of Done

- [ ] 6 compteurs ajoutés au contexte de `_dashboard_admin`
- [ ] 5 cartes ajoutées au template dashboard admin
- [ ] Carte orphelins avec style alerte conditionnel
- [ ] Cartes cliquables vers `admin_enseignants` et `admin_eleves_orphelins`
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 3.2, 5 mises à jour

---

### 🧪 Tests Phase 6 (16 tests)

**Fichier** : `users/tests/test_admin_panel.py`

#### Tests `admin_enseignants_view` (4 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_admin_enseignants_anonyme_redirect_login` | — | `assertEqual(response.status_code, 302)` |
| 2 | `test_admin_enseignants_non_admin_403` | `eleve` | `assertEqual(response.status_code, 403)` |
| 3 | `test_admin_enseignants_admin_200_liste` | `admin_user`, `enseignant` | `assertEqual(response.status_code, 200)`, `assertContains(response, enseignant.last_name)` |
| 4 | `test_admin_enseignants_filtre_recherche` | `admin_user`, `enseignant(last_name="Dupont")`, `enseignant2(last_name="Martin")` | `assertContains(response, "Dupont")`, `assertNotContains(response, "Martin")` (avec `?q=Dupont`) |

#### Tests `admin_enseignant_detail_view` (3 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 5 | `test_admin_enseignant_detail_admin_200` | `admin_user`, `enseignant`, `eleve`, `lien_enseignant_eleve_valide` | `assertContains(response, eleve.last_name)` |
| 6 | `test_admin_enseignant_detail_id_eleve_404` | `admin_user`, `eleve` | `assertEqual(response.status_code, 404)` (ID d'un élève, pas enseignant) |
| 7 | `test_admin_enseignant_detail_non_admin_403` | `enseignant` | `assertEqual(response.status_code, 403)` |

#### Tests `admin_eleves_orphelins_view` (3 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 8 | `test_admin_orphelins_admin_200` | `admin_user`, `eleve` (sans lien) | `assertContains(response, eleve.last_name)` |
| 9 | `test_admin_orphelins_exclut_eleve_lie` | `admin_user`, `eleve`, `enseignant`, `lien_enseignant_eleve_valide` | `assertNotContains(response, eleve.last_name)` |
| 10 | `test_admin_orphelins_inclut_eleve_lien_en_attente` | `admin_user`, `eleve`, `enseignant`, `lien_en_attente` | `assertContains(response, eleve.last_name)` |

#### Tests `admin_forcer_liaison_view` (3 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 11 | `test_forcer_liaison_admin_cree_lien_valide` | `admin_user`, `enseignant`, `eleve` | `assertTrue(LienEnseignantEleve.objects.filter(eleve=eleve, statut="valide").exists())` |
| 12 | `test_forcer_liaison_eleve_deja_lie_erreur` | `admin_user`, `enseignant`, `enseignant2`, `eleve`, `lien_enseignant_eleve_valide` | `assertEqual(LienEnseignantEleve.objects.filter(eleve=eleve, statut="valide").count(), 1)` |
| 13 | `test_forcer_liaison_get_405` | `admin_user` | `assertEqual(response.status_code, 405)` |

#### Tests `admin_supprimer_liaison_view` (2 tests)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 14 | `test_supprimer_liaison_admin_ok` | `admin_user`, `lien_enseignant_eleve_valide` | `assertFalse(LienEnseignantEleve.objects.filter(pk=lien.pk).exists())` |
| 15 | `test_supprimer_liaison_non_admin_403` | `eleve`, `lien_enseignant_eleve_valide` | `assertEqual(response.status_code, 403)` |

#### Tests compteurs dashboard admin (1 test)

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 16 | `test_dashboard_admin_compteurs_corrects` | `admin_user`, `enseignant`, 2 `eleve` (1 lié, 1 orphelin), `parent_user` | `assertEqual(response.context["nb_enseignants"], 1)`, `assertEqual(response.context["nb_orphelins"], 1)`, `assertEqual(response.context["nb_parents"], 1)` |

**Fixtures Phase 6** (en complément des fixtures existantes dans `conftest.py`) :

```python
@pytest.fixture
def enseignant2(db):
    return CustomUser.objects.create_user(
        email="enseignant2@test.fr",
        password="testpass123",
        role=RoleChoices.ENSEIGNANT,
        first_name="Marie",
        last_name="Martin",
    )

@pytest.fixture
def lien_en_attente(enseignant, eleve):
    return LienEnseignantEleve.objects.create(
        enseignant=enseignant,
        eleve=eleve,
        statut=StatutLienChoices.EN_ATTENTE,
    )
```

---

### Résumé des changements par fichier — Phase 6

| Fichier | Action |
|---------|--------|
| `users/admin.py` | Enregistrer `LienEnseignantEleve`, `LienParentEleve`, `Notification`, `Conversation`, `Message` |
| `users/views.py` | Ajouter `admin_enseignants_view`, `admin_enseignant_detail_view`, `admin_eleves_orphelins_view`, `admin_forcer_liaison_view`, `admin_supprimer_liaison_view`, `_get_eleves_orphelins_qs()` ; enrichir `_dashboard_admin` |
| `users/urls.py` | Ajouter 5 URLs : `admin_enseignants`, `admin_enseignant_detail`, `admin_eleves_orphelins`, `admin_forcer_liaison`, `admin_supprimer_liaison` |
| `templates/dashboard/admin_enseignants.html` | **Nouveau** — tableau enseignants avec recherche, tri, pagination |
| `templates/dashboard/admin_enseignant_detail.html` | **Nouveau** — stats classe + tableau élèves d'un enseignant |
| `templates/dashboard/admin_eleves_orphelins.html` | **Nouveau** — tableau élèves sans enseignant + bouton assigner |
| Template dashboard admin existant | Ajouter 5 cartes compteurs |
| `users/tests/test_admin_panel.py` | **Nouveau** — 16 tests panel admin (délégué à `test-writer`) |
| `users/tests/conftest.py` | Ajouter fixtures `enseignant2`, `lien_en_attente` |
| `CODEBASE_REFERENCE.md` | Sections 2.2, 3.2, 5, 8 mises à jour |

### Ordre d'exécution recommandé

```
1. Implementer  → Étape 6.1 (admin.py register)
2. Implementer  → Étape 6.2 (admin_enseignants_view + template)
3. Implementer  → Étape 6.3 (admin_enseignant_detail_view + template)
4. Implementer  → Étape 6.4 (admin_eleves_orphelins_view + template + helper)
5. Implementer  → Étape 6.5 (forcer/supprimer liaisons POST)
6. Implementer  → Étape 6.6 (compteurs dashboard admin)
7. Test Writer  → 16 tests dans users/tests/test_admin_panel.py
8. Implementer  → Mise à jour CODEBASE_REFERENCE.md
```

---

## Phase 7 — Seed data + preview enseignant

> **Objectif** : fournir un jeu de données de test réaliste pour le système multi-rôles (enseignants, élèves avec et sans liaisons, parents, progressions) et permettre à l'admin de simuler la vue d'un enseignant spécifique via le mode preview. Cette phase est le pendant du seed/preview existant pour les élèves, adapté au nouveau rôle enseignant.

### Décisions d'architecture (Phase 7)

| Décision | Justification |
|----------|---------------|
| Management command `seed_roles_test` dans `users/management/commands/` | Cohérent avec les seeds existants (`seed_data`, `seed_chimie_seconde`, etc.) dans `courses/management/commands/`. Placé dans `users/` car les objets créés sont des utilisateurs et liaisons |
| Emails `@test.fr` uniquement | Convention sécurité : aucun vrai domaine email dans les seeds. Jamais `@gmail.com`, `@yahoo.fr`, etc. |
| Preview enseignant via session | Pattern identique au `preview_niveau` existant : clé de session + bannière jaune + bouton sidebar. Réutilise le mécanisme prouvé |
| Adaptation `exit_preview_view` plutôt que nouvelle vue | Moins de code, cohérent : un seul point de sortie pour tous les modes preview |

---

### Étape 7.1 — `seed_roles_test` management command

**Fichier** : `users/management/commands/seed_roles_test.py`

**Commande idempotente** qui crée :

```python
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from datetime import timedelta
import random

from users.models import (
    CustomUser, RoleChoices, LienEnseignantEleve, LienParentEleve,
    StatutLienChoices, Notification, TypeNotificationChoices,
)
from progress.models import UserProgression, UserQuizResultat
from courses.models import Lecon, Quiz


class Command(BaseCommand):
    help = "Crée un jeu de données multi-rôles pour les tests (idempotent)."

    def handle(self, *args, **options):
        with transaction.atomic():
            self._creer_enseignants()
            self._creer_eleves()
            self._creer_parents()
            self._creer_liaisons()
            self._creer_progressions()
            self._creer_connexions_fictives()
            self._creer_notifications()

        self.stdout.write(self.style.SUCCESS("Seed multi-rôles terminé."))
```

**Données créées** :

| Type | Détail | Email |
|------|--------|-------|
| Enseignant 1 | Jean Professeur | `jean.professeur@test.fr` |
| Enseignant 2 | Claire Mentor | `claire.mentor@test.fr` |
| Élève 1 | Lucas Apprenant (Seconde) — lié à Enseignant 1 | `lucas.apprenant@test.fr` |
| Élève 2 | Emma Studieuse (Première) — liée à Enseignant 1 | `emma.studieuse@test.fr` |
| Élève 3 | Hugo Curieux (Terminale) — lié à Enseignant 2 | `hugo.curieux@test.fr` |
| Élève 4 | Léa Brillante (Seconde) — liée à Enseignant 2 | `lea.brillante@test.fr` |
| Élève 5 | Nathan Orphelin (Première) — **sans enseignant** | `nathan.orphelin@test.fr` |
| Élève 6 | Chloé Seule (Terminale) — **sans enseignant** | `chloe.seule@test.fr` |
| Parent 1 | Marc Papa — parent de Lucas | `marc.papa@test.fr` |
| Parent 2 | Sophie Maman — parent de Lucas | `sophie.maman@test.fr` |
| Parent 3 | Pierre Père — parent d'Emma | `pierre.pere@test.fr` |
| Parent 4 | Anne Mère — parent d'Hugo | `anne.mere@test.fr` |
| Parent 5 | David Parent — parent de Léa | `david.parent@test.fr` |
| Parent 6 | Julie Famille — parent de Nathan (orphelin) | `julie.famille@test.fr` |
| Parent 7 | Thomas Tuteur — parent de Chloé (orphelin) | `thomas.tuteur@test.fr` |
| Parent 8 | Isabelle Garde — parent d'Hugo (2e parent) | `isabelle.garde@test.fr` |

**Liaisons** :

| Lien | Type | Statut |
|------|------|--------|
| Enseignant 1 ↔ Lucas | Enseignant-Élève | `VALIDE` |
| Enseignant 1 ↔ Emma | Enseignant-Élève | `VALIDE` |
| Enseignant 2 ↔ Hugo | Enseignant-Élève | `VALIDE` |
| Enseignant 2 ↔ Léa | Enseignant-Élève | `VALIDE` |
| Marc Papa ↔ Lucas | Parent-Élève | `VALIDE` |
| Sophie Maman ↔ Lucas | Parent-Élève | `VALIDE` |
| Pierre Père ↔ Emma | Parent-Élève | `VALIDE` |
| Anne Mère ↔ Hugo | Parent-Élève | `VALIDE` |
| Isabelle Garde ↔ Hugo | Parent-Élève | `VALIDE` |
| David Parent ↔ Léa | Parent-Élève | `VALIDE` |
| Julie Famille ↔ Nathan | Parent-Élève | `VALIDE` |
| Thomas Tuteur ↔ Chloé | Parent-Élève | `VALIDE` |

**Progressions fictives** (réparties aléatoirement) :

- Lucas : 60% leçons terminées, score moyen 75%
- Emma : 80% leçons terminées, score moyen 85%
- Hugo : 40% leçons terminées, score moyen 60%
- Léa : 90% leçons terminées, score moyen 92%
- Nathan : 20% leçons terminées, score moyen 50%
- Chloé : 10% leçons terminées, score moyen 40%

**Connexions fictives** (derniers 90 jours) :

Simuler des `last_login` variés pour tester la heatmap sur les fiches élèves :

```python
def _creer_connexions_fictives(self):
    """Simule des dates de dernière connexion variées."""
    now = timezone.now()
    connexions = {
        "lucas.apprenant@test.fr": now - timedelta(hours=2),
        "emma.studieuse@test.fr": now - timedelta(days=1),
        "hugo.curieux@test.fr": now - timedelta(days=7),
        "lea.brillante@test.fr": now - timedelta(hours=30),
        "nathan.orphelin@test.fr": now - timedelta(days=30),
        "chloe.seule@test.fr": now - timedelta(days=60),
    }
    for email, last_login in connexions.items():
        CustomUser.objects.filter(email=email).update(last_login=last_login)
```

**Notifications de test** :

- 2 notifications `LIEN_VALIDE` pour Enseignant 1 (de Lucas et Emma)
- 1 notification `DEMANDE_LIAISON` pour Nathan (lien parent en attente… non : Julie est validée, mais on peut ajouter un lien en attente d'un 2e parent fictif)
- 3 notifications lues, 2 non lues pour tester les compteurs

**Idempotence** :

```python
def _creer_enseignants(self):
    """Crée les enseignants de test (idempotent via get_or_create)."""
    enseignants = [
        {"email": "jean.professeur@test.fr", "first_name": "Jean", "last_name": "Professeur"},
        {"email": "claire.mentor@test.fr", "first_name": "Claire", "last_name": "Mentor"},
    ]
    for data in enseignants:
        user, created = CustomUser.objects.get_or_create(
            email=data["email"],
            defaults={
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "role": RoleChoices.ENSEIGNANT,
                "is_active": True,
            },
        )
        if created:
            user.set_password("testpass123")
            user.save()
            self.stdout.write(f"  Enseignant créé : {data['email']}")
        else:
            self.stdout.write(f"  Enseignant existant : {data['email']}")
```

Même pattern `get_or_create` pour élèves, parents, liaisons, progressions.

#### 🎯 Critères d'acceptation

- `python manage.py seed_roles_test` crée 2 enseignants, 6 élèves, 8 parents
- Les 12 liaisons sont créées avec les bons statuts
- Nathan et Chloé n'ont PAS de liaison enseignant → apparaissent dans le pool orphelins
- Hugo a 2 parents liés (Anne + Isabelle) — cas max parents = 2 validé
- Lucas a 2 parents liés (Marc + Sophie) — cas max parents = 2 validé
- Les progressions sont créées avec des répartitions variées
- Les `last_login` sont variés sur les 90 derniers jours
- La commande est idempotente : exécutée 2 fois → même résultat, pas de doublon
- Tous les emails utilisent le domaine `@test.fr`
- Le mot de passe de tous les comptes test est `testpass123`
- La commande s'exécute dans un `transaction.atomic()` global

#### 🏗 Architecture

- `get_or_create()` pour chaque entité → idempotence native
- `bulk_create()` pour les progressions et quiz résultats (volume potentiellement élevé)
- `transaction.atomic()` global — tout ou rien
- Méthodes privées par type d'entité (`_creer_enseignants`, `_creer_eleves`, etc.) — lisibilité
- Les progressions sont créées sur les leçons existantes (`Lecon.objects.all()`) — la commande dépend des seeds de contenu préalables

#### 🔒 Sécurité

- **Emails `@test.fr`** : aucun vrai domaine → pas d'envoi accidentel
- **Mot de passe `testpass123`** : acceptable pour des comptes de test ; la commande ne doit PAS être exécutée en production (ajouter un guard `if not settings.DEBUG`)
- **Guard en production** :
  ```python
  def handle(self, *args, **options):
      if not settings.DEBUG:
          self.stderr.write(self.style.ERROR(
              "Cette commande ne peut pas être exécutée en production."
          ))
          return
      # ...
  ```

#### ⚡ Performance

- `bulk_create()` pour les progressions : 1 requête INSERT au lieu de N
- `get_or_create()` pour les utilisateurs et liaisons : acceptable (volume faible, < 20 entités)
- `transaction.atomic()` global : un seul commit pour toutes les insertions

#### ✅ Definition of Done

- [ ] `seed_roles_test.py` créé dans `users/management/commands/`
- [ ] 2 enseignants, 6 élèves, 8 parents créés avec `@test.fr`
- [ ] 12 liaisons créées (10 enseignant-élève + parent-élève validées, 2 orphelins confirmés)
- [ ] Progressions fictives variées pour les 6 élèves
- [ ] Connexions fictives (`last_login`) sur 90 jours
- [ ] Commande idempotente (`get_or_create`)
- [ ] Guard `if not settings.DEBUG` empêchant l'exécution en production
- [ ] `CODEBASE_REFERENCE.md` section 7 (Management Commands) mise à jour

---

### Étape 7.2 — Preview enseignant

**Fichier** : `users/views.py`, `users/urls.py`, `templates/base.html`

**Concept** : l'admin peut « se glisser dans la peau » d'un enseignant pour voir exactement son dashboard, ses élèves, ses conversations — sans créer de compte enseignant fictif.

**Vue d'activation** :

```python
@login_required
def preview_enseignant_view(request, enseignant_id):
    """Active le mode preview enseignant pour un admin."""
    if not request.user.is_admin:
        return HttpResponseForbidden()

    enseignant = get_object_or_404(
        CustomUser, pk=enseignant_id, role=RoleChoices.ENSEIGNANT,
    )

    request.session["preview_enseignant_id"] = enseignant.pk
    request.session["preview_enseignant_nom"] = enseignant.nom_complet

    # Nettoyer le preview niveau si actif (un seul mode preview à la fois)
    request.session.pop("preview_niveau", None)

    messages.info(request, f"Mode preview enseignant activé : {enseignant.nom_complet}")
    return redirect("dashboard")
```

#### URL

```python
# users/urls.py (ajout)
path("preview-enseignant/<int:enseignant_id>/", preview_enseignant_view, name="preview_enseignant"),
```

**Comportement des vues en mode preview** :

Quand `request.session.get("preview_enseignant_id")` est défini :

1. **Dashboard** : affiche le dashboard enseignant au lieu du dashboard admin, avec les données de l'enseignant ciblé
2. **Fiche élève** : accessible pour les élèves liés à l'enseignant en preview
3. **Liste conversations** : affiche les conversations de l'enseignant en preview
4. **Notifications** : affiche les notifications de l'enseignant en preview

**Pattern dans les vues concernées** :

```python
def _get_preview_ou_user(request):
    """Retourne l'enseignant en preview si actif, sinon request.user."""
    preview_id = request.session.get("preview_enseignant_id")
    if preview_id and request.user.is_admin:
        try:
            return CustomUser.objects.get(pk=preview_id, role=RoleChoices.ENSEIGNANT)
        except CustomUser.DoesNotExist:
            # Enseignant supprimé entre-temps → nettoyer la session
            request.session.pop("preview_enseignant_id", None)
            request.session.pop("preview_enseignant_nom", None)
    return request.user
```

**Bannière jaune dans `base.html`** :

```html
{% if request.session.preview_enseignant_id %}
<div class="bg-yellow-100 border-b border-yellow-300 px-4 py-2 text-center text-yellow-800 text-sm">
    👁️ Mode preview enseignant : <strong>{{ request.session.preview_enseignant_nom }}</strong>
    <a href="{% url 'exit_preview' %}"
       class="ml-4 underline text-yellow-900 hover:text-yellow-700">
        Quitter le mode preview
    </a>
</div>
{% endif %}
```

**Boutons dans la sidebar admin** (visible uniquement pour les admins, dans la section panel admin) :

Sur la page `admin_enseignant_detail`, ajouter un bouton :

```html
<a href="{% url 'preview_enseignant' enseignant.pk %}"
   class="inline-flex items-center px-3 py-1.5 bg-yellow-500 text-white text-sm rounded-lg hover:bg-yellow-600">
    👁️ Simuler la vue enseignant
</a>
```

**Règles de preview enseignant** :

- Aucune écriture en base : pas de création de message, notification, ou modification de lien pendant le preview
- Les formulaires POST dans les vues de messagerie et de liaisons retournent 403 si le mode preview est actif :
  ```python
  if request.session.get("preview_enseignant_id"):
      return HttpResponseForbidden("Action interdite en mode preview.")
  ```
- Un seul mode preview à la fois : activer le preview enseignant désactive le preview niveau, et vice-versa

#### 🎯 Critères d'acceptation

- `GET /preview-enseignant/42/` avec admin → active le mode, redirige vers dashboard
- `GET /preview-enseignant/42/` avec non-admin → 403
- `GET /preview-enseignant/42/` anonyme → redirect login
- `GET /preview-enseignant/99999/` → 404
- `GET /preview-enseignant/42/` où user 42 est un élève → 404
- Le dashboard affiche les données de l'enseignant en preview (ses élèves, pas ceux de l'admin)
- La bannière jaune s'affiche sur toutes les pages pendant le preview
- Activer le preview enseignant désactive le preview niveau si actif
- Les actions POST (envoi message, validation lien…) retournent 403 en mode preview
- Le bouton « Simuler la vue enseignant » apparaît sur la page détail enseignant admin
- `_get_preview_ou_user(request)` retourne l'enseignant en preview ou `request.user`

#### 🏗 Architecture

- `request.session["preview_enseignant_id"]` : clé de session (int, PK de l'enseignant)
- `request.session["preview_enseignant_nom"]` : nom complet pour affichage dans la bannière (évite une requête supplémentaire par page)
- `_get_preview_ou_user(request)` : helper centralisé dans `users/views.py` — utilisé par les vues dashboard enseignant, fiche élève, messagerie
- Exclusion mutuelle des previews : `pop("preview_niveau")` quand on active preview enseignant, `pop("preview_enseignant_id")` + `pop("preview_enseignant_nom")` quand on active preview niveau
- Guard POST en preview : vérification au début de chaque vue POST dans les vues enseignant

#### 🔒 Sécurité

- **Admin-only** : seul un admin peut activer le preview
- **IDOR** : `get_object_or_404` avec `role=RoleChoices.ENSEIGNANT` — impossible de preview un élève ou parent
- **Aucune écriture** : toutes les vues POST vérifient l'absence de `preview_enseignant_id` avant d'agir
- **Session fixation** : les clés de session sont les mêmes que pour le preview niveau — pattern déjà sécurisé
- **Nettoyage** : si l'enseignant en preview est supprimé, `_get_preview_ou_user` nettoie la session automatiquement

#### ⚡ Performance

- Le nom de l'enseignant est stocké en session → pas de requête supplémentaire pour la bannière
- `_get_preview_ou_user` fait au maximum 1 requête (lookup par PK, indexé) — uniquement si le preview est actif

#### ✅ Definition of Done

- [ ] `preview_enseignant_view` implémenté dans `users/views.py`
- [ ] `_get_preview_ou_user(request)` helper implémenté
- [ ] URL `preview_enseignant` enregistrée dans `users/urls.py`
- [ ] Bannière jaune dans `base.html` pour le mode preview enseignant
- [ ] Bouton « Simuler » sur la page `admin_enseignant_detail.html`
- [ ] Exclusion mutuelle avec le preview niveau
- [ ] Guard POST en preview sur les vues d'écriture
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` sections 2.2, 3.2, 5, 8 mises à jour

---

### Étape 7.3 — Adapter `exit_preview_view`

**Fichier** : `users/views.py`

**Modification** de la vue existante pour gérer les deux types de preview :

```python
@login_required
def exit_preview_view(request):
    """Quitte le mode preview actif (niveau ou enseignant)."""
    if not request.user.is_admin:
        return HttpResponseForbidden()

    preview_ens = request.session.pop("preview_enseignant_id", None)
    request.session.pop("preview_enseignant_nom", None)
    preview_niv = request.session.pop("preview_niveau", None)

    if preview_ens:
        messages.info(request, "Mode preview enseignant désactivé.")
    elif preview_niv:
        messages.info(request, "Mode preview niveau désactivé.")

    return redirect("dashboard")
```

**Changements** :

- La vue existante nettoie uniquement `preview_niveau` → maintenant elle nettoie aussi `preview_enseignant_id` et `preview_enseignant_nom`
- L'URL `exit_preview` reste la même — pas de changement d'URL
- Le message de confirmation indique quel type de preview a été désactivé

#### 🎯 Critères d'acceptation

- `GET /exit-preview/` avec preview enseignant actif → nettoie les 2 clés de session (`preview_enseignant_id`, `preview_enseignant_nom`), message info, redirect dashboard
- `GET /exit-preview/` avec preview niveau actif → nettoie `preview_niveau`, message info, redirect dashboard (comportement existant préservé)
- `GET /exit-preview/` sans aucun preview actif → redirect dashboard silencieux (pas d'erreur)
- `GET /exit-preview/` avec non-admin → 403
- Après `exit_preview`, le dashboard affiche les données admin normales

#### 🏗 Architecture

- `session.pop()` avec valeur par défaut `None` → pas d'erreur si la clé n'existe pas
- Nettoyage des 3 clés possibles à chaque appel — filet de sécurité contre les clés orphelines
- Pas de nouvelle URL → modification in-place de la vue existante

#### 🔒 Sécurité

- **Admin-only** : vérification conservée
- **Nettoyage complet** : les 3 clés de session sont toujours nettoyées → pas de clé orpheline possible
- **Redirect fixe** : toujours vers `dashboard` (nom d'URL), pas de paramètre externe

#### ⚡ Performance

- 0 requête SQL (hors auth/session middleware) — uniquement des opérations `session.pop()`

#### ✅ Definition of Done

- [ ] `exit_preview_view` adapté pour gérer preview enseignant + niveau
- [ ] Les 3 clés de session sont nettoyées (`preview_enseignant_id`, `preview_enseignant_nom`, `preview_niveau`)
- [ ] Message de confirmation conditionnel selon le type de preview
- [ ] Comportement existant pour preview niveau préservé (non-régression)
- [ ] Tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` section 3.2 mise à jour

---

### 🧪 Tests Phase 7 (14 tests)

**Fichier** : `users/tests/test_seed_roles.py` (8 tests) + `users/tests/test_preview_enseignant.py` (6 tests)

#### Tests `seed_roles_test` (8 tests) — `test_seed_roles.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_seed_cree_2_enseignants` | — (lance la commande) | `assertEqual(CustomUser.objects.filter(role="enseignant").count(), 2)` |
| 2 | `test_seed_cree_6_eleves` | — | `assertEqual(CustomUser.objects.filter(role="eleve").count(), base_count + 6)` |
| 3 | `test_seed_cree_8_parents` | — | `assertEqual(CustomUser.objects.filter(role="parent").count(), 8)` |
| 4 | `test_seed_liaison_enseignant_eleve_4_valide` | — | `assertEqual(LienEnseignantEleve.objects.filter(statut="valide").count(), 4)` |
| 5 | `test_seed_orphelins_2_eleves_sans_enseignant` | — | `assertEqual(_get_eleves_orphelins_qs().count(), 2)` — Nathan + Chloé |
| 6 | `test_seed_hugo_2_parents` | — | `assertEqual(LienParentEleve.objects.filter(eleve__email="hugo.curieux@test.fr", statut="valide").count(), 2)` |
| 7 | `test_seed_idempotent_double_execution` | — | Exécuter 2 fois → `assertEqual(CustomUser.objects.filter(role="enseignant").count(), 2)` (pas de doublon) |
| 8 | `test_seed_emails_domaine_test_fr` | — | `assertTrue(all(u.email.endswith("@test.fr") for u in CustomUser.objects.exclude(role="admin")))` (scope seed) |

#### Tests preview enseignant (6 tests) — `test_preview_enseignant.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 9 | `test_preview_enseignant_admin_active_session` | `admin_user`, `enseignant` | `assertEqual(client.session["preview_enseignant_id"], enseignant.pk)` |
| 10 | `test_preview_enseignant_non_admin_403` | `eleve` | `assertEqual(response.status_code, 403)` |
| 11 | `test_preview_enseignant_id_eleve_404` | `admin_user`, `eleve` | `assertEqual(response.status_code, 404)` |
| 12 | `test_preview_enseignant_desactive_preview_niveau` | `admin_user`, `enseignant` + session `preview_niveau="seconde"` | `assertNotIn("preview_niveau", client.session)` |
| 13 | `test_exit_preview_enseignant_nettoie_session` | `admin_user` + session `preview_enseignant_id`, `preview_enseignant_nom` | `assertNotIn("preview_enseignant_id", client.session)`, `assertNotIn("preview_enseignant_nom", client.session)` |
| 14 | `test_exit_preview_sans_preview_actif_redirect_ok` | `admin_user` (aucun preview actif) | `assertEqual(response.status_code, 302)`, redirect vers dashboard |

**Fixtures Phase 7** (réutilisation des fixtures existantes `admin_user`, `enseignant`, `eleve` de `conftest.py`) :

Pas de nouvelle fixture nécessaire — les tests seed appellent la management command directement :

```python
from django.core.management import call_command

@pytest.fixture
def seed_roles(db):
    call_command("seed_roles_test")
```

---

### Résumé des changements par fichier — Phase 7

| Fichier | Action |
|---------|--------|
| `users/management/commands/seed_roles_test.py` | **Nouveau** — seed multi-rôles idempotent |
| `users/views.py` | Ajouter `preview_enseignant_view`, `_get_preview_ou_user()` ; modifier `exit_preview_view` |
| `users/urls.py` | Ajouter URL `preview_enseignant` |
| `templates/base.html` | Ajouter bannière jaune preview enseignant (en dessous de la bannière preview niveau) |
| `templates/dashboard/admin_enseignant_detail.html` | Ajouter bouton « Simuler la vue enseignant » |
| `users/tests/test_seed_roles.py` | **Nouveau** — 8 tests seed (délégué à `test-writer`) |
| `users/tests/test_preview_enseignant.py` | **Nouveau** — 6 tests preview (délégué à `test-writer`) |
| `CODEBASE_REFERENCE.md` | Sections 2.2, 3.2, 5, 7, 8 mises à jour |

### Ordre d'exécution recommandé

```
1. Implementer  → Étape 7.1 (seed_roles_test management command)
2. Implementer  → Étape 7.2 (preview_enseignant_view + helper + bannière + bouton)
3. Implementer  → Étape 7.3 (adapter exit_preview_view)
4. Test Writer  → 8 tests dans users/tests/test_seed_roles.py
5. Test Writer  → 6 tests dans users/tests/test_preview_enseignant.py
6. Implementer  → Mise à jour CODEBASE_REFERENCE.md
```

---

## Phase 8 — Migrations et déploiement

> **Objectif** : définir l'ordre exact des migrations pour introduire le système multi-rôles sans casser les comptes existants, garantir la rétrocompatibilité du parcours d'inscription, et vérifier qu'aucune nouvelle variable d'environnement n'est requise.

### Décisions d'architecture (Phase 8)

| Décision | Justification |
|----------|---------------|
| Migration en 3 étapes pour `code_identifiant` | Pattern standard (nullable → data migration → non-nullable + unique) pour éviter tout downtime ou perte de données sur les comptes existants |
| `secrets.token_hex(4)` dans la data migration | 8 caractères hex = 4 milliards de combinaisons possibles, suffisant pour le volume attendu. Module `secrets` (cryptographiquement sûr) plutôt que `random` |
| `bulk_update()` dans la data migration | Un seul UPDATE SQL au lieu de N `save()` unitaires — essentiel si la base contient des milliers d'utilisateurs |
| `reverse_code` obligatoire sur tous les `RunPython` | Toute migration doit être réversible pour permettre un rollback sûr en production |
| Indexes ajoutés dans la migration initiale | `db_index=True` sur `code_identifiant` et les FK des tables de liaison — pas de migration d'index séparée |
| `niveau` rendu nullable pour enseignants/parents | Les enseignants et parents n'ont pas de niveau scolaire. Nullable plutôt qu'une valeur sentinelle (pas de `"aucun"` dans `NiveauChoices`) |

---

### Étape 8.1 — Ordre des migrations

**7 migrations à créer dans l'ordre strict suivant** :

#### Migration 1 — Ajouter `code_identifiant` nullable

```python
# users/migrations/XXXX_add_code_identifiant_nullable.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("users", "XXXX_previous")]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="code_identifiant",
            field=models.CharField(
                max_length=8, null=True, blank=True,
                verbose_name="Code d'identification", db_index=True,
            ),
        ),
    ]
```

#### Migration 2 — Data migration : générer les codes existants

```python
# users/migrations/XXXX_backfill_code_identifiant.py
import secrets
from django.db import migrations

BATCH_SIZE = 500

def generer_codes(apps, schema_editor):
    """Génère un code_identifiant unique pour chaque utilisateur existant."""
    CustomUser = apps.get_model("users", "CustomUser")
    users = list(CustomUser.objects.filter(code_identifiant__isnull=True))
    codes_utilises = set(
        CustomUser.objects.exclude(code_identifiant__isnull=True)
        .values_list("code_identifiant", flat=True)
    )
    for user in users:
        code = secrets.token_hex(4)
        while code in codes_utilises:
            code = secrets.token_hex(4)
        user.code_identifiant = code
        codes_utilises.add(code)
    CustomUser.objects.bulk_update(users, ["code_identifiant"], batch_size=BATCH_SIZE)

def effacer_codes(apps, schema_editor):
    """Reverse : remet tous les code_identifiant à NULL."""
    CustomUser = apps.get_model("users", "CustomUser")
    CustomUser.objects.all().update(code_identifiant=None)

class Migration(migrations.Migration):
    dependencies = [("users", "XXXX_add_code_identifiant_nullable")]

    operations = [
        migrations.RunPython(generer_codes, reverse_code=effacer_codes),
    ]
```

#### Migration 3 — Rendre non-nullable + unique

```python
# users/migrations/XXXX_code_identifiant_non_nullable_unique.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("users", "XXXX_backfill_code_identifiant")]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="code_identifiant",
            field=models.CharField(
                max_length=8, unique=True, blank=True,
                verbose_name="Code d'identification", db_index=True,
            ),
        ),
    ]
```

#### Migration 4 — Ajouter choix de rôle enseignant/parent

```python
# users/migrations/XXXX_extend_role_choices.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("users", "XXXX_code_identifiant_non_nullable_unique")]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                max_length=10,
                choices=[
                    ("admin", "Administrateur"),
                    ("eleve", "Élève"),
                    ("enseignant", "Enseignant"),
                    ("parent", "Parent"),
                ],
                default="eleve",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="niveau",
            field=models.CharField(
                max_length=10,
                choices=[
                    ("seconde", "Seconde"),
                    ("premiere", "Première"),
                    ("terminale", "Terminale"),
                ],
                default="seconde",
                null=True,
                blank=True,
            ),
        ),
    ]
```

#### Migration 5 — Créer tables `LienEnseignantEleve`, `LienParentEleve`

```python
# users/migrations/XXXX_create_liens.py
from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):
    dependencies = [("users", "XXXX_extend_role_choices")]

    operations = [
        migrations.CreateModel(
            name="LienEnseignantEleve",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True)),
                ("statut", models.CharField(max_length=10, choices=[...], default="en_attente", db_index=True)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                ("date_validation", models.DateTimeField(null=True, blank=True)),
                ("enseignant", models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="liens_eleves")),
                ("eleve", models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lien_enseignant")),
            ],
            options={"unique_together": {("enseignant", "eleve")}},
        ),
        migrations.CreateModel(
            name="LienParentEleve",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True)),
                ("statut", models.CharField(max_length=10, choices=[...], default="en_attente", db_index=True)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                ("date_validation", models.DateTimeField(null=True, blank=True)),
                ("parent", models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="liens_enfants")),
                ("eleve", models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="liens_parents")),
            ],
            options={"unique_together": {("parent", "eleve")}},
        ),
    ]
```

#### Migration 6 — Créer table `Notification`

```python
# users/migrations/XXXX_create_notification.py
from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):
    dependencies = [("users", "XXXX_create_liens")]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True)),
                ("type", models.CharField(max_length=20, choices=[...], db_index=True)),
                ("titre", models.CharField(max_length=200)),
                ("message", models.TextField()),
                ("lue", models.BooleanField(default=False, db_index=True)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                ("destinataire", models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")),
                ("lien_url", models.CharField(max_length=200, blank=True, default="")),
            ],
        ),
    ]
```

#### Migration 7 — Créer tables `Conversation`, `Message`

```python
# users/migrations/XXXX_create_messagerie.py
from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):
    dependencies = [("users", "XXXX_create_notification")]

    operations = [
        migrations.CreateModel(
            name="Conversation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True)),
                ("sujet", models.CharField(max_length=200)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                ("date_dernier_message", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("participants", models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="conversations")),
            ],
            options={"ordering": ["-date_dernier_message"]},
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True)),
                ("contenu", models.TextField(max_length=5000)),
                ("date_envoi", models.DateTimeField(auto_now_add=True)),
                ("lu", models.BooleanField(default=False)),
                ("conversation", models.ForeignKey("Conversation", on_delete=models.CASCADE, related_name="messages")),
                ("auteur", models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages_envoyes")),
            ],
            options={"ordering": ["date_envoi"]},
        ),
    ]
```

#### 🎯 Critères d'acceptation

- Les 7 migrations s'enchaînent sans erreur : `python manage.py migrate users`
- Après migration 2 : **tous** les utilisateurs existants ont un `code_identifiant` non-null et unique
- Après migration 3 : la contrainte `UNIQUE` est effective — `INSERT` d'un doublon → `IntegrityError`
- Les migrations sont réversibles : `python manage.py migrate users XXXX_previous` revient à l'état initial sans perte de données (hors `code_identifiant`)
- Les nouveaux indexes (`db_index=True`) sont créés : `code_identifiant`, `statut` (liens et notifications), `lue` (notification), `date_dernier_message` (conversation)
- Les `unique_together` sur les liens empêchent les doublons enseignant-élève et parent-élève

#### 🏗 Architecture

- **`reverse_code` obligatoire** sur chaque `RunPython` : migration 2 utilise `effacer_codes` qui remet à `NULL` ; si un futur `RunPython` est ajouté, il doit aussi avoir un `reverse_code` (au minimum `migrations.RunPython.noop` avec commentaire justificatif)
- **`bulk_update()`** dans la data migration : `CustomUser.objects.bulk_update(users, ["code_identifiant"], batch_size=500)` — un seul `UPDATE` SQL au lieu de N `save()`
- **Indexes dans la migration initiale** : pas de migration d'index séparée, les `db_index=True` sont déclarés directement dans les `CreateModel` / `AddField`
- **Dépendances linéaires** : chaque migration dépend de la précédente → pas de conflit d'ordre

#### 🧪 Tests (6 tests) — `users/tests/test_migrations.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_migration_reversible_code_identifiant` | `migrator` (django-test-migrations ou `MigrationExecutor`) — applique migration 3 puis reverse à migration 1 | `assertIsNone(user.code_identifiant)` après reverse ; `assertTrue(migration_recorder.applied("XXXX_add_code_identifiant_nullable"))` au retour |
| 2 | `test_data_migration_genere_codes_existants` | 3 `CustomUser` créés avant migration 2 (appliquée via `MigrationExecutor`) | `assertEqual(CustomUser.objects.filter(code_identifiant__isnull=False).count(), 3)` ; `assertEqual(len(set(codes)), 3)` (unicité) ; `assertTrue(all(len(c) == 8 for c in codes))` |
| 3 | `test_backward_compat_inscription_redirige_choix_role` | `client` (anonyme) | `response = client.get("/inscription/")` → `assertEqual(response.status_code, 200)` ou `assertRedirects(response, "/inscription/choix-role/")` — selon implémentation Phase 2 ; vérifie que le formulaire d'inscription existant reste accessible |
| 4 | `test_utilisateurs_existants_role_eleve_inchange` | 2 `CustomUser(role="eleve")` créés avant migration 4 | `assertEqual(user.role, "eleve")` après migration 4 ; `assertTrue(user.is_eleve)` ; `assertFalse(user.is_enseignant)` |
| 5 | `test_niveau_nullable_pour_enseignant` | `CustomUser(role="enseignant", niveau=None)` | `user.full_clean()` ne lève pas de `ValidationError` ; `assertIsNone(user.niveau)` |
| 6 | `test_niveau_nullable_pour_parent` | `CustomUser(role="parent", niveau=None)` | `user.full_clean()` ne lève pas de `ValidationError` ; `assertIsNone(user.niveau)` |

#### 🔒 Sécurité

- **`secrets.token_hex(4)`** : module `secrets` (cryptographiquement sûr) — jamais `random.choice()` pour des identifiants utilisateur
- **Pas de perte d'accès** : les comptes existants conservent leur rôle `eleve` ou `admin`, leur mot de passe, leur email vérifié. Aucun champ existant n'est supprimé ou modifié (hors ajout `code_identifiant`)
- **Unicité garantie** : la boucle `while code in codes_utilises` dans la data migration prévient les collisions ; la contrainte `UNIQUE` en migration 3 est un filet de sécurité DB

#### ⚡ Performance

- **Indexes dans la migration initiale** : `db_index=True` sur `code_identifiant`, `statut`, `lue`, `date_dernier_message` — pas de migration d'index séparée, pas de `ALTER TABLE ADD INDEX` en production après coup
- **`bulk_update(users, ["code_identifiant"], batch_size=500)`** : un seul `UPDATE` SQL par batch de 500 — scalable même avec des dizaines de milliers d'utilisateurs existants

#### ✅ Definition of Done

- [ ] 7 migrations créées et appliquées sans erreur
- [ ] Data migration génère des `code_identifiant` uniques pour tous les utilisateurs existants
- [ ] Reverse migration fonctionne : `migrate users XXXX_previous` → état initial
- [ ] Indexes `db_index=True` vérifiés dans le schéma DB
- [ ] `unique_together` sur les liens vérifié
- [ ] 6 tests passent (délégué à `test-writer`)
- [ ] `CODEBASE_REFERENCE.md` section 1 (Models) mise à jour

---

### Étape 8.2 — Rétrocompatibilité

**Objectif** : garantir que les comptes existants (admin + élèves) fonctionnent sans aucune action manuelle après les migrations, et que le parcours d'inscription redirige vers le choix de rôle.

**Règles de rétrocompatibilité** :

1. **Comptes existants fonctionnent** :
   - Tous les utilisateurs existants conservent leur rôle (`admin` ou `eleve`) — aucune data migration ne modifie le champ `role`
   - Les propriétés `is_admin`, `is_eleve` continuent de retourner les mêmes valeurs
   - Les dashboards élève et admin affichent les mêmes données qu'avant
   - Les progressions, quiz résultats, et chapitres débloqués sont intacts

2. **`niveau` nullable pour enseignants/parents** :
   - Le champ `niveau` est rendu `null=True, blank=True` en migration 4
   - Les élèves existants conservent leur `niveau` (non-null) — la data migration ne touche pas ce champ
   - Les enseignants et parents peuvent être créés avec `niveau=None`
   - Les vues qui filtrent par `niveau` (ex: `matieres_view`) doivent gérer `niveau=None` gracieusement — un enseignant ou parent accédant à `/matieres/` voit toutes les matières sans filtre de niveau
   - Le formulaire d'inscription enseignant/parent ne demande PAS le niveau

3. **`/inscription/` redirige vers choix rôle** :
   - L'URL `/inscription/` existante redirige vers `/inscription/choix-role/` (nouvelle page)
   - La page choix-rôle propose 3 boutons : « Élève », « Enseignant », « Parent »
   - Chaque bouton mène au formulaire d'inscription spécifique au rôle
   - Le formulaire élève reste identique à l'actuel (+ champ optionnel code enseignant)
   - Les liens existants vers `/inscription/` (emails, bookmarks) continuent de fonctionner via redirect

#### 🎯 Critères d'acceptation

- Un admin existant se connecte → dashboard admin identique, toutes ses données accessibles
- Un élève existant se connecte → dashboard élève identique, progressions intactes, niveau conservé
- `CustomUser(role="enseignant", niveau=None).full_clean()` ne lève pas de `ValidationError`
- `CustomUser(role="parent", niveau=None).full_clean()` ne lève pas de `ValidationError`
- `GET /inscription/` → redirect 302 vers `/inscription/choix-role/`
- `GET /inscription/choix-role/` → 200, affiche les 3 options de rôle
- Les 208 tests existants passent toujours (aucune régression)

#### 🏗 Architecture

- **Aucune modification des vues existantes** pour les rôles admin/eleve — les nouvelles propriétés (`is_enseignant`, `is_parent`) sont additives
- **Guard `niveau` dans les vues** : les vues qui accèdent à `request.user.niveau` doivent vérifier `if user.niveau:` avant de filtrer — pattern :
  ```python
  if user.niveau:
      chapitres = chapitres.filter(niveau=user.niveau)
  # sinon : pas de filtre niveau (enseignant/parent voit tout)
  ```
- **Redirect `/inscription/`** : modifier `InscriptionView` pour retourner un `HttpResponseRedirect` vers `/inscription/choix-role/` — ou créer une vue intermédiaire `choix_role_view`

#### 🧪 Tests (6 tests) — couverts par l'étape 8.1

Les 6 tests de l'étape 8.1 couvrent les scénarios de rétrocompatibilité :

| Test | Scénario couvert |
|------|------------------|
| `test_backward_compat_inscription_redirige_choix_role` | `/inscription/` → redirect vers choix rôle |
| `test_utilisateurs_existants_role_eleve_inchange` | Rôle élève préservé après migration |
| `test_niveau_nullable_pour_enseignant` | Enseignant avec `niveau=None` valide |
| `test_niveau_nullable_pour_parent` | Parent avec `niveau=None` valide |
| `test_migration_reversible_code_identifiant` | Rollback possible sans perte |
| `test_data_migration_genere_codes_existants` | Codes générés pour les existants |

#### 🔒 Sécurité

- **Pas de perte d'accès** : aucun champ existant supprimé, aucun mot de passe modifié, aucun `is_active` changé
- **Redirect sûr** : `/inscription/` redirige vers une URL interne fixe (`/inscription/choix-role/`), pas de paramètre externe dans le redirect
- **Énumération** : la page choix-rôle ne révèle pas d'information sensible — elle liste simplement les rôles disponibles

#### ⚡ Performance

- **Aucun impact** : les vues existantes ne changent pas de nombre de requêtes SQL
- **Guard `niveau`** : un `if` supplémentaire par vue, coût négligeable

#### ✅ Definition of Done

- [ ] Comptes admin existants fonctionnent sans régression
- [ ] Comptes élève existants fonctionnent sans régression (progressions, quiz, niveaux intacts)
- [ ] `niveau=None` accepté pour les rôles enseignant et parent
- [ ] `/inscription/` redirige vers `/inscription/choix-role/`
- [ ] Les 208 tests existants passent
- [ ] `CODEBASE_REFERENCE.md` sections 2.2, 3.2 mises à jour

---

### Étape 8.3 — Variables d'environnement

**Aucune nouvelle variable d'environnement requise.**

Les fonctionnalités de la Phase 8 utilisent exclusivement :

| Fonctionnalité | Source de config |
|----------------|-----------------|
| `code_identifiant` (génération) | `secrets.token_hex()` — module stdlib Python, aucune config externe |
| Nouveaux modèles (liaisons, notifications, messagerie) | Migrations Django standard — utilisent la `DATABASE_URL` existante |
| `niveau` nullable | Migration `AlterField` — aucune variable |
| Redirect `/inscription/` | URL Django interne — aucune variable |

**Variables existantes inchangées** :

- `DATABASE_URL` — PostgreSQL (déjà configurée)
- `SECRET_KEY` — utilisée pour les tokens de vérification email (déjà configurée)
- `SENTRY_DSN` — monitoring (déjà configurée, optionnelle)
- `FIRST_ADMIN_EMAIL` / `FIRST_ADMIN_PASSWORD` — seed admin (déjà configurées)

> **Note** : les variables pour Brevo SMTP (email), le cache Redis, etc. seront évaluées dans les phases suivantes si la messagerie nécessite des notifications email en temps réel.

#### 🎯 Critères d'acceptation

- Le fichier `.env.example` ne nécessite aucun ajout pour la Phase 8
- `docker compose up --build` démarre sans erreur avec le `.env` existant
- Les migrations s'appliquent sans variable d'environnement supplémentaire
- Les tests passent sans variable d'environnement supplémentaire

#### 🏗 Architecture

- Pas de nouveau service Docker (pas de Redis, pas de Celery) dans cette phase
- Pas de nouveau package Python requis pour les migrations

#### 🧪 Tests (0 tests supplémentaires)

Aucun test spécifique — la vérification se fait par l'exécution réussie de `docker compose up --build` et du pipeline CI existant.

#### 🔒 Sécurité

- **`secrets.token_hex()`** : pas de variable d'environnement pour la seed de génération — le module `secrets` utilise l'entropie système (`/dev/urandom`)
- **Pas de clé API** ajoutée dans cette phase — aucun risque de fuite de secret

#### ⚡ Performance

- Aucun impact — pas de nouveau service, pas de nouvelle dépendance

#### ✅ Definition of Done

- [ ] Aucune nouvelle variable dans `.env.example`
- [ ] `docker compose up --build` réussit avec le `.env` existant
- [ ] CI passe sans modification du workflow
- [ ] Documentation vérifiée : aucune instruction de setup supplémentaire

---

### 🧪 Tests Phase 8 (6 tests)

**Fichier** : `users/tests/test_migrations.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_migration_reversible_code_identifiant` | `migrator` — applique migration 3 puis reverse à migration 1 | `assertIsNone(user.code_identifiant)` après reverse ; migration re-applicable sans erreur |
| 2 | `test_data_migration_genere_codes_existants` | 3 `CustomUser` créés avant migration 2 | `assertEqual(CustomUser.objects.filter(code_identifiant__isnull=False).count(), 3)` ; `assertEqual(len(set(codes)), 3)` (unicité) ; `assertTrue(all(len(c) == 8 for c in codes))` (format hex 8 chars) |
| 3 | `test_backward_compat_inscription_redirige_choix_role` | `client` (anonyme) | `response = client.get("/inscription/")` → `assertRedirects(response, "/inscription/choix-role/")` ou `assertEqual(response.status_code, 200)` — vérifie que le formulaire existant reste accessible |
| 4 | `test_utilisateurs_existants_role_eleve_inchange` | 2 `CustomUser(role="eleve")` créés avant migration 4 | `assertEqual(user.role, "eleve")` après migration ; `assertTrue(user.is_eleve)` ; `assertFalse(user.is_enseignant)` ; `assertFalse(user.is_parent)` |
| 5 | `test_niveau_nullable_pour_enseignant` | `CustomUser(role="enseignant", niveau=None)` | `user.full_clean()` → pas de `ValidationError` ; `assertIsNone(user.niveau)` ; `assertTrue(user.is_enseignant)` |
| 6 | `test_niveau_nullable_pour_parent` | `CustomUser(role="parent", niveau=None)` | `user.full_clean()` → pas de `ValidationError` ; `assertIsNone(user.niveau)` ; `assertTrue(user.is_parent)` |

**Fixtures Phase 8** :

```python
# users/tests/conftest.py (ajouts)

@pytest.fixture
def eleve_existant(db):
    """Élève créé avant les migrations multi-rôles (simule un compte existant)."""
    return CustomUser.objects.create_user(
        email="ancien.eleve@test.fr",
        password="testpass123",
        role="eleve",
        niveau="seconde",
    )

@pytest.fixture
def enseignant_sans_niveau(db):
    """Enseignant avec niveau=None."""
    return CustomUser.objects.create_user(
        email="prof.test@test.fr",
        password="testpass123",
        role="enseignant",
        niveau=None,
    )

@pytest.fixture
def parent_sans_niveau(db):
    """Parent avec niveau=None."""
    return CustomUser.objects.create_user(
        email="parent.test@test.fr",
        password="testpass123",
        role="parent",
        niveau=None,
    )
```

---

### Résumé des changements par fichier — Phase 8

| Fichier | Action |
|---------|--------|
| `users/migrations/XXXX_add_code_identifiant_nullable.py` | **Nouveau** — ajoute `code_identifiant` CharField nullable |
| `users/migrations/XXXX_backfill_code_identifiant.py` | **Nouveau** — data migration `secrets.token_hex()` + `bulk_update()` |
| `users/migrations/XXXX_code_identifiant_non_nullable_unique.py` | **Nouveau** — `AlterField` → non-nullable + unique |
| `users/migrations/XXXX_extend_role_choices.py` | **Nouveau** — étend `RoleChoices`, rend `niveau` nullable |
| `users/migrations/XXXX_create_liens.py` | **Nouveau** — crée `LienEnseignantEleve`, `LienParentEleve` |
| `users/migrations/XXXX_create_notification.py` | **Nouveau** — crée `Notification` |
| `users/migrations/XXXX_create_messagerie.py` | **Nouveau** — crée `Conversation`, `Message` |
| `users/tests/test_migrations.py` | **Nouveau** — 6 tests (délégué à `test-writer`) |
| `users/tests/conftest.py` | Ajouter 3 fixtures (`eleve_existant`, `enseignant_sans_niveau`, `parent_sans_niveau`) |
| `CODEBASE_REFERENCE.md` | Section 1 (Models) mise à jour |

### Ordre d'exécution recommandé

```
1. Migration Writer → 7 migrations dans l'ordre strict (8.1)
2. Implementer      → Vérifier rétrocompatibilité dans les vues existantes (8.2)
3. Implementer      → Confirmer aucune variable d'environnement requise (8.3)
4. Test Writer      → 6 tests dans users/tests/test_migrations.py
5. Implementer      → Mise à jour CODEBASE_REFERENCE.md
```

---

## Phase 9 — Réservation, Calendrier et Facturation SAP

> **Objectif** : permettre la réservation de cours particuliers avec double validation (enseignant + élève/parent), pré-autorisation Stripe, synchronisation calendrier iCal, et génération de factures PDF conformes SAP.

### Décisions d'architecture (Phase 9)

| Décision | Justification |
|----------|---------------|
| Nouvelle app `tutoring/` | Séparation des responsabilités : la logique de réservation, paiement et facturation est distincte du contenu pédagogique (`courses/`) et de la progression (`progress/`) |
| Double validation avec machine à états | 4 états (`en_attente_enseignant` → `en_attente_eleve` → `valide` → `annule`) garantissent le consentement des deux parties avant capture du paiement |
| Stripe `capture_method='manual'` | Fonds bloqués dès la soumission, capturés uniquement après double validation — pas de débit sans accord mutuel |
| `services.py` pour Stripe | Isolation de la dépendance tierce — facilite le mock en test et le remplacement futur du provider |
| `calendar.py` pour .ics | Module dédié à la génération iCalendar — séparé des vues pour réutilisabilité |
| `facturation.py` pour PDF | Logique de facturation SAP isolée — WeasyPrint + template dédié, même pattern que `lecon_pdf_view` |
| Token unique par utilisateur pour flux .ics | Pas d'authentification session sur les URLs calendrier (les clients CalDAV ne supportent pas les cookies) — token opaque dans l'URL |
| Celery pour génération PDF asynchrone | Les factures PDF avec WeasyPrint sont lentes (~2-5s) — ne pas bloquer la requête HTTP |

---

### Étape 9.1 — Modèle CoursParticulier

**Objectif** : créer l'app `tutoring/` et le modèle `CoursParticulier` avec machine à états pour la double validation.

#### Modèle `CoursParticulier`

```python
# tutoring/models.py
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


class StatutCoursChoices(models.TextChoices):
    EN_ATTENTE_ENSEIGNANT = "en_attente_enseignant", "En attente de l'enseignant"
    EN_ATTENTE_ELEVE = "en_attente_eleve", "En attente de l'élève"
    VALIDE = "valide", "Validé"
    ANNULE = "annule", "Annulé"


class CoursParticulier(models.Model):
    enseignant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cours_enseignes",
        limit_choices_to={"role": "enseignant"},
    )
    eleve = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cours_suivis",
        limit_choices_to={"role": "eleve"},
    )
    parent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cours_enfants",
        limit_choices_to={"role": "parent"},
    )
    statut = models.CharField(
        max_length=30,
        choices=StatutCoursChoices.choices,
        default=StatutCoursChoices.EN_ATTENTE_ENSEIGNANT,
        db_index=True,
    )
    date_debut = models.DateTimeField()
    duree = models.PositiveIntegerField(help_text="Durée en minutes")
    tarif_horaire = models.DecimalField(max_digits=6, decimal_places=2)
    lieu = models.CharField(max_length=200)
    notes = models.TextField(blank=True, default="")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_debut"]
        indexes = [
            models.Index(fields=["enseignant", "statut"]),
            models.Index(fields=["eleve", "statut"]),
        ]

    def __str__(self):
        return f"Cours {self.pk} — {self.enseignant} → {self.eleve} ({self.get_statut_display()})"

    def clean(self):
        super().clean()
        if self.date_debut and self.date_debut < timezone.now():
            raise ValidationError({"date_debut": "La date de début doit être dans le futur."})
        if self.duree and self.duree < 15:
            raise ValidationError({"duree": "La durée minimale est de 15 minutes."})
        if self.duree and self.duree > 480:
            raise ValidationError({"duree": "La durée maximale est de 8 heures (480 minutes)."})
        if self.tarif_horaire is not None and self.tarif_horaire <= 0:
            raise ValidationError({"tarif_horaire": "Le tarif horaire doit être positif."})

    TRANSITIONS_VALIDES = {
        StatutCoursChoices.EN_ATTENTE_ENSEIGNANT: [
            StatutCoursChoices.EN_ATTENTE_ELEVE,
            StatutCoursChoices.ANNULE,
        ],
        StatutCoursChoices.EN_ATTENTE_ELEVE: [
            StatutCoursChoices.VALIDE,
            StatutCoursChoices.ANNULE,
        ],
        StatutCoursChoices.VALIDE: [
            StatutCoursChoices.ANNULE,
        ],
        StatutCoursChoices.ANNULE: [],
    }

    def transition_vers(self, nouveau_statut):
        """Valide et applique une transition d'état."""
        if nouveau_statut not in self.TRANSITIONS_VALIDES.get(self.statut, []):
            raise ValidationError(
                f"Transition invalide : {self.statut} → {nouveau_statut}"
            )
        self.statut = nouveau_statut
        self.save(update_fields=["statut", "date_modification"])
```

#### 🎯 Critères d'acceptation

- `POST /tutorat/demande/` crée un `CoursParticulier` avec `statut='en_attente_enseignant'`
- L'enseignant valide → `statut` passe à `en_attente_eleve`
- L'élève (ou parent lié) valide → `statut` passe à `valide`
- Toute tentative de transition invalide lève `ValidationError`
- Un cours annulé ne peut plus changer d'état
- Le champ `parent` est nullable — un cours peut exister sans parent lié
- `date_debut` dans le passé est refusée à la validation
- `duree` est bornée entre 15 et 480 minutes
- `tarif_horaire` est strictement positif
- Les indexes composites `(enseignant, statut)` et `(eleve, statut)` existent en DB

#### 🏗 Architecture

- **App `tutoring/`** : `models.py`, `views.py`, `urls.py`, `admin.py`, `services.py`, `calendar.py`, `facturation.py`
- **Machine à états dans le modèle** : méthode `transition_vers()` avec dictionnaire `TRANSITIONS_VALIDES` — pas de lib externe (django-fsm serait overkill)
- **Vues** : `demande_cours_view` (POST, `@login_required`), `valider_cours_view` (POST, vérifie rôle), `annuler_cours_view` (POST, vérifie ownership)
- **URLs** : `tutorat/demande/`, `tutorat/<int:pk>/valider/`, `tutorat/<int:pk>/annuler/`, `tutorat/mes-cours/`
- **Template** : `templates/tutoring/demande.html`, `mes_cours.html`, `detail_cours.html`
- **Admin** : `CoursParticulierAdmin` avec `list_filter = ["statut"]`, `list_display`, `search_fields`

#### 🧪 Tests (5 tests) — `tutoring/tests/test_cours_particulier.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_creation_cours_statut_initial` | `enseignant`, `eleve` via `force_login` | `assertEqual(cours.statut, "en_attente_enseignant")` |
| 2 | `test_transition_valide_enseignant_vers_eleve` | `CoursParticulier` en `en_attente_enseignant` | `cours.transition_vers("en_attente_eleve")` → `assertEqual(cours.statut, "en_attente_eleve")` |
| 3 | `test_transition_invalide_leve_erreur` | `CoursParticulier` en `annule` | `assertRaises(ValidationError, cours.transition_vers, "valide")` |
| 4 | `test_double_validation_complete` | `CoursParticulier` | `transition_vers("en_attente_eleve")` → `transition_vers("valide")` → `assertEqual(cours.statut, "valide")` |
| 5 | `test_clean_date_passee_refuse` | `CoursParticulier` avec `date_debut` hier | `assertRaises(ValidationError, cours.full_clean)` |

#### 🔒 Sécurité

- **Vérification de rôle** : seul un enseignant peut valider `en_attente_enseignant → en_attente_eleve` ; seul l'élève (ou son parent lié) peut valider `en_attente_eleve → valide`
- **Ownership check** : `valider_cours_view` et `annuler_cours_view` vérifient que `request.user` est bien `enseignant`, `eleve`, ou `parent` du cours — sinon HTTP 403
- **CSRF** : toutes les vues POST utilisent `{% csrf_token %}` (par défaut Django)
- **Rate limit** : réutiliser le pattern `_check_quiz_rate_limit()` adapté → `_check_tutorat_rate_limit(user_id)` — 10 demandes/heure max

#### ⚡ Performance

- **Indexes composites** : `(enseignant, statut)` et `(eleve, statut)` pour filtrer les cours par rôle et état sans full table scan
- **`select_related("enseignant", "eleve", "parent")`** dans les vues de listing — pas de N+1

#### ✅ Definition of Done

- [ ] App `tutoring/` créée avec `models.py`, `views.py`, `urls.py`, `admin.py`
- [ ] `CoursParticulier` avec les 4 statuts et transitions validées
- [ ] Vues de demande, validation, annulation et listing fonctionnelles
- [ ] Templates HTMX pour les interactions
- [ ] 5 tests passent
- [ ] `CODEBASE_REFERENCE.md` mis à jour (sections 1, 2, 3, 5)
- [ ] `config/settings/base.py` : `INSTALLED_APPS` inclut `tutoring`

---

### Étape 9.2 — Stripe Pre-auth & Capture

**Objectif** : intégrer Stripe avec pré-autorisation (`capture_method='manual'`). Les fonds sont bloqués à la soumission de la demande, capturés uniquement après double validation, et relâchés en cas d'annulation.

#### Modèle `PaiementCours`

```python
# tutoring/models.py (ajout)

class StatutPaiementChoices(models.TextChoices):
    EN_ATTENTE = "en_attente", "En attente"
    AUTORISE = "autorise", "Pré-autorisé"
    CAPTURE = "capture", "Capturé"
    ANNULE = "annule", "Annulé"
    ECHOUE = "echoue", "Échoué"


class PaiementCours(models.Model):
    cours = models.OneToOneField(
        CoursParticulier,
        on_delete=models.CASCADE,
        related_name="paiement",
    )
    stripe_payment_intent_id = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
    )
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    devise = models.CharField(max_length=3, default="eur")
    statut = models.CharField(
        max_length=20,
        choices=StatutPaiementChoices.choices,
        default=StatutPaiementChoices.EN_ATTENTE,
    )
    date_creation = models.DateTimeField(auto_now_add=True)
    date_capture = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Paiement {self.stripe_payment_intent_id} — {self.get_statut_display()}"
```

#### Service Stripe — `tutoring/services.py`

```python
# tutoring/services.py
import stripe
from django.conf import settings
from decimal import Decimal

stripe.api_key = settings.STRIPE_SECRET_KEY


def creer_preautorisation(cours_particulier):
    """Crée un PaymentIntent avec capture_method='manual'."""
    montant_cents = int(
        cours_particulier.tarif_horaire
        * Decimal(cours_particulier.duree)
        / Decimal("60")
        * 100
    )
    intent = stripe.PaymentIntent.create(
        amount=montant_cents,
        currency="eur",
        capture_method="manual",
        metadata={
            "cours_id": str(cours_particulier.pk),
            "enseignant_id": str(cours_particulier.enseignant_id),
            "eleve_id": str(cours_particulier.eleve_id),
        },
    )
    return intent


def capturer_paiement(payment_intent_id):
    """Capture un PaymentIntent pré-autorisé."""
    return stripe.PaymentIntent.capture(payment_intent_id)


def annuler_paiement(payment_intent_id):
    """Annule un PaymentIntent pré-autorisé (relâche les fonds)."""
    return stripe.PaymentIntent.cancel(payment_intent_id)
```

#### Webhook Stripe — `tutoring/views.py` (extrait)

```python
# tutoring/views.py (webhook)
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@csrf_exempt
@require_POST
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event["type"] == "payment_intent.amount_capturable_updated":
        _handle_preauth_success(event["data"]["object"])
    elif event["type"] == "payment_intent.canceled":
        _handle_payment_canceled(event["data"]["object"])
    elif event["type"] == "payment_intent.payment_failed":
        _handle_payment_failed(event["data"]["object"])

    return HttpResponse(status=200)
```

#### 🎯 Critères d'acceptation

- `POST /tutorat/demande/` crée un `CoursParticulier` statut `en_attente_enseignant` **ET** un `PaymentIntent` avec `capture_method='manual'`
- Le `PaiementCours` associé a `statut='autorise'` une fois la pré-autorisation confirmée par Stripe (via webhook)
- Quand le cours passe à `statut='valide'` (double validation), `capturer_paiement()` est appelé → `PaiementCours.statut='capture'`
- Quand le cours passe à `statut='annule'`, `annuler_paiement()` est appelé → `PaiementCours.statut='annule'` (fonds relâchés)
- Le webhook Stripe vérifie la signature — une requête sans signature valide reçoit HTTP 400
- Le `stripe_payment_intent_id` est unique en DB — pas de doublon possible

#### 🏗 Architecture

- **`tutoring/services.py`** : 3 fonctions pures (`creer_preautorisation`, `capturer_paiement`, `annuler_paiement`) — aucune logique de vue, aucun accès à `request`
- **Webhook** : `stripe_webhook_view` dans `tutoring/views.py`, URL `/tutorat/webhook/stripe/` — `@csrf_exempt` + `@require_POST`
- **Settings** : `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, `STRIPE_WEBHOOK_SECRET` dans `.env` et `config/settings/base.py`
- **Signal ou appel direct** : quand `transition_vers("valide")` est appelé, la vue appelle `capturer_paiement()` — pas de signal Django (trop implicite pour un side effect financier)
- **Montant** : calculé comme `tarif_horaire * duree / 60` en cents — arrondi au centime inférieur

#### 🧪 Tests (4 tests) — `tutoring/tests/test_stripe.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_creer_preautorisation_mock_stripe` | `CoursParticulier`, `@patch("tutoring.services.stripe.PaymentIntent.create")` | Mock retourne `{"id": "pi_test_123"}` ; `assertEqual(paiement.stripe_payment_intent_id, "pi_test_123")` ; `assertEqual(paiement.statut, "en_attente")` |
| 2 | `test_capturer_paiement_apres_double_validation` | `PaiementCours` avec `statut="autorise"`, `@patch("tutoring.services.stripe.PaymentIntent.capture")` | Après `transition_vers("valide")` → `assertEqual(paiement.statut, "capture")` |
| 3 | `test_annuler_paiement_relache_fonds` | `PaiementCours` avec `statut="autorise"`, `@patch("tutoring.services.stripe.PaymentIntent.cancel")` | Après `transition_vers("annule")` → `assertEqual(paiement.statut, "annule")` |
| 4 | `test_webhook_signature_invalide_retourne_400` | `client.post("/tutorat/webhook/stripe/", ...)` sans header `HTTP_STRIPE_SIGNATURE` | `assertEqual(response.status_code, 400)` |

#### 🔒 Sécurité

- **Webhook signature verification** : `stripe.Webhook.construct_event()` avec `STRIPE_WEBHOOK_SECRET` — rejette toute requête non signée par Stripe
- **PCI DSS** : aucun numéro de carte ne transite par le serveur — Stripe Elements ou Checkout côté client, seul le `PaymentIntent` est manipulé côté serveur
- **Secrets** : `STRIPE_SECRET_KEY` et `STRIPE_WEBHOOK_SECRET` dans les variables d'environnement uniquement — jamais dans le code source ou les logs
- **Idempotence** : le webhook vérifie `stripe_payment_intent_id` unique en DB avant de créer/modifier un `PaiementCours` — pas de double traitement
- **`@csrf_exempt` scoped** : uniquement sur la vue webhook (requise car Stripe envoie des requêtes POST sans cookie CSRF) — toutes les autres vues gardent la protection CSRF

#### ⚡ Performance

- **Appels Stripe async-ready** : les appels Stripe API (~200-500ms) se font dans la vue POST — si latence inacceptable, migrer vers Celery task dans une phase ultérieure
- **`select_related("cours")`** sur `PaiementCours` dans les vues webhook pour éviter le N+1

#### ✅ Definition of Done

- [ ] `PaiementCours` modèle créé avec `stripe_payment_intent_id` unique
- [ ] `tutoring/services.py` avec 3 fonctions Stripe (create, capture, cancel)
- [ ] Webhook Stripe fonctionnel avec vérification de signature
- [ ] Flux complet : demande → pre-auth → double validation → capture
- [ ] Flux annulation : annulation → fonds relâchés
- [ ] 4 tests passent (tous avec mock Stripe)
- [ ] Variables `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, `STRIPE_WEBHOOK_SECRET` documentées dans `.env.example`
- [ ] `CODEBASE_REFERENCE.md` mis à jour (sections 1, 2, 3, 6)

---

### Étape 9.3 — Sync calendrier .ics

**Objectif** : générer un flux iCalendar dynamique par utilisateur (enseignant, élève ou parent), sécurisé par token unique, compatible Google Calendar, Outlook et Apple Calendar.

#### Token calendrier — `tutoring/models.py` (ajout)

```python
# tutoring/models.py (ajout)
import secrets

class CalendrierToken(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="calendrier_token",
    )
    token = models.CharField(max_length=64, unique=True, db_index=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_dernier_acces = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(48)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Token calendrier — {self.user}"
```

#### Génération .ics — `tutoring/calendar.py`

```python
# tutoring/calendar.py
from icalendar import Calendar, Event
from django.utils import timezone


def generer_flux_ics(user, cours_queryset):
    """Génère un flux iCalendar RFC 5545 pour un utilisateur."""
    cal = Calendar()
    cal.add("prodid", "-//ScienceLycee//Cours Particuliers//FR")
    cal.add("version", "2.0")
    cal.add("calscale", "GREGORIAN")
    cal.add("x-wr-calname", f"Cours — {user.get_full_name() or user.email}")

    for cours in cours_queryset:
        event = Event()
        event.add("uid", f"cours-{cours.pk}@sciencelycee.fr")
        event.add("dtstart", cours.date_debut)
        event.add("dtend", cours.date_debut + timezone.timedelta(minutes=cours.duree))
        event.add("summary", f"Cours avec {cours.enseignant.get_full_name() or cours.enseignant.email}")
        event.add("location", cours.lieu)
        event.add("description", cours.notes or "")
        event.add("status", "CONFIRMED" if cours.statut == "valide" else "TENTATIVE")
        cal.add_component(event)

    return cal.to_ical()
```

#### 🎯 Critères d'acceptation

- `GET /tutorat/calendrier/<token>.ics` retourne un fichier iCalendar valide (Content-Type: `text/calendar; charset=utf-8`)
- Le flux contient uniquement les cours de l'utilisateur propriétaire du token (enseignant : ses cours enseignés ; élève : ses cours suivis ; parent : cours de ses enfants)
- Les événements respectent RFC 5545 : `DTSTART`, `DTEND`, `UID`, `SUMMARY`, `LOCATION`, `STATUS`
- Les cours `valide` ont `STATUS:CONFIRMED`, les cours en attente ont `STATUS:TENTATIVE`
- Un token invalide retourne HTTP 404 (pas 403 — ne pas révéler l'existence de tokens)
- Le dashboard affiche des boutons « Ajouter à Google Calendar », « Ajouter à Outlook », « Ajouter à Apple Calendar »
- `date_dernier_acces` est mis à jour à chaque requête sur le flux .ics

#### 🏗 Architecture

- **`tutoring/calendar.py`** : fonction `generer_flux_ics(user, cours_queryset)` — retourne `bytes` du fichier .ics
- **Vue** : `calendrier_ics_view(request, token)` — pas de `@login_required` (les clients CalDAV n'envoient pas de cookies de session)
- **URL** : `/tutorat/calendrier/<str:token>.ics` — format slug-safe via `secrets.token_urlsafe(48)`
- **Token** : généré automatiquement au premier accès via le dashboard (bouton « Générer mon lien calendrier »)
- **Régénération** : bouton « Réinitialiser mon lien » → supprime l'ancien token et en crée un nouveau (invalide les anciens abonnements)
- **Package** : `icalendar` ajouté à `requirements.txt`
- **Boutons d'ajout** :
  - Google : `https://calendar.google.com/calendar/r?cid=webcal://{host}/tutorat/calendrier/{token}.ics`
  - Outlook : `https://outlook.live.com/calendar/0/addfromweb?url=webcal://{host}/tutorat/calendrier/{token}.ics`
  - Apple : lien `webcal://` direct

#### 🧪 Tests (3 tests) — `tutoring/tests/test_calendar.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_flux_ics_format_valide_rfc5545` | `CalendrierToken` + 2 `CoursParticulier` (1 validé, 1 en attente) | `assertIn(b"BEGIN:VCALENDAR", response.content)` ; `assertIn(b"BEGIN:VEVENT", response.content)` ; `assertEqual(response["Content-Type"], "text/calendar; charset=utf-8")` ; contient 2 `VEVENT` ; le validé a `STATUS:CONFIRMED`, l'autre `STATUS:TENTATIVE` |
| 2 | `test_token_invalide_retourne_404` | Aucun `CalendrierToken` | `client.get("/tutorat/calendrier/token_inexistant.ics")` → `assertEqual(response.status_code, 404)` |
| 3 | `test_flux_filtre_par_utilisateur` | 2 enseignants, chacun avec 1 cours | Le flux de l'enseignant A contient uniquement son cours — `assertEqual(response.content.count(b"BEGIN:VEVENT"), 1)` |

#### 🔒 Sécurité

- **Token opaque** : `secrets.token_urlsafe(48)` = 48 bytes d'entropie → 64 caractères base64url — brute-force impraticable
- **Pas de `@login_required`** : la vue calendrier utilise uniquement le token comme authentification — les clients CalDAV (Google, Outlook, Apple) ne supportent pas les cookies
- **Token ≠ session** : le token ne donne accès qu'au flux .ics — pas de session Django, pas d'accès aux autres endpoints
- **Régénération** : l'utilisateur peut réinitialiser son token à tout moment — invalide les anciens abonnements
- **404 vs 403** : un token invalide retourne 404 (pas 403) pour ne pas révéler l'existence de l'endpoint avec ce token
- **Rate limit** : rate limit par IP sur l'endpoint .ics — 60 req/heure (protège contre le scraping de tokens)

#### ⚡ Performance

- **QuerySet optimisé** : `select_related("enseignant", "eleve")` sur le queryset passé à `generer_flux_ics()` — 1 requête SQL max
- **Pas de cache** : le flux doit refléter l'état en temps réel des réservations — pas de cache HTTP ni cache Django
- **`date_dernier_acces` update** : `CalendrierToken.objects.filter(pk=token.pk).update(date_dernier_acces=now)` — pas de `save()` pour éviter un SELECT + UPDATE

#### ✅ Definition of Done

- [ ] `CalendrierToken` modèle créé
- [ ] `tutoring/calendar.py` génère du .ics valide RFC 5545
- [ ] Vue `/tutorat/calendrier/<token>.ics` fonctionnelle sans auth
- [ ] Token invalide → 404
- [ ] Boutons « Ajouter à Google/Outlook/Apple » dans le dashboard
- [ ] `icalendar` ajouté à `requirements.txt`
- [ ] 3 tests passent
- [ ] `CODEBASE_REFERENCE.md` mis à jour (sections 1, 2, 3, 5)

---

### Étape 9.4 — Facture SAP

**Objectif** : générer des factures PDF conformes aux exigences SAP (Services à la Personne), avec mentions obligatoires (numéro d'agrément, crédit d'impôt 50%, identification fiscale), et envoi automatique par email aux 3 parties (enseignant, élève, parent).

#### Modèle `Facture`

```python
# tutoring/models.py (ajout)

class Facture(models.Model):
    cours = models.OneToOneField(
        CoursParticulier,
        on_delete=models.CASCADE,
        related_name="facture",
    )
    paiement = models.OneToOneField(
        PaiementCours,
        on_delete=models.CASCADE,
        related_name="facture",
    )
    numero = models.CharField(max_length=20, unique=True, db_index=True)
    montant_ttc = models.DecimalField(max_digits=8, decimal_places=2)
    montant_credit_impot = models.DecimalField(max_digits=8, decimal_places=2)
    date_emission = models.DateTimeField(auto_now_add=True)
    pdf_genere = models.BooleanField(default=False)
    email_envoye = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.numero:
            self.numero = self._generer_numero()
        if not self.montant_credit_impot:
            self.montant_credit_impot = self.montant_ttc * Decimal("0.50")
        super().save(*args, **kwargs)

    @staticmethod
    def _generer_numero():
        """Génère un numéro de facture séquentiel : SAP-YYYYMM-XXXX."""
        from django.utils import timezone
        now = timezone.now()
        prefix = f"SAP-{now.strftime('%Y%m')}"
        dernier = (
            Facture.objects.filter(numero__startswith=prefix)
            .order_by("-numero")
            .values_list("numero", flat=True)
            .first()
        )
        if dernier:
            seq = int(dernier.split("-")[-1]) + 1
        else:
            seq = 1
        return f"{prefix}-{seq:04d}"

    def __str__(self):
        return f"Facture {self.numero}"
```

#### Génération PDF — `tutoring/facturation.py`

```python
# tutoring/facturation.py
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings


def generer_facture_pdf(facture):
    """Génère le PDF de facture SAP avec mentions obligatoires."""
    html_string = render_to_string("tutoring/facture_pdf.html", {
        "facture": facture,
        "cours": facture.cours,
        "paiement": facture.paiement,
        "enseignant": facture.cours.enseignant,
        "eleve": facture.cours.eleve,
        "parent": facture.cours.parent,
        "numero_agrement": settings.SAP_NUMERO_AGREMENT,
        "identification_fiscale": settings.SAP_IDENTIFICATION_FISCALE,
        "raison_sociale": settings.SAP_RAISON_SOCIALE,
        "adresse": settings.SAP_ADRESSE,
    })
    return HTML(string=html_string).write_pdf()


def envoyer_facture_email(facture, pdf_bytes):
    """Envoie la facture PDF par email aux 3 parties."""
    from django.core.mail import EmailMessage

    destinataires = [
        facture.cours.enseignant.email,
        facture.cours.eleve.email,
    ]
    if facture.cours.parent:
        destinataires.append(facture.cours.parent.email)

    email = EmailMessage(
        subject=f"Facture {facture.numero} — Cours particulier ScienceLycée",
        body=(
            f"Bonjour,\n\n"
            f"Veuillez trouver ci-joint la facture {facture.numero} "
            f"pour le cours du {facture.cours.date_debut.strftime('%d/%m/%Y à %H:%M')}.\n\n"
            f"Montant TTC : {facture.montant_ttc} €\n"
            f"Crédit d'impôt (50%) : {facture.montant_credit_impot} €\n\n"
            f"Cordialement,\nScienceLycée"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=destinataires,
    )
    email.attach(
        f"facture_{facture.numero}.pdf",
        pdf_bytes,
        "application/pdf",
    )
    email.send()
```

#### Template PDF — `templates/tutoring/facture_pdf.html`

Mentions SAP obligatoires à inclure :
- Raison sociale et adresse du prestataire
- Numéro d'agrément SAP délivré par la DIRECCTE/DREETS
- Identification fiscale (SIRET, numéro TVA intracommunautaire)
- Identité du bénéficiaire (élève et/ou parent)
- Nature de la prestation : « Cours particulier à domicile — soutien scolaire »
- Date et durée de la prestation
- Montant TTC
- Mention du crédit d'impôt : « Ouvre droit à un crédit d'impôt de 50% au titre de l'article 199 sexdecies du CGI »
- Numéro de facture séquentiel

#### 🎯 Critères d'acceptation

- Quand un `PaiementCours` passe à `statut='capture'`, une `Facture` est créée automatiquement
- Le numéro de facture suit le format `SAP-YYYYMM-XXXX` (séquentiel par mois)
- Le PDF contient toutes les mentions SAP obligatoires (agrément, crédit d'impôt, identification fiscale)
- Le crédit d'impôt est calculé à 50% du montant TTC
- L'email est envoyé aux 3 parties (enseignant, élève, parent si lié) avec le PDF en pièce jointe
- `Facture.pdf_genere` est `True` après génération réussie
- `Facture.email_envoye` est `True` après envoi réussi
- Le numéro de facture est unique en DB

#### 🏗 Architecture

- **`tutoring/facturation.py`** : `generer_facture_pdf(facture)` + `envoyer_facture_email(facture, pdf_bytes)` — fonctions pures, testables unitairement
- **Template** : `templates/tutoring/facture_pdf.html` — même approche que `lecon_pdf.html` (WeasyPrint)
- **Celery task** (recommandé) : la génération PDF + envoi email doit être asynchrone pour ne pas bloquer la requête HTTP de validation du cours
  ```python
  # tutoring/tasks.py
  from celery import shared_task

  @shared_task
  def generer_et_envoyer_facture(facture_id):
      facture = Facture.objects.select_related(
          "cours__enseignant", "cours__eleve", "cours__parent", "paiement"
      ).get(pk=facture_id)
      pdf_bytes = generer_facture_pdf(facture)
      facture.pdf_genere = True
      facture.save(update_fields=["pdf_genere"])
      envoyer_facture_email(facture, pdf_bytes)
      facture.email_envoye = True
      facture.save(update_fields=["email_envoye"])
  ```
- **Settings SAP** : `SAP_NUMERO_AGREMENT`, `SAP_IDENTIFICATION_FISCALE`, `SAP_RAISON_SOCIALE`, `SAP_ADRESSE` dans `.env` et `config/settings/base.py`
- **Fallback synchrone** : si Celery n'est pas configuré, la génération est synchrone dans la vue (acceptable pour le MVP, à migrer en phase ultérieure)

#### 🧪 Tests (4 tests) — `tutoring/tests/test_facturation.py`

| # | Nom du test | Fixture | Assertion clé |
|---|-------------|---------|---------------|
| 1 | `test_generer_facture_pdf_mock_weasyprint` | `Facture` complète, `@patch("tutoring.facturation.HTML")` | Mock `HTML().write_pdf()` retourne `b"%PDF-1.4..."` ; `assertTrue(facture.pdf_genere)` |
| 2 | `test_numero_facture_sequentiel` | 3 `Facture` créées dans le même mois | `assertEqual(f1.numero, "SAP-202603-0001")` ; `assertEqual(f2.numero, "SAP-202603-0002")` ; `assertEqual(f3.numero, "SAP-202603-0003")` |
| 3 | `test_envoi_email_3_destinataires` | `Facture` avec parent lié, `@patch("tutoring.facturation.EmailMessage")` | `assertEqual(len(mock_email.call_args[1]["to"]), 3)` ; l'attachement contient le PDF |
| 4 | `test_envoi_email_2_destinataires_sans_parent` | `Facture` sans parent, `@patch("tutoring.facturation.EmailMessage")` | `assertEqual(len(mock_email.call_args[1]["to"]), 2)` |

#### 🔒 Sécurité

- **Secrets SAP** : `SAP_NUMERO_AGREMENT`, `SAP_IDENTIFICATION_FISCALE` dans les variables d'environnement — données sensibles (identification légale du prestataire)
- **PDF non public** : les factures PDF ne sont pas servies via une URL publique — elles sont uniquement envoyées par email et accessibles via le dashboard (authentifié + ownership check)
- **Injection HTML** : le template `facture_pdf.html` utilise `{{ variable|escape }}` par défaut Django — pas de `|safe` sur les données utilisateur
- **Email spoofing** : `DEFAULT_FROM_EMAIL` configuré avec un domaine vérifié (SPF/DKIM via Brevo)
- **Rate limit** : pas de vue publique pour télécharger les factures — uniquement via email ou dashboard authentifié

#### ⚡ Performance

- **Celery async** : la génération PDF (WeasyPrint ~2-5s) + envoi email ne bloque pas la requête HTTP
- **`select_related` sur le task** : `Facture.objects.select_related("cours__enseignant", "cours__eleve", "cours__parent", "paiement")` — 1 requête SQL
- **Pas de N+1 sur le listing** : la vue dashboard factures utilise `select_related` sur le queryset

#### ✅ Definition of Done

- [ ] Modèle `Facture` créé avec numéro séquentiel `SAP-YYYYMM-XXXX`
- [ ] `tutoring/facturation.py` génère un PDF avec toutes les mentions SAP
- [ ] Template `facture_pdf.html` avec mentions légales complètes
- [ ] Email envoyé aux 3 parties (ou 2 sans parent) avec PDF joint
- [ ] Celery task pour génération async (ou fallback synchrone MVP)
- [ ] 4 tests passent (mock WeasyPrint + mock EmailMessage)
- [ ] Variables SAP documentées dans `.env.example`
- [ ] `CODEBASE_REFERENCE.md` mis à jour (sections 1, 2, 3, 5, 6)

---

### Résumé Phase 9

| Étape | Artefacts principaux | Tests | Dépendances externes |
|-------|---------------------|-------|---------------------|
| 9.1 — CoursParticulier | `tutoring/models.py`, `views.py`, `urls.py`, `admin.py` | 5 | Aucune |
| 9.2 — Stripe Pre-auth | `tutoring/services.py`, webhook, `PaiementCours` | 4 | `stripe` (PyPI) |
| 9.3 — Calendrier .ics | `tutoring/calendar.py`, `CalendrierToken` | 3 | `icalendar` (PyPI) |
| 9.4 — Facture SAP | `tutoring/facturation.py`, `Facture`, Celery task | 4 | `weasyprint` (déjà installé), `celery` (PyPI) |
| **Total** | | **16** | |

### Variables d'environnement à ajouter (Phase 9)

| Variable | Étape | Description |
|----------|-------|-------------|
| `STRIPE_SECRET_KEY` | 9.2 | Clé secrète Stripe (sk_live_... ou sk_test_...) |
| `STRIPE_PUBLISHABLE_KEY` | 9.2 | Clé publique Stripe (pk_live_... ou pk_test_...) |
| `STRIPE_WEBHOOK_SECRET` | 9.2 | Secret de signature webhook (whsec_...) |
| `SAP_NUMERO_AGREMENT` | 9.4 | Numéro d'agrément SAP délivré par la DREETS |
| `SAP_IDENTIFICATION_FISCALE` | 9.4 | SIRET + numéro TVA intracommunautaire |
| `SAP_RAISON_SOCIALE` | 9.4 | Nom légal de l'entreprise |
| `SAP_ADRESSE` | 9.4 | Adresse complète du siège social |
| `CELERY_BROKER_URL` | 9.4 | URL du broker Celery (Redis recommandé) |

### Packages Python à ajouter

| Package | Version | Étape |
|---------|---------|-------|
| `stripe` | ≥ 7.0 | 9.2 |
| `icalendar` | ≥ 5.0 | 9.3 |
| `celery[redis]` | ≥ 5.3 | 9.4 |

### Ordre d'exécution recommandé

```
1. Implementer      → Créer app tutoring/ + modèle CoursParticulier (9.1)
2. Migration Writer → Migration pour CoursParticulier
3. Implementer      → Vues de demande, validation, annulation (9.1)
4. Test Writer      → 5 tests CoursParticulier
5. Implementer      → PaiementCours + services.py Stripe (9.2)
6. Migration Writer → Migration pour PaiementCours
7. Implementer      → Webhook Stripe + intégration dans les vues (9.2)
8. Test Writer      → 4 tests Stripe
9. Implementer      → CalendrierToken + calendar.py (9.3)
10. Migration Writer → Migration pour CalendrierToken
11. Implementer      → Vue .ics + boutons dashboard (9.3)
12. Test Writer      → 3 tests calendrier
13. Implementer      → Facture + facturation.py + Celery task (9.4)
14. Migration Writer → Migration pour Facture
15. Implementer      → Template facture_pdf.html + envoi email (9.4)
16. Test Writer      → 4 tests facturation
17. Implementer      → Mise à jour CODEBASE_REFERENCE.md
```

---

## Ordre d'implémentation recommandé

| Sprint | Phase | Livrable | Tests attendus | Agent(s) |
|--------|-------|----------|----------------|----------|
| 1 | Phase 1 | Modèles + migration | ~12 tests | Implementer + Migration Writer |
| 2 | Phase 2 | Inscription multi-rôles | ~18 tests | Implementer + Test Writer |
| 3 | Phase 3 | Validation liaisons + notifications | ~20 tests | Implementer + Test Writer |
| 4 | Phase 4 | Dashboards + fiche élève | ~26 tests | Implementer + Test Writer |
| 5 | Phase 5 | Messagerie | ~16 tests | Implementer + Test Writer |
| 6 | Phase 6 | Panel admin étendu | ~16 tests | Implementer + Test Writer |
| 7 | Phase 7 | Seed data + preview enseignant | ~14 tests | Implementer + Test Writer |
| 8 | Phase 8 | Migration + déploiement | ~6 tests | Migration Writer + Heroku Deploy |
| 9 | Phase 9 | Réservation, Calendrier, Facturation | ~16 tests | Implementer + Test Writer |
| | | **TOTAL** | **~144 tests** | |

---

## Budget tests par phase

| Phase | Tests min | Domaine principal |
|-------|-----------|-------------------|
| Phase 1 | ~12 | Modèles (création, contraintes, propriétés, enums) |
| Phase 2 | ~18 | Vues (inscription, choix rôle, code enseignant/élève) |
| Phase 3 | ~20 | Vues + helpers (validation liens, notifications, IDOR) |
| Phase 4 | ~26 | Vues + intégration (dashboards, fiche élève, filtres, accès) |
| Phase 5 | ~16 | Vues + intégration (envoi, réception, threads, permissions) |
| Phase 6 | ~16 | Vues + helpers (panel admin, statistiques, gestion) |
| Phase 7 | ~14 | Helpers + intégration (seed data, preview enseignant) |
| Phase 8 | ~6 | Intégration (migration, health check, smoke tests) |
| Phase 9 | ~16 | Modèles + vues (réservation, calendrier, facturation) |
| **TOTAL** | **~144** | |

---

## Checklist qualité par sprint

### Code

- [ ] Docstring 1 ligne sur chaque nouvelle vue et modèle
- [ ] Pas de requête N+1 (`assertNumQueries` ou django-debug-toolbar)
- [ ] Pas de logique dupliquée (helpers extraits)
- [ ] Imports groupés (stdlib / Django / local)
- [ ] Max 200 lignes par vue (sinon extraire helpers)
- [ ] `CODEBASE_REFERENCE.md` mis à jour

### Tests

- [ ] 0 failure, 0 error (`pytest --tb=short`)
- [ ] Ratio ≥ 3 tests par vue (anonyme→redirect, interdit→403, autorisé→200)
- [ ] Tests IDOR pour chaque vue accédant aux données d'un autre utilisateur
- [ ] `client.force_login()` partout (django-axes)
- [ ] Nommage : `test_{action}_{scenario}_{resultat_attendu}`

### Sécurité

- [ ] Aucune vue sans vérification de rôle
- [ ] Aucun `|safe` sur données utilisateur
- [ ] Rate limiting sur endpoints sensibles
- [ ] Messages d'erreur génériques (pas d'info leak)
- [ ] `strip_tags()` sur tout input utilisateur stocké
- [ ] OWASP A01 (Broken Access Control) vérifié

### Performance

- [ ] Budget SQL respecté (liste≤5, détail≤8, dashboard≤12)
- [ ] Pagination sur toutes les listes (25/page, 50 msg/page)
- [ ] `select_related`/`prefetch_related` sur FK/M2M accédés
- [ ] Cache pour compteurs fréquents (notifications, messages non lus)
- [ ] `bulk_create()`/`bulk_update()` dans les seeds et migrations

---

## Fichiers impactés (résumé)

| Fichier | Nature du changement |
|---------|---------------------|
| `users/models.py` | +4 modèles, +1 champ, +2 propriétés, +2 enums |
| `users/forms.py` | +3 formulaires d'inscription |
| `users/views.py` | +20 vues (inscription, validation, dashboards, admin, preview) |
| `users/urls.py` | +20 routes |
| `users/admin.py` | +5 modèles enregistrés |
| `users/helpers.py` | Nouveau : peut_voir_eleve(), contacts_autorises(), valider_lien() |
| `users/tests.py` | +130 tests |
| `users/context_processors.py` | Extension : compteurs notifications + messages |
| `tutoring/` | Nouvelle app : models, views, services, calendar, facturation, urls, admin |
| `courses/management/commands/seed_roles_test.py` | Nouveau : seed enseignants/élèves/parents |
| `templates/base.html` | Sidebar conditionnelle, cloche notifications, preview enseignant |
| `templates/registration/` | +4 templates |
| `templates/dashboard/` | +5 templates |
| `templates/users/` | +4 templates |
| `templates/messaging/` | +5 templates |
| `templates/tutoring/` | +4 templates |
| `config/settings/base.py` | INSTALLED_APPS += tutoring |
