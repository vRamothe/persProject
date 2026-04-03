from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.text import slugify


PLAN_ENRICHISSEMENT_TERMINALE = {
}


SEQUENCES_PAR_CHAPITRE = {
}


class Command(BaseCommand):
    help = "Initialise la base de données avec les matières, chapitres, leçons, quiz et le compte admin."

    def handle(self, *args, **options):
        self._create_admin()
        self._create_content()
        self.stdout.write(self.style.SUCCESS("✅ Données initiales chargées avec succès."))

    # ------------------------------------------------------------------ #
    # Admin                                                                #
    # ------------------------------------------------------------------ #

    def _create_admin(self):
        from users.models import CustomUser
        email = settings.FIRST_ADMIN_EMAIL
        if CustomUser.objects.filter(email=email).exists():
            self.stdout.write(f"  ◆ Admin déjà existant : {email}")
            return
        CustomUser.objects.create_superuser(
            email=email,
            password=settings.FIRST_ADMIN_PASSWORD,
            prenom=settings.FIRST_ADMIN_PRENOM,
            nom=settings.FIRST_ADMIN_NOM,
            is_staff=True,
        )
        self.stdout.write(self.style.SUCCESS(f"  ✔ Admin créé : {email}"))

    # ------------------------------------------------------------------ #
    # Contenu pédagogique                                                 #
    # ------------------------------------------------------------------ #

    def _create_content(self):
        from courses.models import Matiere, MatiereChoices
        from .seed_content import SEED_DATA

        for matiere_nom, matiere_data in SEED_DATA.items():
            matiere, _ = Matiere.objects.get_or_create(
                nom=matiere_nom,
                defaults={"description": matiere_data["description"]},
            )
            self.stdout.write(f"  ◆ Matière : {matiere.get_nom_display()}")

            for niveau, chapitres_list in matiere_data["niveaux"].items():
                for chap_data in chapitres_list:
                    self._create_chapitre(matiere, niveau, chap_data)

            self._create_terminale_enrichment(matiere)

    def _build_enriched_chapitre(self, matiere_nom, ordre, titre, description, mot_cle):
        sequences = SEQUENCES_PAR_CHAPITRE.get(matiere_nom, {}).get(
            titre,
            ["Pré-requis", "Notions clés", "Applications", "Synthèse"],
        )
        liste_sequences = "\n".join([f"{index}. {item}" for index, item in enumerate(sequences, start=1)])
        exercice_corrige = self._build_exercice_corrige(matiere_nom, titre, mot_cle)
        contenu = (
            f"# {titre}\n\n"
            f"## Parcours par séquences\n{liste_sequences}\n\n"
            f"## Objectifs bac\n"
            f"- Maîtriser les notions essentielles de {titre.lower()}.\n"
            f"- Savoir mobiliser ces notions dans un raisonnement rédigé.\n"
            f"- Vérifier systématiquement unités, ordre de grandeur et conclusion.\n\n"
            f"## Exercice type bac (corrigé)\n{exercice_corrige}\n"
        )
        contenu_exercices = (
            f"# Entraînement bac — {titre}\n\n"
            f"## Méthode guidée\n"
            "1. Extraire les données de l'énoncé.\n"
            "2. Choisir la relation ou propriété pertinente.\n"
            "3. Effectuer le calcul de manière rigoureuse.\n"
            "4. Rédiger une conclusion scientifique claire.\n\n"
            f"## Point d'attention\n"
            f"Le chapitre {titre.lower()} est évalué sur la qualité du raisonnement autant que sur le résultat.\n"
        )
        return {
            "ordre": ordre,
            "titre": titre,
            "description": description,
            "score_minimum": 60.0,
            "lecons": [
                {
                    "ordre": 1,
                    "titre": f"Cours structuré — {titre}",
                    "duree": 30,
                    "contenu": contenu,
                    "quiz": {
                        "titre": f"Quiz — {titre}",
                        "score_minimum": 60.0,
                        "questions": [
                            {
                                "ordre": 1,
                                "type": "vrai_faux",
                                "texte": "Cette leçon inclut une méthode d'exercice type bac corrigé.",
                                "options": ["Vrai", "Faux"],
                                "reponse_correcte": "vrai",
                                "explication": "La méthode de résolution guidée est intégrée dans le cours.",
                                "points": 1,
                            },
                        ],
                    },
                },
                {
                    "ordre": 2,
                    "titre": f"Exercices type bac corrigés — {titre}",
                    "duree": 25,
                    "contenu": contenu_exercices,
                    "quiz": {
                        "titre": f"Quiz — Entraînement bac {titre}",
                        "score_minimum": 60.0,
                        "questions": [
                            {
                                "ordre": 1,
                                "type": "qcm",
                                "texte": "Dans une résolution type bac, quelle étape doit toujours apparaître en fin de copie ?",
                                "options": ["Un schéma sans phrase", "Une conclusion argumentée", "Une table de conversion", "Un rappel historique"],
                                "reponse_correcte": "1",
                                "explication": "La conclusion relie calcul et interprétation scientifique.",
                                "points": 1,
                            },

                        ],
                    },
                },
            ],
        }

    def _build_exercice_corrige(self, matiere_nom, titre, mot_cle):
        if matiere_nom == "mathematiques":
            return (
                "On étudie une fonction représentative du chapitre.\n"
                "- Détermination du domaine de définition.\n"
                "- Calcul de la grandeur utile (dérivée, primitive, probabilité, etc.).\n"
                "- Interprétation du résultat avec une phrase de conclusion.\n\n"
                f"Mot-clé attendu dans la conclusion : {mot_cle}."
            )
        if matiere_nom == "physique":
            return (
                "On modélise une situation expérimentale.\n"
                "- Identifier les lois physiques applicables.\n"
                "- Isoler les grandeurs connues et inconnues.\n"
                "- Appliquer une relation dimensionnellement cohérente.\n"
                "- Vérifier la pertinence physique de l'ordre de grandeur.\n\n"
                f"Notion directrice : {mot_cle}."
            )
        return (
            "On réalise une étude chimique complète.\n"
            "- Identifier les espèces en jeu.\n"
            "- Choisir le modèle (réaction, dosage, identification spectrale).\n"
            "- Exploiter les résultats numériques ou spectraux.\n"
            "- Justifier la conclusion au regard du contexte expérimental.\n\n"
            f"Notion directrice : {mot_cle}."
        )



    def _create_terminale_enrichment(self, matiere):
        plan = PLAN_ENRICHISSEMENT_TERMINALE.get(matiere.nom, [])
        for ordre, titre, description, mot_cle in plan:
            chap_data = self._build_enriched_chapitre(matiere.nom, ordre, titre, description, mot_cle)
            self._create_chapitre(matiere, "terminale", chap_data)

    def _create_chapitre(self, matiere, niveau, chap_data):
        from courses.models import Chapitre
        chapitre, created = Chapitre.objects.get_or_create(
            matiere=matiere,
            niveau=niveau,
            ordre=chap_data["ordre"],
            defaults={
                "titre": chap_data["titre"],
                "description": chap_data.get("description", ""),
                "score_minimum_deblocage": chap_data.get("score_minimum", 60.0),
            },
        )
        if not created:
            chapitre.titre = chap_data["titre"]
            chapitre.description = chap_data.get("description", "")
            chapitre.score_minimum_deblocage = chap_data.get("score_minimum", 60.0)
            chapitre.save(update_fields=["titre", "description", "score_minimum_deblocage", "updated_at"])
        if created:
            self.stdout.write(f"    ✔ Ch.{chap_data['ordre']} [{niveau}] {chap_data['titre']}")

        for lecon_data in chap_data.get("lecons", []):
            self._create_lecon(chapitre, lecon_data)

        self._ensure_terminale_enrichissement(chapitre)

    def _ensure_terminale_enrichissement(self, chapitre):
        from courses.models import Lecon, Quiz, Question

        if chapitre.niveau != "terminale":
            return

        # Garantit au moins 2 leçons avec un entraînement type bac corrigé.
        nb_lecons = chapitre.lecons.count()
        if nb_lecons < 2:
            ordre = (chapitre.lecons.order_by("-ordre").first().ordre if nb_lecons else 0) + 1
            lecon, _ = Lecon.objects.update_or_create(
                chapitre=chapitre,
                ordre=ordre,
                defaults={
                    "titre": "Exercices type bac corrigés",
                    "duree_estimee": 25,
                    "contenu": (
                        "# Exercices type bac corrigés\n\n"
                        "## Méthode\n"
                        "1. Identifier les données utiles.\n"
                        "2. Choisir la relation du cours adaptée.\n"
                        "3. Poser un calcul rigoureux avec unités.\n"
                        "4. Vérifier la cohérence du résultat.\n\n"
                        "## Exercice corrigé\n"
                        "Rédige une solution structurée : hypothèses, calculs, conclusion."
                    ),
                },
            )

            quiz, _ = Quiz.objects.update_or_create(
                lecon=lecon,
                defaults={
                    "titre": "Quiz — Exercices type bac",
                    "score_minimum": 60.0,
                },
            )

            Question.objects.update_or_create(
                quiz=quiz,
                ordre=1,
                defaults={
                    "texte": "Dans une résolution type bac, la dernière étape doit être une conclusion rédigée.",
                    "type": "vrai_faux",
                    "options": ["Vrai", "Faux"],
                    "reponse_correcte": "vrai",
                    "explication": f"Pour {chapitre.titre}, une solution bac se termine par une conclusion rédigée et justifiée.",
                    "points": 1,
                },
            )

    def _create_lecon(self, chapitre, lecon_data):
        from courses.models import Lecon, Quiz, Question
        lecon, _ = Lecon.objects.update_or_create(
            chapitre=chapitre,
            ordre=lecon_data["ordre"],
            defaults={
                "titre": lecon_data["titre"],
                "slug": slugify(lecon_data["titre"]),
                "contenu": lecon_data["contenu"],
                "duree_estimee": lecon_data.get("duree", 15),
                "gratuit": lecon_data.get("gratuit", False),
            },
        )

        if lecon_data.get("quiz"):
            qdata = lecon_data["quiz"]
            quiz, _ = Quiz.objects.update_or_create(
                lecon=lecon,
                defaults={
                    "titre": qdata["titre"],
                    "score_minimum": qdata.get("score_minimum", 60.0),
                },
            )
            questions_ordre = []
            for q in qdata.get("questions", []):
                ordre = q["ordre"]
                questions_ordre.append(ordre)
                Question.objects.update_or_create(
                    quiz=quiz,
                    ordre=ordre,
                    defaults={
                        "texte": q["texte"],
                        "type": q.get("type", "qcm"),
                        "options": q.get("options"),
                        "reponse_correcte": str(q["reponse_correcte"]),
                        "tolerances": q.get("tolerances"),
                        "explication": q.get("explication", ""),
                        "points": q.get("points", 1),
                        "difficulte": q.get("difficulte", "moyen"),
                    },
                )
            # Only remove seed-managed questions; leave generated extras untouched
            if questions_ordre:
                max_seed = max(questions_ordre)
                quiz.questions.filter(ordre__lte=max_seed).exclude(ordre__in=questions_ordre).delete()
