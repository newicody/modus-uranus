# PROJET MODUS JP0F — VF1JP0F0H43308282

> Renault Modus 1.5 dCi 2008 (86 ch) — 130 000 km — préparation et fiabilisation complète
> Stratégie V0/V1/V2 + Phase 2 — Objectif 300 000 km

---

## 1 — VÉHICULE

| Identification | Valeur |
|---|---|
| Marque / Modèle | Renault Modus (Phase II) 1.5 dCi 86 CH |
| VIN | VF1JP0F0H43308282 |
| Type véhicule | JP0F |
| Moteur d'origine | K9K766 (1461 cm³, Euro 4, Common Rail) |
| Boîte d'origine | JA5 (5V Quickshift robotisée) |
| Boîte cible | TL4B043 neuve (6V) |
| Kilométrage | 130 000 km |
| Année | 2008 |
| Couple bridé boîte | 240-260 Nm |
| Objectif fiabilité | 300 000 km |

---

## 2 — STRATÉGIE V0/V1/V2 + PHASE 2

Le projet est découpé en 4 étapes pour pragmatisme et étalement budgétaire.

### V0 — Infrastructure (Q3 2026)

Préparation pendant le démontage complet.

- Caisson sous coffre (emplacement roue de secours) avec placoplatre ignifugé
- Tirages câbles V1 + V2 préparés ensemble
- Suppression masses châssis (topologie étoile depuis caisson)
- Anti-corrosion complet (Férose + Restom EAF 2092 + Owatrol)
- Insonorisation HASKYY alubutyl 2mm
- Système thermique passif (KSD301 + chauffage PTC + ventilateur)

### V1 — Faire rouler la Modus (Q3-Q4 2026)

Mécanique complète + électrique passif simple.

- TL4B043 + transmission + freinage + suspension + jantes
- Reprog stage 0 (240-260 Nm)
- Démarreur Modus stock reconditionné
- EverExceed LiFePO4 8Ah + Maxwell 16V 100F supercondos
- ESP32 télémétrie au caisson
- Hub USB 1→3 voies (charge 18650 + chauffage + MT3608 rescue)
- Mode rescue séquentiel via powerbank

### V2 — Architecture iBSG 48V (Q1-Q2 2027)

Remplacement alternateur + démarreur par iBSG Valeo 12 kW.

- iBSG Valeo de casse Mercedes Sprinter eDrive
- Pack LTO 10Ah 20S (7 kg) + banc supercondos 48V (3,5 kg)
- DC/DC bidirectionnel 12V↔48V (500W)
- Onduleur SiC custom 12 kW
- BMS LiFePO4 custom OptiMOS
- 6 modules PCB custom + MCU central AURIX TC375
- Signalisation MT modulée (V2.2)
- Surveillance corrosion RFID NAC1080 (V2.3)
- Tableau de bord Mega Drive (V2.4, phase finale 2028)

### Phase 2 — Swap K9K896 (Q3-Q4 2027+)

Quand le K9K766 montre ses limites.

- K9K896 + ECU Bosch + faisceau + FAP
- Gros turbo (à définir)
- iBSG conservé (compatible à 95%)
- 260 Nm plat large plage

---

## 3 — SOUS-SYSTÈMES DOCUMENTÉS

Chaque sous-système a son document de référence dédié dans `/projet/` :

### Électrique et électronique

- **`elec`** — Câblage électrique V1 (architecture passive minimaliste pour faire rouler) — voir `elec_V18_1_V1.md`
- **`Architecture_Electrique_Electronique_V2.md`** — Architecture complète V2 (iBSG + 6 modules custom) — référence à la racine

### Mécanique

- **`mecanique`** — Architecture mécanique systémique 7 couches (groupe motopropulseur, transmission, suspension/direction, freinage, roues/pneus, admission/échappement, infrastructure moteur) — voir `mecanique_V18_1.md`

