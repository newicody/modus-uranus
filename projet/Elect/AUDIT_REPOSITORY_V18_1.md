# AUDIT REPOSITORY V18.1 — TOUR COMPLET
## Bonjour ! Démarrage par ce document

Ce document est ton point d'entrée pour l'intégration V18.1. Il fait le tour complet du repository : ce qui est livré, ce qui doit être mis à jour, ce qui est obsolète, et les améliorations de mise en page identifiées.

---

## 1 — FICHIERS LIVRÉS DANS V18.1

### À intégrer (4 nouveaux + 4 mis à jour)

| Fichier | Statut | Placement | Action |
|---|---|---|---|
| `README.md` | **REFONTE V18.1** | racine | Remplace README actuel |
| `AUDIT_PROJET_MODUS_V18_1.md` | **MIS À JOUR** | racine | Remplace V16, V17, V18 (archive les anciens) |
| `Architecture_Electrique_Electronique_V2.md` | Conservé V18 | racine | Document V2 inchangé |
| `mecanique_V18_1.md` | **NOUVEAU** | `/projet/mecanique` | Architecture mécanique systémique |
| `renovation_V18_1.md` | **NOUVEAU** | `/projet/renovation` | Rénovation (acoustique, nettoyage, anti-corrosion, visserie) |
| `confort_V18_1.md` | **NOUVEAU** | `/projet/confort` | Confort habitacle |
| `elec_V18_1_V1.md` | **MIS À JOUR** | `/projet/elec` | Précisions session du soir (caisson sous coffre, démarreur stock, USB hub, etc.) |
| `GUIDE_INTEGRATION_V18_1.md` | **NOUVEAU** | racine (temporaire) | Procédure d'intégration |
| `AUDIT_REPOSITORY_V18_1.md` | **CE FICHIER** | racine (temporaire) | Tour du repo + actions |

---

## 2 — FICHIERS DU REPOSITORY — STATUT ACTUEL

### ✅ FICHIERS À JOUR V16 (valides pour V18.1)

| Fichier | Statut | Note |
|---|---|---|
| `projet/Fournisseurs` | V16 valide | Contient les paniers à jour. À vérifier que RoyPow → EverExceed est bien noté |
| `projet/Entretient` | V16 valide | Phase 0 entretien K9K766, valide |
| `projet/Entretient_phase_2` | V16 valide | K9K896 confirmé en V16, valide |
| `projet/Outils` | V16 valide | Liste outils complète |
| `projet/Outils_audit` | V16 valide | Audit outillage Phase 0-3 |
| `projet/Protocole_préparation` | V16 valide | Anti-corrosion 5 étapes complet |
| `projet/Nettoyage_et_inspection` | V16 valide | Procédures inspection |
| `projet/ct` | V16 valide | Conformité CT |
| `projet/Casse` | V16 valide | Réduction prévue (voir section 3) |

### 🔄 FICHIERS À METTRE À JOUR

| Fichier | Problème | Action |
|---|---|---|
| `projet/Budget` | Structure 3 phases mais Phase 1 à supprimer | Refondre en V1/V2 + Phase 2 K9K896 |
| `projet/Taches` | Structure 3 phases mais Phase 1 à supprimer + précisions session du soir | Refondre en V1/V2 + ajouter tirages V0 |
| `projet/Budget_phase_2` | K9K858 obsolète (V15) | Passer en K9K896 (texte déjà V16 mais à vérifier) |
| `projet/Tache_phase_2` | K9K858 obsolète | Passer en K9K896 |
| `projet/elec` | RoyPow 18Ah au lieu d'EverExceed 8Ah + pas de précisions session du soir | **Remplacé par elec_V18_1_V1.md** |
| `AUDIT_PROJET_MODUS_V16.md` | Obsolète | **Remplacé par AUDIT_PROJET_MODUS_V18_1.md** + archive |

### ⛔ FICHIERS À SUPPRIMER

| Fichier | Raison |
|---|---|
| `projet/Cablage_electrique` (V5) | Doublon avec `projet/elec` (maintenant V18.1 V1) |
| `AUDIT_PROJET_MODUS_V16.md` | Remplacé par V18.1 (déplacer en `/archive/`) |
| `AUDIT_PROJET_MODUS_V17.md` (si existe) | Remplacé par V18.1 (déplacer en `/archive/`) |

