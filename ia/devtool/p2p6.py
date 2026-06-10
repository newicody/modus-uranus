import os
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.offline as op

BASE_DIR = '/media/eric/modus/p2p/'
CSV_FILES = {
    "Réseau FTTH/Telecom": "sensors.csv",
    "Alimentation 12V (Batterie)": "reseau_12v.csv",
    "Hybride 48V (iBSG Belt)": "reseau_48v.csv",
    "USB 5V (Recharge Tél)": "reseau_5v_usb.csv",
    "5V Spécial (MegaDrive & ESP32)": "reseau_5v_glovebox.csv",
    "Capteurs 3.3V (Roue Secours)": "reseau_3v3.csv",
    "Organes Mécaniques (Bloc Moteur)": "organes_mecaniques.csv"
}

# Nomenclature Réseau Type Télécom
ORIGINS = {
    "SR-MOT-01": {"coord": np.array([45, 0, 80]), "desc": "Sous-Répartiteur Moteur (PDU/Fusibles Compartiment Avant)"},
    "SR-CHAS-02": {"coord": np.array([60, -55, 45]), "desc": "Sous-Répartiteur Châssis (Centrale de Trajectoire ABS/ESP)"},
    "SR-HAB-03": {"coord": np.array([180, 0, 45]), "desc": "Sous-Répartiteur Habitacle (Platine de Servitude UCH)"},
    "DIS-BAT-12V": {"coord": np.array([45, -25, 70]), "desc": "Distribution Énergie Basse Tension - Batterie Plomb 12V"},
    "DIS-HYB-48V": {"coord": np.array([240, 0, 35]), "desc": "Distribution Puissance iBSG & Pack Hybride 48V Engine-Belt"},
    "SR-SPEC-5V": {"coord": np.array([130, 45, 70]), "desc": "Sous-Répartiteur Régulé 5V (Hub Boîte à Gants Sega & IoT)"},
    "SR-COF-3V3": {"coord": np.array([340, 0, 20]), "desc": "Sous-Répartiteur Instrumentation Basse Puissance 3.3V Fond de Coffre"},
    "MOTEUR": {"coord": np.array([35, 0, 65]), "desc": "Bloc d'Ancrage Mécanique Principal - Moteur K9K dCi"}
}
NRO_CENTER = np.array([120, 0, 75])

CABLE_SPECIFICATIONS = {
    "Réseau FTTH/Telecom": "Fibre Optique Monomode G657.A2 Structure Serrée (Média FTTH)",
    "Alimentation 12V (Batterie)": "Cuivre Multibrins Auto ISO 6722 Class B Gaine PVC Haute Densité",
    "Hybride 48V (iBSG Belt)": "Faisceau Blindé Orange Haute Tension 16mm² (Norme Automobile EMC Shield)",
    "USB 5V (Recharge Tél)": "Câble AWG24/2C + AWG28/2P Gaine PVC Flexible (Standard USB Shielded)",
    "5V Spécial (MegaDrive & ESP32)": "Paire Torsadée Blindée (STP) Cuivre Étamé Écran Alu Anti-Parasites",
    "Capteurs 3.3V (Roue Secours)": "Bus Souple Filaire LiYY 4x0.25mm² Instrumentation (Liaisons I2C/SPI)",
    "Organes Mécaniques (Bloc Moteur)": "Tresse Cuivre Haute Capacité Masse 25mm² / Liaisons Rigides Acier"
}

NETWORK_STYLES = {
    "Réseau FTTH/Telecom": "solid", "Alimentation 12V (Batterie)": "dash", "Hybride 48V (iBSG Belt)": "longdash",
    "USB 5V (Recharge Tél)": "dot", "5V Spécial (MegaDrive & ESP32)": "dashdot", "Capteurs 3.3V (Roue Secours)": "longdashdot",
    "Organes Mécaniques (Bloc Moteur)": "solid"
}

SUBNET_COLORS = {
    "SR-MOT-01": "#FF4136", "SR-CHAS-02": "#7FDBFF", "SR-HAB-03": "#0074D9",
    "DIS-BAT-12V": "#FF851B", "DIS-HYB-48V": "#B10DC9", "SR-SPEC-5V": "#F012BE",
    "SR-COF-3V3": "#39CCCC", "MOTEUR": "#AAAAAA"
}

COLUMNS = ["X", "Y", "Z", "Nom", "PMZ", "Ref_OE", "Type_Cable", "Origine_Signal", "Fonction"]

fig = go.Figure()

