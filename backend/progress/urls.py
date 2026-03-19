from django.urls import path
from . import views

urlpatterns = [
    path("terminer/<int:lecon_pk>/", views.terminer_lecon, name="terminer_lecon"),
    path("quiz/<int:lecon_pk>/soumettre/", views.soumettre_quiz, name="soumettre_quiz"),
]
