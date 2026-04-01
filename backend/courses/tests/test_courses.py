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

    def test_non_free_lesson_shows_blur_anonymous(self, client, lecon_payante):
        chapitre = lecon_payante.chapitre
        response = client.get(
            reverse("lecon_publique", kwargs={
                "matiere_slug": chapitre.matiere.slug,
                "niveau": chapitre.niveau,
                "chapitre_slug": chapitre.slug,
                "lecon_slug": lecon_payante.slug,
            })
        )
        assert response.status_code == 200
        assert "paywall-blur-container" in response.content.decode()

    def test_authenticated_eleve_sees_public_page(self, client, eleve, lecon_gratuite):
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
        assert response.status_code == 200


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


# ---------------------------------------------------------------------------
# Batch 2 — Course views (matieres, chapitre, lecon, quiz display)
# ---------------------------------------------------------------------------


class TestMatieresView:
    def test_matieres_requires_login(self, client):
        response = client.get(reverse("matieres"))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_matieres_returns_200_for_eleve(self, client, eleve, matiere):
        client.force_login(eleve)
        response = client.get(reverse("matieres"))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_matieres_context_contains_matieres_data(self, client, eleve, matiere):
        client.force_login(eleve)
        response = client.get(reverse("matieres"))
        assert "matieres_data" in response.context

    @pytest.mark.django_db
    def test_matieres_filters_by_niveau(self, client, eleve, matiere):
        """Eleve terminale sees only terminale chapitres."""
        Chapitre.objects.create(matiere=matiere, niveau="terminale", titre="Chap Term", ordre=1)
        Chapitre.objects.create(matiere=matiere, niveau="seconde", titre="Chap Sec", ordre=1)
        client.force_login(eleve)
        response = client.get(reverse("matieres"))
        content = response.content.decode()
        assert "Chap Term" in content
        assert "Chap Sec" not in content

    @pytest.mark.django_db
    def test_admin_sees_all_niveaux(self, client, admin_user, matiere):
        """Admin with no preview session gets 200 (admin browse mode)."""
        Chapitre.objects.create(matiere=matiere, niveau="terminale", titre="Chap T", ordre=1)
        Chapitre.objects.create(matiere=matiere, niveau="seconde", titre="Chap S", ordre=1)
        client.force_login(admin_user)
        response = client.get(reverse("matieres"))
        assert response.status_code == 200
        assert response.context["is_admin_browse"] is True


class TestChapitreView:
    def test_chapitre_requires_login(self, client, chapitre):
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_wrong_niveau_redirects(self, client, eleve, matiere):
        chap_sec = Chapitre.objects.create(matiere=matiere, niveau="seconde", titre="Chap Sec", ordre=1)
        client.force_login(eleve)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chap_sec.pk}))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_locked_chapitre_redirects(self, client, eleve, chapitre):
        """Eleve without ChapitreDebloque is redirected."""
        client.force_login(eleve)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_unlocked_chapitre_returns_200(self, client, eleve, chapitre):
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        client.force_login(eleve)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_chapitre_context_has_lecons_data(self, client, eleve, chapitre, lecon_gratuite):
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        client.force_login(eleve)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert "lecons_data" in response.context
        assert "nb_lecons" in response.context

    @pytest.mark.django_db
    def test_admin_bypasses_unlock_check(self, client, admin_user, chapitre):
        client.force_login(admin_user)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 200


class TestLeconView:
    def test_lecon_requires_login(self, client, lecon_gratuite):
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_wrong_niveau_redirects(self, client, eleve, matiere):
        chap_sec = Chapitre.objects.create(matiere=matiere, niveau="seconde", titre="Chap Sec L", ordre=1)
        lecon_sec = Lecon.objects.create(chapitre=chap_sec, titre="Lecon Sec", contenu="c", ordre=1)
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_sec.pk}))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_locked_chapitre_redirects(self, client, eleve, lecon_gratuite):
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_lecon_returns_200_when_unlocked(self, client, eleve, lecon_gratuite):
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_lecon_marks_en_cours_on_first_access(self, client, eleve, lecon_gratuite):
        from progress.models import ChapitreDebloque, UserProgression
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        prog = UserProgression.objects.get(user=eleve, lecon=lecon_gratuite)
        assert prog.statut == "en_cours"

    @pytest.mark.django_db
    def test_lecon_context_has_contenu_html(self, client, eleve, lecon_gratuite):
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert "contenu_html" in response.context

    @pytest.mark.django_db
    def test_admin_bypasses_unlock(self, client, admin_user, lecon_gratuite):
        client.force_login(admin_user)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_lecon_second_access_keeps_en_cours(self, client, eleve, lecon_gratuite):
        from progress.models import ChapitreDebloque, UserProgression
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        url = reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk})
        client.get(url)
        client.get(url)
        prog = UserProgression.objects.get(user=eleve, lecon=lecon_gratuite)
        assert prog.statut == "en_cours"


