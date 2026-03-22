from django.urls import path
from . import views

urlpatterns = [
    path("terminer/<int:lecon_pk>/", views.terminer_lecon, name="terminer_lecon"),
    path("quiz/<int:lecon_pk>/soumettre/", views.soumettre_quiz, name="soumettre_quiz"),
    path("quiz-chapitre/<int:chapitre_pk>/soumettre/", views.soumettre_quiz_chapitre, name="soumettre_quiz_chapitre"),
    path("note/<int:lecon_pk>/sauvegarder/", views.sauvegarder_note, name="sauvegarder_note"),
]
