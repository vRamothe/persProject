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

### Convention de tests

- **`client.force_login(user)`** systématiquement (django-axes)
- **Fixtures par rôle** : `eleve`, `admin_user`, `enseignant`, `parent_user` réutilisables
- **Ratio minimum** : chaque vue doit avoir au moins 3 tests (accès anonyme → redirect, accès rôle interdit → 403, accès rôle autorisé → 200)
- **Fichiers** : `users/tests.py` pour les vues users, `courses/tests/test_courses.py` pour le reste
- **Pattern HTMX** : les tests de vues HTMX vérifient le fragment HTML retourné, pas un redirect

### Convention de sécurité

- **OWASP Top 10** vérifié à chaque phase
- **Broken Access Control** (#1) : chaque vue vérifie le rôle ET le lien validé
- **Injection** (#3) : pas de `|safe` sur des données utilisateur, `escape()` systématique
- **IDOR** : tout accès à une ressource par ID doit vérifier que l'utilisateur a le droit
- **Enumeration** : messages d'erreur génériques pour les codes invalides
- **CSRF** : toutes les actions POST via formulaire ou HTMX (déjà couvert par Django + meta CSRF)
- **Rate limiting** : sur tout endpoint de création (inscription, liaison, message)

### Convention de performance

- **Requêtes N+1** : utiliser `select_related()` et `prefetch_related()` pour les FK/M2M
- **Pagination** : toute liste > 20 éléments doit être paginée (25 par page)
- **Cache** : les compteurs de notifications non lues doivent être cached (invalidation à la création)
- **Indexes** : ajouter `db_index=True` sur les champs utilisés dans les filtres fréquents
- **Bulk operations** : `bulk_create()` pour les seeds, pas de boucle `save()` unitaire

---

## Phase 1 — Modèles de données

### Étape 1.1 — Étendre les choix de rôles

**Fichier** : `users/models.py`

Modifier `RoleChoices` :
```python
class RoleChoices(models.TextChoices):
    ADMIN = "admin", "Administrateur"
    ELEVE = "eleve", "Élève"
    ENSEIGNANT = "enseignant", "Enseignant"
    PARENT = "parent", "Parent"
```

Ajouter des propriétés au modèle `CustomUser` :
```python
@property
def is_enseignant(self):
    return self.role == RoleChoices.ENSEIGNANT

@property
def is_parent(self):
    return self.role == RoleChoices.PARENT
```

### Étape 1.2 — Code identifiant unique

**Fichier** : `users/models.py`

Ajouter un champ `code_identifiant` sur `CustomUser` :
- Type : `CharField(max_length=8, unique=True, editable=False, db_index=True)`
- Généré automatiquement à la création via **`secrets.token_hex()`** (pas `random`)
- Format : `{préfixe_rôle}-{4 caractères alphanumériques aléatoires}`
- Préfixes : `ELV` (élève), `ENS` (enseignant), `PAR` (parent), `ADM` (admin)
- Affiché dans le profil de chaque utilisateur pour le partager

Ajouter une méthode `_generer_code_identifiant()` dans le `save()` override ou dans le manager.

### Étape 1.3 — Modèles de liaison

**Fichier** : `users/models.py`

```python
class StatutLienChoices(models.TextChoices):
    EN_ATTENTE = "en_attente", "En attente de validation"
    VALIDE = "valide", "Validé"
    REFUSE = "refuse", "Refusé"

class LienEnseignantEleve(models.Model):
    enseignant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="eleves_lies")
    eleve = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="enseignants_lies")
    statut = models.CharField(max_length=20, choices=StatutLienChoices.choices, default=StatutLienChoices.EN_ATTENTE, db_index=True)
    demande_par = models.CharField(max_length=20)  # "eleve" ou "enseignant" — qui a initié
    cree_le = models.DateTimeField(auto_now_add=True)
    valide_le = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ["enseignant", "eleve"]

class LienParentEleve(models.Model):
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="enfants_lies")
    eleve = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="parents_lies")
    statut = models.CharField(max_length=20, choices=StatutLienChoices.choices, default=StatutLienChoices.EN_ATTENTE, db_index=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    valide_le = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ["parent", "eleve"]
```

### Étape 1.4 — Modèle de notification interne

**Fichier** : `users/models.py`

```python
class TypeNotificationChoices(models.TextChoices):
    DEMANDE_LIAISON = "demande_liaison", "Demande de liaison"
    LIAISON_VALIDEE = "liaison_validee", "Liaison validée"
    LIAISON_REFUSEE = "liaison_refusee", "Liaison refusée"
    MESSAGE = "message", "Nouveau message"

class Notification(models.Model):
    destinataire = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notifications")
    type = models.CharField(max_length=30, choices=TypeNotificationChoices.choices)
    titre = models.CharField(max_length=200)
    contenu = models.TextField(blank=True)
    lue = models.BooleanField(default=False, db_index=True)
    lien = models.CharField(max_length=255, blank=True)  # URL relative vers l'action
    cree_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-cree_le"]
        indexes = [
            models.Index(fields=["destinataire", "lue", "-cree_le"]),
        ]
```

### Étape 1.5 — Modèle de messagerie

**Fichier** : `users/models.py` (ou nouveau fichier `messaging/models.py`)

```python
class Conversation(models.Model):
    participants = models.ManyToManyField(CustomUser, related_name="conversations")
    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour_le = models.DateTimeField(auto_now=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    auteur = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="messages_envoyes")
    contenu = models.TextField(max_length=2000)
    lu = models.BooleanField(default=False)
    envoye_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["envoye_le"]
        indexes = [
            models.Index(fields=["conversation", "envoye_le"]),
        ]
```

### Étape 1.6 — Migration

Générer et appliquer les migrations pour tous les nouveaux modèles et champs.

### 🧪 Tests Phase 1

**9 tests attendus** :
- Création d'un utilisateur par rôle (élève, enseignant, parent, admin)
- `code_identifiant` auto-généré au `save()`
- `code_identifiant` préfixé correctement selon le rôle
- `code_identifiant` unique (pas de collision)
- Collision de code gérée (retry avec nouveau code)
- `unique_together` sur `LienEnseignantEleve` et `LienParentEleve`
- Max 2 parents validés par élève
- `Notification` ordering par `-cree_le`
- `Message.contenu` max length respecté

### 🔒 Sécurité Phase 1

- Code identifiant généré avec `secrets.token_hex()` (pas `random`)
- Pas d'information sensible exposée dans le `code_identifiant`
- Contenu des messages nettoyé (pas de HTML/script stocké brut)

### ⚡ Performance Phase 1

- `db_index=True` sur `code_identifiant`, `statut` (LienEnseignantEleve, LienParentEleve), `lue` (Notification)
- Index composite `models.Index(fields=["destinataire", "lue", "-cree_le"])` sur Notification
- Index `models.Index(fields=["conversation", "envoye_le"])` sur Message

---

## Phase 2 — Inscription et validation

### Étape 2.1 — Refonte du formulaire d'inscription

**Fichier** : `users/forms.py`

Remplacer `InscriptionForm` par un système en 2 étapes :

**Étape A** — Choix du rôle (nouvelle page ou section) :
- 3 cartes cliquables : "Je suis élève", "Je suis enseignant", "Je suis parent"
- Redirige vers le formulaire adapté

**Étape B** — Formulaires spécialisés :

1. **InscriptionEleveForm** :
   - Champs : prenom, nom, email, niveau (obligatoire), password1, password2
   - Champ optionnel : `code_enseignant` (CharField, non obligatoire)
   - Validation : si `code_enseignant` fourni → vérifier qu'il correspond à un enseignant existant et actif

2. **InscriptionEnseignantForm** :
   - Champs : prenom, nom, email, password1, password2
   - Pas de champ `niveau` (nullable pour les non-élèves)
   - Pas de code requis

3. **InscriptionParentForm** :
   - Champs : prenom, nom, email, password1, password2
   - Champ obligatoire : `code_eleve` (CharField)
   - Validation : `code_eleve` doit correspondre à un élève existant et actif
   - Pas de champ `niveau`

### Étape 2.2 — Vues d'inscription multi-rôles

**Fichier** : `users/views.py`

```
GET  /inscription/               → page de choix du rôle
GET  /inscription/eleve/         → formulaire élève
POST /inscription/eleve/         → création compte élève
GET  /inscription/enseignant/    → formulaire enseignant
POST /inscription/enseignant/    → création compte enseignant
GET  /inscription/parent/        → formulaire parent
POST /inscription/parent/        → création compte parent
```

**Logique POST élève** :
1. Créer le compte (`is_active=False`, `role="eleve"`)
2. Débloquer les premiers chapitres
3. Envoyer l'email de vérification
4. Si `code_enseignant` fourni :
   - Trouver l'enseignant par son `code_identifiant`
   - Créer `LienEnseignantEleve(statut="en_attente", demande_par="eleve")`
   - Créer une `Notification` pour l'enseignant
5. Rediriger vers confirmation

**Logique POST enseignant** :
1. Créer le compte (`is_active=False`, `role="enseignant"`)
2. Envoyer l'email de vérification
3. Rediriger vers confirmation

**Logique POST parent** :
1. Valider que `code_eleve` correspond à un élève actif
2. Créer le compte (`is_active=False`, `role="parent"`)
3. Envoyer l'email de vérification
4. Créer `LienParentEleve(statut="en_attente")`
5. Créer une `Notification` pour l'élève
6. Rediriger vers confirmation

### Étape 2.3 — Templates d'inscription

**Fichiers** :
- `templates/registration/register_choix_role.html` — 3 cartes de choix
- `templates/registration/register_eleve.html` — formulaire élève (basé sur l'actuel `register.html`)
- `templates/registration/register_enseignant.html` — formulaire enseignant
- `templates/registration/register_parent.html` — formulaire parent

### Étape 2.4 — URLs d'inscription

**Fichier** : `users/urls.py`

```python
path("inscription/", views.choix_role_view, name="inscription"),
path("inscription/eleve/", views.InscriptionEleveView.as_view(), name="inscription_eleve"),
path("inscription/enseignant/", views.InscriptionEnseignantView.as_view(), name="inscription_enseignant"),
path("inscription/parent/", views.InscriptionParentView.as_view(), name="inscription_parent"),
```

### 🧪 Tests Phase 2

**13 tests attendus** :
- GET page choix de rôle → 200
- GET formulaire élève → 200
- POST inscription élève sans code enseignant → compte créé, pas de lien
- POST inscription élève avec code enseignant valide → lien en attente créé
- POST inscription élève avec code invalide → erreur formulaire
- POST inscription élève avec mauvais préfixe (code parent) → erreur formulaire
- GET formulaire enseignant → 200
- POST inscription enseignant → compte créé sans lien
- GET formulaire parent → 200
- POST inscription parent sans code élève → erreur formulaire
- POST inscription parent avec code élève valide → lien en attente créé
- POST inscription parent avec code élève inactif → erreur formulaire
- Email dupliqué → erreur formulaire
- Vérification email → activation du compte
- Backward compat : `/inscription/` redirige vers choix de rôle

### 🔒 Sécurité Phase 2

- **Enumeration** : message d'erreur générique pour code invalide (ne pas révéler si le code existe)
- **Brute force codes** : rate limit 5 tentatives/h/IP sur les endpoints d'inscription avec code
- **Password validation** : conservée (Django validators existants)
- **CSRF** : protégé par défaut (Django middleware + meta CSRF)
- **Token email** : signé avec `signing.dumps()`, expire après 24h
- **Input sanitization** : `strip()`, `lower()` sur email, `upper()` sur codes

### ⚡ Performance Phase 2

- Lookup `code_identifiant` en O(1) grâce à l'index unique
- `transaction.atomic()` pour les opérations groupées (création compte + lien + notification)

---

## Phase 3 — Système de validation des liaisons

### Étape 3.1 — Vue de gestion des liaisons (enseignant)

**Fichier** : `users/views.py`

```
GET  /panel-enseignant/liaisons/           → liste des demandes en attente + liaisons actives
POST /panel-enseignant/liaisons/<id>/valider/  → approuver un lien
POST /panel-enseignant/liaisons/<id>/refuser/  → refuser un lien
```

Quand l'enseignant valide :
1. `LienEnseignantEleve.statut = "valide"`, `valide_le = now()`
2. Créer `Notification` pour l'élève : "Votre enseignant X a validé votre demande"

Quand l'enseignant refuse :
1. `LienEnseignantEleve.statut = "refuse"`
2. Créer `Notification` pour l'élève : "Votre enseignant X a refusé votre demande"

### Étape 3.2 — Vue de gestion des liaisons (élève)

**Fichier** : `users/views.py`

```
GET  /panel-eleve/liaisons/              → liste des demandes parent en attente
POST /panel-eleve/liaisons/<id>/valider/ → approuver un parent
POST /panel-eleve/liaisons/<id>/refuser/ → refuser un parent
```

Même logique : valider ou refuser le `LienParentEleve`, notifier le parent.

### Étape 3.3 — Liaison initiée par l'enseignant (ajout d'élève)

L'enseignant doit aussi pouvoir ajouter un élève via son `code_identifiant` :

```
GET  /panel-enseignant/ajouter-eleve/       → formulaire avec champ code_eleve
POST /panel-enseignant/ajouter-eleve/       → créer lien en attente
```

1. Trouver l'élève par `code_identifiant`
2. Créer `LienEnseignantEleve(statut="en_attente", demande_par="enseignant")`
3. Créer `Notification` pour l'élève : "L'enseignant X souhaite vous suivre"
4. L'élève doit alors valider depuis son interface

### Étape 3.4 — Contrainte : un seul enseignant par élève

**Fichier** : `users/views.py`

Lors de la validation d'un `LienEnseignantEleve` :
- Vérifier que l'élève n'a pas déjà un lien enseignant avec `statut="valide"`
- Si oui → refuser automatiquement avec message "Cet élève a déjà un enseignant lié"
- Appliquer aussi dans l'inscription élève avec code : si l'élève a déjà un enseignant validé, le nouveau lien est refusé

### Étape 3.5 — Contrainte : max 2 parents par élève

**Fichier** : `users/views.py`

Lors de la validation d'un `LienParentEleve` :
- Compter les liens parent validés de l'élève
- Si déjà 2 → refuser automatiquement avec message "Cet élève a déjà 2 parents liés"
- Appliquer aussi dans l'inscription parent : si l'élève a déjà 2 parents validés, le lien est créé en attente mais ne pourra pas être validé

### Étape 3.6 — Centre de notifications

**Fichier** : `users/views.py`

```
GET  /notifications/                → liste des notifications (paginée, 25 par page)
POST /notifications/<id>/lue/       → marquer comme lue
POST /notifications/tout-lire/      → marquer toutes les notifications comme lues
```

**Fichier** : `templates/base.html`

Ajouter dans le header : une cloche avec badge (nombre de notifications non lues). Visible pour tous les rôles authentifiés. Fragment HTMX qui se rafraîchit périodiquement ou au clic.

### Étape 3.7 — Templates de validation

**Fichiers** :
- `templates/users/liaisons_enseignant.html` — tableau des liaisons avec boutons Valider/Refuser
- `templates/users/liaisons_eleve.html` — tableau des demandes parent
- `templates/users/ajouter_eleve.html` — formulaire d'ajout par code
- `templates/users/notifications.html` — centre de notifications paginé

### 🧪 Tests Phase 3

**18 tests attendus** :
- Accès page liaisons enseignant (rôle autorisé → 200, rôle interdit → 403)
- Accès page liaisons élève (rôle autorisé → 200, rôle interdit → 403)
- Enseignant valide un lien → statut "valide" + notification créée
- Enseignant refuse un lien → statut "refuse" + notification créée
- Élève valide un parent → statut "valide" + notification créée
- IDOR protection : enseignant tente de valider un lien d'un autre enseignant → 403
- IDOR protection : élève tente de valider un lien d'un autre élève → 403
- Double validation → idempotent (pas d'erreur)
- Ajout d'élève par code (enseignant) → lien en attente créé
- Ajout d'élève avec code invalide → erreur
- Élève a déjà un enseignant validé → nouveau lien refusé
- 3ème parent tenté → validation bloquée
- Liste notifications paginée → 200
- Marquer notification comme lue → `lue=True`
- IDOR notification : marquer une notification d'un autre utilisateur → 403
- Tout marquer comme lu → toutes les notifications `lue=True`

### 🔒 Sécurité Phase 3

- **IDOR** : vérification que le lien à valider/refuser appartient bien au `request.user` (côté enseignant ET côté élève)
- **Race conditions** : `select_for_update()` sur les opérations de validation pour éviter les doubles validations concurrentes
- **Rate limiting** : max 10 demandes de liaison par heure par utilisateur
- **Enumeration** : message d'erreur générique pour code invalide lors de l'ajout par code

### ⚡ Performance Phase 3

- Cache du compteur de notifications non lues (invalidation à chaque création/marquage)
- `select_related("enseignant", "eleve")` sur les requêtes de liaisons
- Pagination des notifications (25 par page)

---

## Phase 4 — Dashboards par rôle

### Étape 4.1 — Router le tableau de bord par rôle

**Fichier** : `users/views.py`

Modifier `TableauDeBordView.get()` :
```python
if user.is_admin:
    return _dashboard_admin(request)
elif user.is_enseignant:
    return _dashboard_enseignant(request)
elif user.is_parent:
    return _dashboard_parent(request)
else:
    return _dashboard_eleve(request)
```

### Étape 4.2 — Dashboard enseignant

**Fichier** : `users/views.py` → `_dashboard_enseignant(request)`
**Template** : `templates/dashboard/enseignant.html`

**Contenu** :
- Nombre d'élèves liés (validés)
- Demandes de liaison en attente (avec lien vers gestion)
- Messages non lus
- Vue d'ensemble de la classe :
  - Progression moyenne
  - Score moyen aux quiz
  - Nombre de leçons terminées cette semaine
- Tableau synthétique des élèves :
  - Nom, niveau, progression %, score moyen, dernière connexion, streak
  - Lien vers le détail de chaque élève
- Graphique : activité de la classe sur 30 jours

### Étape 4.3 — Dashboard parent

**Fichier** : `users/views.py` → `_dashboard_parent(request)`
**Template** : `templates/dashboard/parent.html`

**Contenu** (pour chaque enfant lié et validé) :
- Carte par enfant avec :
  - Nom, niveau, progression globale
  - Dernière connexion (date + heure)
  - Streak actuel
  - Score moyen
- Section détaillée par enfant (expansible ou page dédiée) :
  - Historique des connexions (dates + durées si possible)
  - Notes par matière / chapitre
  - Points forts (chapitres > 80% de score)
  - Points faibles (chapitres < 60% de score)
  - Graphique de progression sur 30 jours
- Messages non lus des enseignants

### Étape 4.4 — Vue détaillée d'un élève (fiche complète)

**Fichier** : `users/views.py` → `fiche_eleve_view(request, eleve_id)`
**Template** : `templates/dashboard/fiche_eleve.html`
**Helper** : `users/helpers.py` → `peut_voir_eleve(user, eleve)` — retourne `True` si `user` est admin, enseignant lié validé, ou parent lié validé de `eleve`

**Accès** : `peut_voir_eleve(request.user, eleve)` doit retourner `True` (sinon 403)

**Données affichées** :

1. **En-tête — Identité**
   - Nom complet, niveau, code identifiant, date d'inscription
   - Statut du compte (actif/inactif)
   - Photo placeholder (initiales)

2. **Relations**
   - **Enseignant** : nom + email de l'enseignant lié (ou "Aucun — suivi par l'administrateur")
   - **Parents** : liste des parents liés (max 2), avec nom + email + date de liaison
   - Bouton admin : forcer/supprimer un lien

3. **Connexions**
   - Dernière connexion (date + heure)
   - Calendrier heatmap des 90 derniers jours (style GitHub contributions)
   - Fréquence moyenne (connexions/semaine)
   - Streak actuel + meilleur streak

4. **Notes et scores**
   - Score moyen global + par matière (gauge ou barre)
   - Tableau des résultats de quiz : chapitre, score, nb tentatives, date
   - Évolution du score sur 30 jours (graphique Chart.js)

5. **Points forts**
   - Top 5 chapitres par score moyen (>= 80%)
   - Badge vert par matière dominante

6. **Points faibles**
   - Bottom 5 chapitres par score moyen (<= 60%)
   - Badge rouge
   - Questions les plus échouées (box Leitner = 1, nb_total > 3)

7. **Progression**
   - Barre de progression globale + par matière
   - Chapitres débloqués vs total
   - Leçons terminées vs total

### Étape 4.5 — Adaptation du dashboard élève

**Fichier** : `templates/dashboard/eleve.html`

Ajouter :
- Section "Mes enseignants" : liste des enseignants liés (validés)
- Section "Mes parents" : liste des parents liés (validés)
- Code identifiant affiché (pour le partager à un parent)
- Badge de notifications en attente (liaisons parent à valider)

### Étape 4.6 — Adaptation de la sidebar

**Fichier** : `templates/base.html`

Adapter la navigation selon le rôle :

**Élève** (actuel + ajouts) :
- Tableau de bord
- Mes cours
- Révisions
- *(nouveau)* Mes liaisons
- *(nouveau)* Messages
- Profil

**Enseignant** :
- Tableau de bord
- Mes élèves
- Demandes en attente
- Messages
- Profil

**Parent** :
- Tableau de bord
- Mes enfants
- Messages
- Profil

**Admin** : inchangé

### 🧪 Tests Phase 4

**18 tests attendus** :
- Routage dashboard admin → template admin
- Routage dashboard enseignant → template enseignant
- Routage dashboard parent → template parent
- Routage dashboard élève → template élève
- Fiche élève : accès admin → 200
- Fiche élève : accès enseignant lié validé → 200
- Fiche élève : accès enseignant non lié → 403
- Fiche élève : accès parent lié validé → 200
- Fiche élève : accès parent en attente → 403
- Fiche élève : accès parent non lié → 403
- Fiche élève : accès élève (même si c'est lui) → 403
- Fiche élève : accès anonyme → redirect login
- Nombre d'élèves affiché correctement dans dashboard enseignant
- Enfants affichés correctement dans dashboard parent
- Sidebar enseignant affiche les bons liens
- Sidebar parent affiche les bons liens
- Sidebar élève affiche les bons liens
- Helper `peut_voir_eleve()` : retourne correctement True/False selon les cas

### 🔒 Sécurité Phase 4

- **IDOR fiche élève** : vérification via `peut_voir_eleve()` — pas d'accès par simple devinette d'ID
- **Pas d'emails parents visibles entre parents** : un parent ne voit que ses propres données, pas celles de l'autre parent
- **Preview mode** : les writes (progression, quiz) restent désactivés pendant la preview enseignant
- **Sidebar** : n'affiche que les liens autorisés pour le rôle courant

### ⚡ Performance Phase 4

- `prefetch_related("eleves_lies__eleve")` pour le dashboard enseignant (évite N+1 sur les élèves)
- `prefetch_related("enfants_lies__eleve")` pour le dashboard parent
- Fiche élève : max 3 requêtes pour les calculs lourds (progressions, quiz résultats, historique questions)
- `TruncDate` + `Avg` pour le graphique de score 30 jours (une seule requête agrégée)

---

## Phase 5 — Messagerie

### Étape 5.1 — Règles d'accès à la messagerie

| Expéditeur | Destinataire(s) autorisé(s) |
|------------|---------------------------|
| Enseignant | Ses élèves liés (validés) + leurs parents liés (validés) |
| Parent | Les enseignants liés à ses enfants (validés) |
| Élève | Ses enseignants liés (validés) |
| Admin | Tout le monde |

Un parent ne peut PAS écrire directement à un autre parent.
Un élève ne peut PAS écrire à un parent via la plateforme.

**Helper** : `users/helpers.py` → `contacts_autorises(user)` — retourne le queryset des utilisateurs avec lesquels `user` peut échanger des messages, selon les règles ci-dessus.

### Étape 5.2 — Vues de messagerie

**Fichier** : `users/views.py` (ou nouvelle app `messaging/views.py`)

```
GET  /messages/                       → liste des conversations
GET  /messages/<conversation_id>/     → détail d'une conversation
POST /messages/<conversation_id>/     → envoyer un message (HTMX)
GET  /messages/nouveau/               → formulaire nouvelle conversation
POST /messages/nouveau/               → créer conversation + premier message
```

### Étape 5.3 — Templates de messagerie

**Fichiers** :
- `templates/messaging/liste_conversations.html` — inbox
- `templates/messaging/conversation.html` — fil de messages (style chat)
- `templates/messaging/nouvelle_conversation.html` — choix du destinataire + message

### Étape 5.4 — Notifications de messages

Lors de l'envoi d'un message :
1. Créer une `Notification(type="message")` pour le destinataire
2. Optionnel : envoyer un email de notification (configurable par l'utilisateur)

### 🧪 Tests Phase 5

**14 tests attendus** :
- Enseignant envoie message à élève lié → OK
- Parent envoie message à enseignant de son enfant → OK
- Élève envoie message à son enseignant lié → OK
- Parent envoie message à un autre parent → 403
- Élève envoie message à un parent → 403
- Utilisateur non autorisé envoie message → 403
- Inbox trié par dernier message récent
- Accès à une conversation dont on n'est pas participant → 403
- Message > 2000 caractères → erreur formulaire
- `contacts_autorises()` enseignant → ses élèves + parents de ses élèves
- `contacts_autorises()` parent → enseignants de ses enfants
- `contacts_autorises()` élève → ses enseignants
- Compteur messages non lus correct
- Fragment HTMX conversation → retourne le bon HTML partiel

### 🔒 Sécurité Phase 5

- **Vérification destinataire** : `destinataire in contacts_autorises(request.user)` avant tout envoi
- **IDOR conversation** : vérifier que `request.user` est participant de la conversation
- **XSS contenu** : `strip_tags()` + `escape()` sur le contenu des messages
- **Rate limiting** : max 30 messages par heure par utilisateur
- **Pas de `|safe`** sur le contenu des messages dans les templates

### ⚡ Performance Phase 5

- `select_related("auteur")` + `prefetch_related("messages")` pour l'inbox
- Pagination : 50 messages par page dans une conversation
- Cache du compteur de messages non lus (invalidation à la réception)
- Email de notification envoyé uniquement si l'utilisateur est déconnecté depuis > 5 min

---

## Phase 6 — Panel admin étendu

### Étape 6.1 — Admin Django (modèles)

**Fichier** : `users/admin.py`

Enregistrer les nouveaux modèles :
- `LienEnseignantEleve` : filtres par statut, enseignant, élève
- `LienParentEleve` : filtres par statut, parent, élève
- `Notification` : filtres par type, lue/non lue
- `Conversation` et `Message` : lecture seule pour modération

### Étape 6.2 — Onglet "Enseignants" dans le panel admin

**Fichier** : `users/views.py` → `admin_enseignants_view(request)`
**Template** : `templates/dashboard/admin_enseignants.html`
**URL** : `/admin-panel/enseignants/`

**Vue liste** :
- Tableau de tous les enseignants inscrits :
  - Nom, email, date d'inscription, statut (actif/inactif)
  - Nombre d'élèves liés (validés)
  - Dernière connexion
- Filtres : recherche par nom/email, actif/inactif
- Lien cliquable sur chaque enseignant → détail

**Fichier** : `templates/base.html`

Ajouter dans la sidebar admin (entre "Élèves" et "Voir les cours") :
```
{% include "components/nav_item.html" with url="admin_enseignants" icon="teacher" label="Enseignants" %}
```

### Étape 6.3 — Détail d'un enseignant (ses élèves)

**Fichier** : `users/views.py` → `admin_enseignant_detail_view(request, enseignant_id)`
**Template** : `templates/dashboard/admin_enseignant_detail.html`
**URL** : `/admin-panel/enseignants/<int:enseignant_id>/`

**Contenu** :
- En-tête : nom, email, code identifiant, date inscription, dernière connexion
- Stats agrégées de ses élèves :
  - Progression moyenne de la classe
  - Score moyen de la classe
  - Nombre de leçons terminées cette semaine
- Tableau de ses élèves :
  - Nom, niveau, progression %, score moyen, dernière connexion, streak
  - Parents liés (noms)
  - Chaque ligne cliquable → fiche élève (étape 4.4)

### Étape 6.4 — Pool "Élèves sans enseignant" dans le dashboard admin

**Fichier** : `users/views.py` → Modifier `_dashboard_admin(request)`

Ajouter au dashboard admin existant :
- Section "Élèves sans enseignant" :
  - Compteur : nombre d'élèves actifs sans lien enseignant validé
  - Tableau compact : nom, niveau, dernière connexion
  - Bouton "Assigner à un enseignant" (select dropdown des enseignants actifs)
  - Chaque ligne cliquable → fiche élève

**Logique de requête** :
```python
# Élèves sans enseignant = élèves actifs n'ayant aucun LienEnseignantEleve avec statut="valide"
eleves_orphelins = CustomUser.objects.filter(
    role="eleve", is_active=True
).exclude(
    enseignants_lies__statut="valide"
)
```

### Étape 6.5 — Forcer/supprimer des liaisons depuis l'admin

**Fichier** : `users/views.py`

```
POST /admin-panel/eleves/<eleve_id>/assigner-enseignant/  → créer un lien "valide" directement
POST /admin-panel/liaisons/<lien_id>/supprimer/           → supprimer un lien
```

L'admin peut :
- Assigner un enseignant à un élève orphelin (crée un `LienEnseignantEleve` avec statut "valide" directement, sans validation)
- Supprimer un lien existant (l'élève retourne dans le pool admin)
- Forcer la validation d'un lien en attente

### Étape 6.6 — Dashboard admin : compteurs étendus

Modifier `_dashboard_admin(request)` pour ajouter les compteurs :
- Nombre d'enseignants actifs
- Nombre de parents actifs
- Nombre de liaisons actives (enseignant-élève + parent-élève)
- Nombre d'élèves orphelins (sans enseignant)
- Nombre de demandes de liaison en attente

Modifier `templates/dashboard/admin.html` : ajouter les cartes correspondantes dans la grille de stats.

### 🧪 Tests Phase 6

**11 tests attendus** :
- Accès liste enseignants : admin → 200, non-admin → 403
- Accès détail enseignant : admin → 200, non-admin → 403
- IDOR : accès détail avec `enseignant_id` inexistant → 404
- Pool élèves orphelins : affiche les bons élèves (sans lien validé)
- Assigner un enseignant à un élève orphelin → lien validé créé
- Assigner un enseignant à un élève déjà lié → erreur
- Supprimer un lien → élève retourne dans le pool
- Forcer validation d'un lien en attente → statut "valide"
- Compteurs admin : nombre correct d'enseignants actifs
- Compteurs admin : nombre correct de parents actifs
- Compteurs admin : nombre correct de demandes en attente

### 🔒 Sécurité Phase 6

- **Vérification admin** : toutes les vues admin panel protégées par `request.user.is_admin`
- **IDOR `enseignant_id`** : vérifier que l'ID correspond à un utilisateur avec `role="enseignant"`
- **POST only** : les actions de modification (assigner, supprimer, forcer) sont POST uniquement

### ⚡ Performance Phase 6

- `annotate(Count("eleves_lies"))` pour la liste enseignants (évite N+1 sur le compteur d'élèves)
- `prefetch_related` pour le détail enseignant (élèves + parents de ses élèves)
- `Exists()` subquery pour identifier les élèves orphelins (plus performant que `exclude`)
- Pagination sur la liste des enseignants (25 par page)

---

## Phase 7 — Mode prévisualisation enseignant + Seed data

### Étape 7.1 — Seed data : enseignants, élèves et parents fictifs

**Fichier** : `courses/management/commands/seed_roles_test.py` (nouveau)

Commande : `python manage.py seed_roles_test`

Crée les comptes fictifs suivants (idempotent, basé sur l'email) :

**2 enseignants** :
| Prénom | Nom | Email | Code |
|--------|-----|-------|------|
| Marie | Curie | marie.curie@test.fr | ENS-MC01 |
| Albert | Einstein | albert.einstein@test.fr | ENS-AE02 |

**6 élèves** (3 par enseignant, un par niveau) :
| Prénom | Nom | Email | Niveau | Enseignant |
|--------|-----|-------|--------|------------|
| Lucas | Martin | lucas.martin@test.fr | seconde | Marie Curie |
| Emma | Bernard | emma.bernard@test.fr | premiere | Marie Curie |
| Hugo | Petit | hugo.petit@test.fr | terminale | Marie Curie |
| Léa | Dubois | lea.dubois@test.fr | seconde | Albert Einstein |
| Noah | Moreau | noah.moreau@test.fr | premiere | Albert Einstein |
| Chloé | Laurent | chloe.laurent@test.fr | terminale | Albert Einstein |

**8 parents** (certains élèves ont 1 parent, d'autres 2) :
| Prénom | Nom | Email | Enfant(s) |
|--------|-----|-------|-----------|
| Pierre | Martin | pierre.martin@test.fr | Lucas Martin |
| Sophie | Martin | sophie.martin@test.fr | Lucas Martin |
| Jean | Bernard | jean.bernard@test.fr | Emma Bernard |
| Isabelle | Bernard | isabelle.bernard@test.fr | Emma Bernard |
| François | Petit | francois.petit@test.fr | Hugo Petit |
| Claire | Dubois | claire.dubois@test.fr | Léa Dubois |
| Marc | Moreau | marc.moreau@test.fr | Noah Moreau |
| Anne | Laurent | anne.laurent@test.fr | Chloé Laurent |

**2 élèves orphelins** (sans enseignant, pour tester le pool admin) :
| Prénom | Nom | Email | Niveau |
|--------|-----|-------|--------|
| Thomas | Leroy | thomas.leroy@test.fr | seconde |
| Camille | Roux | camille.roux@test.fr | terminale |

Tous les comptes avec mot de passe `Test1234!`, tous actifs, tous les liens en statut "valide".

Le seed doit aussi :
- Débloquer les premiers chapitres pour chaque élève
- Créer quelques `UserProgression` et `UserQuizResultat` fictifs pour que les dashboards aient des données
- Créer quelques `ConnexionLog` sur les 30 derniers jours pour chaque élève

### Étape 7.2 — Mode prévisualisation enseignant

**Fichier** : `users/views.py`

Même pattern que le mode prévisualisation élève existant (`preview_niveau_view`) :

```
GET /admin-panel/preview/enseignant/<int:enseignant_id>/  → active la preview
GET /admin-panel/preview/exit/                            → quitte (existant, déjà implémenté)
```

**Logique** :
1. `request.session["preview_enseignant_id"] = enseignant_id`
2. Rediriger vers "tableau_de_bord"
3. Dans `TableauDeBordView.get()` : si `preview_enseignant_id` en session → appeler `_dashboard_enseignant(request)` avec les données de cet enseignant (au lieu de `request.user`)
4. Adapter `_dashboard_enseignant()` pour accepter un paramètre optionnel `enseignant_user` (par défaut = `request.user`)

**Fichier** : `templates/base.html`

Ajouter dans la section "Prévisualisation" de la sidebar admin :
- Sous les boutons Seconde/Première/Terminale, une nouvelle section "Vue enseignant" avec un select ou des boutons pour chaque enseignant seed
- Quand actif : bannière jaune "Prévisualisation enseignant : Marie Curie" avec bouton "Quitter"

**Fichier** : `templates/dashboard/admin.html`

Ajouter une section dans le dashboard admin :
- Titre : "Simuler la vue enseignant"
- Liste des enseignants avec un bouton "Voir comme" pour chacun
- Pattern identique à la section "Simuler la vue élève" existante

### Étape 7.3 — Adaptation de `exit_preview_view`

**Fichier** : `users/views.py`

Modifier `exit_preview_view` pour aussi nettoyer `preview_enseignant_id` :
```python
def exit_preview_view(request):
    request.session.pop("preview_niveau", None)
    request.session.pop("preview_enseignant_id", None)
    return redirect("tableau_de_bord")
```

### 🧪 Tests Phase 7

**8 tests attendus** :
- `seed_roles_test` est idempotent (exécuter 2 fois → pas d'erreur)
- `seed_roles_test` crée les bons comptes avec les bons rôles
- `seed_roles_test` crée les liens enseignant-élève validés
- `seed_roles_test` crée les liens parent-élève validés
- Élèves orphelins n'ont pas de lien enseignant
- Preview enseignant : admin peut activer → session key set + redirect dashboard
- Preview enseignant : non-admin tente d'activer → 403
- Exit preview nettoie `preview_enseignant_id` et `preview_niveau`

### 🔒 Sécurité Phase 7

- **Preview réservée à l'admin** : vérification `request.user.is_admin` avant activation
- **Rôle enseignant vérifié** : l'`enseignant_id` doit correspondre à un user avec `role="enseignant"`
- **Writes désactivés** : les writes (progression, quiz) restent désactivés pendant la preview enseignant
- **Emails seed** : tous en `@test.fr` pour ne pas polluer les vrais comptes

---

## Phase 8 — Migrations et déploiement

### Étape 8.1 — Ordre des migrations

1. Ajouter `code_identifiant` à `CustomUser` (nullable d'abord)
2. Data migration : générer les codes pour les utilisateurs existants
3. Rendre `code_identifiant` non-nullable + unique
4. Ajouter les nouveaux choix de rôle
5. Créer les tables `LienEnseignantEleve`, `LienParentEleve`
6. Créer les tables `Notification`
7. Créer les tables `Conversation`, `Message`

### Étape 8.2 — Rétrocompatibilité

- Les comptes élèves existants continuent de fonctionner sans aucun lien
- Le `niveau` est nullable pour les enseignants et parents
- L'ancien URL `/inscription/` redirige vers le choix de rôle
- Les vues existantes ne sont pas cassées (check `is_admin` reste valide)

### Étape 8.3 — Variables d'environnement

Aucune nouvelle variable requise pour cette feature. Les emails de notification utilisent le backend déjà configuré.

### 🧪 Tests Phase 8

**4 tests attendus** :
- Migration réversible (forward + backward sans erreur)
- Data migration : `code_identifiant` généré pour les utilisateurs existants
- Backward compat : `/inscription/` redirige vers choix de rôle
- Les utilisateurs existants (admin + élèves) restent fonctionnels après migration

### 🔒 Sécurité Phase 8

- **Data migration** : les codes générés utilisent `secrets.token_hex()` (pas `random`)
- **Backward compat** : aucune perte d'accès pour les utilisateurs existants

### ⚡ Performance Phase 8

- Les indexes sont créés dans la migration initiale (pas de migration séparée pour les indexes)
- `bulk_update()` pour la data migration des codes (pas de boucle `save()` unitaire)

---

## Ordre d'implémentation recommandé

| Sprint | Phase | Livrable | Tests attendus |
|--------|-------|----------|----------------|
| 1 | Phase 1 | Modèles + migration | 9 tests modèles |
| 2 | Phase 2 | Inscription multi-rôles | 13 tests inscription |
| 3 | Phase 3 | Validation liaisons + notifications | 18 tests validation |
| 4 | Phase 4 | Dashboards + fiche élève | 18 tests dashboards |
| 5 | Phase 5 | Messagerie | 14 tests messagerie |
| 6 | Phase 6 | Panel admin étendu | 11 tests admin |
| 7 | Phase 7 | Seed data + preview enseignant | 8 tests seed/preview |
| 8 | Phase 8 | Migration + déploiement | 4 tests migration |
| | | **TOTAL** | **~95 tests** |

---

## Checklist qualité par sprint

À valider avant de passer au sprint suivant :

### Code
- [ ] Toutes les nouvelles vues ont un docstring
- [ ] Pas de requête N+1 (vérifier avec `django-debug-toolbar` ou `assertNumQueries`)
- [ ] Pas de logique dupliquée (helpers extraits)
- [ ] Imports propres (stdlib / Django / local)

### Tests
- [ ] Tous les tests du sprint passent (0 failure, 0 error)
- [ ] Ratio ≥ 3 tests par vue (anonyme, interdit, autorisé)
- [ ] Tests IDOR pour chaque vue accédant aux données d'un autre utilisateur
- [ ] `force_login()` utilisé partout (pas d'`authenticate()`)

### Sécurité
- [ ] Aucune vue sans vérification de rôle
- [ ] Aucun `|safe` sur des données utilisateur
- [ ] Rate limiting configuré sur les endpoints sensibles
- [ ] Messages d'erreur génériques (pas de fuite d'information)

### Performance
- [ ] Requêtes listées et comptées (objectif : < 10 requêtes par page)
- [ ] Pagination sur toutes les listes
- [ ] `select_related` / `prefetch_related` sur les FK/M2M
- [ ] Cache utilisé pour les compteurs fréquents

---

## Fichiers impactés (résumé)

| Fichier | Nature du changement |
|---------|---------------------|
| `users/models.py` | +4 modèles, +1 champ, +2 propriétés, +1 enum |
| `users/forms.py` | +3 formulaires d'inscription |
| `users/views.py` | +20 vues environ (inscription, validation, dashboards, monitoring, admin enseignants, preview) |
| `users/urls.py` | +20 routes environ |
| `users/admin.py` | +4 modèles enregistrés |
| `users/helpers.py` | Nouveau fichier : `peut_voir_eleve()`, `contacts_autorises()` |
| `users/tests.py` | +95 tests environ |
| `courses/management/commands/seed_roles_test.py` | Nouveau : seed enseignants/élèves/parents fictifs |
| `templates/base.html` | Sidebar conditionnelle par rôle + cloche notifications + preview enseignant |
| `templates/registration/` | +4 templates (choix rôle + 3 formulaires) |
| `templates/dashboard/` | +5 templates (enseignant, parent, fiche élève, admin enseignants, admin enseignant détail) |
| `templates/users/` | +4 templates (liaisons enseignant, liaisons élève, ajout élève, notifications) |
| `templates/messaging/` | +3 templates (inbox, conversation, nouveau) |
| `config/settings/base.py` | Aucun changement requis |
| `progress/models.py` | Aucun changement requis |
