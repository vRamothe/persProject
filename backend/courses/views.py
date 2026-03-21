import markdown
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .models import Matiere, Chapitre, Lecon


@login_required
def matieres_view(request):
    """Liste toutes les matières avec les chapitres du niveau de l'élève."""
    user = request.user
    matieres = Matiere.objects.prefetch_related("chapitres__lecons").all()

    # Mode prévisualisation : l'admin simule la vue d'un élève d'un niveau donné
    preview_niveau = request.session.get("preview_niveau") if user.is_admin else None

    from progress.models import ChapitreDebloque, UserProgression, StatutLeconChoices

    debloques_ids = set(
        ChapitreDebloque.objects.filter(user=user).values_list("chapitre_id", flat=True)
    )
    progressions_map = {
        p.lecon_id: p.statut
        for p in UserProgression.objects.filter(user=user).only("lecon_id", "statut")
    }

    matieres_data = []
    for matiere in matieres:
        if user.is_admin and not preview_niveau:
            chapitres = matiere.chapitres.all()
        else:
            niveau_filtre = preview_niveau or user.niveau
            chapitres = matiere.chapitres.filter(niveau=niveau_filtre)

        chapitres_data = []
        for chap in chapitres.order_by("ordre"):
            lecons = sorted(chap.lecons.all(), key=lambda lecon: lecon.ordre)
            lecons_data = []
            nb_terminees = 0
            for lecon in lecons:
                statut = progressions_map.get(lecon.id, StatutLeconChoices.NON_COMMENCE)
                if statut == StatutLeconChoices.TERMINE:
                    nb_terminees += 1
                lecons_data.append({
                    "lecon": lecon,
                    "statut": statut,
                })

            chapitres_data.append({
                "chapitre": chap,
                "debloque": chap.id in debloques_ids or user.is_admin,
                "lecons": lecons_data,
                "nb_lecons": len(lecons_data),
                "nb_terminees": nb_terminees,
                "progression_pct": int(nb_terminees / len(lecons_data) * 100) if lecons_data else 0,
            })

        matieres_data.append({
            "matiere": matiere,
            "chapitres": chapitres_data,
        })

    return render(request, "courses/matieres.html", {"matieres_data": matieres_data})


@login_required
def chapitre_view(request, chapitre_pk):
    """Détail d'un chapitre : liste des leçons."""
    user = request.user
    chapitre = get_object_or_404(Chapitre, pk=chapitre_pk)

    # Vérifier l'accès au niveau
    if not user.is_admin and chapitre.niveau != user.niveau:
        return redirect("matieres")

    from progress.models import ChapitreDebloque, UserProgression, StatutLeconChoices

    # Vérifier que le chapitre est débloqué
    if not user.is_admin:
        if not ChapitreDebloque.objects.filter(user=user, chapitre=chapitre).exists():
            return redirect("matieres")

    lecons = chapitre.lecons.order_by("ordre")

    progressions = {
        p.lecon_id: p
        for p in UserProgression.objects.filter(user=user, lecon__in=lecons)
    }

    lecons_data = []
    for lecon in lecons:
        prog = progressions.get(lecon.id)
        lecons_data.append({
            "lecon": lecon,
            "statut": prog.statut if prog else "non_commence",
            "termine": prog.statut == StatutLeconChoices.TERMINE if prog else False,
        })

    nb_lecons = len(lecons_data)
    nb_terminees = sum(1 for ld in lecons_data if ld["statut"] == "termine")
    progression_pct = int(nb_terminees / nb_lecons * 100) if nb_lecons > 0 else 0

    return render(request, "courses/chapitres.html", {
        "chapitre": chapitre,
        "lecons_data": lecons_data,
        "nb_lecons": nb_lecons,
        "nb_terminees": nb_terminees,
        "progression_pct": progression_pct,
    })


@login_required
def lecon_view(request, lecon_pk):
    """Affichage d'une leçon avec son contenu Markdown rendu."""
    user = request.user
    lecon = get_object_or_404(Lecon.objects.select_related("chapitre__matiere"), pk=lecon_pk)
    chapitre = lecon.chapitre

    # Vérifier l'accès au niveau
    if not user.is_admin and chapitre.niveau != user.niveau:
        return redirect("matieres")

    from progress.models import ChapitreDebloque, UserProgression, StatutLeconChoices

    # Vérifier que le chapitre est débloqué
    if not user.is_admin:
        if not ChapitreDebloque.objects.filter(user=user, chapitre=chapitre).exists():
            return redirect("matieres")

    # En mode prévisualisation, ne pas écrire de données de progression
    preview_niveau = request.session.get("preview_niveau") if user.is_admin else None
    if preview_niveau:
        prog = UserProgression.objects.filter(user=user, lecon=lecon).first()
        est_terminee = prog.statut == StatutLeconChoices.TERMINE if prog else False
    else:
        # Marquer comme "en cours" si pas encore commencée
        prog, _ = UserProgression.objects.get_or_create(user=user, lecon=lecon)
        if prog.statut == StatutLeconChoices.NON_COMMENCE:
            prog.statut = StatutLeconChoices.EN_COURS
            prog.save(update_fields=["statut", "derniere_activite"])
        est_terminee = prog.statut == StatutLeconChoices.TERMINE

    # Rendu Markdown → HTML
    md = markdown.Markdown(extensions=["extra", "tables", "toc", "nl2br"])
    contenu_html = md.convert(lecon.contenu)

    context = {
        "lecon": lecon,
        "chapitre": chapitre,
        "contenu_html": contenu_html,
        "progression": prog,
        "lecon_precedente": lecon.get_lecon_precedente(),
        "lecon_suivante": lecon.get_lecon_suivante(),
        "est_terminee": est_terminee,
    }
    return render(request, "courses/lecon.html", context)


@login_required
def quiz_view(request, lecon_pk):
    """Affichage et soumission d'un quiz."""
    user = request.user
    lecon = get_object_or_404(Lecon.objects.select_related("chapitre__matiere"), pk=lecon_pk)
    chapitre = lecon.chapitre

    if not user.is_admin and chapitre.niveau != user.niveau:
        return redirect("matieres")

    from progress.models import ChapitreDebloque, UserQuizResultat

    if not user.is_admin:
        if not ChapitreDebloque.objects.filter(user=user, chapitre=chapitre).exists():
            return redirect("matieres")

    if not lecon.has_quiz:
        return redirect("lecon", lecon_pk=lecon_pk)

    quiz = lecon.quiz
    questions = quiz.questions.order_by("ordre")
    resultat_existant = UserQuizResultat.objects.filter(user=user, quiz=quiz).first()

    context = {
        "lecon": lecon,
        "chapitre": chapitre,
        "quiz": quiz,
        "questions": questions,
        "resultat_existant": resultat_existant,
    }
    return render(request, "courses/quiz.html", context)
