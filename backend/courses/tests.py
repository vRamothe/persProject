import pytest
from django.test import Client
from django.urls import reverse
from courses.models import Matiere, Chapitre, Lecon, Quiz, Question
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
def matiere(db):
    return Matiere.objects.create(nom="mathematiques", description="Maths")


@pytest.fixture
def chapitre(matiere):
    return Chapitre.objects.create(
        matiere=matiere,
        niveau="terminale",
        titre="Les Suites Numériques",
        ordre=1,
    )


@pytest.fixture
def lecon_gratuite(chapitre):
    return Lecon.objects.create(
        chapitre=chapitre,
        titre="Définition et premiers exemples",
        contenu="# Introduction\nContenu de la leçon.",
        ordre=1,
        gratuit=True,
    )


@pytest.fixture
def lecon_payante(chapitre):
    return Lecon.objects.create(
        chapitre=chapitre,
        titre="Suites arithmétiques",
        contenu="# Suites arithmétiques\nContenu payant.",
        ordre=2,
        gratuit=False,
    )


class TestSlugGeneration:
    def test_matiere_slug_auto_generated(self, matiere):
        assert matiere.slug == "mathematiques"

    def test_chapitre_slug_auto_generated(self, chapitre):
        assert chapitre.slug == "les-suites-numeriques"

    def test_lecon_slug_auto_generated(self, lecon_gratuite):
        assert lecon_gratuite.slug == "definition-et-premiers-exemples"

    def test_slug_unique_within_scope(self, chapitre):
        """Two lessons in the same chapter cannot have the same slug."""
        Lecon.objects.create(
            chapitre=chapitre,
            titre="Test unique",
            contenu="Test",
            ordre=10,
        )
        # A different chapitre can have the same slug
        matiere2 = Matiere.objects.create(nom="physique")
        chapitre2 = Chapitre.objects.create(
            matiere=matiere2, niveau="terminale", titre="Autre chapitre", ordre=1,
        )
        lecon2 = Lecon.objects.create(
            chapitre=chapitre2,
            titre="Test unique",
            contenu="Test",
            ordre=1,
        )
        assert lecon2.slug == "test-unique"


class TestPublicPages:
    def test_catalogue_accessible_anonymous(self, client, matiere):
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": "mathematiques"})
        )
        assert response.status_code == 200

    def test_free_lesson_accessible_anonymous(self, client, lecon_gratuite):
        chapitre = lecon_gratuite.chapitre
        response = client.get(
            reverse("lecon_publique", kwargs={
                "matiere_slug": chapitre.matiere.slug,
                "niveau": chapitre.niveau,
                "chapitre_slug": chapitre.slug,
                "lecon_slug": lecon_gratuite.slug,
            })
        )
        assert response.status_code == 200

    def test_non_free_lesson_redirects_to_login(self, client, lecon_payante):
        chapitre = lecon_payante.chapitre
        response = client.get(
            reverse("lecon_publique", kwargs={
                "matiere_slug": chapitre.matiere.slug,
                "niveau": chapitre.niveau,
                "chapitre_slug": chapitre.slug,
                "lecon_slug": lecon_payante.slug,
            })
        )
        assert response.status_code == 302
        assert "connexion" in response.url

    def test_authenticated_user_redirected_to_pk_view(self, client, eleve, lecon_gratuite):
        client.login(email="eleve@test.com", password="TestPass123!")
        chapitre = lecon_gratuite.chapitre
        response = client.get(
            reverse("lecon_publique", kwargs={
                "matiere_slug": chapitre.matiere.slug,
                "niveau": chapitre.niveau,
                "chapitre_slug": chapitre.slug,
                "lecon_slug": lecon_gratuite.slug,
            })
        )
        assert response.status_code == 302
        assert f"/cours/lecon/{lecon_gratuite.pk}/" in response.url
