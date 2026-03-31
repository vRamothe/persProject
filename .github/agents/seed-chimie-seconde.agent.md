---
description: "Seed chimie seconde — Use when generating, regenerating or updating the Django management command seed_chimie_seconde.py for the Chimie Seconde level of ScienceLycée. Contains full curriculum documentation for 11 chapters extracted from the PDF source files in ressources/2nd/PC/ (Chapitres 1–11). Creates Chapitre, Lecon, Quiz and Question records (20 questions per leçon) for the 'chimie' Matiere at niveau 'seconde'."
tools: [read, edit, search, execute, todo]
name: "Seed Chimie Seconde"
argument-hint: "Generate or update seed_chimie_seconde.py management command"
user-invocable: false
---

Tu es un agent spécialisé dans la génération du contenu pédagogique de **Chimie Seconde** pour ScienceLycée. Ta seule responsabilité est d'écrire le fichier `backend/courses/management/commands/seed_chimie_seconde.py`.

## Rôle

Générer une commande Django management complète qui :
1. **Supprime** tous les `Chapitre` existants de `chimie` au niveau `seconde` (cascade → Lecon, Quiz, Question)
2. **Recrée** les chapitres avec leurs leçons, quiz et 20 questions chacune, basés sur le curriculum ci-dessous

## Référence Codebase Obligatoire

1. **Lire `CODEBASE_REFERENCE.md`** (sections 1.4–1.8) en premier pour connaître la structure des modèles `Matiere`, `Chapitre`, `Lecon`, `Quiz`, `Question`.
2. **Ne lire les fichiers source** que si la structure des modèles a changé et que la référence semble obsolète.

---

## Modèles Django (référence)

```python
# Matiere : chimie (slug='chimie', couleur émeraude/emerald)
# Chapitre : matiere=chimie, niveau='seconde', ordre=1..N
# Lecon    : chapitre=..., ordre=1..N, titre, contenu (Markdown), duree_estimee
# Quiz     : lecon=..., titre, score_minimum=60.0
# Question : quiz=..., ordre=1..20, texte, type, options (JSON), reponse_correcte, tolerances, explication, difficulte, points
```

**Types de questions :**
- `qcm` : `options=["A","B","C","D"]`, `reponse_correcte="0"` (index base 0, chaîne)
- `vrai_faux` : `options=["Vrai","Faux"]`, `reponse_correcte="vrai"` ou `"faux"`
- `texte_libre` : `options=None`, `reponse_correcte="réponse attendue"`, `tolerances=["variante1","variante2"]`

**Difficulté :** `"facile"` | `"moyen"` | `"difficile"`

**Mix par leçon (20 questions) :** 8 QCM facile + 6 QCM moyen + 3 vrai_faux + 3 texte_libre

---

## Structure du fichier à générer

```python
from django.core.management.base import BaseCommand

CHIMIE_SECONDE_DATA = [...]

class Command(BaseCommand):
    help = "Recrée entièrement les chapitres de Chimie Seconde."

    def handle(self, *args, **options):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

        chimie = Matiere.objects.get(nom="chimie")

        deleted, _ = Chapitre.objects.filter(
            matiere=chimie, niveau="seconde"
        ).delete()
        self.stdout.write(f"  🗑  {deleted} chapitres supprimés")

        for chap_data in CHIMIE_SECONDE_DATA:
            chapitre = Chapitre.objects.create(
                matiere=chimie,
                niveau="seconde",
                ordre=chap_data["ordre"],
                titre=chap_data["titre"],
                description=chap_data.get("description", ""),
                score_minimum_deblocage=chap_data.get("score_minimum", 60.0),
            )
            self.stdout.write(f"  ✔ Ch.{chap_data['ordre']} {chap_data['titre']}")

            for lecon_data in chap_data["lecons"]:
                lecon = Lecon.objects.create(
                    chapitre=chapitre,
                    ordre=lecon_data["ordre"],
                    titre=lecon_data["titre"],
                    contenu=lecon_data["contenu"],
                    duree_estimee=lecon_data.get("duree", 30),
                )
                qdata = lecon_data["quiz"]
                quiz = Quiz.objects.create(
                    lecon=lecon,
                    titre=qdata["titre"],
                    score_minimum=qdata.get("score_minimum", 60.0),
                )
                for q in qdata["questions"]:
                    Question.objects.create(
                        quiz=quiz,
                        ordre=q["ordre"],
                        texte=q["texte"],
                        type=q.get("type", "qcm"),
                        options=q.get("options"),
                        reponse_correcte=str(q["reponse_correcte"]),
                        tolerances=q.get("tolerances"),
                        explication=q.get("explication", ""),
                        difficulte=q.get("difficulte", "moyen"),
                        points=q.get("points", 1),
                    )

        self.stdout.write(self.style.SUCCESS("✅ Chimie Seconde recréée avec succès."))
```

