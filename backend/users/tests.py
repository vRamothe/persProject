import pytest
from django.test import Client
from django.urls import reverse
from django.core import signing
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


class TestAccessControl:
    def test_connexion_page_accessible_anonymous(self, client):
        response = client.get(reverse("connexion"))
        assert response.status_code == 200

    def test_inscription_page_accessible_anonymous(self, client):
        response = client.get(reverse("inscription"))
        assert response.status_code == 200

    def test_dashboard_redirects_anonymous_to_login(self, client):
        response = client.get(reverse("tableau_de_bord"))
        assert response.status_code == 302
        assert "connexion" in response.url

    def test_profil_requires_login(self, client):
        response = client.get(reverse("profil"))
        assert response.status_code == 302
        assert "connexion" in response.url

    def test_admin_panel_forbidden_for_eleve(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("admin_utilisateurs"))
        # Non-admin gets redirected to dashboard
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    def test_admin_panel_accessible_for_admin(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 200


class TestInscription:
    def test_inscription_creates_eleve(self, client, db):
        response = client.post(reverse("inscription"), {
            "email": "nouveau@test.com",
            "prenom": "Marie",
            "nom": "Martin",
            "niveau": "seconde",
            "password1": "SecurePass99!",
            "password2": "SecurePass99!",
        })
        assert response.status_code == 302
        user = CustomUser.objects.get(email="nouveau@test.com")
        assert user.role == "eleve"
        assert user.niveau == "seconde"

    def test_inscription_user_is_inactive_after_registration(self, client, db):
        client.post(reverse("inscription"), {
            "email": "inactive@test.com",
            "prenom": "Lucie",
            "nom": "Fontaine",
            "niveau": "premiere",
            "password1": "SecurePass99!",
            "password2": "SecurePass99!",
        })
        user = CustomUser.objects.get(email="inactive@test.com")
        assert user.is_active is False

    def test_inscription_sends_verification_email(self, client, db):
        from django.core import mail
        client.post(reverse("inscription"), {
            "email": "veriftest@test.com",
            "prenom": "Pierre",
            "nom": "Leclerc",
            "niveau": "terminale",
            "password1": "SecurePass99!",
            "password2": "SecurePass99!",
        })
        assert len(mail.outbox) == 1
        assert "veriftest@test.com" in mail.outbox[0].to
        assert "verifier-email" in mail.outbox[0].body

    def test_valid_token_activates_account(self, client, db):
        user = CustomUser.objects.create_user(
            email="toactivate@test.com", password="pass", prenom="A", nom="B",
            role="eleve", niveau="seconde", is_active=False,
        )
        token = signing.dumps(user.pk, salt="email-verification")
        response = client.get(reverse("verifier_email", kwargs={"token": token}))
        assert response.status_code == 302
        user.refresh_from_db()
        assert user.is_active is True

    def test_tampered_token_returns_400(self, client, db):
        response = client.get(reverse("verifier_email", kwargs={"token": "completely-invalid"}))
        assert response.status_code == 400

    def test_inscription_confirmation_page_accessible(self, client):
        response = client.get(reverse("inscription_confirmation"))
        assert response.status_code == 200


class TestInscriptionFormValidation:
    """Unit tests for InscriptionForm validation logic."""

    def _valid_data(self, **overrides):
        data = {
            "email": "test@example.com",
            "prenom": "Marie",
            "nom": "Dupont",
            "niveau": "seconde",
            "password1": "SecurePass99!",
            "password2": "SecurePass99!",
        }
        data.update(overrides)
        return data

    @pytest.mark.django_db
    def test_password_too_short_rejected(self):
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(password1="Ab1", password2="Ab1"))
        assert form.is_valid() is False
        assert "password1" in form.errors

    @pytest.mark.django_db
    def test_password_no_uppercase_rejected(self):
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(password1="securepass99!", password2="securepass99!"))
        assert form.is_valid() is False
        assert "password1" in form.errors

    @pytest.mark.django_db
    def test_password_no_digit_rejected(self):
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(password1="SecurePass!", password2="SecurePass!"))
        assert form.is_valid() is False
        assert "password1" in form.errors

    @pytest.mark.django_db
    def test_passwords_mismatch_rejected(self):
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(password1="SecurePass99!", password2="Different99!"))
        assert form.is_valid() is False
        assert "password2" in form.errors

    @pytest.mark.django_db
    def test_duplicate_email_rejected(self):
        from users.forms import InscriptionForm
        CustomUser.objects.create_user(
            email="test@example.com", password="pass", role="eleve", niveau="seconde",
        )
        form = InscriptionForm(data=self._valid_data())
        assert form.is_valid() is False
        assert "email" in form.errors

    @pytest.mark.django_db
    def test_niveau_required(self):
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data(niveau=""))
        assert form.is_valid() is False
        assert "niveau" in form.errors

    @pytest.mark.django_db
    def test_valid_form_creates_user(self):
        from users.forms import InscriptionForm
        form = InscriptionForm(data=self._valid_data())
        assert form.is_valid() is True
        user = form.save()
        assert user.role == "eleve"
        assert user.niveau == "seconde"
        assert user.email == "test@example.com"

    @pytest.mark.django_db
    def test_inscription_redirects_to_confirmation(self, client):
        response = client.post(reverse("inscription"), self._valid_data())
        assert response.status_code == 302
        assert "confirmation" in response.url


