from django.contrib import admin
from .models import UserProgression, UserQuizResultat, ChapitreDebloque, UserChapitreQuizResultat


@admin.register(UserProgression)
class UserProgressionAdmin(admin.ModelAdmin):
    list_display = ["user", "lecon", "statut", "derniere_activite"]
    list_filter = ["statut"]
    raw_id_fields = ["user", "lecon"]


@admin.register(UserQuizResultat)
class UserQuizResultatAdmin(admin.ModelAdmin):
    list_display = ["user", "quiz", "score", "passe", "nb_tentatives", "derniere_tentative"]
    list_filter = ["passe"]
    raw_id_fields = ["user", "quiz"]


@admin.register(ChapitreDebloque)
class ChapitreDebloqueAdmin(admin.ModelAdmin):
    list_display = ["user", "chapitre", "debloque_le"]
    raw_id_fields = ["user", "chapitre"]


@admin.register(UserChapitreQuizResultat)
class UserChapitreQuizResultatAdmin(admin.ModelAdmin):
    list_display = ["user", "chapitre", "score", "passe", "nb_tentatives", "derniere_tentative"]
    list_filter = ["passe"]
    raw_id_fields = ["user", "chapitre"]
