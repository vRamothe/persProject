import pytest
from django.test import Client
from django.urls import reverse
from django.core import signing
from users.models import CustomUser


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def eleve(db):
    return CustomUser.objects.create_user(
        email="eleve@test.com",
        password="TestPass123!",
        prenom="Jean",
        nom="Dupont",
        role="eleve",
        niveau="terminale",
    )


@pytest.fixture
def admin_user(db):
    return CustomUser.objects.create_user(
        email="admin@test.com",
        password="AdminPass123!",
        prenom="Admin",
        nom="Principal",
        role="admin",
        is_staff=True,
    )


class TestAccessControl:
    def test_connexion_page_accessible_anonymous(self, client):
        """
        Teste: Accessibilité de la page de connexion pour les utilisateurs anonymes
        Raison: Garantir que la page de login est publique et accessible sans authentification
        Features: Authentification, Page de connexion
        Criticité: basse
        """
        response = client.get(reverse("connexion"))
        assert response.status_code == 200

    def test_inscription_page_accessible_anonymous(self, client):
        """
        Teste: Accessibilité de la page d'inscription pour les utilisateurs anonymes
        Raison: Garantir que la page d'inscription est publique pour permettre les nouvelles inscriptions
        Features: Inscription, Page publique
        Criticité: basse
        """
        response = client.get(reverse("inscription"))
        assert response.status_code == 200

    def test_dashboard_redirects_anonymous_to_login(self, client):
        """
        Teste: Redirection des utilisateurs anonymes vers la page de connexion
        Raison: Protéger le tableau de bord contre les accès non authentifiés
        Features: Authentification, Tableau de bord
        Criticité: haute
        """
        response = client.get(reverse("tableau_de_bord"))
        assert response.status_code == 302
        assert "connexion" in response.url

    def test_profil_requires_login(self, client):
        """
        Teste: Redirection de la page profil pour les utilisateurs non connectés
        Raison: Protéger les données personnelles contre les accès non authentifiés
        Features: Authentification, Profil utilisateur
        Criticité: haute
        """
        response = client.get(reverse("profil"))
        assert response.status_code == 302
        assert "connexion" in response.url

    def test_admin_panel_forbidden_for_eleve(self, client, eleve):
        """
        Teste: Interdiction d'accès au panneau admin pour un élève
        Raison: Empêcher l'escalade de privilèges — seuls les admins doivent gérer les utilisateurs
        Features: Permissions, Panneau admin
        Criticité: haute
        """
        client.force_login(eleve)
        response = client.get(reverse("admin_utilisateurs"))
        # Non-admin gets redirected to dashboard
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    def test_admin_panel_accessible_for_admin(self, client, admin_user):
        """
        Teste: Accès au panneau admin pour un administrateur
        Raison: Vérifier que les admins ont bien accès à la gestion des utilisateurs
        Features: Permissions, Panneau admin
        Criticité: haute
        """
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 200


class TestInscription:
    def test_inscription_creates_eleve(self, client, db):
        """
        Teste: Création d'un compte élève via le formulaire d'inscription
        Raison: Vérifier que l'inscription produit un utilisateur avec le rôle élève et le bon niveau
        Features: Inscription, Création utilisateur
        Criticité: moyenne
        """
        response = client.post(reverse("inscription"), {
            "email": "nouveau@test.com",
            "prenom": "Marie",
            "nom": "Martin",
            "niveau": "seconde",
            "password1": "SecurePass99!",
            "password2": "SecurePass99!",
        })
        assert response.status_code == 302
        user = CustomUser.objects.get(email="nouveau@test.com")
        assert user.role == "eleve"
        assert user.niveau == "seconde"

    def test_inscription_user_is_inactive_after_registration(self, client, db):
        """
        Teste: Compte inactif après inscription (avant vérification email)
        Raison: Empêcher l'accès au compte tant que l'email n'est pas vérifié — protection anti-spam
        Features: Inscription, Vérification email, Sécurité
        Criticité: haute
        """
        client.post(reverse("inscription"), {
            "email": "inactive@test.com",
            "prenom": "Lucie",
            "nom": "Fontaine",
            "niveau": "premiere",
            "password1": "SecurePass99!",
            "password2": "SecurePass99!",
        })
        user = CustomUser.objects.get(email="inactive@test.com")
        assert user.is_active is False

    def test_inscription_sends_verification_email(self, client, db):
        """
        Teste: Envoi d'un email de vérification après inscription
        Raison: Garantir que le flux de vérification email est bien déclenché pour activer le compte
        Features: Inscription, Vérification email
        Criticité: haute
        """
        from django.core import mail
        client.post(reverse("inscription"), {
            "email": "veriftest@test.com",
            "prenom": "Pierre",
            "nom": "Leclerc",
            "niveau": "terminale",
            "password1": "SecurePass99!",
            "password2": "SecurePass99!",
        })
        assert len(mail.outbox) == 1
        assert "veriftest@test.com" in mail.outbox[0].to
        assert "verifier-email" in mail.outbox[0].body

    def test_valid_token_activates_account(self, client, db):
        """
        Teste: Activation du compte avec un token de vérification valide
        Raison: Vérifier que le token signé active correctement le compte et autorise la connexion
        Features: Vérification email, Activation compte, Sécurité
        Criticité: haute
        """
        user = CustomUser.objects.create_user(
            email="toactivate@test.com", password="pass", prenom="A", nom="B",
            role="eleve", niveau="seconde", is_active=False,
        )
        token = signing.dumps(user.pk, salt="email-verification")
        response = client.get(reverse("verifier_email", kwargs={"token": token}))
        assert response.status_code == 302
        user.refresh_from_db()
        assert user.is_active is True

    def test_tampered_token_returns_400(self, client, db):
        """
        Teste: Rejet d'un token de vérification falsifié ou invalide (HTTP 400)
        Raison: Empêcher l'activation de comptes via des tokens forgés — protection anti-falsification
        Features: Vérification email, Sécurité
        Criticité: haute
        """
        response = client.get(reverse("verifier_email", kwargs={"token": "completely-invalid"}))
        assert response.status_code == 400

    def test_inscription_confirmation_page_accessible(self, client):
        """
        Teste: Accessibilité de la page de confirmation d'inscription
        Raison: Vérifier que la page de confirmation s'affiche correctement après inscription
        Features: Inscription, Page de confirmation
        Criticité: basse
        """
        response = client.get(reverse("inscription_confirmation"))
        assert response.status_code == 200


