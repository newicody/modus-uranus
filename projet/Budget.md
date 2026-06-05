# BUDGET — REFONTE V19 (structure V0 / V1 / V2 + Phase 2)
**Véhicule :** Modus 1.5 dCi JP0F K9K766 JA5 — VF1JP0F0H43308282 — 130 000 km
**Boîte :** TL4B043 **neuve** (Eurofrance24, OE 320109255R / 8201057476) · couple bridé 240-260 Nm
**Stratégie :** V0 infra → V1 roulante → V2 iBSG 48V → Phase 2 K9K896 · 5 juin 2026

---

## ⚠️ CORRECTIONS BUDGÉTAIRES (à appliquer avant de re-commander)
| # | Sujet | Correction | Impact € |
|---|---|---|---|
| 1 | **Disques de frein** | « Disques AV TRW DF4274BS » (Oscaro 109,88) = **disque ARRIÈRE 240mm**, doublon des Brembo 09.9078.75 (AR, 83,26). **Tu n'as PAS de disques AVANT.** | Retirer 1 jeu AR (~84-110) **+ ajouter vrais disques AV 260mm** (~50-80) |
| 2 | RoyPow 18Ah (69,99) | Remplacé par **EverExceed 8Ah** (déjà commandé) | −69,99 |
| 3 | BDA604 + BDA605 (68,25) | Audi A6 incompatibles → **retirés** | −68,25 |
| 4 | Chape étrier AR | 1 seule chez Autodoc (65,99) → **ajouter 2ᵉ côté BDA1088** | +66 |
| 5 | Fusées AR « version disque » (50-180) | **RÉSOLU** : trous de chape présents → bolt-on, **aucune fusée AR à acheter** | −50 à −180 |
| 6 | Démarreur | **Modus stock reconditionné** (décidé, pas Clio GT) — charbons/bagues | ~20-40 |
| 7 | Insonorisation | HASKYY → **Reckhorn ABX-tra 2,5mm + mousse ODIPIE + feutre capot casse** | ~80-115 |

---

## COMMANDES PAYÉES — 1 087 € (réparties par version)
| Fournisseur | Détail | € | Version |
|---|---|---|---|
| Eurofrance24 | TL4B043 neuve + livraison | 531,79 | V1 |
| GT2i | Powerflex ×6 (PF-F60901/902/920/821/525 + R60810) | 392,40 | V1 |
| Norauto ×3 | Chandelles 2T + extracteur moyeu + E-Torx + clés + barre force + clé purge + adapt. | 162,88 | Outillage |
| | **TOTAL PAYÉ** | **1 087,07** | |

---

## V0 — INFRASTRUCTURE (corrosion · insonorisation · caisson · câblage)
*À faire en premier, caisse ouverte.*

### Anti-corrosion (Férose → Restom → Owatrol)
| Pièce | Réf | € |
|---|---|---|
| Époxy blindage | RESTOM EAF 2092 RAL9003 1kg + diluant | 64,00 |
| Transport Restom | | 9,90 |
| Convertisseur rouille | FÉROSE 1L | 49,99 |
| Owatrol Rustol aérosol 500ml | | 34,50 |
| Owatrol huile 1L + pinceau | | 29,00 |
| **Sous-total corrosion** | | **187,39** |

### Insonorisation (corrosion traitée d'abord ; 0 mousse pare-feu/capot)
| Pièce | € est. |
|---|---|
| Alubutyl Reckhorn ABX-tra 2,5mm (~2 m², rouleau 0,40×5m) | 30-45 |
| Mousse ODIPIE coton auto-adhésive (4-5 m², ~10 €/m²) | 40-50 |
| Feutre capot Modus d'origine (casse) | 10-20 |
| **Sous-total insonorisation** | **80-115** |

### Caisson sous coffre + thermique + câblage
| Poste | € est. |
|---|---|
| Caisson (bois/alu, mousse, plancher renforcé, ventilation, KSD301 + PTC + ventilateur fail-safe) | 80-180 |
| Tirages câbles **V1** (cranking, alternateur, USB, ESP32) + passe-fils IP65 | 60-120 |
| Tirages câbles **V2 en attente** (bus 48V 25-35mm², CAN-C blindé, LIN, RFID 24 pts) | 80-180 |
| Élec infra (boîte fusibles KAOLALI 16,49 + disjoncteur EPLZON 13,99 + fusibles AGU 1,76) | 32,24 |
| Suppression masses châssis (retours dédiés étoile) — câble + cosses | 20-40 |
| **Sous-total caisson/câblage** | **272-552** |