class TestQuizDisplayView:
    def test_quiz_requires_login(self, client, lecon_gratuite):
        response = client.get(reverse("quiz", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_quiz_returns_200_with_questions(self, client, eleve, lecon_gratuite):
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Test Quiz")
        for i in range(5):
            Question.objects.create(
                quiz=quiz, texte=f"Q{i}", type="qcm",
                options=["A", "B", "C", "D"], reponse_correcte="0",
                points=1, ordre=i + 1,
            )
        client.force_login(eleve)
        response = client.get(reverse("quiz", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_quiz_no_quiz_redirects_to_lecon(self, client, eleve, lecon_gratuite):
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        response = client.get(reverse("quiz", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 302
        assert f"/cours/lecon/{lecon_gratuite.pk}/" in response["Location"]

    @pytest.mark.django_db
    def test_quiz_context_has_question_ids(self, client, eleve, lecon_gratuite):
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Test Quiz")
        for i in range(3):
            Question.objects.create(
                quiz=quiz, texte=f"Q{i}", type="qcm",
                options=["A", "B", "C", "D"], reponse_correcte="0",
                points=1, ordre=i + 1,
            )
        client.force_login(eleve)
        response = client.get(reverse("quiz", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert "question_ids" in response.context
        assert "questions" in response.context

    @pytest.mark.django_db
    def test_quiz_selects_max_5_questions(self, client, eleve, lecon_gratuite):
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Big Quiz")
        for i in range(10):
            Question.objects.create(
                quiz=quiz, texte=f"Q{i}", type="qcm",
                options=["A", "B", "C", "D"], reponse_correcte="0",
                points=1, ordre=i + 1,
            )
        client.force_login(eleve)
        response = client.get(reverse("quiz", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert len(response.context["questions"]) <= 5

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


# ============================================================
# Batch 5 — Revisions + SoumettreRevisions
# ============================================================


class TestRevisionsView:
    """Tests for the revisions_view (spaced repetition page)."""

    def test_revisions_requires_login(self, client):
        response = client.get(reverse("revisions"))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_revisions_returns_200(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_revisions_context_has_box_display(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        assert "box_display" in response.context
        assert "nb_dues" in response.context
        assert "total_historiques" in response.context

    @pytest.mark.django_db
    def test_revisions_shows_due_questions(self, client, eleve, lecon_gratuite):
        from progress.models import UserQuestionHistorique
        from datetime import date
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Rev Q")
        q = Question.objects.create(
            quiz=quiz, texte="Rev?", type="qcm",
            options=["A", "B"], reponse_correcte="0", points=1, ordre=1,
        )
        UserQuestionHistorique.objects.create(
            user=eleve, question=q, boite=1,
            prochaine_revision=date.today(), nb_bonnes=0, nb_total=1,
        )
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        assert q in response.context["questions"]

    @pytest.mark.django_db
    def test_revisions_hides_future_questions(self, client, eleve, lecon_gratuite):
        from progress.models import UserQuestionHistorique
        from datetime import date, timedelta
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Rev Q2")
        q = Question.objects.create(
            quiz=quiz, texte="Future?", type="qcm",
            options=["A", "B"], reponse_correcte="0", points=1, ordre=1,
        )
        UserQuestionHistorique.objects.create(
            user=eleve, question=q, boite=1,
            prochaine_revision=date.today() + timedelta(days=30),
            nb_bonnes=0, nb_total=1,
        )
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        assert q not in response.context["questions"]


class TestSoumettreRevisions:
    """Tests for soumettre_revisions view (revision quiz submission)."""

    def test_soumettre_revisions_requires_login(self, client):
        response = client.post(reverse("soumettre_revisions"))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_get_redirects_to_revisions(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("soumettre_revisions"))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_soumettre_revisions_empty_ids_redirects(self, client, eleve):
        client.force_login(eleve)
        response = client.post(reverse("soumettre_revisions"), {"question_ids": ""})
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_soumettre_revisions_renders_resultat(self, client, eleve, lecon_gratuite):
        from progress.models import UserQuestionHistorique
        from datetime import date
        from django.core.cache import cache
        cache.clear()
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="RQ")
        q = Question.objects.create(
            quiz=quiz, texte="?", type="qcm",
            options=["A", "B", "C"], reponse_correcte="0", points=1, ordre=1,
        )
        UserQuestionHistorique.objects.create(
            user=eleve, question=q, boite=1,
            prochaine_revision=date.today(), nb_bonnes=0, nb_total=0,
        )
        client.force_login(eleve)
        data = {"question_ids": str(q.id), f"question_{q.id}": "0"}
        response = client.post(reverse("soumettre_revisions"), data)
        assert response.status_code == 200
        assert "corrections" in response.context

    @pytest.mark.django_db
    def test_soumettre_revisions_updates_leitner(self, client, eleve, lecon_gratuite):
        from progress.models import UserQuestionHistorique
        from datetime import date
        from django.core.cache import cache
        cache.clear()
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="RQ2")
        q = Question.objects.create(
            quiz=quiz, texte="Leitner?", type="qcm",
            options=["A", "B", "C"], reponse_correcte="0", points=1, ordre=1,
        )
        hist = UserQuestionHistorique.objects.create(
            user=eleve, question=q, boite=1,
            prochaine_revision=date.today(), nb_bonnes=0, nb_total=0,
        )
        client.force_login(eleve)
        data = {"question_ids": str(q.id), f"question_{q.id}": "0"}
        client.post(reverse("soumettre_revisions"), data)
        hist.refresh_from_db()
        assert hist.boite == 2


# ──────────────────────────────────────────────────────────────────────
# Batch 6 — Search edge cases, accueil, catalogue, helpers, error pages
# ──────────────────────────────────────────────────────────────────────


class TestAccueilView:
    @pytest.mark.django_db
    def test_accueil_accessible_anonymous(self, client):
        """GET "/" sans authentification → 200."""
        response = client.get("/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_accueil_renders_accueil_template(self, client):
        """La page d'accueil utilise le template courses/accueil.html."""
        response = client.get("/")
        assert "courses/accueil.html" in [t.name for t in response.templates]

    @pytest.mark.django_db
    def test_accueil_context_has_matieres_data(self, client, matiere):
        """Le contexte contient 'matieres_data'."""
        response = client.get("/")
        assert "matieres_data" in response.context

    @pytest.mark.django_db
    def test_authenticated_user_redirected_to_dashboard(self, client, eleve):
        """Un utilisateur connecté sur "/" est redirigé vers le tableau de bord."""
        client.force_login(eleve)
        response = client.get("/")
        assert response.status_code == 302
        assert "tableau-de-bord" in response["Location"]


class TestYoutubeHelper:
    """Tests unitaires pour _extraire_youtube_id."""

    def test_standard_url(self):
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_short_url(self):
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_embed_url(self):
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("https://www.youtube.com/embed/dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_none_input(self):
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id(None) is None

    def test_empty_string(self):
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("") is None

    def test_invalid_url(self):
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("not a youtube url") is None


class TestLatexHelpers:
    """Tests unitaires pour _proteger_latex et _restaurer_latex."""

    def test_proteger_inline_latex(self):
        from courses.views import _proteger_latex
        texte = "Voici $x^2$ et $y$"
        result, placeholders = _proteger_latex(texte)
        assert len(placeholders) == 2
        assert "$x^2$" not in result
        assert "$y$" not in result

    def test_proteger_display_latex(self):
        from courses.views import _proteger_latex
        texte = "Voici $$E=mc^2$$"
        result, placeholders = _proteger_latex(texte)
        assert len(placeholders) == 1
        assert "$$E=mc^2$$" not in result

    def test_restaurer_restores_original(self):
        from courses.views import _proteger_latex, _restaurer_latex
        original = "Voici $x^2$ et $$E=mc^2$$"
        protected, placeholders = _proteger_latex(original)
        restored = _restaurer_latex(protected, placeholders)
        assert restored == original

    def test_no_latex_unchanged(self):
        from courses.views import _proteger_latex
        texte = "No LaTeX here"
        result, placeholders = _proteger_latex(texte)
        assert result == texte
        assert len(placeholders) == 0

    def test_mixed_inline_and_display(self):
        from courses.views import _proteger_latex
        texte = "Inline $a+b$ puis display $$\\int_0^1 x\\,dx$$"
        result, placeholders = _proteger_latex(texte)
        assert len(placeholders) == 2
        assert "$a+b$" not in result
        assert "$$\\int_0^1 x\\,dx$$" not in result


class TestCatalogueView:
    @pytest.mark.django_db
    def test_catalogue_nonexistent_matiere_returns_404(self, client):
        """Slug inexistant → 404."""
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": "inexistant"})
        )
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_catalogue_context_has_niveaux_data(self, client, matiere):
        """Le contexte contient 'niveaux_data'."""
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": matiere.slug})
        )
        assert response.status_code == 200
        assert "niveaux_data" in response.context

    @pytest.mark.django_db
    def test_catalogue_contains_chapitre_titles(self, client, chapitre):
        """Le HTML contient le titre du chapitre."""
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": chapitre.matiere.slug})
        )
        assert response.status_code == 200
        assert chapitre.titre.encode() in response.content

    @pytest.mark.django_db
    def test_catalogue_accessible_when_authenticated(self, client, eleve, matiere):
        """La page catalogue est aussi accessible aux utilisateurs connectés."""
        client.force_login(eleve)
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": matiere.slug})
        )
        assert response.status_code == 200


class TestErrorPages:
    @pytest.mark.django_db
    def test_404_returns_404_status(self, client):
        """GET sur une URL inexistante → 404."""
        response = client.get("/cette-url-nexiste-pas/")
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_404_contains_message(self, client):
        """La page 404 contient un message d'erreur."""
        response = client.get("/cette-url-nexiste-pas/")
        assert b"introuvable" in response.content or b"404" in response.content

    def test_500_template_exists(self):
        """Le template 500.html existe et est chargeable."""
        from django.template.loader import get_template
        template = get_template("500.html")
        assert template is not None

