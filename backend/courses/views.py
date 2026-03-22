import random
import re

import markdown
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .models import Matiere, Chapitre, Lecon, Question


def _extraire_youtube_id(url):
    """Extrait l'identifiant vidéo d'une URL YouTube."""
    if not url:
        return None
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def _proteger_latex(contenu):
    """Protège les blocs LaTeX ($$...$$ et $...$) du traitement Markdown.

    Remplace chaque bloc par un placeholder unique, renvoie le texte modifié
    et un dictionnaire placeholder → LaTeX original.
    """
    placeholders = {}
    counter = 0

    def _remplacer(match):
        nonlocal counter
        key = f"\x00LATEX{counter}\x00"
        placeholders[key] = match.group(0)
        counter += 1
        return key

    # $$...$$ (display) en premier, puis $...$ (inline)
    contenu = re.sub(r'\$\$.+?\$\$', _remplacer, contenu, flags=re.DOTALL)
    contenu = re.sub(r'\$(?!\$).+?\$', _remplacer, contenu, flags=re.DOTALL)
    return contenu, placeholders


def _restaurer_latex(html, placeholders):
    """Réinsère les blocs LaTeX originaux dans le HTML rendu."""
    for key, latex in placeholders.items():
        html = html.replace(key, latex)
    return html


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

    from progress.models import ChapitreDebloque, UserProgression, UserChapitreQuizResultat, StatutLeconChoices

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

    # Résultat du quiz de chapitre
    chapitre_quiz_resultat = UserChapitreQuizResultat.objects.filter(user=user, chapitre=chapitre).first()
    # Le quiz de chapitre est accessible seulement si toutes les leçons sont terminées
    toutes_lecons_terminees = nb_terminees == nb_lecons and nb_lecons > 0
    # Vérifier qu'il y a des questions disponibles pour le quiz
    nb_questions_chapitre = Question.objects.filter(quiz__lecon__chapitre=chapitre).count()

    return render(request, "courses/chapitres.html", {
        "chapitre": chapitre,
        "lecons_data": lecons_data,
        "nb_lecons": nb_lecons,
        "nb_terminees": nb_terminees,
        "progression_pct": progression_pct,
        "chapitre_quiz_resultat": chapitre_quiz_resultat,
        "toutes_lecons_terminees": toutes_lecons_terminees,
        "nb_questions_chapitre": nb_questions_chapitre,
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

    # Rendu Markdown → HTML (protéger le LaTeX des transformations Markdown)
    contenu_protege, placeholders_latex = _proteger_latex(lecon.contenu)
    md = markdown.Markdown(extensions=["extra", "tables", "toc", "nl2br"])
    contenu_html = md.convert(contenu_protege)
    contenu_html = _restaurer_latex(contenu_html, placeholders_latex)

    # Vidéo — construire le HTML d'embed
    youtube_id = _extraire_youtube_id(lecon.video_youtube_url)
    video_html = ""
    if youtube_id:
        video_html = (
            '<div class="my-6">'
            '<div class="relative w-full rounded-xl overflow-hidden shadow-sm" style="padding-bottom:56.25%">'
            f'<iframe class="absolute inset-0 w-full h-full" src="https://www.youtube.com/embed/{youtube_id}?rel=0" '
            f'title="{lecon.titre}" frameborder="0" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
            '</div></div>'
        )
    elif lecon.video_fichier:
        video_html = (
            '<div class="my-6">'
            '<video class="w-full rounded-xl shadow-sm" controls preload="metadata">'
            f'<source src="{lecon.video_fichier.url}" type="video/mp4">'
            'Votre navigateur ne prend pas en charge la lecture vidéo.'
            '</video></div>'
        )

    # Remplacer le marqueur [video] dans le contenu s'il existe
    video_placeholder = "<p>[video]</p>"
    video_in_content = video_placeholder in contenu_html
    if video_in_content and video_html:
        contenu_html = contenu_html.replace(video_placeholder, video_html, 1)
    elif video_in_content:
        # Marqueur présent mais pas de vidéo configurée — retirer le placeholder
        contenu_html = contenu_html.replace(video_placeholder, "", 1)

    context = {
        "lecon": lecon,
        "chapitre": chapitre,
        "contenu_html": contenu_html,
        "progression": prog,
        "lecon_precedente": lecon.get_lecon_precedente(),
        "lecon_suivante": lecon.get_lecon_suivante(),
        "est_terminee": est_terminee,
        "youtube_id": youtube_id,
        "video_in_content": video_in_content,
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
    toutes_questions = list(quiz.questions.order_by("ordre"))
    resultat_existant = UserQuizResultat.objects.filter(user=user, quiz=quiz).first()

    # Tirage aléatoire de 5 questions parmi les disponibles
    nb_tirage = min(5, len(toutes_questions))
    questions = random.sample(toutes_questions, nb_tirage)
    question_ids = ",".join(str(q.id) for q in questions)

    context = {
        "lecon": lecon,
        "chapitre": chapitre,
        "quiz": quiz,
        "questions": questions,
        "question_ids": question_ids,
        "nb_total_questions": len(toutes_questions),
        "resultat_existant": resultat_existant,
    }
    return render(request, "courses/quiz.html", context)


@login_required
def quiz_chapitre_view(request, chapitre_pk):
    """Quiz de fin de chapitre : 10 questions piochées parmi tous les quiz du chapitre."""
    user = request.user
    chapitre = get_object_or_404(Chapitre.objects.select_related("matiere"), pk=chapitre_pk)

    if not user.is_admin and chapitre.niveau != user.niveau:
        return redirect("matieres")

    from progress.models import ChapitreDebloque, UserChapitreQuizResultat

    if not user.is_admin:
        if not ChapitreDebloque.objects.filter(user=user, chapitre=chapitre).exists():
            return redirect("matieres")

    # Rassembler toutes les questions des quiz de ce chapitre
    toutes_questions = list(
        Question.objects.filter(quiz__lecon__chapitre=chapitre).select_related("quiz")
    )

    if not toutes_questions:
        return redirect("chapitre", chapitre_pk=chapitre_pk)

    nb_tirage = min(10, len(toutes_questions))
    questions = random.sample(toutes_questions, nb_tirage)
    question_ids = ",".join(str(q.id) for q in questions)

    resultat_existant = UserChapitreQuizResultat.objects.filter(user=user, chapitre=chapitre).first()

    context = {
        "chapitre": chapitre,
        "questions": questions,
        "question_ids": question_ids,
        "nb_total_questions": len(toutes_questions),
        "resultat_existant": resultat_existant,
        "score_minimum": 80,
    }
    return render(request, "courses/quiz_chapitre.html", context)


@login_required
def revisions_view(request):
    """Page de révision espacée : affiche les questions dues aujourd'hui."""
    from datetime import date
    from progress.models import UserQuestionHistorique

    user = request.user

    # Questions dues (prochaine_revision <= aujourd'hui), priorité aux boîtes basses
    historiques = (
        UserQuestionHistorique.objects.filter(user=user, prochaine_revision__lte=date.today())
        .select_related("question__quiz__lecon__chapitre__matiere")
        .order_by("boite", "prochaine_revision")
    )

    # Statistiques de révision
    total_historiques = UserQuestionHistorique.objects.filter(user=user).count()
    nb_dues = historiques.count()
    nb_maitrisees = UserQuestionHistorique.objects.filter(user=user, boite__gte=4).count()

    # Pour le mode quiz de révision : tirer jusqu'à 10 questions
    questions_dues = [h.question for h in historiques[:10]]
    question_ids = ",".join(str(q.id) for q in questions_dues)

    # Répartition par boîte pour la vue d'ensemble
    from django.db.models import Count
    repartition_boites = dict(
        UserQuestionHistorique.objects.filter(user=user)
        .values_list("boite")
        .annotate(c=Count("id"))
        .values_list("boite", "c")
    )
    box_colors = {
        1: "bg-red-400", 2: "bg-orange-400", 3: "bg-yellow-400",
        4: "bg-lime-400", 5: "bg-emerald-400",
    }
    box_display = [
        (i, repartition_boites.get(i, 0), box_colors[i])
        for i in range(1, 6)
    ]

    context = {
        "questions": questions_dues,
        "question_ids": question_ids,
        "nb_dues": nb_dues,
        "total_historiques": total_historiques,
        "nb_maitrisees": nb_maitrisees,
        "box_display": box_display,
    }
    return render(request, "courses/revisions.html", context)


@login_required
def soumettre_revisions(request):
    """Soumission du quiz de révision espacée."""
    from datetime import date
    from progress.models import UserQuestionHistorique

    if request.method != "POST":
        return redirect("revisions")

    user = request.user

    question_ids_raw = request.POST.get("question_ids", "")
    if not question_ids_raw:
        return redirect("revisions")

    try:
        question_ids = [int(qid) for qid in question_ids_raw.split(",") if qid.strip()]
    except ValueError:
        return redirect("revisions")

    questions = list(Question.objects.filter(id__in=question_ids).select_related("quiz__lecon__chapitre__matiere"))

    corrections = []
    for question in questions:
        cle = f"question_{question.id}"
        reponse = request.POST.get(cle, "").strip()

        correct = reponse.lower() == str(question.reponse_correcte).strip().lower()
        if not correct and question.type == "texte_libre" and question.tolerances:
            normalized = reponse.strip().lower()
            for alt in question.tolerances:
                if normalized == str(alt).strip().lower():
                    correct = True
                    break

        # Mettre à jour le Leitner
        hist, _ = UserQuestionHistorique.objects.get_or_create(
            user=user,
            question=question,
            defaults={"prochaine_revision": date.today()},
        )
        hist.enregistrer_reponse(correct)

        if question.type == "qcm" and question.options:
            try:
                reponse_donnee_texte = question.options[int(reponse)] if reponse.isdigit() else reponse
            except (IndexError, ValueError):
                reponse_donnee_texte = reponse
            try:
                reponse_correcte_texte = question.options[int(question.reponse_correcte)]
            except (IndexError, ValueError):
                reponse_correcte_texte = question.reponse_correcte
        else:
            reponse_donnee_texte = reponse if reponse else "—"
            reponse_correcte_texte = question.reponse_correcte

        corrections.append({
            "question": question,
            "reponse_donnee": reponse,
            "reponse_donnee_texte": reponse_donnee_texte,
            "reponse_correcte_texte": reponse_correcte_texte,
            "correct": correct,
        })

    nb_bonnes_reponses = sum(1 for c in corrections if c["correct"])
    score = round(nb_bonnes_reponses / len(corrections) * 100, 1) if corrections else 0

    return render(request, "courses/revisions_resultat.html", {
        "corrections": corrections,
        "nb_bonnes_reponses": nb_bonnes_reponses,
        "score": score,
        "total": len(corrections),
    })


# ============================================================
# PUBLIC VIEWS — no @login_required
# ============================================================

def catalogue_matiere_view(request, matiere_slug):
    """Page publique listant les chapitres d'une matière par niveau."""
    matiere = get_object_or_404(Matiere, slug=matiere_slug)
    chapitres = matiere.chapitres.prefetch_related("lecons").order_by("niveau", "ordre")

    from .models import NiveauChoices
    niveaux_data = []
    for niveau_val, niveau_label in NiveauChoices.choices:
        chaps = [c for c in chapitres if c.niveau == niveau_val]
        if not chaps:
            continue
        chapitres_data = []
        for chap in chaps:
            lecons = sorted(chap.lecons.all(), key=lambda l: l.ordre)
            lecons_data = []
            for lecon in lecons:
                lecons_data.append({
                    "lecon": lecon,
                    "gratuit": lecon.gratuit,
                })
            chapitres_data.append({
                "chapitre": chap,
                "lecons": lecons_data,
                "nb_lecons": len(lecons_data),
            })
        niveaux_data.append({
            "niveau_val": niveau_val,
            "niveau_label": niveau_label,
            "chapitres": chapitres_data,
        })

    return render(request, "courses/catalogue.html", {
        "matiere": matiere,
        "niveaux_data": niveaux_data,
    })


def lecon_publique_view(request, matiere_slug, niveau, chapitre_slug, lecon_slug):
    """Affichage public d'une leçon gratuite (sans login)."""
    matiere = get_object_or_404(Matiere, slug=matiere_slug)
    chapitre = get_object_or_404(
        Chapitre, matiere=matiere, niveau=niveau, slug=chapitre_slug
    )
    lecon = get_object_or_404(
        Lecon.objects.select_related("chapitre__matiere"),
        chapitre=chapitre, slug=lecon_slug,
    )

    # Non-free lesson → redirect to login
    if not lecon.gratuit:
        from django.urls import reverse
        from urllib.parse import urlencode
        login_url = reverse("connexion")
        next_url = request.get_full_path()
        return redirect(f"{login_url}?{urlencode({'next': next_url})}")

    # Authenticated user → redirect to the full lesson view with progression
    if request.user.is_authenticated:
        return redirect("lecon", lecon_pk=lecon.pk)

    # Render lesson content (read-only, no progression)
    contenu_protege, placeholders_latex = _proteger_latex(lecon.contenu)
    md = markdown.Markdown(extensions=["extra", "tables", "toc", "nl2br"])
    contenu_html = md.convert(contenu_protege)
    contenu_html = _restaurer_latex(contenu_html, placeholders_latex)

    youtube_id = _extraire_youtube_id(lecon.video_youtube_url)
    video_html = ""
    if youtube_id:
        video_html = (
            '<div class="my-6">'
            '<div class="relative w-full rounded-xl overflow-hidden shadow-sm" style="padding-bottom:56.25%">'
            f'<iframe class="absolute inset-0 w-full h-full" src="https://www.youtube.com/embed/{youtube_id}?rel=0" '
            f'title="{lecon.titre}" frameborder="0" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
            '</div></div>'
        )
    elif lecon.video_fichier:
        video_html = (
            '<div class="my-6">'
            '<video class="w-full rounded-xl shadow-sm" controls preload="metadata">'
            f'<source src="{lecon.video_fichier.url}" type="video/mp4">'
            'Votre navigateur ne prend pas en charge la lecture vidéo.'
            '</video></div>'
        )

    video_placeholder = "<p>[video]</p>"
    video_in_content = video_placeholder in contenu_html
    if video_in_content and video_html:
        contenu_html = contenu_html.replace(video_placeholder, video_html, 1)
    elif video_in_content:
        contenu_html = contenu_html.replace(video_placeholder, "", 1)

    # Strip Markdown for meta description
    import re as _re
    meta_description = _re.sub(r'[#*_\[\]()>`$]', '', lecon.contenu)
    meta_description = ' '.join(meta_description.split())[:160]

    return render(request, "courses/lecon_publique.html", {
        "lecon": lecon,
        "chapitre": chapitre,
        "matiere": matiere,
        "contenu_html": contenu_html,
        "youtube_id": youtube_id,
        "video_in_content": video_in_content,
        "meta_description": meta_description,
    })


def accueil_view(request):
    """Page d'accueil publique affichant toutes les matières et leurs chapitres."""
    from .models import NiveauChoices

    matieres_data = []
    for matiere in Matiere.objects.prefetch_related("chapitres__lecons").all():
        chapitres = matiere.chapitres.order_by("niveau", "ordre")
        niveaux_data = []
        for niveau_val, niveau_label in NiveauChoices.choices:
            chaps = [c for c in chapitres if c.niveau == niveau_val]
            if not chaps:
                continue
            chapitres_data = []
            for chap in chaps:
                lecons = sorted(chap.lecons.all(), key=lambda l: l.ordre)
                lecons_data = [{"lecon": l, "gratuit": l.gratuit} for l in lecons]
                chapitres_data.append({
                    "chapitre": chap,
                    "lecons": lecons_data,
                    "nb_lecons": len(lecons_data),
                })
            niveaux_data.append({
                "niveau_val": niveau_val,
                "niveau_label": niveau_label,
                "chapitres": chapitres_data,
            })
        matieres_data.append({
            "matiere": matiere,
            "niveaux_data": niveaux_data,
        })

    return render(request, "courses/accueil.html", {
        "matieres_data": matieres_data,
    })