### 📦 FICHIERS À RÉORGANISER

| Action | Détail |
|---|---|
| Créer `/archive/` | Y déplacer V16 et V17 obsolètes |
| Créer `/projet/mecanique` | Nouveau document mécanique |
| Créer `/projet/renovation` | Nouveau document rénovation |
| Créer `/projet/confort` | Nouveau document confort |
| Renommer si possible | Standardiser les noms : minuscules, underscores, .md systématique |

---

## 3 — CORRECTIONS DE CONTENU IDENTIFIÉES

### 3.1 — `projet/Casse` à réduire

Le fichier `projet/Casse` liste des pièces qui ont été remplacées par des achats neufs entretemps. À retirer de la liste casse :

| Pièce | Statut | Source actuelle |
|---|---|---|
| Gardes-boue | Acheté neuf | BLIC Trodo (panier actuel) |
| Cache moteur | Acheté neuf | BLIC Trodo (panier actuel) |
| Fusées AV | Acheté neuf | VAICO Autodoc (panier actuel) |
| Démarreur | **Conservé stock** (session du soir) | Modus stock reconditionné |

Pièces à **conserver** dans la liste casse :
- Support alu supérieur BV (OE 8200338385)
- Levier 6V + rotule + embase
- Câbles sélection + engagement
- Habillage console levier
- Pédalier embrayage complet
- **Fusées AR disques COMPLÈTES** (paire) — CRITIQUE
- Câbles frein à main

Note : **le démarreur n'est plus à récupérer en casse** (décision session du soir).

### 3.2 — `projet/Fournisseurs` — corrections

À vérifier/corriger :
- Remplacer **RoyPow LiFePO4 18Ah** par **EverExceed LiFePO4 8Ah** dans le panier Amazon
- Retirer **BDA604 + BDA605** (Audi, incompatibles) du panier Amazon
- Ajouter **composants V1 électronique** : LTC4359, MOSFET IRFP4368, NTC SCK-103, relais Songle, ESP32, INA219, DS18B20, hub USB, MT3608, TP4056, 18650 + holder
- Préciser **fusées AR** : à sourcer (OE Renault ou casse)
- **Powerbank USB** : à acquérir ou utiliser une existante

### 3.3 — `projet/Taches` — refonte

Le plan d'action doit être refait avec :
- **Suppression Phase 1** (turbo hybride VGT) confirmée
- **Strukture V0 / V1 / V2** au lieu de Phase 0-A / 0-B / 0-C / 0-D
- **V0 = Infrastructure** : caisson sous coffre, tirages câbles V1+V2, suppression masses châssis, traitement anti-corrosion
- **V1 = Électrique passif + mécanique complète** : faire rouler la Modus
- **V2 = Architecture iBSG 48V** : 6 modules custom + iBSG Valeo

### 3.4 — `projet/Budget` — refonte

Restructurer :
- **V0** : infrastructure (caisson sous coffre, tirages préparés)
- **V1** : matériel pour rouler (mécanique + électrique passif)
- **V2** : matériel iBSG + 6 modules custom
- **Phase 2** : swap K9K896 + gros turbo

---

## 4 — AMÉLIORATIONS DE MISE EN PAGE IDENTIFIÉES

### 🟢 `projet/Outils` — Restructuration en tableaux

**Problème** : très condensé, presque illisible pour navigation rapide.

**Suggestion** :
- Structurer en tableaux par catégorie : levage, serrage, distribution, freinage, électrique, anti-corrosion, divers
- Colonnes : Outil / Référence / Statut (✅ acheté / ⬜ à acheter) / Prix / Source / Date

### 🟢 `projet/Entretient` et `projet/Entretient_phase_2` — Tableaux d'intervalles

**Problème** : intervalles d'entretien en lignes denses, dur à scanner visuellement.

**Suggestion** :
- Tableau structuré avec colonnes : Échéance km / Tâche / Pièce / Référence / Prix estimé / Notes
- Ajouter colonne "Statut" (à faire / fait / à venir)

