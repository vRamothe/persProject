import pytest
from datetime import date, timedelta
from django.test import Client
from django.urls import reverse

from courses.models import Matiere, Chapitre, Lecon, Quiz, Question
from progress.models import (
    UserProgression, UserQuizResultat, UserChapitreQuizResultat, ChapitreDebloque,
    UserQuestionHistorique, LEITNER_INTERVALLES, StatutLeconChoices,
)
from progress.views import _comparer_texte_libre, _enregistrer_historique_questions
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
        """Teste: Une réponse QCM correcte donne un score de 100%
        Raison: Vérifie que le scoring de base fonctionne et que le résultat est bien enregistré
        Features: quiz, scoring, UserQuizResultat
        Criticité: haute"""
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
        """Teste: Une réponse QCM incorrecte donne un score de 0%
        Raison: Vérifie qu'aucun point n'est attribué pour une mauvaise réponse
        Features: quiz, scoring, UserQuizResultat
        Criticité: haute"""
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
        """Teste: Une réponse vrai/faux correcte donne un score de 100%
        Raison: Vérifie le scoring pour le type de question vrai/faux
        Features: quiz, scoring, vrai_faux
        Criticité: moyenne"""
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
        """Teste: La réponse exacte en texte libre est acceptée
        Raison: Vérifie la correspondance exacte avec reponse_correcte
        Features: quiz, texte_libre, _comparer_texte_libre
        Criticité: haute"""
        assert _comparer_texte_libre("diazote", question_texte_libre) is True

    def test_texte_libre_tolerance_match(self, question_texte_libre):
        """Teste: Les réponses alternatives définies dans tolerances sont acceptées
        Raison: Vérifie que le champ tolerances JSONField fonctionne pour les synonymes
        Features: quiz, texte_libre, tolerances
        Criticité: haute"""
        assert _comparer_texte_libre("azote", question_texte_libre) is True
        assert _comparer_texte_libre("N2", question_texte_libre) is True

    def test_texte_libre_case_insensitive(self, question_texte_libre):
        """Teste: La comparaison texte libre est insensible à la casse
        Raison: Les élèves peuvent saisir en majuscules/minuscules — le scoring doit être tolérant
        Features: quiz, texte_libre, _comparer_texte_libre
        Criticité: moyenne"""
        assert _comparer_texte_libre("DIAZOTE", question_texte_libre) is True
        assert _comparer_texte_libre("Azote", question_texte_libre) is True
        assert _comparer_texte_libre("n2", question_texte_libre) is True

    def test_texte_libre_wrong_answer(self, question_texte_libre):
        """Teste: Une réponse texte libre incorrecte est refusée
        Raison: Vérifie qu'une réponse hors tolérance ne valide pas la question
        Features: quiz, texte_libre, _comparer_texte_libre
        Criticité: haute"""
        assert _comparer_texte_libre("oxygène", question_texte_libre) is False


# ---- Chapter unlock tests ----

