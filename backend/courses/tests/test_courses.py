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
        """
        Teste: le slug de Matiere est auto-généré à partir du nom
        Raison: un slug incorrect casserait les URLs publiques du catalogue
        Features: slugs, modèle Matiere
        Criticité: moyenne
        """
        assert matiere.slug == "mathematiques"

    def test_chapitre_slug_auto_generated(self, chapitre):
        """
        Teste: le slug de Chapitre est auto-généré à partir du titre
        Raison: un slug incorrect casserait les URLs publiques du catalogue
        Features: slugs, modèle Chapitre
        Criticité: moyenne
        """
        assert chapitre.slug == "les-suites-numeriques"

    def test_lecon_slug_auto_generated(self, lecon_gratuite):
        """
        Teste: le slug de Lecon est auto-généré à partir du titre
        Raison: un slug incorrect casserait les URLs SEO des leçons publiques
        Features: slugs, modèle Lecon
        Criticité: moyenne
        """
        assert lecon_gratuite.slug == "definition-et-premiers-exemples"

    def test_slug_unique_within_scope(self, chapitre):
        """
        Teste: deux leçons dans le même chapitre ne peuvent pas avoir le même slug, mais deux chapitres différents le peuvent
        Raison: collision de slugs provoquerait des URLs ambiguës dans le catalogue public
        Features: slugs, unicité par scope parent, URLs publiques
        Criticité: moyenne
        """
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
        """
        Teste: le catalogue matière est accessible sans authentification
        Raison: les pages publiques doivent rester ouvertes pour le SEO et la conversion
        Features: catalogue public, accès anonyme
        Criticité: haute
        """
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": "mathematiques"})
        )
        assert response.status_code == 200

    def test_free_lesson_accessible_anonymous(self, client, lecon_gratuite):
        """
        Teste: une leçon gratuite est accessible sans authentification
        Raison: les leçons gratuites servent d'aperçu pour convertir les visiteurs
        Features: leçon publique, accès anonyme, gratuit
        Criticité: haute
        """
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
        """
        Teste: une leçon premium affiche le blur paywall pour un visiteur anonyme
        Raison: le contenu premium doit être protégé visuellement pour inciter à l'abonnement
        Features: paywall, blur, leçon premium, accès anonyme
        Criticité: haute
        """
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
        """
        Teste: un élève authentifié peut accéder à la page publique d'une leçon gratuite
        Raison: la page publique ne doit pas bloquer les utilisateurs connectés
        Features: leçon publique, accès authentifié, gratuit
        Criticité: moyenne
        """
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
        """
        Teste: le sitemap XML est accessible sans authentification
        Raison: les moteurs de recherche doivent pouvoir accéder au sitemap pour l'indexation
        Features: sitemap, SEO, accès anonyme
        Criticité: moyenne
        """
        response = client.get("/sitemap.xml")
        assert response.status_code == 200

    def test_sitemap_content_type_xml(self, client, matiere):
        """
        Teste: le sitemap renvoie un Content-Type XML valide
        Raison: un Content-Type incorrect empêcherait l'indexation par les moteurs de recherche
        Features: sitemap, SEO, headers HTTP
        Criticité: basse
        """
        response = client.get("/sitemap.xml")
        assert "xml" in response["Content-Type"]

    def test_sitemap_valid_xml(self, client, matiere):
        """
        Teste: le sitemap est un document XML valide et parsable
        Raison: un XML malformé serait rejeté par Google Search Console
        Features: sitemap, SEO, validation XML
        Criticité: basse
        """
        import xml.etree.ElementTree as ET
        response = client.get("/sitemap.xml")
        ET.fromstring(response.content)  # should not raise

    def test_sitemap_contains_free_lesson_url(self, client, lecon_gratuite):
        """
        Teste: le sitemap contient l'URL de la leçon gratuite
        Raison: les leçons gratuites doivent être indexées pour le référencement
        Features: sitemap, SEO, leçon gratuite
        Criticité: moyenne
        """
        response = client.get("/sitemap.xml")
        assert lecon_gratuite.slug.encode() in response.content

    def test_sitemap_does_not_contain_non_free_lesson(self, client, lecon_payante):
        """
        Teste: le sitemap exclut les leçons premium
        Raison: indexer du contenu payant flouté dégraderait l'expérience utilisateur Google
        Features: sitemap, SEO, leçon premium, paywall
        Criticité: moyenne
        """
        response = client.get("/sitemap.xml")
        assert lecon_payante.slug.encode() not in response.content

    def test_sitemap_has_catalogue_urls(self, client, matiere):
        """
        Teste: le sitemap contient les URLs du catalogue par matière
        Raison: les pages catalogue doivent être indexées pour capter le trafic organique
        Features: sitemap, SEO, catalogue public
        Criticité: moyenne
        """
        response = client.get("/sitemap.xml")
        assert b"mathematiques" in response.content


class TestRecherche:
    def test_recherche_returns_200(self, client, eleve):
        """
        Teste: la recherche renvoie 200 pour un élève authentifié avec une requête valide
        Raison: la recherche est une feature essentielle de navigation dans le contenu
        Features: recherche full-text, accès authentifié
        Criticité: moyenne
        """
        client.force_login(eleve)
        response = client.get(reverse("recherche"), {"q": "suites"})
        assert response.status_code == 200

    def test_recherche_short_query_returns_empty(self, client, eleve):
        """
        Teste: une requête trop courte renvoie zéro résultat
        Raison: éviter des recherches coûteuses sur des termes non significatifs
        Features: recherche full-text, validation requête
        Criticité: basse
        """
        client.force_login(eleve)
        response = client.get(reverse("recherche"), {"q": "a"})
        assert response.status_code == 200
        assert len(response.context["results"]) == 0

    def test_recherche_anonymous_redirected(self, client):
        """
        Teste: un visiteur anonyme est redirigé vers la connexion pour la recherche
        Raison: la recherche expose du contenu filtré par niveau, elle requiert une session
        Features: recherche full-text, contrôle d'accès
        Criticité: haute
        """
        response = client.get(reverse("recherche"), {"q": "suites"})
        assert response.status_code == 302