### Rénovation

- **`renovation`** — Architecture rénovation 6 couches (inspection, nettoyage, anti-corrosion, insonorisation, fiabilisation faisceaux, visserie inox) — voir `renovation_V18_1.md`

### Confort

- **`confort`** — Architecture confort 7 couches (acoustique, ergonomie, climatisation, sellerie, éclairage, tableau de bord, sécurité) — voir `confort_V18_1.md`

---

## 4 — DOCUMENTS PROJET COMPLEMENTAIRES

Dans `/projet/` :

### À jour V18.1
- `elec` (V18.1 V1)
- `mecanique` (V18.1 nouveau)
- `renovation` (V18.1 nouveau)
- `confort` (V18.1 nouveau)

### À jour V16 (valides V18.1)
- `Fournisseurs` — Contacts et paniers
- `Entretient` — Entretien préventif Phase 0
- `Entretient_phase_2` — Entretien Phase 2 K9K896
- `Outils` — Liste outils complète
- `Outils_audit` — Audit outillage Phase 0-3
- `Protocole_préparation` — Anti-corrosion 5 étapes (intégré dans `renovation`)
- `Nettoyage_et_inspection` — Procédures inspection (intégré dans `renovation`)
- `ct` — Conformité CT
- `Casse` — Pièces de casse Clio 3 GT

### À mettre à jour V18.1
- `Budget` — Refonte V0/V1/V2 + Phase 2 (à faire dans une session dédiée)
- `Taches` — Refonte V0/V1/V2 + Phase 2 (à faire dans une session dédiée)
- `Budget_phase_2` — Vérifier K9K896 confirmé
- `Tache_phase_2` — Vérifier K9K896 confirmé

### Obsolète à archiver
- `AUDIT_PROJET_MODUS_V16.md` → `/archive/`
- `Cablage_electrique_V5` (doublon) → supprimer

---

## 5 — STRUCTURE REPOSITORY V18.1

```
./
├── README.md                                      # CE FICHIER (V18.1)
├── AUDIT_PROJET_MODUS_V18_1.md                    # Audit principal V18.1
├── Architecture_Electrique_Electronique_V2.md     # Architecture V2 (référence)
├── AUDIT_REPOSITORY_V18_1.md                      # Tour du repo + actions
├── GUIDE_INTEGRATION_V18_1.md                     # Procédure intégration
│
├── archive/                                       # Versions obsolètes
│   ├── AUDIT_PROJET_MODUS_V16.md
│   ├── AUDIT_PROJET_MODUS_V17.md
│   ├── elec_V16
│   └── Cablage_electrique_V5_obsolete
│
├── projet/                                        # Documents projet par fonction
│   ├── elec                                       # V18.1 - Câblage V1
│   ├── mecanique                                  # V18.1 - Architecture mécanique
│   ├── renovation                                 # V18.1 - Architecture rénovation
│   ├── confort                                    # V18.1 - Architecture confort
│   ├── Budget                                     # V18.1 (à refondre V0/V1/V2)
│   ├── Budget_phase_2                             # K9K896
│   ├── Taches                                     # V18.1 (à refondre V0/V1/V2)
│   ├── Tache_phase_2                              # K9K896
│   ├── Entretient                                 # Phase 0
│   ├── Entretient_phase_2                         # K9K896
│   ├── Fournisseurs                               # 13 fournisseurs
│   ├── Casse                                      # Clio 3 GT
│   ├── Outils                                     # Liste outils
│   ├── Outils_audit                               # Audit Phase 0-3
│   ├── Protocole_préparation                      # Détail anti-corrosion (compl. à renovation)
│   ├── Nettoyage_et_inspection                    # Détail nettoyage (compl. à renovation)
│   └── ct                                         # Conformité CT
│
├── IA/                                            # Conversations IA archivées
├── FOURNISSEURS/                                  # Bons de commande détaillés
├── Commandes/                                     # Commandes en cours/passées
├── Journal.md                                     # Journal de bord
├── methodes_modus/                                # Astuces Modus
├── problemes/                                     # Problèmes rencontrés
├── café_modus/                                    # Notes diverses
├── garage/                                        # Location box
├── tools/                                         # Outils détaillés
├── carnet_entretient/                             # Carnet entretien
├── programmation/                                 # Reprog ECU
├── todolist/                                      # Process à faire
├── process/                                       # Instructions opératoires
├── prévisionnel/                                  # Performances attendues
├── insonorisation/                                # Réduction bruit (intégré renovation)
├── inspection/                                    # Procédures inspection (intégré renovation)
├── nettoyage/                                     # Procédures nettoyage (intégré renovation)
└── vis_boulons_filetages_écrous_rondelles/       # Visserie détaillée (intégré renovation)
```

