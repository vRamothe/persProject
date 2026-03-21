from django.db import models


class MatiereChoices(models.TextChoices):
    PHYSIQUE = "physique", "Physique"
    CHIMIE = "chimie", "Chimie"
    MATHEMATIQUES = "mathematiques", "Mathématiques"


class NiveauChoices(models.TextChoices):
    SECONDE = "seconde", "Seconde"
    PREMIERE = "premiere", "Première"
    TERMINALE = "terminale", "Terminale"


class TypeQuestionChoices(models.TextChoices):
    QCM = "qcm", "QCM (choix multiple)"
    VRAI_FAUX = "vrai_faux", "Vrai / Faux"
    TEXTE_LIBRE = "texte_libre", "Réponse texte libre"


MATIERE_COULEURS = {
    "physique": {"bg": "bg-blue-600", "light": "bg-blue-50", "text": "text-blue-600", "border": "border-blue-200", "hex": "#2563eb"},
    "chimie": {"bg": "bg-emerald-600", "light": "bg-emerald-50", "text": "text-emerald-600", "border": "border-emerald-200", "hex": "#059669"},
    "mathematiques": {"bg": "bg-purple-600", "light": "bg-purple-50", "text": "text-purple-600", "border": "border-purple-200", "hex": "#7c3aed"},
}


class Matiere(models.Model):
    nom = models.CharField(max_length=50, choices=MatiereChoices.choices, unique=True, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Matières"
        ordering = ["nom"]

    def __str__(self):
        return self.get_nom_display()

    @property
    def couleurs(self):
        return MATIERE_COULEURS.get(self.nom, MATIERE_COULEURS["physique"])

    @property
    def icone_svg(self):
        icones = {
            "physique": "⚛",
            "chimie": "🧪",
            "mathematiques": "∑",
        }
        return icones.get(self.nom, "📚")


class Chapitre(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="chapitres", verbose_name="Matière")
    niveau = models.CharField(max_length=20, choices=NiveauChoices.choices, verbose_name="Niveau")
    titre = models.CharField(max_length=255, verbose_name="Titre")
    description = models.TextField(blank=True, verbose_name="Description")
    ordre = models.PositiveIntegerField(default=1, verbose_name="Ordre")
    score_minimum_deblocage = models.FloatField(
        default=60.0,
        verbose_name="Score minimum pour débloquer le suivant (%)",
        help_text="Score moyen aux quiz requis pour débloquer le chapitre suivant.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Chapitre"
        verbose_name_plural = "Chapitres"
        ordering = ["matiere", "niveau", "ordre"]
        unique_together = [["matiere", "niveau", "ordre"]]

    def __str__(self):
        return f"[{self.matiere} – {self.get_niveau_display()}] Ch.{self.ordre} — {self.titre}"

    def get_nb_lecons(self):
        return self.lecons.count()


class Lecon(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE, related_name="lecons", verbose_name="Chapitre")
    titre = models.CharField(max_length=255, verbose_name="Titre")
    contenu = models.TextField(verbose_name="Contenu (Markdown)", help_text="Rédigez le cours en Markdown. Utilisez $...$ pour les équations LaTeX.")
    ordre = models.PositiveIntegerField(default=1, verbose_name="Ordre")
    duree_estimee = models.PositiveIntegerField(default=15, verbose_name="Durée estimée (min)")
    video_youtube_url = models.URLField(
        blank=True,
        default="",
        verbose_name="URL YouTube",
        help_text="Lien YouTube (ex: https://www.youtube.com/watch?v=... ou https://youtu.be/...)",
    )
    video_fichier = models.FileField(
        upload_to="lecons/videos/",
        blank=True,
        default="",
        verbose_name="Fichier vidéo",
        help_text="Téléversez un fichier vidéo (MP4 recommandé). Ignoré si une URL YouTube est renseignée.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Leçon"
        verbose_name_plural = "Leçons"
        ordering = ["chapitre", "ordre"]
        unique_together = [["chapitre", "ordre"]]

    def __str__(self):
        return f"{self.chapitre.titre} – L.{self.ordre} {self.titre}"

    @property
    def has_quiz(self):
        return hasattr(self, "quiz")

    def get_lecon_precedente(self):
        return Lecon.objects.filter(chapitre=self.chapitre, ordre=self.ordre - 1).first()

    def get_lecon_suivante(self):
        return Lecon.objects.filter(chapitre=self.chapitre, ordre=self.ordre + 1).first()


class Quiz(models.Model):
    lecon = models.OneToOneField(Lecon, on_delete=models.CASCADE, related_name="quiz", verbose_name="Leçon")
    titre = models.CharField(max_length=255, verbose_name="Titre")
    score_minimum = models.FloatField(default=60.0, verbose_name="Score minimum pour valider (%)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quiz"

    def __str__(self):
        return f"Quiz – {self.lecon.titre}"

    def get_total_points(self):
        return sum(q.points for q in self.questions.all()) or 1


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions", verbose_name="Quiz")
    texte = models.TextField(verbose_name="Énoncé de la question")
    type = models.CharField(
        max_length=20,
        choices=TypeQuestionChoices.choices,
        default=TypeQuestionChoices.QCM,
        verbose_name="Type",
    )
    options = models.JSONField(
        null=True, blank=True,
        verbose_name="Options de réponse",
        help_text='Pour QCM : ["Option A", "Option B", "Option C", "Option D"]',
    )
    reponse_correcte = models.CharField(
        max_length=500,
        verbose_name="Réponse correcte",
        help_text="Pour QCM : index 0-based (ex: 0, 1, 2...). Pour Vrai/Faux : 'vrai' ou 'faux'. Pour Texte libre : la réponse attendue (insensible à la casse).",
    )
    tolerances = models.JSONField(
        null=True, blank=True,
        verbose_name="Réponses alternatives acceptées",
        help_text='Texte libre uniquement — liste de variantes acceptées : ["réponse alt 1", "réponse alt 2"]',
    )
    explication = models.TextField(blank=True, verbose_name="Explication de la réponse")
    points = models.PositiveIntegerField(default=1, verbose_name="Points")
    ordre = models.PositiveIntegerField(default=1, verbose_name="Ordre")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ["quiz", "ordre"]

    def __str__(self):
        return f"Q{self.ordre}: {self.texte[:60]}…"
