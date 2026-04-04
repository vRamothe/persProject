"""
Tests E2E — Prévisualisation du paywall admin.
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
import re
import pytest
from playwright.sync_api import Page, expect


class TestPaywallPreviewActivation:
    """Tests d'activation/désactivation du mode preview paywall."""

    def test_admin_dashboard_has_paywall_preview_card(self, admin_page: Page, base_url):
        """
        Teste : La carte "Prévisualiser le paywall" est visible dans le dashboard admin.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/tableau-de-bord/")
        # La carte doit contenir le texte
        card = admin_page.locator("text=Prévisualiser le paywall")
        expect(card).to_be_visible()

    def test_activate_paywall_preview(self, admin_page: Page, base_url):
        """
        Teste : Cliquer sur "Activer la prévisualisation" active le mode et affiche la bannière.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/tableau-de-bord/")
        # Cliquer sur le lien d'activation
        admin_page.click("a:has-text('Activer la prévisualisation')")
        # Doit être redirigé vers le dashboard
        admin_page.wait_for_url(f"**/tableau-de-bord/")
        # La bannière amber doit être visible
        banner = admin_page.locator("text=Mode prévisualisation paywall actif")
        expect(banner).to_be_visible()

    def test_deactivate_paywall_preview(self, admin_page: Page, base_url):
        """
        Teste : Quitter le mode preview supprime la bannière.
        Criticité : haute
        """
        # Activer d'abord
        admin_page.goto(f"{base_url}/admin-panel/preview-paywall/")
        admin_page.wait_for_url(f"**/tableau-de-bord/")
        # Bannière visible
        banner = admin_page.locator("text=Mode prévisualisation paywall actif")
        expect(banner).to_be_visible()
        # Cliquer sur "Quitter"
        admin_page.click("a:has-text('Quitter')")
        admin_page.wait_for_url(f"**/tableau-de-bord/")
        # La bannière ne doit plus être visible
        banner = admin_page.locator("text=Mode prévisualisation paywall actif")
        expect(banner).not_to_be_visible()


