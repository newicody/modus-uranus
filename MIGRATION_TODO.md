# MIGRATION TODO (post-réorg)

## Schéma & déplacements à finaliser

- Décider du rapatriement de `doc/**/photos` vers `/photos` (doc/ est marqué SOURCE 'ne pas alourdir' dans le README).
- Migrer le schéma de `ia/populate/data/organes_mecaniques.csv` vers : id,nom,systeme,sous_systeme,X,Y,Z,zone,ref_oe,ref_montee,etat,phase,couple_nm
- Migrer le schéma de `ia/populate/data/reseau_12v.csv` vers : id,nom,systeme,sous_systeme,X,Y,Z,zone,ref_oe,ref_montee,etat,phase,couple_nm
- Migrer le schéma de `ia/populate/data/reseau_3v3.csv` vers : id,nom,systeme,sous_systeme,X,Y,Z,zone,ref_oe,ref_montee,etat,phase,couple_nm
- Migrer le schéma de `ia/populate/data/reseau_48v.csv` vers : id,nom,systeme,sous_systeme,X,Y,Z,zone,ref_oe,ref_montee,etat,phase,couple_nm
- Migrer le schéma de `ia/populate/data/reseau_5v_glovebox.csv` vers : id,nom,systeme,sous_systeme,X,Y,Z,zone,ref_oe,ref_montee,etat,phase,couple_nm
- Migrer le schéma de `ia/populate/data/reseau_5v_usb.csv` vers : id,nom,systeme,sous_systeme,X,Y,Z,zone,ref_oe,ref_montee,etat,phase,couple_nm
- Migrer le schéma de `ia/populate/data/sensors.csv` vers : id,nom,systeme,sous_systeme,X,Y,Z,zone,ref_oe,ref_montee,etat,phase,couple_nm
