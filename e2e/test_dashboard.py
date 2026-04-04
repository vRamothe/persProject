"""
Tests E2E — Dashboards (admin et élève).
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
from playwright.sync_api import Page, expect


class TestAdminDashboard:
    """Tests du tableau de bord administrateur."""

    def test_admin_dashboard_has_stats_cards(self, admin_page: Page, base_url):
        """
        Teste : Le dashboard admin affiche les cartes stats (Élèves, Chapitres, Leçons).
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/tableau-de-bord/")
        expect(admin_page.locator("text=Élèves actifs").first).to_be_visible()
        expect(admin_page.locator("text=Chapitres").first).to_be_visible()
        expect(admin_page.locator("text=Leçons").first).to_be_visible()

    def test_admin_dashboard_has_derniers_inscrits(self, admin_page: Page, base_url):
        """
        Teste : La section "Derniers inscrits" est visible sur le dashboard admin.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/tableau-de-bord/")
        expect(admin_page.locator("text=Derniers inscrits").first).to_be_visible()

    def test_admin_dashboard_has_preview_cards(self, admin_page: Page, base_url):
        """
        Teste : Les cartes de prévisualisation niveau et paywall sont présentes.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/tableau-de-bord/")
        expect(admin_page.locator("text=Simuler la vue élève").first).to_be_visible()
        expect(admin_page.locator("text=Prévisualiser le paywall").first).to_be_visible()

    def test_admin_can_access_analytics(self, admin_page: Page, base_url):
        """
        Teste : L'admin peut accéder à la page analytics via le lien sidebar.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/tableau-de-bord/")
        admin_page.locator("a[href='/admin-panel/analytics/']").first.click()
        admin_page.wait_for_load_state("networkidle")
        expect(admin_page).to_have_url(f"{base_url}/admin-panel/analytics/")
        expect(admin_page.get_by_role("heading", name="Analytics plateforme")).to_be_visible()

    def test_admin_can_access_user_list(self, admin_page: Page, base_url):
        """
        Teste : L'admin peut accéder à la liste des utilisateurs.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/tableau-de-bord/")
        admin_page.locator("a[href='/admin-panel/utilisateurs/']").first.click()
        admin_page.wait_for_load_state("networkidle")
        expect(admin_page).to_have_url(f"{base_url}/admin-panel/utilisateurs/")
