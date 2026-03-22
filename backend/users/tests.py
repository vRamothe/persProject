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
        response = client.get(reverse("connexion"))
        assert response.status_code == 200

    def test_inscription_page_accessible_anonymous(self, client):
        response = client.get(reverse("inscription"))
        assert response.status_code == 200

    def test_dashboard_redirects_anonymous_to_login(self, client):
        response = client.get(reverse("tableau_de_bord"))
        assert response.status_code == 302
        assert "connexion" in response.url

    def test_profil_requires_login(self, client):
        response = client.get(reverse("profil"))
        assert response.status_code == 302
        assert "connexion" in response.url

    def test_admin_panel_forbidden_for_eleve(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("admin_utilisateurs"))
        # Non-admin gets redirected to dashboard
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    def test_admin_panel_accessible_for_admin(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 200


class TestInscription:
    def test_inscription_creates_eleve(self, client, db):
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
        response = client.get(reverse("verifier_email", kwargs={"token": "completely-invalid"}))
        assert response.status_code == 400

    def test_inscription_confirmation_page_accessible(self, client):
        response = client.get(reverse("inscription_confirmation"))
        assert response.status_code == 200


class TestPasswordReset:
    def test_password_reset_page_accessible(self, client):
        response = client.get(reverse("password_reset"))
        assert response.status_code == 200

    def test_password_reset_done_page_accessible(self, client):
        response = client.get(reverse("password_reset_done"))
        assert response.status_code == 200

    def test_password_reset_complete_page_accessible(self, client):
        response = client.get(reverse("password_reset_complete"))
        assert response.status_code == 200


class TestAdminAnalytics:
    def test_anonymous_redirected(self, client):
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 302

    def test_eleve_redirected_to_dashboard(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 302

    def test_admin_gets_200(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 200

    def test_weak_questions_in_context(self, client, admin_user, db):
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
        client.force_login(admin_user)
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 200


class TestHealthCheck:
    def test_health_returns_200(self, client):
        response = client.get(reverse("health"))
        assert response.status_code == 200

    def test_health_content_type_json(self, client):
        response = client.get(reverse("health"))
        assert "application/json" in response["Content-Type"]

    def test_health_body(self, client):
        import json
        response = client.get(reverse("health"))
        data = json.loads(response.content)
        assert data == {"status": "ok"}

