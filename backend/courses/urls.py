from django.urls import path
from . import views

urlpatterns = [
    path("", views.matieres_view, name="matieres"),
    path("revisions/", views.revisions_view, name="revisions"),
    path("revisions/soumettre/", views.soumettre_revisions, name="soumettre_revisions"),
    path("chapitre/<int:chapitre_pk>/", views.chapitre_view, name="chapitre"),
    path("chapitre/<int:chapitre_pk>/quiz/", views.quiz_chapitre_view, name="quiz_chapitre"),
    path("lecon/<int:lecon_pk>/", views.lecon_view, name="lecon"),
    path("lecon/<int:lecon_pk>/quiz/", views.quiz_view, name="quiz"),
    path("lecon/<int:lecon_pk>/pdf/", views.lecon_pdf_view, name="lecon_pdf"),
    path("recherche/", views.recherche_view, name="recherche"),
    # Public routes (no login required)
    path("<slug:matiere_slug>/", views.catalogue_matiere_view, name="catalogue_matiere"),
    path("<slug:matiere_slug>/<str:niveau>/<slug:chapitre_slug>/<slug:lecon_slug>/",
         views.lecon_publique_view, name="lecon_publique"),
]
