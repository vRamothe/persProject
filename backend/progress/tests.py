import pytest
from datetime import date, timedelta
from django.test import Client
from django.urls import reverse

from courses.models import Matiere, Chapitre, Lecon, Quiz, Question
from progress.models import (
    UserQuizResultat, UserChapitreQuizResultat, ChapitreDebloque,
    UserQuestionHistorique, LEITNER_INTERVALLES,
)
from progress.views import _comparer_texte_libre
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
def matiere(db):
    return Matiere.objects.create(nom="mathematiques", description="Maths")


@pytest.fixture
def chapitre(matiere):
    return Chapitre.objects.create(
        matiere=matiere, niveau="terminale", titre="Suites", ordre=1,
    )


@pytest.fixture
def chapitre_suivant(matiere):
    return Chapitre.objects.create(
        matiere=matiere, niveau="terminale", titre="Limites", ordre=2,
    )


@pytest.fixture
def lecon(chapitre):
    return Lecon.objects.create(
        chapitre=chapitre, titre="Intro suites", contenu="Contenu", ordre=1,
    )


@pytest.fixture
def quiz(lecon):
    return Quiz.objects.create(lecon=lecon, titre="Quiz suites")


@pytest.fixture
def question_qcm(quiz):
    return Question.objects.create(
        quiz=quiz,
        texte="Quelle est la réponse ?",
        type="qcm",
        options=["Paris", "Lyon", "Marseille", "Toulouse"],
        reponse_correcte="0",
        points=1,
        ordre=1,
    )


@pytest.fixture
def question_vrai_faux(quiz):
    return Question.objects.create(
        quiz=quiz,
        texte="2+2 = 4 ?",
        type="vrai_faux",
        reponse_correcte="vrai",
        points=1,
        ordre=2,
    )


@pytest.fixture
def question_texte_libre(quiz):
    return Question.objects.create(
        quiz=quiz,
        texte="Quel gaz est le plus abondant dans l'air ?",
        type="texte_libre",
        reponse_correcte="diazote",
        tolerances=["azote", "N2"],
        points=1,
        ordre=3,
    )


def _make_questions(quiz, count=10):
    """Create `count` QCM questions in the given quiz, all with answer '0'."""
    questions = []
    for i in range(1, count + 1):
        q = Question.objects.create(
            quiz=quiz,
            texte=f"Question {i}",
            type="qcm",
            options=["A", "B", "C", "D"],
            reponse_correcte="0",
            points=1,
            ordre=i,
        )
        questions.append(q)
    return questions


# ---- Quiz scoring tests ----

class TestQuizScoring:
    def test_qcm_correct_answer_scores(self, client, eleve, lecon, quiz, question_qcm):
        client.force_login(eleve)
        response = client.post(
            reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}),
            {
                "question_ids": str(question_qcm.id),
                f"question_{question_qcm.id}": "0",
            },
        )
        assert response.status_code == 200
        resultat = UserQuizResultat.objects.get(user=eleve, quiz=quiz)
        assert resultat.score == 100.0

    def test_qcm_wrong_answer_zero(self, client, eleve, lecon, quiz, question_qcm):
        client.force_login(eleve)
        client.post(
            reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}),
            {
                "question_ids": str(question_qcm.id),
                f"question_{question_qcm.id}": "2",
            },
        )
        resultat = UserQuizResultat.objects.get(user=eleve, quiz=quiz)
        assert resultat.score == 0.0

    def test_vrai_faux_scoring(self, client, eleve, lecon, quiz, question_vrai_faux):
        client.force_login(eleve)
        client.post(
            reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}),
            {
                "question_ids": str(question_vrai_faux.id),
                f"question_{question_vrai_faux.id}": "vrai",
            },
        )
        resultat = UserQuizResultat.objects.get(user=eleve, quiz=quiz)
        assert resultat.score == 100.0

    def test_texte_libre_exact_match(self, question_texte_libre):
        assert _comparer_texte_libre("diazote", question_texte_libre) is True

    def test_texte_libre_tolerance_match(self, question_texte_libre):
        assert _comparer_texte_libre("azote", question_texte_libre) is True
        assert _comparer_texte_libre("N2", question_texte_libre) is True

    def test_texte_libre_case_insensitive(self, question_texte_libre):
        assert _comparer_texte_libre("DIAZOTE", question_texte_libre) is True
        assert _comparer_texte_libre("Azote", question_texte_libre) is True
        assert _comparer_texte_libre("n2", question_texte_libre) is True

    def test_texte_libre_wrong_answer(self, question_texte_libre):
        assert _comparer_texte_libre("oxygène", question_texte_libre) is False