class TestInscriptionFormValidation:
    """Unit tests for InscriptionForm validation logic."""

    def _valid_data(self, **overrides):
        data = {
            "email": "test@example.com",
            "prenom": "Marie",
            "nom": "Dupont",
            "niveau": "seconde",
            "password1": "SecurePass99!",
            "password2": "SecurePass99!",
        }
        data.update(overrides)
        return data

    @pytest.mark.django_db
    def test_password_too_short_rejected(self):
        """
        Teste: Rejet d'un mot de passe trop court à l'inscription
        Raison: Imposer une longueur minimale pour résister aux attaques par force brute
        Features: Inscription, Validation mot de passe, Sécurité
        Criticité: haute
        """
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(password1="Ab1", password2="Ab1"))
        assert form.is_valid() is False
        assert "password1" in form.errors

    @pytest.mark.django_db
    def test_password_no_uppercase_rejected(self):
        """
        Teste: Rejet d'un mot de passe sans majuscule à l'inscription
        Raison: Exiger au moins une majuscule pour renforcer la complexité du mot de passe
        Features: Inscription, Validation mot de passe, Sécurité
        Criticité: haute
        """
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(password1="securepass99!", password2="securepass99!"))
        assert form.is_valid() is False
        assert "password1" in form.errors

    @pytest.mark.django_db
    def test_password_no_digit_rejected(self):
        """
        Teste: Rejet d'un mot de passe sans chiffre à l'inscription
        Raison: Exiger au moins un chiffre pour renforcer la complexité du mot de passe
        Features: Inscription, Validation mot de passe, Sécurité
        Criticité: haute
        """
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(password1="SecurePass!", password2="SecurePass!"))
        assert form.is_valid() is False
        assert "password1" in form.errors

    @pytest.mark.django_db
    def test_passwords_mismatch_rejected(self):
        """
        Teste: Rejet quand les deux mots de passe ne correspondent pas
        Raison: Éviter les erreurs de saisie menant à un mot de passe inconnu de l'utilisateur
        Features: Inscription, Validation formulaire
        Criticité: moyenne
        """
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(password1="SecurePass99!", password2="Different99!"))
        assert form.is_valid() is False
        assert "password2" in form.errors

    @pytest.mark.django_db
    def test_duplicate_email_rejected(self):
        """
        Teste: Rejet d'une inscription avec un email déjà utilisé
        Raison: Garantir l'unicité des comptes et empêcher l'énumération d'utilisateurs
        Features: Inscription, Unicité email, Sécurité
        Criticité: moyenne
        """
        from users.forms import InscriptionForm
        CustomUser.objects.create_user(
            email="test@example.com", password="pass", role="eleve", niveau="seconde",
        )
        form = InscriptionForm(data=self._valid_data())
        assert form.is_valid() is False
        assert "email" in form.errors

    @pytest.mark.django_db
    def test_niveau_required(self):
        """
        Teste: Rejet de l'inscription sans niveau scolaire sélectionné
        Raison: Le niveau est obligatoire pour filtrer le contenu pédagogique affiché à l'élève
        Features: Inscription, Validation formulaire
        Criticité: moyenne
        """
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(niveau=""))
        assert form.is_valid() is False
        assert "niveau" in form.errors

    @pytest.mark.django_db
    def test_valid_form_creates_user(self):
        """
        Teste: Création d'un utilisateur avec des données valides via InscriptionForm
        Raison: Vérifier le chemin nominal d'inscription — rôle, niveau et email corrects
        Features: Inscription, Création utilisateur
        Criticité: moyenne
        """
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data())
        assert form.is_valid() is True
        user = form.save()
        assert user.role == "eleve"
        assert user.niveau == "seconde"
        assert user.email == "test@example.com"

    @pytest.mark.django_db
    def test_inscription_redirects_to_confirmation(self, client):
        """
        Teste: Redirection vers la page de confirmation après inscription réussie
        Raison: Vérifier le flux post-inscription — l'utilisateur doit être guidé vers la confirmation
        Features: Inscription, Redirection
        Criticité: basse
        """
        response = client.post(reverse("inscription"), self._valid_data())
        assert response.status_code == 302
        assert "confirmation" in response.url


class TestProfilFormValidation:
    """Unit tests for ProfilForm validation logic."""

    @pytest.mark.django_db
    def test_profil_form_valid(self, eleve):
        """
        Teste: Validation du formulaire de profil avec des données correctes
        Raison: Vérifier le chemin nominal de modification de profil
        Features: Profil utilisateur, Validation formulaire
        Criticité: moyenne
        """
        from users.forms import ProfilForm
        form = ProfilForm(
            data={"prenom": "Jean", "nom": "Dupont", "email": "eleve@test.com", "niveau": "terminale"},
            instance=eleve,
        )
        assert form.is_valid() is True

    @pytest.mark.django_db
    def test_profil_form_email_required(self, eleve):
        """
        Teste: Rejet du formulaire de profil sans email
        Raison: L'email est l'identifiant unique du compte — son absence casserait l'authentification
        Features: Profil utilisateur, Validation formulaire
        Criticité: moyenne
        """
        from users.forms import ProfilForm
        form = ProfilForm(
            data={"prenom": "Jean", "nom": "Dupont", "email": "", "niveau": "terminale"},
            instance=eleve,
        )
        assert form.is_valid() is False
        assert "email" in form.errors

    @pytest.mark.django_db
    def test_profil_form_saves_changes(self, eleve):
        """
        Teste: Sauvegarde effective des modifications de profil en base de données
        Raison: Vérifier que les changements de prénom, nom et niveau sont bien persistés
        Features: Profil utilisateur, Mise à jour données
        Criticité: moyenne
        """
        from users.forms import ProfilForm
        form = ProfilForm(
            data={"prenom": "Pierre", "nom": "Martin", "email": "eleve@test.com", "niveau": "premiere"},
            instance=eleve,
        )
        assert form.is_valid() is True
        form.save()
        eleve.refresh_from_db()
        assert eleve.prenom == "Pierre"
        assert eleve.nom == "Martin"
        assert eleve.niveau == "premiere"


class TestMotDePasseFormValidation:
    """Unit tests for MotDePasseForm validation logic."""

    def test_mdp_form_valid(self):
        """
        Teste: Validation du formulaire de changement de mot de passe avec données correctes
        Raison: Vérifier le chemin nominal du changement de mot de passe
        Features: Changement mot de passe, Validation formulaire
        Criticité: moyenne
        """
        from users.forms import MotDePasseForm
        form = MotDePasseForm(data={
            "ancien": "OldPass123!",
            "nouveau1": "NewSecure99!",
            "nouveau2": "NewSecure99!",
        })
        assert form.is_valid() is True

    def test_mdp_form_mismatch(self):
        """
        Teste: Rejet quand les deux nouveaux mots de passe ne correspondent pas
        Raison: Empêcher un changement vers un mot de passe que l'utilisateur ne maîtrise pas
        Features: Changement mot de passe, Validation formulaire
        Criticité: moyenne
        """
        from users.forms import MotDePasseForm
        form = MotDePasseForm(data={
            "ancien": "OldPass123!",
            "nouveau1": "NewSecure99!",
            "nouveau2": "Different99!",
        })
        assert form.is_valid() is False
        assert "__all__" in form.errors

    def test_mdp_form_too_short(self):
        """
        Teste: Rejet d'un nouveau mot de passe trop court
        Raison: Imposer une longueur minimale pour résister aux attaques par force brute
        Features: Changement mot de passe, Validation mot de passe, Sécurité
        Criticité: haute
        """
        from users.forms import MotDePasseForm
        form = MotDePasseForm(data={
            "ancien": "OldPass123!",
            "nouveau1": "Ab1",
            "nouveau2": "Ab1",
        })
        assert form.is_valid() is False


