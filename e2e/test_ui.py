"""
Tests E2E — UI transversale (dark mode, KaTeX, responsive).
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
import re
from playwright.sync_api import Page, expect


class TestDarkMode:
    """Tests du toggle dark mode et de la persistance du thème."""

    def _reset_theme_light(self, page: Page, base_url: str):
        """Remet le thème en light mode via localStorage puis recharge."""
        page.goto(f"{base_url}/")
        page.evaluate("localStorage.setItem('theme', 'light')")
        page.evaluate("document.documentElement.classList.remove('dark')")
        page.reload()
        page.wait_for_load_state("networkidle")

    def _get_toggle_button(self, page: Page):
        """Retourne le bouton toggle thème (sélection par @click Alpine.js)."""
        return page.locator("[\\@click='toggleTheme()']").first

    def test_dark_mode_toggle_adds_class(self, page: Page, base_url):
        """
        Teste : Cliquer le toggle sun/moon ajoute la classe 'dark' à <html>.
        Criticité : haute
        """
        self._reset_theme_light(page, base_url)
        # Vérifier état initial : pas de classe dark
        has_dark = page.evaluate("document.documentElement.classList.contains('dark')")
        assert not has_dark, "Le thème devrait être light après reset"
        # Cliquer le toggle
        self._get_toggle_button(page).click()
        # Vérifier que <html> a la classe dark
        has_dark = page.evaluate("document.documentElement.classList.contains('dark')")
        assert has_dark, "Après clic, <html> devrait avoir la classe 'dark'"

    def test_dark_mode_persists_on_reload(self, page: Page, base_url):
        """
        Teste : Activer dark mode puis recharger → <html> a toujours la classe 'dark'.
        Criticité : haute
        """
        self._reset_theme_light(page, base_url)
        # Activer dark mode
        self._get_toggle_button(page).click()
        has_dark = page.evaluate("document.documentElement.classList.contains('dark')")
        assert has_dark
        # Recharger la page
        page.reload()
        page.wait_for_load_state("networkidle")
        # Vérifier la persistance
        has_dark_after = page.evaluate("document.documentElement.classList.contains('dark')")
        assert has_dark_after, "Le dark mode devrait persister après rechargement"

    def test_dark_mode_toggle_removes_class(self, page: Page, base_url):
        """
        Teste : Cliquer 2 fois → <html> n'a plus la classe 'dark'.
        Criticité : haute
        """
        self._reset_theme_light(page, base_url)
        toggle = self._get_toggle_button(page)
        # Premier clic → dark
        toggle.click()
        has_dark = page.evaluate("document.documentElement.classList.contains('dark')")
        assert has_dark
        # Deuxième clic → light
        toggle.click()
        has_dark = page.evaluate("document.documentElement.classList.contains('dark')")
        assert not has_dark, "Après 2 clics, <html> ne devrait plus avoir la classe 'dark'"


class TestKatexRendering:
    """Tests du rendu KaTeX dans les leçons."""

    def test_lecon_with_latex_renders_katex(self, admin_page: Page, base_url):
        """
        Teste : En tant qu'admin, une leçon contenant des formules génère des éléments .katex.
        Criticité : haute
        """
        # Naviguer vers /cours/ → premier chapitre → première leçon
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")
        # Déplier les matières (accordéons Alpine.js)
        count = admin_page.locator("button:has-text('Voir les cours')").count()
        for _ in range(count):
            admin_page.locator("button:has-text('Voir les cours')").first.click()
            admin_page.wait_for_timeout(300)
        # Déplier les niveaux (admin 3-level accordion)
        niveau_buttons = admin_page.locator("button:has-text('chapitre')")
        for i in range(niveau_buttons.count()):
            niveau_buttons.nth(i).click()
            admin_page.wait_for_timeout(200)
        admin_page.locator("a[href*='/cours/chapitre/']").first.click()
        admin_page.wait_for_load_state("networkidle")
        admin_page.locator("a[href*='/cours/lecon/']").first.click()
        admin_page.wait_for_load_state("networkidle")
        # L'URL doit correspondre à une leçon
        expect(admin_page).to_have_url(re.compile(r"/cours/lecon/\d+/"))
        # Attendre que KaTeX ait rendu (auto-render peut prendre un instant)
        admin_page.wait_for_timeout(1000)
        katex_elements = admin_page.locator(".katex")
        assert katex_elements.count() > 0, \
            "Aucun élément .katex trouvé — la leçon ne contient peut-être pas de formules LaTeX"
