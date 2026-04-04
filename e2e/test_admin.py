"""
Tests E2E — Admin panel (gestion élèves, analytics, preview niveau).
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
from playwright.sync_api import Page, expect


class TestAdminUserManagement:
    """Tests de la page de gestion des utilisateurs."""

    def test_user_list_loads(self, admin_page: Page, base_url):
        """
        Teste : /admin-panel/utilisateurs/ affiche la liste des élèves.
        Criticité : haute
        """
        response = admin_page.goto(f"{base_url}/admin-panel/utilisateurs/")
        assert response.status == 200
        admin_page.wait_for_load_state("networkidle")
        # Le heading "Utilisateurs" doit être visible
        expect(admin_page.get_by_role("heading", name="Utilisateurs")).to_be_visible()

    def test_user_list_has_search(self, admin_page: Page, base_url):
        """
        Teste : Le champ de recherche est visible sur la page utilisateurs.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/admin-panel/utilisateurs/")
        admin_page.wait_for_load_state("networkidle")
        search_input = admin_page.locator("input[name='q']").first
        expect(search_input).to_be_visible()

    def test_user_list_has_filters(self, admin_page: Page, base_url):
        """
        Teste : Les filtres niveau et statut actif sont visibles.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/admin-panel/utilisateurs/")
        admin_page.wait_for_load_state("networkidle")
        # Filtre niveau
        niveau_select = admin_page.locator("select[name='niveau']")
        expect(niveau_select).to_be_visible()
        # Filtre statut actif
        actif_select = admin_page.locator("select[name='actif']")
        expect(actif_select).to_be_visible()


class TestAdminPreviewNiveau:
    """Tests de l'activation/désactivation du preview niveau."""

    def test_activate_preview_seconde(self, admin_page: Page, base_url):
        """
        Teste : Activer le preview Seconde → bannière jaune "Mode prévisualisation" visible.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/admin-panel/preview/seconde/")
        admin_page.wait_for_load_state("networkidle")
        # La bannière "Mode prévisualisation" doit être visible
        banner = admin_page.locator("text=Mode prévisualisation")
        expect(banner.first).to_be_visible()
        # Elle doit mentionner "Seconde"
        expect(admin_page.locator("text=Seconde").first).to_be_visible()

    def test_exit_preview(self, admin_page: Page, base_url):
        """
        Teste : Quitter le preview → la bannière disparaît.
        Criticité : haute
        """
        # Activer le preview
        admin_page.goto(f"{base_url}/admin-panel/preview/seconde/")
        admin_page.wait_for_load_state("networkidle")
        banner = admin_page.locator("text=Mode prévisualisation")
        expect(banner.first).to_be_visible()
        # Quitter
        admin_page.locator("a:has-text('Quitter')").first.click()
        admin_page.wait_for_load_state("networkidle")
        # La bannière ne doit plus être visible
        banner = admin_page.locator("text=Mode prévisualisation —")
        expect(banner).not_to_be_visible()


class TestAdminAnalytics:
    """Tests de la page analytics admin."""

    def test_analytics_page_loads(self, admin_page: Page, base_url):
        """
        Teste : /admin-panel/analytics/ se charge et affiche la section analytics.
        Criticité : haute
        """
        response = admin_page.goto(f"{base_url}/admin-panel/analytics/")
        assert response.status == 200
        admin_page.wait_for_load_state("networkidle")
        expect(admin_page.get_by_role("heading", name="Analytics plateforme")).to_be_visible()