class TestChapterUnlock:
    def test_chapitre_quiz_pass_at_80_percent(self, client, eleve, chapitre, lecon, quiz):
        """Teste: Un score >= 80% au quiz de chapitre est validé (passe=True)
        Raison: Le seuil de 80% est critique pour la progression — un bug fausserait le déblocage
        Features: quiz_chapitre, scoring, UserChapitreQuizResultat
        Criticité: haute"""
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
        """Teste: Un score < 80% au quiz de chapitre échoue (passe=False)
        Raison: Empêche le déblocage du chapitre suivant sans maîtrise suffisante
        Features: quiz_chapitre, scoring, UserChapitreQuizResultat
        Criticité: haute"""
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
        """Teste: Réussir le quiz de chapitre crée un ChapitreDebloque pour le chapitre suivant
        Raison: Mécanisme central de progression — sans déblocage, l'élève est bloqué
        Features: quiz_chapitre, déblocage, ChapitreDebloque
        Criticité: haute"""
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
        """Teste: Une bonne réponse fait monter la question d'une boîte Leitner
        Raison: Mécanisme fondamental de la répétition espacée — progression vers la maîtrise
        Features: leitner, UserQuestionHistorique, enregistrer_reponse
        Criticité: haute"""
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=1,
            prochaine_revision=date.today(),
        )
        hist.enregistrer_reponse(True)
        assert hist.boite == 2

    def test_wrong_answer_resets_to_box_1(self, eleve, question_qcm):
        """Teste: Une mauvaise réponse réinitialise la question à la boîte 1
        Raison: Principe Leitner — l'erreur impose de recommencer le cycle de mémorisation
        Features: leitner, UserQuestionHistorique, enregistrer_reponse
        Criticité: haute"""
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=3,
            prochaine_revision=date.today(),
        )
        hist.enregistrer_reponse(False)
        assert hist.boite == 1

    def test_max_box_is_5(self, eleve, question_qcm):
        """Teste: La boîte maximale est 5 — une bonne réponse en boîte 5 ne dépasse pas 5
        Raison: Éviter un dépassement de borne qui casserait le calcul des intervalles
        Features: leitner, UserQuestionHistorique, enregistrer_reponse
        Criticité: moyenne"""
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=5,
            prochaine_revision=date.today(),
        )
        hist.enregistrer_reponse(True)
        assert hist.boite == 5

    def test_prochaine_revision_calculated_correctly(self, eleve, question_qcm):
        """Teste: La date de prochaine révision correspond à l'intervalle Leitner de la nouvelle boîte
        Raison: Un mauvais calcul d'intervalle fausse tout le planning de révision de l'élève
        Features: leitner, LEITNER_INTERVALLES, prochaine_revision
        Criticité: haute"""
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
        """Teste: Une mauvaise réponse remet l'intervalle de révision à celui de la boîte 1
        Raison: Vérifie la cohérence entre le reset de boîte et le recalcul de prochaine_revision
        Features: leitner, LEITNER_INTERVALLES, prochaine_revision
        Criticité: haute"""
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
        """Teste: Le premier appel quiz d'un utilisateur n'est pas limité
        Raison: Vérifie que le rate limiter ne bloque pas un usage normal
        Features: rate_limiting, _check_quiz_rate_limit
        Criticité: moyenne"""
        from progress.views import _check_quiz_rate_limit
        from django.core.cache import cache
        cache.clear()
        assert _check_quiz_rate_limit(9999) is False

    def test_29th_call_not_limited(self):
        """Teste: Le 29ème appel dans la fenêtre n'est pas encore limité
        Raison: Vérifie que la limite est bien à 30 et non avant
        Features: rate_limiting, _check_quiz_rate_limit
        Criticité: moyenne"""
        from progress.views import _check_quiz_rate_limit
        from django.core.cache import cache
        cache.clear()
        for _ in range(29):
            result = _check_quiz_rate_limit(8888)
        assert result is False

    def test_30th_call_is_limited(self):
        """Teste: Le 31ème appel est bloqué après 30 requêtes dans la fenêtre
        Raison: Protège contre le brute-force de quiz — seuil de 30 req/min
        Features: rate_limiting, _check_quiz_rate_limit
        Criticité: haute"""
        from progress.views import _check_quiz_rate_limit
        from django.core.cache import cache
        cache.clear()
        for _ in range(30):
            _check_quiz_rate_limit(7777)
        assert _check_quiz_rate_limit(7777) is True

    def test_different_users_independent_counters(self):
        """Teste: Les compteurs de rate limit sont indépendants par utilisateur
        Raison: Un utilisateur limité ne doit pas bloquer les autres — isolation des compteurs
        Features: rate_limiting, _check_quiz_rate_limit
        Criticité: haute"""
        from progress.views import _check_quiz_rate_limit
        from django.core.cache import cache
        cache.clear()
        for _ in range(30):
            _check_quiz_rate_limit(6666)
        # user 5555 is not limited even though 6666 is
        assert _check_quiz_rate_limit(5555) is False

    def test_soumettre_quiz_returns_429_when_limited(self, client, eleve, lecon, quiz, question_qcm):
        """Teste: La vue soumettre_quiz retourne HTTP 429 quand le rate limit est atteint
        Raison: Vérifie l'intégration du rate limiter dans la vue de soumission de quiz
        Features: rate_limiting, soumettre_quiz, HTTP 429
        Criticité: haute"""
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
        """Teste: La vue soumettre_quiz_chapitre retourne HTTP 429 quand le rate limit est atteint
        Raison: Vérifie l'intégration du rate limiter dans la vue de soumission de quiz chapitre
        Features: rate_limiting, soumettre_quiz_chapitre, HTTP 429
        Criticité: haute"""
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
        """Teste: La sauvegarde d'une note retourne HTTP 200
        Raison: Vérifie que l'endpoint HTMX de sauvegarde de note fonctionne
        Features: notes, sauvegarder_note, HTMX
        Criticité: moyenne"""
        client.force_login(eleve)
        response = client.post(
            reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}),
            {"contenu": "Mes notes importantes"},
        )
        assert response.status_code == 200

    def test_second_save_updates_existing_note(self, client, eleve, lecon):
        """Teste: La deuxième sauvegarde met à jour la note existante au lieu d'en créer une nouvelle
        Raison: Garantit le respect de unique_together (user, lecon) — pas de doublons en base
        Features: notes, sauvegarder_note, UserNote, unique_together
        Criticité: haute"""
        from progress.models import UserNote
        client.force_login(eleve)
        client.post(reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}), {"contenu": "v1"})
        client.post(reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}), {"contenu": "v2"})
        assert UserNote.objects.filter(user=eleve, lecon=lecon).count() == 1
        assert UserNote.objects.get(user=eleve, lecon=lecon).contenu == "v2"

    def test_content_truncated_to_2000_chars(self, client, eleve, lecon):
        """Teste: Le contenu de la note est tronqué à 2000 caractères maximum
        Raison: Protège contre l'injection de données volumineuses en base
        Features: notes, sauvegarder_note, validation
        Criticité: haute"""
        from progress.models import UserNote
        client.force_login(eleve)
        client.post(
            reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}),
            {"contenu": "x" * 2001},
        )
        note = UserNote.objects.get(user=eleve, lecon=lecon)
        assert len(note.contenu) == 2000

    def test_empty_post_saves_empty_string(self, client, eleve, lecon):
        """Teste: Un POST avec contenu vide sauvegarde une chaîne vide
        Raison: L'élève doit pouvoir effacer ses notes sans erreur
        Features: notes, sauvegarder_note, edge-case
        Criticité: basse"""
        from progress.models import UserNote
        client.force_login(eleve)
        client.post(reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}), {"contenu": ""})
        note = UserNote.objects.get(user=eleve, lecon=lecon)
        assert note.contenu == ""

    def test_anonymous_post_redirects(self, client, lecon):
        """Teste: Un utilisateur non connecté est redirigé lors de la sauvegarde d'une note
        Raison: Les notes sont privées — un accès anonyme doit être bloqué par @login_required
        Features: notes, sauvegarder_note, authentification
        Criticité: haute"""
        response = client.post(
            reverse("sauvegarder_note", kwargs={"lecon_pk": lecon.pk}),
            {"contenu": "test"},
        )
        assert response.status_code == 302

    def test_two_users_can_each_have_note_on_same_lecon(self, db, lecon):
        """Teste: Deux utilisateurs peuvent chacun avoir une note sur la même leçon
        Raison: Vérifie que unique_together porte sur (user, lecon) et non lecon seule
        Features: notes, UserNote, unique_together, isolation utilisateurs
        Criticité: haute"""
        from progress.models import UserNote
        u1 = CustomUser.objects.create_user(email="u1@test.com", password="pass", prenom="A", nom="B", role="eleve", niveau="terminale")
        u2 = CustomUser.objects.create_user(email="u2@test.com", password="pass", prenom="C", nom="D", role="eleve", niveau="terminale")
        UserNote.objects.create(user=u1, lecon=lecon, contenu="note u1")
        UserNote.objects.create(user=u2, lecon=lecon, contenu="note u2")
        assert UserNote.objects.filter(lecon=lecon).count() == 2

    def test_deleting_lecon_cascades_to_notes(self, db, lecon):
        """Teste: La suppression d'une leçon supprime en cascade les notes associées
        Raison: Évite les notes orphelines en base — intégrité référentielle via CASCADE
        Features: notes, UserNote, CASCADE, intégrité données
        Criticité: haute"""
        from progress.models import UserNote
        u = CustomUser.objects.create_user(email="cascade@test.com", password="pass", prenom="C", nom="D", role="eleve", niveau="terminale")
        UserNote.objects.create(user=u, lecon=lecon, contenu="to be deleted")
        lecon.delete()
        assert UserNote.objects.filter(contenu="to be deleted").count() == 0

    def test_lecon_view_context_contains_note(self, client, eleve, lecon, chapitre):
        """Teste: Le contexte de la vue leçon contient la note de l'utilisateur
        Raison: Le panneau de notes dans lecon.html dépend de cette variable de contexte
        Features: notes, lecon_view, contexte template
        Criticité: moyenne"""
        from progress.models import UserNote, ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        lecon.gratuit = True
        lecon.save(update_fields=["gratuit"])
        note = UserNote.objects.create(user=eleve, lecon=lecon, contenu="noter quelque chose")
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon.pk}))
        assert response.context["note"] == note


