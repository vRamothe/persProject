from django.urls import path
from . import views

urlpatterns = [
    path("connexion/", views.ConnexionView.as_view(), name="connexion"),
    path("inscription/", views.InscriptionView.as_view(), name="inscription"),
    path("deconnexion/", views.deconnexion_view, name="deconnexion"),
    path("tableau-de-bord/", views.TableauDeBordView.as_view(), name="tableau_de_bord"),
    path("profil/", views.ProfilView.as_view(), name="profil"),
    path("admin-panel/utilisateurs/", views.admin_utilisateurs, name="admin_utilisateurs"),
    path("admin-panel/utilisateurs/<int:user_id>/toggle/", views.admin_toggle_actif, name="admin_toggle_actif"),
    path("admin-panel/preview/<str:niveau>/", views.preview_niveau_view, name="preview_niveau"),
    path("admin-panel/preview/exit/", views.exit_preview_view, name="exit_preview"),
]
