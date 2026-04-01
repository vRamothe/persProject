from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager


class NiveauChoices(models.TextChoices):
    SECONDE = "seconde", "Seconde"
    PREMIERE = "premiere", "Première"
    TERMINALE = "terminale", "Terminale"


class RoleChoices(models.TextChoices):
    ADMIN = "admin", "Administrateur"
    ELEVE = "eleve", "Élève"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Adresse email")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    role = models.CharField(
        max_length=10,
        choices=RoleChoices.choices,
        default=RoleChoices.ELEVE,
        verbose_name="Rôle",
    )
    niveau = models.CharField(
        max_length=20,
        choices=NiveauChoices.choices,
        blank=True,
        null=True,
        verbose_name="Niveau",
    )
    is_active = models.BooleanField(default=True, verbose_name="Compte actif")
    is_staff = models.BooleanField(default=False, verbose_name="Accès admin Django")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["prenom", "nom"]

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ["nom", "prenom"]

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"

    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    @property
    def initiales(self):
        return f"{self.prenom[:1]}{self.nom[:1]}".upper()

    @property
    def is_admin(self):
        return self.role == RoleChoices.ADMIN

    @property
    def is_eleve(self):
        return self.role == RoleChoices.ELEVE


class ConnexionLog(models.Model):
    """Enregistre chaque connexion réussie d'un utilisateur."""
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="connexions",
        verbose_name="Utilisateur",
    )
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date / heure")
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="Adresse IP")

    class Meta:
        verbose_name = "Connexion"
        verbose_name_plural = "Connexions"
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.user.email} — {self.timestamp}"


class PlanChoices(models.TextChoices):
    MENSUEL = "mensuel", "Mensuel"
    ANNUEL = "annuel", "Annuel"


class StatutAbonnementChoices(models.TextChoices):
    ACTIF = "actif", "Actif"
    ANNULE = "annule", "Annulé"
    EXPIRE = "expire", "Expiré"


class Abonnement(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="abonnement",
        verbose_name="Utilisateur",
    )
    stripe_customer_id = models.CharField(
        max_length=255, verbose_name="Stripe Customer ID"
    )
    stripe_subscription_id = models.CharField(
        max_length=255, blank=True, default="", verbose_name="Stripe Subscription ID"
    )
    plan = models.CharField(
        max_length=20, choices=PlanChoices.choices, verbose_name="Plan"
    )
    statut = models.CharField(
        max_length=20,
        choices=StatutAbonnementChoices.choices,
        default=StatutAbonnementChoices.ACTIF,
        verbose_name="Statut",
    )
    date_debut = models.DateTimeField(verbose_name="Date de début")
    date_fin = models.DateTimeField(null=True, blank=True, verbose_name="Date de fin")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Mis à jour le")

    class Meta:
        verbose_name = "Abonnement"
        verbose_name_plural = "Abonnements"
        indexes = [
            models.Index(fields=["user", "statut"]),
        ]

    def __str__(self):
        return f"{self.user.email} — {self.plan} ({self.statut})"
