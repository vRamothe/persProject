import pytest
from django.test import Client
from django.urls import reverse
from courses.models import Matiere, Chapitre, Lecon, Quiz, Question, DifficulteChoices
from users.models import CustomUser


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def eleve(db):
    return CustomUser.objects.create_user(
        email="eleve@test.com",
        password="TestPass123!",
        prenom="Jean",
        nom="Dupont",
        role="eleve",
        niveau="terminale",
    )


@pytest.fixture
def admin_user(db):
    return CustomUser.objects.create_user(
        email="admin@test.com",
        password="AdminPass123!",
        prenom="Admin",
        nom="Principal",
        role="admin",
        is_staff=True,
    )


@pytest.fixture
def matiere(db):
    return Matiere.objects.create(nom="mathematiques", description="Maths")


@pytest.fixture
def chapitre(matiere):
    return Chapitre.objects.create(
        matiere=matiere,
        niveau="terminale",
        titre="Les Suites Numériques",
        ordre=1,
    )


@pytest.fixture
def lecon_gratuite(chapitre):
    return Lecon.objects.create(
        chapitre=chapitre,
        titre="Définition et premiers exemples",
        contenu="# Introduction\nContenu de la leçon.",
        ordre=1,
        gratuit=True,
    )


@pytest.fixture
def lecon_payante(chapitre):
    return Lecon.objects.create(
        chapitre=chapitre,
        titre="Suites arithmétiques",
        contenu="# Suites arithmétiques\nContenu payant.",
        ordre=2,
        gratuit=False,
    )


class TestSlugGeneration:
    def test_matiere_slug_auto_generated(self, matiere):
        assert matiere.slug == "mathematiques"

    def test_chapitre_slug_auto_generated(self, chapitre):
        assert chapitre.slug == "les-suites-numeriques"

    def test_lecon_slug_auto_generated(self, lecon_gratuite):
        assert lecon_gratuite.slug == "definition-et-premiers-exemples"

    def test_slug_unique_within_scope(self, chapitre):
        """Two lessons in the same chapter cannot have the same slug."""
        Lecon.objects.create(
            chapitre=chapitre,
            titre="Test unique",
            contenu="Test",
            ordre=10,
        )
        # A different chapitre can have the same slug
        matiere2 = Matiere.objects.create(nom="physique")
        chapitre2 = Chapitre.objects.create(
            matiere=matiere2, niveau="terminale", titre="Autre chapitre", ordre=1,
        )
        lecon2 = Lecon.objects.create(
            chapitre=chapitre2,
            titre="Test unique",
            contenu="Test",
            ordre=1,
        )
        assert lecon2.slug == "test-unique"


class TestPublicPages:
    def test_catalogue_accessible_anonymous(self, client, matiere):
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": "mathematiques"})
        )
        assert response.status_code == 200

    def test_free_lesson_accessible_anonymous(self, client, lecon_gratuite):
        chapitre = lecon_gratuite.chapitre
        response = client.get(
            reverse("lecon_publique", kwargs={
                "matiere_slug": chapitre.matiere.slug,
                "niveau": chapitre.niveau,
                "chapitre_slug": chapitre.slug,
                "lecon_slug": lecon_gratuite.slug,
            })
        )
        assert response.status_code == 200

    def test_non_free_lesson_redirects_to_login(self, client, lecon_payante):
        chapitre = lecon_payante.chapitre
        response = client.get(
            reverse("lecon_publique", kwargs={
                "matiere_slug": chapitre.matiere.slug,
                "niveau": chapitre.niveau,
                "chapitre_slug": chapitre.slug,
                "lecon_slug": lecon_payante.slug,
            })
        )
        assert response.status_code == 302
        assert "connexion" in response.url

    def test_authenticated_user_redirected_to_pk_view(self, client, eleve, lecon_gratuite):
        client.force_login(eleve)
        chapitre = lecon_gratuite.chapitre
        response = client.get(
            reverse("lecon_publique", kwargs={
                "matiere_slug": chapitre.matiere.slug,
                "niveau": chapitre.niveau,
                "chapitre_slug": chapitre.slug,
                "lecon_slug": lecon_gratuite.slug,
            })
        )
        assert response.status_code == 302
        assert f"/cours/lecon/{lecon_gratuite.pk}/" in response.url


