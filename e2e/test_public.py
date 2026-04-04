"""
Tests E2E — Pages publiques (catalogue, leçons publiques, accueil).
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
from playwright.sync_api import Page, expect


class TestCataloguePublic:
    """Tests du catalogue public (pages matières)."""

    def test_catalogue_accessible_anonymous(self, page: Page, base_url):
        """
        Teste : /cours/physique/ est accessible sans authentification, chapitres visibles.
        Criticité : critique
        """
        response = page.goto(f"{base_url}/cours/physique/")
        assert response.status == 200
        page.wait_for_load_state("networkidle")
        # Au moins un chapitre doit être visible (bouton accordion)
        chapitres = page.locator("h3:has-text('Ch.')")
        expect(chapitres.first).to_be_visible()

    def test_catalogue_shows_premium_badge(self, page: Page, base_url):
        """
        Teste : Les leçons premium affichent un badge "Premium".
        Criticité : haute
        """
        page.goto(f"{base_url}/cours/physique/")
        page.wait_for_load_state("networkidle")
        # Ouvrir le premier chapitre (accordion Alpine.js)
        page.locator("button:has-text('Ch.')").first.click()
        # Attendre que la liste de leçons apparaisse
        page.wait_for_timeout(300)
        # Badge Premium visible
        premium_badge = page.locator("text=Premium")
        expect(premium_badge.first).to_be_visible()

    def test_catalogue_shows_gratuit_badge(self, page: Page, base_url):
        """
        Teste : Les leçons gratuites affichent un badge "Gratuit".
        Criticité : haute
        """
        page.goto(f"{base_url}/cours/physique/")
        page.wait_for_load_state("networkidle")
        # Ouvrir tous les chapitres pour trouver une leçon gratuite
        chapter_buttons = page.locator("button:has-text('Ch.')")
        count = chapter_buttons.count()
        for i in range(count):
            chapter_buttons.nth(i).click()
            page.wait_for_timeout(200)
        # Badge Gratuit visible
        gratuit_badge = page.locator("text=Gratuit")
        expect(gratuit_badge.first).to_be_visible()


class TestLeconPublique:
    """Tests des leçons publiques (vue slug, blur/paywall)."""

    def test_free_lesson_shows_full_content(self, page: Page, base_url):
        """
        Teste : Une leçon gratuite affiche le contenu complet, sans blur.
        Criticité : critique
        """
        page.goto(f"{base_url}/cours/physique/")
        page.wait_for_load_state("networkidle")
        # Ouvrir les chapitres et trouver un lien "Gratuit"
        chapter_buttons = page.locator("button:has-text('Ch.')")
        count = chapter_buttons.count()
        for i in range(count):
            chapter_buttons.nth(i).click()
            page.wait_for_timeout(200)
        # Cliquer sur la première leçon gratuite (le lien précède le badge "Gratuit")
        gratuit_badges = page.locator("span:has-text('Gratuit')")
        assert gratuit_badges.count() > 0, "Aucune leçon gratuite trouvée dans le catalogue physique"
        # Le lien de la leçon est le <a> frère du badge dans le même <div>
        first_gratuit_row = gratuit_badges.first.locator("xpath=ancestor::div[contains(@class, 'px-5')]")
        lesson_link = first_gratuit_row.locator("a").first
        lesson_link.click()
        page.wait_for_load_state("networkidle")
        # Pas de blur visible
        blur = page.locator(".paywall-blur-container")
        expect(blur).not_to_be_visible()
        # Contenu prose visible
        prose = page.locator(".prose")
        expect(prose.first).to_be_visible()

    def test_premium_lesson_shows_blur_anonymous(self, page: Page, base_url):
        """
        Teste : Une leçon premium vue par un anonyme affiche le blur (.paywall-blur-container).
        Criticité : critique
        """
        page.goto(f"{base_url}/cours/physique/")
        page.wait_for_load_state("networkidle")
        # Ouvrir les chapitres et trouver un lien Premium
        chapter_buttons = page.locator("button:has-text('Ch.')")
        count = chapter_buttons.count()
        for i in range(count):
            chapter_buttons.nth(i).click()
            page.wait_for_timeout(200)
        # Cliquer sur la première leçon Premium
        premium_badges = page.locator("span:has-text('Premium')")
        assert premium_badges.count() > 0, "Aucune leçon premium trouvée dans le catalogue physique"
        first_premium_row = premium_badges.first.locator("xpath=ancestor::div[contains(@class, 'px-5')]")
        lesson_link = first_premium_row.locator("a").first
        lesson_link.click()
        page.wait_for_load_state("networkidle")
        # Le conteneur blur doit être visible
        blur = page.locator(".paywall-blur-container")
        expect(blur).to_be_visible()

    def test_premium_lesson_has_paywall_modal(self, page: Page, base_url):
        """
        Teste : Une leçon premium a un bouton "Débloquer" qui ouvre le modal paywall.
        Criticité : haute
        """
        page.goto(f"{base_url}/cours/physique/")
        page.wait_for_load_state("networkidle")
        # Ouvrir les chapitres
        chapter_buttons = page.locator("button:has-text('Ch.')")
        count = chapter_buttons.count()
        for i in range(count):
            chapter_buttons.nth(i).click()
            page.wait_for_timeout(200)
        # Cliquer sur la première leçon Premium
        premium_badges = page.locator("span:has-text('Premium')")
        assert premium_badges.count() > 0, "Aucune leçon premium trouvée"
        first_premium_row = premium_badges.first.locator("xpath=ancestor::div[contains(@class, 'px-5')]")
        first_premium_row.locator("a").first.click()
        page.wait_for_load_state("networkidle")
        # Cliquer sur "Débloquer cette leçon"
        debloquer_btn = page.locator("button:has-text('Débloquer cette leçon')").first
        expect(debloquer_btn).to_be_visible()
        debloquer_btn.click()
        # Le modal paywall doit apparaître (Alpine.js showPaywall=true)
        paywall_modal = page.locator("text=Débloquez tout ScienceLycée")
        expect(paywall_modal.first).to_be_visible(timeout=3000)
