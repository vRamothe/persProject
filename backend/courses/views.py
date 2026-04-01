import logging
import random
import re

from django.contrib.auth.decorators import login_required
from django.utils.html import escape
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .models import Matiere, Chapitre, Lecon, Question
from collections import defaultdict
from .utils.latex_parser import render_markdown_to_html, proteger_latex as _proteger_latex, restaurer_latex as _restaurer_latex
from .utils.truncate import tronquer_contenu_markdown

logger = logging.getLogger(__name__)


def _selectionner_questions_chapitre(chapitre, nb_total=10):
    """Sélectionne questions avec mix équilibré facile/moyen/difficile."""
    toutes = list(
        Question.objects.filter(quiz__lecon__chapitre=chapitre).select_related("quiz")
    )
    if not toutes:
        return []

    par_difficulte = defaultdict(list)
    for q in toutes:
        par_difficulte[q.difficulte].append(q)

    quotas = {"facile": 4, "moyen": 4, "difficile": 2}
    selection = []
    for diff, quota in quotas.items():
        pool = par_difficulte[diff][:]
        random.shuffle(pool)
        selection.extend(pool[:quota])

    if len(selection) < nb_total:
        already = {q.id for q in selection}
        reste = [q for q in toutes if q.id not in already]
        random.shuffle(reste)
        selection.extend(reste[:nb_total - len(selection)])

    random.shuffle(selection)
    return selection[:nb_total]


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