# --- 1. GABARIT CHÂSSIS (Trace 0) ---
fig.add_trace(go.Mesh3d(
    x=[0, 80, 140, 260, 380, 380, 260, 140, 80, 0, 0, 80, 140, 260, 380, 380, 260, 140, 80, 0],
    y=[85, 85, 85, 85, 60, -60, -85, -85, -85, -85, -85, -85, -85, -85, -60, 60, 85, 85, 85, 85],
    z=[40, 85, 160, 160, 85, 85, 160, 160, 85, 40, 40, 85, 160, 160, 85, 85, 160, 160, 85, 40],
    opacity=0.03, color="grey", name="Châssis Modus", hoverinfo="skip"
))

# --- 2. NŒUDS INFRASTRUCTURE (Trace 1) ---
node_x, node_y, node_z, node_text, node_custom = [NRO_CENTER[0]], [NRO_CENTER[1]], [NRO_CENTER[2]], ["NRO-UC (Unité Centrale Maître / UCH Delphi)"], [["Calculateur Maître", "Faisceau Inter-Réseaux", "Routage Multiplexé", "Gestionnaire de trames"]]
for name, info in ORIGINS.items():
    node_x.append(info["coord"][0])
    node_y.append(info["coord"][1])
    node_z.append(info["coord"][2])
    node_text.append(name)
    node_custom.append(["Boîtier Nœud Infra", "N/A structural", name, info["desc"]])

fig.add_trace(go.Scatter3d(
    x=node_x, y=node_y, z=node_z, mode='markers',
    marker=dict(size=10, color='gold', symbol='diamond', line=dict(color='black', width=1.5)),
    text=node_text, customdata=np.array(node_custom),
    hovertemplate="<b>Nœud Réseau :</b> %{text}<br><extra></extra>",
    name="Nodes_Infra"
))

# Indexation dynamique des traces (0: Châssis, 1: Nœuds)
trace_counter = 2
menu_structure = {}

# --- 3. CHARGEMENT ET CALCUL DES INDEX DE TRACES ---
for net_name, filename in CSV_FILES.items():
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        continue
    df = pd.read_csv(path)
    
    if net_name not in menu_structure:
        menu_structure[net_name] = {}
        
    for subnet_id, group in df.groupby("PMZ"):
        color = SUBNET_COLORS.get(subnet_id, "#FFFFFF")
        dash_style = NETWORK_STYLES.get(net_name, "solid")
        
        # AJOUT TRACE LIGNE (Câbles)
        x_lines, y_lines, z_lines = [], [], []
        for idx, row in group.iterrows():
            if subnet_id in ORIGINS:
                start = ORIGINS[subnet_id]["coord"]
                x_lines.extend([start[0], row["X"], None])
                y_lines.extend([start[1], row["Y"], None])
                z_lines.extend([start[2], row["Z"], None])
                
        fig.add_trace(go.Scatter3d(
            x=x_lines, y=y_lines, z=z_lines, mode='lines',
            line=dict(color=color, width=2.5, dash=dash_style),
            name=f"Line || {net_name} || {subnet_id}", hoverinfo='skip', showlegend=False
        ))
        trace_counter += 1  # Incrément pour la ligne
        
        # AJOUT TRACE POINTS (Équipements / Abonnés)
        c_matrix = np.stack((group['Ref_OE'].fillna('N/A'), group['Type_Cable'].fillna('N/A'), group['Origine_Signal'].fillna('N/A'), group['Fonction'].fillna('N/A')), axis=-1)
        fig.add_trace(go.Scatter3d(
            x=group["X"], y=group["Y"], z=group["Z"], mode='markers',
            marker=dict(size=5.5, color=color, symbol='circle', line=dict(color='black', width=0.4)),
            text=group["Nom"], customdata=c_matrix,
            hovertemplate="<b>Composant :</b> %{text}<br><extra></extra>",
            name=f"Point || {net_name} || {subnet_id}", showlegend=False
        ))
        
        point_trace_idx = trace_counter
        trace_counter += 1  # Incrément pour le point
        
        # Remplissage de l'arborescence pour l'interface HTML
        menu_structure[net_name][subnet_id] = {"color": color, "elements": []}
        
        for p_idx, (_, row) in enumerate(group.iterrows()):
            menu_structure[net_name][subnet_id]["elements"].append({
                "nom": str(row["Nom"]).replace('"', '&quot;'),
                "ref": str(row["Ref_OE"]).replace('"', '&quot;'),
                "cable": str(row["Type_Cable"]).replace('"', '&quot;'),
                "origin": str(row["Origine_Signal"]).replace('"', '&quot;'),
                "func": str(row["Fonction"]).replace('"', '&quot;'),
                "trace_idx": point_trace_idx,
                "point_idx": p_idx
            })

