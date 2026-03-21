"""
Commande Django : pad_quiz_questions
Supprime les questions texte_libre puis complète chaque quiz à 20 QCM
en exploitant le contenu Markdown des leçons.
"""

import hashlib
import random
import re

from django.core.management.base import BaseCommand
from django.db.models import Max


TARGET_PAR_QUIZ = 20

# --------------------------------------------------------------------- #
# Distracteurs génériques par matière                                    #
# --------------------------------------------------------------------- #
_DISTRACTEURS = {
    "physique": [
        "La force gravitationnelle",
        "Le champ magnétique",
        "L'énergie cinétique",
        "La puissance électrique",
        "Le vecteur accélération",
        "La longueur d'onde",
        "La conservation de l'énergie",
        "Le principe d'inertie",
        "La résistance électrique",
        "La fréquence du signal",
        "La vitesse de la lumière",
        "Le travail d'une force",
    ],
    "chimie": [
        "Le numéro atomique",
        "La liaison covalente",
        "L'électronégativité",
        "Le pH de la solution",
        "La concentration molaire",
        "Le tableau d'avancement",
        "Le spectre d'absorption",
        "La réaction d'oxydoréduction",
        "L'équation de dissolution",
        "La masse molaire",
        "Le nombre d'Avogadro",
        "La polarité de la molécule",
    ],
    "mathematiques": [
        "La dérivée de la fonction",
        "La limite en l'infini",
        "La primitive de f",
        "La convergence de la suite",
        "L'intégrale de la fonction",
        "Le coefficient directeur",
        "La matrice de transition",
        "La probabilité conditionnelle",
        "Le théorème de Pythagore",
        "La formule de récurrence",
        "Le domaine de définition",
        "L'intervalle de confiance",
    ],
}


class Command(BaseCommand):
    help = "Supprime les texte_libre et complète chaque quiz à 20 QCM"

    def handle(self, *args, **options):
        from courses.models import Quiz, Question

        # 1. Supprimer toutes les questions texte_libre
        nb_del, _ = Question.objects.filter(type="texte_libre").delete()
        self.stdout.write(f"Supprimé {nb_del} questions texte_libre")

        # 2. Compléter chaque quiz
        quizzes = Quiz.objects.select_related(
            "lecon", "lecon__chapitre", "lecon__chapitre__matiere"
        ).all()

        total = 0
        for quiz in quizzes:
            existing = quiz.questions.count()
            needed = TARGET_PAR_QUIZ - existing
            if needed <= 0:
                continue

            pool = _build_pool(quiz.lecon)
            matiere = quiz.lecon.chapitre.matiere.nom
            new_qs = _generate(pool, quiz.lecon, matiere, needed)

            mx = quiz.questions.aggregate(m=Max("ordre"))["m"] or 0
            for i, qd in enumerate(new_qs):
                Question.objects.create(quiz=quiz, ordre=mx + 1 + i, **qd)

            total += len(new_qs)
            self.stdout.write(
                f"  {quiz.lecon.titre[:50]:50s}  +{len(new_qs):2d}"
                f"  (→ {existing + len(new_qs)})"
            )

        self.stdout.write(self.style.SUCCESS(f"\nTerminé : {total} QCM créées"))


# ===================================================================== #
# Extraction de connaissances                                            #
# ===================================================================== #

def _clean(text):
    """Nettoie le markdown inline d'un extrait, en préservant les délimiteurs LaTeX."""
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"[#>]", "", text)
    return text.strip(" -:*\n\t")


def _sentence_around(contenu, start, end):
    """Retourne la phrase/ligne contenant la plage [start, end]."""
    s = contenu.rfind("\n", 0, start)
    s = 0 if s == -1 else s + 1
    e = contenu.find("\n", end)
    if e == -1:
        e = len(contenu)
    return contenu[s:e].strip()


def _first_content_line(text):
    """Première ligne non vide / non header / non table-separator."""
    for line in text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("|--") or line == "---":
            continue
        cleaned = _clean(line)
        if len(cleaned) > 10:
            return cleaned[:200]
    return ""


