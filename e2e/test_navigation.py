"""
Tests E2E — Navigation dans les cours (matières, chapitres, leçons).
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
import re
from playwright.sync_api import Page, expect


class TestCourseNavigation:
    """Tests de navigation dans l'arborescence des cours."""

    @staticmethod
    def _expand_matieres(page):
        """Déplie les accordéons matières + niveaux sur /cours/ (admin 3-level accordion)."""
        # 1. Expand matières ("Voir les cours" → "Masquer les cours")
        count = page.locator("button:has-text('Voir les cours')").count()
        for _ in range(count):
            page.locator("button:has-text('Voir les cours')").first.click()
            page.wait_for_timeout(300)
        # 2. Expand niveaux (admin sees Seconde/Première/Terminale grouping)
        #    Niveau buttons contain "chapitre" text (e.g., "5 chapitres")
        niveau_buttons = page.locator("button:has-text('chapitre')")
        nb = niveau_buttons.count()
        for i in range(nb):
            niveau_buttons.nth(i).click()
            page.wait_for_timeout(200)

    def test_matieres_page_loads(self, admin_page: Page, base_url):
        """
        Teste : La page /cours/ affiche les trois matières.
        Criticité : critique
        """
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")
        expect(admin_page.get_by_role("heading", name="Physique")).to_be_visible()
        expect(admin_page.get_by_role("heading", name="Chimie")).to_be_visible()
        expect(admin_page.get_by_role("heading", name="Mathématiques")).to_be_visible()

    def test_click_chapitre_loads_lecons(self, admin_page: Page, base_url):
        """
        Teste : Cliquer sur un chapitre mène à une page avec des liens vers les leçons.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")
        self._expand_matieres(admin_page)
        # Cliquer sur le premier lien chapitre
        chapitre_link = admin_page.locator("a[href*='/cours/chapitre/']").first
        expect(chapitre_link).to_be_visible()
        chapitre_link.click()
        admin_page.wait_for_load_state("networkidle")
        # L'URL doit correspondre à /cours/chapitre/<pk>/
        expect(admin_page).to_have_url(re.compile(r"/cours/chapitre/\d+/"))
        # Il doit y avoir au moins un lien vers une leçon
        lecon_links = admin_page.locator("a[href*='/cours/lecon/']")
        expect(lecon_links.first).to_be_visible()

    def test_click_lecon_shows_content(self, admin_page: Page, base_url):
        """
        Teste : Cliquer sur une leçon affiche du contenu Markdown rendu (pas de balises ## brutes).
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")
        self._expand_matieres(admin_page)
        # Naviguer : chapitre → leçon
        admin_page.locator("a[href*='/cours/chapitre/']").first.click()
        admin_page.wait_for_load_state("networkidle")
        admin_page.locator("a[href*='/cours/lecon/']").first.click()
        admin_page.wait_for_load_state("networkidle")
        expect(admin_page).to_have_url(re.compile(r"/cours/lecon/\d+/"))
        # Le contenu rendu est dans une div .prose
        prose = admin_page.locator(".prose")
        expect(prose).to_be_visible()
        # Vérifier qu'il n'y a pas de balises Markdown brutes (## en début de ligne)
        content_text = prose.inner_text()
        assert not re.search(r"^#{2,}\s", content_text, re.MULTILINE), \
            "Du Markdown brut (##) a été trouvé dans le contenu rendu"

    def test_lecon_has_quiz_link(self, admin_page: Page, base_url):
        """
        Teste : Une leçon avec quiz affiche un lien vers le quiz.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")
        self._expand_matieres(admin_page)
        # Naviguer vers un chapitre puis une leçon
        admin_page.locator("a[href*='/cours/chapitre/']").first.click()
        admin_page.wait_for_load_state("networkidle")
        admin_page.locator("a[href*='/cours/lecon/']").first.click()
        admin_page.wait_for_load_state("networkidle")
        # Le lien quiz est soit "Passer le quiz →" soit "Refaire le quiz"
        quiz_link = admin_page.locator("a[href*='/quiz/']")
        expect(quiz_link.first).to_be_visible()

    def test_lecon_navigation_buttons(self, admin_page: Page, base_url):
        """
        Teste : Les boutons de navigation précédent/suivant sont visibles selon la position.
        Criticité : moyenne
        """
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")
        self._expand_matieres(admin_page)
        # Naviguer vers un chapitre avec plusieurs leçons
        admin_page.locator("a[href*='/cours/chapitre/']").first.click()
        admin_page.wait_for_load_state("networkidle")
        # Compter les leçons disponibles
        lecon_links = admin_page.locator("a[href*='/cours/lecon/']")
        nb_lecons = lecon_links.count()

        if nb_lecons >= 2:
            # Aller sur la 2e leçon (qui n'est ni la première ni la dernière si >= 3,
            # ou qui est la dernière si == 2 → au moins le bouton précédent)
            lecon_links.nth(1).click()
            admin_page.wait_for_load_state("networkidle")
            # La 2e leçon doit avoir un lien "précédent" (lien avec flèche gauche ←)
            prev_link = admin_page.locator("a[href*='/cours/lecon/']").filter(
                has=admin_page.locator("svg")
            ).first
            expect(prev_link).to_be_visible()
        else:
            # S'il n'y a qu'une leçon, aller dessus et vérifier qu'il n'y a pas de nav
            lecon_links.first.click()
            admin_page.wait_for_load_state("networkidle")
            # Au minimum la page se charge sans erreur
            expect(admin_page).to_have_url(re.compile(r"/cours/lecon/\d+/"))
