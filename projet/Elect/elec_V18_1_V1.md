# CÂBLAGE ÉLECTRIQUE V18.1 V1 — POUR FAIRE ROULER LA MODUS

**Véhicule :** VF1JP0F0H43308282 — Modus 1.5 dCi
> Ce fichier remplace les anciens "Elec V15/V16/V17/V18", "Cablage_electrique V5".
> Pour l'architecture V2 (iBSG 48V + 6 modules custom), voir `Architecture_Electrique_Electronique_V2.md`.
> V18.1 intègre les précisions session du soir : caisson sous coffre, démarreur stock, hub USB, mode rescue séquentiel, tirages V0 préparés, masses châssis supprimées Phase 0.

---

## 0 — VISION D'ENSEMBLE V1

Architecture passive double source 12V avec mode rescue intelligent :

- **Maxwell 16V 100F** pour les pics de cranking (200-400A instantané)
- **EverExceed LiFePO4 8Ah** pour la veille et le bus accessoires
- ESP32 télémétrie au caisson sous coffre (autonome via cellule 18650)
- Sous-circuit avant LTC4359 (diode idéale + pré-charge NTC)
- **Hub USB interne 1→3 voies** (charge 18650 / chauffage PTC / MT3608 rescue)
- **Port USB conducteur** (console centrale) pour brancher powerbank
- Mode rescue séquentiel intelligent
- Alternateur K9K stock (charbons + bagues neufs)
- **Démarreur Modus stock reconditionné** (pas Clio 3 GT)
- Topologie étoile depuis caisson sous coffre (pas de masses châssis)

---

## 1 — CAISSON SOUS COFFRE (emplacement roue de secours)

### Pourquoi cet emplacement

| Critère | Sous banquette AR | Sous coffre (roue secours) |
|---|---|---|
| Volume disponible | 15-25 L | **45-65 L** ✅ |
| Centre de gravité | Bas | Très bas ✅ |
| Accès maintenance | Moyen (banquette) | Facile (lever plancher) ✅ |
| Isolation thermique | À construire | Logement déjà fermé ✅ |
| Sécurité crash AR | Bonne | Excellente ✅ |
| Gêne passagers AR | Possible | Aucune ✅ |
| Modification | Caisson custom | Plancher coffre adapté |
| Roue de secours | Conservée | Supprimée → kit anti-crevaison |

### Dimensions à vérifier physiquement

À mesurer dès accès véhicule :
- Diamètre intérieur (haut et bas)
- Profondeur libre sous plancher
- Épaisseur plancher au-dessus
- Présence d'éléments structuraux à contourner
- Accès depuis le coffre (charnière du plancher)

Estimations Modus II : diamètre 60-65 cm, profondeur 15-20 cm, volume 45-65 L.

### Volume occupé V1 + V2

| Composant | Phase | Volume |
|---|---|---|
| EverExceed LiFePO4 8Ah | V1 | 1 L |
| Banc Maxwell 16V 100F | V1 | 3-5 L |
| ESP32 + Hub USB + accessoires | V1 | 1-2 L |
| Pré-charge + LTC4359 | V1 | 1 L |
| Pack LTO 10Ah 20S | V2 | 4-5 L |
| Banc supercondos 48V (20× 1500F) | V2 | 3-4 L |
| Onduleur SiC custom | V2 | 2-3 L |
| BMS LTO + DC/DC + connectique | V2 | 3-5 L |
| Isolation thermique + mousse + espace ventilation | V0 | 5-10 L |
| **TOTAL V1+V2** | | **23-36 L** |

**Marge** : 9-42 L dans un caisson de 45-65 L. Largement OK.

### Caisson chauffé en V0 (infrastructure de base)

Construit avant tout autre travail électrique. Permet d'avoir l'infrastructure prête quand on installera la partie active.

**Structure** :
- Châssis bois MDF 18mm + plaque alu blindage interne
- Mousse PE thermique 20mm en parois
- Plancher renforcé pour supporter 30 kg (V2)
- Mise à l'air calibrée (évacuation dégazage anormal)
- Étanchéité IP65 (joint EPDM périphérie)
- Fixations M6 inox + rondelles éventail

**Système thermique passif** :
- KSD301 NC 15°C en série avec PTC + fusible thermique 60°C (fail-OFF)
- KSD301 NO 40°C + ventilateur PC 12V (fail-ON)
- Chauffage PTC commandé par MOSFET via ESP32

