from datetime import datetime, date, timedelta
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from courses.models import Lecon, Chapitre, Question
from .models import (
    UserProgression, UserQuizResultat, UserChapitreQuizResultat,
    ChapitreDebloque, StatutLeconChoices, UserQuestionHistorique,
)


@require_POST
@login_required
def terminer_lecon(request, lecon_pk):
    """Marque une leçon sans quiz comme terminée."""
    user = request.user
    lecon = get_object_or_404(Lecon, pk=lecon_pk)

    if not user.is_admin and lecon.chapitre.niveau != user.niveau:
        return JsonResponse({"erreur": "Accès non autorisé"}, status=403)

    prog, _ = UserProgression.objects.get_or_create(user=user, lecon=lecon)
    if prog.statut != StatutLeconChoices.TERMINE:
        prog.statut = StatutLeconChoices.TERMINE
        prog.termine_le = datetime.utcnow()
        prog.save()
        _verifier_deblocage_chapitre_suivant(user, lecon.chapitre)

    from django.http import HttpResponse
    from django.urls import reverse
    redirect_url = reverse("lecon", kwargs={"lecon_pk": lecon_pk})
    # HTMX: return HX-Redirect header to trigger full page navigation
    if request.headers.get("HX-Request"):
        response = HttpResponse()
        response["HX-Redirect"] = redirect_url
        return response
    return redirect(redirect_url)


@require_POST
@login_required
def soumettre_quiz(request, lecon_pk):
    """Soumission d'un quiz, calcul du score, mise à jour de la progression."""
    user = request.user
    lecon = get_object_or_404(Lecon, pk=lecon_pk)

    if not lecon.has_quiz:
        return redirect("lecon", lecon_pk=lecon_pk)

    if not user.is_admin and lecon.chapitre.niveau != user.niveau:
        return redirect("matieres")

    quiz = lecon.quiz

    # Récupérer les IDs des questions tirées au sort depuis le formulaire
    question_ids_raw = request.POST.get("question_ids", "")
    if question_ids_raw:
        try:
            question_ids = [int(qid) for qid in question_ids_raw.split(",") if qid.strip()]
        except ValueError:
            question_ids = []
        questions = list(quiz.questions.filter(id__in=question_ids))
    else:
        questions = list(quiz.questions.order_by("ordre"))

    total_points = sum(q.points for q in questions)

    points_obtenus = 0
    reponses_soumises = {}
    corrections = []

    for question in questions:
        cle = f"question_{question.id}"
        reponse = request.POST.get(cle, "").strip()
        reponses_soumises[str(question.id)] = reponse

        correct = reponse.lower() == str(question.reponse_correcte).strip().lower()
        if not correct and question.type == "texte_libre":
            correct = _comparer_texte_libre(reponse, question)
        if correct:
            points_obtenus += question.points

        # Libellés lisibles pour l'affichage dans les corrections
        if question.type == "qcm" and question.options:
            try:
                reponse_donnee_texte = question.options[int(reponse)] if reponse.isdigit() else reponse
            except (IndexError, ValueError):
                reponse_donnee_texte = reponse
            try:
                reponse_correcte_texte = question.options[int(question.reponse_correcte)]
            except (IndexError, ValueError):
                reponse_correcte_texte = question.reponse_correcte
        elif question.type == "texte_libre":
            reponse_donnee_texte = reponse if reponse else "—"
            reponse_correcte_texte = question.reponse_correcte
        else:
            reponse_donnee_texte = reponse.capitalize() if reponse else "—"
            reponse_correcte_texte = str(question.reponse_correcte).capitalize()

        corrections.append({
            "question": question,
            "reponse_donnee": reponse,
            "reponse_donnee_texte": reponse_donnee_texte,
            "reponse_correcte_texte": reponse_correcte_texte,
            "correct": correct,
        })

    score = (points_obtenus / total_points * 100) if total_points > 0 else 0.0
    passe = score >= quiz.score_minimum

    # Enregistrer ou mettre à jour le résultat (on garde le meilleur score)
    resultat, created = UserQuizResultat.objects.get_or_create(user=user, quiz=quiz)
    resultat.nb_tentatives += 1
    resultat.reponses = reponses_soumises
    if score > resultat.score:
        resultat.score = score
    if passe:
        resultat.passe = True
    resultat.save()

    # Répétition espacée : enregistrer chaque réponse
    _enregistrer_historique_questions(user, corrections)

    # Marquer la leçon comme "terminée" si quiz passé
    if passe:
        prog, _ = UserProgression.objects.get_or_create(user=user, lecon=lecon)
        if prog.statut != StatutLeconChoices.TERMINE:
            prog.statut = StatutLeconChoices.TERMINE
            prog.termine_le = datetime.utcnow()
            prog.save()
        debloque_suivant = _verifier_deblocage_chapitre_suivant(user, lecon.chapitre)
    else:
        debloque_suivant = False

    nb_bonnes_reponses = sum(1 for c in corrections if c["correct"])
    lecon_suivante = lecon.get_lecon_suivante()

    from django.shortcuts import render
    return render(request, "courses/quiz_resultat.html", {
        "lecon": lecon,
        "chapitre": lecon.chapitre,
        "quiz": quiz,
        "score": round(score, 1),
        "passe": passe,
        "corrections": corrections,
        "resultat": resultat,
        "questions": questions,
        "nb_bonnes_reponses": nb_bonnes_reponses,
        "debloque_suivant": debloque_suivant,
        "lecon_suivante": lecon_suivante,
    })


