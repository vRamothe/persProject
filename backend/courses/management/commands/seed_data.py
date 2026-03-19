from django.core.management.base import BaseCommand
from django.conf import settings


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
        if created:
            self.stdout.write(f"    ✔ Ch.{chap_data['ordre']} [{niveau}] {chap_data['titre']}")

        for lecon_data in chap_data.get("lecons", []):
            self._create_lecon(chapitre, lecon_data)

    def _create_lecon(self, chapitre, lecon_data):
        from courses.models import Lecon, Quiz, Question
        lecon, created = Lecon.objects.get_or_create(
            chapitre=chapitre,
            ordre=lecon_data["ordre"],
            defaults={
                "titre": lecon_data["titre"],
                "contenu": lecon_data["contenu"],
                "duree_estimee": lecon_data.get("duree", 15),
            },
        )

        if created and lecon_data.get("quiz"):
            qdata = lecon_data["quiz"]
            quiz = Quiz.objects.create(
                lecon=lecon,
                titre=qdata["titre"],
                score_minimum=qdata.get("score_minimum", 60.0),
            )
            for q in qdata.get("questions", []):
                Question.objects.create(
                    quiz=quiz,
                    texte=q["texte"],
                    type=q.get("type", "qcm"),
                    options=q.get("options"),
                    reponse_correcte=str(q["reponse_correcte"]),
                    explication=q.get("explication", ""),
                    points=q.get("points", 1),
                    ordre=q["ordre"],
                )