**Composants V0 caisson** :

| Composant | Quantité | Prix |
|---|---|---|
| Bois MDF 18mm | 1 panneau | 15-25 € |
| Plaque alu 1mm | 0,5 m² | 15-20 € |
| Mousse PE 20mm | 0,5 m² | 10-15 € |
| Joint EPDM périphérie | 2 m | 8-12 € |
| Vis inox M6 + rondelles éventail | Kit | 10-15 € |
| KSD301 NC 15°C | 1 | 3-5 € |
| KSD301 NO 40°C | 1 | 3-5 € |
| Ventilateur PC 12V 80mm | 1 | 8-12 € |
| Chauffage PTC 12V 20W | 1 | 8-12 € |
| Fusible thermique 60°C | 1 | 2-3 € |
| Mise à l'air calibrée | 1 | 5-10 € |
| Connectique étanchéité | Kit | 10-20 € |
| **TOTAL caisson V0** | | **97-154 €** |

---

## 2 — TIRAGES CÂBLES V0 (V1 + V2 préparés)

Pendant qu'on démonte tout pour l'anti-corrosion et l'insonorisation, on tire tous les câbles V1+V2 et on les laisse en attente, gainés et marqués.

### Tirages V1 (à connecter immédiatement)

| Câble | Section | Trajet | Longueur estimée |
|---|---|---|---|
| Cranking 35-50 mm² | 35-50 mm² | Caisson sous coffre → démarreur baie moteur | 4-5 m |
| Alternateur charge | 16 mm² | Alternateur → bus 12V caisson | 4-5 m |
| Accessoires 12V | 6 mm² | Caisson → boîte fusibles habitacle | 3-4 m |
| Retours masse dédiés (×5-10) | 1,5-2,5 mm² | Caisson → consommateurs (ECU, EPAS, éclairage, etc.) | 3-5 m × 5-10 |
| USB conducteur | Câble USB blindé | Caisson → console centrale | 3-4 m |
| Faisceau capteurs ESP32 | I2C + 1-Wire | Caisson interne | 1-2 m |
| Câble masse principal (transitoire) | 35 mm² | Caisson → point de masse châssis (sera retiré après finitions) | 1 m |

### Tirages V2 (à laisser en attente, gainés et marqués)

| Câble | Section/Type | Trajet | Longueur estimée |
|---|---|---|---|
| Bus 48V positif | 25-35 mm² | Caisson → emplacement iBSG baie moteur | 4-5 m |
| Bus 48V négatif | 25-35 mm² | Caisson → emplacement iBSG baie moteur | 4-5 m |
| CAN-C blindé | Paire torsadée 120Ω blindée | Caisson → 8 emplacements PCB capteurs distribués | 8 × 2-4 m |
| LIN | Paire torsadée simple | Caisson → emplacements capteurs lents | 4-6 m |
| Signalisation MT 48V | Paire blindée HV | Caisson → feux arrière | 3-4 m |
| RFID corrosion 13,56 MHz | Coaxial 50Ω | Caisson → 24 points châssis | 24 × 1-3 m |
| Réserve évolution | 3-4 paires torsadées | Caisson → endroits stratégiques | 5-10 m |

### Marquage et gainage

- Chaque câble V2 en attente : gaine annelée Ø10-25 selon section
- Extrémités scellées (thermo) en attendant connexion
- Étiquettes thermorétractables aux deux extrémités : type + destination + section
- Boucle de mou 30-50 cm de chaque côté pour ajustements ultérieurs

### Budget tirages V0

| Catégorie | Estimation |
|---|---|
| Câble cuivre étamé V1 (cranking, alternateur, accessoires) | 80-120 € |
| Câble cuivre étamé V2 bus 48V (25-35 mm²) | 60-100 € |
| Paires torsadées CAN-C blindées | 30-50 € |
| Câbles coaxiaux 50Ω RFID | 40-60 € |
| Gaines annelées assorties | 30-50 € |
| Cosses, connecteurs, étiquettes | 30-60 € |
| **TOTAL tirages V0** | **270-440 €** |

---

## 3 — SUPPRESSION DES MASSES CHÂSSIS (Phase 0)

### Pourquoi cette décision

Les masses châssis sont historiquement la cause N°1 des problèmes électriques sur véhicules vieillissants :
- Corrosion entre boulon et tôle
- Boucles galvaniques entre points de masse différents
- Résistance variable selon humidité
- Difficile à diagnostiquer
- Vibrations qui desserrent les boulons

