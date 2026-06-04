# ARCHITECTURE ÉLECTRIQUE & ÉLECTRONIQUE V2 — MODUS JP0F
## Architecture iBSG 48V — Déploiement Q1-Q2 2027

**Véhicule :** VF1JP0F0H43308282 — Renault Modus 1.5 dCi K9K766 → K9K896 (Phase 2)
**Architecture :** 6 PCB modulaires + bus 48V dédié iBSG + bus 12V conservé
**Cible fiabilité :** 300 000 km — environnement automotive AEC-Q100
**Date :** 31 mai 2026 — document de référence pour V2 (post V1 fonctionnelle)

---

## 0 — POSITIONNEMENT V2

Ce document décrit l'architecture **complète après évolution V1 → V2**. La V1 fait rouler la Modus avec une électronique passive simple (voir `elec_V18_V1.md`). La V2 ajoute :

- iBSG Valeo 48V 12 kW (remplace alternateur + démarreur)
- Bus 48V dédié avec pack LTO + supercondos
- DC/DC bidirectionnel 12V ↔ 48V
- PCB custom pour les 6 sous-systèmes
- MCU central AURIX TC375
- Signalisation MT modulée
- Surveillance corrosion RFID
- Tableau de bord Mega Drive (phase finale)

**Objectif** : transformer la Modus en mild-hybrid 48V avec performances et économies significatives, tout en gardant la fiabilité d'une voiture stock.

---

## 1 — VUE D'ENSEMBLE ARCHITECTURE V2

### Les 6 modules + MCU central

| # | Module | Fonction | Position | Phase déploiement |
|---|---|---|---|---|
| 0 | **MCU central AURIX TC375** | Coordination 6 modules | Caisson AR | V2.0 |
| 1 | **Batterie & BMS OptiMOS** | LiFePO4 12V 8Ah + monitoring cellule | Caisson AR (héritage V1) | V2.0 |
| 2 | **Stockage 48V (LTO + supercondos)** | Pack LTO 7 kg + banc condos 3,5 kg | Caisson AR | V2.0 |
| 3 | **iBSG Valeo + onduleur SiC** | Cranking + générateur + boost 12 kW | Compartiment moteur | V2.0 |
| 4 | **Signalisation MT** | Feux modulés par décélération | Arrière véhicule | V2.2 |
| 5 | **Capteurs distribués** | Réseau CAN/LIN environnementaux | Distribué (cabine + moteur + dessous) | V2.1 |
| 6 | **Contrôle corrosion** | Tags RFID NAC1080 | Châssis | V2.3 |

### Hiérarchie des bus

```
        ┌──────────────────────────────────────────┐
        │       MCU CENTRAL (AURIX TC375)          │
        │   Coordination 6 sous-systèmes           │
        └──────┬──────────────────┬────────────────┘
               │ CAN-C 500 kbps    │ LIN 20 kbps
               │ (modules critiques)│ (capteurs lents)
               │                    │
   ┌───────────┼────────┬─────────┐ │
   │           │        │         │ │
[Module 1] [Module 2] [Module 3] [Module 4]
Batterie   Stockage   iBSG       Signalisation
12V        48V        Valeo      MT
                                       │
                                  [Module 5]
                                  Capteurs distribués
                                       │
                                  [Module 6]
                                  Corrosion RFID (NFC bridge)
```

### Stratégie d'isolation et sécurité

- **Isolation galvanique** entre bus 12V et bus 48V (via DC/DC isolé)
- **Fail-safe matériel** sur fonctions critiques (thermique caisson, ASC iBSG)
- **Redondance capteurs** : DS18B20 + KSD301 pour T°, INA228 + diviseur ADC pour tension
- **Watchdog hardware** sur tous les MCU (AURIX, CH32V203 satellites)
- **Sectionnement par fusibles** à chaque interface entre modules

---

## 2 — MODULE 1 : BATTERIE & BMS LiFePO4 12V

### Fonction

Fournir l'énergie principale au bus 12V véhicule (ECU, capteurs, éclairage, EPAS) de manière fiable et durable. Migration du BMS basic V1 vers un BMS custom utilisant les MOSFETs SiC Infineon OptiMOS.

### Composants V2

