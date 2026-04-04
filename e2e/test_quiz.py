"""
Tests E2E — Quiz (leçon et chapitre).
Prérequis : docker compose up --build -d + seed_data exécuté.
"""
import re
from playwright.sync_api import Page, expect


class TestQuizFlow:
    """Tests du flux quiz : affichage, soumission, corrections."""

    def _navigate_to_quiz(self, admin_page: Page, base_url: str):
        """Helper : navigue vers la page quiz de la première leçon disponible."""
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
        # Cliquer sur le lien quiz
        quiz_link = admin_page.locator("a[href*='/quiz/']").first
        expect(quiz_link).to_be_visible()
        quiz_link.click()
        admin_page.wait_for_load_state("networkidle")

    def test_quiz_page_has_questions(self, admin_page: Page, base_url):
        """
        Teste : La page quiz affiche au moins 1 question.
        Criticité : critique
        """
        self._navigate_to_quiz(admin_page, base_url)
        # Vérifier la présence du formulaire quiz
        form = admin_page.locator("#quiz-container form")
        expect(form).to_be_visible()
        # Au moins un bloc de question (div avec les radio/input dans le form)
        questions = admin_page.locator(
            "#quiz-container input[type='radio'], #quiz-container input[type='text']"
        )
        assert questions.count() >= 1, "Aucune question trouvée sur la page quiz"

    def test_quiz_submit_shows_result(self, admin_page: Page, base_url):
        """
        Teste : Répondre aux questions et soumettre affiche une page résultat avec score.
        Criticité : critique
        """
        self._navigate_to_quiz(admin_page, base_url)
        # Répondre à chaque question : sélectionner la première option disponible
        # Les questions sont groupées par name="question_<pk>"
        form = admin_page.locator("#quiz-container form")
        # Trouver tous les groupes de questions (noms uniques de radio/text inputs)
        radio_groups = form.locator("input[type='radio']")
        text_inputs = form.locator("input[type='text'][name^='question_']")

        # Cocher le premier radio de chaque groupe de questions
        answered_groups = set()
        for i in range(radio_groups.count()):
            radio = radio_groups.nth(i)
            name = radio.get_attribute("name")
            if name and name not in answered_groups:
                radio.check(force=True)
                answered_groups.add(name)

        # Remplir les champs texte libre
        for i in range(text_inputs.count()):
            text_input = text_inputs.nth(i)
            text_input.fill("test")

        # Soumettre le quiz (HTMX remplace #quiz-container)
        submit_btn = admin_page.locator("button:has-text('Valider mes réponses')")
        submit_btn.click()
        # Attendre la réponse HTMX
        admin_page.wait_for_load_state("networkidle")

        # Le score doit être affiché (format: XX%)
        score_element = admin_page.locator("#quiz-container").locator("text=/%/")
        # Alternative : chercher le texte de résultat
        result_container = admin_page.locator("#quiz-container")
        result_text = result_container.inner_text()
        assert re.search(r"\d+\s*%", result_text), \
            f"Score non trouvé dans le résultat du quiz: {result_text[:200]}"

    def test_quiz_result_shows_corrections(self, admin_page: Page, base_url):
        """
        Teste : Après soumission, les corrections détaillées sont affichées.
        Criticité : haute
        """
        self._navigate_to_quiz(admin_page, base_url)
        # Répondre à chaque question
        form = admin_page.locator("#quiz-container form")
        radio_groups = form.locator("input[type='radio']")
        text_inputs = form.locator("input[type='text'][name^='question_']")

        answered_groups = set()
        for i in range(radio_groups.count()):
            radio = radio_groups.nth(i)
            name = radio.get_attribute("name")
            if name and name not in answered_groups:
                radio.check(force=True)
                answered_groups.add(name)

        for i in range(text_inputs.count()):
            text_inputs.nth(i).fill("test")

        # Soumettre
        admin_page.locator("button:has-text('Valider mes réponses')").click()
        admin_page.wait_for_load_state("networkidle")

        # Vérifier la section "Correction détaillée"
        correction_heading = admin_page.locator("text=Correction détaillée")
        expect(correction_heading).to_be_visible()

        # Vérifier qu'il y a des indicateurs correct/incorrect (✅ ou ❌)
        result_text = admin_page.locator("#quiz-container").inner_text()
        has_correct = "✅" in result_text
        has_incorrect = "❌" in result_text
        assert has_correct or has_incorrect, \
            "Aucun indicateur de correction (✅/❌) trouvé dans les résultats"