---

## 6 — BUDGET PROJET V18.1

### Phase 0 V0+V1 (faire rouler)

| Catégorie | Montant |
|---|---|
| Déjà payé | 1 087 € |
| Paniers V1 en cours (13 fournisseurs) | ~4 736 € |
| Restes V0+V1 (fusées AR, pneus, casse, EverExceed, composants V1, tirages V0) | 970-1 580 € |
| **TOTAL PHASE 0 (V0+V1)** | **6 793-7 403 €** |

### V2 (iBSG + 6 modules custom)

| Catégorie | Montant |
|---|---|
| iBSG Valeo + adaptation + onduleur | 1 730-3 440 € |
| Pack LTO 10Ah 20S + supercondos 48V + BMS | 1 237-1 786 € |
| Modules 1-4-5-6 + MCU AURIX + DC/DC | 1 595-2 615 € |
| **TOTAL V2** | **4 562-7 841 €** |

### Phase 2 (swap K9K896 + gros turbo)

| Catégorie | Montant |
|---|---|
| Moteur + ECU + faisceau + FAP (casse) | 900-2 140 € |
| Préparation + reprog + consommables | 560-1 195 € |
| Gros turbo | 400-600 € |
| **TOTAL PHASE 2** | **1 860-3 935 €** |

### Total projet

**13 215-19 179 €** étalés sur 2-3 ans.

---

## 7 — PERFORMANCE ATTENDUE

| Étape | 0-100 km/h | Couple max au volant moteur | Note |
|---|---|---|---|
| Modus stock 2008 | 13,0 s | 200 Nm | Référence départ |
| V1 (reprog stage 0) | 11,5-12 s | 240-260 Nm | Faire rouler |
| V2 (iBSG 12 kW + pack LTO) | 9,5-10,5 s | 260 Nm dès 1500 tr/min | Hybride mild |
| Phase 2 (K9K896 + gros turbo + iBSG) | 7,5-8,5 s | 260 Nm plat large plage | Performance max sous limite TL4 |

---

## 8 — STATUT ACTUEL (1er juin 2026)

### Avancement
- ✅ Audit V18.1 réalisé avec stratégie V0/V1/V2 + Phase 2
- ✅ TL4B043 payée et reçue (Eurofrance24)
- ✅ Powerflex ×6 payés et reçus (GT2i)
- ✅ Outillage de base acquis
- ✅ Architecture V1 minimaliste définie (caisson sous coffre, démarreur stock)
- ✅ Architecture V2 documentée (iBSG 48V, 6 modules custom)
- ✅ Documents complémentaires créés : mécanique, rénovation, confort
- 🟡 Paniers V1 en cours (13 fournisseurs)
- 🟡 Vérifications physiques à faire (emplacement roue secours, supports étrier)
- ⬜ Exécution V0 + V1

### Prochaines étapes

**Cette semaine** :
1. Salon Infineon Nuremberg (semaine du 7 juin) — contacts pour V2
2. Mesure physique emplacement roue de secours
3. Corrections paniers V18.1 (retraits BDA, ajouts EverExceed + composants V1 + tirages V0)