### 🟢 `projet/Fournisseurs` — Table des matières + dates

**Problème** : trois sections (payées / annulées / paniers) sans navigation claire.

**Suggestion** :
- Ajouter table des matières au début
- Dates de dernière modification par section
- Indicateurs visuels cohérents (✅ ❌ 🟡 ⛔) systématiques

### 🟢 `projet/Protocole_préparation` — Ancres internes

**Problème** : très long (>30 pages texte), difficile à naviguer.

**Suggestion** :
- Table des matières détaillée au début
- Ancres internes (`<a name="..."></a>`) pour navigation rapide vers sections 1-9

### 🟢 `projet/Nettoyage_et_inspection` — Fusion possible

**Problème** : redondance partielle avec `Protocole_préparation`.

**Suggestion** :
- Soit fusionner les deux en un seul `Protocole_renovation_complet.md`
- Soit clarifier dans chaque header la portée de chaque document

### 🟢 `projet/Casse` — Structuration en tableau

**Problème** : format texte simple, pas accessible visuellement.

**Suggestion** :
- Structurer en tableau : Pièce / Référence / État / Statut commande / Date / Notes
- Retirer pièces commandées neuves (voir 3.1)

### 🟢 `projet/elec` (sera V18.1)

**Problème** : V16 obsolète.

**Suggestion** : remplacé par `elec_V18_1_V1.md` qui intègre toutes les précisions.

---

## 5 — STRUCTURE REPOSITORY CIBLE V18.1

```
./
├── README.md                                      # REFONTE V18.1
├── AUDIT_PROJET_MODUS_V18_1.md                    # MIS À JOUR
├── Architecture_Electrique_Electronique_V2.md     # CONSERVÉ V18
│
├── archive/                                       # NOUVEAU
│   ├── AUDIT_PROJET_MODUS_V16.md
│   ├── AUDIT_PROJET_MODUS_V17.md
│   ├── elec_V16
│   ├── elec_V17.md
│   └── Cablage_electrique_V5_obsolete
│
├── projet/                                        # Documents projet (réorganisé)
│   ├── Budget                                     # À refondre V18.1
│   ├── Budget_phase_2                             # À vérifier K9K896
│   ├── Taches                                     # À refondre V18.1
│   ├── Tache_phase_2                              # À vérifier K9K896
│   ├── Entretient                                 # V16 valide
│   ├── Entretient_phase_2                         # V16 valide
│   ├── elec                                       # Contenu de elec_V18_1_V1.md
│   ├── mecanique                                  # NOUVEAU contenu de mecanique_V18_1.md
│   ├── renovation                                 # NOUVEAU contenu de renovation_V18_1.md
│   ├── confort                                    # NOUVEAU contenu de confort_V18_1.md
│   ├── Fournisseurs                               # V16 + corrections
│   ├── Casse                                      # V16 réduit (voir 3.1)
│   ├── Outils                                     # V16 valide (mise en page à améliorer)
│   ├── Outils_audit                               # V16 valide
│   ├── Protocole_préparation                      # V16 valide (mise en page à améliorer)
│   ├── Nettoyage_et_inspection                    # V16 valide (fusion possible)
│   └── ct                                         # V16 valide
│
├── IA/                                            # CONSERVÉ
│   ├── links/
│   └── corrosion_gérale
│
├── FOURNISSEURS/                                  # CONSERVÉ
├── Commandes/                                     # CONSERVÉ
│   ├── EDITING.md
│   ├── PROCESSING.md
│   └── ACHIVED.md
│
├── Journal.md                                     # CONSERVÉ
├── methodes_modus/                                # CONSERVÉ
├── problemes/                                     # CONSERVÉ
├── café_modus/                                    # CONSERVÉ
├── garage/                                        # CONSERVÉ
├── tools/                                         # CONSERVÉ
├── carnet_entretient/                             # CONSERVÉ
├── programmation/                                 # CONSERVÉ
├── todolist/                                      # CONSERVÉ
│
├── process/                                       # CONSERVÉ
│   ├── phase0/
│   ├── phase1/                                    # OBSOLÈTE — à vider ou archiver
│   └── phase2/
│
├── prévisionnel/                                  # CONSERVÉ
├── insonorisation/                                # CONSERVÉ ou fusion avec renovation
├── inspection/                                    # CONSERVÉ ou fusion avec renovation
├── nettoyage/                                     # CONSERVÉ ou fusion avec renovation
└── vis_boulons_filetages_écrous_rondelles/       # CONSERVÉ
```

