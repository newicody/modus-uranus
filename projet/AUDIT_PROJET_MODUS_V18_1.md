# AUDIT PROJET V18.1 — MODUS JP0F — VF1JP0F0H43308282
## 1er juin 2026 — Stratégie V0/V1/V2 + Phase 2

---

## 0 — VÉHICULE

| Identification | Valeur |
|---|---|
| Marque / Modèle | Renault Modus (Phase II) 1.5 dCi 86 CH |
| VIN | VF1JP0F0H43308282 |
| Type véhicule | JP0F |
| Moteur d'origine | K9K766 (1461 cm³, Euro 4, Common Rail) |
| Boîte d'origine | JA5 (5 vitesses Quickshift robotisée) |
| Kilométrage | 130 000 km |
| Année | 2008 |
| Boîte cible | TL4B043 neuve (Eurofrance24 — 531,79 € PAYÉ) |
| Couple bridé boîte | 240-260 Nm |
| Objectif fiabilité | 300 000 km |

---

## 1 — STRATÉGIE V0 / V1 / V2 + PHASE 2

### Évolution V17 → V18 → V18.1

| Version | Stratégie | Statut |
|---|---|---|
| V16 | 3 phases mécaniques (KP35 → BV39 → K9K896) | Obsolète |
| V17 | Architecture électronique 6 modules ajoutée | Intermédiaire |
| V18 | Stratégie V1/V2 actée, Phase 1 supprimée | Précédent |
| **V18.1** | **V0 infrastructure + V1 rouler + V2 iBSG + Phase 2 swap** | **Actuel** |

### Découpage V18.1

| Étape | Périmètre | Période visée |
|---|---|---|
| **V0** | Infrastructure : caisson sous coffre + tirages câbles V1+V2 + suppression masses châssis + anti-corrosion + insonorisation | Q3 2026 |
| **V1** | Mécanique complète + électrique passif simple → la Modus roule | Q3-Q4 2026 |
| **V2** | Architecture iBSG 48V + 6 modules custom + MCU AURIX | Q1-Q2 2027 |
| **Phase 2** | Swap K9K896 + gros turbo + démarreur (iBSG conservé) | Q3-Q4 2027+ |

### Détail V0 — Infrastructure (à faire EN PREMIER)

C'est la phase préparatoire pendant qu'on démonte tout. Tout ce qui peut être anticipé pour V1+V2 doit être préparé maintenant.

- Construction du **caisson sous coffre** (emplacement roue de secours) avec mousse, plancher renforcé, ventilation
- Système thermique passif (KSD301 + chauffage PTC + ventilateur fail-safe ON)
- Étanchéité et fixations IP65
- Passages câbles pré-percés avec passe-fils caoutchouc
- **Tirage des câbles V1** : cranking, alternateur, USB conducteur, faisceau ESP32
- **Tirage des câbles V2 en attente** : bus 48V 25-35mm², CAN-C blindé, LIN, signalisation MT, RFID corrosion (24 points)
- **Suppression des masses châssis** corrosives : retours dédiés pour tous les circuits (étoile depuis caisson)
- **Anti-corrosion complet** : Férose + Restom EAF 2092 + Owatrol
- **Insonorisation HASKYY** alubutyl 2mm (cloison, plancher, portes, coffre)

### Détail V1 — Électrique passif + mécanique complète

Faire rouler la Modus avec une électronique simple et fiable.

**Mécanique** :
- TL4B043 + transmission complète (cardans SKF, embrayage Valeo 845077)
- Freinage AV+AR (FEBI + TRW + Brembo + flexibles HEL/Goodridge)
- Suspension Bilstein B8 + Eibach Pro-Kit + Powerflex ×6
- Jantes JR-7 16" + pneus 195/55 R16
- FMIC NRF 30481
- Oil catch can
- Reprog stage 0 (240-260 Nm)
- **Démarreur Modus stock reconditionné** (pas Clio 3 GT — décision actée)
- Alternateur K9K stock (charbons + bagues neufs)

**Électrique passif** :
- EverExceed LiFePO4 12V 8Ah (déjà commandé)
- Maxwell 16V 100F supercondos (déjà commandé)
- Sous-circuit avant LTC4359 + pré-charge NTC
- ESP32 télémétrie au caisson sous coffre
- **Hub USB interne 1→3 voies** : charge cellule 18650 / chauffage PTC / MT3608 rescue
- **Mode rescue séquentiel** : powerbank → 18650 ESP32 → ESP32 réveille → diagnostique → active chauffage si besoin → réveille MT3608 → bus 12V vivant
- **Port USB conducteur** (console centrale) pour brancher powerbank