def _generer_video_html(lecon, youtube_id):
    """Génère le code HTML pour l'intégration de la vidéo (YouTube ou fichier local)."""
    if youtube_id:
        return (
            '<div class="my-6">'
            '<div class="relative w-full rounded-xl overflow-hidden shadow-sm" style="padding-bottom:56.25%">'
            f'<iframe class="absolute inset-0 w-full h-full" src="https://www.youtube.com/embed/{youtube_id}?rel=0" '
            f'title="{escape(lecon.titre)}" frameborder="0" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
            '</div></div>'
        )
    elif lecon.video_fichier:
        return (
            '<div class="my-6">'
            '<video class="w-full rounded-xl shadow-sm" controls preload="metadata">'
            f'<source src="{lecon.video_fichier.url}" type="video/mp4">'
            'Votre navigateur ne prend pas en charge la lecture vidéo.'
            '</video></div>'
        )
    return ""


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

    def _build_chapitres_data(chapitres_qs):
        chapitres_data = []
        for chap in chapitres_qs.order_by("ordre"):
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
        return chapitres_data

    is_admin_browse = user.is_admin and not preview_niveau
    niveaux_labels = {"seconde": "Seconde", "premiere": "Première", "terminale": "Terminale"}

    matieres_data = []
    for matiere in matieres:
        if is_admin_browse:
            niveaux_data = []
            for niv_val, niv_label in niveaux_labels.items():
                chapitres_qs = matiere.chapitres.filter(niveau=niv_val)
                if chapitres_qs.exists():
                    niveaux_data.append({
                        "niveau_val": niv_val,
                        "niveau_label": niv_label,
                        "chapitres": _build_chapitres_data(chapitres_qs),
                    })
            matieres_data.append({
                "matiere": matiere,
                "niveaux": niveaux_data,
            })
        else:
            niveau_filtre = preview_niveau or user.niveau
            chapitres = matiere.chapitres.filter(niveau=niveau_filtre)
            matieres_data.append({
                "matiere": matiere,
                "chapitres": _build_chapitres_data(chapitres),
            })

    return render(request, "courses/matieres.html", {
        "matieres_data": matieres_data,
        "is_admin_browse": is_admin_browse,
    })


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

    from progress.models import ChapitreDebloque, UserProgression, StatutLeconChoices, UserNote

    # Vérifier que le chapitre est débloqué
    if not user.is_admin:
        if not ChapitreDebloque.objects.filter(user=user, chapitre=chapitre).exists():
            return redirect("matieres")

    # Vérifier l'accès premium côté serveur
    if not lecon.gratuit and not user.is_admin:
        from users.views import _user_has_active_subscription
        if not _user_has_active_subscription(user):
            return redirect("lecon_publique", matiere_slug=chapitre.matiere.slug, niveau=chapitre.niveau, chapitre_slug=chapitre.slug, lecon_slug=lecon.slug)

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

    # Rendu Markdown → HTML (le LaTeX est restauré pour le rendu client via MathJax/KaTeX)
    contenu_html = render_markdown_to_html(lecon.contenu, latex_to_svg=False)

    # Vidéo — construire le HTML d'embed
    youtube_id = _extraire_youtube_id(lecon.video_youtube_url)
    video_html = _generer_video_html(lecon, youtube_id)

    # Remplacer le marqueur [video] dans le contenu s'il existe
    video_placeholder = "<p>[video]</p>"
    video_in_content = video_placeholder in contenu_html
    if video_in_content and video_html:
        contenu_html = contenu_html.replace(video_placeholder, video_html, 1)
    elif video_in_content:
        # Marqueur présent mais pas de vidéo configurée — retirer le placeholder
        contenu_html = contenu_html.replace(video_placeholder, "", 1)

    # Note personnelle de l'élève pour cette leçon
    note = UserNote.objects.filter(user=user, lecon=lecon).first()

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
        "note": note,
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

    # Vérifier l'accès premium côté serveur
    if not lecon.gratuit and not user.is_admin:
        from users.views import _user_has_active_subscription
        if not _user_has_active_subscription(user):
            return redirect("lecon_publique", matiere_slug=chapitre.matiere.slug, niveau=chapitre.niveau, chapitre_slug=chapitre.slug, lecon_slug=lecon.slug)

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

    # Rassembler les questions avec tirage équilibré facile/moyen/difficile
    questions = _selectionner_questions_chapitre(chapitre, nb_total=10)

    if not questions:
        return redirect("chapitre", chapitre_pk=chapitre_pk)

    question_ids = ",".join(str(q.id) for q in questions)

    resultat_existant = UserChapitreQuizResultat.objects.filter(user=user, chapitre=chapitre).first()

    context = {
        "chapitre": chapitre,
        "questions": questions,
        "question_ids": question_ids,
        "nb_total_questions": Question.objects.filter(quiz__lecon__chapitre=chapitre).count(),
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
    from django.http import HttpResponse
    from progress.models import UserQuestionHistorique
    from progress.views import _check_quiz_rate_limit, _evaluer_reponses

    if request.method != "POST":
        return redirect("revisions")

    user = request.user

    if _check_quiz_rate_limit(user.id):
        return HttpResponse("Trop de soumissions. Veuillez patienter une minute.", status=429)

    question_ids_raw = request.POST.get("question_ids", "")
    if not question_ids_raw:
        return redirect("revisions")

    try:
        question_ids = [int(qid) for qid in question_ids_raw.split(",") if qid.strip()]
    except ValueError:
        return redirect("revisions")

    # Vérification de sécurité (IDOR) : s'assurer que les questions correspondent au niveau de l'utilisateur
    if user.is_admin:
        questions = list(Question.objects.filter(id__in=question_ids).select_related("quiz__lecon__chapitre__matiere"))
    else:
        questions = list(Question.objects.filter(id__in=question_ids, quiz__lecon__chapitre__niveau=user.niveau).select_related("quiz__lecon__chapitre__matiere"))

    corrections, _, _ = _evaluer_reponses(questions, request.POST)

    # Mettre à jour le Leitner pour chaque question
    for c in corrections:
        hist, _ = UserQuestionHistorique.objects.get_or_create(
            user=user,
            question=c["question"],
            defaults={"prochaine_revision": date.today()},
        )
        hist.enregistrer_reponse(c["correct"])

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
    """Affichage public d'une leçon (gratuite ou premium avec blur)."""
    matiere = get_object_or_404(Matiere, slug=matiere_slug)
    chapitre = get_object_or_404(
        Chapitre, matiere=matiere, niveau=niveau, slug=chapitre_slug
    )
    lecon = get_object_or_404(
        Lecon.objects.select_related("chapitre__matiere"),
        chapitre=chapitre, slug=lecon_slug,
    )

    est_premium = not lecon.gratuit
    from users.views import _user_has_active_subscription
    user_a_acces = (
        request.user.is_authenticated and (
            request.user.is_admin or
            _user_has_active_subscription(request.user)
        )
    )

    # Admin with full access → redirect to internal view
    if request.user.is_authenticated and request.user.is_admin:
        return redirect("lecon", lecon_pk=lecon.pk)

    if est_premium and not user_a_acces:
        contenu_md, a_ete_tronque = tronquer_contenu_markdown(lecon.contenu, max_mots=2000)
    else:
        contenu_md = lecon.contenu
        a_ete_tronque = False

    contenu_html = render_markdown_to_html(contenu_md, latex_to_svg=False)

    youtube_id = _extraire_youtube_id(lecon.video_youtube_url)
    video_html = _generer_video_html(lecon, youtube_id)

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

    est_floute = est_premium and not user_a_acces

    return render(request, "courses/lecon_publique.html", {
        "lecon": lecon,
        "chapitre": chapitre,
        "matiere": matiere,
        "contenu_html": contenu_html,
        "youtube_id": youtube_id,
        "video_in_content": video_in_content,
        "meta_description": meta_description,
        "est_premium": est_premium,
        "est_floute": est_floute,
        "a_ete_tronque": a_ete_tronque,
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


@login_required
def recherche_view(request):
    """Recherche plein-texte dans les leçons (titre + contenu) — PostgreSQL SearchVector."""
    from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

    query_str = request.GET.get("q", "").strip()
    results = []

    if len(query_str) >= 2:
        user = request.user
        query = SearchQuery(query_str, config="french")
        vector = SearchVector("titre", weight="A", config="french") + SearchVector("contenu", weight="B", config="french")
        lecons_qs = (
            Lecon.objects.select_related("chapitre__matiere")
            .annotate(rank=SearchRank(vector, query))
            .filter(rank__gt=0)
            .order_by("-rank")
        )
        # Filtrer selon le niveau si l'utilisateur est un élève
        if not user.is_admin:
            lecons_qs = lecons_qs.filter(chapitre__niveau=user.niveau)
        results = lecons_qs[:20]

    return render(request, "courses/recherche.html", {
        "results": results,
        "query": query_str,
    })


@login_required
def lecon_pdf_view(request, lecon_pk):
    """Génère et renvoie la leçon en PDF via WeasyPrint."""
    from weasyprint import HTML
    from django.http import HttpResponse
    from django.template.loader import render_to_string

    lecon = get_object_or_404(Lecon.objects.select_related("chapitre__matiere"), pk=lecon_pk)
    user = request.user

    # Vérification d'accès niveau
    if not user.is_admin and lecon.chapitre.niveau != user.niveau:
        return redirect("matieres")

    # Vérifier l'accès premium côté serveur
    if not lecon.gratuit and not user.is_admin:
        from users.views import _user_has_active_subscription
        if not _user_has_active_subscription(user):
            return redirect("lecon_publique", matiere_slug=lecon.chapitre.matiere.slug, niveau=lecon.chapitre.niveau, chapitre_slug=lecon.chapitre.slug, lecon_slug=lecon.slug)

    # Rendu Markdown → HTML avec compilation LaTeX en SVG pour le PDF
    contenu_html = render_markdown_to_html(lecon.contenu, latex_to_svg=True)
    html_string = render_to_string("courses/lecon_pdf.html", {
        "lecon": lecon,
        "chapitre": lecon.chapitre,
        "contenu_html": contenu_html,
        "request": request,
    })

    pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri("/")).write_pdf()

    response = HttpResponse(pdf_file, content_type="application/pdf")
    safe_titre = lecon.titre.replace(" ", "_")[:50]
    response["Content-Disposition"] = f'attachment; filename="{safe_titre}.pdf"'
    return response
