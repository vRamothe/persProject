import logging

from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core import signing
from django.core.mail import send_mail
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.db.models import Avg
from django.db.models.functions import TruncDate

from .forms import ConnexionForm, InscriptionForm, ProfilForm, MotDePasseForm
from .models import CustomUser, ConnexionLog

logger = logging.getLogger(__name__)


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
            # Enregistrer la connexion
            ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR"))
            if ip:
                ip = ip.split(",")[0].strip()
            ConnexionLog.objects.create(user=user, ip=ip or None)
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
            user = form.save(commit=False)
            user.is_active = False  # attend la confirmation email
            user.save()
            # Débloquer le 1er chapitre de chaque matière pour le niveau de l'élève
            _debloquer_premiers_chapitres(user)
            _envoyer_email_verification(request, user)
            return redirect("inscription_confirmation")
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
    from progress.models import UserProgression, UserQuizResultat, ChapitreDebloque, StatutLeconChoices, UserQuestionHistorique
    from courses.models import Lecon, Chapitre, Matiere
    import json
    from datetime import date, timedelta

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

    # --- Per-subject stats ---
    matieres = Matiere.objects.all()
    matieres_stats = []
    for matiere in matieres:
        lecons_mat = Lecon.objects.filter(chapitre__matiere=matiere, chapitre__niveau=user.niveau)
        total_mat = lecons_mat.count()
        done_mat = UserProgression.objects.filter(
            user=user, lecon__in=lecons_mat, statut=StatutLeconChoices.TERMINE
        ).count()
        quiz_mat = UserQuizResultat.objects.filter(
            user=user, quiz__lecon__chapitre__matiere=matiere
        )
        score_mat = quiz_mat.aggregate(avg=Avg("score"))["avg"] or 0.0
        if total_mat > 0:
            matieres_stats.append({
                "matiere": matiere,
                "total_lecons": total_mat,
                "done": done_mat,
                "pct": round(done_mat / total_mat * 100),
                "score_moyen": round(score_mat, 1),
            })

    # --- Streak (consecutive days with activity) ---
    today = date.today()
    activite_dates = set(
        UserProgression.objects.filter(user=user)
        .values_list("derniere_activite__date", flat=True)
    )
    # Also include connexion dates
    connexion_dates = set(
        user.connexions.values_list("timestamp__date", flat=True)
    )
    all_dates = activite_dates | connexion_dates
    streak = 0
    d = today
    while d in all_dates:
        streak += 1
        d -= timedelta(days=1)

    # --- Score trend (last 30 days) ---
    depuis = today - timedelta(days=29)
    quiz_recents = (
        resultats_quiz.filter(derniere_tentative__date__gte=depuis)
        .annotate(jour=TruncDate("derniere_tentative"))
        .values("jour")
        .annotate(avg_score=Avg("score"))
        .order_by("jour")
    )
    scores_par_jour = {row["jour"]: round(row["avg_score"], 1) for row in quiz_recents}
    labels_scores = []
    data_scores = []
    for i in range(30):
        d = depuis + timedelta(days=i)
        labels_scores.append(d.strftime("%d/%m"))
        data_scores.append(scores_par_jour.get(d, None))

    # Fill None values with the last known score for a smoother chart
    last_val = None
    data_scores_filled = []
    for v in data_scores:
        if v is not None:
            last_val = v
        data_scores_filled.append(last_val)

    # --- Spaced repetition stats ---
    nb_revisions_dues = UserQuestionHistorique.objects.filter(
        user=user, prochaine_revision__lte=today
    ).count()

    # --- Weak areas (chapters with lowest quiz scores) ---
    from django.db.models import Count as DbCount
    chapitres_faibles = (
        UserQuizResultat.objects.filter(user=user)
        .values("quiz__lecon__chapitre__id", "quiz__lecon__chapitre__titre", "quiz__lecon__chapitre__matiere__nom")
        .annotate(avg_score=Avg("score"), nb_quiz=DbCount("id"))
        .filter(avg_score__lt=70)
        .order_by("avg_score")[:5]
    )

    context = {
        "total_lecons": total_lecons,
        "lecons_terminees": lecons_terminees,
        "chapitres_debloques": chapitres_debloques,
        "quiz_passes": quiz_passes,
        "score_moyen": round(score_moyen, 1),
        "progression_globale": round(progression_globale, 1),
        "activite_recente": activite_recente,
        "matieres_stats": matieres_stats,
        "streak": streak,
        "nb_revisions_dues": nb_revisions_dues,
        "chapitres_faibles": list(chapitres_faibles),
        "labels_scores_json": json.dumps(labels_scores),
        "data_scores_json": json.dumps(data_scores_filled),
    }
    return render(request, "dashboard/eleve.html", context)