def _verifier_deblocage_chapitre_suivant(user, chapitre_actuel):
    """Vérifie si le quiz de chapitre est validé (≥ 80%) et débloque le suivant."""
    # Le quiz de chapitre doit être passé avec ≥ 80%
    resultat_chapitre = UserChapitreQuizResultat.objects.filter(
        user=user, chapitre=chapitre_actuel, passe=True
    ).first()
    if not resultat_chapitre:
        return False

    # Débloquer le chapitre suivant
    chapitre_suivant = Chapitre.objects.filter(
        matiere=chapitre_actuel.matiere,
        niveau=chapitre_actuel.niveau,
        ordre=chapitre_actuel.ordre + 1,
    ).first()

    if chapitre_suivant:
        _, created = ChapitreDebloque.objects.get_or_create(user=user, chapitre=chapitre_suivant)
        return created  # True si nouvellement débloqué
    return False


def _comparer_texte_libre(reponse, question):
    """Compare une réponse saisie librement avec la réponse attendue et ses variantes.

    La comparaison est insensible à la casse et ignore les espaces en trop.
    """
    normalized = reponse.strip().lower()
    if normalized == question.reponse_correcte.strip().lower():
        return True
    if question.tolerances:
        for alt in question.tolerances:
            if normalized == str(alt).strip().lower():
                return True
    return False


@require_POST
@login_required
def soumettre_quiz_chapitre(request, chapitre_pk):
    """Soumission du quiz de fin de chapitre, calcul du score, déblocage du suivant."""
    user = request.user
    chapitre = get_object_or_404(Chapitre, pk=chapitre_pk)

    if not user.is_admin and chapitre.niveau != user.niveau:
        return redirect("matieres")

    # Récupérer les IDs des questions tirées au sort
    question_ids_raw = request.POST.get("question_ids", "")
    if question_ids_raw:
        try:
            question_ids = [int(qid) for qid in question_ids_raw.split(",") if qid.strip()]
        except ValueError:
            question_ids = []
        questions = list(Question.objects.filter(id__in=question_ids).select_related("quiz"))
    else:
        return redirect("quiz_chapitre", chapitre_pk=chapitre_pk)

    total_points = sum(q.points for q in questions)
    points_obtenus = 0
    reponses_soumises = {}
    corrections = []

    for question in questions:
        cle = f"question_{question.id}"
        reponse = request.POST.get(cle, "").strip()
        reponses_soumises[str(question.id)] = reponse

        correct = reponse.lower() == str(question.reponse_correcte).strip().lower()
        if not correct and question.type == "texte_libre":
            correct = _comparer_texte_libre(reponse, question)
        if correct:
            points_obtenus += question.points

        if question.type == "qcm" and question.options:
            try:
                reponse_donnee_texte = question.options[int(reponse)] if reponse.isdigit() else reponse
            except (IndexError, ValueError):
                reponse_donnee_texte = reponse
            try:
                reponse_correcte_texte = question.options[int(question.reponse_correcte)]
            except (IndexError, ValueError):
                reponse_correcte_texte = question.reponse_correcte
        elif question.type == "texte_libre":
            reponse_donnee_texte = reponse if reponse else "—"
            reponse_correcte_texte = question.reponse_correcte
        else:
            reponse_donnee_texte = reponse.capitalize() if reponse else "—"
            reponse_correcte_texte = str(question.reponse_correcte).capitalize()

        corrections.append({
            "question": question,
            "reponse_donnee": reponse,
            "reponse_donnee_texte": reponse_donnee_texte,
            "reponse_correcte_texte": reponse_correcte_texte,
            "correct": correct,
        })

    score = (points_obtenus / total_points * 100) if total_points > 0 else 0.0
    score_minimum = 80.0
    passe = score >= score_minimum

    # Enregistrer ou mettre à jour le résultat (on garde le meilleur score)
    resultat, _ = UserChapitreQuizResultat.objects.get_or_create(user=user, chapitre=chapitre)
    resultat.nb_tentatives += 1
    resultat.reponses = reponses_soumises
    if score > resultat.score:
        resultat.score = score
    if passe:
        resultat.passe = True
    resultat.save()

    # Répétition espacée : enregistrer chaque réponse
    _enregistrer_historique_questions(user, corrections)

    # Débloquer le chapitre suivant si validé
    debloque_suivant = False
    if passe:
        debloque_suivant = _verifier_deblocage_chapitre_suivant(user, chapitre)

    nb_bonnes_reponses = sum(1 for c in corrections if c["correct"])

    from django.shortcuts import render
    return render(request, "courses/quiz_chapitre_resultat.html", {
        "chapitre": chapitre,
        "score": round(score, 1),
        "score_minimum": score_minimum,
        "passe": passe,
        "corrections": corrections,
        "resultat": resultat,
        "questions": questions,
        "nb_bonnes_reponses": nb_bonnes_reponses,
        "debloque_suivant": debloque_suivant,
    })


def _enregistrer_historique_questions(user, corrections):
    """Met à jour le suivi Leitner pour chaque question répondue."""
    from .models import LEITNER_INTERVALLES

    for c in corrections:
        question = c["question"]
        hist, created = UserQuestionHistorique.objects.get_or_create(
            user=user,
            question=question,
            defaults={"prochaine_revision": date.today() + timedelta(days=1)},
        )
        hist.enregistrer_reponse(c["correct"])
