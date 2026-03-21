from django.urls import path
from . import views

urlpatterns = [
    path("", views.matieres_view, name="matieres"),
    path("chapitre/<int:chapitre_pk>/", views.chapitre_view, name="chapitre"),
    path("chapitre/<int:chapitre_pk>/quiz/", views.quiz_chapitre_view, name="quiz_chapitre"),
    path("lecon/<int:lecon_pk>/", views.lecon_view, name="lecon"),
    path("lecon/<int:lecon_pk>/quiz/", views.quiz_view, name="quiz"),
]
