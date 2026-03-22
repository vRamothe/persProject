from django.contrib import admin
from .models import Matiere, Chapitre, Lecon, Quiz, Question


class LeconInline(admin.TabularInline):
    model = Lecon
    extra = 1
    fields = ["ordre", "titre", "duree_estimee"]
    show_change_link = True


class ChapitreInline(admin.TabularInline):
    model = Chapitre
    extra = 0
    fields = ["niveau", "ordre", "titre", "score_minimum_deblocage"]
    show_change_link = True


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2
    fields = ["ordre", "type", "texte", "options", "reponse_correcte", "tolerances", "explication", "points"]


@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ["get_nom_display", "slug", "description"]
    prepopulated_fields = {"slug": ("nom",)}
    inlines = [ChapitreInline]

    def get_nom_display(self, obj):
        return obj.get_nom_display()
    get_nom_display.short_description = "Matière"


@admin.register(Chapitre)
class ChapitreAdmin(admin.ModelAdmin):
    list_display = ["titre", "slug", "matiere", "get_niveau_display", "ordre", "score_minimum_deblocage", "get_nb_lecons"]
    list_filter = ["matiere", "niveau"]
    search_fields = ["titre"]
    ordering = ["matiere", "niveau", "ordre"]
    prepopulated_fields = {"slug": ("titre",)}
    inlines = [LeconInline]

    def get_niveau_display(self, obj):
        return obj.get_niveau_display()
    get_niveau_display.short_description = "Niveau"

    def get_nb_lecons(self, obj):
        return obj.get_nb_lecons()
    get_nb_lecons.short_description = "Nb leçons"


@admin.register(Lecon)
class LeconAdmin(admin.ModelAdmin):
    list_display = ["titre", "slug", "chapitre", "ordre", "duree_estimee", "gratuit", "has_quiz"]
    list_filter = ["gratuit", "chapitre__matiere", "chapitre__niveau"]
    search_fields = ["titre", "chapitre__titre"]
    ordering = ["chapitre__matiere", "chapitre__niveau", "chapitre__ordre", "ordre"]
    prepopulated_fields = {"slug": ("titre",)}
    fields = ["chapitre", "ordre", "titre", "slug", "gratuit", "duree_estimee", "video_youtube_url", "video_fichier", "contenu"]

    def has_quiz(self, obj):
        return obj.has_quiz
    has_quiz.boolean = True
    has_quiz.short_description = "Quiz"


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["titre", "lecon", "score_minimum", "get_nb_questions"]
    search_fields = ["titre", "lecon__titre"]
    inlines = [QuestionInline]

    def get_nb_questions(self, obj):
        return obj.questions.count()
    get_nb_questions.short_description = "Nb questions"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["texte_court", "quiz", "type", "points", "ordre"]
    list_filter = ["type"]
    search_fields = ["texte", "quiz__lecon__titre"]
    fieldsets = [
        (None, {"fields": ["quiz", "ordre", "type", "texte", "points"]}),
        ("Réponse", {"fields": ["options", "reponse_correcte", "tolerances", "explication"],
                     "description": "Pour Texte libre : laissez «&nbsp;Options&nbsp;» vide. "
                                    "«&nbsp;Réponses alternatives&nbsp;» accepte d'autres formulations, ex: [\"azote\", \"N₂\"]."}),
    ]

    def texte_court(self, obj):
        return obj.texte[:60] + "…" if len(obj.texte) > 60 else obj.texte
    texte_court.short_description = "Question"
