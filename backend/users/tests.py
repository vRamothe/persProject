import pytest
from django.test import Client
from django.urls import reverse
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
        client.login(email="eleve@test.com", password="TestPass123!")
        response = client.get(reverse("admin_utilisateurs"))
        # Non-admin gets redirected to dashboard
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    def test_admin_panel_accessible_for_admin(self, client, admin_user):
        client.login(email="admin@test.com", password="AdminPass123!")
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