def _dashboard_admin(request):
    from progress.models import UserProgression, UserQuizResultat, StatutLeconChoices
    from courses.models import Lecon, Chapitre

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
    # Dernière connexion par élève (batch, sans N+1)
    from users.models import ConnexionLog
    from django.db.models import Max as DbMax
    last_connexion_by_user = dict(
        ConnexionLog.objects.filter(user__in=eleves)
        .values("user_id")
        .annotate(derniere=DbMax("timestamp"))
        .values_list("user_id", "derniere")
    )

    for eleve in eleves:
        total = total_by_niveau.get(eleve.niveau, 0)
        done = done_by_user.get(eleve.pk, 0)
        eleve.progression_pct = int(done / total * 100) if total > 0 else 0
        eleve.derniere_connexion = eleve.last_login or last_connexion_by_user.get(eleve.pk)

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


@login_required
def admin_eleve_detail(request, user_id):
    if not request.user.is_admin:
        return redirect("tableau_de_bord")

    eleve = get_object_or_404(CustomUser, id=user_id, role="eleve")

    from progress.models import UserProgression, UserQuizResultat, ChapitreDebloque, StatutLeconChoices
    from courses.models import Lecon, Chapitre, Matiere
    from django.db.models import Count as DbCount, Avg
    import json
    from datetime import date, timedelta

    # --- Progression globale ---
    total_lecons = Lecon.objects.filter(chapitre__niveau=eleve.niveau).count()
    lecons_terminees_qs = UserProgression.objects.filter(
        user=eleve, statut=StatutLeconChoices.TERMINE
    )
    nb_terminees = lecons_terminees_qs.count()
    progression_globale = round(nb_terminees / total_lecons * 100, 1) if total_lecons > 0 else 0.0

    resultats_quiz = UserQuizResultat.objects.filter(user=eleve)
    nb_quiz_passes = resultats_quiz.filter(passe=True).count()
    score_moyen = resultats_quiz.aggregate(avg=Avg("score"))["avg"] or 0.0

    # --- Chapitres du niveau avec statut de déblocage ---
    chapitres = Chapitre.objects.filter(niveau=eleve.niveau).select_related("matiere").order_by("matiere", "ordre")
    debloques_ids = set(
        ChapitreDebloque.objects.filter(user=eleve).values_list("chapitre_id", flat=True)
    )
    lecons_par_chapitre = {
        row["chapitre_id"]: row["c"]
        for row in Lecon.objects.filter(chapitre__niveau=eleve.niveau)
        .values("chapitre_id")
        .annotate(c=DbCount("id"))
    }
    terminees_par_chapitre = {
        row["lecon__chapitre_id"]: row["c"]
        for row in lecons_terminees_qs.select_related("lecon")
        .values("lecon__chapitre_id")
        .annotate(c=DbCount("id"))
    }
    chapitres_data = []
    for ch in chapitres:
        total_ch = lecons_par_chapitre.get(ch.id, 0)
        done_ch = terminees_par_chapitre.get(ch.id, 0)
        chapitres_data.append({
            "chapitre": ch,
            "debloque": ch.id in debloques_ids,
            "total_lecons": total_ch,
            "lecons_terminees": done_ch,
            "progression_pct": round(done_ch / total_ch * 100) if total_ch > 0 else 0,
        })

    # --- Fréquence de connexions : 30 derniers jours ---
    today = date.today()
    depuis = today - timedelta(days=29)
    connexions_qs = eleve.connexions.filter(timestamp__date__gte=depuis)
    connexions_par_jour = {
        row["jour"]: row["c"]
        for row in connexions_qs.annotate(jour=TruncDate("timestamp"))
        .values("jour")
        .annotate(c=DbCount("id"))
    }
    labels_connexions = []
    data_connexions = []
    for i in range(30):
        d = depuis + timedelta(days=i)
        labels_connexions.append(d.strftime("%d/%m"))
        data_connexions.append(connexions_par_jour.get(d, 0))

    nb_connexions_total = eleve.connexions.count()
    derniere_connexion = eleve.connexions.first()

    # --- Courbe de progression : leçons terminées cumulées sur 30 jours ---
    progressions_recentes = (
        lecons_terminees_qs.filter(termine_le__date__gte=depuis)
        .annotate(jour=TruncDate("termine_le"))
        .values("jour")
        .annotate(c=DbCount("id"))
    )
    prog_par_jour = {row["jour"]: row["c"] for row in progressions_recentes}
    data_progression = []
    cumul = nb_terminees - sum(prog_par_jour.values())  # leçons terminées avant la fenêtre
    for i in range(30):
        d = depuis + timedelta(days=i)
        cumul += prog_par_jour.get(d, 0)
        data_progression.append(cumul)

    context = {
        "eleve": eleve,
        "total_lecons": total_lecons,
        "nb_terminees": nb_terminees,
        "progression_globale": progression_globale,
        "nb_quiz_passes": nb_quiz_passes,
        "score_moyen": round(score_moyen, 1),
        "nb_connexions_total": nb_connexions_total,
        "derniere_connexion": derniere_connexion,
        "chapitres_data": chapitres_data,
        "labels_connexions_json": json.dumps(labels_connexions),
        "data_connexions_json": json.dumps(data_connexions),
        "labels_progression_json": json.dumps(labels_connexions),  # mêmes labels
        "data_progression_json": json.dumps(data_progression),
    }
    return render(request, "dashboard/admin_eleve_detail.html", context)


