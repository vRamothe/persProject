from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("connexion/", views.ConnexionView.as_view(), name="connexion"),
    path("inscription/", views.InscriptionView.as_view(), name="inscription"),
    path("inscription/confirmation/", views.inscription_confirmation_view, name="inscription_confirmation"),
    path("verifier-email/<str:token>/", views.verifier_email_view, name="verifier_email"),
    path("deconnexion/", views.deconnexion_view, name="deconnexion"),
    path("tableau-de-bord/", views.TableauDeBordView.as_view(), name="tableau_de_bord"),
    path("profil/", views.ProfilView.as_view(), name="profil"),
    # Password reset
    path("mot-de-passe-oublie/", auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset.html",
        email_template_name="registration/password_reset_email.html",
        subject_template_name="registration/password_reset_subject.txt",
        success_url=reverse_lazy("password_reset_done"),
    ), name="password_reset"),
    path("mot-de-passe-oublie/envoye/", auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html",
    ), name="password_reset_done"),
    path("reinitialiser/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html",
        success_url=reverse_lazy("password_reset_complete"),
    ), name="password_reset_confirm"),
    path("reinitialiser/termine/", auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html",
    ), name="password_reset_complete"),
    # Admin panel
    path("admin-panel/utilisateurs/", views.admin_utilisateurs, name="admin_utilisateurs"),
    path("admin-panel/utilisateurs/<int:user_id>/toggle/", views.admin_toggle_actif, name="admin_toggle_actif"),
    path("admin-panel/utilisateurs/<int:user_id>/", views.admin_eleve_detail, name="admin_eleve_detail"),
    path("admin-panel/utilisateurs/<int:user_id>/chapitre/<int:chapitre_id>/toggle/", views.admin_toggle_chapitre, name="admin_toggle_chapitre"),
    path("admin-panel/preview/exit/", views.exit_preview_view, name="exit_preview"),
    path("admin-panel/preview/<str:niveau>/", views.preview_niveau_view, name="preview_niveau"),
    path("admin-panel/analytics/", views.admin_analytics_view, name="admin_analytics"),
    path("admin-panel/tests/", views.admin_tests_view, name="admin_tests"),
    path("admin-panel/rapport-tests/", views.admin_test_report_view, name="admin_test_report"),
    path("admin-panel/rapport-tests/raw/", views.admin_serve_test_report, name="admin_serve_report"),
    path("admin-panel/rapport-tests/run/", views.admin_run_tests_view, name="admin_run_tests"),
]