**TOTAL V0 ≈ 540 - 855 €**

---

## V1 — MÉCANIQUE COMPLÈTE + ÉLEC PASSIF (la Modus roule)

### Boîte / embrayage / conversion manuelle
| Pièce | Réf | € |
|---|---|---|
| TL4B043 neuve | OE 320109255R | (payé) |
| Kit embrayage 4P conversion (volant rigide + CSC) | VALEO 845077 | 340,90 |
| Émetteur embrayage | VALEO 804816 | 74,20 |
| Contacteur pédale embrayage | METZGER (OE 8200276359) | 6,59 |
| Contacteur feu de recul | FEBI | 12,49 |
| Support BV gauche | LEMFÖRDER 37966 01 | 61,99 |
| Biellette reprise couple inf. | LEMFÖRDER 36284 01 | 43,70 |
| Huile BV 75W-80 (4×1L, besoin ~2,5L) | MOTUL | 65,96 |
| Patte alu support sup. + levier 6V + câbles + pédalier | Casse (Modus 105/106 idéal) | 100-300 |

### Transmission
| Cardan G / D | SKF **VKJC 6010 / 6009** | 360,29 |
| Soufflets direction ×2 | SKF VKJP 2011 | 21,60 |
| Graisse molybdène ×4 | FEBI | 11,96 |

### Moteur (fiabilisation K9K)
| Kit distrib + pompe eau 123 dents | SKF | 54,99 |
| Piges calage | YATO | 19,49 |
| Calorstat | AISIN THRAZ-7009 | 18,90 |
| SPI vilo AV / AR / AAC | Corteco 20031906B / Reinz 81-38528-00 / 81-34367-00 | 69,71 |
| Boulons de bielle ×4 🔴 | ENGINETEAM BS0029 | 10,75 |
| Coussinets de bielle (après inspection) | ACL/King | 40-80 |
| Supports moteur inserts | Powerflex PF-F60920/821 | (payé) |
| Bougies préchauffage + graisse cuivre | Bardahl | 9,90 |
| FMIC intercooler | NRF 30481 | 118,90 |
| Oil catch can | — | 20-40 |
| Reprog stage 0 (240-260 Nm) DIY | Kess V2 + KTAG | 40,79 |

### Suspension / train
| Bilstein B8 AV ×2 / AR ×2 | BILSTEIN 35-128649 / monotube | 549,31 |
| Ressorts | EIBACH Pro-Kit E10-75-008 | 179,50 |
| Kit coupelle AV 6 pcs ×2 | SNR KB655.32 | 117,80 |
| Kit protection amortisseur | MEYLE 16-14 740 0001 | 17,28 |
| Triangles AV ×2 | MEYLE | 125,98 |
| Rotules direction ext. ×2 / int. ×2 | MEYLE M14×1.5 / 16-16 031 0015 | 66,56 |
| Biellettes stab AV HD ×2 / AR ×2 | MEYLE | 88,12 |
| Moyeux AV ×2 | MEYLE | 59,98 |
| Roulements AV ×2 | SKF VKBA 3596 | 55,40 |
| Fusées AV neuves G / D | VAICO | 159,98 |

### Freinage (AV 260mm + conversion disque AR)
| Étriers AV fonte G / D | FEBI | 125,48 |
| Chapes étrier AV ×2 | TRW | 64,98 |
| **Disques AV 260mm ×2** ⚠️ À AJOUTER (manquants) | (Clio 3 GT/dCi 260mm) | 50-80 |
| Plaquettes AV | Brembo P 68 033X | 45,49 |
| Étriers AR alu G / D | TRW BHQ243 / BHQ244 | 216,98 |
| Chapes étrier AR | TRW BDA671 (+ **BDA1088 2ᵉ côté**) | 65,99 + ~66 |
| **Disques AR 240mm roulement+ABS ×2** | Brembo 09.9078.75 **OU** TRW DF4274BS (un seul) | 83,26 |
| Plaquettes AR | TRW GDB1330 | 19,90 |
| Flexibles aviation AV+AR | Goodridge | 109,23 |
| Loctite 243 ×3 | | 32,70 |
| Bouchon vidange + outils freins (clé dynamo VOREL, repousse-piston) | Corteco / Neo | 39,57 |