**Solution V18.1** : topologie étoile complète depuis le caisson sous coffre. Tous les retours sont des fils dédiés qui reviennent au point de masse central du caisson.

### Topologie cible

```
       CAISSON SOUS COFFRE
              │
              │ POINT DE MASSE CENTRAL (bus en cuivre 50mm²)
              │
              ├── Retour démarreur (35 mm²)
              ├── Retour alternateur (16 mm²)
              ├── Retour ECU (2,5 mm²)
              ├── Retour EPAS (6 mm²)
              ├── Retour éclairage AV (2,5 mm²)
              ├── Retour éclairage AR (2,5 mm²)
              ├── Retour accessoires habitacle (2,5 mm²)
              ├── Retour pompe carburant (2,5 mm²)
              ├── Retour ventilateur radiateur (4 mm²)
              ├── Retour ventilation habitacle (2,5 mm²)
              ├── Retour airbags (1,5 mm²)
              └── Retour capteurs (1,5 mm²)
```

### Exécution en Phase 0

Pendant le démontage complet pour l'anti-corrosion et l'insonorisation :

1. **Identifier toutes les masses châssis** existantes (boulons à cosse plate fixés au châssis)
2. **Photographier** chaque emplacement avant démontage (référence)
3. **Tracer chaque consommateur** jusqu'à son retour actuel
4. **Tirer un fil dédié** depuis chaque consommateur jusqu'au caisson
5. **Retirer les boulons de masse châssis** et boucher les trous (mastic + rondelle inox)
6. **Vérifier la continuité** caisson ↔ consommateur avec ohmmètre (< 100 mΩ)

### Exceptions (masses châssis conservées)

Quelques cas où une masse châssis reste plus pratique :
- Démarreur (très forte intensité, proximité immédiate) — débattre selon décision finale
- Capteurs de roue ABS (proximité immédiate)

Toutes les autres masses sont supprimées.

### Budget suppression masses

Coût marginal car la majeure partie est compensée par les tirages V0 déjà prévus :
- Câbles supplémentaires (compté dans tirages V0)
- Mastic + rondelles inox pour boucher anciens trous : 15-25 €
- Diélectromètre pour vérifications : 30-50 € (achat unique)

---

## 4 — ARCHITECTURE CAISSON SOUS COFFRE

### Schéma détaillé

```
EMPLACEMENT ROUE DE SECOURS — CAISSON CHAUFFÉ
┌────────────────────────────────────────────────────────────────┐
│ ANNEAU PÉRIPHÉRIQUE — MOUSSE PE 20mm + PLAQUE ALU BLINDAGE     │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  ZONE PRINCIPALE                                          │ │
│  │                                                            │ │
│  │  ┌───────────┐  ┌───────────────┐                        │ │
│  │  │ MAXWELL   │  │ EVEREXCEED    │  ← BMS interne          │ │
│  │  │ 16V 100F  │  │ LiFePO4 12V   │     (V1)                │ │
│  │  │ SUPERCAP  │  │ 8Ah 96Wh      │                          │ │
│  │  └─────┬─────┘  └────┬──────────┘                        │ │
│  │        │            │                                      │ │
│  │   LTC4359 ── // ───┘ ← diode idéale + pré-charge NTC     │ │
│  │                                                            │ │
│  │  ┌──────────────────────────┐                            │ │
│  │  │ ESP32 + 18650 + TP4056   │                            │ │
│  │  │ INA219 ×2 + DS18B20 ×3   │ ← télémétrie autonome      │ │
│  │  │ Hub USB 1→3 voies        │                            │ │
│  │  │ MT3608 5V→14V             │                            │ │
│  │  └──────────────────────────┘                            │ │
│  │                                                            │ │
│  │  ┌──────────────────────────┐                            │ │
│  │  │ POINT DE MASSE CENTRAL    │ ← bus cuivre 50mm²        │ │
│  │  │ + tirages V2 en attente  │                            │ │
│  │  └──────────────────────────┘                            │ │
│  │                                                            │ │
│  │  ZONE LIBRE V2 (≈30-40% du volume) :                     │ │
│  │  - Pack LTO 10Ah 20S (V2)                                │ │
│  │  - Banc supercondos 48V (V2)                              │ │
│  │  - Onduleur SiC custom (V2)                              │ │
│  │  - BMS LTO + DC/DC (V2)                                  │ │
│  │                                                            │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                  │
│  SYSTÈME THERMIQUE :                                            │
│  - KSD301 NC 15°C + PTC 20W + fusible Tf 60°C (fail-OFF)       │
│  - KSD301 NO 40°C + ventilateur PC 80mm (fail-ON)              │
│  - DS18B20 ×3 (cells + ambiant + extérieur)                    │
│                                                                  │
│  MISE À L'AIR CALIBRÉE (évac dégazage anormal)                 │
│                                                                  │
└────────────────────────────────────────────────────────────────┘
         │                                                
         │ PASSAGES CÂBLES (tirages V0)                          
         │
         ├── Bus 12V → mégafuse 150A → câble cranking 35-50mm²
         │                                  │
         │                                  └── démarreur baie moteur
         │
         ├── Câbles V1 retours masse étoile (vers consommateurs)
         │
         ├── Câble USB conducteur (vers console centrale)
         │
         └── TIRAGES V2 EN ATTENTE :
             - Bus 48V (25-35mm²) → emplacement iBSG futur
             - CAN-C blindé (×8) → emplacements capteurs distribués
             - LIN (×N) → capteurs lents
             - MT 48V → feux AR
             - RFID coaxial (×24) → points châssis
             - Réserve (×3-4 paires)
```

