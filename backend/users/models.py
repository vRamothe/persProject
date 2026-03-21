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