class TestProfilFormValidation:
    """Unit tests for ProfilForm validation logic."""

    @pytest.mark.django_db
    def test_profil_form_valid(self, eleve):
        from users.forms import ProfilForm
        form = ProfilForm(
            data={"prenom": "Jean", "nom": "Dupont", "email": "eleve@test.com", "niveau": "terminale"},
            instance=eleve,
        )
        assert form.is_valid() is True

    @pytest.mark.django_db
    def test_profil_form_email_required(self, eleve):
        from users.forms import ProfilForm
        form = ProfilForm(
            data={"prenom": "Jean", "nom": "Dupont", "email": "", "niveau": "terminale"},
            instance=eleve,
        )
        assert form.is_valid() is False
        assert "email" in form.errors

    @pytest.mark.django_db
    def test_profil_form_saves_changes(self, eleve):
        from users.forms import ProfilForm
        form = ProfilForm(
            data={"prenom": "Pierre", "nom": "Martin", "email": "eleve@test.com", "niveau": "premiere"},
            instance=eleve,
        )
        assert form.is_valid() is True
        form.save()
        eleve.refresh_from_db()
        assert eleve.prenom == "Pierre"
        assert eleve.nom == "Martin"
        assert eleve.niveau == "premiere"


class TestMotDePasseFormValidation:
    """Unit tests for MotDePasseForm validation logic."""

    def test_mdp_form_valid(self):
        from users.forms import MotDePasseForm
        form = MotDePasseForm(data={
            "ancien": "OldPass123!",
            "nouveau1": "NewSecure99!",
            "nouveau2": "NewSecure99!",
        })
        assert form.is_valid() is True

    def test_mdp_form_mismatch(self):
        from users.forms import MotDePasseForm
        form = MotDePasseForm(data={
            "ancien": "OldPass123!",
            "nouveau1": "NewSecure99!",
            "nouveau2": "Different99!",
        })
        assert form.is_valid() is False
        assert "__all__" in form.errors

    def test_mdp_form_too_short(self):
        from users.forms import MotDePasseForm
        form = MotDePasseForm(data={
            "ancien": "OldPass123!",
            "nouveau1": "Ab1",
            "nouveau2": "Ab1",
        })
        assert form.is_valid() is False


class TestConnexionView:
    """Tests for the ConnexionView (login page)."""

    def test_connexion_page_renders_form(self, client):
        response = client.get(reverse("connexion"))
        assert response.status_code == 200
        content = response.content.decode()
        assert "Connexion" in content or "form" in content

    @pytest.mark.django_db
    def test_connexion_post_invalid_credentials(self, client):
        response = client.post(reverse("connexion"), {
            "username": "fake@test.com",
            "password": "wrongpassword",
        })
        # Invalid creds re-render the form (200), not redirect (302)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authenticated_user_redirected_from_connexion(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("connexion"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url


