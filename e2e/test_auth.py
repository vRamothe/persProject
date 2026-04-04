"""
Tests E2E — Authentification (connexion, déconnexion, inscription).
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
from playwright.sync_api import Page, expect


class TestConnexionDeconnexion:
    """Tests de connexion et déconnexion admin."""

    def test_login_with_valid_credentials(self, page: Page, base_url, admin_credentials):
        """
        Teste : Connexion avec les bons identifiants redirige vers le dashboard.
        Criticité : critique
        """
        page.goto(f"{base_url}/connexion/")
        page.fill('input[name="username"]', admin_credentials["email"])
        page.fill('input[name="password"]', admin_credentials["password"])
        page.click('button[type="submit"]')
        page.wait_for_url("**/tableau-de-bord/")
        expect(page).to_have_url(f"{base_url}/tableau-de-bord/")

    def test_login_with_invalid_credentials(self, page: Page, base_url, admin_credentials):
        """
        Teste : Connexion avec un mauvais mot de passe reste sur /connexion/ avec erreur.
        Criticité : critique
        """
        page.goto(f"{base_url}/connexion/")
        page.fill('input[name="username"]', admin_credentials["email"])
        page.fill('input[name="password"]', "mauvais_mot_de_passe_999")
        page.click('button[type="submit"]')
        # Reste sur la page de connexion
        expect(page).to_have_url(f"{base_url}/connexion/")
        # Message d'erreur visible (div rouge avec les non_field_errors)
        error_box = page.locator(".bg-red-50")
        expect(error_box).to_be_visible()

    def test_logout_redirects_to_login(self, admin_page: Page, base_url):
        """
        Teste : La déconnexion redirige vers /connexion/.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/deconnexion/")
        admin_page.wait_for_url("**/connexion/")
        expect(admin_page).to_have_url(f"{base_url}/connexion/")

    def test_logout_prevents_dashboard_access(self, admin_page: Page, base_url):
        """
        Teste : Après déconnexion, /tableau-de-bord/ redirige vers login.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/deconnexion/")
        admin_page.wait_for_url("**/connexion/")
        # Tenter d'accéder au dashboard
        admin_page.goto(f"{base_url}/tableau-de-bord/")
        # Doit être redirigé vers la page de connexion
        expect(admin_page).to_have_url(f"{base_url}/connexion/?next=/tableau-de-bord/")


class TestInscriptionForm:
    """Tests du formulaire d'inscription."""

    def test_registration_form_has_all_fields(self, page: Page, base_url):
        """
        Teste : Le formulaire d'inscription contient tous les champs requis.
        Criticité : haute
        """
        page.goto(f"{base_url}/inscription/")
        expect(page.locator('input[name="email"]')).to_be_visible()
        expect(page.locator('input[name="prenom"]')).to_be_visible()
        expect(page.locator('input[name="nom"]')).to_be_visible()
        expect(page.locator('select[name="niveau"]')).to_be_visible()
        expect(page.locator('input[name="password1"]')).to_be_visible()
        expect(page.locator('input[name="password2"]')).to_be_visible()

    def test_registration_invalid_password_shows_error(self, page: Page, base_url):
        """
        Teste : Un mot de passe trop court affiche un message d'erreur.
        Criticité : haute
        """
        page.goto(f"{base_url}/inscription/")
        page.fill('input[name="prenom"]', "Test")
        page.fill('input[name="nom"]', "Erreur")
        page.fill('input[name="email"]', "test_erreur_e2e@example.com")
        page.locator('select[name="niveau"]').select_option("seconde")
        page.fill('input[name="password1"]', "court")
        page.fill('input[name="password2"]', "court")
        page.click('button[type="submit"]')
        # Reste sur la page d'inscription
        expect(page).to_have_url(f"{base_url}/inscription/")
        # Message d'erreur visible sur le champ password1
        error_msg = page.locator("text=Le mot de passe doit contenir au moins 8 caractères").first
        expect(error_msg).to_be_visible()
