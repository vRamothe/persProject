import csv
import secrets
import string

from django.core.management.base import BaseCommand

from users.models import CustomUser, NiveauChoices


NIVEAUX_VALIDES = {c.value for c in NiveauChoices}


def _generer_mot_de_passe(longueur=12):
    """Génère un mot de passe aléatoire sécurisé."""
    alphabet = string.ascii_letters + string.digits + "!@#$%&*"
    return "".join(secrets.choice(alphabet) for _ in range(longueur))


class Command(BaseCommand):
    help = "Crée des comptes bêta-testeurs (élèves) avec accès premium gratuit."

    def add_arguments(self, parser):
        parser.add_argument(
            "entries",
            nargs="*",
            help="Liste email:niveau (ex: alice@example.com:seconde bob@example.com:terminale)",
        )
        parser.add_argument(
            "--csv",
            dest="csv_file",
            help="Chemin vers un fichier CSV avec colonnes email,niveau",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Affiche ce qui serait fait sans rien créer",
        )
        parser.add_argument(
            "--no-email",
            action="store_true",
            help="Ne pas envoyer d'email de bienvenue (affiche les mots de passe dans stdout)",
        )

    def handle(self, *args, **options):
        entries = self._collecter_entrees(options)
        if not entries:
            self.stderr.write(self.style.ERROR("Aucune entrée fournie. Utilise email:niveau ou --csv."))
            return

        dry_run = options["dry_run"]
        if dry_run:
            self.stdout.write(self.style.WARNING("=== MODE DRY-RUN — aucune modification ===\n"))

        comptes_crees = []
        comptes_existants = []

        for email, niveau in entries:
            email = email.strip().lower()
            niveau = niveau.strip().lower()

            if niveau not in NIVEAUX_VALIDES:
                self.stderr.write(self.style.ERROR(
                    f"  ✗ Niveau invalide « {niveau} » pour {email}. "
                    f"Valeurs acceptées : {', '.join(sorted(NIVEAUX_VALIDES))}"
                ))
                continue

            existant = CustomUser.objects.filter(email=email).first()
            if existant:
                if not dry_run:
                    if not existant.is_beta:
                        existant.is_beta = True
                        existant.save(update_fields=["is_beta"])
                comptes_existants.append(email)
                self.stdout.write(f"  ◆ Déjà existant : {email} → is_beta=True")
                continue

            mot_de_passe = _generer_mot_de_passe()

            if not dry_run:
                user = CustomUser.objects.create_user(
                    email=email,
                    password=mot_de_passe,
                    prenom="Bêta",
                    nom="Testeur",
                    role="eleve",
                    niveau=niveau,
                    is_beta=True,
                )
                user.is_active = True
                user.save(update_fields=["is_active"])

                # Débloquer les premiers chapitres
                from users.views import _debloquer_premiers_chapitres
                _debloquer_premiers_chapitres(user)

            comptes_crees.append((email, niveau, mot_de_passe))
            self.stdout.write(self.style.SUCCESS(
                f"  ✔ Créé : {email} | niveau={niveau} | mdp={mot_de_passe}"
            ))

        # Résumé
        self.stdout.write("")
        self.stdout.write("=" * 50)
        self.stdout.write(f"Comptes créés : {len(comptes_crees)}")
        self.stdout.write(f"Comptes existants mis à jour : {len(comptes_existants)}")
        if dry_run:
            self.stdout.write(self.style.WARNING("(dry-run — rien n'a été modifié)"))
        self.stdout.write("=" * 50)

    def _collecter_entrees(self, options):
        """Collecte les paires (email, niveau) depuis les arguments ou le CSV."""
        entries = []

        # Depuis les arguments positionnels
        for entry in options.get("entries", []):
            if ":" not in entry:
                self.stderr.write(self.style.ERROR(
                    f"  ✗ Format invalide : « {entry} ». Attendu : email:niveau"
                ))
                continue
            email, niveau = entry.split(":", 1)
            entries.append((email, niveau))

        # Depuis le fichier CSV
        csv_path = options.get("csv_file")
        if csv_path:
            try:
                with open(csv_path, newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        email = row.get("email", "").strip()
                        niveau = row.get("niveau", "").strip()
                        if email and niveau:
                            entries.append((email, niveau))
                        else:
                            self.stderr.write(self.style.WARNING(
                                f"  ⚠ Ligne CSV ignorée (champ manquant) : {row}"
                            ))
            except FileNotFoundError:
                self.stderr.write(self.style.ERROR(f"Fichier CSV introuvable : {csv_path}"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Erreur lecture CSV : {e}"))

        return entries