def _build_pool(lecon):
    """Liste de nuggets (type, terme, définition) tirés du contenu."""
    contenu = lecon.contenu or ""
    pool = []

    # Bold terms
    for m in re.finditer(r"\*\*([^*]{3,80})\*\*", contenu):
        term = m.group(1).strip()
        defn = _clean(_sentence_around(contenu, m.start(), m.end()))
        if len(defn) > 15:
            pool.append(("def", term, defn))

    # Section headers
    for m in re.finditer(r"^#{2,4}\s*(.+)$", contenu, re.M):
        header = m.group(1).strip()
        rest = contenu[m.end(): m.end() + 800]
        first = _first_content_line(rest)
        if first:
            pool.append(("sec", header, first))

    # Table rows
    for m in re.finditer(
        r"^\|\s*([^|]{3,60})\s*\|\s*([^|]{3,}?)\s*\|", contenu, re.M
    ):
        prop = m.group(1).strip()
        val = _clean(m.group(2).strip())
        if prop.lower() not in ("---", "propriété", "formule", "propriete", ""):
            pool.append(("tbl", prop, val))

    # Blockquotes
    for m in re.finditer(r"^>\s*(.{20,}?)$", contenu, re.M):
        txt = _clean(m.group(1))
        if txt and len(txt) > 20:
            pool.append(("quote", "", txt[:200]))

    # List items
    for m in re.finditer(r"^[-*]\s+(.{20,})$", contenu, re.M):
        item = _clean(m.group(1))
        if item and len(item) > 20:
            pool.append(("list", "", item[:200]))

    # Deduplicate
    seen = set()
    deduped = []
    for nugget in pool:
        key = (nugget[1] + nugget[2][:30]).lower()
        if key not in seen:
            seen.add(key)
            deduped.append(nugget)

    return deduped


# ===================================================================== #
# Génération de questions                                                #
# ===================================================================== #

def _pick_distractors(correct, candidates, n, rng, matiere):
    """Choisit n distracteurs différents du correct."""
    others = [c[:130] for c in candidates if c[:130] != correct[:130]]
    if len(others) < n:
        fallbacks = _DISTRACTEURS.get(matiere, _DISTRACTEURS["physique"])
        others.extend(fallbacks)
    rng.shuffle(others)
    # Ensure uniqueness
    used = {correct[:130]}
    result = []
    for o in others:
        if o not in used:
            used.add(o)
            result.append(o)
        if len(result) == n:
            break
    # Ultimate fallback
    i = 1
    while len(result) < n:
        filler = f"Aucune des propositions précédentes ({i})"
        if filler not in used:
            result.append(filler)
            used.add(filler)
        i += 1
    return result


def _generic_terms(matiere):
    return list(_DISTRACTEURS.get(matiere, _DISTRACTEURS["physique"]))