---

## 5 — HUB USB INTERNE 1→3 VOIES

### Principe

Le port USB extérieur (console centrale conducteur) reçoit le 5V depuis une powerbank ou un téléphone OTG. À l'intérieur du caisson, un hub USB passif ou un splitter répartit ce 5V vers 3 fonctions :

```
Port USB conducteur (console centrale)
        │
        │ Câble USB blindé 3-4 m
        │
        ↓
[Hub USB 1→3 voies internes au caisson]
        │
        ├── Voie 1 : TP4056 → Cellule 18650 → Alimentation ESP32
        │           Priorité absolue en mode rescue
        │           5V → 4,2V → 3,3V via régulateur ESP32
        │
        ├── Voie 2 : MOSFET commande chauffage → Chauffage PTC 12V
        │           Activé par ESP32 si T° < 5°C
        │           Limite 1A continu pour ne pas vider powerbank
        │
        └── Voie 3 : MT3608 5V→14V → Bus 12V (mode rescue)
                    Activé par ESP32 après diagnostic
                    Réveille batterie EverExceed
```

### Composants

| Composant | Référence cible | Rôle | Prix |
|---|---|---|---|
| Hub USB 4 ports passif | Type-A femelle ×4 | Distribution interne | 5-10 € |
| Port USB-A conducteur | IP67 marine automotive | Connexion powerbank | 5-10 € |
| Câble USB blindé 3-4m | USB-A vers USB-A | Liaison conducteur ↔ caisson | 5-10 € |
| TP4056 module | Charge LiPo 1S | Charge cellule 18650 | 1-2 € |
| Cellule 18650 + holder | Samsung 25R ou Panasonic NCR18650B | Alim ESP32 | 5-8 € |
| MT3608 boost | 5V→3.3-28V réglable | Mode rescue 5V→14V | 1-2 € |
| MOSFET commande PTC | IRLZ44N ou similaire | Activation chauffage | 1-2 € |
| Diode anti-retour | Schottky SS56 60V 5A | Protection MT3608 | 1 € |
| **TOTAL hub USB système** | | | **24-45 €** |

---

## 6 — MODE RESCUE SÉQUENTIEL

### Séquence d'activation

**Étape 1 — Powerbank branchée**
- Utilisateur connecte powerbank USB sur port conducteur (console centrale)
- 5V parvient au hub USB interne du caisson
- TP4056 commence à charger la cellule 18650

**Étape 2 — Cellule 18650 atteint ~3,5V (charge minimum)**
- ESP32 démarre
- Lecture des capteurs : tension batterie EverExceed, températures cellules + ambiante
- Affichage état via BLE smartphone si connecté
- Estimation du SoH de la batterie

**Étape 3 — Diagnostic ESP32**

Conditions évaluées :
- T° batterie < 5°C ? → préchauffage nécessaire
- Tension cellule LiFePO4 < 2,8V ? → BMS verrouillé, réveil délicat
- Tension cellule LiFePO4 entre 2,8 et 3,2V ? → BMS récupérable, réveil OK
- Tension cellule LiFePO4 > 3,2V ? → batterie OK, problème ailleurs