@login_required
def admin_toggle_chapitre(request, user_id, chapitre_id):
    if not request.user.is_admin:
        return redirect("tableau_de_bord")
    if request.method != "POST":
        return redirect("admin_eleve_detail", user_id=user_id)

    from progress.models import ChapitreDebloque
    from courses.models import Chapitre

    eleve = get_object_or_404(CustomUser, id=user_id, role="eleve")
    chapitre = get_object_or_404(Chapitre, id=chapitre_id)

    obj = ChapitreDebloque.objects.filter(user=eleve, chapitre=chapitre).first()
    if obj:
        obj.delete()
        messages.success(request, f"Chapitre « {chapitre.titre} » verrouillé pour {eleve.nom_complet}.")
    else:
        ChapitreDebloque.objects.create(user=eleve, chapitre=chapitre)
        messages.success(request, f"Chapitre « {chapitre.titre} » débloqué pour {eleve.nom_complet}.")

    return redirect("admin_eleve_detail", user_id=user_id)


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

def _envoyer_email_verification(request, user):
    """Envoie un email de vérification avec un lien signé valable 24h."""
    from django.urls import reverse
    token = signing.dumps(user.pk, salt="email-verification")
    url = request.build_absolute_uri(
        reverse("verifier_email", kwargs={"token": token})
    )
    logger = logging.getLogger(__name__)
    try:
        send_mail(
            subject="ScienceLycée — Confirmez votre adresse email",
            message=f"Bonjour {user.prenom},\n\nCliquez sur ce lien pour activer votre compte :\n{url}\n\nCe lien est valable 24 heures.",
            from_email=None,  # utilise DEFAULT_FROM_EMAIL
            recipient_list=[user.email],
        )
    except Exception as e:
        logger.error("Échec envoi email de vérification pour user pk=%s : %s", user.pk, e)


def inscription_confirmation_view(request):
    """Page affichée après l'inscription, invitant à vérifier l'email."""
    return render(request, "registration/inscription_confirmation.html")


def verifier_email_view(request, token):
    """Active le compte de l'utilisateur via le lien de vérification signé."""
    try:
        user_pk = signing.loads(token, salt="email-verification", max_age=86400)
    except signing.SignatureExpired:
        return render(request, "registration/email_verification_invalid.html",
                      {"raison": "expiré"}, status=400)
    except signing.BadSignature:
        return render(request, "registration/email_verification_invalid.html",
                      {"raison": "invalide"}, status=400)

    user = get_object_or_404(CustomUser, pk=user_pk)
    if not user.is_active:
        user.is_active = True
        user.save(update_fields=["is_active"])
    login(request, user, backend="django.contrib.auth.backends.ModelBackend")
    messages.success(request, "Votre compte a été activé avec succès. Bienvenue !")
    return redirect("tableau_de_bord")


def _debloquer_premiers_chapitres(user):
    from courses.models import Chapitre
    from progress.models import ChapitreDebloque

    premiers = Chapitre.objects.filter(niveau=user.niveau, ordre=1)
    for chap in premiers:
        ChapitreDebloque.objects.get_or_create(user=user, chapitre=chap)


# ---- Admin analytics ----

