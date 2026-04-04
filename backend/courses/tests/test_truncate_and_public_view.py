"""
Tests for tronquer_contenu_markdown helper and lecon_publique_view (blur paywall).
"""
import pytest
from django.test import Client
from django.urls import reverse

from courses.models import Matiere, Chapitre, Lecon
from courses.utils.truncate import tronquer_contenu_markdown
from users.models import CustomUser


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def admin_user(db):
    return CustomUser.objects.create_user(
        email="admin-trunc@test.com",
        password="AdminPass123!",
        prenom="Admin",
        nom="Trunc",
        role="admin",
        is_staff=True,
    )


@pytest.fixture
def matiere(db):
    return Matiere.objects.create(nom="physique", description="Physique")


@pytest.fixture
def chapitre(matiere):
    return Chapitre.objects.create(
        matiere=matiere,
        niveau="terminale",
        titre="Mécanique Newtonienne",
        ordre=1,
    )


@pytest.fixture
def lecon_gratuite(chapitre):
    return Lecon.objects.create(
        chapitre=chapitre,
        titre="Introduction forces",
        contenu="# Forces\n\nLes forces sont des vecteurs.",
        ordre=1,
        gratuit=True,
    )


def _generer_contenu_long(nb_mots: int = 2500, marqueur_fin: str = "MOT_MARQUEUR_FIN") -> str:
    """Génère un contenu Markdown avec nb_mots mots et un marqueur vers la fin."""
    paragraphe = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    mots_par_paragraphe = len(paragraphe.split())
    nb_paragraphes = (nb_mots // mots_par_paragraphe) + 5

    lignes = ["# Titre principal\n"]
    for i in range(nb_paragraphes):
        lignes.append(paragraphe)
        if i % 5 == 4:
            lignes.append("")  # double newline = paragraph break in Markdown
    # Ajouter le marqueur bien au-delà des 2000 mots
    lignes.append(f"\n\n## Section finale\n\n{marqueur_fin} Ce paragraphe contient le marqueur.")
    contenu = "\n".join(lignes)
    assert len(contenu.split()) > nb_mots, f"Contenu généré trop court: {len(contenu.split())} mots"
    return contenu


@pytest.fixture
def lecon_premium_longue(chapitre):
    return Lecon.objects.create(
        chapitre=chapitre,
        titre="Cours complet mécanique",
        contenu=_generer_contenu_long(2500),
        ordre=2,
        gratuit=False,
    )


@pytest.fixture
def lecon_premium_courte(chapitre):
    return Lecon.objects.create(
        chapitre=chapitre,
        titre="Intro mécanique",
        contenu="# Mécanique\n\nCours court premium.",
        ordre=3,
        gratuit=False,
    )


# ===========================================================================
# Tests de truncation (tronquer_contenu_markdown)
# ===========================================================================


class TestTronquerContenuMarkdown:
    def test_tronquer_contenu_court(self):
        """
        Teste: Contenu < 2000 mots retourné intact avec a_ete_tronque=False
        Raison: Vérifie que la truncation ne modifie pas un contenu court
        Features: truncation markdown, paywall
        Criticité: moyenne
        """
        contenu = "Un deux trois quatre cinq."
        resultat, a_ete_tronque = tronquer_contenu_markdown(contenu)
        assert resultat == contenu
        assert a_ete_tronque is False

    def test_tronquer_contenu_long(self):
        """
        Teste: Contenu > 2000 mots tronqué avec a_ete_tronque=True et ≤ 2000 mots en sortie
        Raison: Vérifie que le contenu premium long est bien coupé pour le paywall
        Features: truncation markdown, paywall
        Criticité: moyenne
        """
        contenu = _generer_contenu_long(2500)
        resultat, a_ete_tronque = tronquer_contenu_markdown(contenu)
        assert a_ete_tronque is True
        nb_mots_resultat = len(resultat.split())
        assert nb_mots_resultat <= 2000

    def test_tronquer_coupe_sur_paragraphe(self):
        """
        Teste: La coupure se fait sur une frontière de paragraphe, pas au milieu d'une phrase
        Raison: Évite un rendu cassé avec du Markdown tronqué en plein milieu de texte
        Features: truncation markdown, rendu public
        Criticité: moyenne
        """
        # Construire un contenu avec des paragraphes clairs
        paragraphes = []
        for i in range(250):
            # ~10 mots par paragraphe → ~2500 mots au total
            paragraphes.append(f"Paragraphe numéro {i} avec quelques mots supplémentaires ici maintenant encore plus.")
        contenu = "\n\n".join(paragraphes)
        assert len(contenu.split()) > 2000

        resultat, a_ete_tronque = tronquer_contenu_markdown(contenu)
        assert a_ete_tronque is True
        # Le résultat doit se terminer à une frontière de paragraphe (pas au milieu)
        assert resultat.endswith((".", "!", "?", "plus."))
        # Vérifier que le résultat est un préfixe exact du contenu original
        assert contenu.startswith(resultat)

    def test_tronquer_contenu_vide(self):
        """
        Teste: Contenu vide retourné intact sans erreur
        Raison: Cas limite — la fonction ne doit pas planter sur une chaîne vide
        Features: truncation markdown
        Criticité: basse
        """
        resultat, a_ete_tronque = tronquer_contenu_markdown("")
        assert resultat == ""
        assert a_ete_tronque is False


# ===========================================================================
# Tests de vue (lecon_publique_view)
# ===========================================================================


def _url_publique(lecon):
    chapitre = lecon.chapitre
    return reverse("lecon_publique", kwargs={
        "matiere_slug": chapitre.matiere.slug,
        "niveau": chapitre.niveau,
        "chapitre_slug": chapitre.slug,
        "lecon_slug": lecon.slug,
    })


class TestLeconPubliqueView:
    @pytest.mark.django_db
    def test_premium_lecon_publique_no_redirect(self, client, lecon_premium_courte):
        """
        Teste: GET leçon premium en anonyme retourne un status 200 sans redirection
        Raison: Les visiteurs anonymes doivent voir l'aperçu tronqué, pas être redirigés
        Features: lecon_publique_view, accès premium
        Criticité: haute
        """
        response = client.get(_url_publique(lecon_premium_courte))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_premium_lecon_publique_content_truncated(self, client, lecon_premium_longue):
        """
        Teste: GET leçon premium en anonyme — le texte au-delà des ~2000 mots est absent du HTML
        Raison: Le contenu premium ne doit pas fuiter au-delà de la troncature côté serveur
        Features: lecon_publique_view, truncation markdown, accès premium
        Criticité: haute
        """
        response = client.get(_url_publique(lecon_premium_longue))
        assert response.status_code == 200
        html = response.content.decode()
        assert "MOT_MARQUEUR_FIN" not in html

    @pytest.mark.django_db
    def test_premium_lecon_publique_blur_classes_present(self, client, lecon_premium_courte):
        """
        Teste: Le HTML contient la div paywall-blur-container pour une leçon premium en anonyme
        Raison: Le blur CSS doit être appliqué pour signaler visuellement le contenu premium
        Features: lecon_publique_view, paywall blur
        Criticité: moyenne
        """
        response = client.get(_url_publique(lecon_premium_courte))
        html = response.content.decode()
        # Vérifier la div blur (pas juste la définition CSS)
        assert 'class="px-6 py-6 paywall-blur-container"' in html

    @pytest.mark.django_db
    def test_premium_lecon_publique_cta_present(self, client, lecon_premium_courte):
        """
        Teste: Le bouton 'Débloquer cette leçon' est présent pour une leçon premium en anonyme
        Raison: Le CTA de conversion doit être visible pour inciter à l'abonnement
        Features: lecon_publique_view, paywall CTA
        Criticité: moyenne
        """
        response = client.get(_url_publique(lecon_premium_courte))
        html = response.content.decode()
        assert "bloquer cette le" in html.lower()

    @pytest.mark.django_db
    def test_free_lecon_publique_no_blur(self, client, lecon_gratuite):
        """
        Teste: GET leçon gratuite — pas de div paywall-blur-container dans le HTML
        Raison: Les leçons gratuites ne doivent jamais afficher le blur paywall
        Features: lecon_publique_view, paywall blur, leçons gratuites
        Criticité: moyenne
        """
        response = client.get(_url_publique(lecon_gratuite))
        assert response.status_code == 200
        html = response.content.decode()
        # La div blur ne doit pas être rendue (la CSS est toujours là, mais pas la div)
        assert 'class="px-6 py-6 paywall-blur-container"' not in html

    @pytest.mark.django_db
    def test_admin_redirected_to_lecon_view(self, client, admin_user, lecon_gratuite):
        """
        Teste: Un admin authentifié est redirigé vers la vue leçon par PK
        Raison: Les admins doivent accéder à la vue complète, pas à la vue publique tronquée
        Features: lecon_publique_view, redirection admin
        Criticité: moyenne
        """
        client.force_login(admin_user)
        response = client.get(_url_publique(lecon_gratuite))
        assert response.status_code == 302
        assert f"/cours/lecon/{lecon_gratuite.pk}/" in response["Location"]


# ===========================================================================
# Tests paywall visuel — catalogue & accueil
# ===========================================================================


class TestPaywallVisuel:
    """Tests du rendu paywall (cadenas, badge Premium, modal) sur catalogue et accueil."""

    @pytest.mark.django_db
    def test_catalogue_shows_lock_icon_on_premium_lessons(self, client, matiere, lecon_premium_courte):
        """
        Teste: GET catalogue d'une matière avec leçon premium — icône 🔒 présente
        Raison: L'indicateur visuel premium doit apparaître pour informer les visiteurs
        Features: catalogue, paywall visuel, badge premium
        Criticité: moyenne
        """
        url = reverse("catalogue_matiere", kwargs={"matiere_slug": matiere.slug})
        response = client.get(url)
        assert response.status_code == 200
        html = response.content.decode()
        assert "🔒" in html

    @pytest.mark.django_db
    def test_catalogue_no_lock_on_free_lessons(self, client, matiere, chapitre):
        """
        Teste: GET catalogue avec uniquement des leçons gratuites — aucun 🔒 affiché
        Raison: Les leçons gratuites ne doivent pas afficher d'indicateur de verrouillage
        Features: catalogue, paywall visuel, leçons gratuites
        Criticité: moyenne
        """
        # Créer uniquement des leçons gratuites (sans utiliser la fixture premium)
        Lecon.objects.filter(chapitre=chapitre, gratuit=False).delete()
        Lecon.objects.create(
            chapitre=chapitre,
            titre="Leçon gratuite A",
            contenu="Contenu A",
            ordre=10,
            gratuit=True,
        )
        url = reverse("catalogue_matiere", kwargs={"matiere_slug": matiere.slug})
        response = client.get(url)
        assert response.status_code == 200
        html = response.content.decode()
        assert "🔒" not in html

    @pytest.mark.django_db
    def test_paywall_modal_markup_present(self, client, lecon_premium_courte):
        """
        Teste: GET leçon premium en anonyme — composant Alpine showPaywall inclus dans le HTML
        Raison: La modal paywall doit être rendue pour permettre la conversion Stripe
        Features: lecon_publique_view, paywall modal, Stripe checkout
        Criticité: moyenne
        """
        response = client.get(_url_publique(lecon_premium_courte))
        assert response.status_code == 200
        html = response.content.decode()
        assert "showPaywall" in html

    @pytest.mark.django_db
    def test_accueil_shows_lock_icon_on_premium_lessons(self, client, lecon_premium_courte):
        """
        Teste: GET page d'accueil en anonyme avec leçon premium — icône 🔒 présente
        Raison: Le cadenas premium doit apparaître aussi sur la page d'accueil
        Features: accueil, paywall visuel, badge premium
        Criticité: moyenne
        """
        response = client.get(reverse("home"))
        assert response.status_code == 200
        html = response.content.decode()
        assert "🔒" in html


# ===========================================================================
# Tests Admin Paywall Preview Mode (lecon_publique_view)
# ===========================================================================


class TestAdminPaywallPreviewOnPublicView:
    """Tests du comportement de lecon_publique_view avec session["preview_paywall"]."""

    @pytest.mark.django_db
    def test_admin_sans_preview_redirige_vers_lecon_interne(self, client, admin_user, lecon_gratuite):
        """
        Teste: Un admin SANS preview_paywall est redirigé vers la vue leçon interne (par PK)
        Raison: Comportement normal — les admins accèdent à la vue complète, pas à la vue publique
        Features: lecon_publique_view, redirection admin
        Criticité: haute
        """
        client.force_login(admin_user)
        response = client.get(_url_publique(lecon_gratuite))
        assert response.status_code == 302
        assert f"/cours/lecon/{lecon_gratuite.pk}/" in response["Location"]

    @pytest.mark.django_db
    def test_admin_avec_preview_lecon_premium_voit_blur(self, client, admin_user, lecon_premium_courte):
        """
        Teste: Un admin AVEC preview_paywall sur une leçon premium voit la page publique avec est_floute
        Raison: Le mode preview doit simuler la vue d'un visiteur non-abonné face au paywall
        Features: lecon_publique_view, preview paywall, blur
        Criticité: haute
        """
        client.force_login(admin_user)
        session = client.session
        session["preview_paywall"] = True
        session.save()
        response = client.get(_url_publique(lecon_premium_courte))
        assert response.status_code == 200
        assert response.context["est_floute"] is True
        assert response.context["est_premium"] is True

    @pytest.mark.django_db
    def test_admin_avec_preview_lecon_gratuite_pas_de_blur(self, client, admin_user, lecon_gratuite):
        """
        Teste: Un admin AVEC preview_paywall sur une leçon gratuite voit la page normalement (pas de blur)
        Raison: Les leçons gratuites ne doivent jamais afficher le paywall, même en mode preview
        Features: lecon_publique_view, preview paywall, leçons gratuites
        Criticité: haute
        """
        client.force_login(admin_user)
        session = client.session
        session["preview_paywall"] = True
        session.save()
        response = client.get(_url_publique(lecon_gratuite))
        assert response.status_code == 200
        assert response.context["est_floute"] is False
        assert response.context["est_premium"] is False

    @pytest.mark.django_db
    def test_admin_avec_preview_pas_de_redirect(self, client, admin_user, lecon_premium_courte):
        """
        Teste: Un admin AVEC preview_paywall n'est PAS redirigé vers la vue interne
        Raison: En mode preview, l'admin doit rester sur la page publique pour voir le rendu paywall
        Features: lecon_publique_view, preview paywall, pas de redirect
        Criticité: haute
        """
        client.force_login(admin_user)
        session = client.session
        session["preview_paywall"] = True
        session.save()
        response = client.get(_url_publique(lecon_premium_courte))
        # Pas de 302, on reste sur la page publique
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_admin_avec_preview_context_est_floute_true(self, client, admin_user, lecon_premium_courte):
        """
        Teste: Le contexte template contient est_floute=True pour une leçon premium en preview paywall
        Raison: La variable de contexte pilote l'affichage du blur — elle doit être True en preview
        Features: lecon_publique_view, preview paywall, contexte template
        Criticité: moyenne
        """
        client.force_login(admin_user)
        session = client.session
        session["preview_paywall"] = True
        session.save()
        response = client.get(_url_publique(lecon_premium_courte))
        assert response.status_code == 200
        assert response.context["est_floute"] is True
        assert response.context["preview_paywall"] is True

    @pytest.mark.django_db
    def test_admin_avec_preview_lecon_gratuite_context_pas_floute(self, client, admin_user, lecon_gratuite):
        """
        Teste: Le contexte template contient est_floute=False pour une leçon gratuite en preview paywall
        Raison: Les leçons gratuites ne doivent jamais être floutées, même en preview
        Features: lecon_publique_view, preview paywall, contexte template
        Criticité: moyenne
        """
        client.force_login(admin_user)
        session = client.session
        session["preview_paywall"] = True
        session.save()
        response = client.get(_url_publique(lecon_gratuite))
        assert response.status_code == 200
        assert response.context["est_floute"] is False


# ===========================================================================
# Tests Paywall Preview Redirect from Internal Views (lecon_view, quiz_view, lecon_pdf_view)
# ===========================================================================


class TestPaywallPreviewRedirectFromInternalViews:
    """Tests : les vues internes redirigent vers lecon_publique quand preview_paywall est actif."""

    def _url_lecon(self, lecon):
        return reverse("lecon", kwargs={"lecon_pk": lecon.pk})

    def _url_quiz(self, lecon):
        return reverse("quiz", kwargs={"lecon_pk": lecon.pk})

    def _url_pdf(self, lecon):
        return reverse("lecon_pdf", kwargs={"lecon_pk": lecon.pk})

    def _expected_redirect(self, lecon):
        ch = lecon.chapitre
        return reverse("lecon_publique", kwargs={
            "matiere_slug": ch.matiere.slug,
            "niveau": ch.niveau,
            "chapitre_slug": ch.slug,
            "lecon_slug": lecon.slug,
        })

    def _activate_preview_paywall(self, client):
        session = client.session
        session["preview_paywall"] = True
        session.save()

    # ---- lecon_view ----

    @pytest.mark.django_db
    def test_lecon_view_preview_paywall_premium_redirige(self, client, admin_user, lecon_premium_courte):
        """
        Teste: Admin + preview_paywall actif + leçon premium → 302 vers lecon_publique
        Features: lecon_view, preview paywall, redirect
        Criticité: haute
        """
        client.force_login(admin_user)
        self._activate_preview_paywall(client)
        response = client.get(self._url_lecon(lecon_premium_courte))
        assert response.status_code == 302
        assert response["Location"] == self._expected_redirect(lecon_premium_courte)

    @pytest.mark.django_db
    def test_lecon_view_preview_paywall_gratuite_redirige(self, client, admin_user, lecon_gratuite):
        """
        Teste: Admin + preview_paywall actif + leçon gratuite → 302 vers lecon_publique aussi
        Features: lecon_view, preview paywall, redirect, leçon gratuite
        Criticité: haute
        """
        client.force_login(admin_user)
        self._activate_preview_paywall(client)
        response = client.get(self._url_lecon(lecon_gratuite))
        assert response.status_code == 302
        assert response["Location"] == self._expected_redirect(lecon_gratuite)

    @pytest.mark.django_db
    def test_lecon_view_sans_preview_paywall_pas_de_redirect(self, client, admin_user, lecon_premium_courte):
        """
        Teste: Admin SANS preview_paywall → 200 (comportement normal)
        Features: lecon_view, pas de preview paywall
        Criticité: haute
        """
        client.force_login(admin_user)
        response = client.get(self._url_lecon(lecon_premium_courte))
        assert response.status_code == 200

    # ---- quiz_view ----

    @pytest.mark.django_db
    def test_quiz_view_preview_paywall_redirige(self, client, admin_user, lecon_premium_courte):
        """
        Teste: Admin + preview_paywall actif → 302 vers lecon_publique depuis quiz_view
        Features: quiz_view, preview paywall, redirect
        Criticité: haute
        """
        from courses.models import Quiz
        Quiz.objects.create(lecon=lecon_premium_courte, titre="Quiz test", score_minimum=60.0)
        client.force_login(admin_user)
        self._activate_preview_paywall(client)
        response = client.get(self._url_quiz(lecon_premium_courte))
        assert response.status_code == 302
        assert response["Location"] == self._expected_redirect(lecon_premium_courte)

    @pytest.mark.django_db
    def test_quiz_view_sans_preview_paywall_pas_de_redirect(self, client, admin_user, lecon_premium_courte):
        """
        Teste: Admin SANS preview_paywall sur quiz_view → 200
        Features: quiz_view, pas de preview paywall
        Criticité: haute
        """
        from courses.models import Quiz, Question
        quiz = Quiz.objects.create(lecon=lecon_premium_courte, titre="Quiz test", score_minimum=60.0)
        Question.objects.create(
            quiz=quiz, ordre=1, texte="Q?", type="qcm",
            options=["A", "B"], reponse_correcte="0", points=1,
        )
        client.force_login(admin_user)
        response = client.get(self._url_quiz(lecon_premium_courte))
        assert response.status_code == 200

    # ---- lecon_pdf_view ----

    @pytest.mark.django_db
    def test_pdf_view_preview_paywall_redirige(self, client, admin_user, lecon_premium_courte):
        """
        Teste: Admin + preview_paywall actif → 302 vers lecon_publique depuis lecon_pdf_view
        Features: lecon_pdf_view, preview paywall, redirect
        Criticité: haute
        """
        client.force_login(admin_user)
        self._activate_preview_paywall(client)
        response = client.get(self._url_pdf(lecon_premium_courte))
        assert response.status_code == 302
        assert response["Location"] == self._expected_redirect(lecon_premium_courte)

    # ---- Combinaison preview_paywall + preview_niveau ----

    @pytest.mark.django_db
    def test_lecon_view_preview_paywall_et_niveau_redirige(self, client, admin_user, lecon_premium_courte):
        """
        Teste: Admin + preview_paywall + preview_niveau=terminale + leçon premium → 302 vers lecon_publique
        Features: lecon_view, preview paywall, preview niveau, redirect
        Criticité: haute
        """
        client.force_login(admin_user)
        session = client.session
        session["preview_paywall"] = True
        session["preview_niveau"] = "terminale"
        session.save()
        response = client.get(self._url_lecon(lecon_premium_courte))
        assert response.status_code == 302
        assert response["Location"] == self._expected_redirect(lecon_premium_courte)