fig.update_layout(
    scene=dict(
        xaxis=dict(title='Longueur (cm)', range=[0, 400]),
        yaxis=dict(title='Largeur (cm)', range=[-100, 100]),
        zaxis=dict(title='Hauteur (cm)', range=[0, 180]),
        aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.9)
    ),
    margin=dict(r=0, l=0, b=0, t=0), showlegend=False
)

plotly_div = op.plot(fig, output_type='div', include_plotlyjs=False)

# --- 4. CONSTRUCTION DE L'ARBORESCENCE HTML AVEC CAPTEURS ---
menu_html = ""
for net, subnets_dict in menu_structure.items():
    menu_html += f"""
    <details class="mb-2 bg-slate-800 rounded-lg border border-slate-700 overflow-hidden">
        <summary class="p-3 cursor-pointer font-bold text-xs text-slate-200 uppercase tracking-wider bg-slate-800/50 hover:bg-slate-700 transition flex justify-between items-center">
            <span>{net}</span>
            <span class="text-[10px] text-slate-400 bg-slate-900 px-2 py-0.5 rounded-full">{len(subnets_dict)} S/R</span>
        </summary>
        <div class="p-2 bg-slate-900/40 space-y-2 border-t border-slate-800">
    """
    for sub, data in subnets_dict.items():
        menu_html += f"""
        <div class="bg-slate-950/60 p-2 rounded border border-slate-800">
            <label class="flex items-center space-x-2 text-xs text-slate-300 font-bold cursor-pointer hover:text-white transition pb-1 mb-1 border-b border-slate-900">
                <input type="checkbox" checked class="subnet-toggle rounded border-slate-700 bg-slate-800 text-indigo-500 focus:ring-0" data-net="{net}" data-sub="{sub}">
                <span class="w-2.5 h-2.5 rounded-full inline-block" style="background-color: {data['color']};"></span>
                <span class="font-mono text-[10px]">{sub}</span>
            </label>
            <div class="space-y-0.5 pt-1 pl-1">
        """
        for el in data["elements"]:
            menu_html += f"""
                <div class="element-locator flex items-center justify-between text-[11px] text-slate-400 hover:text-indigo-400 cursor-pointer transition py-0.5 px-1 rounded hover:bg-slate-900" 
                     data-trace="{el['trace_idx']}" data-point="{el['point_idx']}" data-nom="{el['nom']}" data-ref="{el['ref']}" data-cable="{el['cable']}" data-origin="{el['origin']}" data-func="{el['func']}">
                    <span class="truncate max-w-[210px]">⊙ {el['nom']}</span>
                    <span class="text-[8px] font-black tracking-widest text-slate-500 bg-slate-800 px-1 py-0.2 rounded uppercase hover:bg-indigo-950 hover:text-indigo-300">Loc</span>
                </div>
            """
        menu_html += "</div></div>"
    menu_html += "</div></details>"