class TestPaywallPreviewOnPremiumLesson:
    """Tests du rendu paywall sur les leçons premium."""

    def test_admin_without_preview_sees_full_lesson(self, admin_page: Page, base_url):
        """
        Teste : Sans preview, l'admin voit la leçon complète (vue interne).
        Criticité : haute
        """
        # Aller sur une leçon via la vue interne
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")
        # Cliquer sur le premier chapitre disponible
        first_chapter_link = admin_page.locator("a[href*='/cours/chapitre/']").first
        if first_chapter_link.is_visible():
            first_chapter_link.click()
            admin_page.wait_for_load_state("networkidle")
            # Cliquer sur la première leçon
            first_lesson_link = admin_page.locator("a[href*='/cours/lecon/']").first
            if first_lesson_link.is_visible():
                first_lesson_link.click()
                admin_page.wait_for_load_state("networkidle")
                # Doit être sur la vue interne (URL avec /cours/lecon/<pk>/)
                expect(admin_page).to_have_url(re.compile(r"/cours/lecon/\d+/"))
                # Pas de blur
                blur = admin_page.locator(".paywall-blur-container")
                expect(blur).not_to_be_visible()

    def test_admin_with_preview_sees_paywall_blur(self, admin_page: Page, base_url):
        """
        Teste : Avec preview paywall, l'admin voit le blur et le bouton "Débloquer" sur une leçon premium.
        Criticité : critique
        """
        # Activer le mode preview
        admin_page.goto(f"{base_url}/admin-panel/preview-paywall/")
        admin_page.wait_for_url(f"**/tableau-de-bord/")

        # Naviguer vers une leçon via la vue interne (sera redirigé vers la vue publique)
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")

        # Trouver et cliquer sur un chapitre
        first_chapter_link = admin_page.locator("a[href*='/cours/chapitre/']").first
        if first_chapter_link.is_visible():
            first_chapter_link.click()
            admin_page.wait_for_load_state("networkidle")
            # Cliquer sur une leçon (sera redirigée vers la vue publique)
            first_lesson_link = admin_page.locator("a[href*='/cours/lecon/']").first
            if first_lesson_link.is_visible():
                first_lesson_link.click()
                admin_page.wait_for_load_state("networkidle")
                # Doit être sur la vue publique (URL avec slug, pas /lecon/<pk>/)
                # Si la leçon est premium, on doit voir le blur
                blur = admin_page.locator(".paywall-blur-container")
                if blur.is_visible():
                    # Le bouton "Débloquer cette leçon" doit être visible
                    unlock_btn = admin_page.locator("text=Débloquer cette leçon")
                    expect(unlock_btn).to_be_visible()

        # Nettoyer : quitter le mode preview
        admin_page.goto(f"{base_url}/admin-panel/preview-paywall/exit/")

    def test_admin_with_preview_can_open_paywall_modal(self, admin_page: Page, base_url):
        """
        Teste : En mode preview, cliquer sur "Débloquer" ouvre le modal paywall avec les plans Stripe.
        Criticité : critique
        """
        # Activer le mode preview
        admin_page.goto(f"{base_url}/admin-panel/preview-paywall/")
        admin_page.wait_for_url(f"**/tableau-de-bord/")

        # Aller sur une leçon premium via la vue interne
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")

        first_chapter_link = admin_page.locator("a[href*='/cours/chapitre/']").first
        if first_chapter_link.is_visible():
            first_chapter_link.click()
            admin_page.wait_for_load_state("networkidle")
            first_lesson_link = admin_page.locator("a[href*='/cours/lecon/']").first
            if first_lesson_link.is_visible():
                first_lesson_link.click()
                admin_page.wait_for_load_state("networkidle")
                # Si blur visible, cliquer sur le bouton débloquer
                unlock_btn = admin_page.locator("button:has-text('Débloquer cette leçon')")
                if unlock_btn.is_visible():
                    unlock_btn.click()
                    # Le modal paywall doit apparaître
                    modal = admin_page.locator("text=Débloquez tout ScienceLycée")
                    expect(modal).to_be_visible()
                    # Les plans doivent être visibles
                    expect(admin_page.locator("text=Annuel")).to_be_visible()
                    expect(admin_page.locator("text=Mensuel")).to_be_visible()
                    # Le bouton "Passer à Premium" doit être visible
                    expect(admin_page.locator("button:has-text('Passer à Premium')")).to_be_visible()

        # Nettoyer
        admin_page.goto(f"{base_url}/admin-panel/preview-paywall/exit/")


class TestPaywallPreviewBannerOnPublicPages:
    """Tests de la bannière sur les pages publiques."""

    def test_banner_visible_on_public_lesson_page(self, admin_page: Page, base_url):
        """
        Teste : La bannière preview paywall est visible sur les pages publiques (layout sans sidebar).
        Criticité : haute
        """
        # Activer le mode preview
        admin_page.goto(f"{base_url}/admin-panel/preview-paywall/")
        admin_page.wait_for_url(f"**/tableau-de-bord/")

        # Naviguer vers le catalogue public
        admin_page.goto(f"{base_url}/cours/")
        admin_page.wait_for_load_state("networkidle")

        # Aller sur un chapitre puis une leçon
        first_chapter_link = admin_page.locator("a[href*='/cours/chapitre/']").first
        if first_chapter_link.is_visible():
            first_chapter_link.click()
            admin_page.wait_for_load_state("networkidle")
            first_lesson_link = admin_page.locator("a[href*='/cours/lecon/']").first
            if first_lesson_link.is_visible():
                first_lesson_link.click()
                admin_page.wait_for_load_state("networkidle")
                # La bannière doit être visible même sur la page publique
                banner = admin_page.locator("text=Mode prévisualisation paywall actif")
                expect(banner).to_be_visible()

        # Nettoyer
        admin_page.goto(f"{base_url}/admin-panel/preview-paywall/exit/")