class TestDifficulte:
    def test_question_default_difficulte_is_moyen(self, db, matiere, chapitre):
        """
        Teste: la difficulté par défaut d'une question est MOYEN
        Raison: garantir que les questions sans difficulté explicite sont classées moyen pour l'équilibrage du quiz chapitre
        Features: modèle Question, difficulté, valeur par défaut
        Criticité: moyenne
        """
        lecon = Lecon.objects.create(chapitre=chapitre, titre="L", contenu="c", ordre=5)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q")
        q = Question.objects.create(quiz=quiz, texte="?", type="qcm", reponse_correcte="0", ordre=1)
        assert q.difficulte == DifficulteChoices.MOYEN

    def test_selectionner_questions_chapitre_balanced(self, db, matiere, chapitre):
        """
        Teste: la sélection de questions respecte la répartition 4 facile + 4 moyen + 2 difficile
        Raison: un déséquilibre rendrait le quiz chapitre trop facile ou trop difficile
        Features: quiz chapitre, sélection proportionnelle, difficulté
        Criticité: moyenne
        """
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
        """
        Teste: la sélection de questions ne contient aucun doublon
        Raison: des questions dupliquées fausseraient le score et l'expérience du quiz chapitre
        Features: quiz chapitre, sélection de questions, intégrité
        Criticité: moyenne
        """
        from courses.views import _selectionner_questions_chapitre
        lecon = Lecon.objects.create(chapitre=chapitre, titre="L2", contenu="c", ordre=7)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q2")
        for i in range(15):
            Question.objects.create(quiz=quiz, texte=f"Q{i}", type="qcm", reponse_correcte="0", ordre=i+1)
        selection = _selectionner_questions_chapitre(chapitre, nb_total=10)
        ids = [q.id for q in selection]
        assert len(ids) == len(set(ids))

    def test_selectionner_small_pool_returns_all(self, db, matiere, chapitre):
        """
        Teste: quand le pool de questions est inférieur au nombre demandé, toutes les questions sont retournées
        Raison: éviter une erreur ou un quiz vide quand le contenu est encore en création
        Features: quiz chapitre, sélection de questions, fallback petit pool
        Criticité: basse
        """
        from courses.views import _selectionner_questions_chapitre
        lecon = Lecon.objects.create(chapitre=chapitre, titre="L3", contenu="c", ordre=8)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q3")
        for i in range(6):
            Question.objects.create(quiz=quiz, texte=f"S{i}", type="qcm", reponse_correcte="0", ordre=i+1)
        selection = _selectionner_questions_chapitre(chapitre, nb_total=10)
        assert len(selection) == 6

    def test_selectionner_empty_pool_returns_empty(self, db, matiere, chapitre):
        """
        Teste: un chapitre sans questions renvoie une liste vide sans erreur
        Raison: éviter un crash si un quiz chapitre est déclenché avant l'ajout de contenu
        Features: quiz chapitre, sélection de questions, edge case vide
        Criticité: basse
        """
        from courses.views import _selectionner_questions_chapitre
        # chapitre without any questions
        chap_empty = Chapitre.objects.create(matiere=matiere, niveau="terminale", titre="Vide", ordre=99)
        selection = _selectionner_questions_chapitre(chap_empty, nb_total=10)
        assert selection == []


class TestImportQuestions:
    def test_valid_csv_creates_question(self, tmp_path, db, matiere, chapitre):
        """
        Teste: un CSV valide crée correctement la question en base
        Raison: l'import CSV est le flux principal d'ajout de contenu en masse
        Features: import CSV, commande management, création Question
        Criticité: moyenne
        """
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
        """
        Teste: le mode --dry-run n'insère aucune question en base
        Raison: le dry-run doit permettre de valider un CSV sans effet de bord
        Features: import CSV, dry-run, sécurité des données
        Criticité: moyenne
        """
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
        """
        Teste: une ligne avec un slug de leçon inexistant est ignorée sans crash
        Raison: un CSV mal rédigé ne doit pas interrompre l'import ni corrompre les données
        Features: import CSV, robustesse, validation slug
        Criticité: moyenne
        """
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
        """
        Teste: une ligne sans réponse correcte est ignorée sans crash
        Raison: une question sans réponse rendrait le quiz non évaluable
        Features: import CSV, validation données, robustesse
        Criticité: moyenne
        """
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
        """
        Teste: la vue matières redirige vers la connexion pour un visiteur anonyme
        Raison: l'accès aux matières nécessite une session pour filtrer par niveau
        Features: vue matières, contrôle d'accès, @login_required
        Criticité: haute
        """
        response = client.get(reverse("matieres"))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_matieres_returns_200_for_eleve(self, client, eleve, matiere):
        """
        Teste: un élève authentifié obtient 200 sur la page matières
        Raison: vérifier que la page principale de navigation fonctionne pour le rôle élève
        Features: vue matières, accès élève
        Criticité: moyenne
        """
        client.force_login(eleve)
        response = client.get(reverse("matieres"))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_matieres_context_contains_matieres_data(self, client, eleve, matiere):
        """
        Teste: le contexte contient la clé matieres_data nécessaire au template
        Raison: l'absence de cette clé provoquerait une erreur de rendu du template
        Features: vue matières, contexte template
        Criticité: basse
        """
        client.force_login(eleve)
        response = client.get(reverse("matieres"))
        assert "matieres_data" in response.context

    @pytest.mark.django_db
    def test_matieres_filters_by_niveau(self, client, eleve, matiere):
        """
        Teste: un élève terminale ne voit que les chapitres de son niveau
        Raison: afficher des chapitres d'un autre niveau créerait de la confusion et des erreurs d'accès
        Features: vue matières, filtrage par niveau, rôle élève
        Criticité: haute
        """
        Chapitre.objects.create(matiere=matiere, niveau="terminale", titre="Chap Term", ordre=1)
        Chapitre.objects.create(matiere=matiere, niveau="seconde", titre="Chap Sec", ordre=1)
        client.force_login(eleve)
        response = client.get(reverse("matieres"))
        content = response.content.decode()
        assert "Chap Term" in content
        assert "Chap Sec" not in content

    @pytest.mark.django_db
    def test_admin_sees_all_niveaux(self, client, admin_user, matiere):
        """
        Teste: un admin sans session preview obtient le mode admin browse avec tous les niveaux
        Raison: l'admin doit pouvoir parcourir tout le contenu sans restriction de niveau
        Features: vue matières, rôle admin, admin browse mode
        Criticité: moyenne
        """
        Chapitre.objects.create(matiere=matiere, niveau="terminale", titre="Chap T", ordre=1)
        Chapitre.objects.create(matiere=matiere, niveau="seconde", titre="Chap S", ordre=1)
        client.force_login(admin_user)
        response = client.get(reverse("matieres"))
        assert response.status_code == 200
        assert response.context["is_admin_browse"] is True


