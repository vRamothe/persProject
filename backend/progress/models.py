from django.db import models
from django.conf import settings


class StatutLeconChoices(models.TextChoices):
    NON_COMMENCE = "non_commence", "Non commencé"
    EN_COURS = "en_cours", "En cours"
    TERMINE = "termine", "Terminé"


class UserProgression(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="progressions",
        verbose_name="Élève",
    )
    lecon = models.ForeignKey(
        "courses.Lecon",
        on_delete=models.CASCADE,
        related_name="progressions",
        verbose_name="Leçon",
    )
    statut = models.CharField(
        max_length=20,
        choices=StatutLeconChoices.choices,
        default=StatutLeconChoices.NON_COMMENCE,
    )
    derniere_activite = models.DateTimeField(auto_now=True)
    termine_le = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Progression"
        verbose_name_plural = "Progressions"
        unique_together = [["user", "lecon"]]

    def __str__(self):
        return f"{self.user.email} — {self.lecon.titre} ({self.get_statut_display()})"


class UserQuizResultat(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quiz_resultats",
        verbose_name="Élève",
    )
    quiz = models.ForeignKey(
        "courses.Quiz",
        on_delete=models.CASCADE,
        related_name="resultats",
        verbose_name="Quiz",
    )
    score = models.FloatField(default=0.0, verbose_name="Meilleur score (%)")
    nb_tentatives = models.PositiveIntegerField(default=0, verbose_name="Nombre de tentatives")
    passe = models.BooleanField(default=False, verbose_name="Quiz validé")
    reponses = models.JSONField(null=True, blank=True, verbose_name="Dernières réponses")
    premiere_tentative = models.DateTimeField(auto_now_add=True)
    derniere_tentative = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Résultat de quiz"
        verbose_name_plural = "Résultats de quiz"
        unique_together = [["user", "quiz"]]

    def __str__(self):
        return f"{self.user.email} — {self.quiz} — {self.score:.1f}%"


class ChapitreDebloque(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chapitres_debloques",
        verbose_name="Élève",
    )
    chapitre = models.ForeignKey(
        "courses.Chapitre",
        on_delete=models.CASCADE,
        related_name="deblocages",
        verbose_name="Chapitre",
    )
    debloque_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Chapitre débloqué"
        verbose_name_plural = "Chapitres débloqués"
        unique_together = [["user", "chapitre"]]

    def __str__(self):
        return f"{self.user.email} — {self.chapitre.titre}"