**Étape 4 — Préchauffage si nécessaire**
- Si T° < 5°C, ESP32 active MOSFET chauffage PTC
- Chauffage limité à 1A continu (5W via powerbank)
- Durée : 15-30 min selon T° ambiante
- ESP32 surveille la montée en T° (DS18B20)

**Étape 5 — Réveil bus 12V**
- ESP32 active MT3608 boost 5V → 14V
- Bus 12V passe progressivement à 14V (limitation courant powerbank ~500-1000 mA)
- BMS interne EverExceed se déverrouille si tension cellule remonte
- ESP32 monitore la remontée en tension du pack LiFePO4

**Étape 6 — Tentative de démarrage**
- Si tension batterie atteint >12V stable, ECU peut démarrer
- Tentative de démarrage via le démarreur stock reconditionné
- Alternateur prend le relais
- Mode rescue se désactive automatiquement

**Étape 7 — Désactivation rescue**
- ESP32 détecte alternateur actif (tension >13,5V)
- Coupe MT3608 (pas besoin du boost USB)
- Coupe chauffage PTC (alternateur peut maintenant alimenter le chauffage natif si nécessaire)
- Continue à charger sa cellule 18650 pour la prochaine fois

### Pseudocode ESP32 mode rescue

```
état_init:
    démarrage ESP32 sur cellule 18650
    lecture INA219 batterie, INA219 condos, DS18B20 ×3
    SoC_batterie = estimation(V_batterie, V_cellules)
    notification_BLE("Mode rescue actif, diagnostic en cours")

état_diagnostic:
    SI V_batterie > 12V:
        notification_BLE("Batterie OK, problème ailleurs (ECU/alternateur)")
        attendre_action_utilisateur()
    
    SI T_batterie < 5°C:
        actionner_MOSFET_chauffage(ON)
        notification_BLE("Préchauffage batterie en cours")
        attendre(T_batterie > 5°C, max 30 min)
        actionner_MOSFET_chauffage(OFF)
    
    SI V_cellule_min < 2,8V:
        notification_BLE("BMS verrouillé, tentative réveil délicat")
    
    passer_à_état_reveil()

état_reveil:
    actionner_MT3608(ON, 14V)
    notification_BLE("Réveil bus 12V en cours")
    attendre(V_batterie > 12V, max 60 min)
    SI V_batterie > 12V:
        notification_BLE("Bus 12V réveillé, tenter démarrage")
        attendre_action_utilisateur()
    SINON:
        notification_BLE("Échec réveil, batterie trop dégradée")
        actionner_MT3608(OFF)
        état_assistance_externe()

état_actif:
    SI alternateur_actif (V_bus > 13,5V):
        actionner_MT3608(OFF)
        actionner_MOSFET_chauffage(OFF si non nécessaire)
        notification_BLE("Système en marche, rescue désactivé")
    continuer_monitoring()
```

---

## 7 — RELOCATION BATTERIE — COMPOSANTS V1

### Composants principaux

| Composant | Rôle | Réf. | Prix | Fournisseur |
|---|---|---|---|---|
| **Maxwell 16V 100F** (6× 2.7V 600F) | Pics cranking 200-400A | — | ~57 € | AliExpress ✅ |
| **EverExceed LiFePO4 12V 8Ah 96Wh** | Stockage veille + accessoires | — | 50-80 € | Amazon |
| Fusibles AGU 30A ×2 | Protection circuits | — | 1,76 € | Amazon ✅ |
| Boîte fusibles 6 voies KAOLALI | Distribution secondaire | — | 16,49 € | Amazon ✅ |
| Disjoncteur 30A réarmable EPLZON | Protection accessoires | — | 13,99 € | Amazon ✅ |
| Mégafuse ANL 150A | Protection chemin cranking | — | 8-15 € | AliExpress |
| Câble cuivre étamé 35-50mm² | Cranking | — | 30-50 € (3m) | Spécialisé |
| Cosses sertissables M8 | Bornes pack et fusibles | — | 10-15 € | Amazon |

### Sous-circuit avant (LTC4359 + pré-charge)