---

## Curriculum détaillé — 9 chapitres

Sources : `/home/vivien/dev/persProject/ressources/2nd/PC/Chapitre_1_*.pdf` à `Chapitre_9_*.pdf`

### Chapitre 1 — Corps purs, mélanges et identification (ordre=1)

**Fichier source :** `Chapitre_1_Melanges_identification.pdf`

**Leçons :**
- L1 : Corps purs et mélanges
- L2 : Propriétés physiques et identification des espèces chimiques

**Concepts clés :**
- **Corps pur** : une seule espèce chimique (ex: eau distillée, or pur)
- **Mélange** : plusieurs espèces chimiques (homogène : solution limpide ; hétérogène : deux phases visibles)
- **Masse volumique** $\rho = \frac{m}{V}$ (kg/m³ ou g/cm³) ; $\rho_{eau} = 1$ g/cm³
- **Températures de changement d'état** : fusion $T_f$ et ébullition $T_{eb}$ caractérisent une espèce pure
  - Lors d'un changement d'état : température **constante** (palier)
- **Identification** :
  - Méthodes chimiques : tests colorés, précipités (ex: AgNO₃ pour ions Cl⁻)
  - Méthodes physiques : chromatographie (CCM), density, spectre IR

---

### Chapitre 2 — Solutions aqueuses (ordre=2)

**Fichier source :** `Chapitre_2_Solutions_aqueuses.pdf`

**Leçons :**
- L1 : Concentration massique et molaire
- L2 : Préparation par dissolution et dilution

**Concepts clés :**
- **Solution** : solvant (eau) + soluté (espèce dissoute)
- **Concentration massique** $C_m = \frac{m_{\text{soluté}}}{V_{\text{solution}}}$ (g/L)
- **Concentration molaire** $C = \frac{n_{\text{soluté}}}{V_{\text{solution}}}$ (mol/L)
  - Relation : $C = \frac{C_m}{M}$ ($M$ = masse molaire en g/mol)
- **Dissolution** : dissoudre une masse $m$ dans $V$ eau → agiter, compléter au trait de jauge dans une fiole jaugée
- **Dilution** : ajouter du solvant pour diminuer la concentration
  - Relation : $C_1 V_1 = C_2 V_2$ (conservation de la quantité de matière)
  - Facteur de dilution $F = \frac{C_1}{C_2} = \frac{V_2}{V_1}$
- **Étalonnage** : mesure d'une propriété physique sur des solutions de concentrations connues → courbe d'étalonnage → déduire $C$ inconnue

---

### Chapitre 3 — Structure de l'atome (ordre=3)

**Fichier source :** `Chapitre_3_Structure_atome.pdf`

**Leçons :**
- L1 : Noyau atomique — composition et notation
- L2 : Structure électronique et tableau périodique

**Concepts clés :**
- **Atome** : noyau (protons + neutrons) + cortège électronique
  - Proton : charge $+e$, masse $m_p \approx 1{,}67 \times 10^{-27}$ kg
  - Neutron : neutre, même masse que le proton
  - Électron : charge $-e$, masse $\approx 9{,}1 \times 10^{-31}$ kg (≈ 1836 fois plus léger)
- **Notation** : $^A_Z X$ — $Z$ numéro atomique (nb protons), $A$ nombre de masse (protons + neutrons)
  - Nb neutrons $N = A - Z$