**Mois prochain** :
4. Commandes Phase 0 V1 mécanique + EverExceed + composants V1 + powerbank
5. Location box garage
6. Préparation V0 (caisson sous coffre + tirages câbles + anti-corrosion + insonorisation)

---

## 9 — CONTACTS PRINCIPAUX

### Fournisseurs V0 + V1

| Fournisseur | URL | Spécialité |
|---|---|---|
| Carter Cash | carter-cash.com | Retrait Essey-lès-Nancy |
| Autodoc | autodoc.fr | Pièces auto |
| Eurofrance24 | eurofrance24.com | BV neuves |
| Norauto | norauto.fr | Outils, pressage, géométrie |
| Oscaro | oscaro.com | Pièces en ligne |
| GT2i | gt2i.fr | Performance, Powerflex |
| Ultraperformance | ultraperformance.fr | Jantes |
| Goodridge | goodridge.com | Flexibles aviation |
| Amazon | amazon.fr | Consommables, électrique |
| AliExpress | aliexpress.com | Maxwell supercondos |
| R.tech | rtec.ws | Bilstein, suspension |
| Trodo | trodo.fr | Pièces auto |
| Restom | restom.net | Anti-corrosion époxy |

### Fournisseurs V2 (futur)

| Fournisseur | URL | Spécialité |
|---|---|---|
| NKON.nl | nkon.nl | Cellules LTO Pays-Bas |
| DIYbattery.eu | diybattery.eu | Cellules LTO + BMS Allemagne |
| Tycorun (AliExpress) | aliexpress.com | LTO 10Ah économique |
| Mouser / Farnell | mouser.com / farnell.com | Infineon, AURIX |
| JLCPCB / PCBWay | jlcpcb.com / pcbway.com | Fabrication PCB custom |

### Documentation technique
- **RTA B775.5** : Modus 1.5 dCi
- **RTA B700.5** : Clio 3 (donneur)
- **OE Renault** : 320109255R / 8201057476 (TL4B043)

---

## 10 — PHILOSOPHIE DU PROJET

Ce projet combine plusieurs objectifs :

- **Fiabilité** : voiture qui doit tenir 300 000 km avec maintenance minimale
- **Performance** : ressentir l'amélioration sans toucher au moteur thermique en V1
- **Économie** : conso optimisée par hybridation 48V mild (V2)
- **Originalité technique** : architecture custom moderne (SiC, RISC-V, FOC, RFID corrosion)
- **Plaisir** : Mega Drive comme tableau de bord (V2.4), identité visuelle Sega
- **Apprentissage** : projet exploratoire pour monter en compétence sur tous les sous-systèmes automotive

La stratégie **V0/V1/V2** est cohérente avec cette philosophie :
- V0 prépare l'infrastructure (caisson + tirages câbles + anti-corrosion)
- V1 fait rouler vite la voiture
- V2 ajoute l'hybridation 48V quand le V1 est stable
- Phase 2 garde la flexibilité d'évolution moteur thermique

---

## 11 — POUR L'INTÉGRATION DU REPOSITORY

Pour intégrer V18.1, voir le document `GUIDE_INTEGRATION_V18_1.md` qui détaille :

1. La procédure git de mise à jour
2. Les fichiers à supprimer / archiver / créer
3. Les corrections de paniers Fournisseurs
4. Les améliorations de mise en page identifiées sur d'autres fichiers du repository

L'audit complet du repository est dans `AUDIT_REPOSITORY_V18_1.md` (à lire en premier).

---

*PROJET MODUS JP0F — Dernière mise à jour README : 1er juin 2026*
*Version audit : V18.1 — Stratégie V0/V1/V2 + Phase 2 actée*
*Documents complets : audit, electrical V1, architecture V2, mécanique, rénovation, confort*