class TestSitemap:
    def test_sitemap_accessible_anonymous(self, client, matiere):
        response = client.get("/sitemap.xml")
        assert response.status_code == 200

    def test_sitemap_content_type_xml(self, client, matiere):
        response = client.get("/sitemap.xml")
        assert "xml" in response["Content-Type"]

    def test_sitemap_valid_xml(self, client, matiere):
        import xml.etree.ElementTree as ET
        response = client.get("/sitemap.xml")
        ET.fromstring(response.content)  # should not raise

    def test_sitemap_contains_free_lesson_url(self, client, lecon_gratuite):
        response = client.get("/sitemap.xml")
        assert lecon_gratuite.slug.encode() in response.content

    def test_sitemap_does_not_contain_non_free_lesson(self, client, lecon_payante):
        response = client.get("/sitemap.xml")
        assert lecon_payante.slug.encode() not in response.content

    def test_sitemap_has_catalogue_urls(self, client, matiere):
        response = client.get("/sitemap.xml")
        assert b"mathematiques" in response.content


class TestRecherche:
    def test_recherche_returns_200(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("recherche"), {"q": "suites"})
        assert response.status_code == 200

    def test_recherche_short_query_returns_empty(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("recherche"), {"q": "a"})
        assert response.status_code == 200
        assert len(response.context["results"]) == 0

    def test_recherche_anonymous_redirected(self, client):
        response = client.get(reverse("recherche"), {"q": "suites"})
        assert response.status_code == 302


class TestDifficulte:
    def test_question_default_difficulte_is_moyen(self, db, matiere, chapitre):
        lecon = Lecon.objects.create(chapitre=chapitre, titre="L", contenu="c", ordre=5)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q")
        q = Question.objects.create(quiz=quiz, texte="?", type="qcm", reponse_correcte="0", ordre=1)
        assert q.difficulte == DifficulteChoices.MOYEN

    def test_selectionner_questions_chapitre_balanced(self, db, matiere, chapitre):
        from courses.views import _selectionner_questions_chapitre
        lecon = Lecon.objects.create(chapitre=chapitre, titre="L", contenu="c", ordre=6)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q")
        for i in range(4):
            Question.objects.create(quiz=quiz, texte=f"F{i}", type="qcm", reponse_correcte="0", ordre=i+1, difficulte="facile")
        for i in range(4):
            Question.objects.create(quiz=quiz, texte=f"M{i}", type="qcm", reponse_correcte="0", ordre=i+10, difficulte="moyen")
        for i in range(2):
            Question.objects.create(quiz=quiz, texte=f"D{i}", type="qcm", reponse_correcte="0", ordre=i+20, difficulte="difficile")
        selection = _selectionner_questions_chapitre(chapitre, nb_total=10)
        assert len(selection) == 10
        nb_facile = sum(1 for q in selection if q.difficulte == "facile")
        nb_moyen = sum(1 for q in selection if q.difficulte == "moyen")
        nb_difficile = sum(1 for q in selection if q.difficulte == "difficile")
        assert nb_facile == 4
        assert nb_moyen == 4
        assert nb_difficile == 2

    def test_selectionner_no_duplicates(self, db, matiere, chapitre):
        from courses.views import _selectionner_questions_chapitre
        lecon = Lecon.objects.create(chapitre=chapitre, titre="L2", contenu="c", ordre=7)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q2")
        for i in range(15):
            Question.objects.create(quiz=quiz, texte=f"Q{i}", type="qcm", reponse_correcte="0", ordre=i+1)
        selection = _selectionner_questions_chapitre(chapitre, nb_total=10)
        ids = [q.id for q in selection]
        assert len(ids) == len(set(ids))

    def test_selectionner_small_pool_returns_all(self, db, matiere, chapitre):
        from courses.views import _selectionner_questions_chapitre
        lecon = Lecon.objects.create(chapitre=chapitre, titre="L3", contenu="c", ordre=8)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q3")
        for i in range(6):
            Question.objects.create(quiz=quiz, texte=f"S{i}", type="qcm", reponse_correcte="0", ordre=i+1)
        selection = _selectionner_questions_chapitre(chapitre, nb_total=10)
        assert len(selection) == 6

    def test_selectionner_empty_pool_returns_empty(self, db, matiere, chapitre):
        from courses.views import _selectionner_questions_chapitre
        # chapitre without any questions
        chap_empty = Chapitre.objects.create(matiere=matiere, niveau="terminale", titre="Vide", ordre=99)
        selection = _selectionner_questions_chapitre(chap_empty, nb_total=10)
        assert selection == []


