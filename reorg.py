#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reorg_uranus.py — Réorganise le dépôt modus-uranus selon
SPEC_modus_uranus_populate.md (v3), §6.

USAGE
  python3 reorg_uranus.py            # DRY-RUN : affiche le plan, n'écrit rien
  python3 reorg_uranus.py --apply    # exécute (git mv si possible)
  python3 reorg_uranus.py --apply --aux   # + crée les tables auxiliaires *_couples / *_photos

Garanties : idempotent · ne clobbe jamais (conflits -> "À REVOIR") ·
préserve l'historique git · écrit REORG_REPORT.md + MIGRATION_TODO.md.
À lancer depuis la racine du dépôt.
"""
import os, sys, subprocess, shutil
from pathlib import Path

# ---------------------------------------------------------------- config
POPULATE_DIR = "ia/populate"          # cible SPEC (ex ia/devtool)
LEGACY_DEVTOOL = "ia/devtool"
STD_HEADER = "id,nom,systeme,sous_systeme,X,Y,Z,zone,ref_oe,ref_montee,etat,phase,couple_nm"

# Systèmes mécaniques/physiques (SPEC §1) -> 1 CSV chacun.
# organes_mecaniques.csv = source du GMP (nom conservé, cité dans la SPEC).
SYSTEMS = [
    "transmission", "liaison_sol", "direction", "freinage",
    "echappement", "thermique", "fluides", "habitacle",
    "carrosserie", "securite",
]
GMP_FILE = "organes_mecaniques.csv"   # déjà présent, = groupe_motopropulseur

# Réseaux électriques (SPEC §1). ⊕ = à ajouter.
NETWORKS = [
    "reseau_can", "reseau_lin", "reseau_masse",
    "reseau_eclairage", "reseau_diag",
]

# Tables transverses
CAMERAS_HEADER = ("id,nom,X,Y,Z,cible_X,cible_Y,cible_Z,"
                  "pieces_surbrillance,youtube_url,commentaire")
DERIVED = {
    "budget.csv":       "id,poste,systeme,phase,ref_oe,quantite,prix_unitaire,prix_total,fournisseur,statut",
    "taches.csv":       "id,tache,systeme,phase,priorite,statut,echeance_km,note",
    "fournisseurs.csv": "id,fournisseur,categorie,url,statut,note",
}

# projet/ : fichiers sans extension -> .md (SPEC §6)
PROJET_RENAME = [
    "Budget", "Budget_phase_2", "Entretient", "Entretient_phase_2",
    "Fournisseurs", "Outils", "Outils_audit", "Tache_phase_2", "ct",
]
HTML_SRC, HTML_DST = "modus_3d_interactive.html", "atelier.html"

# ---------------------------------------------------------------- helpers
APPLY = "--apply" in sys.argv
AUX   = "--aux" in sys.argv
ROOT  = Path.cwd()
plan, review, todo = [], [], []

def is_git():
    return (ROOT / ".git").exists()

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def git_tracked(p: Path):
    if not is_git(): return False
    r = run(["git", "ls-files", "--error-unmatch", str(p)])
    return r.returncode == 0

def mv(src: Path, dst: Path, why: str):
    """Déplace/renomme sans jamais écraser. git mv si suivi."""
    if not src.exists():
        return  # rien à faire (idempotent)
    if dst.exists():
        review.append(f"CONFLIT — `{src}` → `{dst}` existe déjà. {why}")
        return
    plan.append(f"MV  {src}  →  {dst}   ({why})")
    if APPLY:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if git_tracked(src):
            r = run(["git", "mv", str(src), str(dst)])
            if r.returncode != 0:
                shutil.move(str(src), str(dst))
        else:
            shutil.move(str(src), str(dst))

def mkdir(p: Path, why: str):
    if p.exists(): return
    plan.append(f"DIR {p}   ({why})")
    if APPLY: p.mkdir(parents=True, exist_ok=True)

def write_stub(p: Path, content: str, why: str):
    if p.exists():
        return  # idempotent : on ne touche pas l'existant
    plan.append(f"NEW {p}   ({why})")
    if APPLY:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content + "\n", encoding="utf-8")

def gitkeep(d: Path):
    write_stub(d / ".gitkeep", "", "garder le dossier vide sous git")

# ---------------------------------------------------------------- 1. ia/devtool -> ia/populate
dev, pop = ROOT / LEGACY_DEVTOOL, ROOT / POPULATE_DIR
if dev.exists() and not pop.exists():
    mv(dev, pop, "ia/devtool -> ia/populate (SPEC §6)")
elif dev.exists() and pop.exists():
    review.append(f"`{LEGACY_DEVTOOL}` ET `{POPULATE_DIR}` coexistent — fusion manuelle requise.")
# à partir d'ici on travaille dans pop/
data, plans = pop / "data", pop / "plans"
mkdir(pop, "dossier outil")
mkdir(data, "CSV par système (SPEC §6)")
mkdir(plans, "schémas RTA/PartSouq")
gitkeep(plans)

# 2. atelier.html
mv(pop / HTML_SRC, pop / HTML_DST, "vue 3D = atelier.html (SPEC §6)")

# 3. CSV existants + générateur -> data/ ; SPEC/readme restent à la racine de pop/
KEEP_AT_ROOT = {"SPEC_modus_uranus_populate.md", "readme.md", "p2p6.py", HTML_DST, "data", "plans"}
if pop.exists():
    for f in sorted(pop.iterdir()):
        if f.is_file() and f.suffix == ".csv":
            mv(f, data / f.name, "CSV -> data/")

# 4. systèmes manquants (schéma TecDoc-like)
for s in SYSTEMS:
    write_stub(data / f"{s}.csv", STD_HEADER, f"système manquant: {s}")
    if AUX:
        write_stub(data / f"{s}_couples.csv", "id,piece_id,couple_nm,methode,note", "table couples")
        write_stub(data / f"{s}_photos.csv",  "id,piece_id,photo,commentaire", "table photos")

# 5. réseaux manquants
for n in NETWORKS:
    write_stub(data / f"{n}.csv", STD_HEADER, f"réseau manquant: {n}")

# 6. transverses
write_stub(data / "cameras.csv", CAMERAS_HEADER, "caméras virtuelles (SPEC §2/§4)")
write_stub(data / "historique.md",
           "# Historique pièces (N-N photo↔pièce)\n\n| piece_id | photo | date | info |\n|---|---|---|---|",
           "métadonnées photos/infos (SPEC §2)")
for fn, hdr in DERIVED.items():
    write_stub(data / fn, hdr, "dérivé des .md projet/ (SPEC §2)")

# 7. photos/ racine (on NE déplace PAS doc/.../photos : c'est la base SOURCE)
mkdir(ROOT / "photos", "photos centralisées (SPEC §6)")
gitkeep(ROOT / "photos")
if (ROOT / "doc").exists():
    todo.append("Décider du rapatriement de `doc/**/photos` vers `/photos` "
                "(doc/ est marqué SOURCE 'ne pas alourdir' dans le README).")

# 8. projet/ : sans extension -> .md (sans clobber)
projet = ROOT / "projet"
if projet.exists():
    for name in PROJET_RENAME:
        mv(projet / name, projet / f"{name}.md", "extension .md (SPEC §6)")

# 9. fichier parasite racine "Finalisation v19"
stray = ROOT / "Finalisation v19"
if stray.exists():
    review.append("`Finalisation v19` (racine, espace dans le nom) — doublon probable "
                  "de `projet/FINALISATION_V19.md`. À vérifier puis archiver/supprimer.")

# 10. flag migration de schéma des CSV legacy
for f in sorted((data).glob("*.csv")) if data.exists() else []:
    try:
        h = f.read_text(encoding="utf-8", errors="ignore").splitlines()[0]
    except Exception:
        continue
    if h.strip() != STD_HEADER and not h.startswith("id,"):
        todo.append(f"Migrer le schéma de `{f.relative_to(ROOT)}` vers : {STD_HEADER}")

# ---------------------------------------------------------------- rapport
def section(title, items):
    out = [f"## {title}", ""]
    out += [f"- {x}" for x in items] if items else ["- (rien)"]
    return "\n".join(out) + "\n"

report = "# REORG_REPORT — modus-uranus populate\n\n"
report += f"Mode : {'APPLY' if APPLY else 'DRY-RUN'}  ·  git : {is_git()}  ·  aux : {AUX}\n\n"
report += section("Plan d'opérations", plan)
report += "\n" + section("⚠️ À REVOIR (non touché)", review)

print(report)
print(f"\n>>> {len(plan)} opérations · {len(review)} à revoir · {len(todo)} TODO migration")
print(">>> DRY-RUN (rien écrit). Relancer avec --apply pour exécuter." if not APPLY
      else ">>> APPLIQUÉ. Vérifier `git status` puis commit.")

if APPLY:
    (ROOT / "REORG_REPORT.md").write_text(report, encoding="utf-8")
    (ROOT / "MIGRATION_TODO.md").write_text(
        "# MIGRATION TODO (post-réorg)\n\n" + section("Schéma & déplacements à finaliser", todo),
        encoding="utf-8")