class TestConnexionView:
    """Tests for the ConnexionView (login page)."""

    def test_connexion_page_renders_form(self, client):
        """
        Teste: Affichage du formulaire de connexion sur la page de login
        Raison: Vérifier que la page de connexion rend bien un formulaire fonctionnel
        Features: Authentification, Page de connexion
        Criticité: basse
        """
        response = client.get(reverse("connexion"))
        assert response.status_code == 200
        content = response.content.decode()
        assert "Connexion" in content or "form" in content

    @pytest.mark.django_db
    def test_connexion_post_invalid_credentials(self, client):
        """
        Teste: Rejet de la connexion avec des identifiants invalides (pas de redirection)
        Raison: Vérifier qu'un attaquant ne peut pas deviner des identifiants valides via le code HTTP
        Features: Authentification, Sécurité
        Criticité: haute
        """
        response = client.post(reverse("connexion"), {
            "username": "fake@test.com",
            "password": "wrongpassword",
        })
        # Invalid creds re-render the form (200), not redirect (302)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authenticated_user_redirected_from_connexion(self, client, eleve):
        """
        Teste: Redirection d'un utilisateur déjà connecté depuis la page de connexion
        Raison: Éviter qu'un utilisateur authentifié accède inutilement au formulaire de login
        Features: Authentification, Redirection
        Criticité: basse
        """
        client.force_login(eleve)
        response = client.get(reverse("connexion"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url


class TestPasswordReset:
    def test_password_reset_page_accessible(self, client):
        """
        Teste: Accessibilité de la page de demande de réinitialisation de mot de passe
        Raison: Vérifier que le flux de récupération de compte est disponible publiquement
        Features: Réinitialisation mot de passe, Page publique
        Criticité: basse
        """
        response = client.get(reverse("password_reset"))
        assert response.status_code == 200

    def test_password_reset_done_page_accessible(self, client):
        """
        Teste: Accessibilité de la page de confirmation d'envoi du lien de réinitialisation
        Raison: Vérifier que l'utilisateur voit la page de confirmation après sa demande
        Features: Réinitialisation mot de passe, Page publique
        Criticité: basse
        """
        response = client.get(reverse("password_reset_done"))
        assert response.status_code == 200

    def test_password_reset_complete_page_accessible(self, client):
        """
        Teste: Accessibilité de la page de confirmation de réinitialisation de mot de passe
        Raison: Vérifier que la dernière étape du flux de récupération est accessible
        Features: Réinitialisation mot de passe, Page publique
        Criticité: basse
        """
        response = client.get(reverse("password_reset_complete"))
        assert response.status_code == 200


class TestAdminAnalytics:
    def test_anonymous_redirected(self, client):
        """
        Teste: Redirection d'un utilisateur anonyme depuis la page analytics admin
        Raison: Les analytics admin contiennent des données sensibles — accès interdit sans authentification
        Features: Admin analytics, Authentification
        Criticité: haute
        """
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 302

    def test_eleve_redirected_to_dashboard(self, client, eleve):
        """
        Teste: Redirection d'un élève vers le tableau de bord depuis la page analytics
        Raison: Seuls les admins doivent accéder aux analytics — un élève ne doit pas voir les statistiques globales
        Features: Admin analytics, Permissions
        Criticité: haute
        """
        client.force_login(eleve)
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 302

    def test_admin_gets_200(self, client, admin_user):
        """
        Teste: Accès réussi à la page analytics pour un administrateur
        Raison: Vérifier que le chemin nominal d'accès admin fonctionne correctement
        Features: Admin analytics, Permissions
        Criticité: haute
        """
        client.force_login(admin_user)
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 200

    def test_weak_questions_in_context(self, client, admin_user, db):
        """
        Teste: Présence des questions faibles dans le contexte de la page analytics
        Raison: Les questions avec un faible taux de réussite doivent être identifiées pour améliorer le contenu
        Features: Admin analytics, Questions faibles
        Criticité: moyenne
        """
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question
        from progress.models import UserQuestionHistorique
        client.force_login(admin_user)
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="T", ordre=1)
        lecon = Lecon.objects.create(chapitre=chap, titre="L", contenu="c", ordre=1)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q")
        q = Question.objects.create(quiz=quiz, texte="?", type="qcm", reponse_correcte="0", ordre=1)
        UserQuestionHistorique.objects.create(
            user=admin_user, question=q, boite=1,
            prochaine_revision="2024-01-01", nb_bonnes=0, nb_total=5,
        )
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 200
        assert "weak_questions" in response.context

    def test_empty_db_does_not_crash(self, client, admin_user):
        """
        Teste: La page analytics ne plante pas avec une base de données vide
        Raison: Éviter une erreur 500 quand aucun contenu n'existe encore (premier déploiement)
        Features: Admin analytics, Robustesse
        Criticité: moyenne
        """
        client.force_login(admin_user)
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 200


class TestHealthCheck:
    def test_health_returns_200(self, client):
        """
        Teste: Le endpoint health check retourne un code 200
        Raison: Vérifier que le serveur répond — utilisé par le monitoring et les load balancers
        Features: Health check, Monitoring
        Criticité: moyenne
        """
        response = client.get(reverse("health"))
        assert response.status_code == 200

    def test_health_content_type_json(self, client):
        """
        Teste: Le endpoint health check retourne du JSON
        Raison: Les outils de monitoring attendent un Content-Type JSON pour parser la réponse
        Features: Health check, Monitoring
        Criticité: basse
        """
        response = client.get(reverse("health"))
        assert "application/json" in response["Content-Type"]

    def test_health_body(self, client):
        """
        Teste: Le corps de la réponse health check contient {"status": "ok"}
        Raison: Vérifier le format exact attendu par les systèmes de monitoring
        Features: Health check, Monitoring
        Criticité: basse
        """
        import json
        response = client.get(reverse("health"))
        data = json.loads(response.content)
        assert data == {"status": "ok"}


# ============================================================
# Batch 4 — Admin panel views + Preview mode
# ============================================================


class TestAdminUtilisateurs:
    """Tests for the admin_utilisateurs view (user management list)."""

    @pytest.mark.django_db
    def test_eleve_cannot_access(self, client, eleve):
        """
        Teste: Un élève ne peut pas accéder à la liste des utilisateurs admin
        Raison: La liste des utilisateurs expose des données personnelles — accès restreint aux admins
        Features: Admin utilisateurs, Permissions
        Criticité: haute
        """
        client.force_login(eleve)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_gets_200(self, client, admin_user):
        """
        Teste: Un admin accède avec succès à la liste des utilisateurs
        Raison: Vérifier le chemin nominal de la gestion des utilisateurs
        Features: Admin utilisateurs, Permissions
        Criticité: haute
        """
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_filters_by_niveau(self, client, admin_user):
        """
        Teste: Le filtre par niveau retourne uniquement les élèves du niveau sélectionné
        Raison: L'admin doit pouvoir cibler un niveau pour la gestion et le suivi
        Features: Admin utilisateurs, Filtrage
        Criticité: moyenne
        """
        CustomUser.objects.create_user(
            email="sec@t.com", password="p", prenom="A", nom="Sec",
            role="eleve", niveau="seconde",
        )
        CustomUser.objects.create_user(
            email="term@t.com", password="p", prenom="B", nom="Term",
            role="eleve", niveau="terminale",
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"), {"niveau": "seconde"})
        assert response.status_code == 200
        eleves = response.context["eleves"]
        assert all(e.niveau == "seconde" for e in eleves)
        assert any(e.email == "sec@t.com" for e in eleves)

    @pytest.mark.django_db
    def test_filters_by_actif(self, client, admin_user):
        """
        Teste: Le filtre par statut actif/inactif fonctionne correctement
        Raison: L'admin doit distinguer les comptes actifs des comptes désactivés pour la modération
        Features: Admin utilisateurs, Filtrage
        Criticité: moyenne
        """
        active = CustomUser.objects.create_user(
            email="act@t.com", password="p", prenom="A", nom="Act",
            role="eleve", niveau="seconde", is_active=True,
        )
        inactive = CustomUser.objects.create_user(
            email="inact@t.com", password="p", prenom="B", nom="Inact",
            role="eleve", niveau="seconde", is_active=False,
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"), {"actif": "1"})
        assert response.status_code == 200
        eleves = response.context["eleves"]
        emails = [e.email for e in eleves]
        assert active.email in emails
        assert inactive.email not in emails

    @pytest.mark.django_db
    def test_search_by_name(self, client, admin_user):
        """
        Teste: La recherche par nom retourne l'utilisateur correspondant
        Raison: L'admin doit pouvoir retrouver rapidement un élève par son nom
        Features: Admin utilisateurs, Recherche
        Criticité: moyenne
        """
        CustomUser.objects.create_user(
            email="unique@t.com", password="p", prenom="A", nom="UniqueNom",
            role="eleve", niveau="seconde",
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"), {"q": "UniqueNom"})
        assert response.status_code == 200
        eleves = response.context["eleves"]
        assert any(e.nom == "UniqueNom" for e in eleves)

    @pytest.mark.django_db
    def test_empty_search_returns_all(self, client, admin_user):
        """
        Teste: Une recherche vide retourne tous les élèves
        Raison: Vérifier que l'absence de filtre ne masque aucun utilisateur
        Features: Admin utilisateurs, Recherche
        Criticité: basse
        """
        CustomUser.objects.create_user(
            email="e1@t.com", password="p", prenom="A", nom="A",
            role="eleve", niveau="seconde",
        )
        CustomUser.objects.create_user(
            email="e2@t.com", password="p", prenom="B", nom="B",
            role="eleve", niveau="terminale",
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 200
        eleves = response.context["eleves"]
        assert len(eleves) >= 2

    @pytest.mark.django_db
    def test_context_has_progression_pct(self, client, admin_user):
        """
        Teste: Chaque élève dans la liste a un attribut progression_pct
        Raison: Le pourcentage de progression est affiché dans le tableau admin — son absence casserait le template
        Features: Admin utilisateurs, Progression
        Criticité: moyenne
        """
        CustomUser.objects.create_user(
            email="prog@t.com", password="p", prenom="A", nom="Prog",
            role="eleve", niveau="seconde",
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        eleves = response.context["eleves"]
        assert len(eleves) >= 1
        assert hasattr(eleves[0], "progression_pct")


class TestAdminToggleActif:
    """Tests for the admin_toggle_actif view."""

    @pytest.mark.django_db
    def test_eleve_cannot_toggle(self, client, eleve):
        """
        Teste: Un élève ne peut pas activer/désactiver un compte utilisateur
        Raison: Le toggle actif/inactif est une action admin critique — un élève ne doit jamais y accéder
        Features: Admin toggle actif, Permissions
        Criticité: haute
        """
        client.force_login(eleve)
        url = reverse("admin_toggle_actif", kwargs={"user_id": eleve.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_toggles_active_to_inactive(self, client, admin_user, eleve):
        """
        Teste: Un admin peut désactiver un compte élève actif
        Raison: Permettre la suspension de comptes en cas d'abus ou de demande de suppression
        Features: Admin toggle actif, Gestion comptes
        Criticité: haute
        """
        assert eleve.is_active is True
        client.force_login(admin_user)
        url = reverse("admin_toggle_actif", kwargs={"user_id": eleve.pk})
        response = client.post(url)
        assert response.status_code == 302
        eleve.refresh_from_db()
        assert eleve.is_active is False

    @pytest.mark.django_db
    def test_admin_toggles_inactive_to_active(self, client, admin_user):
        """
        Teste: Un admin peut réactiver un compte élève inactif
        Raison: Permettre la réactivation d'un compte après une suspension temporaire
        Features: Admin toggle actif, Gestion comptes
        Criticité: haute
        """
        inactive_eleve = CustomUser.objects.create_user(
            email="off@t.com", password="p", prenom="A", nom="Off",
            role="eleve", niveau="seconde", is_active=False,
        )
        client.force_login(admin_user)
        url = reverse("admin_toggle_actif", kwargs={"user_id": inactive_eleve.pk})
        response = client.post(url)
        assert response.status_code == 302
        inactive_eleve.refresh_from_db()
        assert inactive_eleve.is_active is True

    @pytest.mark.django_db
    def test_get_request_redirects(self, client, admin_user, eleve):
        """
        Teste: Une requête GET sur toggle_actif redirige sans modifier l'état du compte
        Raison: Seul POST doit modifier l'état — empêcher les modifications accidentelles via navigation
        Features: Admin toggle actif, Sécurité CSRF
        Criticité: haute
        """
        client.force_login(admin_user)
        url = reverse("admin_toggle_actif", kwargs={"user_id": eleve.pk})
        response = client.get(url)
        assert response.status_code == 302
        # GET should NOT toggle is_active
        eleve.refresh_from_db()
        assert eleve.is_active is True


class TestAdminEleveDetail:
    """Tests for the admin_eleve_detail view."""

    @pytest.mark.django_db
    def test_eleve_cannot_access(self, client, eleve):
        """
        Teste: Un élève ne peut pas accéder au détail d'un autre élève
        Raison: Les données de progression individuelles sont confidentielles — accès admin uniquement
        Features: Admin détail élève, Permissions
        Criticité: haute
        """
        client.force_login(eleve)
        url = reverse("admin_eleve_detail", kwargs={"user_id": eleve.pk})
        response = client.get(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_gets_200(self, client, admin_user, eleve):
        """
        Teste: Un admin accède avec succès au détail d'un élève
        Raison: Vérifier le chemin nominal d'accès à la fiche élève
        Features: Admin détail élève, Permissions
        Criticité: haute
        """
        client.force_login(admin_user)
        url = reverse("admin_eleve_detail", kwargs={"user_id": eleve.pk})
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_context_has_progression_data(self, client, admin_user, eleve):
        """
        Teste: Le contexte de la page détail élève contient les données de progression
        Raison: Le template affiche la progression globale — son absence provoquerait une erreur de rendu
        Features: Admin détail élève, Progression
        Criticité: moyenne
        """
        client.force_login(admin_user)
        url = reverse("admin_eleve_detail", kwargs={"user_id": eleve.pk})
        response = client.get(url)
        assert "progression_globale" in response.context
        assert "eleve" in response.context

    @pytest.mark.django_db
    def test_nonexistent_user_returns_404(self, client, admin_user):
        """
        Teste: Un ID utilisateur inexistant retourne une erreur 404
        Raison: Éviter une erreur 500 si un admin accède à un utilisateur supprimé ou inexistant
        Features: Admin détail élève, Robustesse
        Criticité: moyenne
        """
        client.force_login(admin_user)
        url = reverse("admin_eleve_detail", kwargs={"user_id": 99999})
        response = client.get(url)
        assert response.status_code == 404


class TestAdminToggleChapitre:
    """Tests for the admin_toggle_chapitre view."""

    @pytest.mark.django_db
    def test_eleve_cannot_toggle_chapitre(self, client, eleve):
        """
        Teste: Un élève ne peut pas débloquer/verrouiller un chapitre manuellement
        Raison: Le déblocage de chapitres est une action admin — un élève contournerait la progression
        Features: Admin toggle chapitre, Permissions
        Criticité: haute
        """
        from courses.models import Matiere, Chapitre
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="Ch", ordre=1)
        client.force_login(eleve)
        url = reverse("admin_toggle_chapitre", kwargs={"user_id": eleve.pk, "chapitre_id": chap.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_unlocks_chapitre(self, client, admin_user, eleve):
        """
        Teste: Un admin peut débloquer un chapitre pour un élève
        Raison: Permettre le déblocage manuel en cas de besoin pédagogique ou de support
        Features: Admin toggle chapitre, Déblocage
        Criticité: haute
        """
        from courses.models import Matiere, Chapitre
        from progress.models import ChapitreDebloque
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="Ch", ordre=1)
        assert ChapitreDebloque.objects.filter(user=eleve, chapitre=chap).count() == 0
        client.force_login(admin_user)
        url = reverse("admin_toggle_chapitre", kwargs={"user_id": eleve.pk, "chapitre_id": chap.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert ChapitreDebloque.objects.filter(user=eleve, chapitre=chap).count() == 1

    @pytest.mark.django_db
    def test_admin_locks_chapitre(self, client, admin_user, eleve):
        """
        Teste: Un admin peut reverrouiller un chapitre déjà débloqué
        Raison: Permettre la correction d'un déblocage accidentel ou la réinitialisation de progression
        Features: Admin toggle chapitre, Verrouillage
        Criticité: haute
        """
        from courses.models import Matiere, Chapitre
        from progress.models import ChapitreDebloque
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="Ch", ordre=1)
        ChapitreDebloque.objects.create(user=eleve, chapitre=chap)
        client.force_login(admin_user)
        url = reverse("admin_toggle_chapitre", kwargs={"user_id": eleve.pk, "chapitre_id": chap.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert ChapitreDebloque.objects.filter(user=eleve, chapitre=chap).count() == 0

    @pytest.mark.django_db
    def test_get_request_redirects(self, client, admin_user, eleve):
        """
        Teste: Une requête GET sur toggle_chapitre redirige sans modifier le déblocage
        Raison: Seul POST doit modifier l'état — empêcher les modifications accidentelles via navigation
        Features: Admin toggle chapitre, Sécurité CSRF
        Criticité: haute
        """
        from courses.models import Matiere, Chapitre
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="Ch", ordre=1)
        client.force_login(admin_user)
        url = reverse("admin_toggle_chapitre", kwargs={"user_id": eleve.pk, "chapitre_id": chap.pk})
        response = client.get(url)
        assert response.status_code == 302


class TestPreviewMode:
    """Tests for preview_niveau_view and exit_preview_view."""

    @pytest.mark.django_db
    def test_eleve_cannot_activate_preview(self, client, eleve):
        """
        Teste: Un élève ne peut pas activer le mode preview
        Raison: Le mode preview est réservé aux admins — un élève pourrait voir du contenu hors de son niveau
        Features: Preview mode, Permissions
        Criticité: haute
        """
        client.force_login(eleve)
        url = reverse("preview_niveau", kwargs={"niveau": "seconde"})
        response = client.get(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_activates_preview(self, client, admin_user):
        """
        Teste: Un admin active le mode preview et est redirigé vers les cours
        Raison: Vérifier que le mode preview stocke le niveau en session et redirige correctement
        Features: Preview mode, Session
        Criticité: moyenne
        """
        client.force_login(admin_user)
        url = reverse("preview_niveau", kwargs={"niveau": "seconde"})
        response = client.get(url)
        assert response.status_code == 302
        assert "cours" in response.url  # redirects to matieres
        session = client.session
        assert session.get("preview_niveau") == "seconde"

    @pytest.mark.django_db
    def test_invalid_niveau_redirects(self, client, admin_user):
        """
        Teste: Un niveau invalide redirige vers le tableau de bord
        Raison: Empêcher l'injection de valeurs arbitraires dans la session preview
        Features: Preview mode, Validation
        Criticité: moyenne
        """
        client.force_login(admin_user)
        url = reverse("preview_niveau", kwargs={"niveau": "invalid"})
        response = client.get(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_exit_preview_clears_session(self, client, admin_user):
        """
        Teste: La sortie du mode preview supprime la clé de session
        Raison: Un résidu de session provoquerait un filtrage incorrect des contenus après la sortie
        Features: Preview mode, Session
        Criticité: moyenne
        """
        client.force_login(admin_user)
        session = client.session
        session["preview_niveau"] = "seconde"
        session.save()
        response = client.get(reverse("exit_preview"))
        assert response.status_code == 302
        assert "preview_niveau" not in client.session

    @pytest.mark.django_db
    def test_exit_preview_redirects_to_dashboard(self, client, admin_user):
        """
        Teste: La sortie du mode preview redirige vers le tableau de bord
        Raison: L'admin doit retrouver son interface normale après avoir quitté le mode preview
        Features: Preview mode, Redirection
        Criticité: basse
        """
        client.force_login(admin_user)
        response = client.get(reverse("exit_preview"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_preview_mode_lecon_no_progression_write(self, client, admin_user):
        """
        Teste: En mode preview, visiter une leçon ne crée pas de UserProgression
        Raison: Le mode preview simule la vue élève — écrire en base fausserait les statistiques
        Features: Preview mode, Progression, Intégrité données
        Criticité: haute
        """
        from courses.models import Matiere, Chapitre, Lecon
        from progress.models import UserProgression
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(
            matiere=mat, niveau="seconde", titre="Preview Ch", ordre=1,
        )
        lecon = Lecon.objects.create(
            chapitre=chap, ordre=1, titre="Preview Lecon",
            contenu="# Test", duree_estimee=10,
        )
        client.force_login(admin_user)
        # Activate preview mode
        session = client.session
        session["preview_niveau"] = "seconde"
        session.save()
        url = reverse("lecon", kwargs={"lecon_pk": lecon.pk})
        response = client.get(url)
        assert response.status_code == 200
        assert UserProgression.objects.filter(user=admin_user, lecon=lecon).count() == 0


# ============================================================
# Batch 5 — ProfilView
# ============================================================


class TestProfilView:
    """Tests for the ProfilView CBV (profile + password change)."""

    @pytest.mark.django_db
    def test_profil_requires_login(self, client):
        """
        Teste: L'accès au profil redirige vers la connexion si non authentifié
        Raison: La page profil contient des données personnelles — accès non authentifié interdit
        Features: Profil, Authentification
        Criticité: haute
        """
        response = client.get(reverse("profil"))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_profil_get_returns_200(self, client, eleve):
        """
        Teste: Un élève connecté accède à sa page profil avec un code 200
        Raison: Vérifier le chemin nominal d'accès au profil
        Features: Profil
        Criticité: moyenne
        """
        client.force_login(eleve)
        response = client.get(reverse("profil"))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_profil_get_has_forms_in_context(self, client, eleve):
        """
        Teste: Le contexte de la page profil contient les formulaires profil et mot de passe
        Raison: L'absence de ces formulaires casserait le rendu du template
        Features: Profil, Formulaires
        Criticité: moyenne
        """
        client.force_login(eleve)
        response = client.get(reverse("profil"))
        assert "form_profil" in response.context
        assert "form_mdp" in response.context

    @pytest.mark.django_db
    def test_profil_update_nom_prenom(self, client, eleve):
        """
        Teste: La mise à jour du nom et prénom via le formulaire profil fonctionne
        Raison: Vérifier que les données personnelles sont bien persistées en base
        Features: Profil, Formulaires
        Criticité: moyenne
        """
        client.force_login(eleve)
        data = {
            "action": "profil",
            "prenom": "NouveauPrenom",
            "nom": "NouveauNom",
            "email": eleve.email,
            "niveau": eleve.niveau,
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 302
        eleve.refresh_from_db()
        assert eleve.prenom == "NouveauPrenom"
        assert eleve.nom == "NouveauNom"

    @pytest.mark.django_db
    def test_profil_update_invalid_email(self, client, eleve):
        """
        Teste: Un email vide dans le formulaire profil provoque une erreur de validation
        Raison: L'email est le login unique — un email vide corromprait le compte
        Features: Profil, Validation formulaires
        Criticité: haute
        """
        client.force_login(eleve)
        data = {
            "action": "profil",
            "prenom": "Jean",
            "nom": "Dupont",
            "email": "",
            "niveau": eleve.niveau,
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 200
        assert response.context["form_profil"].errors

    @pytest.mark.django_db
    def test_password_change_success(self, client, eleve):
        """
        Teste: Le changement de mot de passe avec les bonnes données réussit
        Raison: Vérifier que le nouveau mot de passe est bien hashé et persisté
        Features: Profil, Changement mot de passe
        Criticité: haute
        """
        client.force_login(eleve)
        data = {
            "action": "mot_de_passe",
            "ancien": "TestPass123!",
            "nouveau1": "NewSecure88!",
            "nouveau2": "NewSecure88!",
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 302
        eleve.refresh_from_db()
        assert eleve.check_password("NewSecure88!")

    @pytest.mark.django_db
    def test_password_change_wrong_ancien(self, client, eleve):
        """
        Teste: Un ancien mot de passe incorrect est rejeté avec une erreur de validation
        Raison: Empêcher un attaquant ayant volé une session de changer le mot de passe
        Features: Profil, Changement mot de passe, Sécurité
        Criticité: haute
        """
        client.force_login(eleve)
        data = {
            "action": "mot_de_passe",
            "ancien": "WrongOldPass!",
            "nouveau1": "NewSecure88!",
            "nouveau2": "NewSecure88!",
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 200
        assert "ancien" in response.context["form_mdp"].errors

    @pytest.mark.django_db
    def test_password_change_mismatch(self, client, eleve):
        """
        Teste: Des mots de passe de confirmation différents sont rejetés
        Raison: Empêcher un changement de mot de passe avec une erreur de saisie
        Features: Profil, Changement mot de passe, Validation
        Criticité: haute
        """
        client.force_login(eleve)
        data = {
            "action": "mot_de_passe",
            "ancien": "TestPass123!",
            "nouveau1": "NewSecure88!",
            "nouveau2": "DifferentPass99!",
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 200


# ---------------------------------------------------------------------------
# Stripe Integration Tests
# ---------------------------------------------------------------------------

import json
from unittest.mock import patch, MagicMock
from users.models import Abonnement
from courses.models import Matiere, Chapitre, Lecon


@pytest.fixture
def eleve_stripe(db):
    return CustomUser.objects.create_user(
        email="stripe_eleve@test.com",
        password="TestPass123!",
        prenom="Marie",
        nom="Curie",
        role="eleve",
        niveau="terminale",
    )


@pytest.fixture
def admin_stripe(db):
    return CustomUser.objects.create_user(
        email="stripe_admin@test.com",
        password="AdminPass123!",
        prenom="Admin",
        nom="Stripe",
        role="admin",
        is_staff=True,
    )


@pytest.fixture
def matiere_stripe(db):
    return Matiere.objects.create(nom="physique")


@pytest.fixture
def chapitre_stripe(db, matiere_stripe):
    return Chapitre.objects.create(
        matiere=matiere_stripe,
        niveau="terminale",
        ordre=1,
        titre="Mécanique",
        description="Chapitre mécanique",
    )


@pytest.fixture
def lecon_premium(db, chapitre_stripe):
    return Lecon.objects.create(
        chapitre=chapitre_stripe,
        ordre=1,
        titre="Forces et interactions",
        contenu="# Forces\n\nContenu premium.",
        duree_estimee=30,
        gratuit=False,
    )


@pytest.fixture
def lecon_gratuite_stripe(db, chapitre_stripe):
    return Lecon.objects.create(
        chapitre=chapitre_stripe,
        ordre=2,
        titre="Introduction mécanique",
        contenu="# Intro\n\nContenu gratuit.",
        duree_estimee=15,
        gratuit=True,
    )


@pytest.fixture
def abonnement_actif(db, eleve_stripe):
    from django.utils import timezone

    return Abonnement.objects.create(
        user=eleve_stripe,
        stripe_customer_id="cus_test123",
        stripe_subscription_id="sub_test123",
        plan="mensuel",
        statut="actif",
        date_debut=timezone.now(),
    )


class TestStripeCheckout:
    @pytest.mark.django_db
    @patch("users.views.stripe.checkout.Session.create")
    @patch("users.views.stripe.Customer.create")
    def test_creer_checkout_session_redirects_to_stripe(
        self, mock_customer_create, mock_session_create, client, eleve_stripe
    ):
        """
        Teste: La création d'une session checkout Stripe redirige vers l'URL Stripe
        Raison: Vérifier que le flux de paiement mensuel redirige correctement vers Stripe
        Features: Stripe, Paiement, Checkout
        Criticité: haute
        """
        mock_customer_create.return_value = MagicMock(id="cus_new123")
        mock_session = MagicMock()
        mock_session.url = "https://checkout.stripe.com/test_session"
        mock_session_create.return_value = mock_session

        client.force_login(eleve_stripe)
        response = client.post(reverse("checkout"), {"plan": "mensuel"})
        assert response.status_code == 302
        assert response["Location"] == "https://checkout.stripe.com/test_session"
        mock_session_create.assert_called_once()

    @pytest.mark.django_db
    @patch("users.views.stripe.checkout.Session.create")
    @patch("users.views.stripe.Customer.create")
    def test_creer_checkout_session_annual(
        self, mock_customer_create, mock_session_create, client, eleve_stripe, settings
    ):
        """
        Teste: Le checkout annuel utilise le bon price_id Stripe
        Raison: Un mauvais price_id facturerait un montant incorrect à l'utilisateur
        Features: Stripe, Paiement, Checkout annuel
        Criticité: haute
        """
        mock_customer_create.return_value = MagicMock(id="cus_new456")
        mock_session = MagicMock()
        mock_session.url = "https://checkout.stripe.com/annual_session"
        mock_session_create.return_value = mock_session

        settings.STRIPE_PRICE_ANNUAL = "price_annual_test"

        client.force_login(eleve_stripe)
        response = client.post(reverse("checkout"), {"plan": "annuel"})
        assert response.status_code == 302

        call_kwargs = mock_session_create.call_args[1]
        assert call_kwargs["line_items"][0]["price"] == "price_annual_test"

    @pytest.mark.django_db
    def test_checkout_requires_login(self, client):
        """
        Teste: L'endpoint checkout redirige vers la connexion si non authentifié
        Raison: Un utilisateur anonyme ne doit pas pouvoir initier un paiement
        Features: Stripe, Checkout, Authentification
        Criticité: haute
        """
        response = client.post(reverse("checkout"), {"plan": "mensuel"})
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]


class TestStripeWebhook:
    def _build_webhook_payload(self, event_type, data_object, event_id="evt_test1"):
        return {
            "id": event_id,
            "type": event_type,
            "data": {"object": data_object},
        }

    @pytest.mark.django_db
    @patch("users.views.stripe.Webhook.construct_event")
    def test_webhook_checkout_completed_creates_abonnement(
        self, mock_construct, client, eleve_stripe
    ):
        """
        Teste: Le webhook checkout.session.completed crée un abonnement actif
        Raison: C'est le point d'activation du paiement — une défaillance bloquerait l'accès premium
        Features: Stripe, Webhook, Abonnement
        Criticité: haute
        """
        event_data = self._build_webhook_payload(
            "checkout.session.completed",
            {
                "metadata": {
                    "user_id": str(eleve_stripe.pk),
                    "plan": "mensuel",
                },
                "customer": "cus_webhook123",
                "subscription": "sub_webhook123",
            },
        )
        mock_construct.return_value = event_data

        response = client.post(
            reverse("stripe_webhook"),
            data=json.dumps(event_data),
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="sig_test",
        )
        assert response.status_code == 200

        abo = Abonnement.objects.get(user=eleve_stripe)
        assert abo.statut == "actif"
        assert abo.stripe_customer_id == "cus_webhook123"
        assert abo.stripe_subscription_id == "sub_webhook123"
        assert abo.plan == "mensuel"

    @pytest.mark.django_db
    @patch("users.views.stripe.Webhook.construct_event")
    def test_webhook_subscription_deleted_deactivates(
        self, mock_construct, client, eleve_stripe, abonnement_actif
    ):
        """
        Teste: Le webhook subscription.deleted désactive l'abonnement
        Raison: Un abonnement annulé chez Stripe doit couper l'accès premium côté Django
        Features: Stripe, Webhook, Désactivation abonnement
        Criticité: haute
        """
        event_data = self._build_webhook_payload(
            "customer.subscription.deleted",
            {
                "id": "sub_test123",
                "status": "canceled",
            },
        )
        mock_construct.return_value = event_data

        response = client.post(
            reverse("stripe_webhook"),
            data=json.dumps(event_data),
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="sig_test",
        )
        assert response.status_code == 200

        abonnement_actif.refresh_from_db()
        assert abonnement_actif.statut == "annule"

    @pytest.mark.django_db
    @patch("users.views.stripe.Webhook.construct_event")
    def test_webhook_rejects_invalid_signature(self, mock_construct, client):
        """
        Teste: Un webhook avec une signature invalide est rejeté avec un code 400
        Raison: Empêcher l'injection de faux événements Stripe par un attaquant
        Features: Stripe, Webhook, Sécurité signature
        Criticité: haute
        """
        import stripe as _stripe

        mock_construct.side_effect = _stripe.error.SignatureVerificationError(
            "Invalid signature", "sig_header"
        )

        response = client.post(
            reverse("stripe_webhook"),
            data=b"bad_payload",
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="bad_sig",
        )
        assert response.status_code == 400

    @pytest.mark.django_db
    @patch("users.views.stripe.Webhook.construct_event")
    def test_webhook_idempotent_on_duplicate_event(
        self, mock_construct, client, eleve_stripe
    ):
        """
        Teste: Un événement webhook dupliqué ne crée pas de doublon d'abonnement
        Raison: Stripe peut renvoyer le même événement — l'idempotence évite les données corrompues
        Features: Stripe, Webhook, Idempotence
        Criticité: haute
        """
        event_data = self._build_webhook_payload(
            "checkout.session.completed",
            {
                "metadata": {
                    "user_id": str(eleve_stripe.pk),
                    "plan": "annuel",
                },
                "customer": "cus_idem123",
                "subscription": "sub_idem123",
            },
            event_id="evt_duplicate",
        )
        mock_construct.return_value = event_data

        for _ in range(2):
            response = client.post(
                reverse("stripe_webhook"),
                data=json.dumps(event_data),
                content_type="application/json",
                HTTP_STRIPE_SIGNATURE="sig_test",
            )
            assert response.status_code == 200

        assert Abonnement.objects.filter(user=eleve_stripe).count() == 1


class TestPremiumLessonAccess:
    def _lecon_publique_url(self, matiere, lecon):
        return reverse(
            "lecon_publique",
            kwargs={
                "matiere_slug": matiere.slug,
                "niveau": lecon.chapitre.niveau,
                "chapitre_slug": lecon.chapitre.slug,
                "lecon_slug": lecon.slug,
            },
        )

    @pytest.mark.django_db
    def test_premium_lesson_requires_active_subscription(
        self, client, eleve_stripe, matiere_stripe, lecon_premium
    ):
        """
        Teste: Une leçon premium est floutée pour un élève sans abonnement actif
        Raison: Le contenu premium ne doit pas être lisible sans paiement
        Features: Accès premium, Paywall, Abonnement
        Criticité: haute
        """
        client.force_login(eleve_stripe)
        url = self._lecon_publique_url(matiere_stripe, lecon_premium)
        response = client.get(url)
        assert response.status_code == 200
        assert response.context["est_floute"] is True

    @pytest.mark.django_db
    def test_premium_lesson_accessible_with_active_subscription(
        self, client, eleve_stripe, matiere_stripe, lecon_premium, abonnement_actif
    ):
        """
        Teste: Une leçon premium est accessible sans flou avec un abonnement actif
        Raison: Un abonné payant doit accéder au contenu complet sans restriction
        Features: Accès premium, Abonnement
        Criticité: haute
        """
        client.force_login(eleve_stripe)
        url = self._lecon_publique_url(matiere_stripe, lecon_premium)
        response = client.get(url)
        assert response.status_code == 200
        assert response.context["est_floute"] is False

    @pytest.mark.django_db
    def test_admin_bypasses_subscription_check(
        self, client, admin_stripe, matiere_stripe, lecon_premium
    ):
        """
        Teste: Un admin est redirigé vers la vue interne sans vérification d'abonnement
        Raison: Les admins doivent toujours accéder au contenu pour le vérifier
        Features: Accès premium, Admin bypass
        Criticité: haute
        """
        client.force_login(admin_stripe)
        url = self._lecon_publique_url(matiere_stripe, lecon_premium)
        response = client.get(url)
        # Admin gets redirected to internal lecon view
        assert response.status_code == 302
        expected_url = reverse("lecon", kwargs={"lecon_pk": lecon_premium.pk})
        assert response["Location"] == expected_url


class TestPortailClient:
    @pytest.mark.django_db
    @patch("users.views.stripe.billing_portal.Session.create")
    def test_portail_client_redirects_to_stripe(
        self, mock_portal_create, client, eleve_stripe, abonnement_actif
    ):
        """
        Teste: Le portail client redirige vers le portail Stripe Billing
        Raison: L'utilisateur doit pouvoir gérer son abonnement via Stripe
        Features: Stripe, Portail client, Abonnement
        Criticité: haute
        """
        mock_session = MagicMock()
        mock_session.url = "https://billing.stripe.com/portal_session"
        mock_portal_create.return_value = mock_session

        client.force_login(eleve_stripe)
        response = client.get(reverse("portail_abonnement"))
        assert response.status_code == 302
        assert response["Location"] == "https://billing.stripe.com/portal_session"

    @pytest.mark.django_db
    def test_portail_client_no_subscription(self, client, eleve_stripe):
        """
        Teste: Un utilisateur sans abonnement est redirigé vers le profil
        Raison: Éviter une erreur Stripe si aucun customer_id n'existe
        Features: Stripe, Portail client
        Criticité: moyenne
        """
        client.force_login(eleve_stripe)
        response = client.get(reverse("portail_abonnement"))
        assert response.status_code == 302
        assert "/profil/" in response["Location"]


class TestUserHasActiveSubscription:
    @pytest.mark.django_db
    def test_user_has_active_subscription_true(self, eleve_stripe, abonnement_actif):
        """
        Teste: Un utilisateur avec un abonnement actif retourne True
        Raison: Vérifier le chemin nominal de la vérification d'abonnement
        Features: Abonnement, Accès premium
        Criticité: haute
        """
        from users.views import _user_has_active_subscription

        assert _user_has_active_subscription(eleve_stripe) is True

    @pytest.mark.django_db
    def test_user_has_active_subscription_false(self, eleve_stripe):
        """
        Teste: Un utilisateur sans abonnement retourne False
        Raison: Un non-abonné ne doit pas avoir accès au contenu premium
        Features: Abonnement, Accès premium
        Criticité: haute
        """
        from users.views import _user_has_active_subscription

        assert _user_has_active_subscription(eleve_stripe) is False

    @pytest.mark.django_db
    def test_user_has_active_subscription_annule(self, eleve_stripe, abonnement_actif):
        """
        Teste: Un abonnement annulé retourne False
        Raison: Un abonnement annulé ne doit plus donner accès au contenu premium
        Features: Abonnement, Désactivation, Accès premium
        Criticité: haute
        """
        from users.views import _user_has_active_subscription

        abonnement_actif.statut = "annule"
        abonnement_actif.save()
        assert _user_has_active_subscription(eleve_stripe) is False


# ============================================================
# Batch — Beta-test system
# ============================================================


@pytest.fixture
def eleve_beta(db):
    return CustomUser.objects.create_user(
        email="beta@test.com",
        password="TestPass123!",
        prenom="Bêta",
        nom="Testeur",
        role="eleve",
        niveau="terminale",
        is_beta=True,
    )


@pytest.fixture
def matiere_beta(db):
    return Matiere.objects.create(nom="chimie")


@pytest.fixture
def chapitre_beta(db, matiere_beta):
    return Chapitre.objects.create(
        matiere=matiere_beta,
        niveau="terminale",
        ordre=1,
        titre="Chapitre Bêta",
        description="Chapitre pour tests bêta",
    )


@pytest.fixture
def lecon_premium_beta(db, chapitre_beta):
    return Lecon.objects.create(
        chapitre=chapitre_beta,
        ordre=1,
        titre="Leçon Premium Bêta",
        contenu="# Premium\n\nContenu premium pour bêta.",
        duree_estimee=25,
        gratuit=False,
    )


class TestCustomUserIsBeta:
    """Tests pour le champ is_beta et la property is_beta_testeur."""

    @pytest.mark.django_db
    def test_is_beta_default_false(self):
        """
        Teste: Le champ is_beta est False par défaut à la création d'un utilisateur
        Raison: Un nouvel utilisateur ne doit pas être bêta-testeur sauf action explicite
        Features: Beta, Modèle utilisateur
        Criticité: moyenne
        """
        user = CustomUser.objects.create_user(
            email="default_beta@test.com",
            password="TestPass123!",
            prenom="Test",
            nom="Default",
            role="eleve",
            niveau="seconde",
        )
        assert user.is_beta is False

    @pytest.mark.django_db
    def test_is_beta_testeur_property_true(self, eleve_beta):
        """
        Teste: La property is_beta_testeur retourne True pour un utilisateur bêta
        Raison: Cette property est utilisée dans les templates pour afficher le badge bêta
        Features: Beta, Modèle utilisateur
        Criticité: moyenne
        """
        assert eleve_beta.is_beta_testeur is True

    @pytest.mark.django_db
    def test_is_beta_testeur_property_false(self, eleve):
        """
        Teste: La property is_beta_testeur retourne False pour un utilisateur normal
        Raison: Un utilisateur standard ne doit pas être identifié comme bêta-testeur
        Features: Beta, Modèle utilisateur
        Criticité: moyenne
        """
        assert eleve.is_beta_testeur is False


class TestUserHasActiveSubscriptionBeta:
    """Tests pour _user_has_active_subscription avec le flag bêta."""

    @pytest.mark.django_db
    def test_beta_user_without_subscription_returns_true(self, eleve_beta):
        """
        Teste: Un bêta-testeur sans abonnement Stripe a accès au contenu premium
        Raison: Le flag bêta doit court-circuiter la vérification Stripe
        Features: Beta, Accès premium, Abonnement
        Criticité: haute
        """
        from users.views import _user_has_active_subscription

        assert _user_has_active_subscription(eleve_beta) is True

    @pytest.mark.django_db
    def test_non_beta_user_without_subscription_returns_false(self, eleve):
        """
        Teste: Un utilisateur non-bêta sans abonnement n'a pas accès au contenu premium
        Raison: Vérifier que le flag bêta n'affecte pas les utilisateurs normaux
        Features: Beta, Accès premium, Abonnement
        Criticité: haute
        """
        from users.views import _user_has_active_subscription

        assert _user_has_active_subscription(eleve) is False

    @pytest.mark.django_db
    def test_beta_user_with_active_subscription_returns_true(self, eleve_beta):
        """
        Teste: Un bêta-testeur avec un abonnement actif retourne True
        Raison: Les deux conditions (bêta + abonnement) ne doivent pas interférer
        Features: Beta, Abonnement, Accès premium
        Criticité: haute
        """
        from users.views import _user_has_active_subscription
        from django.utils import timezone

        Abonnement.objects.create(
            user=eleve_beta,
            stripe_customer_id="cus_beta123",
            stripe_subscription_id="sub_beta123",
            plan="mensuel",
            statut="actif",
            date_debut=timezone.now(),
        )
        assert _user_has_active_subscription(eleve_beta) is True


class TestBetaPremiumAccess:
    """Tests d'accès au contenu premium pour les bêta-testeurs."""

    @pytest.mark.django_db
    def test_beta_eleve_accesses_premium_lecon(
        self, client, eleve_beta, chapitre_beta, lecon_premium_beta
    ):
        """
        Teste: Un bêta-testeur accède à une leçon premium via la vue interne
        Raison: Le contenu premium doit être accessible aux bêta-testeurs pour validation
        Features: Beta, Accès premium, Leçon
        Criticité: haute
        """
        from progress.models import ChapitreDebloque

        ChapitreDebloque.objects.create(user=eleve_beta, chapitre=chapitre_beta)
        client.force_login(eleve_beta)
        url = reverse("lecon", kwargs={"lecon_pk": lecon_premium_beta.pk})
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_non_beta_eleve_redirected_from_premium_lecon(
        self, client, eleve, matiere_beta, chapitre_beta, lecon_premium_beta
    ):
        """
        Teste: Un élève non-bêta est redirigé vers la vue publique pour une leçon premium
        Raison: Sans abonnement ni flag bêta, l'accès direct au contenu premium est interdit
        Features: Beta, Accès premium, Paywall, Redirection
        Criticité: haute
        """
        from progress.models import ChapitreDebloque

        # eleve fixture has niveau=terminale, matching chapitre_beta
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre_beta)
        client.force_login(eleve)
        url = reverse("lecon", kwargs={"lecon_pk": lecon_premium_beta.pk})
        response = client.get(url)
        assert response.status_code == 302
        expected_url = reverse(
            "lecon_publique",
            kwargs={
                "matiere_slug": matiere_beta.slug,
                "niveau": chapitre_beta.niveau,
                "chapitre_slug": chapitre_beta.slug,
                "lecon_slug": lecon_premium_beta.slug,
            },
        )
        assert response["Location"] == expected_url


class TestCreateBetaAccountsCommand:
    """Tests pour la commande create_beta_accounts."""

    @pytest.mark.django_db
    def test_creates_beta_user(self):
        """
        Teste: La commande crée un compte bêta-testeur avec les bons attributs
        Raison: Vérifier le chemin nominal de la création de comptes bêta en batch
        Features: Beta, Commande management, Création compte
        Criticité: moyenne
        """
        from django.core.management import call_command
        from io import StringIO

        out = StringIO()
        call_command(
            "create_beta_accounts",
            "newbeta@test.com:seconde",
            stdout=out,
        )
        user = CustomUser.objects.get(email="newbeta@test.com")
        assert user.is_beta is True
        assert user.role == "eleve"
        assert user.is_active is True
        assert user.niveau == "seconde"

    @pytest.mark.django_db
    def test_existing_email_sets_is_beta(self):
        """
        Teste: La commande active le flag bêta sur un compte existant
        Raison: Un utilisateur existant doit pouvoir devenir bêta-testeur sans recréer son compte
        Features: Beta, Commande management
        Criticité: moyenne
        """
        from django.core.management import call_command
        from io import StringIO

        user = CustomUser.objects.create_user(
            email="existing@test.com",
            password="TestPass123!",
            prenom="Exist",
            nom="User",
            role="eleve",
            niveau="premiere",
        )
        assert user.is_beta is False

        out = StringIO()
        call_command(
            "create_beta_accounts",
            "existing@test.com:premiere",
            stdout=out,
        )
        user.refresh_from_db()
        assert user.is_beta is True

    @pytest.mark.django_db
    def test_dry_run_does_not_create_user(self):
        """
        Teste: Le mode dry-run ne crée aucun compte en base
        Raison: Le dry-run doit permettre de prévisualiser sans effet de bord
        Features: Beta, Commande management, Dry-run
        Criticité: moyenne
        """
        from django.core.management import call_command
        from io import StringIO

        out = StringIO()
        call_command(
            "create_beta_accounts",
            "dryrun@test.com:terminale",
            "--dry-run",
            stdout=out,
        )
        assert not CustomUser.objects.filter(email="dryrun@test.com").exists()


class TestAdminBetaBadge:
    """Tests pour le badge Bêta dans les pages admin."""

    @pytest.mark.django_db
    def test_admin_utilisateurs_shows_beta_badge(self, client, admin_user, eleve_beta):
        """
        Teste: La liste admin affiche le badge Beta pour un bêta-testeur
        Raison: L'admin doit identifier visuellement les bêta-testeurs dans la liste
        Features: Beta, Admin utilisateurs, Badge UI
        Criticité: basse
        """
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 200
        assert "Beta" in response.content.decode()

    @pytest.mark.django_db
    def test_admin_eleve_detail_shows_beta_badge(self, client, admin_user, eleve_beta):
        """
        Teste: La page détail admin affiche le label Bêta-testeur
        Raison: L'admin doit voir le statut bêta sur la fiche individuelle de l'élève
        Features: Beta, Admin détail élève, Badge UI
        Criticité: basse
        """
        client.force_login(admin_user)
        url = reverse("admin_eleve_detail", kwargs={"user_id": eleve_beta.pk})
        response = client.get(url)
        assert response.status_code == 200
        assert "Bêta-testeur" in response.content.decode()


# ============================================================
# Batch 8 — Preview Paywall Mode
# ============================================================


class TestPreviewPaywallMode:
    """Tests for preview_paywall_view and exit_preview_paywall_view."""

    @pytest.mark.django_db
    def test_admin_active_preview_paywall(self, client, admin_user):
        """
        Teste: Un admin active le mode preview paywall → session["preview_paywall"] = True + redirect
        Raison: Vérifier que le mode preview paywall stocke la clé en session et redirige vers le dashboard
        Features: Preview paywall, Session, Permissions
        Criticité: haute
        """
        client.force_login(admin_user)
        response = client.get(reverse("preview_paywall"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url
        assert client.session.get("preview_paywall") is True

    @pytest.mark.django_db
    def test_eleve_cannot_activate_preview_paywall(self, client, eleve):
        """
        Teste: Un élève ne peut pas activer le mode preview paywall
        Raison: Le mode preview paywall est réservé aux admins — un élève ne doit pas pouvoir contourner le paywall
        Features: Preview paywall, Permissions
        Criticité: haute
        """
        client.force_login(eleve)
        response = client.get(reverse("preview_paywall"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url
        assert client.session.get("preview_paywall") is None

    @pytest.mark.django_db
    def test_anonymous_cannot_activate_preview_paywall(self, client):
        """
        Teste: Un utilisateur non authentifié est redirigé vers la connexion
        Raison: Les vues @login_required doivent empêcher l'accès anonyme
        Features: Preview paywall, Authentification
        Criticité: haute
        """
        response = client.get(reverse("preview_paywall"))
        assert response.status_code == 302
        assert "connexion" in response.url

    @pytest.mark.django_db
    def test_exit_preview_paywall_clears_session(self, client, admin_user):
        """
        Teste: La sortie du mode preview paywall supprime la clé de session
        Raison: Un résidu de session forcerait l'admin à voir le paywall indéfiniment
        Features: Preview paywall, Session
        Criticité: moyenne
        """
        client.force_login(admin_user)
        session = client.session
        session["preview_paywall"] = True
        session.save()
        response = client.get(reverse("exit_preview_paywall"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url
        assert "preview_paywall" not in client.session

    @pytest.mark.django_db
    def test_exit_preview_paywall_without_active_session(self, client, admin_user):
        """
        Teste: Quitter le mode preview paywall sans session active ne crash pas
        Raison: L'admin peut cliquer sur «quitter» même si le mode n'est plus actif — robustesse
        Features: Preview paywall, Robustesse
        Criticité: basse
        """
        client.force_login(admin_user)
        response = client.get(reverse("exit_preview_paywall"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_anonymous_cannot_exit_preview_paywall(self, client):
        """
        Teste: Un utilisateur non authentifié est redirigé vers la connexion sur exit
        Raison: Les vues @login_required doivent empêcher l'accès anonyme
        Features: Preview paywall, Authentification
        Criticité: haute
        """
        response = client.get(reverse("exit_preview_paywall"))
        assert response.status_code == 302
        assert "connexion" in response.url


