from django.db import models
from django.conf import settings
from datetime import date, timedelta


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


class UserChapitreQuizResultat(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chapitre_quiz_resultats",
        verbose_name="Élève",
    )
    chapitre = models.ForeignKey(
        "courses.Chapitre",
        on_delete=models.CASCADE,
        related_name="quiz_resultats",
        verbose_name="Chapitre",
    )
    score = models.FloatField(default=0.0, verbose_name="Meilleur score (%)")
    nb_tentatives = models.PositiveIntegerField(default=0, verbose_name="Nombre de tentatives")
    passe = models.BooleanField(default=False, verbose_name="Quiz chapitre validé")
    reponses = models.JSONField(null=True, blank=True, verbose_name="Dernières réponses")
    premiere_tentative = models.DateTimeField(auto_now_add=True)
    derniere_tentative = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Résultat quiz chapitre"
        verbose_name_plural = "Résultats quiz chapitres"
        unique_together = [["user", "chapitre"]]

    def __str__(self):
        return f"{self.user.email} — {self.chapitre.titre} — {self.score:.1f}%"


# Intervalles Leitner (jours) par boîte
LEITNER_INTERVALLES = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}


class UserQuestionHistorique(models.Model):
    """Suivi par question pour la répétition espacée (système Leitner)."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="question_historiques",
        verbose_name="Élève",
    )
    question = models.ForeignKey(
        "courses.Question",
        on_delete=models.CASCADE,
        related_name="historiques",
        verbose_name="Question",
    )
    boite = models.PositiveSmallIntegerField(default=1, verbose_name="Boîte Leitner (1–5)")
    prochaine_revision = models.DateField(verbose_name="Prochaine révision")
    derniere_reponse_correcte = models.BooleanField(default=False)
    nb_bonnes = models.PositiveIntegerField(default=0)
    nb_total = models.PositiveIntegerField(default=0)
    mis_a_jour_le = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Historique question"
        verbose_name_plural = "Historiques questions"
        unique_together = [["user", "question"]]

    def __str__(self):
        return f"{self.user.email} — Q{self.question_id} boîte {self.boite}"

    def enregistrer_reponse(self, correcte):
        """Met à jour la boîte et la date de prochaine révision."""
        self.nb_total += 1
        self.derniere_reponse_correcte = correcte
        if correcte:
            self.nb_bonnes += 1
            self.boite = min(self.boite + 1, 5)
        else:
            self.boite = 1
        intervalle = LEITNER_INTERVALLES[self.boite]
        self.prochaine_revision = date.today() + timedelta(days=intervalle)
        self.save()