class TestPasswordReset:
    def test_password_reset_page_accessible(self, client):
        response = client.get(reverse("password_reset"))
        assert response.status_code == 200

    def test_password_reset_done_page_accessible(self, client):
        response = client.get(reverse("password_reset_done"))
        assert response.status_code == 200

    def test_password_reset_complete_page_accessible(self, client):
        response = client.get(reverse("password_reset_complete"))
        assert response.status_code == 200


class TestAdminAnalytics:
    def test_anonymous_redirected(self, client):
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 302

    def test_eleve_redirected_to_dashboard(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 302

    def test_admin_gets_200(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 200

    def test_weak_questions_in_context(self, client, admin_user, db):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question
        from progress.models import UserQuestionHistorique
        client.force_login(admin_user)
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="T", ordre=1)
        lecon = Lecon.objects.create(chapitre=chap, titre="L", contenu="c", ordre=1)
        quiz = Quiz.objects.create(lecon=lecon, titre="Q")
        q = Question.objects.create(quiz=quiz, texte="?", type="qcm", reponse_correcte="0", ordre=1)
        UserQuestionHistorique.objects.create(
            user=admin_user, question=q, boite=1,
            prochaine_revision="2024-01-01", nb_bonnes=0, nb_total=5,
        )
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 200
        assert "weak_questions" in response.context

    def test_empty_db_does_not_crash(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get(reverse("admin_analytics"))
        assert response.status_code == 200


class TestHealthCheck:
    def test_health_returns_200(self, client):
        response = client.get(reverse("health"))
        assert response.status_code == 200

    def test_health_content_type_json(self, client):
        response = client.get(reverse("health"))
        assert "application/json" in response["Content-Type"]

    def test_health_body(self, client):
        import json
        response = client.get(reverse("health"))
        data = json.loads(response.content)
        assert data == {"status": "ok"}


# ============================================================
# Batch 4 — Admin panel views + Preview mode
# ============================================================


class TestAdminUtilisateurs:
    """Tests for the admin_utilisateurs view (user management list)."""

    @pytest.mark.django_db
    def test_eleve_cannot_access(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_gets_200(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_filters_by_niveau(self, client, admin_user):
        CustomUser.objects.create_user(
            email="sec@t.com", password="p", prenom="A", nom="Sec",
            role="eleve", niveau="seconde",
        )
        CustomUser.objects.create_user(
            email="term@t.com", password="p", prenom="B", nom="Term",
            role="eleve", niveau="terminale",
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"), {"niveau": "seconde"})
        assert response.status_code == 200
        eleves = response.context["eleves"]
        assert all(e.niveau == "seconde" for e in eleves)
        assert any(e.email == "sec@t.com" for e in eleves)

    @pytest.mark.django_db
    def test_filters_by_actif(self, client, admin_user):
        active = CustomUser.objects.create_user(
            email="act@t.com", password="p", prenom="A", nom="Act",
            role="eleve", niveau="seconde", is_active=True,
        )
        inactive = CustomUser.objects.create_user(
            email="inact@t.com", password="p", prenom="B", nom="Inact",
            role="eleve", niveau="seconde", is_active=False,
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"), {"actif": "1"})
        assert response.status_code == 200
        eleves = response.context["eleves"]
        emails = [e.email for e in eleves]
        assert active.email in emails
        assert inactive.email not in emails

    @pytest.mark.django_db
    def test_search_by_name(self, client, admin_user):
        CustomUser.objects.create_user(
            email="unique@t.com", password="p", prenom="A", nom="UniqueNom",
            role="eleve", niveau="seconde",
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"), {"q": "UniqueNom"})
        assert response.status_code == 200
        eleves = response.context["eleves"]
        assert any(e.nom == "UniqueNom" for e in eleves)

    @pytest.mark.django_db
    def test_empty_search_returns_all(self, client, admin_user):
        CustomUser.objects.create_user(
            email="e1@t.com", password="p", prenom="A", nom="A",
            role="eleve", niveau="seconde",
        )
        CustomUser.objects.create_user(
            email="e2@t.com", password="p", prenom="B", nom="B",
            role="eleve", niveau="terminale",
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        assert response.status_code == 200
        eleves = response.context["eleves"]
        assert len(eleves) >= 2

    @pytest.mark.django_db
    def test_context_has_progression_pct(self, client, admin_user):
        CustomUser.objects.create_user(
            email="prog@t.com", password="p", prenom="A", nom="Prog",
            role="eleve", niveau="seconde",
        )
        client.force_login(admin_user)
        response = client.get(reverse("admin_utilisateurs"))
        eleves = response.context["eleves"]
        assert len(eleves) >= 1
        assert hasattr(eleves[0], "progression_pct")


class TestAdminToggleActif:
    """Tests for the admin_toggle_actif view."""

    @pytest.mark.django_db
    def test_eleve_cannot_toggle(self, client, eleve):
        client.force_login(eleve)
        url = reverse("admin_toggle_actif", kwargs={"user_id": eleve.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_toggles_active_to_inactive(self, client, admin_user, eleve):
        assert eleve.is_active is True
        client.force_login(admin_user)
        url = reverse("admin_toggle_actif", kwargs={"user_id": eleve.pk})
        response = client.post(url)
        assert response.status_code == 302
        eleve.refresh_from_db()
        assert eleve.is_active is False

    @pytest.mark.django_db
    def test_admin_toggles_inactive_to_active(self, client, admin_user):
        inactive_eleve = CustomUser.objects.create_user(
            email="off@t.com", password="p", prenom="A", nom="Off",
            role="eleve", niveau="seconde", is_active=False,
        )
        client.force_login(admin_user)
        url = reverse("admin_toggle_actif", kwargs={"user_id": inactive_eleve.pk})
        response = client.post(url)
        assert response.status_code == 302
        inactive_eleve.refresh_from_db()
        assert inactive_eleve.is_active is True

    @pytest.mark.django_db
    def test_get_request_redirects(self, client, admin_user, eleve):
        client.force_login(admin_user)
        url = reverse("admin_toggle_actif", kwargs={"user_id": eleve.pk})
        response = client.get(url)
        assert response.status_code == 302
        # GET should NOT toggle is_active
        eleve.refresh_from_db()
        assert eleve.is_active is True


class TestAdminEleveDetail:
    """Tests for the admin_eleve_detail view."""

    @pytest.mark.django_db
    def test_eleve_cannot_access(self, client, eleve):
        client.force_login(eleve)
        url = reverse("admin_eleve_detail", kwargs={"user_id": eleve.pk})
        response = client.get(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_gets_200(self, client, admin_user, eleve):
        client.force_login(admin_user)
        url = reverse("admin_eleve_detail", kwargs={"user_id": eleve.pk})
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_context_has_progression_data(self, client, admin_user, eleve):
        client.force_login(admin_user)
        url = reverse("admin_eleve_detail", kwargs={"user_id": eleve.pk})
        response = client.get(url)
        assert "progression_globale" in response.context
        assert "eleve" in response.context

    @pytest.mark.django_db
    def test_nonexistent_user_returns_404(self, client, admin_user):
        client.force_login(admin_user)
        url = reverse("admin_eleve_detail", kwargs={"user_id": 99999})
        response = client.get(url)
        assert response.status_code == 404


class TestAdminToggleChapitre:
    """Tests for the admin_toggle_chapitre view."""

    @pytest.mark.django_db
    def test_eleve_cannot_toggle_chapitre(self, client, eleve):
        from courses.models import Matiere, Chapitre
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="Ch", ordre=1)
        client.force_login(eleve)
        url = reverse("admin_toggle_chapitre", kwargs={"user_id": eleve.pk, "chapitre_id": chap.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_unlocks_chapitre(self, client, admin_user, eleve):
        from courses.models import Matiere, Chapitre
        from progress.models import ChapitreDebloque
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="Ch", ordre=1)
        assert ChapitreDebloque.objects.filter(user=eleve, chapitre=chap).count() == 0
        client.force_login(admin_user)
        url = reverse("admin_toggle_chapitre", kwargs={"user_id": eleve.pk, "chapitre_id": chap.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert ChapitreDebloque.objects.filter(user=eleve, chapitre=chap).count() == 1

    @pytest.mark.django_db
    def test_admin_locks_chapitre(self, client, admin_user, eleve):
        from courses.models import Matiere, Chapitre
        from progress.models import ChapitreDebloque
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="Ch", ordre=1)
        ChapitreDebloque.objects.create(user=eleve, chapitre=chap)
        client.force_login(admin_user)
        url = reverse("admin_toggle_chapitre", kwargs={"user_id": eleve.pk, "chapitre_id": chap.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert ChapitreDebloque.objects.filter(user=eleve, chapitre=chap).count() == 0

    @pytest.mark.django_db
    def test_get_request_redirects(self, client, admin_user, eleve):
        from courses.models import Matiere, Chapitre
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(matiere=mat, niveau="terminale", titre="Ch", ordre=1)
        client.force_login(admin_user)
        url = reverse("admin_toggle_chapitre", kwargs={"user_id": eleve.pk, "chapitre_id": chap.pk})
        response = client.get(url)
        assert response.status_code == 302


class TestPreviewMode:
    """Tests for preview_niveau_view and exit_preview_view."""

    @pytest.mark.django_db
    def test_eleve_cannot_activate_preview(self, client, eleve):
        client.force_login(eleve)
        url = reverse("preview_niveau", kwargs={"niveau": "seconde"})
        response = client.get(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_admin_activates_preview(self, client, admin_user):
        client.force_login(admin_user)
        url = reverse("preview_niveau", kwargs={"niveau": "seconde"})
        response = client.get(url)
        assert response.status_code == 302
        assert "cours" in response.url  # redirects to matieres
        session = client.session
        assert session.get("preview_niveau") == "seconde"

    @pytest.mark.django_db
    def test_invalid_niveau_redirects(self, client, admin_user):
        client.force_login(admin_user)
        url = reverse("preview_niveau", kwargs={"niveau": "invalid"})
        response = client.get(url)
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_exit_preview_clears_session(self, client, admin_user):
        client.force_login(admin_user)
        session = client.session
        session["preview_niveau"] = "seconde"
        session.save()
        response = client.get(reverse("exit_preview"))
        assert response.status_code == 302
        assert "preview_niveau" not in client.session

    @pytest.mark.django_db
    def test_exit_preview_redirects_to_dashboard(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get(reverse("exit_preview"))
        assert response.status_code == 302
        assert "tableau-de-bord" in response.url

    @pytest.mark.django_db
    def test_preview_mode_lecon_no_progression_write(self, client, admin_user):
        """In preview mode, visiting a lecon should NOT create UserProgression."""
        from courses.models import Matiere, Chapitre, Lecon
        from progress.models import UserProgression
        mat = Matiere.objects.create(nom="physique")
        chap = Chapitre.objects.create(
            matiere=mat, niveau="seconde", titre="Preview Ch", ordre=1,
        )
        lecon = Lecon.objects.create(
            chapitre=chap, ordre=1, titre="Preview Lecon",
            contenu="# Test", duree_estimee=10,
        )
        client.force_login(admin_user)
        # Activate preview mode
        session = client.session
        session["preview_niveau"] = "seconde"
        session.save()
        url = reverse("lecon", kwargs={"lecon_pk": lecon.pk})
        response = client.get(url)
        assert response.status_code == 200
        assert UserProgression.objects.filter(user=admin_user, lecon=lecon).count() == 0


# ============================================================
# Batch 5 — ProfilView
# ============================================================


class TestProfilView:
    """Tests for the ProfilView CBV (profile + password change)."""

    @pytest.mark.django_db
    def test_profil_requires_login(self, client):
        response = client.get(reverse("profil"))
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]

    @pytest.mark.django_db
    def test_profil_get_returns_200(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("profil"))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_profil_get_has_forms_in_context(self, client, eleve):
        client.force_login(eleve)
        response = client.get(reverse("profil"))
        assert "form_profil" in response.context
        assert "form_mdp" in response.context

    @pytest.mark.django_db
    def test_profil_update_nom_prenom(self, client, eleve):
        client.force_login(eleve)
        data = {
            "action": "profil",
            "prenom": "NouveauPrenom",
            "nom": "NouveauNom",
            "email": eleve.email,
            "niveau": eleve.niveau,
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 302
        eleve.refresh_from_db()
        assert eleve.prenom == "NouveauPrenom"
        assert eleve.nom == "NouveauNom"

    @pytest.mark.django_db
    def test_profil_update_invalid_email(self, client, eleve):
        client.force_login(eleve)
        data = {
            "action": "profil",
            "prenom": "Jean",
            "nom": "Dupont",
            "email": "",
            "niveau": eleve.niveau,
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 200
        assert response.context["form_profil"].errors

    @pytest.mark.django_db
    def test_password_change_success(self, client, eleve):
        client.force_login(eleve)
        data = {
            "action": "mot_de_passe",
            "ancien": "TestPass123!",
            "nouveau1": "NewSecure88!",
            "nouveau2": "NewSecure88!",
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 302
        eleve.refresh_from_db()
        assert eleve.check_password("NewSecure88!")

    @pytest.mark.django_db
    def test_password_change_wrong_ancien(self, client, eleve):
        client.force_login(eleve)
        data = {
            "action": "mot_de_passe",
            "ancien": "WrongOldPass!",
            "nouveau1": "NewSecure88!",
            "nouveau2": "NewSecure88!",
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 200
        assert "ancien" in response.context["form_mdp"].errors

    @pytest.mark.django_db
    def test_password_change_mismatch(self, client, eleve):
        client.force_login(eleve)
        data = {
            "action": "mot_de_passe",
            "ancien": "TestPass123!",
            "nouveau1": "NewSecure88!",
            "nouveau2": "DifferentPass99!",
        }
        response = client.post(reverse("profil"), data)
        assert response.status_code == 200


# ---------------------------------------------------------------------------
# Stripe Integration Tests
# ---------------------------------------------------------------------------

import json
from unittest.mock import patch, MagicMock
from users.models import Abonnement
from courses.models import Matiere, Chapitre, Lecon


@pytest.fixture
def eleve_stripe(db):
    return CustomUser.objects.create_user(
        email="stripe_eleve@test.com",
        password="TestPass123!",
        prenom="Marie",
        nom="Curie",
        role="eleve",
        niveau="terminale",
    )


@pytest.fixture
def admin_stripe(db):
    return CustomUser.objects.create_user(
        email="stripe_admin@test.com",
        password="AdminPass123!",
        prenom="Admin",
        nom="Stripe",
        role="admin",
        is_staff=True,
    )


@pytest.fixture
def matiere_stripe(db):
    return Matiere.objects.create(nom="physique")


@pytest.fixture
def chapitre_stripe(db, matiere_stripe):
    return Chapitre.objects.create(
        matiere=matiere_stripe,
        niveau="terminale",
        ordre=1,
        titre="Mécanique",
        description="Chapitre mécanique",
    )


@pytest.fixture
def lecon_premium(db, chapitre_stripe):
    return Lecon.objects.create(
        chapitre=chapitre_stripe,
        ordre=1,
        titre="Forces et interactions",
        contenu="# Forces\n\nContenu premium.",
        duree_estimee=30,
        gratuit=False,
    )


@pytest.fixture
def lecon_gratuite_stripe(db, chapitre_stripe):
    return Lecon.objects.create(
        chapitre=chapitre_stripe,
        ordre=2,
        titre="Introduction mécanique",
        contenu="# Intro\n\nContenu gratuit.",
        duree_estimee=15,
        gratuit=True,
    )


@pytest.fixture
def abonnement_actif(db, eleve_stripe):
    from django.utils import timezone

    return Abonnement.objects.create(
        user=eleve_stripe,
        stripe_customer_id="cus_test123",
        stripe_subscription_id="sub_test123",
        plan="mensuel",
        statut="actif",
        date_debut=timezone.now(),
    )


class TestStripeCheckout:
    @pytest.mark.django_db
    @patch("users.views.stripe.checkout.Session.create")
    @patch("users.views.stripe.Customer.create")
    def test_creer_checkout_session_redirects_to_stripe(
        self, mock_customer_create, mock_session_create, client, eleve_stripe
    ):
        mock_customer_create.return_value = MagicMock(id="cus_new123")
        mock_session = MagicMock()
        mock_session.url = "https://checkout.stripe.com/test_session"
        mock_session_create.return_value = mock_session

        client.force_login(eleve_stripe)
        response = client.post(reverse("checkout"), {"plan": "mensuel"})
        assert response.status_code == 302
        assert response["Location"] == "https://checkout.stripe.com/test_session"
        mock_session_create.assert_called_once()

    @pytest.mark.django_db
    @patch("users.views.stripe.checkout.Session.create")
    @patch("users.views.stripe.Customer.create")
    def test_creer_checkout_session_annual(
        self, mock_customer_create, mock_session_create, client, eleve_stripe, settings
    ):
        mock_customer_create.return_value = MagicMock(id="cus_new456")
        mock_session = MagicMock()
        mock_session.url = "https://checkout.stripe.com/annual_session"
        mock_session_create.return_value = mock_session

        settings.STRIPE_PRICE_ANNUAL = "price_annual_test"

        client.force_login(eleve_stripe)
        response = client.post(reverse("checkout"), {"plan": "annuel"})
        assert response.status_code == 302

        call_kwargs = mock_session_create.call_args[1]
        assert call_kwargs["line_items"][0]["price"] == "price_annual_test"

    @pytest.mark.django_db
    def test_checkout_requires_login(self, client):
        response = client.post(reverse("checkout"), {"plan": "mensuel"})
        assert response.status_code == 302
        assert "/connexion/" in response["Location"]


class TestStripeWebhook:
    def _build_webhook_payload(self, event_type, data_object, event_id="evt_test1"):
        return {
            "id": event_id,
            "type": event_type,
            "data": {"object": data_object},
        }

    @pytest.mark.django_db
    @patch("users.views.stripe.Webhook.construct_event")
    def test_webhook_checkout_completed_creates_abonnement(
        self, mock_construct, client, eleve_stripe
    ):
        event_data = self._build_webhook_payload(
            "checkout.session.completed",
            {
                "metadata": {
                    "user_id": str(eleve_stripe.pk),
                    "plan": "mensuel",
                },
                "customer": "cus_webhook123",
                "subscription": "sub_webhook123",
            },
        )
        mock_construct.return_value = event_data

        response = client.post(
            reverse("stripe_webhook"),
            data=json.dumps(event_data),
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="sig_test",
        )
        assert response.status_code == 200

        abo = Abonnement.objects.get(user=eleve_stripe)
        assert abo.statut == "actif"
        assert abo.stripe_customer_id == "cus_webhook123"
        assert abo.stripe_subscription_id == "sub_webhook123"
        assert abo.plan == "mensuel"

    @pytest.mark.django_db
    @patch("users.views.stripe.Webhook.construct_event")
    def test_webhook_subscription_deleted_deactivates(
        self, mock_construct, client, eleve_stripe, abonnement_actif
    ):
        event_data = self._build_webhook_payload(
            "customer.subscription.deleted",
            {
                "id": "sub_test123",
                "status": "canceled",
            },
        )
        mock_construct.return_value = event_data

        response = client.post(
            reverse("stripe_webhook"),
            data=json.dumps(event_data),
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="sig_test",
        )
        assert response.status_code == 200

        abonnement_actif.refresh_from_db()
        assert abonnement_actif.statut == "annule"

    @pytest.mark.django_db
    @patch("users.views.stripe.Webhook.construct_event")
    def test_webhook_rejects_invalid_signature(self, mock_construct, client):
        import stripe as _stripe

        mock_construct.side_effect = _stripe.error.SignatureVerificationError(
            "Invalid signature", "sig_header"
        )

        response = client.post(
            reverse("stripe_webhook"),
            data=b"bad_payload",
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="bad_sig",
        )
        assert response.status_code == 400

    @pytest.mark.django_db
    @patch("users.views.stripe.Webhook.construct_event")
    def test_webhook_idempotent_on_duplicate_event(
        self, mock_construct, client, eleve_stripe
    ):
        event_data = self._build_webhook_payload(
            "checkout.session.completed",
            {
                "metadata": {
                    "user_id": str(eleve_stripe.pk),
                    "plan": "annuel",
                },
                "customer": "cus_idem123",
                "subscription": "sub_idem123",
            },
            event_id="evt_duplicate",
        )
        mock_construct.return_value = event_data

        for _ in range(2):
            response = client.post(
                reverse("stripe_webhook"),
                data=json.dumps(event_data),
                content_type="application/json",
                HTTP_STRIPE_SIGNATURE="sig_test",
            )
            assert response.status_code == 200

        assert Abonnement.objects.filter(user=eleve_stripe).count() == 1


class TestPremiumLessonAccess:
    def _lecon_publique_url(self, matiere, lecon):
        return reverse(
            "lecon_publique",
            kwargs={
                "matiere_slug": matiere.slug,
                "niveau": lecon.chapitre.niveau,
                "chapitre_slug": lecon.chapitre.slug,
                "lecon_slug": lecon.slug,
            },
        )

    @pytest.mark.django_db
    def test_premium_lesson_requires_active_subscription(
        self, client, eleve_stripe, matiere_stripe, lecon_premium
    ):
        client.force_login(eleve_stripe)
        url = self._lecon_publique_url(matiere_stripe, lecon_premium)
        response = client.get(url)
        assert response.status_code == 200
        assert response.context["est_floute"] is True

    @pytest.mark.django_db
    def test_premium_lesson_accessible_with_active_subscription(
        self, client, eleve_stripe, matiere_stripe, lecon_premium, abonnement_actif
    ):
        client.force_login(eleve_stripe)
        url = self._lecon_publique_url(matiere_stripe, lecon_premium)
        response = client.get(url)
        assert response.status_code == 200
        assert response.context["est_floute"] is False

    @pytest.mark.django_db
    def test_admin_bypasses_subscription_check(
        self, client, admin_stripe, matiere_stripe, lecon_premium
    ):
        client.force_login(admin_stripe)
        url = self._lecon_publique_url(matiere_stripe, lecon_premium)
        response = client.get(url)
        # Admin gets redirected to internal lecon view
        assert response.status_code == 302
        expected_url = reverse("lecon", kwargs={"lecon_pk": lecon_premium.pk})
        assert response["Location"] == expected_url


class TestPortailClient:
    @pytest.mark.django_db
    @patch("users.views.stripe.billing_portal.Session.create")
    def test_portail_client_redirects_to_stripe(
        self, mock_portal_create, client, eleve_stripe, abonnement_actif
    ):
        mock_session = MagicMock()
        mock_session.url = "https://billing.stripe.com/portal_session"
        mock_portal_create.return_value = mock_session

        client.force_login(eleve_stripe)
        response = client.get(reverse("portail_abonnement"))
        assert response.status_code == 302
        assert response["Location"] == "https://billing.stripe.com/portal_session"

    @pytest.mark.django_db
    def test_portail_client_no_subscription(self, client, eleve_stripe):
        client.force_login(eleve_stripe)
        response = client.get(reverse("portail_abonnement"))
        assert response.status_code == 302
        assert "/profil/" in response["Location"]


class TestUserHasActiveSubscription:
    @pytest.mark.django_db
    def test_user_has_active_subscription_true(self, eleve_stripe, abonnement_actif):
        from users.views import _user_has_active_subscription

        assert _user_has_active_subscription(eleve_stripe) is True

    @pytest.mark.django_db
    def test_user_has_active_subscription_false(self, eleve_stripe):
        from users.views import _user_has_active_subscription

        assert _user_has_active_subscription(eleve_stripe) is False

    @pytest.mark.django_db
    def test_user_has_active_subscription_annule(self, eleve_stripe, abonnement_actif):
        from users.views import _user_has_active_subscription

        abonnement_actif.statut = "annule"
        abonnement_actif.save()
        assert _user_has_active_subscription(eleve_stripe) is False