| Composant | Réf. cible | Rôle | Prix |
|---|---|---|---|
| Diode idéale | LTC4359 | Aiguillage condos→bus | 8-12 € |
| MOSFET principal | IRFP4368PBF ou IPB180N10S3 | Élément actif | 4-8 € |
| NTC pré-charge | SCK-103 (10Ω 4A) | Limitation inrush | 2-5 € |
| Relais bypass | Songle SRD-12VDC-SL-C | Court-circuit NTC | 3-5 € |
| Comparateur | LM393 + TL431 | Seuil bascule 12,5V | 2-3 € |
| Résistances précision 1% | 10kΩ ×6 | Diviseur tension | 1-2 € |
| LED verte 5mm | — | Indicateur cockpit | 0,5 € |
| Résistance LED | 470Ω-1kΩ | Limitation courant | 0,5 € |
| Boîtier IP65 | Alu/plastique 100×80×40 | Protection compartiment moteur | 15-30 € |
| Connectique | Cosses faston isolés | Bornes accessibles | 5-10 € |
| **TOTAL sous-circuit avant** | | | **40-75 €** |

### ESP32 télémétrie + composants caisson

| Composant | Référence cible | Rôle | Prix |
|---|---|---|---|
| ESP32-WROOM-32 ou ESP32-S3 | DevKit | MCU principal | 5-10 € |
| Cellule 18650 + holder | Samsung 25R | Alim auto-suffisante | 5-8 € |
| TP4056 module | TC4056A | Charge LiPo | 1-2 € |
| MT3608 boost | MT3608 | Mode rescue 5V→14V | 1-2 € |
| INA219 ×2 | I2C V/I | Mesure V/I batterie + condos | 3-6 € |
| DS18B20 ×3 | 1-Wire T° | T° cellules + ambiant | 3-6 € |
| Hub USB 4 ports passif | USB-A | Distribution interne | 5-10 € |
| Port USB-A conducteur | IP67 automotive | Console centrale | 5-10 € |
| Câble USB blindé 3-4m | USB-A vers USB-A | Liaison | 5-10 € |
| MOSFET commande PTC | IRLZ44N | Activation chauffage | 1-2 € |
| Diode anti-retour | Schottky SS56 | Protection MT3608 | 1 € |
| Connectique JST/Dupont | Câbles + connecteurs | Liaison | 5-10 € |
| Boîtier IP54 | ABS 60×80×30 | Protection ESP32 | 5-10 € |
| **TOTAL ESP32 + Hub USB** | | | **45-87 €** |

---

## 8 — ALTERNATEUR K9K (V1 conservation stock)

| Action | Détail |
|---|---|
| Maintenance préventive | Charbons + bagues neufs (400-600 km après reprise) |
| Contrôle tension | 13,3-14,7V au ralenti, 14,7V max sous charge |
| Régulateur | OE Renault (intégré alternateur) |
| Remplacement V2 | Sera remplacé par l'iBSG Valeo |

---

## 9 — DÉMARREUR STOCK RECONDITIONNÉ (décision V18.1)

### Décision actée

Conservation du démarreur Modus stock au lieu du Clio 3 GT donneur. Économie sur le sourcing en casse + temps gagné.

### Maintenance préventive

| Opération | Détail |
|---|---|
| Démontage complet | Avec marquage des sens de bobinage |
| Nettoyage extérieur | Brosse + dégraissant, élimination de la rouille superficielle |
| Nettoyage intérieur | Souffler à l'air comprimé, dépoussiérage collecteur |
| Contrôle balais (charbons) | Longueur résiduelle > 5 mm (sinon remplacement) |
| Lubrification lanceur | Graisse silicone haute température |
| Contrôle bobinage | Mesure résistance (court-circuit, coupure) |
| Contrôle solénoïde | Ressort de rappel, contacts (sains) |
| Remontage | Serrage couples constructeur + Loctite 243 sur vis solénoïde |
| Test sur banc | Si possible, sinon test in situ après remontage |

### Coût

- Maintenance préventive : 30-50 € (charbons + graisse + nettoyant)
- Pas de sourcing casse nécessaire
- **Économie : 50-100 €** vs Clio 3 GT donneur

---

## 10 — FIABILISATION CÂBLAGE MOTEUR

Référence : Tâches 25 et 26 du projet.

| Élément | Action |
|---|---|
| Connecteurs | Nettoyant contact + graisse diélectrique + contrôle pin |
| Gaines | Remplacement gaines fendues par gaine annelée neuve, ruban Tesa 51608 |
| Quickshift résiduel | Isolation propre connecteurs BVR déconnectés (gaine thermo + ruban) |

**Note** : les masses châssis ne sont plus traitées (supprimées en Phase 0).

---