### Roues / carrosserie
| Jantes JR-7 16×7 ET38 4×100 ×4 | Ultraperformance | 596,00 |
| Pneus 195/55 R16 ×4 | Norauto | 280-320 |
| Passage de roue / cache moteur | BLIC | 68,40 |
| Agrafes/rivets (clip 7703077435 lots de 10) + visserie M6/M8/M12 + rivnuts | — | 30-50 |

### Élec passif V1
| Batterie | EverExceed LiFePO4 12V 8Ah | (commandé) |
| Supercondos | Maxwell 16V 100F | 57,28 |
| Sous-circuit AV (LTC4359 + pré-charge NTC) + ESP32 télémétrie + hub USB + MT3608 rescue | — | 60-150 |

**TOTAL V1 ≈ 4 550 - 5 050 €** (dont ~924 € déjà payés inclus dans le total projet)

---

## V2 — ARCHITECTURE iBSG 48V (estimation, ~4-6 mois après V1)
| Poste | € mini | € maxi |
|---|---|---|
| iBSG Valeo 12 kW (casse Mercedes Sprinter eDrive) | 200 | 600 |
| Pack LTO 10Ah 20S | 200 | 400 |
| Banc supercondos 48V (20× 1500F) | 150 | 300 |
| DC/DC bidirectionnel 12↔48V 500W | 80 | 200 |
| Onduleur SiC custom 12 kW (CoolSiC) | 200 | 500 |
| BMS LiFePO4 custom OptiMOS + 6 PCB custom + MCU AURIX TC375 | 200 | 600 |
| Signalisation MT + surveillance corrosion RFID NAC1080 | 80 | 200 |
| **TOTAL V2 (indicatif)** | **~1 110** | **~2 800** |
> Budget à affiner après le Salon Infineon (réfs MOSFETs/drivers).

---

## PHASE 2 — SWAP K9K896 (inchangé)
| Poste | € mini | € maxi |
|---|---|---|
| Casse (K9K896 + ECU EDC17C84 + faisceau + FAP) | 900 | 2 140 |
| Pièces neuves (distrib/coussinets/joints/calorstat + reprog + gros turbo) | 960 | 1 795 |
| **TOTAL PHASE 2** | **1 860** | **3 935** |

---

## OUTILLAGE (transversal — déjà payé en grande partie)
Chandelles 2T ×2, extracteur moyeu, E-Torx, T50, clés, barre de force, clé purge 8mm + adaptateur, clé dynamométrique VOREL 1/2", repousse-piston rotatif, piges YATO. **≈ 186 € (payé)** + carré 8mm/clé 22 manquants ~20-30 €.

---

## RÉSUMÉ FINANCIER GLOBAL
| Étape | € mini | € maxi |
|---|---|---|
| **V0 — Infrastructure** | 540 | 855 |
| **V1 — Roulante (mécanique + élec passif)** | 4 550 | 5 050 |
| **V2 — iBSG 48V** | 1 110 | 2 800 |
| **Phase 2 — K9K896** | 1 860 | 3 935 |
| **TOTAL PROJET** | **~8 060** | **~12 640** |
> Dont **~1 087 € déjà payés**. Net corrections appliquées : −206 € (doublon disque AR + RoyPow + BDA) / +116-146 € (disques AV + 2ᵉ chape AR).

---

## RESTANT À COMMANDER (priorité V0→V1)
1. **Disques AV 260mm ×2** (manquants — erreur DF4274BS) — 50-80 €
2. 2ᵉ chape étrier AR **BDA1088** — ~66 €
3. Disques AV : retirer 1 doublon AR (Brembo OU DF4274BS) — économie 83-110 €
4. Pneus 195/55 R16 ×4 — 280-320 €
5. Insonorisation Reckhorn + ODIPIE + feutre capot — 80-115 €
6. Matériaux caisson + câbles tirages V1/V2 — 220-470 €
7. Pièces casse (levier/pédalier/câbles + patte alu) — 100-300 €
8. Coussinets bielle (après inspection) — 40-80 €
9. Démarreur recond (charbons/bagues) — 20-40 €

*Retirer du panier : RoyPow 18Ah, BDA604, BDA605, 1 jeu disques AR en double, ligne « fusées AR version disque ».*