# ---- Chapter unlock tests ----

class TestChapterUnlock:
    def test_chapitre_quiz_pass_at_80_percent(self, client, eleve, chapitre, lecon, quiz):
        """Scoring >= 80% on the chapter quiz should pass."""
        questions = _make_questions(quiz, 10)
        client.force_login(eleve)

        # Answer 8/10 correctly (80%)
        data = {"question_ids": ",".join(str(q.id) for q in questions)}
        for i, q in enumerate(questions):
            data[f"question_{q.id}"] = "0" if i < 8 else "1"  # 8 correct, 2 wrong

        response = client.post(
            reverse("soumettre_quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}),
            data,
        )
        assert response.status_code == 200
        resultat = UserChapitreQuizResultat.objects.get(user=eleve, chapitre=chapitre)
        assert resultat.passe is True
        assert resultat.score >= 80.0

    def test_chapitre_quiz_fail_below_80_percent(self, client, eleve, chapitre, lecon, quiz):
        """Scoring < 80% on the chapter quiz should fail."""
        questions = _make_questions(quiz, 10)
        client.force_login(eleve)

        # Answer 7/10 correctly (70%)
        data = {"question_ids": ",".join(str(q.id) for q in questions)}
        for i, q in enumerate(questions):
            data[f"question_{q.id}"] = "0" if i < 7 else "1"

        client.post(
            reverse("soumettre_quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}),
            data,
        )
        resultat = UserChapitreQuizResultat.objects.get(user=eleve, chapitre=chapitre)
        assert resultat.passe is False

    def test_passing_creates_chapitre_debloque(
        self, client, eleve, chapitre, chapitre_suivant, lecon, quiz
    ):
        """Passing the chapter quiz should create a ChapitreDebloque for the next chapter."""
        questions = _make_questions(quiz, 10)
        client.force_login(eleve)

        data = {"question_ids": ",".join(str(q.id) for q in questions)}
        for q in questions:
            data[f"question_{q.id}"] = "0"  # All correct

        client.post(
            reverse("soumettre_quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}),
            data,
        )
        assert ChapitreDebloque.objects.filter(
            user=eleve, chapitre=chapitre_suivant
        ).exists()


# ---- Leitner spaced repetition tests ----

class TestLeitner:
    def test_correct_answer_moves_box_up(self, eleve, question_qcm):
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=1,
            prochaine_revision=date.today(),
        )
        hist.enregistrer_reponse(True)
        assert hist.boite == 2

    def test_wrong_answer_resets_to_box_1(self, eleve, question_qcm):
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=3,
            prochaine_revision=date.today(),
        )
        hist.enregistrer_reponse(False)
        assert hist.boite == 1

    def test_max_box_is_5(self, eleve, question_qcm):
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=5,
            prochaine_revision=date.today(),
        )
        hist.enregistrer_reponse(True)
        assert hist.boite == 5

    def test_prochaine_revision_calculated_correctly(self, eleve, question_qcm):
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=1,
            prochaine_revision=date.today(),
        )
        hist.enregistrer_reponse(True)  # box 1 -> 2, interval = 3 days
        expected = date.today() + timedelta(days=LEITNER_INTERVALLES[2])
        assert hist.prochaine_revision == expected

    def test_wrong_resets_interval_to_box_1(self, eleve, question_qcm):
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=4,
            prochaine_revision=date.today(),
        )
        hist.enregistrer_reponse(False)  # box -> 1, interval = 1 day
        expected = date.today() + timedelta(days=LEITNER_INTERVALLES[1])
        assert hist.prochaine_revision == expected


# ---- Rate limiting tests ----