### Détail V2 — Architecture iBSG 48V

Évolution majeure 4-6 mois après V1 stable.

- iBSG Valeo 12 kW (de casse Mercedes Sprinter eDrive)
- Suppression alternateur K9K + démarreur stock (remplacés par iBSG)
- Pack LTO 10Ah 20S Tycorun/Liantian (7 kg)
- Banc supercondos 48V (20× 1500F = 3,5 kg)
- DC/DC bidirectionnel 12V↔48V (500W)
- Onduleur SiC custom 12 kW
- BMS LiFePO4 custom OptiMOS (remplace BMS interne EverExceed)
- 6 modules PCB custom + MCU central AURIX TC375
- Signalisation MT modulée par décélération
- Surveillance corrosion RFID NAC1080
- Tableau de bord Mega Drive (phase finale 2028)

### Détail Phase 2 — Swap K9K896

Quand le K9K766 montre ses limites.

- Bloc K9K896 + ECU Bosch EDC17C84 + faisceau + FAP
- Gros turbo (à définir)
- Démarreur conservé (sera l'iBSG V2 si déjà installé)
- iBSG V2 transférable à 95% (juste mapping ECU différent)
- 260 Nm plat large plage

---

## 2 — CHANGEMENTS V18 → V18.1 (session du soir)

| Élément | V18 | V18.1 |
|---|---|---|
| Position caisson | Sous banquette AR | **Sous coffre** (emplacement roue de secours) |
| Démarreur | Clio 3 GT donneur | **Modus stock reconditionné** |
| Distribution USB | Port USB direct vers MT3608 | **Hub USB 1→3 voies** internes (TP4056, chauffage, MT3608) |
| Mode rescue | Direct MT3608 5V→14V | **Séquentiel** : 18650 ESP32 → diagnostic → chauffage si besoin → MT3608 |
| Masses châssis | Suppression progressive | **Suppression totale en V0** (anti-corrosion + étoile) |
| Tirages V2 | À faire le moment venu | **Préparés en V0** pendant démontage |
| Caisson chauffé | En V1 | **En V0** (infrastructure de base) |
| Port USB | Caisson uniquement | **Caisson + console centrale** (powerbank accessible) |

---

## 3 — RÉSUMÉ FINANCIER

### Coûts engagés

| | Montant |
|---|---|
| **Déjà payé** | 1 087 € |
| Eurofrance24 (TL4B043 + livraison) | 531,79 € |
| GT2i (Powerflex ×6) | 392,40 € |
| Norauto (outils ×3 commandes) | 162,88 € |
| **Paniers V1** (13 fournisseurs) | ~4 736 € |

### Restes à acheter V0+V1

| Catégorie | Estimation |
|---|---|
| Fusées AR version disque | 100-200 € |
| Pneus 195/55 R16 ×4 | 240-400 € |
| Pièces casse Clio 3 GT (levier 6V, pédalier, câbles, support alu) | 200-400 € |
| EverExceed LiFePO4 8Ah (remplacement RoyPow) | 50-80 € |
| Composants électronique V1 | 60-100 € |
| Hub USB + connectique interne caisson | 20-40 € |
| Powerbank USB (ou existante) | 30-50 € |
| Tirages câbles V2 préparés en V0 | 200-400 € |
| Divers (fusibles, gaines, cosses) | 50-100 € |
| **TOTAL RESTE V0+V1** | **950-1 770 €** |

### Coûts par étape

| Étape | Coût estimé | Cumul |
|---|---|---|
| **V0** Infrastructure (inclus dans V1) | inclus | 6 770-7 590 € |
| **V1** Mécanique + électrique passif | 6 770-7 590 € | 6 770-7 590 € |
| **V2** iBSG + 6 modules custom | 4 660-7 960 € | 11 430-15 550 € |
| **Phase 2** K9K896 + gros turbo | 1 860-3 935 € | **13 290-19 485 €** |

---

## 4 — ACTIONS PRIORITAIRES V18.1

| # | Action | Priorité | Échéance |
|---|---|---|---|
| 1 | Retirer BDA604 + BDA605 Amazon | 🔴 Critique | Avant commandes |
| 2 | Sourcer fusées AR version disque | 🔴 Critique | Avant V1 mécanique |
| 3 | Mesurer emplacement roue de secours | 🔴 Critique | Dès accès véhicule |
| 4 | Remplacer RoyPow 18Ah par EverExceed 8Ah | 🟡 Important | Avant commandes |
| 5 | Ajouter composants V1 électronique au panier | 🟡 Important | Avant commandes |
| 6 | Ajouter tirages câbles V2 au panier | 🟡 Important | Avant V0 |
| 7 | Acquérir/identifier powerbank USB | 🟢 Quand possible | Avant V1 électrique |
| 8 | Vérifier supports étrier AV ABS 260mm | 🟡 Important | Avant commandes |
| 9 | Vérifier kit Goodridge AV+AR | 🟡 Important | Avant commandes |
| 10 | Réduire Casse (pièces neuves retirées + démarreur retiré) | 🟢 Quand possible | Mise à jour fichier |
| 11 | Refondre Budget V18.1 (V0/V1/V2) | 🟢 Plus tard | Dans une session dédiée |
| 12 | Refondre Taches V18.1 (V0/V1/V2) | 🟢 Plus tard | Dans une session dédiée |

---

## 5 — DOCUMENTS LIVRÉS V18.1

| Document | Statut | Référence |
|---|---|---|
| `README.md` | Refonte | Point d'entrée repository |
| `AUDIT_PROJET_MODUS_V18_1.md` | Ce document | Audit principal |
| `Architecture_Electrique_Electronique_V2.md` | Conservé V18 | Architecture iBSG complète |
| `mecanique_V18_1.md` | Nouveau | Architecture mécanique systémique |
| `renovation_V18_1.md` | Nouveau | Rénovation (acoustique, nettoyage, anti-corrosion, visserie) |
| `confort_V18_1.md` | Nouveau | Confort habitacle |
| `elec_V18_1_V1.md` | Mis à jour | Câblage V1 avec précisions session du soir |
| `GUIDE_INTEGRATION_V18_1.md` | Nouveau | Procédure d'intégration repository |
| `AUDIT_REPOSITORY_V18_1.md` | Nouveau | Tour complet du repository + actions |

---

## 6 — PRÉPARATION SALON INFINEON NUREMBERG

Voir détail dans `Architecture_Electrique_Electronique_V2.md` §14.

**Documents à imprimer en couleur A4** :
- AUDIT_PROJET_MODUS_V18_1.md
- Architecture_Electrique_Electronique_V2.md
- elec_V18_1_V1.md
- Photos véhicule

**Questions prioritaires à poser** :

| Module | Question |
|---|---|
| Module 1 BMS | MOSFETs OptiMOS pour BMS LiFePO4 8Ah 12V — référence ? |
| Module 2 Stockage | Alternative LTC4359 chez Infineon ? Driver gate pour pic 300A ? |
| Module 3 iBSG | MOSFETs CoolSiC 100V 200A pour onduleur 48V triphasé ? Référence design BSG 48V ? |
| Module 4 Signalisation | Drivers MT type VN5050AJ ou équivalent ? |
| Module 5 Capteurs | Capteurs MEMS Infineon vs Bosch ? Drivers LIN/CAN ? |
| Module 6 Corrosion | NFC reader PN7160 ou alternative Infineon ? |
| MCU central | AURIX TC275 vs TC375 ? Échantillonnage possible ? |

---

## 7 — STATUT ACTUEL (1er juin 2026)

### Avancement

- ✅ Audit V18.1 réalisé avec stratégie V0/V1/V2
- ✅ TL4B043 payée et reçue
- ✅ Powerflex ×6 payés et reçus
- ✅ Outillage de base acquis
- ✅ Architecture V1 minimaliste définie (caisson sous coffre)
- ✅ Architecture V2 documentée pour déploiement futur
- ✅ Documents complémentaires créés : mecanique, renovation, confort
- 🟡 Paniers V1 en cours (13 fournisseurs)
- 🟡 Vérifications physiques en attente (emplacement roue secours, supports étrier)
- ⬜ Exécution V0/V1

### Prochaines étapes

1. **Salon Infineon Nuremberg** (semaine du 7 juin) — contacts pour V2
2. Corrections paniers V18.1 :
   - Retraits BDA604+BDA605
   - RoyPow → EverExceed
   - Ajouts composants V1 électronique + hub USB + tirages V2
3. Mesure emplacement roue de secours
4. Location box garage
5. Démarrage V0 (infrastructure caisson + tirages câbles + anti-corrosion + insonorisation)

---

*AUDIT V18.1 — 1er juin 2026*
*Stratégie V0/V1/V2 + Phase 2 actée — V0 infrastructure prioritaire pendant démontage*