| Composant | Référence cible | Rôle | Évolution V1→V2 |
|---|---|---|---|
| Cellules LiFePO4 | EverExceed 12V 8Ah 96Wh (héritage V1) | Stockage énergie | Conservé |
| BMS MOSFETs charge | Infineon OptiMOS BSC014N04LS ×2 | Coupure charge à 14,4V | Nouveau V2 (remplace BMS interne) |
| BMS MOSFETs décharge | Infineon OptiMOS BSC014N04LS ×2 | Coupure décharge à 10V | Nouveau V2 |
| Équilibrage actif | 4× résistances 1Ω 0,5W + commutateur MCU | Balancing cellule | Nouveau V2 |
| MCU BMS | CH32V203C8T6 (RISC-V) | Lecture cellule, équilibrage, CAN | Nouveau V2 |
| Capteur courant | INA228 (20-bit ADC) | Mesure I bus 12V | Nouveau V2 |
| Capteur température | DS18B20 ×4 | T° par cellule + T° caisson | Conservé V1 |
| Transcepteur CAN | TJA1051 | Communication bus principal | Nouveau V2 |

### Interfaces

| Interface | Direction | Type | Détail |
|---|---|---|---|
| Bus +12V principal | Sortie | Puissance | Fusible interne 30A, kill switch externe |
| CAN-C | Bidirectionnel | Communication | Trames SOC, V, I, T° toutes 100 ms |
| Chauffage USB | Entrée | Auxiliaire | Active PTC si T° < 5°C ET USB connecté |
| Programmation BMS | Maintenance | SWD/JTAG | Connecteur 6 pins interne |

### Sécurités matérielles

- **Fail-safe haute tension** : si V_bus > 15V (alternateur défaillant), BMS coupe charge
- **Fail-safe basse tension** : si V_cell < 2,8V, BMS coupe décharge
- **Fail-safe surchauffe cellule** : coupure totale si T° > 55°C sur une cellule
- **Recharge depuis bus 48V** : via DC/DC bidirectionnel (priorité au courant maintenu)

---

## 3 — MODULE 2 : STOCKAGE 48V (LTO + SUPERCONDOS)

### Fonction

Fournir l'énergie au bus 48V pour l'iBSG : pics instantanés (cranking, boost) via supercondos, énergie soutenue via pack LTO. Récupération d'énergie en régen vers les deux sources selon la cinétique.

### Pack LTO 10Ah 20S

| Paramètre | Valeur |
|---|---|
| Tension nominale | 46 V (54V max, 36V min utile) |
| Capacité | 10 Ah |
| Énergie totale | 460 Wh = 1 656 kJ |
| Énergie utile (14% DoD) | 220 kJ par cycle |
| Cellules | 20× LTO 10Ah Tycorun ou Liantian |
| Masse | 7 kg |
| Volume | 4-5 L |
| Cycles attendus | 40 000+ cycles |
| BMS | JK 20S 100A configurable LTO (V2.0), évolution custom OptiMOS plus tard |

### Banc supercondos 48V

| Paramètre | Valeur |
|---|---|
| Configuration | 20× cellules 2,7V 1500F en série |
| Tension max | 54V |
| Capacité | 75F équivalent banc |
| Énergie utile (54V → 36V) | 47 kJ |
| IR | < 10 mΩ |
| Rôle | Absorption pics instantanés, support cranking |
| Masse | 3,5 kg |

### Architecture combinée

```
                BUS +48V (dédié iBSG)
                      │
        ┌─────────────┼────────────┐
        │             │            │
   [PACK LTO]   [SUPERCONDOS]  [iBSG Valeo]
   20S × 10Ah   20× 1500F        12 kW
   7 kg         3,5 kg
   IR 40 mΩ     IR < 10 mΩ
   1656 kJ      47 kJ utile
   Énergie      Pics instantanés
   soutenue
```

**Stratégie de répartition** :
- Pic court (cranking, 1-2s) : supercondos fournissent 80% du courant
- Boost 5-10s : supercondos puis pack LTO
- Boost prolongé (>10s) : pack LTO majoritairement, supercondos rechargés en parallèle par iBSG
- Régen : supercondos absorbent en priorité (impédance plus faible), surplus vers pack LTO

### Composants