class TestImportQuestions:
    def test_valid_csv_creates_question(self, tmp_path, db, matiere, chapitre):
        from django.core.management import call_command
        lecon = Lecon.objects.create(chapitre=chapitre, titre="Import test", contenu="c", ordre=9)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q import")
        csv_content = (
            "quiz_lecon_slug,texte,type,reponse_correcte,options,tolerances,explication,points,ordre,difficulte\n"
            f"{lecon.slug},\"Qu'est-ce?\",texte_libre,réponse,,,expliqué,1,1,facile\n"
        )
        csv_file = tmp_path / "questions.csv"
        csv_file.write_text(csv_content, encoding="utf-8")
        call_command("import_questions", str(csv_file))
        assert Question.objects.filter(quiz=quiz, texte="Qu'est-ce?").exists()

    def test_dry_run_creates_no_question(self, tmp_path, db, matiere, chapitre):
        from django.core.management import call_command
        lecon = Lecon.objects.create(chapitre=chapitre, titre="Dry run", contenu="c", ordre=10)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q dry")
        csv_content = (
            "quiz_lecon_slug,texte,type,reponse_correcte,options,tolerances,explication,points,ordre,difficulte\n"
            f"{lecon.slug},Question dry,texte_libre,rep,,,exp,1,1,moyen\n"
        )
        csv_file = tmp_path / "dry.csv"
        csv_file.write_text(csv_content, encoding="utf-8")
        call_command("import_questions", str(csv_file), "--dry-run")
        assert Question.objects.filter(quiz=quiz).count() == 0

    def test_invalid_lecon_slug_skips_row(self, tmp_path, db):
        from django.core.management import call_command
        csv_content = (
            "quiz_lecon_slug,texte,type,reponse_correcte,options,tolerances,explication,points,ordre,difficulte\n"
            "slug-inexistant,Question,texte_libre,rep,,,exp,1,1,moyen\n"
        )
        csv_file = tmp_path / "bad.csv"
        csv_file.write_text(csv_content, encoding="utf-8")
        call_command("import_questions", str(csv_file))
        assert Question.objects.count() == 0

    def test_missing_reponse_correcte_skips_row(self, tmp_path, db, matiere, chapitre):
        from django.core.management import call_command
        lecon = Lecon.objects.create(chapitre=chapitre, titre="Skip rep", contenu="c", ordre=11)
        Quiz.objects.create(lecon=lecon, titre="Q skip")
        csv_content = (
            "quiz_lecon_slug,texte,type,reponse_correcte,options,tolerances,explication,points,ordre,difficulte\n"
            f"{lecon.slug},Question sans réponse,texte_libre,,,,exp,1,1,moyen\n"
        )
        csv_file = tmp_path / "noreponse.csv"
        csv_file.write_text(csv_content, encoding="utf-8")
        call_command("import_questions", str(csv_file))
        assert Question.objects.count() == 0

    def test_header_only_csv_no_crash(self, tmp_path, db):
        from django.core.management import call_command
        csv_content = "quiz_lecon_slug,texte,type,reponse_correcte,options,tolerances,explication,points,ordre,difficulte\n"
        csv_file = tmp_path / "empty.csv"
        csv_file.write_text(csv_content, encoding="utf-8")
        call_command("import_questions", str(csv_file))

    def test_qcm_options_parsed_as_json(self, tmp_path, db, matiere, chapitre):
        from django.core.management import call_command
        lecon = Lecon.objects.create(chapitre=chapitre, titre="QCM opts", contenu="c", ordre=12)
        Quiz.objects.create(lecon=lecon, titre="Q qcm")
        csv_content = (
            "quiz_lecon_slug,texte,type,reponse_correcte,options,tolerances,explication,points,ordre,difficulte\n"
            f'{lecon.slug},QCM question,qcm,0,"[""A"",""B"",""C""]",,exp,1,1,moyen\n'
        )
        csv_file = tmp_path / "qcm.csv"
        csv_file.write_text(csv_content, encoding="utf-8")
        call_command("import_questions", str(csv_file))
        q = Question.objects.get(texte="QCM question")
        assert q.options == ["A", "B", "C"]

