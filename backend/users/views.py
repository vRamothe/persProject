from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.db.models import Count, Avg

from .forms import ConnexionForm, InscriptionForm, ProfilForm, MotDePasseForm
from .models import CustomUser


class ConnexionView(View):
    template_name = "registration/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("tableau_de_bord")
        return render(request, self.template_name, {"form": ConnexionForm()})

    def post(self, request):
        form = ConnexionForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get("next", "tableau_de_bord")
            return redirect(next_url)
        return render(request, self.template_name, {"form": form})


class InscriptionView(View):
    template_name = "registration/register.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("tableau_de_bord")
        return render(request, self.template_name, {"form": InscriptionForm()})

    def post(self, request):
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Débloquer le 1er chapitre de chaque matière pour le niveau de l'élève
            _debloquer_premiers_chapitres(user)
            login(request, user)
            messages.success(request, f"Bienvenue {user.prenom} ! Votre compte a été créé avec succès.")
            return redirect("tableau_de_bord")
        return render(request, self.template_name, {"form": form})


def deconnexion_view(request):
    logout(request)
    return redirect("connexion")


@method_decorator(login_required, name="dispatch")
class TableauDeBordView(View):
    def get(self, request):
        user = request.user
        if user.is_admin:
            return _dashboard_admin(request)
        return _dashboard_eleve(request)


def _dashboard_eleve(request):
    from progress.models import UserProgression, UserQuizResultat, ChapitreDebloque, StatutLeconChoices
    from courses.models import Lecon, Chapitre

    user = request.user

    # Stats globales
    total_lecons = Lecon.objects.filter(chapitre__niveau=user.niveau).count()
    lecons_terminees = UserProgression.objects.filter(
        user=user, statut=StatutLeconChoices.TERMINE
    ).count()
    chapitres_debloques = ChapitreDebloque.objects.filter(user=user).count()
    resultats_quiz = UserQuizResultat.objects.filter(user=user)
    quiz_passes = resultats_quiz.filter(passe=True).count()
    score_moyen = resultats_quiz.aggregate(avg=Avg("score"))["avg"] or 0.0

    progression_globale = (lecons_terminees / total_lecons * 100) if total_lecons > 0 else 0.0

    # Activité récente
    activite_recente = (
        UserProgression.objects.filter(user=user)
        .select_related("lecon__chapitre__matiere")
        .order_by("-derniere_activite")[:5]
    )

    context = {
        "total_lecons": total_lecons,
        "lecons_terminees": lecons_terminees,
        "chapitres_debloques": chapitres_debloques,
        "quiz_passes": quiz_passes,
        "score_moyen": round(score_moyen, 1),
        "progression_globale": round(progression_globale, 1),
        "activite_recente": activite_recente,
    }
    return render(request, "dashboard/eleve.html", context)


def _dashboard_admin(request):
    from progress.models import UserProgression, UserQuizResultat, StatutLeconChoices
    from courses.models import Lecon, Chapitre, Matiere

    nb_eleves = CustomUser.objects.filter(role="eleve", is_active=True).count()
    nb_chapitres = Chapitre.objects.count()
    nb_lecons = Lecon.objects.count()
    nb_completions = UserProgression.objects.filter(statut=StatutLeconChoices.TERMINE).count()

    eleves_par_niveau = {
        "seconde": CustomUser.objects.filter(role="eleve", niveau="seconde").count(),
        "premiere": CustomUser.objects.filter(role="eleve", niveau="premiere").count(),
        "terminale": CustomUser.objects.filter(role="eleve", niveau="terminale").count(),
    }

    derniers_inscrits = CustomUser.objects.filter(role="eleve").order_by("-date_joined")[:8]

    context = {
        "nb_eleves": nb_eleves,
        "nb_chapitres": nb_chapitres,
        "nb_lecons": nb_lecons,
        "nb_completions": nb_completions,
        "eleves_par_niveau": eleves_par_niveau,
        "derniers_inscrits": derniers_inscrits,
    }
    return render(request, "dashboard/admin.html", context)