# ---- Terminer leçon tests ----

class TestTerminerLecon:
    def test_terminer_lecon_requires_post(self, client, eleve, lecon):
        """Teste: La vue terminer_lecon rejette les requêtes GET avec HTTP 405
        Raison: Seul POST doit modifier l'état de progression — empêche les modifications accidentelles via navigation
        Features: terminer_lecon, méthodes HTTP
        Criticité: moyenne"""
        client.force_login(eleve)
        response = client.get(reverse("terminer_lecon", kwargs={"lecon_pk": lecon.pk}))
        assert response.status_code == 405

    def test_terminer_lecon_requires_login(self, client, lecon):
        """Teste: Un utilisateur non connecté est redirigé vers la connexion
        Raison: La progression est personnelle — @login_required doit bloquer les accès anonymes
        Features: terminer_lecon, authentification, @login_required
        Criticité: haute"""
        response = client.post(reverse("terminer_lecon", kwargs={"lecon_pk": lecon.pk}))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    def test_terminer_lecon_wrong_niveau_returns_403(self, client, eleve, matiere):
        """Teste: Un élève de terminale ne peut pas terminer une leçon de seconde (HTTP 403)
        Raison: Un élève ne doit modifier que la progression de son propre niveau — contrôle d'accès par niveau
        Features: terminer_lecon, filtrage niveau, autorisation
        Criticité: haute"""
        chap_sec = Chapitre.objects.create(matiere=matiere, niveau="seconde", titre="Sec", ordre=10)
        lecon_sec = Lecon.objects.create(chapitre=chap_sec, titre="Sec L", contenu="c", ordre=1)
        client.force_login(eleve)
        response = client.post(reverse("terminer_lecon", kwargs={"lecon_pk": lecon_sec.pk}))
        assert response.status_code == 403

    def test_terminer_lecon_marks_termine(self, client, eleve, lecon):
        """Teste: Le POST marque la leçon comme terminée avec date de complétion
        Raison: Cœur de la fonctionnalité — la progression doit être enregistrée correctement en base
        Features: terminer_lecon, UserProgression, statut, termine_le
        Criticité: haute"""
        client.force_login(eleve)
        client.post(reverse("terminer_lecon", kwargs={"lecon_pk": lecon.pk}))
        prog = UserProgression.objects.get(user=eleve, lecon=lecon)
        assert prog.statut == StatutLeconChoices.TERMINE
        assert prog.termine_le is not None

    def test_terminer_lecon_idempotent(self, client, eleve, lecon):
        """Teste: Terminer deux fois la même leçon ne crée pas de doublon en base
        Raison: L'idempotence protège contre les double-clics et les requêtes réseau rejouées
        Features: terminer_lecon, UserProgression, idempotence
        Criticité: haute"""
        client.force_login(eleve)
        client.post(reverse("terminer_lecon", kwargs={"lecon_pk": lecon.pk}))
        client.post(reverse("terminer_lecon", kwargs={"lecon_pk": lecon.pk}))
        assert UserProgression.objects.filter(user=eleve, lecon=lecon).count() == 1
        prog = UserProgression.objects.get(user=eleve, lecon=lecon)
        assert prog.statut == StatutLeconChoices.TERMINE

    def test_terminer_lecon_htmx_returns_hx_redirect(self, client, eleve, lecon):
        """Teste: Une requête HTMX reçoit un header HX-Redirect dans la réponse
        Raison: HTMX a besoin de HX-Redirect pour naviguer côté client après soumission
        Features: terminer_lecon, HTMX, HX-Redirect
        Criticité: moyenne"""
        client.force_login(eleve)
        response = client.post(
            reverse("terminer_lecon", kwargs={"lecon_pk": lecon.pk}),
            HTTP_HX_REQUEST="true",
        )
        assert "HX-Redirect" in response