class TestRateLimiting:
    def test_first_call_not_limited(self):
        from progress.views import _check_quiz_rate_limit
        from django.core.cache import cache
        cache.clear()
        assert _check_quiz_rate_limit(9999) is False

    def test_29th_call_not_limited(self):
        from progress.views import _check_quiz_rate_limit
        from django.core.cache import cache
        cache.clear()
        for _ in range(29):
            result = _check_quiz_rate_limit(8888)
        assert result is False

    def test_30th_call_is_limited(self):
        from progress.views import _check_quiz_rate_limit
        from django.core.cache import cache
        cache.clear()
        for _ in range(30):
            _check_quiz_rate_limit(7777)
        assert _check_quiz_rate_limit(7777) is True

    def test_different_users_independent_counters(self):
        from progress.views import _check_quiz_rate_limit
        from django.core.cache import cache
        cache.clear()
        for _ in range(30):
            _check_quiz_rate_limit(6666)
        # user 5555 is not limited even though 6666 is
        assert _check_quiz_rate_limit(5555) is False

    def test_soumettre_quiz_returns_429_when_limited(self, client, eleve, lecon, quiz, question_qcm):
        from django.core.cache import cache
        cache.clear()
        cache.set(f"quiz_rate_{eleve.id}", 30, timeout=60)
        client.force_login(eleve)
        response = client.post(
            reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}),
            {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "0"},
        )
        assert response.status_code == 429

    def test_soumettre_quiz_chapitre_returns_429_when_limited(self, client, eleve, chapitre, lecon, quiz, question_qcm):
        from django.core.cache import cache
        cache.clear()
        cache.set(f"quiz_rate_{eleve.id}", 30, timeout=60)
        client.force_login(eleve)
        response = client.post(
            reverse("soumettre_quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}),
            {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "0"},
        )
        assert response.status_code == 429


# ---- UserNote tests ----

class TestUserNote:
    def test_save_note_returns_200(self, client, eleve, lecon):
        client.force_login(eleve)
        response = client.post(
            reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}),
            {"contenu": "Mes notes importantes"},
        )
        assert response.status_code == 200

    def test_second_save_updates_existing_note(self, client, eleve, lecon):
        from progress.models import UserNote
        client.force_login(eleve)
        client.post(reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}), {"contenu": "v1"})
        client.post(reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}), {"contenu": "v2"})
        assert UserNote.objects.filter(user=eleve, lecon=lecon).count() == 1
        assert UserNote.objects.get(user=eleve, lecon=lecon).contenu == "v2"

    def test_content_truncated_to_2000_chars(self, client, eleve, lecon):
        from progress.models import UserNote
        client.force_login(eleve)
        client.post(
            reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}),
            {"contenu": "x" * 2001},
        )
        note = UserNote.objects.get(user=eleve, lecon=lecon)
        assert len(note.contenu) == 2000

    def test_empty_post_saves_empty_string(self, client, eleve, lecon):
        from progress.models import UserNote
        client.force_login(eleve)
        client.post(reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}), {"contenu": ""})
        note = UserNote.objects.get(user=eleve, lecon=lecon)
        assert note.contenu == ""

    def test_anonymous_post_redirects(self, client, lecon):
        response = client.post(
            reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}),
            {"contenu": "test"},
        )
        assert response.status_code == 302

    def test_two_users_can_each_have_note_on_same_lecon(self, db, lecon):
        from progress.models import UserNote
        u1 = CustomUser.objects.create_user(email="u1@test.com", password="pass", prenom="A", nom="B", role="eleve", niveau="terminale")
        u2 = CustomUser.objects.create_user(email="u2@test.com", password="pass", prenom="C", nom="D", role="eleve", niveau="terminale")
        UserNote.objects.create(user=u1, lecon=lecon, contenu="note u1")
        UserNote.objects.create(user=u2, lecon=lecon, contenu="note u2")
        assert UserNote.objects.filter(lecon=lecon).count() == 2

    def test_deleting_lecon_cascades_to_notes(self, db, lecon):
        from progress.models import UserNote
        u = CustomUser.objects.create_user(email="cascade@test.com", password="pass", prenom="C", nom="D", role="eleve", niveau="terminale")
        UserNote.objects.create(user=u, lecon=lecon, contenu="to be deleted")
        lecon.delete()
        assert UserNote.objects.filter(contenu="to be deleted").count() == 0

    def test_lecon_view_context_contains_note(self, client, eleve, lecon, chapitre):
        from progress.models import UserNote, ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        note = UserNote.objects.create(user=eleve, lecon=lecon, contenu="noter quelque chose")
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon.pk}))
        assert response.context["note"] == note
