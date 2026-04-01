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
        """Contenu < 2000 mots → retourné intact, a_ete_tronque=False."""
        contenu = "Un deux trois quatre cinq."
        resultat, a_ete_tronque = tronquer_contenu_markdown(contenu)
        assert resultat == contenu
        assert a_ete_tronque is False

    def test_tronquer_contenu_long(self):
        """Contenu > 2000 mots → tronqué, a_ete_tronque=True, ≤ 2000 mots."""
        contenu = _generer_contenu_long(2500)
        resultat, a_ete_tronque = tronquer_contenu_markdown(contenu)
        assert a_ete_tronque is True
        nb_mots_resultat = len(resultat.split())
        assert nb_mots_resultat <= 2000

    def test_tronquer_coupe_sur_paragraphe(self):
        """La coupure se fait sur \\n\\n, pas au milieu d'une phrase."""
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
        """Contenu vide → retourné intact."""
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
        """GET leçon premium en anonyme → status 200 (plus de redirect)."""
        response = client.get(_url_publique(lecon_premium_courte))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_premium_lecon_publique_content_truncated(self, client, lecon_premium_longue):
        """GET leçon premium en anonyme → le texte au-delà des ~2000 mots est absent."""
        response = client.get(_url_publique(lecon_premium_longue))
        assert response.status_code == 200
        html = response.content.decode()
        assert "MOT_MARQUEUR_FIN" not in html

    @pytest.mark.django_db
    def test_premium_lecon_publique_blur_classes_present(self, client, lecon_premium_courte):
        """Le HTML contient la div paywall-blur-container pour une leçon premium en anonyme."""
        response = client.get(_url_publique(lecon_premium_courte))
        html = response.content.decode()
        # Vérifier la div blur (pas juste la définition CSS)
        assert 'class="px-6 py-6 paywall-blur-container"' in html

    @pytest.mark.django_db
    def test_premium_lecon_publique_cta_present(self, client, lecon_premium_courte):
        """Le bouton 'Débloquer cette leçon' est présent pour une leçon premium."""
        response = client.get(_url_publique(lecon_premium_courte))
        html = response.content.decode()
        assert "bloquer cette le" in html.lower()

    @pytest.mark.django_db
    def test_free_lecon_publique_no_blur(self, client, lecon_gratuite):
        """GET leçon gratuite → pas de div paywall-blur-container."""
        response = client.get(_url_publique(lecon_gratuite))
        assert response.status_code == 200
        html = response.content.decode()
        # La div blur ne doit pas être rendue (la CSS est toujours là, mais pas la div)
        assert 'class="px-6 py-6 paywall-blur-container"' not in html

    @pytest.mark.django_db
    def test_admin_redirected_to_lecon_view(self, client, admin_user, lecon_gratuite):
        """Un admin authentifié est redirigé vers la vue lecon PK."""
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
        """GET catalogue d'une matière avec leçon premium → 🔒 présent."""
        url = reverse("catalogue_matiere", kwargs={"matiere_slug": matiere.slug})
        response = client.get(url)
        assert response.status_code == 200
        html = response.content.decode()
        assert "🔒" in html

    @pytest.mark.django_db
    def test_catalogue_no_lock_on_free_lessons(self, client, matiere, chapitre):
        """GET catalogue avec uniquement des leçons gratuites → aucun 🔒."""
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
        """GET leçon premium en anonyme → composant Alpine showPaywall inclus."""
        response = client.get(_url_publique(lecon_premium_courte))
        assert response.status_code == 200
        html = response.content.decode()
        assert "showPaywall" in html

    @pytest.mark.django_db
    def test_accueil_shows_lock_icon_on_premium_lessons(self, client, lecon_premium_courte):
        """GET / en anonyme avec leçon premium → 🔒 présent."""
        response = client.get(reverse("home"))
        assert response.status_code == 200
        html = response.content.decode()
        assert "🔒" in html