# ---- Soumettre quiz e2e flow tests ----

class TestSoumettreQuizFlow:
    def test_soumettre_quiz_requires_post(self, client, eleve, lecon, quiz, question_qcm):
        """Teste: La vue soumettre_quiz rejette les requêtes GET avec HTTP 405
        Raison: La soumission de quiz modifie les données — seul POST est autorisé
        Features: soumettre_quiz, méthodes HTTP
        Criticité: moyenne"""
        from django.core.cache import cache
        cache.clear()
        client.force_login(eleve)
        response = client.get(reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}))
        assert response.status_code == 405

    def test_soumettre_quiz_creates_resultat(self, client, eleve, lecon, quiz, question_qcm):
        """Teste: La soumission d'un quiz crée un enregistrement UserQuizResultat en base
        Raison: Le résultat doit être persisté pour le suivi de progression et le tableau de bord
        Features: soumettre_quiz, UserQuizResultat, progression
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        client.force_login(eleve)
        client.post(
            reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}),
            {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "0"},
        )
        assert UserQuizResultat.objects.filter(user=eleve, quiz=quiz).exists()

    def test_soumettre_quiz_keeps_best_score(self, client, eleve, lecon, quiz, question_qcm):
        """Teste: Le meilleur score est conservé quand une tentative inférieure suit une réussite
        Raison: Le score ne doit jamais régresser — politique du meilleur score pour la motivation
        Features: soumettre_quiz, UserQuizResultat, meilleur score
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        client.force_login(eleve)
        url = reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk})
        # First submit: 100%
        client.post(url, {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "0"})
        # Second submit: 0%
        client.post(url, {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "2"})
        resultat = UserQuizResultat.objects.get(user=eleve, quiz=quiz)
        assert resultat.score == 100.0

    def test_soumettre_quiz_updates_if_higher(self, client, eleve, lecon, quiz, question_qcm):
        """Teste: Le score est mis à jour quand une nouvelle tentative est meilleure
        Raison: Le système doit permettre l'amélioration — un score bas ne doit pas bloquer la progression
        Features: soumettre_quiz, UserQuizResultat, mise à jour score
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        client.force_login(eleve)
        url = reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk})
        # First submit: 0%
        client.post(url, {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "2"})
        # Second submit: 100%
        client.post(url, {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "0"})
        resultat = UserQuizResultat.objects.get(user=eleve, quiz=quiz)
        assert resultat.score == 100.0

    def test_soumettre_quiz_marks_progression_termine(self, client, eleve, lecon, quiz, question_qcm):
        """Teste: La soumission du quiz marque automatiquement la leçon comme terminée
        Raison: La progression doit avancer automatiquement après un quiz — cohérence du parcours
        Features: soumettre_quiz, UserProgression, statut, terminer_lecon
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        client.force_login(eleve)
        client.post(
            reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}),
            {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "0"},
        )
        prog = UserProgression.objects.get(user=eleve, lecon=lecon)
        assert prog.statut == StatutLeconChoices.TERMINE

    def test_soumettre_quiz_creates_leitner_history(self, client, eleve, lecon, quiz, question_qcm):
        """Teste: La soumission du quiz crée un historique Leitner pour la révision espacée
        Raison: Chaque réponse doit alimenter le système de répétition espacée pour les révisions futures
        Features: soumettre_quiz, UserQuestionHistorique, Leitner, révision espacée
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        client.force_login(eleve)
        client.post(
            reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}),
            {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "0"},
        )
        assert UserQuestionHistorique.objects.filter(user=eleve, question=question_qcm).exists()

    def test_soumettre_quiz_renders_resultat_template(self, client, eleve, lecon, quiz, question_qcm):
        """Teste: La soumission retourne HTTP 200 avec corrections et score dans le contexte
        Raison: Le template quiz_resultat.html dépend de ces variables pour afficher le feedback
        Features: soumettre_quiz, quiz_resultat, contexte template
        Criticité: moyenne"""
        from django.core.cache import cache
        cache.clear()
        client.force_login(eleve)
        response = client.post(
            reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}),
            {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "0"},
        )
        assert response.status_code == 200
        assert "corrections" in response.context
        assert "score" in response.context

    def test_soumettre_quiz_empty_question_ids_redirects(self, client, eleve, lecon, quiz, question_qcm):
        """Teste: Un POST avec question_ids vide retombe sur toutes les questions et retourne HTTP 200
        Raison: Gestion du cas limite où le formulaire est soumis sans IDs — pas de crash serveur
        Features: soumettre_quiz, edge-case, robustesse
        Criticité: basse"""
        from django.core.cache import cache
        cache.clear()
        client.force_login(eleve)
        response = client.post(
            reverse("soumettre_quiz", kwargs={"lecon_pk": lecon.pk}),
            {"question_ids": ""},
        )
        # With empty question_ids, it falls back to all questions and renders result
        assert response.status_code == 200


# ---- Soumettre quiz chapitre e2e flow tests ----

class TestSoumettreQuizChapitreFlow:
    def test_chapitre_quiz_creates_resultat(self, client, eleve, chapitre, lecon, quiz):
        """Teste: La soumission du quiz chapitre crée un UserChapitreQuizResultat en base
        Raison: Le résultat du quiz chapitre est nécessaire pour le déblocage des chapitres suivants
        Features: soumettre_quiz_chapitre, UserChapitreQuizResultat, progression
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        questions = _make_questions(quiz, 5)
        client.force_login(eleve)
        data = {"question_ids": ",".join(str(q.id) for q in questions)}
        for q in questions:
            data[f"question_{q.id}"] = "0"
        client.post(reverse("soumettre_quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}), data)
        assert UserChapitreQuizResultat.objects.filter(user=eleve, chapitre=chapitre).exists()

    def test_chapitre_quiz_keeps_best_score(self, client, eleve, chapitre, lecon, quiz):
        """Teste: Le meilleur score du quiz chapitre est conservé entre les tentatives
        Raison: Comme pour les quiz leçon, le score ne doit jamais régresser
        Features: soumettre_quiz_chapitre, UserChapitreQuizResultat, meilleur score
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        questions = _make_questions(quiz, 5)
        client.force_login(eleve)
        url = reverse("soumettre_quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk})
        # First submit: 100%
        data_100 = {"question_ids": ",".join(str(q.id) for q in questions)}
        for q in questions:
            data_100[f"question_{q.id}"] = "0"
        client.post(url, data_100)
        # Second submit: 0%
        data_0 = {"question_ids": ",".join(str(q.id) for q in questions)}
        for q in questions:
            data_0[f"question_{q.id}"] = "3"
        client.post(url, data_0)
        resultat = UserChapitreQuizResultat.objects.get(user=eleve, chapitre=chapitre)
        assert resultat.score == 100.0

    def test_chapitre_quiz_pass_triggers_unlock(self, client, eleve, chapitre, chapitre_suivant, lecon, quiz):
        """Teste: Réussir le quiz chapitre (≥80%) débloque le chapitre suivant
        Raison: Le déblocage progressif est le cœur du système de progression — doit fonctionner correctement
        Features: soumettre_quiz_chapitre, ChapitreDebloque, déblocage, progression
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        questions = _make_questions(quiz, 5)
        client.force_login(eleve)
        data = {"question_ids": ",".join(str(q.id) for q in questions)}
        for q in questions:
            data[f"question_{q.id}"] = "0"
        client.post(reverse("soumettre_quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}), data)
        resultat = UserChapitreQuizResultat.objects.get(user=eleve, chapitre=chapitre)
        assert resultat.passe is True
        assert ChapitreDebloque.objects.filter(user=eleve, chapitre=chapitre_suivant).exists()

    def test_chapitre_quiz_fail_no_unlock(self, client, eleve, chapitre, chapitre_suivant, lecon, quiz):
        """Teste: Échouer le quiz chapitre (<80%) ne débloque pas le chapitre suivant
        Raison: Le déblocage ne doit se faire qu'en cas de réussite — évite l'accès non mérité au contenu
        Features: soumettre_quiz_chapitre, ChapitreDebloque, échec, blocage
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        questions = _make_questions(quiz, 5)
        client.force_login(eleve)
        data = {"question_ids": ",".join(str(q.id) for q in questions)}
        for q in questions:
            data[f"question_{q.id}"] = "3"  # All wrong
        client.post(reverse("soumettre_quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}), data)
        resultat = UserChapitreQuizResultat.objects.get(user=eleve, chapitre=chapitre)
        assert resultat.passe is False
        assert not ChapitreDebloque.objects.filter(user=eleve, chapitre=chapitre_suivant).exists()

    def test_chapitre_quiz_empty_ids_redirects(self, client, eleve, chapitre, lecon, quiz):
        """Teste: Un POST avec question_ids vide redirige (HTTP 302)
        Raison: Gestion du cas limite — soumission sans questions ne doit pas créer de résultat invalide
        Features: soumettre_quiz_chapitre, edge-case, robustesse
        Criticité: basse"""
        from django.core.cache import cache
        cache.clear()
        client.force_login(eleve)
        response = client.post(
            reverse("soumettre_quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}),
            {"question_ids": ""},
        )
        assert response.status_code == 302


# ---- _enregistrer_historique_questions unit tests ----

class TestEnregistrerHistoriqueQuestions:
    def test_creates_new_historique(self, eleve, question_qcm):
        """Teste: Une bonne réponse crée un historique Leitner en boîte 2
        Raison: La première bonne réponse doit placer la question en boîte 2 (progression initiale)
        Features: _enregistrer_historique_questions, UserQuestionHistorique, Leitner
        Criticité: haute"""
        corrections_correct = [{"question": question_qcm, "correct": True}]
        _enregistrer_historique_questions(eleve, corrections_correct)
        hist = UserQuestionHistorique.objects.get(user=eleve, question=question_qcm)
        assert hist.boite == 2

    def test_updates_existing_historique(self, eleve, question_qcm):
        """Teste: Une bonne réponse sur un historique existant incrémente la boîte Leitner
        Raison: La progression dans les boîtes est essentielle au système de répétition espacée
        Features: _enregistrer_historique_questions, UserQuestionHistorique, Leitner, progression boîte
        Criticité: haute"""
        hist = UserQuestionHistorique.objects.create(
            user=eleve, question=question_qcm, boite=2, prochaine_revision=date.today(),
        )
        corrections = [{"question": question_qcm, "correct": True}]
        _enregistrer_historique_questions(eleve, corrections)
        hist.refresh_from_db()
        assert hist.boite == 3

    def test_wrong_answer_resets_to_box_1(self, eleve, question_qcm):
        """Teste: Une mauvaise réponse remet la question en boîte 1 (reset Leitner)
        Raison: Le principe Leitner impose un retour en boîte 1 sur erreur — révision plus fréquente
        Features: _enregistrer_historique_questions, UserQuestionHistorique, Leitner, reset boîte
        Criticité: haute"""
        hist = UserQuestionHistorique.objects.create(
            user=eleve, question=question_qcm, boite=3, prochaine_revision=date.today(),
        )
        corrections = [{"question": question_qcm, "correct": False}]
        _enregistrer_historique_questions(eleve, corrections)
        hist.refresh_from_db()
        assert hist.boite == 1


# ---- Soumettre révisions tests ----

class TestSoumettreRevisions:
    def test_soumettre_revisions_requires_post(self, client, eleve, quiz, question_qcm):
        """Teste: GET sur soumettre_revisions redirige vers la page révisions
        Raison: Seul POST modifie les données Leitner — GET doit rediriger
        Features: soumettre_revisions, méthodes HTTP, redirect
        Criticité: moyenne"""
        client.force_login(eleve)
        response = client.get(reverse("soumettre_revisions"))
        assert response.status_code == 302

    def test_soumettre_revisions_requires_login(self, client, question_qcm):
        """Teste: Un utilisateur non connecté est redirigé vers la connexion
        Raison: Les révisions sont personnelles — @login_required doit bloquer les accès anonymes
        Features: soumettre_revisions, authentification, @login_required
        Criticité: haute"""
        response = client.post(
            reverse("soumettre_revisions"),
            {"question_ids": str(question_qcm.id), f"question_{question_qcm.id}": "0"},
        )
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    def test_soumettre_revisions_updates_leitner_boxes(self, client, eleve, quiz, question_qcm):
        """Teste: Une bonne réponse en révision fait monter la boîte Leitner
        Raison: Le mécanisme de progression Leitner doit fonctionner via la vue soumettre_revisions
        Features: soumettre_revisions, Leitner, UserQuestionHistorique, boîte
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=2,
            prochaine_revision=date.today() - timedelta(days=1),
        )
        client.force_login(eleve)
        client.post(
            reverse("soumettre_revisions"),
            {
                "question_ids": str(question_qcm.id),
                f"question_{question_qcm.id}": "0",
            },
        )
        hist.refresh_from_db()
        assert hist.boite == 3

    def test_soumettre_revisions_wrong_answer_resets_box(self, client, eleve, quiz, question_qcm):
        """Teste: Une mauvaise réponse en révision remet la boîte Leitner à 1
        Raison: Principe Leitner — l'erreur impose un retour en boîte 1
        Features: soumettre_revisions, Leitner, UserQuestionHistorique, reset boîte
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        hist = UserQuestionHistorique.objects.create(
            user=eleve,
            question=question_qcm,
            boite=4,
            prochaine_revision=date.today() - timedelta(days=1),
        )
        client.force_login(eleve)
        client.post(
            reverse("soumettre_revisions"),
            {
                "question_ids": str(question_qcm.id),
                f"question_{question_qcm.id}": "3",  # mauvaise réponse
            },
        )
        hist.refresh_from_db()
        assert hist.boite == 1

    def test_soumettre_revisions_rate_limited(self, client, eleve, quiz, question_qcm):
        """Teste: La vue soumettre_revisions retourne HTTP 429 quand le rate limit est atteint
        Raison: Protège contre le brute-force de révisions — seuil de 30 req/min
        Features: soumettre_revisions, rate_limiting, HTTP 429
        Criticité: haute"""
        from django.core.cache import cache
        cache.clear()
        cache.set(f"quiz_rate_{eleve.id}", 30, timeout=60)
        client.force_login(eleve)
        response = client.post(
            reverse("soumettre_revisions"),
            {
                "question_ids": str(question_qcm.id),
                f"question_{question_qcm.id}": "0",
            },
        )
        assert response.status_code == 429