| Composant | Référence cible | Rôle | Prix estimé |
|---|---|---|---|
| Cellules LTO 10Ah | Tycorun ou Liantian | Stockage soutenue | 615-825 € |
| BMS JK 20S 100A | AliExpress | Gestion 20 cellules LTO | 100 € |
| Banc supercondos | 20× Maxwell K2 2,7V 1500F | Pics instantanés | 250-400 € |
| Balancing supercondos | Module passif 20 cellules | Équilibrage | 30-50 € |
| Diode idéale 48V | LTC4359 (jusqu'à 80V) | Aiguillage | 8-12 € |
| MOSFET 100V/200A | Infineon CoolSiC IMW65R027M1 | Élément actif | 20-40 € |
| Pré-charge 48V | NTC + relais Kilovac LEV200 | Limitation inrush | 50-80 € |
| Fusible 250A 80V | Eaton Bussmann megafuse | Protection bus 48V | 25-40 € |
| MCU local | CH32V203 (intégré au BMS) | Télémétrie banc | 5 € |
| Capteurs T° | DS18B20 ×4 | Monitoring banc | 4 € |
| Câblage 25-35mm² | Cuivre étamé HV | Sortie vers iBSG | 50-80 € |
| Boîtier IP65 | Custom alu | Protection caisson AR | 80-150 € |
| **TOTAL Module 2** | | | **1 237-1 786 €** |

---

## 4 — MODULE 3 : iBSG VALEO + ONDULEUR SiC

### Fonction

L'iBSG Valeo 48V 12 kW remplace l'alternateur et le démarreur stock. Il assure cranking, génération en cruise, boost en accélération, et régénération en décélération.

### Spécifications cible

| Paramètre | Valeur |
|---|---|
| Puissance pic | 12 kW |
| Puissance continue | 8,4 kW (limitée par pack LTO 7 kg pour stabilité tension) |
| Couple au vilebrequin | 45 Nm pic |
| Tension bus | 48V nominal (36-54V plage) |
| Rendement | 85-90% |

### Sourcing iBSG Valeo

| Source | Modèle | Prix typique | Disponibilité |
|---|---|---|---|
| Mercedes Sprinter eDrive 48V | iBSG utilitaire | 800-1200 € | Bon en casse (utilitaire courant) |
| Mercedes Classe E 220d MHEV (W213) | iBSG (M254/M256 base) | 1000-1500 € | Moyen |
| Renault Captur E-Tech / Arkana | iBSG2 Hybrid Assist | 1200-1800 € | Faible (rare en casse) |

**Recommandation** : Mercedes Sprinter eDrive 48V pour le rapport qualité/prix/disponibilité.

### Récupération en casse

| Élément | Récupération | Réutilisation |
|---|---|---|
| iBSG machine seule | OUI | Cœur du projet |
| Contrôleur Valeo intégré | OUI mais inutilisable (crypto) | À jeter |
| Capteur position rotor | OUI, intégré à l'iBSG | Réutilisable directement |
| Faisceau électrique 48V | OUI | Étude du brochage |
| Bracket de montage | OUI mais incompatible K9K | Référence dimensionnelle |
| OAD (Overrunning Decoupler) | OUI mais pas adapté K9K | Récupération pour pièces |
| Tendeur hydraulique | OUI mais spécifique | Référence + achat neuf |

### Adaptation mécanique K9K

| Poste | Coût estimé |
|---|---|
| Bracket d'adaptation K9K (custom CNC) | 300-600 € |
| OAD compatible (INA ou Litens) | 80-180 € |
| Tendeur hydraulique neuf | 80-200 € |
| Courroie aramide 6PK | 30-60 € |
| Visserie inox + colle frein | 30-50 € |
| Ajustements et tests | 50-100 € |
| **TOTAL adaptation mécanique** | **570-1 190 €** |

### Onduleur SiC custom

| Composant | Référence cible | Rôle | Prix |
|---|---|---|---|
| MOSFETs SiC 100V 200A | Infineon CoolSiC IMW65R027M1 ×6 | Pont triphasé bidirectionnel | 80-150 € |
| Driver gate isolé | Infineon 1ED Compact ×6 | Pilotage 6 MOSFETs | 30-60 € |
| MCU contrôle FOC | Infineon AURIX TC275 ou STM32G474 | FOC haute fréquence 20 kHz | 20-100 € |
| Capteurs courant phase | LEM HASS-50S ×3 ou Allegro ACS758 | Mesure I phases pour FOC | 60-120 € |
| Convertisseur RDC | AD2S1210 (si résolveur) | Position rotor | 30 € |
| Condensateurs DC-link | 470µF 100V × plusieurs | Filtrage bus DC | 30-80 € |
| Boîtier IP65 dissipateur | Alu fraisé avec ailettes | Refroidissement passif/actif | 80-150 € |
| Connecteurs HV | Anderson SB350 ou Amphenol HVS | Connexions puissance | 30-60 € |
| **TOTAL onduleur custom** | | | **360-750 €** |

### Coût total Module 3

| Catégorie | Montant |
|---|---|
| iBSG Valeo (casse) | 800-1500 € |
| Adaptation mécanique | 570-1190 € |
| Onduleur SiC custom | 360-750 € |
| **TOTAL Module 3** | **1 730-3 440 €** |

---

## 5 — DC/DC BIDIRECTIONNEL 12V ↔ 48V

### Fonction

Couplage entre bus 12V et bus 48V. Principalement en mode 48V → 12V pour alimenter le bus accessoires depuis l'iBSG en marche. Mode 12V → 48V uniquement pour pré-charge initiale ou backup.

### Spécifications

| Paramètre | Valeur |
|---|---|
| Tension entrée | 9-15V (côté 12V) et 36-54V (côté 48V) |
| Puissance continue | 500W |
| Direction | Bidirectionnel |
| Isolation galvanique | Recommandée |
| Régulation | Programmable via CAN |

### Composants

| Option | Coût | Verdict |
|---|---|---|
| Custom design Infineon CoolSiC + LLC | 200-400 € composants | Cohérent angle Infineon |
| DEM-12-48V VVKB 500W bidirectionnel | 200-300 € | Turnkey rapide |
| Mean Well RSP-2400-48 + back-to-back | 300-450 € | Industriel robuste |

**Recommandation** : Custom design Infineon avec composants CoolSiC. Cohérent avec ton angle salon Nuremberg.

---

## 6 — MODULE 4 : SIGNALISATION MT

### Fonction

Feux arrière (stop, position, clignotants) modulés en intensité par la décélération réelle du véhicule (lue depuis IMU du Module 5). Le feu stop devient une signalisation graduée pour les suiveurs.

### Composants

| Composant | Référence cible | Rôle | Prix |
|---|---|---|---|
| LEDs HP | Cree XHP70.2 ×6 | Source lumière feu stop/position | 60-100 € |
| Drivers LED constant-current | Mean Well LDD-700H ×4 | Pilotage MT 48V | 40-80 € |
| Capteur décélération | IMU LSM6DSOX (depuis Module 5 via CAN) | Lecture accélération | 0 € (mutualisé) |
| MCU pilotage | CH32V203 | Modulation PWM des drivers | 5 € |
| Transcepteur CAN | TJA1051 | Réception commandes stop + IMU | 3 € |
| Connecteurs HV automotive | Rosenberger ou TE | Étanchéité + sécurité | 30-50 € |
| Boîtier IP65 | Custom | Protection | 30-50 € |
| **Option HT future** (non peuplée V2.0) | Transformateur flyback 48V→HT | Évolution composants HT | 100-200 € (en option) |
| **TOTAL Module 4** | | | **170-300 €** |

### Logique de modulation

```
Décélération mesurée (m/s²)   →   Intensité feu stop (%)
   0 à 1 m/s² (frein doux)    →   30%
   1 à 3 m/s² (frein normal)  →   60%
   3 à 6 m/s² (frein urgent)  →   100%
   > 6 m/s² (frein d'urgence) →   100% + clignotement 4 Hz (ESS)
```

### Architecture HT prévue

Le PCB est conçu avec emplacement pour transformateur flyback HT 48V → 300V (non peuplé en V2.0). Permet évolution future vers composants à émission de champ sous vide ou moteur HT si disponibilité commerciale dans 5-10 ans.

---

## 7 — MODULE 5 : CAPTEURS DISTRIBUÉS

### Fonction

Réseau de PCB capteur miniatures (3×3 cm) déployés en plusieurs points du véhicule, communiquant via bus LIN (capteurs lents) ou CAN (capteurs critiques) avec le MCU central.

### Composants par PCB capteur

| Composant | Référence | Rôle | Prix |
|---|---|---|---|
| MCU | CH32V203C8T6 (RISC-V) | Lecture + communication | 1-2 € |
| Transcepteur LIN | TJA1021 | Bus série bas débit | 2 € |
| Transcepteur CAN | TJA1050 | Bus haut débit | 2 € |
| Régulateur 3,3V | TPS7A2033 | Alim MCU + capteurs | 1 € |
| Capteur (selon position) | Voir cartographie | Mesure spécifique | Variable |
| Connecteur véhicule | JST-XH 4 pins étanche | +12V, GND, signal bus | 1-2 € |

### Cartographie des capteurs déployés

| Position | Capteurs | Bus | Données |
|---|---|---|---|
| Cabine tableau de bord | BME688 + AGS02MA + SGP40 | LIN | T°, HR, pression, qualité air |
| Cabine sous siège | LSM6DSOX | CAN | Accéléromètre + gyro 6 axes |
| Baie moteur turbo | BME688 + capteur T° K-type | CAN | T° admission, pression, T° collecteur |
| Baie moteur alternateur (V1) / iBSG (V2) | INA228 + DS18B20 | CAN | I/V, T° |
| Baie moteur bloc | DS18B20 ×2 | LIN | T° culasse, T° huile |
| Dessous proche échappement | BME688 + DS18B20 | LIN | T° + qualité air (post-FAP) |
| Coffre caisson batterie 12V | BME688 + DS18B20 ×2 | CAN | T°, HR caisson |
| Caisson stockage 48V | BME688 + DS18B20 ×4 | CAN | Monitoring spécifique pack LTO |
| Coffre proche réservoir | SGP40 | LIN | Détection vapeurs carburant |

**Total** : 8-9 PCB capteurs distribués + capteurs ad-hoc selon évolution.

### Coût

| Catégorie | Montant |
|---|---|
| 9× PCB capteurs (fabrication + assemblage) | 120-180 € |
| Composants capteurs (BME688, AGS02MA, etc.) | 150-220 € |
| Connectique + câblage CAN/LIN | 50-100 € |
| **TOTAL Module 5** | **320-500 €** |

---

## 8 — MODULE 6 : CONTRÔLE CORROSION RFID

### Fonction

Tags RFID passifs avec mesure de potentiel électrochimique collés sur les points critiques du châssis. Détection de corrosion en cours avant qu'elle ne soit visible.

### Composants

| Composant | Référence cible | Rôle | Prix |
|---|---|---|---|
| Tags RFID passifs | NeoCortec NAC1080 ×24 | Mesure potentiel + ID unique | 240-360 € |
| Bridge NFC | PN7160 (NXP) | Lecture périodique | 30 € |
| MCU bridge | CH32V203 | Coordination + CAN | 5 € |
| Antennes RFID flex | Custom 13,56 MHz | Couplage tags | 80-120 € |
| **TOTAL Module 6** | | | **355-515 €** |

### Stratégie de placement (24 tags)

| Zone | Nombre |
|---|---|
| Passages de roue AV ×2 | 4 |
| Bas de portes ×4 | 8 |
| Longerons sous voiture ×2 | 4 |
| Supports moteur ×4 | 4 |
| Bas de pare-chocs AV+AR | 2 |
| Coffre AR (fond) | 1 |
| Cellule de référence externe | 1 |
| **TOTAL** | **24 tags** |

---

## 9 — MCU CENTRAL AURIX TC375

### Rôle

Hub de coordination des 6 sous-systèmes. Reçoit les données de chaque module via CAN/LIN, applique la logique métier (boost timing, alertes, modulation signalisation), historise les données, communique avec l'utilisateur via BLE et avec le tableau de bord Mega Drive (phase finale).

### Composants

| Composant | Référence cible | Prix |
|---|---|---|
| MCU | Infineon AURIX TC375 ou TC275 | 30-80 € |
| Alimentation isolée | Custom buck-boost | 30-50 € |
| Mémoire SD | µSD 16-32 GB | 10 € |
| Module BLE | ESP32-S3 dédié (en plus de l'ESP32 caisson AR) | 10 € |
| PCB 6 couches | Fabrication JLCPCB ou PCBWay | 100-150 € |
| Boîtier IP65 | Custom | 50-100 € |
| **TOTAL MCU central** | | **230-400 €** |

### Fonctions logicielles

- Surveillance temps réel des 6 modules
- Détection d'anomalies multi-capteurs
- **Gestion du mode boost iBSG (timing, contraintes, sécurité)**
- **Calcul DoD prévisionnel + témoin rouge/vert**
- Modulation signalisation MT en fonction IMU
- Historisation sur SD card embarquée
- Communication BLE smartphone (app compagnon)
- Communication tableau de bord Mega Drive (phase finale)
- Stratégie de gestion énergétique F1-inspired

---

## 10 — INTERFACE UTILISATEUR

### Témoin rouge/vert + bouton volant

**Témoin** :
- LED bicolore au tableau de bord (V2.0)
- Évolution OLED 1,3" couleur (V2.1)
- Évolution Mega Drive tableau de bord complet (V2.4)

**Logique** :
- VERT : boost autorisé (DoD prévisionnel < 10%, T° cellules OK)
- ROUGE : boost déconseillé (au-delà du DoD cible) mais conducteur peut forcer
- Monitoring DoD réel en temps réel par ESP32

**Bouton volant** :
- Bouton-poussoir illuminé sous le logo Renault central
- Appui court : enclenche/désenclenche le mode boost
- Appui long (>2s) : reset système
- LED interne synchronisée avec témoin tableau de bord
- Câblage via faisceau volant existant + contacteur tournant

---

## 11 — BUDGET ESTIMATIF V2

| Module | Coût |
|---|---|
| Module 1 BMS LiFePO4 OptiMOS (évolution V1) | 220 € |
| Module 2 Stockage 48V (LTO + supercondos) | 1237-1786 € |
| Module 3 iBSG + adaptation + onduleur | 1730-3440 € |
| Module 4 Signalisation MT | 170-300 € |
| Module 5 Capteurs distribués | 320-500 € |
| Module 6 Corrosion RFID | 355-515 € |
| MCU central AURIX | 230-400 € |
| DC/DC bidirectionnel 500W | 200-400 € |
| Câblage 48V + connectique HV | 200-400 € |
| **TOTAL V2** | **4 662-7 961 €** |

---

## 12 — COMPATIBILITÉ K9K896 PHASE 2

L'architecture V2 est conçue pour être **transférable à 95% sur K9K896** :

**Compatible direct** :
- Pack LTO et supercondos (bus 48V indépendant du moteur)
- iBSG (même architecture, ajustement bracket)
- DC/DC bidirectionnel
- Tous les capteurs distribués
- MCU central
- Signalisation MT

**Ajustements requis** :
- Mapping CAN ECU Bosch EDC17C84 (vs Siemens SID303 K9K766) : effort logiciel
- Vérification dimensionnelle bracket iBSG (probable compatibilité directe)
- Recalibration seuils de boost (TPS, RPM thresholds) pour nouvelle courbe couple
- Tests progressifs avant validation

**Gain Phase 2 avec iBSG conservé** :
- K9K896 stock : 110 ch / 240 Nm
- + reprog stage 2 (gros turbo) : 145-160 ch / 260 Nm bridé boîte
- + iBSG boost : 260 Nm dispo dès 1200 tr/min (vs 1700 sans iBSG)
- 0-100 km/h estimé : 7,5-8,5 s

---

## 13 — ROADMAP V2

| Phase | Période | Contenu |
|---|---|---|
| V2.0 | Q1-Q2 2027 | iBSG + onduleur + pack LTO + supercondos + DC/DC + BMS OptiMOS |
| V2.1 | Q3 2027 | Capteurs distribués + OLED tableau de bord |
| V2.2 | Q4 2027 | Signalisation MT modulée |
| V2.3 | Q1 2028 | Surveillance corrosion RFID |
| V2.4 | Q2-Q3 2028 | Tableau de bord Mega Drive |

---

## 14 — PRÉPARATION SALON INFINEON NUREMBERG

### Questions techniques prioritaires

**Module 1 BMS**
- OptiMOS recommandé pour BMS LiFePO4 8Ah 12V
- INA228 vs alternatives Infineon

**Module 2 Stockage 48V**
- LTC4359 alternative chez Infineon
- Driver gate pour MOSFET 300A pic

**Module 3 iBSG**
- MOSFETs CoolSiC 100V 200A pour onduleur 48V triphasé
- Référence design BSG 48V chez Infineon
- AURIX TC275 vs TC375 pour pilotage FOC

**Module 4 Signalisation**
- Drivers MT type VN5050AJ ou équivalent récent
- Composants à émission sous vide (information)

**Module 5 Capteurs**
- Capteurs MEMS Infineon en complément Bosch
- Drivers LIN/CAN Infineon vs NXP

**Module 6 Corrosion**
- NFC reader automotive PN7160 ou alternative Infineon
- Tags RFID NAC1080 ou alternative

**MCU central**
- AURIX TC375 vs TC275 différence pratique
- Échantillonnage possible
- Stack logiciel hobbyiste

### Documents à apporter

- Architecture_Electrique_Electronique_V2.md (1 ex. couleur A4)
- elec_V18_V1.md (état actuel V1)
- AUDIT_PROJET_MODUS_V18.md
- BOM ciblée par module V2

---

*ARCHITECTURE V2 — 31 mai 2026*
*Document de référence pour déploiement Q1-Q2 2027 (post V1 fonctionnelle)*
*Architecture iBSG 48V avec 6 modules custom et MCU central AURIX*
