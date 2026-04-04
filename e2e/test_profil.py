"""
Tests E2E — Page de profil.
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
from playwright.sync_api import Page, expect


class TestProfilPage:
    """Tests de la page Mon profil."""

    def test_profil_page_loads(self, admin_page: Page, base_url):
        """
        Teste : /profil/ se charge et affiche les formulaires profil et mot de passe.
        Criticité : haute
        """
        response = admin_page.goto(f"{base_url}/profil/")
        assert response.status == 200
        admin_page.wait_for_load_state("networkidle")
        # Heading profil
        expect(admin_page.get_by_role("heading", name="Mon profil")).to_be_visible()
        # Section informations personnelles
        expect(admin_page.locator("text=Informations personnelles").first).to_be_visible()
        # Section mot de passe
        expect(admin_page.locator("text=Changer le mot de passe").first).to_be_visible()

    def test_profil_has_info_fields(self, admin_page: Page, base_url):
        """
        Teste : Les champs prénom, nom, email sont visibles et pré-remplis.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/profil/")
        admin_page.wait_for_load_state("networkidle")
        # Champ prénom
        prenom = admin_page.locator("input[name='prenom']")
        expect(prenom).to_be_visible()
        assert prenom.input_value() != "", "Le champ prénom devrait être pré-rempli"
        # Champ nom
        nom = admin_page.locator("input[name='nom']")
        expect(nom).to_be_visible()
        assert nom.input_value() != "", "Le champ nom devrait être pré-rempli"
        # Champ email
        email = admin_page.locator("input[name='email']")
        expect(email).to_be_visible()
        assert email.input_value() != "", "Le champ email devrait être pré-rempli"

    def test_profil_has_password_form(self, admin_page: Page, base_url):
        """
        Teste : Les champs ancien mot de passe, nouveau et confirmation sont visibles.
        Criticité : haute
        """
        admin_page.goto(f"{base_url}/profil/")
        admin_page.wait_for_load_state("networkidle")
        # Ancien mot de passe
        old_pwd = admin_page.locator("input[name='old_password']")
        expect(old_pwd).to_be_visible()
        # Nouveau mot de passe
        new_pwd1 = admin_page.locator("input[name='new_password1']")
        expect(new_pwd1).to_be_visible()
        # Confirmation
        new_pwd2 = admin_page.locator("input[name='new_password2']")
        expect(new_pwd2).to_be_visible()
