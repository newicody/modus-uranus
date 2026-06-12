# Architecture Électronique & Multiplexage — Renault Modus Phase 2
## Spécifications Techniques : 1.5 dCi 86 ch (Injection Delphi dCi) — Plateforme B (Clio 3)

Ce document cartographie l'architecture électronique et les protocoles de communication du véhicule. La Modus Phase 2 s'inscrit dans l'ère du **multiplexage de transition**, articulé autour de l'Unité Centrale d'Habitacle (UCH) agissant comme passerelle centrale (*Gateway*).

---

## 1. Le Réseau CAN Habitacle (V-CAN / Body CAN)
Gère le confort, la carrosserie et la vie à bord. L'UCH sert de nœud central et de passerelle d'aiguillage vers les autres bus.

* **Interface Physique (Couche 1) :**
    * **Câblage :** Paire torsadée de fils en cuivre (CAN-High / CAN-Low).
    * **Tensions nominales :** CAN-H varie entre 2,5V et 3,5V | CAN-L varie entre 2,5V et 1,5V.
    * **Vitesse de transmission :** CAN Basse Vitesse (*Low Speed*), cadencé à 125 kbps ou 250 kbps.
* **Interface Logique (Couches Supérieures) :**
    * **Format des Trames :** Trames CAN standard (identifiants 11 bits) selon la norme **ISO 11898-3** (*Fault-Tolerant CAN*).
    * **Protocole Constructeur :** Matrice de commutation Renault (gestion des états ouvrants, essuyage, éclairage, habitacle).
* **Calculateurs Connectés :**
    * UCH (Unité Centrale d'Habitacle)
    * Tableau de bord (Combiné d'instruments)
    * Radio / Afficheur déporté
    * Climatisation régulée
    * Calculateur d'aide au stationnement (Radar de recul)

---

## 2. Le Réseau CAN Inter-Systèmes (M-CAN / Powertrain CAN)
Bus critique à haute vitesse dédié à la sécurité active et à la chaîne de traction.

* **Interface Physique (Couche 1) :**
    * **Câblage :** Paire torsadée en cuivre, topologie de bus fermée par deux résistances de fin de ligne de 120 Ohms.
    * **Vitesse de transmission :** CAN Haute Vitesse (*High Speed*) à 500 kbps.
    * **Tensions nominales :** Norme **ISO 11898-2** (CAN-H à 3,5V et CAN-L à 1,5V en état dominant).
* **Interface Logique (Couches Supérieures) :**
    * **Format des Trames :** Trames CAN standard (11 bits), norme **ISO 11898-2**.
    * **Protocole Constructeur :** Trames hautes priorités (requêtes de couple moteur, régime, vitesse de roue, régulation de trajectoire dynamique).
* **Calculateurs Connectés :**
    * ECU Moteur (Delphi DCM 1.2 ou DCM 3.4)
    * Bloc ABS / ESP
    * DAE (Direction Assistée Électrique — couplage permanent avec l'ECU Moteur)
    * Boîtier Airbag (diffusion de l'état de choc et vitesse véhicule)

---

## 3. Le Réseau de Diagnostic (Prise OBD2)
Interface de communication avec l'extérieur (Outil constructeur Renault CLIP ou scanners OBD-II standards). Utilise deux couches physiques distinctes sur le même connecteur standardisé.

### A. Le CAN Diag
* **Interface Physique :** Broches 6 (CAN-H) et 14 (CAN-L) de la prise OBD2. Vitesse fixe à 500 kbps.
* **Interface Logique :**
    * **ISO 15765-4 :** Standard légal requis pour les diagnostics antipollution d'urgence.
    * **ISO 14229 (UDS)** & **KWP2000 sur CAN :** Protocoles spécifiques Renault (télécodage d'injecteurs Delphi, configurations et flux de données étendus).

### B. La Ligne K (Diagnostic Legacy)
Présente pour la rétrocompatibilité et les procédures de réveil de calculateurs d'anciennes générations.

* **Interface Physique :** Liaison monofilaire en cuivre, broche 7 de la prise OBD2. Ligne de communication tirée au 12V (type UART). Vitesse de 10.4 kbps.
* **Interface Logique :** Normes **ISO 9141-2** et **ISO 14230** (KWP2000 sur ligne K).

---

## 4. Le Réseau LIN (Local Interconnect Network)
Réseau secondaire de type Maître/Esclave destiné aux périphériques de carrosserie locaux ne requérant pas la bande passante d'un bus CAN. L'UCH y joue systématiquement le rôle de *Master*.

* **Interface Physique (Couche 1) :**
    * **Câblage :** Un seul fil de cuivre (monofilaire).
    * **Tensions nominales :** Commutation logique entre 0V (Masse) et 12V (Batterie).
    * **Vitesse de transmission :** Économique et basse vitesse, fixée à 19.2 kbps.
* **Interface Logique (Couches Supérieures) :**
    * Protocole LIN fondé sur une transmission série asynchrone (type UART), norme **ISO 17987**.
* **Composants Périphériques (Slaves) :**
    * Platine de commande des lève-vitres (porte conducteur)
    * Capteur mixte de pluie et de luminosité (embase de rétroviseur)
    * Sirène d'alarme volumétrique
    * Alternateur piloté (liaison LIN directe vers l'ECU Moteur pour la charge intelligente)

---

## 5. Les Liaisons Filaires Point à Point (Signaux Analogiques & Logiques Purs)
Liaisons électriques brutes directes où la couche physique fait directement office de support logique, sans encapsulation protocolaire.

| Système / Ligne | Interface Physique | Interface Logique / Signal | Description |
| :--- | :--- | :--- | :--- |
| **Circuit Airbag** | Liaison bifilaire dédiée en cuivre direct. | Impulsion calibrée en courant continu ($I_{dc}$). | Déclenchement pyrotechnique instantané des allumeurs depuis le boîtier Airbag. |
| **Ligne d'Inhibition (Crash)** | Câblage direct point à point (Boîtier Airbag $\rightarrow$ UCH & ECU Moteur). | Signal de masse permanent ($0\text{V}$) en cas d'impact. | Commande d'urgence forçant l'ECU Delphi à couper immédiatement la pompe d'alimentation en carburant. |
| **Anti-démarrage (W-Line)** | Bague de transpondeur Neiman $\rightarrow$ UCH. | Signal RF 125 kHz converti en modulation numérique filaire. | Transmission du code d'authentification de la clé (ID de type HITAG 2). |
| **Capteur PMH (Régime)** | Liaison bifilaire torsadée et blindée vers l'ECU. | Tension alternative sinusoïdale ($V_{ac}$). | Signal d'un capteur inductif dont la fréquence change proportionnellement à la vitesse de rotation du vilebrequin. |
