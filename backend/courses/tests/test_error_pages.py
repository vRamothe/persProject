import pytest
from django.test import Client


@pytest.fixture
def client():
    return Client()


class TestCustomErrorPages:
    @pytest.mark.django_db
    def test_404_returns_custom_page(self, client):
        """
        Teste: une URL inexistante retourne 404 avec le template personnalisé
        Raison: le handler 404 personnalisé doit retourner le bon code et un message utile
        Features: page 404, handler personnalisé, gestion erreurs
        Criticité: moyenne
        """
        response = client.get("/url-qui-nexiste-vraiment-pas-12345/")
        assert response.status_code == 404
        content = response.content.decode()
        assert "404" in content or "introuvable" in content