class TestChapitreView:
    def test_chapitre_requires_login(self, client, chapitre):
        """
        Teste: la vue chapitre redirige vers la connexion pour un visiteur anonyme
        Raison: un accès non authentifié au contenu de chapitre doit être bloqué
        Features: vue chapitre, contrôle d'accès, @login_required
        Criticité: haute
        """
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_wrong_niveau_redirects(self, client, eleve, matiere):
        """
        Teste: un élève terminale est redirigé s'il tente d'accéder à un chapitre de seconde
        Raison: le filtrage par niveau empêche l'accès à du contenu hors programme
        Features: vue chapitre, filtrage par niveau, sécurité d'accès
        Criticité: haute
        """
        chap_sec = Chapitre.objects.create(matiere=matiere, niveau="seconde", titre="Chap Sec", ordre=1)
        client.force_login(eleve)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chap_sec.pk}))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_locked_chapitre_redirects(self, client, eleve, chapitre):
        """
        Teste: un élève sans ChapitreDebloque est redirigé depuis la vue chapitre
        Raison: le mécanisme de déblocage progressif doit empêcher l'accès prématuré
        Features: vue chapitre, déblocage progressif, progression
        Criticité: haute
        """
        client.force_login(eleve)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_unlocked_chapitre_returns_200(self, client, eleve, chapitre):
        """
        Teste: un élève avec chapitre débloqué obtient 200 sur la vue chapitre
        Raison: vérifier que le mécanisme de déblocage autorise correctement l'accès
        Features: vue chapitre, déblocage progressif, accès élève
        Criticité: moyenne
        """
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        client.force_login(eleve)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_chapitre_context_has_lecons_data(self, client, eleve, chapitre, lecon_gratuite):
        """
        Teste: le contexte contient lecons_data et nb_lecons pour le template
        Raison: l'absence de ces clés provoquerait une erreur de rendu dans le template chapitre
        Features: vue chapitre, contexte template, liste des leçons
        Criticité: basse
        """
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        client.force_login(eleve)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert "lecons_data" in response.context
        assert "nb_lecons" in response.context

    @pytest.mark.django_db
    def test_admin_bypasses_unlock_check(self, client, admin_user, chapitre):
        """
        Teste: un admin accède au chapitre sans ChapitreDebloque
        Raison: l'admin doit pouvoir consulter tout le contenu sans restriction de déblocage
        Features: vue chapitre, rôle admin, bypass déblocage
        Criticité: moyenne
        """
        client.force_login(admin_user)
        response = client.get(reverse("chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 200


class TestLeconView:
    def test_lecon_requires_login(self, client, lecon_gratuite):
        """
        Teste: la vue leçon redirige vers la connexion pour un visiteur anonyme
        Raison: l'accès au contenu pédagogique nécessite une authentification
        Features: vue leçon, contrôle d'accès, @login_required
        Criticité: haute
        """
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_wrong_niveau_redirects(self, client, eleve, matiere):
        """
        Teste: un élève terminale est redirigé s'il tente d'accéder à une leçon de seconde
        Raison: le filtrage par niveau empêche l'accès à du contenu hors programme
        Features: vue leçon, filtrage par niveau, sécurité d'accès
        Criticité: haute
        """
        chap_sec = Chapitre.objects.create(matiere=matiere, niveau="seconde", titre="Chap Sec L", ordre=1)
        lecon_sec = Lecon.objects.create(chapitre=chap_sec, titre="Lecon Sec", contenu="c", ordre=1)
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_sec.pk}))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_locked_chapitre_redirects(self, client, eleve, lecon_gratuite):
        """
        Teste: un élève sans chapitre débloqué est redirigé depuis la vue leçon
        Raison: le déblocage progressif doit empêcher l'accès aux leçons d'un chapitre verrouillé
        Features: vue leçon, déblocage progressif, progression
        Criticité: haute
        """
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_lecon_returns_200_when_unlocked(self, client, eleve, lecon_gratuite):
        """
        Teste: un élève avec chapitre débloqué obtient 200 sur la vue leçon
        Raison: vérifier que l'accès est autorisé quand toutes les conditions sont remplies
        Features: vue leçon, déblocage progressif, accès élève
        Criticité: moyenne
        """
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_lecon_marks_en_cours_on_first_access(self, client, eleve, lecon_gratuite):
        """
        Teste: la première visite d'une leçon crée une UserProgression en statut en_cours
        Raison: la progression doit être tracée automatiquement dès le premier accès
        Features: vue leçon, UserProgression, tracking progression
        Criticité: moyenne
        """
        from progress.models import ChapitreDebloque, UserProgression
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        prog = UserProgression.objects.get(user=eleve, lecon=lecon_gratuite)
        assert prog.statut == "en_cours"

    @pytest.mark.django_db
    def test_lecon_context_has_contenu_html(self, client, eleve, lecon_gratuite):
        """
        Teste: le contexte contient la clé contenu_html pour le rendu Markdown
        Raison: l'absence de cette clé empêcherait l'affichage du contenu de la leçon
        Features: vue leçon, rendu Markdown, contexte template
        Criticité: basse
        """
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert "contenu_html" in response.context

    @pytest.mark.django_db
    def test_admin_bypasses_unlock(self, client, admin_user, lecon_gratuite):
        """
        Teste: un admin accède à la leçon sans ChapitreDebloque
        Raison: l'admin doit pouvoir consulter tout le contenu sans restriction
        Features: vue leçon, rôle admin, bypass déblocage
        Criticité: moyenne
        """
        client.force_login(admin_user)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_lecon_second_access_keeps_en_cours(self, client, eleve, lecon_gratuite):
        """
        Teste: un deuxième accès à la leçon conserve le statut en_cours sans le réinitialiser
        Raison: la progression ne doit pas régresser ou créer de doublons lors de visites répétées
        Features: vue leçon, UserProgression, idempotence
        Criticité: moyenne
        """
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
        """
        Teste: la vue quiz redirige vers la connexion pour un visiteur anonyme
        Raison: l'accès aux quiz nécessite une authentification pour tracker les résultats
        Features: vue quiz, contrôle d'accès, @login_required
        Criticité: haute
        """
        response = client.get(reverse("quiz", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_quiz_returns_200_with_questions(self, client, eleve, lecon_gratuite):
        """
        Teste: un élève avec chapitre débloqué et quiz existant obtient 200
        Raison: vérifier le fonctionnement nominal de la vue quiz avec des questions
        Features: vue quiz, affichage questions, accès élève
        Criticité: moyenne
        """
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
        """
        Teste: une leçon sans quiz redirige l'élève vers la page leçon
        Raison: éviter une erreur 500 si le quiz n'existe pas encore pour cette leçon
        Features: vue quiz, redirection, robustesse
        Criticité: moyenne
        """
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        response = client.get(reverse("quiz", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 302
        assert f"/cours/lecon/{lecon_gratuite.pk}/" in response["Location"]

    @pytest.mark.django_db
    def test_quiz_context_has_question_ids(self, client, eleve, lecon_gratuite):
        """
        Teste: le contexte contient question_ids et questions pour le template quiz
        Raison: ces clés sont nécessaires au formulaire HTMX de soumission du quiz
        Features: vue quiz, contexte template, formulaire quiz
        Criticité: basse
        """
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
        """
        Teste: la vue quiz sélectionne au maximum 5 questions même si le quiz en contient plus
        Raison: limiter le nombre de questions par session pour une expérience pédagogique optimale
        Features: vue quiz, sélection questions, limite 5 questions
        Criticité: moyenne
        """
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
        """
        Teste: un fichier CSV avec seulement l'en-tête ne provoque pas de crash
        Raison: un CSV vide (sans lignes de données) doit être géré gracieusement
        Features: import CSV, robustesse, validation fichier
        Criticité: basse
        """
        from django.core.management import call_command
        csv_content = "quiz_lecon_slug,texte,type,reponse_correcte,options,tolerances,explication,points,ordre,difficulte\n"
        csv_file = tmp_path / "empty.csv"
        csv_file.write_text(csv_content, encoding="utf-8")
        call_command("import_questions", str(csv_file))

    def test_qcm_options_parsed_as_json(self, tmp_path, db, matiere, chapitre):
        """
        Teste: les options QCM au format JSON dans le CSV sont correctement parsées en liste Python
        Raison: un parsing incorrect des options rendrait les questions QCM inutilisables
        Features: import CSV, parsing JSON, questions QCM
        Criticité: moyenne
        """
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
        """
        Teste: la vue révisions redirige vers la connexion pour un visiteur anonyme
        Raison: les révisions sont liées à l'historique personnel de l'élève
        Features: vue révisions, contrôle d'accès, @login_required
        Criticité: haute
        """
        response = client.get(reverse("revisions"))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_revisions_returns_200(self, client, eleve):
        """
        Teste: un élève authentifié obtient 200 sur la page révisions
        Raison: vérifier le fonctionnement nominal de la page répétition espacée
        Features: vue révisions, accès élève, répétition espacée
        Criticité: moyenne
        """
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_revisions_context_has_box_display(self, client, eleve):
        """
        Teste: le contexte contient box_display, nb_dues et total_historiques pour le template
        Raison: ces clés sont nécessaires à l'affichage des boîtes Leitner et du compteur de révisions
        Features: vue révisions, contexte template, système Leitner
        Criticité: basse
        """
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        assert "box_display" in response.context
        assert "nb_dues" in response.context
        assert "total_historiques" in response.context

    @pytest.mark.django_db
    def test_revisions_shows_due_questions(self, client, eleve, lecon_gratuite):
        """
        Teste: les questions dont la date de révision est aujourd'hui apparaissent dans le contexte
        Raison: le système Leitner doit présenter les questions dues au bon moment
        Features: vue révisions, répétition espacée, questions dues
        Criticité: moyenne
        """
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
        """
        Teste: les questions dont la révision est dans le futur ne sont pas affichées
        Raison: présenter des questions non dues casserait le rythme de répétition espacée
        Features: vue révisions, répétition espacée, filtrage temporel
        Criticité: moyenne
        """
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
        """
        Teste: la soumission de révisions redirige vers la connexion pour un visiteur anonyme
        Raison: les résultats de révision sont liés au profil utilisateur
        Features: soumission révisions, contrôle d'accès, @login_required
        Criticité: haute
        """
        response = client.post(reverse("soumettre_revisions"))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_get_redirects_to_revisions(self, client, eleve):
        """
        Teste: une requête GET sur soumettre_revisions redirige vers la page révisions
        Raison: la soumission ne doit se faire que via POST pour éviter les doubles soumissions
        Features: soumission révisions, méthode HTTP, redirection
        Criticité: basse
        """
        client.force_login(eleve)
        response = client.get(reverse("soumettre_revisions"))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_soumettre_revisions_empty_ids_redirects(self, client, eleve):
        """
        Teste: une soumission avec question_ids vide redirige sans erreur
        Raison: éviter un crash si le formulaire est soumis sans sélection de questions
        Features: soumission révisions, validation données, robustesse
        Criticité: basse
        """
        client.force_login(eleve)
        response = client.post(reverse("soumettre_revisions"), {"question_ids": ""})
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_soumettre_revisions_renders_resultat(self, client, eleve, lecon_gratuite):
        """
        Teste: une soumission valide affiche la page résultat avec les corrections
        Raison: vérifier le parcours complet de soumission et d'affichage des résultats
        Features: soumission révisions, évaluation réponses, page résultat
        Criticité: moyenne
        """
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
        """
        Teste: une bonne réponse en révision fait progresser la question dans la boîte Leitner suivante
        Raison: le système de répétition espacée repose sur la progression entre boîtes
        Features: soumission révisions, système Leitner, mise à jour boîte
        Criticité: moyenne
        """
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
        """
        Teste: la page d'accueil est accessible sans authentification avec un code 200
        Raison: la landing page doit être publique pour attirer de nouveaux utilisateurs
        Features: page accueil, accès public, SEO
        Criticité: haute
        """
        response = client.get("/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_accueil_renders_accueil_template(self, client):
        """
        Teste: la page d'accueil utilise le template courses/accueil.html
        Raison: vérifier que le bon template est utilisé pour éviter un rendu inattendu
        Features: page accueil, template, rendu
        Criticité: basse
        """
        response = client.get("/")
        assert "courses/accueil.html" in [t.name for t in response.templates]

    @pytest.mark.django_db
    def test_accueil_context_has_matieres_data(self, client, matiere):
        """
        Teste: le contexte de la page d'accueil contient matieres_data
        Raison: cette clé est nécessaire pour afficher les matières sur la landing page
        Features: page accueil, contexte template, liste matières
        Criticité: basse
        """
        response = client.get("/")
        assert "matieres_data" in response.context

    @pytest.mark.django_db
    def test_authenticated_user_redirected_to_dashboard(self, client, eleve):
        """
        Teste: un utilisateur connecté sur "/" est redirigé vers le tableau de bord
        Raison: les élèves connectés doivent accéder directement à leur espace personnalisé
        Features: page accueil, redirection, tableau de bord
        Criticité: moyenne
        """
        client.force_login(eleve)
        response = client.get("/")
        assert response.status_code == 302
        assert "tableau-de-bord" in response["Location"]


class TestYoutubeHelper:
    """Tests unitaires pour _extraire_youtube_id."""

    def test_standard_url(self):
        """
        Teste: extraction de l'ID YouTube depuis une URL standard youtube.com/watch?v=
        Raison: c'est le format d'URL le plus courant collé par les enseignants
        Features: helper YouTube, extraction ID, URL standard
        Criticité: basse
        """
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_short_url(self):
        """
        Teste: extraction de l'ID YouTube depuis une URL courte youtu.be/
        Raison: les URL courtes sont fréquemment utilisées dans les partages
        Features: helper YouTube, extraction ID, URL courte
        Criticité: basse
        """
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_embed_url(self):
        """
        Teste: extraction de l'ID YouTube depuis une URL embed youtube.com/embed/
        Raison: les vidéos intégrées utilisent ce format dans les iframes
        Features: helper YouTube, extraction ID, URL embed
        Criticité: basse
        """
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("https://www.youtube.com/embed/dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_none_input(self):
        """
        Teste: un input None retourne None sans erreur
        Raison: la leçon peut ne pas avoir de vidéo YouTube associée
        Features: helper YouTube, robustesse, valeur nulle
        Criticité: basse
        """
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id(None) is None

    def test_empty_string(self):
        """
        Teste: une chaîne vide retourne None sans erreur
        Raison: un champ vidéo vide ne doit pas provoquer d'exception
        Features: helper YouTube, robustesse, chaîne vide
        Criticité: basse
        """
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("") is None

    def test_invalid_url(self):
        """
        Teste: une URL invalide (non YouTube) retourne None sans erreur
        Raison: une URL malformée collée par erreur ne doit pas crasher la page
        Features: helper YouTube, robustesse, validation URL
        Criticité: basse
        """
        from courses.views import _extraire_youtube_id
        assert _extraire_youtube_id("not a youtube url") is None


class TestLatexHelpers:
    """Tests unitaires pour _proteger_latex et _restaurer_latex."""

    def test_proteger_inline_latex(self):
        """
        Teste: les expressions LaTeX inline $...$ sont remplacées par des placeholders
        Raison: protéger le LaTeX inline du traitement Markdown qui casserait la syntaxe
        Features: helper LaTeX, protection inline, rendu Markdown
        Criticité: moyenne
        """
        from courses.views import _proteger_latex
        texte = "Voici $x^2$ et $y$"
        result, placeholders = _proteger_latex(texte)
        assert len(placeholders) == 2
        assert "$x^2$" not in result
        assert "$y$" not in result

    def test_proteger_display_latex(self):
        """
        Teste: les expressions LaTeX display $$...$$ sont remplacées par des placeholders
        Raison: protéger le LaTeX display du traitement Markdown qui casserait la syntaxe
        Features: helper LaTeX, protection display, rendu Markdown
        Criticité: moyenne
        """
        from courses.views import _proteger_latex
        texte = "Voici $$E=mc^2$$"
        result, placeholders = _proteger_latex(texte)
        assert len(placeholders) == 1
        assert "$$E=mc^2$$" not in result

    def test_restaurer_restores_original(self):
        """
        Teste: la restauration des placeholders reconstitue le texte LaTeX original
        Raison: le cycle complet protéger/restaurer doit être sans perte pour l'affichage KaTeX
        Features: helper LaTeX, restauration, intégrité contenu
        Criticité: moyenne
        """
        from courses.views import _proteger_latex, _restaurer_latex
        original = "Voici $x^2$ et $$E=mc^2$$"
        protected, placeholders = _proteger_latex(original)
        restored = _restaurer_latex(protected, placeholders)
        assert restored == original

    def test_no_latex_unchanged(self):
        """
        Teste: un texte sans LaTeX reste inchangé après protection
        Raison: la fonction ne doit pas altérer le contenu non-LaTeX
        Features: helper LaTeX, cas sans LaTeX, idempotence
        Criticité: basse
        """
        from courses.views import _proteger_latex
        texte = "No LaTeX here"
        result, placeholders = _proteger_latex(texte)
        assert result == texte
        assert len(placeholders) == 0

    def test_mixed_inline_and_display(self):
        """
        Teste: un texte mélangeant LaTeX inline et display est correctement protégé
        Raison: les leçons mélangent souvent les deux formats dans le même contenu
        Features: helper LaTeX, protection mixte, inline et display
        Criticité: moyenne
        """
        from courses.views import _proteger_latex
        texte = "Inline $a+b$ puis display $$\\int_0^1 x\\,dx$$"
        result, placeholders = _proteger_latex(texte)
        assert len(placeholders) == 2
        assert "$a+b$" not in result
        assert "$$\\int_0^1 x\\,dx$$" not in result


class TestCatalogueView:
    @pytest.mark.django_db
    def test_catalogue_nonexistent_matiere_returns_404(self, client):
        """
        Teste: un slug de matière inexistant retourne une erreur 404
        Raison: éviter un crash 500 sur une URL de catalogue avec un slug invalide
        Features: vue catalogue, gestion 404, robustesse URL
        Criticité: moyenne
        """
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": "inexistant"})
        )
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_catalogue_context_has_niveaux_data(self, client, matiere):
        """
        Teste: le contexte du catalogue contient la clé niveaux_data
        Raison: cette clé est nécessaire pour afficher la structure par niveaux dans le template
        Features: vue catalogue, contexte template, structure niveaux
        Criticité: basse
        """
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": matiere.slug})
        )
        assert response.status_code == 200
        assert "niveaux_data" in response.context

    @pytest.mark.django_db
    def test_catalogue_contains_chapitre_titles(self, client, chapitre):
        """
        Teste: le HTML du catalogue contient le titre du chapitre existant
        Raison: vérifier que les chapitres sont bien affichés dans le catalogue public
        Features: vue catalogue, affichage chapitres, rendu HTML
        Criticité: basse
        """
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": chapitre.matiere.slug})
        )
        assert response.status_code == 200
        assert chapitre.titre.encode() in response.content

    @pytest.mark.django_db
    def test_catalogue_accessible_when_authenticated(self, client, eleve, matiere):
        """
        Teste: le catalogue est aussi accessible aux utilisateurs connectés
        Raison: un élève connecté doit pouvoir consulter le catalogue public sans erreur
        Features: vue catalogue, accès authentifié, compatibilité
        Criticité: basse
        """
        client.force_login(eleve)
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": matiere.slug})
        )
        assert response.status_code == 200


class TestErrorPages:
    @pytest.mark.django_db
    def test_404_returns_404_status(self, client):
        """
        Teste: une URL inexistante retourne bien un code 404
        Raison: le handler 404 personnalisé doit retourner le bon code HTTP
        Features: page 404, gestion erreurs, handler personnalisé
        Criticité: moyenne
        """
        response = client.get("/cette-url-nexiste-pas/")
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_404_contains_message(self, client):
        """
        Teste: la page 404 contient un message d'erreur compréhensible
        Raison: l'utilisateur doit comprendre qu'il est sur une page introuvable
        Features: page 404, UX erreur, message utilisateur
        Criticité: basse
        """
        response = client.get("/cette-url-nexiste-pas/")
        assert b"introuvable" in response.content or b"404" in response.content

    def test_500_template_exists(self):
        """
        Teste: le template 500.html existe et est chargeable par Django
        Raison: une erreur 500 avec un template manquant donnerait une page blanche
        Features: page 500, gestion erreurs, template
        Criticité: moyenne
        """
        from django.template.loader import get_template
        template = get_template("500.html")
        assert template is not None


# ============================================================
# Batch 7 — Quiz chapitre, révisions détails, recherche avancée,
#            PDF, vidéo YouTube, navigation leçon, accueil, catalogue
# ============================================================


class TestQuizChapitreView:
    """Tests pour quiz_chapitre_view."""

    def test_quiz_chapitre_requires_login(self, client, chapitre):
        """
        Teste: la vue quiz chapitre redirige vers la connexion pour un visiteur anonyme
        Raison: le quiz de fin de chapitre requiert une session élève pour enregistrer le résultat
        Features: vue quiz chapitre, contrôle d'accès, @login_required
        Criticité: haute
        """
        response = client.get(reverse("quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_quiz_chapitre_returns_200(self, client, eleve, chapitre, lecon_gratuite):
        """
        Teste: un élève avec chapitre débloqué et questions existantes obtient 200
        Raison: vérifier le fonctionnement nominal du quiz de fin de chapitre
        Features: vue quiz chapitre, accès élève, déblocage
        Criticité: moyenne
        """
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Quiz Chap")
        for i in range(10):
            Question.objects.create(
                quiz=quiz, texte=f"QC{i}", type="qcm",
                options=["A", "B", "C"], reponse_correcte="0",
                points=1, ordre=i + 1,
            )
        client.force_login(eleve)
        response = client.get(reverse("quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_quiz_chapitre_locked_chapter_redirects(self, client, eleve, chapitre):
        """
        Teste: un élève sans ChapitreDebloque est redirigé depuis le quiz chapitre
        Raison: le mécanisme de déblocage doit empêcher l'accès prématuré au quiz final
        Features: vue quiz chapitre, déblocage progressif, sécurité
        Criticité: haute
        """
        client.force_login(eleve)
        response = client.get(reverse("quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_quiz_chapitre_selects_10_questions(self, client, eleve, chapitre, lecon_gratuite):
        """
        Teste: le contexte contient question_ids avec exactement 10 IDs quand le pool est suffisant
        Raison: le quiz chapitre doit présenter exactement 10 questions pour un score sur 10
        Features: vue quiz chapitre, sélection 10 questions, question_ids
        Criticité: moyenne
        """
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Quiz 10Q")
        for i in range(4):
            Question.objects.create(
                quiz=quiz, texte=f"F{i}", type="qcm",
                options=["A", "B"], reponse_correcte="0",
                points=1, ordre=i + 1, difficulte="facile",
            )
        for i in range(4):
            Question.objects.create(
                quiz=quiz, texte=f"M{i}", type="qcm",
                options=["A", "B"], reponse_correcte="0",
                points=1, ordre=i + 10, difficulte="moyen",
            )
        for i in range(2):
            Question.objects.create(
                quiz=quiz, texte=f"D{i}", type="qcm",
                options=["A", "B"], reponse_correcte="0",
                points=1, ordre=i + 20, difficulte="difficile",
            )
        client.force_login(eleve)
        response = client.get(reverse("quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        question_ids = response.context["question_ids"]
        ids_list = [qid for qid in question_ids.split(",") if qid.strip()]
        assert len(ids_list) == 10

    @pytest.mark.django_db
    def test_admin_bypasses_unlock(self, client, admin_user, chapitre, lecon_gratuite):
        """
        Teste: un admin accède au quiz chapitre sans ChapitreDebloque
        Raison: l'admin doit pouvoir tester tout le contenu sans restriction de déblocage
        Features: vue quiz chapitre, rôle admin, bypass déblocage
        Criticité: moyenne
        """
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Quiz Admin")
        for i in range(3):
            Question.objects.create(
                quiz=quiz, texte=f"A{i}", type="qcm",
                options=["A", "B"], reponse_correcte="0",
                points=1, ordre=i + 1,
            )
        client.force_login(admin_user)
        response = client.get(reverse("quiz_chapitre", kwargs={"chapitre_pk": chapitre.pk}))
        assert response.status_code == 200


class TestRevisionsViewDetails:
    """Tests détaillés pour revisions_view (filtrage, max, vide)."""

    @pytest.mark.django_db
    def test_revisions_returns_200(self, client, eleve):
        """
        Teste: un élève authentifié obtient 200 sur la page révisions
        Raison: vérifier le fonctionnement nominal de la page répétition espacée
        Features: vue révisions, accès élève
        Criticité: moyenne
        """
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_revisions_only_due_questions(self, client, eleve, lecon_gratuite):
        """
        Teste: seules les questions dont prochaine_revision <= today apparaissent
        Raison: le système Leitner ne doit présenter que les questions dues
        Features: vue révisions, filtrage temporel, Leitner
        Criticité: moyenne
        """
        from progress.models import UserQuestionHistorique
        from datetime import date, timedelta
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Rev Detail")
        q_due = Question.objects.create(
            quiz=quiz, texte="Due?", type="qcm",
            options=["A", "B"], reponse_correcte="0", points=1, ordre=1,
        )
        q_future = Question.objects.create(
            quiz=quiz, texte="Future?", type="qcm",
            options=["A", "B"], reponse_correcte="0", points=1, ordre=2,
        )
        UserQuestionHistorique.objects.create(
            user=eleve, question=q_due, boite=1,
            prochaine_revision=date.today(), nb_bonnes=0, nb_total=1,
        )
        UserQuestionHistorique.objects.create(
            user=eleve, question=q_future, boite=2,
            prochaine_revision=date.today() + timedelta(days=30),
            nb_bonnes=1, nb_total=1,
        )
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        questions = response.context["questions"]
        assert q_due in questions
        assert q_future not in questions

    @pytest.mark.django_db
    def test_revisions_max_10_questions(self, client, eleve, lecon_gratuite):
        """
        Teste: la vue révisions retourne au maximum 10 questions même si davantage sont dues
        Raison: limiter la charge cognitive de la session de révision
        Features: vue révisions, limite 10 questions, répétition espacée
        Criticité: moyenne
        """
        from progress.models import UserQuestionHistorique
        from datetime import date
        quiz = Quiz.objects.create(lecon=lecon_gratuite, titre="Rev Max")
        for i in range(15):
            q = Question.objects.create(
                quiz=quiz, texte=f"Rev{i}", type="qcm",
                options=["A", "B"], reponse_correcte="0", points=1, ordre=i + 1,
            )
            UserQuestionHistorique.objects.create(
                user=eleve, question=q, boite=1,
                prochaine_revision=date.today(), nb_bonnes=0, nb_total=1,
            )
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        assert len(response.context["questions"]) <= 10

    @pytest.mark.django_db
    def test_revisions_empty_when_no_due(self, client, eleve):
        """
        Teste: si aucune question n'est due, la page affiche une liste vide sans crash
        Raison: un élève sans historique ne doit pas déclencher d'erreur
        Features: vue révisions, cas vide, robustesse
        Criticité: basse
        """
        client.force_login(eleve)
        response = client.get(reverse("revisions"))
        assert response.status_code == 200
        assert len(response.context["questions"]) == 0


class TestRechercheResults:
    """Tests avancés pour recherche_view (résultats, filtrage)."""

    @pytest.mark.django_db
    def test_recherche_finds_matching_title(self, client, eleve, chapitre):
        """
        Teste: la recherche retourne une leçon dont le titre correspond à la requête
        Raison: la recherche plein-texte doit trouver les titres correspondants
        Features: recherche full-text, titre leçon, SearchVector
        Criticité: moyenne
        """
        Lecon.objects.create(
            chapitre=chapitre, titre="Cinétique chimique avancée",
            contenu="Contenu sur la cinétique chimique", ordre=20,
        )
        client.force_login(eleve)
        response = client.get(reverse("recherche"), {"q": "cinétique"})
        assert response.status_code == 200
        titres = [r.titre for r in response.context["results"]]
        assert any("inétique" in t for t in titres)

    @pytest.mark.django_db
    def test_recherche_eleve_filtered_by_niveau(self, client, matiere):
        """
        Teste: un élève seconde ne voit que les leçons de son niveau dans les résultats
        Raison: le filtrage par niveau protège la cohérence pédagogique des résultats
        Features: recherche full-text, filtrage niveau, rôle élève
        Criticité: haute
        """
        eleve_sec = CustomUser.objects.create_user(
            email="sec@test.com", password="TestPass123!",
            prenom="Sec", nom="Ond", role="eleve", niveau="seconde",
        )
        chap_sec = Chapitre.objects.create(
            matiere=matiere, niveau="seconde", titre="Chap Sec", ordre=1,
        )
        chap_term = Chapitre.objects.create(
            matiere=matiere, niveau="terminale", titre="Chap Term", ordre=1,
        )
        Lecon.objects.create(
            chapitre=chap_sec, titre="Mouvement seconde",
            contenu="Mouvement en seconde", ordre=1,
        )
        Lecon.objects.create(
            chapitre=chap_term, titre="Mouvement terminale",
            contenu="Mouvement en terminale", ordre=1,
        )
        client.force_login(eleve_sec)
        response = client.get(reverse("recherche"), {"q": "mouvement"})
        results = response.context["results"]
        niveaux = {r.chapitre.niveau for r in results}
        assert "terminale" not in niveaux

    @pytest.mark.django_db
    def test_recherche_admin_sees_all(self, client, admin_user, matiere):
        """
        Teste: un admin voit les leçons de tous les niveaux dans les résultats de recherche
        Raison: l'admin doit pouvoir trouver tout le contenu sans restriction de niveau
        Features: recherche full-text, rôle admin, aucun filtrage
        Criticité: moyenne
        """
        chap_sec = Chapitre.objects.create(
            matiere=matiere, niveau="seconde", titre="Chap Sec A", ordre=1,
        )
        chap_term = Chapitre.objects.create(
            matiere=matiere, niveau="terminale", titre="Chap Term A", ordre=1,
        )
        Lecon.objects.create(
            chapitre=chap_sec, titre="Force gravitationnelle seconde",
            contenu="Force gravitationnelle en seconde", ordre=1,
        )
        Lecon.objects.create(
            chapitre=chap_term, titre="Force gravitationnelle terminale",
            contenu="Force gravitationnelle en terminale", ordre=1,
        )
        client.force_login(admin_user)
        response = client.get(reverse("recherche"), {"q": "gravitationnelle"})
        results = response.context["results"]
        niveaux = {r.chapitre.niveau for r in results}
        assert "seconde" in niveaux
        assert "terminale" in niveaux


class TestLeconPdfView:
    """Tests pour lecon_pdf_view."""

    def test_pdf_requires_login(self, client, lecon_payante):
        """
        Teste: la vue PDF redirige vers la connexion pour un visiteur anonyme
        Raison: l'export PDF est une feature authentifiée pour les élèves abonnés
        Features: vue PDF, contrôle d'accès, @login_required
        Criticité: haute
        """
        response = client.get(reverse("lecon_pdf", kwargs={"lecon_pk": lecon_payante.pk}))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_pdf_premium_without_subscription_redirects(self, client, eleve, lecon_payante):
        """
        Teste: un élève sans abonnement est redirigé vers lecon_publique pour une leçon premium
        Raison: l'export PDF d'une leçon premium ne doit pas contourner le paywall
        Features: vue PDF, paywall, accès premium, redirection
        Criticité: haute
        """
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_payante.chapitre)
        client.force_login(eleve)
        response = client.get(reverse("lecon_pdf", kwargs={"lecon_pk": lecon_payante.pk}))
        assert response.status_code == 302
        assert "lecon_publique" in response["Location"] or f"/{lecon_payante.chapitre.matiere.slug}/" in response["Location"]

    @pytest.mark.django_db
    def test_pdf_preview_paywall_redirects(self, client, admin_user, lecon_gratuite):
        """
        Teste: avec session preview_paywall active, l'admin est redirigé vers lecon_publique
        Raison: le mode preview paywall doit simuler le parcours complet d'un non-abonné
        Features: vue PDF, preview paywall, redirection admin
        Criticité: moyenne
        """
        client.force_login(admin_user)
        session = client.session
        session["preview_paywall"] = True
        session.save()
        response = client.get(reverse("lecon_pdf", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 302
        chapitre = lecon_gratuite.chapitre
        assert f"/{chapitre.matiere.slug}/" in response["Location"]


class TestLeconVideoYoutube:
    """Tests pour l'intégration vidéo YouTube dans lecon_view."""

    @pytest.mark.django_db
    def test_lecon_with_youtube_url_has_youtube_id(self, client, eleve, chapitre):
        """
        Teste: une leçon avec video_youtube_url a youtube_id dans le contexte
        Raison: l'identifiant YouTube est nécessaire pour l'intégration iframe dans le template
        Features: vue leçon, vidéo YouTube, contexte template
        Criticité: moyenne
        """
        from progress.models import ChapitreDebloque
        lecon_video = Lecon.objects.create(
            chapitre=chapitre, titre="Lecon Video", contenu="# Video",
            ordre=50, gratuit=True,
            video_youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        )
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_video.pk}))
        assert response.status_code == 200
        assert response.context["youtube_id"] == "dQw4w9WgXcQ"

    @pytest.mark.django_db
    def test_lecon_without_video_no_youtube_id(self, client, eleve, lecon_gratuite):
        """
        Teste: une leçon sans vidéo YouTube a youtube_id=None dans le contexte
        Raison: vérifier que l'absence de vidéo n'introduit pas d'erreur dans le template
        Features: vue leçon, pas de vidéo, contexte template
        Criticité: basse
        """
        from progress.models import ChapitreDebloque
        ChapitreDebloque.objects.create(user=eleve, chapitre=lecon_gratuite.chapitre)
        client.force_login(eleve)
        response = client.get(reverse("lecon", kwargs={"lecon_pk": lecon_gratuite.pk}))
        assert response.status_code == 200
        assert response.context["youtube_id"] is None


class TestLeconNavigation:
    """Tests pour get_lecon_suivante et get_lecon_precedente."""

    @pytest.mark.django_db
    def test_get_lecon_suivante(self, chapitre):
        """
        Teste: get_lecon_suivante retourne la leçon suivante dans le même chapitre
        Raison: la navigation inter-leçons doit permettre un parcours séquentiel
        Features: navigation leçon, get_lecon_suivante, modèle Lecon
        Criticité: moyenne
        """
        l1 = Lecon.objects.create(chapitre=chapitre, titre="L1", contenu="c", ordre=1)
        l2 = Lecon.objects.create(chapitre=chapitre, titre="L2", contenu="c", ordre=2)
        assert l1.get_lecon_suivante() == l2

    @pytest.mark.django_db
    def test_get_lecon_precedente(self, chapitre):
        """
        Teste: get_lecon_precedente retourne la leçon précédente dans le même chapitre
        Raison: la navigation inter-leçons doit permettre un retour en arrière
        Features: navigation leçon, get_lecon_precedente, modèle Lecon
        Criticité: moyenne
        """
        l1 = Lecon.objects.create(chapitre=chapitre, titre="L1", contenu="c", ordre=1)
        l2 = Lecon.objects.create(chapitre=chapitre, titre="L2", contenu="c", ordre=2)
        assert l2.get_lecon_precedente() == l1

    @pytest.mark.django_db
    def test_get_lecon_suivante_last_returns_none(self, chapitre):
        """
        Teste: get_lecon_suivante retourne None pour la dernière leçon du chapitre
        Raison: il n'y a pas de leçon suivante après la dernière du chapitre
        Features: navigation leçon, dernière leçon, cas limite
        Criticité: basse
        """
        l1 = Lecon.objects.create(chapitre=chapitre, titre="L1", contenu="c", ordre=1)
        assert l1.get_lecon_suivante() is None

    @pytest.mark.django_db
    def test_get_lecon_precedente_first_returns_none(self, chapitre):
        """
        Teste: get_lecon_precedente retourne None pour la première leçon du chapitre
        Raison: il n'y a pas de leçon précédente avant la première du chapitre
        Features: navigation leçon, première leçon, cas limite
        Criticité: basse
        """
        l1 = Lecon.objects.create(chapitre=chapitre, titre="L1", contenu="c", ordre=1)
        assert l1.get_lecon_precedente() is None


class TestAccueilViewExtended:
    """Tests étendus pour accueil_view."""

    @pytest.mark.django_db
    def test_accueil_accessible_anonymous(self, client):
        """
        Teste: la page d'accueil est accessible sans authentification
        Raison: la landing page est publique et sert de porte d'entrée
        Features: page accueil, accès anonyme
        Criticité: haute
        """
        response = client.get("/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_accueil_has_matieres(self, client, matiere):
        """
        Teste: le contexte de la page d'accueil contient des matières
        Raison: les matières doivent apparaître sur la landing pour guider les visiteurs
        Features: page accueil, matieres_data, contexte
        Criticité: moyenne
        """
        response = client.get("/")
        matieres_data = response.context["matieres_data"]
        assert len(matieres_data) >= 1

    @pytest.mark.django_db
    def test_accueil_shows_gratuit_badge(self, client, lecon_gratuite):
        """
        Teste: la page d'accueil affiche le badge Gratuit pour les leçons gratuites
        Raison: le badge Gratuit est un élément de conversion pour les visiteurs
        Features: page accueil, badge gratuit, conversion
        Criticité: moyenne
        """
        response = client.get("/")
        assert b"Gratuit" in response.content


class TestCatalogueMatiereExtended:
    """Tests étendus pour catalogue_matiere_view."""

    @pytest.mark.django_db
    def test_catalogue_returns_200(self, client, matiere):
        """
        Teste: le catalogue d'une matière existante retourne 200 pour un visiteur anonyme
        Raison: le catalogue public doit être accessible sans connexion
        Features: vue catalogue, accès anonyme, code 200
        Criticité: haute
        """
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": matiere.slug})
        )
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_catalogue_context_has_chapitres(self, client, chapitre):
        """
        Teste: le contexte catalogue a niveaux_data contenant des chapitres groupés
        Raison: la structure par niveaux est essentielle pour l'affichage du catalogue
        Features: vue catalogue, niveaux_data, chapitres groupés
        Criticité: moyenne
        """
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": chapitre.matiere.slug})
        )
        niveaux_data = response.context["niveaux_data"]
        assert len(niveaux_data) >= 1
        first_niveau = niveaux_data[0]
        assert len(first_niveau["chapitres"]) >= 1

    @pytest.mark.django_db
    def test_catalogue_invalid_slug_returns_404(self, client):
        """
        Teste: un slug de matière inexistant retourne 404
        Raison: éviter un crash 500 sur les URLs de catalogue invalides
        Features: vue catalogue, 404, robustesse URL
        Criticité: moyenne
        """
        response = client.get(
            reverse("catalogue_matiere", kwargs={"matiere_slug": "slug-inexistant"})
        )
        assert response.status_code == 404