@login_required
def admin_analytics_view(request):
    """Tableau de bord analytique : taux de réussite, complétion, questions difficiles."""
    if not request.user.is_admin:
        return redirect("tableau_de_bord")

    from progress.models import UserQuestionHistorique, UserProgression, UserChapitreQuizResultat, StatutLeconChoices
    from courses.models import Lecon, Chapitre
    from django.db.models import Avg, Count as DbCount, Sum, FloatField, ExpressionWrapper

    # Taux de réussite par question (depuis Leitner)
    questions_stats = (
        UserQuestionHistorique.objects.values(
            "question__id", "question__texte", "question__quiz__lecon__titre"
        )
        .annotate(
            nb_bonnes=Sum("nb_bonnes"),
            nb_total=Sum("nb_total"),
        )
        .filter(nb_total__gt=0)
    )
    weak_questions = []
    for qs in questions_stats:
        taux = qs["nb_bonnes"] / qs["nb_total"] * 100
        if taux < 40:
            weak_questions.append({
                "question_id": qs["question__id"],
                "texte": qs["question__texte"],
                "lecon": qs["question__quiz__lecon__titre"],
                "taux": round(taux, 1),
                "nb_bonnes": qs["nb_bonnes"],
                "nb_total": qs["nb_total"],
            })
    weak_questions.sort(key=lambda x: x["taux"])

    # Taux de complétion par leçon
    total_eleves = CustomUser.objects.filter(role="eleve", is_active=True).count()
    if total_eleves > 0:
        lecon_completion = {}
        for prog in (
            UserProgression.objects.filter(statut=StatutLeconChoices.TERMINE)
            .values("lecon__id", "lecon__titre", "lecon__chapitre__niveau")
            .annotate(nb=DbCount("user", distinct=True))
        ):
            total_niveau = CustomUser.objects.filter(
                role="eleve", is_active=True, niveau=prog["lecon__chapitre__niveau"]
            ).count()
            pct = round(prog["nb"] / total_niveau * 100, 1) if total_niveau > 0 else 0
            lecon_completion[prog["lecon__id"]] = {
                "titre": prog["lecon__titre"],
                "pct": pct,
                "nb": prog["nb"],
                "total": total_niveau,
            }
    else:
        lecon_completion = {}

    # Taux de passage du quiz de chapitre
    chapitre_pass_rate = {}
    for res in (
        UserChapitreQuizResultat.objects.values("chapitre__id", "chapitre__titre")
        .annotate(nb_total=DbCount("id"), nb_passes=DbCount("id", filter=models.Q(passe=True)))
    ):
        pct = round(res["nb_passes"] / res["nb_total"] * 100, 1) if res["nb_total"] > 0 else 0
        chapitre_pass_rate[res["chapitre__id"]] = {
            "titre": res["chapitre__titre"],
            "pct": pct,
            "nb_passes": res["nb_passes"],
            "nb_total": res["nb_total"],
        }

    return render(request, "dashboard/admin_analytics.html", {
        "weak_questions": weak_questions,
        "lecon_completion": lecon_completion,
        "chapitre_pass_rate": chapitre_pass_rate,
        "total_eleves": total_eleves,
    })


# ---- Rapport de tests local ----

@login_required
def admin_test_report_view(request):
    """Affiche le rapport de tests local (test_report.html) dans une iframe."""
    if not request.user.is_admin:
        return redirect("tableau_de_bord")

    report_path = settings.BASE_DIR / "test_report.html"
    report_exists = report_path.exists()

    passed = failed = error = total = 0
    status = "gray"
    if report_exists:
        from .context_processors import _parse_test_report
        stats = _parse_test_report(report_path)
        if stats:
            passed = stats["passed"]
            failed = stats["failed"]
            error = stats["error"]
            total = stats["total"]
            status = stats["status"]

    return render(request, "dashboard/admin_test_report.html", {
        "report_exists": report_exists,
        "passed": passed,
        "failed": failed,
        "error": error,
        "total": total,
        "status": status,
    })


@login_required
def admin_serve_test_report(request):
    """Sert le contenu brut de test_report.html pour l'iframe."""
    if not request.user.is_admin:
        return redirect("tableau_de_bord")

    report_path = settings.BASE_DIR / "test_report.html"
    if not report_path.exists():
        return HttpResponse("Aucun rapport disponible", status=404)

    return HttpResponse(
        report_path.read_text(encoding="utf-8"),
        content_type="text/html",
    )


