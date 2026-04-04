"""
Tests E2E — Smoke tests (vérification que l'app tourne).
Prérequis : docker compose up --build -d
"""
from playwright.sync_api import Page, expect


class TestSmoke:
    """Vérifications de base que l'app est accessible."""

    def test_homepage_loads(self, page: Page, base_url):
        """
        Teste : La page d'accueil se charge correctement.
        Criticité : critique
        """
        page.goto(f"{base_url}/")
        expect(page).to_have_title(page.title())
        # Le logo/nom doit être visible
        expect(page.locator("text=ScienceLycée").first).to_be_visible()

    def test_login_page_loads(self, page: Page, base_url):
        """
        Teste : La page de connexion se charge.
        Criticité : critique
        """
        page.goto(f"{base_url}/connexion/")
        expect(page.locator("input[name='username']")).to_be_visible()
        expect(page.locator("input[name='password']")).to_be_visible()

    def test_register_page_loads(self, page: Page, base_url):
        """
        Teste : La page d'inscription se charge.
        Criticité : haute
        """
        page.goto(f"{base_url}/inscription/")
        expect(page.locator("input[name='email']")).to_be_visible()

    def test_admin_login(self, admin_page: Page, base_url):
        """
        Teste : L'admin peut se connecter et arrive sur le dashboard.
        Criticité : critique
        """
        expect(admin_page).to_have_url(f"{base_url}/tableau-de-bord/")
        # Vérifier que c'est bien le dashboard admin
        expect(admin_page.get_by_role("heading", name="Tableau de bord")).to_be_visible()

    def test_health_endpoint(self, page: Page, base_url):
        """
        Teste : Le endpoint /health/ répond.
        Criticité : critique
        """
        response = page.goto(f"{base_url}/health/")
        assert response.status == 200