---

## 6 — ACTIONS PRIORITAIRES POUR L'INTÉGRATION

### Niveau 1 — Critique (à faire en premier)

1. **Backup repository** avant toute modification
2. **Créer branche `update_V18_1`** pour le travail
3. **Créer `/archive/`** et y déplacer AUDIT V16, V17, elec V16 obsolètes
4. **Supprimer** `projet/Cablage_electrique` (doublon)
5. **Copier** les 8 fichiers V18.1 livrés à leur emplacement cible

### Niveau 2 — Important (à faire ensuite)

6. **Refondre** `projet/Budget` en structure V0/V1/V2 + Phase 2 (à faire dans une session dédiée)
7. **Refondre** `projet/Taches` en structure V0/V1/V2 + Phase 2 (à faire dans une session dédiée)
8. **Corriger** `projet/Fournisseurs` (RoyPow → EverExceed, retraits BDA, ajouts V1 électronique)
9. **Réduire** `projet/Casse` (retirer pièces neuves)
10. **Vérifier** `projet/Budget_phase_2` et `projet/Tache_phase_2` (K9K896)

### Niveau 3 — Confort (à faire quand possible)

11. Améliorer mise en page `projet/Outils` (tableaux par catégorie)
12. Améliorer mise en page `projet/Entretient` (tableaux d'intervalles)
13. Ajouter ancres internes à `projet/Protocole_préparation`
14. Fusionner ou clarifier `projet/Nettoyage_et_inspection` vs `projet/Protocole_préparation`
15. Vider ou archiver `process/phase1/` (Phase 1 supprimée)

### Niveau 4 — Préparation Infineon

16. Imprimer en couleur A4 :
    - `AUDIT_PROJET_MODUS_V18_1.md`
    - `Architecture_Electrique_Electronique_V2.md`
    - `elec_V18_1_V1.md`
    - Photos véhicule
17. Préparer BOM ciblée par module V2 pour échantillons Infineon
18. Préparer questions techniques précises par module (voir Architecture V2 section 14)

---

## 7 — POINTS DE VIGILANCE V18.1

### Décisions actées (session du soir)

| Décision | Impact |
|---|---|
| Démarreur stock reconditionné (pas Clio 3 GT) | Économie 50-100€ + temps sourcing |
| Caisson sous coffre (pas sous banquette) | Volume 2-3× plus grand, dimensions à mesurer |
| Hub USB interne 1→3 voies | Réveil ESP32 prioritaire, chauffage, MT3608 |
| Mode rescue séquentiel via 18650 | Réveil intelligent au lieu de brutal 5V→14V |
| Suppression masses châssis Phase 0 | Câblage propre étoile depuis caisson sous coffre |
| Tirages V1+V2 préparés en V0 | Gain massif pour V2 (juste connexion ensuite) |
| Caisson chauffé en V0 | Infrastructure prête avant tout |
| Port USB conducteur | Powerbank branchable depuis la place conducteur |

### Décisions architecturales actées (V17/V18)

| Décision | Impact |
|---|---|
| Phase 1 turbo hybride supprimée | Économie 1300-2000€ |
| Compresseur AC supprimé Phase 0 | Libère courroie pour iBSG (+22% couple) |
| Pas de stop-start | Préserve ECU stock |
| EverExceed 8Ah remplace RoyPow 18Ah | Format compact pour caisson |
| Pack LTO 10Ah 20S Tycorun pour V2 | 7 kg, 615-825€ |
| Banc supercondos 48V V2 | 3,5 kg, 250-400€ |
| Architecture 6 modules + MCU AURIX | Plan V2 documenté |

### À vérifier physiquement (dès accès véhicule)

| Vérification | Procédure |
|---|---|
| Dimensions emplacement roue de secours | Mètre ruban : diamètre haut, diamètre bas, profondeur, accès charnières |
| Réf. supports étrier AV (Autodoc) | ABS / 260mm compatible |
| Réf. support étrier AR ×1 (Autodoc) | Vérifier si universel G+D ou si manque le 2e côté |
| Kit Goodridge | AV seul ou AV+AR après conversion disque |

---

## 8 — RÉCAPITULATIF BUDGET V18.1

| Phase | Coût estimé | Période |
|---|---|---|
| **Déjà payé** | 1 087 € | Mai 2026 |
| **Paniers V1** (13 fournisseurs) | ~4 736 € | Juin 2026 |
| **Restes V1** (fusées AR, pneus, casse, EverExceed, composants V1, powerbank) | 730-1 330 € | Juin-Juillet 2026 |
| **TOTAL V1** (faire rouler) | **6 550-7 150 €** | Q3 2026 |
| **V2** (iBSG + 6 modules custom + 4 mois plus tard) | 4 660-7 960 € | Q1-Q2 2027 |
| **Phase 2** (swap K9K896 + gros turbo) | 1 860-3 935 € | Q3-Q4 2027 |
| **TOTAL PROJET COMPLET** | **12 800-18 400 €** | 2-3 ans |

---

## 9 — TIMELINE PROPOSÉE

### Juin 2026
- Salon Infineon Nuremberg (semaine 1)
- Corrections paniers V18.1
- Commandes V1 mécanique + EverExceed + composants V1 + powerbank

### Juillet-Août 2026
- Location box garage
- Mesure emplacement roue de secours
- Construction caisson V0 sous coffre

### Septembre-Octobre 2026 — Phase V1 mécanique
- Démontage complet
- Anti-corrosion Férose + Restom + Owatrol
- Insonorisation HASKYY alubutyl
- Transmission TL4B043 + cardans + embrayage
- Freinage + suspension + jantes
- Tirages câbles V1 + V2 préparés
- Suppression masses châssis

### Novembre-Décembre 2026 — Phase V1 électrique
- Assemblage caisson sous coffre (EverExceed + supercondos + ESP32 + LTC4359)
- Mode rescue USB
- Câblage cranking
- Maintenance alternateur + démarreur stock
- Reprog stage 0
- **Test routier V1 → Modus roule**

### Q1 2027 — Préparation V2
- Sourcing iBSG Valeo en casse
- Conception PCB BMS + onduleur
- Pack LTO 10Ah 20S + supercondos 48V

### Q2 2027 — Déploiement V2
- Bracket d'adaptation K9K
- Intégration véhicule iBSG
- Onduleur SiC custom 12 kW
- Tests progressifs
- **Test routier V2 → boost iBSG actif**

### Q3 2027 — V2.1 à V2.4
- Capteurs distribués (V2.1)
- Signalisation MT modulée (V2.2)
- Corrosion RFID (V2.3)

### 2028 — Phase 2 + finitions
- Swap K9K896 + gros turbo
- Tableau de bord Mega Drive (V2.4)
- Documentation finale projet

---

## 10 — POUR LA SUITE

Quand tu auras intégré V18.1, on pourra travailler dans des discussions dédiées sur :

1. **Budget V18.1** — refonte V0/V1/V2 + Phase 2
2. **Taches V18.1** — refonte V0/V1/V2 + Phase 2
3. **Salon Infineon** — préparation des rendez-vous et questions
4. **V0 Infrastructure** — détail du caisson sous coffre + tirages câbles V1+V2
5. **Module 1 V2 — BMS OptiMOS** (post-V1)
6. **Module 2 V2 — Stockage 48V LTO + supercondos** (post-V1)
7. **Module 3 V2 — iBSG Valeo + onduleur SiC** (post-V1)
8. **Module 4 V2 — Signalisation MT** (post-V1)
9. **Module 5 V2 — Capteurs distribués** (post-V1)
10. **Module 6 V2 — Corrosion RFID** (post-V1)
11. **MCU central AURIX** (post-V1)
12. **Mega Drive tableau de bord** (phase finale)

Bonne nuit ! 🌙

---

*AUDIT REPOSITORY V18.1 — 1er juin 2026*
*Tour complet du repository + actions d'intégration*