def _generate(pool, lecon, matiere, count):
    """Génère `count` QCM à partir du pool de nuggets."""
    rng = random.Random(
        int(hashlib.md5(lecon.titre.encode()).hexdigest()[:8], 16)
    )
    questions = []

    all_defs = [n[2] for n in pool if n[2]]
    defs = [n for n in pool if n[0] == "def" and n[1]]
    secs = [n for n in pool if n[0] == "sec"]
    tbls = [n for n in pool if n[0] == "tbl"]
    facts = [n for n in pool if n[0] in ("list", "quote")]
    all_terms = [n[1] for n in defs]

    # ── Pass 1 : « Qu'est-ce que [term] ? » ────────────────────────── #
    for d in defs:
        if len(questions) >= count:
            break
        _, term, defn = d
        correct = defn[:130]
        distractors = _pick_distractors(correct, all_defs, 3, rng, matiere)
        options = distractors + [correct]
        rng.shuffle(options)
        questions.append({
            "type": "qcm",
            "texte": f"Qu'est-ce que « {term} » ?",
            "options": options,
            "reponse_correcte": str(options.index(correct)),
            "explication": f"{term} : {defn[:200]}",
            "points": 1,
        })

    # ── Pass 2 : « Quel terme désigne … ? » ─────────────────────────── #
    defs_shuffled = list(defs)
    rng.shuffle(defs_shuffled)
    for d in defs_shuffled:
        if len(questions) >= count:
            break
        _, term, defn = d
        other_terms = [t for t in all_terms if t.lower() != term.lower()]
        if len(other_terms) < 3:
            other_terms.extend(_generic_terms(matiere))
        rng.shuffle(other_terms)
        options = other_terms[:3] + [term]
        rng.shuffle(options)
        questions.append({
            "type": "qcm",
            "texte": f"Quel terme désigne : « {defn[:120]} » ?",
            "options": options,
            "reponse_correcte": str(options.index(term)),
            "explication": f"Le terme correct est « {term} ».",
            "points": 1,
        })

    # ── Pass 3 : questions table ─────────────────────────────────────── #
    for t in tbls:
        if len(questions) >= count:
            break
        _, prop, val = t
        correct = val[:130]
        other_vals = [x[2][:130] for x in tbls if x[2] != val]
        if len(other_vals) < 3:
            other_vals.extend(_generic_terms(matiere))
        rng.shuffle(other_vals)
        distractors = []
        used = {correct}
        for o in other_vals:
            if o not in used:
                distractors.append(o)
                used.add(o)
            if len(distractors) == 3:
                break
        while len(distractors) < 3:
            distractors.append(f"Aucune de ces réponses ({len(distractors)})")
        options = distractors + [correct]
        rng.shuffle(options)
        questions.append({
            "type": "qcm",
            "texte": f"Quelle est la valeur ou formule associée à « {prop} » ?",
            "options": options,
            "reponse_correcte": str(options.index(correct)),
            "explication": f"{prop} → {val[:200]}",
            "points": 1,
        })

    # ── Pass 4 : sections ────────────────────────────────────────────── #
    for s in secs:
        if len(questions) >= count:
            break
        _, header, first_line = s
        correct = first_line[:130]
        distractors = _pick_distractors(correct, all_defs, 3, rng, matiere)
        options = distractors + [correct]
        rng.shuffle(options)
        questions.append({
            "type": "qcm",
            "texte": f"Concernant la section « {header} », quelle proposition est correcte ?",
            "options": options,
            "reponse_correcte": str(options.index(correct)),
            "explication": f"Section « {header} » : {first_line[:200]}",
            "points": 1,
        })

    # ── Pass 5 : faits / citations ───────────────────────────────────── #
    for f in facts:
        if len(questions) >= count:
            break
        _, _, text = f
        correct = text[:130]
        distractors = _pick_distractors(correct, all_defs, 3, rng, matiere)
        options = distractors + [correct]
        rng.shuffle(options)
        questions.append({
            "type": "qcm",
            "texte": "Laquelle de ces affirmations est correcte ?",
            "options": options,
            "reponse_correcte": str(options.index(correct)),
            "explication": text[:200],
            "points": 1,
        })

    # ── Pass 6 : variations supplémentaires (contexte + application) ── #
    for d in defs:
        if len(questions) >= count:
            break
        _, term, defn = d
        correct = term
        other_terms = [t for t in all_terms if t.lower() != term.lower()]
        if len(other_terms) < 3:
            other_terms.extend(_generic_terms(matiere))
        rng.shuffle(other_terms)
        distractors = []
        used = {correct}
        for o in other_terms:
            if o not in used:
                distractors.append(o)
                used.add(o)
            if len(distractors) == 3:
                break
        while len(distractors) < 3:
            distractors.append(f"Aucune de ces notions ({len(distractors)})")
        options = distractors + [correct]
        rng.shuffle(options)
        questions.append({
            "type": "qcm",
            "texte": f"Dans cette leçon, quelle notion correspond à : « {defn[:100]} » ?",
            "options": options,
            "reponse_correcte": str(options.index(correct)),
            "explication": f"La notion est « {term} ».",
            "points": 1,
        })

    # ── Fallback : questions génériques sur le sujet ─────────────────── #
    headers = [n[1] for n in secs if n[1]]
    titre = lecon.titre
    chapitre_titre = lecon.chapitre.titre

    fallback_templates = [
        f"Quel est le thème principal de la leçon « {titre} » ?",
        f"Quelle notion est abordée dans le chapitre « {chapitre_titre} » ?",
        f"Parmi ces sujets, lequel fait partie de la leçon « {titre} » ?",
        f"Dans la leçon « {titre} », quel concept est étudié en premier ?",
        f"Quel objectif pédagogique vise la leçon « {titre} » ?",
        f"Quelle compétence est travaillée dans « {titre} » ?",
        f"Comment se nomme le chapitre qui contient la leçon « {titre} » ?",
        f"Quel domaine scientifique est concerné par « {chapitre_titre} » ?",
        f"Parmi ces propositions, laquelle est liée à « {titre} » ?",
        f"Quel pré-requis est utile pour la leçon « {titre} » ?",
        f"Quelle méthode est recommandée pour « {titre} » ?",
        f"Dans « {titre} », quel type de raisonnement est privilégié ?",
        f"Quel résultat important découle de « {titre} » ?",
        f"Quelle propriété fondamentale est rappelée dans « {titre} » ?",
        f"Quel est l'enjeu principal de la leçon « {titre} » ?",
        f"Parmi ces notions, laquelle est centrale dans « {chapitre_titre} » ?",
        f"Quel vocabulaire spécifique est introduit dans « {titre} » ?",
        f"Quelle application concrète est présentée dans « {titre} » ?",
        f"Quel théorème ou loi est utilisé(e) dans « {titre} » ?",
        f"Quel est le lien entre « {titre} » et « {chapitre_titre} » ?",
    ]

    idx = 0
    while len(questions) < count:
        tpl = fallback_templates[idx % len(fallback_templates)]
        idx += 1

        # Build options from available pool or headers
        if headers:
            correct = headers[rng.randint(0, len(headers) - 1)]
        else:
            correct = titre

        fallbacks = _generic_terms(matiere)
        rng.shuffle(fallbacks)
        distractors = []
        used = {correct}
        for fb in fallbacks:
            if fb not in used:
                distractors.append(fb)
                used.add(fb)
            if len(distractors) == 3:
                break
        while len(distractors) < 3:
            distractors.append(f"Hors programme ({len(distractors)})")

        options = distractors + [correct]
        rng.shuffle(options)
        questions.append({
            "type": "qcm",
            "texte": tpl,
            "options": options,
            "reponse_correcte": str(options.index(correct)),
            "explication": f"Cette question porte sur la leçon « {titre} ».",
            "points": 1,
        })

    return questions[:count]