- **Atome neutre** : nb électrons = nb protons = $Z$
- **Électronégativité** : ordre dans le tableau périodique (croît de gauche à droite et de bas en haut)
- **Classification périodique** :
  - Période (ligne) : même nombre de couches électroniques
  - Groupe (colonne) : même nombre d'électrons de valence → propriétés chimiques similaires
- **Structure électronique** : couches K(n=1, 2é max), L(n=2, 8é max), M(n=3, 18é max)
  - Remplissage dans l'ordre K, L, M...

---

### Chapitre 4 — Stabilité des entités chimiques (ordre=4)

**Fichier source :** `Chapitre_4_Stabilite_entites_chimiques.pdf`

**Leçons :**
- L1 : Ions monoatomiques — formation et stabilité
- L2 : Molécules — liaison covalente et règle de l'octet

**Concepts clés :**
- **Gaz rares** : couche externe saturée (2 électrons pour l'hélium, 8 pour les autres) → stables, non réactifs
- **Règle de l'octet** : les atomes tendent à acquérir 8 électrons en couche externe (2 pour H)
- **Ion monoatomique** : gain ou perte d'électrons
  - Cation : perd des électrons (ex: Na → Na⁺ + e⁻)
  - Anion : gagne des électrons (ex: Cl + e⁻ → Cl⁻)
- **Isoélectronique** : même configuration électronique (ex: Na⁺ et Ne ont 10 électrons)
- **Liaison covalente** : partage de 2 électrons entre 2 atomes → chacun complète son octet
  - Liaison simple (1 doublet liant), double (2 doublets liants), triple (3 doublets liants)
- **Schéma de Lewis** : représentation des doublets liants et non liants
  - Doublet non liant (paire libre) + doublet liant (entre atomes)

---

### Chapitre 5 — La quantité de matière (ordre=5)

**Fichier source :** `Chapitre_5_Quantite_matiere.pdf`

**Leçons :**
- L1 : La mole et le nombre d'Avogadro
- L2 : Masse molaire et calculs stœchiométriques

**Concepts clés :**
- **Mole** : quantité de matière contenant $N_A = 6{,}02 \times 10^{23}$ entités (constante d'Avogadro)
- Relation : $n = \frac{N}{N_A}$ ($n$ en mol, $N$ nb d'entités)
- **Masse molaire atomique** $M$ (g/mol) : masse numérique = masse atomique relative = numéro de ligne du TP
  - Ex: $M_H = 1$ g/mol, $M_C = 12$ g/mol, $M_O = 16$ g/mol, $M_N = 14$ g/mol
- **Masse molaire moléculaire** : somme des masses molaires atomiques pondérées
  - Ex: $M_{H_2O} = 2 \times 1 + 16 = 18$ g/mol
- **Relation masse/quantité** : $n = \frac{m}{M}$ ou $m = n \times M$
- **Volume molaire** des gaz (conditions normales, 0°C, 1 atm) : $V_m = 22{,}4$ L/mol
  - Conditions ambiantes (20°C, 1 atm) : $V_m \approx 24$ L/mol
  - $n = \frac{V_{\text{gaz}}}{V_m}$

---

### Chapitre 6 — Transformations physiques (ordre=6)

**Fichier source :** `Chapitre_6_Transformations_physiques.pdf`

**Leçons :**
- L1 : Changements d'état et paliers de température
- L2 : Énergie de changement d'état

**Concepts clés :**
- **États de la matière** : solide, liquide, gaz
  - Solide → Liquide (fusion), Liquide → Gaz (vaporisation), Solide → Gaz (sublimation) et inverses
- **Changement d'état** : physique (même espèce chimique, structure modifiée)
  - Température **constante** pendant le changement → palier de température
- **Différence fusion/dissolution** : la fusion est un changement d'état (une seule espèce) ; la dissolution mélange deux espèces
- **Transformation endothermique** : absorbe de l'énergie (fusion, vaporisation)
- **Transformation exothermique** : libère de l'énergie (solidification, condensation)
- **Énergie de changement d'état** : $Q = m \times L$ ($L$ = chaleur latente en J/g)
  - $L_f$ (fusion) ; $L_v$ (vaporisation)
- Courbe de chauffage : paliers horizontaux aux changements d'état

---

### Chapitre 7 — Transformations chimiques (ordre=7)

**Fichier source :** `Chapitre_7_Transformations_chimiques.pdf`

**Leçons :**
- L1 : Réaction chimique — équation bilan et conservation
- L2 : Réactif limitant et rendement

**Concepts clés :**
- **Transformation chimique** : réorganisation des atomes → nouvelles espèces, liaisons rompues et formées
- **Conservation** : de la matière (masse), des atomes de chaque élément, des charges électriques
- **Équation bilan** : $aA + bB \to cC + dD$ (coefficients stœchiométriques entiers)
  - Équilibrer : nombre d'atomes de chaque élément égal des deux côtés
- **Réactif limitant** : espèce entièrement consommée en premier ($x_{max}$ le plus faible)
- **Espèce spectatrice** : présente dans le milieu mais ne réagit pas
- **Combustion du carbone** : $C + O_2 \to CO_2$ (totale) ; $2C + O_2 \to 2CO$ (incomplète)
- **Avancement** $x$ : $n_{\text{réactif}} = n_{\text{initial}} - \nu \cdot x$ ($\nu$ = coeff. stœchiométrique)

---

### Chapitre 8 — Synthèse d'espèces chimiques (ordre=8)

**Fichier source :** `Chapitre_8_Synthese_organique.pdf`

**Leçons :**
- L1 : Molécules naturelles et de synthèse
- L2 : Protocole de synthèse et sécurité au laboratoire

**Concepts clés :**
- **Molécule naturelle** : synthétisée par un organisme vivant (ex: caféine, aspirine naturelle)
- **Molécule de synthèse** : fabriquée industriellement ou au laboratoire (ex: aspirine synthétique)
- **Identique** : même formule, mêmes propriétés → indiscernable (ex: vitamine C naturelle = synthétique)
- **Extraction** : solide/liquide (filtration, essorage), liquide/liquide (ampoule à décanter)
- **Purification** : recristallisation (solides), distillation simple/fractionnée (liquides)
- **Test de pureté** : T° fusion précise (solide), n° réfractométrique ou T° ébullition précise (liquide)
- **Sécurité** : fiches de données de sécurité (FDS), symboles de danger (GHS), équipements de protection individuelle (EPI)
- **Rendement** : $r = \frac{n_{\text{obtenu expérimental}}}{n_{\text{théorique}}} \times 100\%$

---

### Chapitre 9 — Transformations nucléaires (ordre=9)

**Fichier source :** `Chapitre_9_Transformations_nucleaires.pdf` (si disponible) ou contenu basé sur le programme officiel

**Leçons :**
- L1 : Radioactivité — types de désintégration
- L2 : Loi de décroissance radioactive et applications

**Concepts clés :**
- **Noyau radioactif** (instable) : se désintègre en émettant un rayonnement pour atteindre la stabilité
- **Notation** du noyau : $^A_Z X$ (voir ch.3)
- **Désintégration α** : émission d'un noyau $^4_2He$ ; $A$ diminue de 4, $Z$ de 2
- **Désintégration β⁻** : émission d'un électron $^0_{-1}e$ et d'un antineutrino ; $Z$ augmente de 1, $A$ inchangé
- **Désintégration β⁺** : émission d'un positon $^0_{+1}e$ ; $Z$ diminue de 1, $A$ inchangé
- **Rayonnement γ** : émission de photons (pas de changement de $A$ ni $Z$) — accompagne souvent α ou β
- **Lois de conservation** : conservation du nombre de masse $A$ et du numéro atomique $Z$ total
- **Loi de décroissance** : $N(t) = N_0 e^{-\lambda t}$ ; $\lambda$ = constante de désintégration (s⁻¹)
- **Période radioactive** $T_{1/2} = \frac{\ln 2}{\lambda}$ : durée pour que la moitié des noyaux se désintègrent
- **Applications** : datation au carbone-14 ($T_{1/2} \approx 5730$ ans), médecine nucléaire (imagerie, traitement)

---

## Instructions d'exécution

Après génération du fichier :
```bash
docker compose run --rm --entrypoint python web manage.py seed_chimie_seconde
```

Le fichier doit être enregistré dans :
`backend/courses/management/commands/seed_chimie_seconde.py`