# --- 5. INTERFACE CLIENT (GABARIT SANS INTERFÉRENCE AVEC LES ACCOLADES PYTHON) ---
html_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Dashboard Multi-Réseaux Cyber-Modus</title>
    <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans overflow-hidden w-screen h-screen flex">

    <div class="w-[380px] h-full bg-slate-900 border-r border-slate-800 flex flex-col justify-between p-4 z-50 shadow-2xl shrink-0">
        <div class="flex flex-col flex-1 min-h-0">
            <div class="mb-4">
                <h1 class="text-lg font-black tracking-tight text-white flex items-center space-x-2">
                    <span class="bg-indigo-600 px-2 py-0.5 rounded text-xs font-mono">V5.0</span>
                    <span>CYBER-MODUS INFRA</span>
                </h1>
                <p class="text-[11px] text-slate-400 mt-1">Cliquez sur un composant pour le localiser en 3D</p>
            </div>
            
            <div class="flex-1 overflow-y-auto pr-1 custom-scrollbar">
                <h2 class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-2">Composants par Sous-Répartiteur</h2>
                __MENU_HTML__
            </div>
        </div>
        
        <div class="mt-4 bg-slate-950 rounded-xl p-4 border border-slate-800 h-[260px] flex flex-col justify-between shadow-inner">
            <div>
                <div class="text-[10px] font-bold text-indigo-400 uppercase tracking-widest mb-1">Fiche d'Information Matériel</div>
                <h3 id="info-title" class="text-xs font-bold text-white truncate">Sélectionnez un élément à gauche...</h3>
            </div>
            
            <div class="space-y-1.5 flex-1 mt-3 overflow-y-auto text-[11px] text-slate-300">
                <div class="flex justify-between border-b border-slate-900 pb-1"><span class="text-slate-500">Réf Constructeur / OE :</span><span id="info-ref" class="font-mono text-white text-[10px]">--</span></div>
                <div class="flex flex-col border-b border-slate-900 pb-1"><span class="text-slate-500">Média (Type de câble) :</span><span id="info-cable" class="text-indigo-200 text-[10px] font-medium mt-0.5">--</span></div>
                <div class="flex justify-between border-b border-slate-900 pb-1"><span class="text-slate-500">Nœud Source :</span><span id="info-origin" class="font-mono text-emerald-400 text-[10px]">--</span></div>
                <div class="mt-1"><span class="text-slate-500 block mb-0.5">Rôle & Spécification :</span><p id="info-function" class="text-slate-400 italic leading-relaxed text-[10px]">En attente d'interaction.</p></div>
            </div>
        </div>
    </div>

    <div class="flex-1 h-full relative bg-slate-950">
        __PLOTLY_DIV__
    </div>

    <script>
        window.addEventListener('DOMContentLoaded', (event) => {
            const plotDiv = document.getElementsByClassName('plotly-graph-div')[0];
            const graphId = plotDiv.id;
            const gd = document.getElementById(graphId);

            // 1. FILTRAGE ET MASQUAGE DYNAMIQUE DE TRACES
            document.querySelectorAll('.subnet-toggle').forEach(box => {
                box.addEventListener('change', function() {
                    const net = this.getAttribute('data-net');
                    const sub = this.getAttribute('data-sub');
                    const isVisible = this.checked;

                    const targetNames = [
                        `Line || ${net} || ${sub}`,
                        `Point || ${net} || ${sub}`
                    ];

                    const indices = [];
                    for(let i=0; i < gd.data.length; i++) {
                        if(targetNames.includes(gd.data[i].name)) {
                            indices.push(i);
                        }
                    }
                    if(indices.length > 0) {
                        Plotly.restyle(gd, { visible: isVisible ? true : 'legendonly' }, indices);
                    }
                });
            });

            // 2. RECHERCHE ET LOCALISATION DEPUIS LA LISTE DE GAUCHE
            document.querySelectorAll('.element-locator').forEach(item => {
                item.addEventListener('click', function() {
                    const tIdx = parseInt(this.getAttribute('data-trace'));
                    const pIdx = parseInt(this.getAttribute('data-point'));
                    
                    // Remplissage immédiat de l'infobox statique de gauche
                    document.getElementById('info-title').innerText = this.getAttribute('data-nom');
                    document.getElementById('info-ref').innerText = this.getAttribute('data-ref');
                    document.getElementById('info-cable').innerText = this.getAttribute('data-cable');
                    document.getElementById('info-origin').innerText = this.getAttribute('data-origin');
                    document.getElementById('info-function').innerText = this.getAttribute('data-func');
                    
                    // Déclenchement de l'infobulle éphémère en lévitation 3D
                    Plotly.Fx.hover(gd, [
                        { curveNumber: tIdx, pointNumber: pIdx }
                    ], 'scene');
                });
            });

            // 3. SYNCHRONISATION DU HOVER SOURIS (3D -> Gauche)
            gd.on('plotly_hover', function(data) {
                if(data.points && data.points[0]) {
                    const pts = data.points[0];
                    if(pts.text && pts.customdata && pts.customdata.length >= 4) {
                        document.getElementById('info-title').innerText = pts.text;
                        document.getElementById('info-ref').innerText = pts.customdata[0];
                        document.getElementById('info-cable').innerText = pts.customdata[1];
                        document.getElementById('info-origin').innerText = pts.customdata[2];
                        document.getElementById('info-function').innerText = pts.customdata[3];
                    }
                }
            });
        });
    </script>
</body>
</html>
"""

full_html = html_template.replace("__MENU_HTML__", menu_html).replace("__PLOTLY_DIV__", plotly_div)

output_html = os.path.join(BASE_DIR, 'modus_3d_interactive.html')
with open(output_html, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"\n[SUCCÈS] Intégration terminée. Les liaisons bidirectionnelles sont opérationnelles.")
print(f"-> Fichier disponible : {output_html}")
