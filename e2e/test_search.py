"""
Tests E2E — Recherche.
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
from playwright.sync_api import Page, expect


class TestSearch:
    """Tests de la fonctionnalité de recherche plein-texte."""

    def test_search_page_loads(self, admin_page: Page, base_url):
        """
        Teste : La page /cours/recherche/ se charge avec un champ de recherche visible.
        Criticité : haute
        """
        response = admin_page.goto(f"{base_url}/cours/recherche/")
        assert response.status == 200
        # Le champ de recherche doit être visible
        search_input = admin_page.locator("input[name='q'][autofocus]")
        expect(search_input).to_be_visible()
        # Le bouton "Rechercher" doit être visible
        expect(admin_page.locator("button:has-text('Rechercher')")).to_be_visible()

    def test_search_returns_results(self, admin_page: Page, base_url):
        """
        Teste : Une recherche avec un mot pertinent retourne des résultats.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/cours/recherche/")
        admin_page.wait_for_load_state("networkidle")
        # Chercher un terme courant dans les leçons de sciences
        admin_page.fill("input[name='q'][autofocus]", "mouvement")
        admin_page.click("button:has-text('Rechercher')")
        admin_page.wait_for_load_state("networkidle")
        # Vérifier qu'il y a au moins un résultat (lien vers une leçon)
        result_text = admin_page.locator("body").inner_text()
        # Soit on a "X résultat(s)" soit on a des liens de résultats
        has_results = "résultat" in result_text and "Aucun résultat" not in result_text
        has_links = admin_page.locator("a[href*='/cours/lecon/']").count() > 0
        assert has_results or has_links, \
            "Aucun résultat trouvé pour la recherche 'mouvement'"

    def test_search_short_query_no_results(self, admin_page: Page, base_url):
        """
        Teste : Une recherche avec 1 seul caractère ne retourne pas de résultats.
        Criticité : moyenne
        """
        admin_page.goto(f"{base_url}/cours/recherche/")
        admin_page.wait_for_load_state("networkidle")
        # Taper un seul caractère
        admin_page.fill("input[name='q']", "x")
        admin_page.click("button:has-text('Rechercher')")
        admin_page.wait_for_load_state("networkidle")
        # Pas de résultats : soit "Aucun résultat" soit absence de liens
        no_result_msg = admin_page.locator("text=Aucun résultat")
        result_links = admin_page.locator("a[href*='/cours/lecon/']")
        has_no_results = no_result_msg.is_visible() or result_links.count() == 0
        assert has_no_results, \
            "Des résultats ont été trouvés pour une recherche d'un seul caractère"
