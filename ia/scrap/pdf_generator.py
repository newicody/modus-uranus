# pdf_generator.py
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Image, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
import pandas as pd

# Enregistrer une police qui supporte les caractères français
try:
    pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))
    FONT_NAME = 'DejaVu'
except:
    FONT_NAME = 'Helvetica'

def create_a4_plate(image_path, df_parts, output_pdf, title="Schéma"):
    doc = SimpleDocTemplate(output_pdf, pagesize=A4,
                            leftMargin=15*mm, rightMargin=15*mm,
                            topMargin=15*mm, bottomMargin=15*mm)
    elements = []
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CenterTitle', parent=styles['Title'], alignment=1, fontName=FONT_NAME))

    # Style pour les cellules avec wrapping automatique
    cell_style = ParagraphStyle(
        'CellStyle',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=7,
        leading=9,
        alignment=0,
        wordWrap='CJK'  # meilleur pour le français
    )

    # Titre
    elements.append(Paragraph(f"<b>{title}</b>", styles['CenterTitle']))
    elements.append(Spacer(1, 5*mm))

    # Image
    if image_path and os.path.exists(image_path):
        try:
            pil_img = PILImage.open(image_path)
            img_width, img_height = pil_img.size
            max_width = 170 * mm
            max_height = 120 * mm
            if img_width > max_width:
                ratio = max_width / img_width
                img_width = max_width
                img_height = img_height * ratio
            if img_height > max_height:
                ratio = max_height / img_height
                img_height = max_height
                img_width = img_width * ratio
            img = Image(image_path, width=img_width, height=img_height)
            elements.append(img)
            elements.append(Spacer(1, 5*mm))
        except Exception as e:
            elements.append(Paragraph(f"Erreur chargement image : {e}", styles['Normal']))
    else:
        elements.append(Paragraph("Aucune image disponible", styles['Normal']))
        elements.append(Spacer(1, 5*mm))

    # Tableau
    if not df_parts.empty:
        df = df_parts.head(40)  # limiter pour éviter overflow
        # Convertir en Paragraphs
        header_cells = [Paragraph(f"<b>{h}</b>", cell_style) for h in df.columns]
        data = [header_cells]
        for _, row in df.iterrows():
            row_cells = []
            for val in row:
                text = str(val).replace('\n', '<br/>') if val else ''
                row_cells.append(Paragraph(text, cell_style))
            data.append(row_cells)

        # Largeur des colonnes : répartition égale
        col_widths = [doc.width / len(df.columns)] * len(df.columns)
        table = Table(data, colWidths=col_widths, repeatRows=1, splitByRow=True)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), FONT_NAME),
            ('FONTSIZE', (0, 0), (-1, 0), 8),
            ('FONTSIZE', (0, 1), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEADING', (0, 0), (-1, -1), 9),
        ]))
        elements.append(table)
    else:
        elements.append(Paragraph("Aucune nomenclature extraite.", styles['Normal']))

    doc.build(elements)
