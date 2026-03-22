"""Commande de gestion : importation de questions depuis un fichier CSV.

Usage:
    python manage.py import_questions <csv_file> [--dry-run]

Format CSV attendu (avec en-têtes) :
    quiz_lecon_slug,chapitre_slug,matiere,niveau,texte,type,options,reponse_correcte,
    tolerances,explication,points,ordre,difficulte

Colonnes obligatoires : quiz_lecon_slug, texte, type, reponse_correcte
"""
import csv
import json
import sys

from django.core.management.base import BaseCommand, CommandError

from courses.models import DifficulteChoices, Lecon, Question, TypeQuestionChoices


class Command(BaseCommand):
    help = "Importe des questions depuis un fichier CSV"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Chemin vers le fichier CSV")
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Valide le fichier sans créer de questions",
        )

    def handle(self, *args, **options):
        csv_path = options["csv_file"]
        dry_run = options["dry_run"]

        nb_crees = 0
        nb_erreurs = 0

        try:
            with open(csv_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
        except FileNotFoundError:
            raise CommandError(f"Fichier introuvable : {csv_path}")
        except Exception as exc:
            raise CommandError(f"Erreur lecture CSV : {exc}")

        if not rows:
            self.stdout.write(self.style.WARNING("Aucune ligne de données. 0 question créée."))
            return

        types_valides = {c[0] for c in TypeQuestionChoices.choices}
        difficultes_valides = {c[0] for c in DifficulteChoices.choices}

        for i, row in enumerate(rows, start=2):  # ligne 2 = première ligne de données
            lecon_slug = (row.get("quiz_lecon_slug") or "").strip()
            texte = (row.get("texte") or "").strip()
            type_q = (row.get("type") or "").strip()
            reponse_correcte = (row.get("reponse_correcte") or "").strip()

            # Validations obligatoires
            if not lecon_slug:
                self.stderr.write(f"Ligne {i}: quiz_lecon_slug manquant — ignorée")
                nb_erreurs += 1
                continue

            if not texte:
                self.stderr.write(f"Ligne {i}: texte manquant — ignorée")
                nb_erreurs += 1
                continue

            if type_q not in types_valides:
                self.stderr.write(
                    f"Ligne {i}: type '{type_q}' invalide (attendu : {', '.join(types_valides)}) — ignorée"
                )
                nb_erreurs += 1
                continue

            if not reponse_correcte:
                self.stderr.write(f"Ligne {i}: reponse_correcte vide — ignorée")
                nb_erreurs += 1
                continue

            # Points
            points_raw = (row.get("points") or "1").strip()
            try:
                points = int(points_raw)
                if points <= 0:
                    raise ValueError
            except ValueError:
                self.stderr.write(f"Ligne {i}: points '{points_raw}' invalide (entier positif requis) — ignorée")
                nb_erreurs += 1
                continue

            # Ordre
            ordre_raw = (row.get("ordre") or "1").strip()
            try:
                ordre = int(ordre_raw)
            except ValueError:
                ordre = 1

            # Difficulté
            difficulte = (row.get("difficulte") or DifficulteChoices.MOYEN).strip()
            if difficulte not in difficultes_valides:
                difficulte = DifficulteChoices.MOYEN

            # Options (JSON)
            options = None
            options_raw = (row.get("options") or "").strip()
            if options_raw:
                try:
                    options = json.loads(options_raw)
                    if not isinstance(options, list):
                        raise ValueError("options doit être un tableau JSON")
                except (json.JSONDecodeError, ValueError) as exc:
                    self.stderr.write(f"Ligne {i}: options JSON invalide ({exc}) — ignorée")
                    nb_erreurs += 1
                    continue

            # Tolérances (JSON)
            tolerances = None
            tolerances_raw = (row.get("tolerances") or "").strip()
            if tolerances_raw:
                try:
                    tolerances = json.loads(tolerances_raw)
                    if not isinstance(tolerances, list):
                        raise ValueError("tolerances doit être un tableau JSON")
                except (json.JSONDecodeError, ValueError) as exc:
                    self.stderr.write(f"Ligne {i}: tolerances JSON invalide ({exc}) — ignorée")
                    nb_erreurs += 1
                    continue

            explication = (row.get("explication") or "").strip()

            # Récupérer la leçon
            try:
                lecon = Lecon.objects.get(slug=lecon_slug)
            except Lecon.DoesNotExist:
                self.stderr.write(f"Ligne {i}: leçon slug='{lecon_slug}' introuvable — ignorée")
                nb_erreurs += 1
                continue

            if not hasattr(lecon, "quiz") or lecon.quiz is None:
                # Pas de quiz sur cette leçon — on peut l'ignorer ou signaler
                try:
                    _ = lecon.quiz
                except Exception:
                    self.stderr.write(f"Ligne {i}: leçon '{lecon_slug}' n'a pas de quiz — ignorée")
                    nb_erreurs += 1
                    continue

            quiz = lecon.quiz

            if not dry_run:
                Question.objects.create(
                    quiz=quiz,
                    texte=texte,
                    type=type_q,
                    options=options,
                    reponse_correcte=reponse_correcte,
                    tolerances=tolerances,
                    explication=explication,
                    points=points,
                    ordre=ordre,
                    difficulte=difficulte,
                )

            nb_crees += 1

        prefix = "[DRY-RUN] " if dry_run else ""
        self.stdout.write(
            self.style.SUCCESS(
                f"{prefix}{nb_crees} question(s) {'à créer' if dry_run else 'créée(s)'}, "
                f"{nb_erreurs} ignorée(s) sur erreur."
            )
        )