@method_decorator(login_required, name="dispatch")
class ProfilView(View):
    template_name = "users/profile.html"

    def get(self, request):
        return render(request, self.template_name, {
            "form_profil": ProfilForm(instance=request.user),
            "form_mdp": MotDePasseForm(),
        })

    def post(self, request):
        action = request.POST.get("action")
        if action == "profil":
            form = ProfilForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profil mis à jour avec succès.")
                return redirect("profil")
            return render(request, self.template_name, {
                "form_profil": form,
                "form_mdp": MotDePasseForm(),
            })
        elif action == "mot_de_passe":
            form = MotDePasseForm(request.POST)
            if form.is_valid():
                user = request.user
                if not user.check_password(form.cleaned_data["ancien"]):
                    form.add_error("ancien", "Le mot de passe actuel est incorrect.")
                    return render(request, self.template_name, {
                        "form_profil": ProfilForm(instance=user),
                        "form_mdp": form,
                    })
                user.set_password(form.cleaned_data["nouveau1"])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Mot de passe modifié avec succès.")
                return redirect("profil")
            return render(request, self.template_name, {
                "form_profil": ProfilForm(instance=request.user),
                "form_mdp": form,
            })
        return redirect("profil")


# ---- Vue Admin : gestion des utilisateurs ----

@login_required
def admin_utilisateurs(request):
    if not request.user.is_admin:
        return redirect("tableau_de_bord")

    niveau_filtre = request.GET.get("niveau", "")
    search = request.GET.get("q", "")
    actif_filtre = request.GET.get("actif", "")

    eleves = CustomUser.objects.filter(role="eleve")
    if niveau_filtre:
        eleves = eleves.filter(niveau=niveau_filtre)
    if actif_filtre == "1":
        eleves = eleves.filter(is_active=True)
    elif actif_filtre == "0":
        eleves = eleves.filter(is_active=False)
    if search:
        eleves = (
            eleves.filter(nom__icontains=search)
            | eleves.model.objects.filter(prenom__icontains=search, role="eleve")
            | eleves.model.objects.filter(email__icontains=search, role="eleve")
        ).distinct()
        if niveau_filtre:
            eleves = eleves.filter(niveau=niveau_filtre)

    eleves = list(eleves.order_by("nom", "prenom"))

    # Calcul progression par élève (batch, sans N+1)
    from progress.models import UserProgression, StatutLeconChoices
    from courses.models import Lecon
    from django.db.models import Count as DbCount

    done_by_user = dict(
        UserProgression.objects.filter(user__in=eleves, statut=StatutLeconChoices.TERMINE)
        .values("user_id")
        .annotate(c=DbCount("id"))
        .values_list("user_id", "c")
    )
    niveaux_presents = {e.niveau for e in eleves if e.niveau}
    total_by_niveau = {
        niv: Lecon.objects.filter(chapitre__niveau=niv).count()
        for niv in niveaux_presents
    }
    for eleve in eleves:
        total = total_by_niveau.get(eleve.niveau, 0)
        done = done_by_user.get(eleve.pk, 0)
        eleve.progression_pct = int(done / total * 100) if total > 0 else 0

    return render(request, "dashboard/admin_users.html", {
        "eleves": eleves,
        "niveau_filtre": niveau_filtre,
        "search": search,
        "actif_filtre": actif_filtre,
    })


@login_required
def admin_toggle_actif(request, user_id):
    if not request.user.is_admin:
        return redirect("tableau_de_bord")
    if request.method == "POST":
        eleve = get_object_or_404(CustomUser, id=user_id, role="eleve")
        eleve.is_active = not eleve.is_active
        eleve.save()
        statut = "activé" if eleve.is_active else "désactivé"
        messages.success(request, f"Le compte de {eleve.nom_complet} a été {statut}.")
    return redirect("admin_utilisateurs")


# ---- Prévisualisation élève ----

NIVEAUX_PREVIEW = ["seconde", "premiere", "terminale"]

@login_required
def preview_niveau_view(request, niveau):
    """Active la prévisualisation de l'interface élève pour un niveau donné."""
    if not request.user.is_admin:
        return redirect("tableau_de_bord")
    if niveau not in NIVEAUX_PREVIEW:
        return redirect("tableau_de_bord")
    request.session["preview_niveau"] = niveau
    return redirect("matieres")


@login_required
def exit_preview_view(request):
    """Quitte le mode prévisualisation et retourne au tableau de bord admin."""
    request.session.pop("preview_niveau", None)
    return redirect("tableau_de_bord")


# ---- Helpers ----

def _debloquer_premiers_chapitres(user):
    from courses.models import Chapitre
    from progress.models import ChapitreDebloque

    premiers = Chapitre.objects.filter(niveau=user.niveau, ordre=1)
    for chap in premiers:
        ChapitreDebloque.objects.get_or_create(user=user, chapitre=chap)