## 11 — CONTACTEURS ET CAPTEURS

### Contacteur pédale embrayage

- Référence : METZGER ✅ Autodoc (OE 8200276359)
- 2 fils calculateur, reprog UCH BVR → BVM nécessaire (Renolink)
- Indispensable pour la conversion Quickshift → BVM

### Contacteur marche arrière

- Référence : Febi 37169 ✅ Autodoc (OE 8200209496)
- Clé de 22 pour démontage
- Feux de recul fonctionnels = CT OK

---

## 12 — OIL CATCH CAN

- Reniflard moteur → Catch can alu (entre vanne EGR et admission)
- Vidanger tous les 5 000 km
- Si >100 ml : surveillance segments (signe d'usure moteur K9K766)

---

## 13 — RÉFÉRENCES ARCHITECTURE V2

Voir document complet : `Architecture_Electrique_Electronique_V2.md`

### Conservé en V2 (depuis V1)
- Batterie LiFePO4 EverExceed 12V 8Ah
- Banc supercondos Maxwell 16V 100F
- Sous-circuit avant LTC4359 + pré-charge
- Caisson sous coffre chauffé (V0)
- ESP32 télémétrie (avec extensions capteurs 48V)
- Hub USB + mode rescue séquentiel
- Câblage cranking 12V

### Ajouts V2
- Suppression alternateur K9K stock
- Suppression démarreur stock
- Installation iBSG Valeo 12 kW (remplace alternateur + démarreur)
- Bus 48V dédié (tirages déjà préparés en V0)
- Pack LTO 10Ah 20S Tycorun (7 kg)
- Banc supercondos 48V (20× 1500F = 3,5 kg)
- DC/DC bidirectionnel 12V ↔ 48V (500W)
- Onduleur SiC custom 12 kW
- BMS LTO custom (JK 20S 100A initialement, OptiMOS custom plus tard)
- Capteurs INA228 sur bus 48V (extension ESP32)
- Bracket d'adaptation K9K + OAD + tendeur hydraulique + courroie aramide

---

## 14 — COÛT TOTAL V0+V1 ÉLECTRIQUE

| Catégorie | € mini | € maxi |
|---|---|---|
| Caisson V0 (infrastructure) | 97 | 154 |
| Tirages V0 (V1+V2 préparés) | 270 | 440 |
| Batterie + supercondos | 107 | 137 |
| Fusibles + distribution | 32 | 47 |
| Câblage cranking | 40 | 65 |
| Sous-circuit avant (LTC4359 + pré-charge) | 40 | 75 |
| ESP32 + Hub USB | 45 | 87 |
| Maintenance alternateur stock | 30 | 50 |
| Maintenance démarreur stock | 30 | 50 |
| Mastic + rondelles inox (boucher anciens trous masses) | 15 | 25 |
| Diélectromètre | 30 | 50 |
| Boîtiers + connectique | 30 | 60 |
| **TOTAL ÉLECTRIQUE V0+V1** | **766** | **1 240** |

---

## 15 — VIGILANCE V18.1

### Sécurité

- Fusible mégafuse 150A max 30 cm de la batterie
- Gaine annelée TOUT le parcours du câble +12V
- Cloison étanche avec passe-fil caoutchouc + mastic Sikaflex 221
- Caisson sous coffre immobilisé (visserie M6 inox + rondelles éventail)
- Bornes batterie protégées (capuchons isolants automotive)
- Mise à l'air calibrée pour évacuation en cas de dégazage anormal

### Préparation V2 (tirages V0)

- Tous les câbles V2 sont en attente, gainés et marqués
- Boucle de mou 30-50 cm de chaque côté pour ajustements
- Étiquettes thermorétractables : type + destination + section
- Extrémités scellées par thermo en attendant connexion

### Préparation Phase 2

- Laisser 30-40 cm de mou côté baie pour futur ECU Bosch K9K896
- Câble 48V dimensionné pour la durée du projet (pas à refaire)

### Sécurité retrait masses châssis

- Travail à effectuer en Phase 0 (batterie débranchée)
- Vérifier la continuité de chaque circuit après modification
- Boucher tous les trous de masse châssis (mastic + rondelle inox)
- Documenter les modifications dans le journal de bord

---

*CÂBLAGE V18.1 V1 — 1er juin 2026*
*Architecture minimaliste pour faire rouler la Modus rapidement*
*V0 infrastructure + V1 électrique passif + préparation V2 complète*
