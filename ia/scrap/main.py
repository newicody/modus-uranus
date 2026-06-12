# main.py
import asyncio
import os
from PyPDF2 import PdfMerger
from scraper_partsouq import PartsouqScraper
from scraper_epcdata import EpcDataScraper

async def main():
    # 1. Partsouq - exemple avec le lien Renault fourni
    #    partsouq_url = "https://partsouq.com/fr/catalog/genuine/vehicle?c=Renault&ssd=%24%2AKwHL_-7TtcmQu6C8qsjF45OHp6C-z8DNzN7xwoqMv6u3s7Gy9-DMpoiMiLmvtqfh_PbLwrKRnY2Mg9fHgLnLxs7BysnMlZgAAAAAnaCGbg%3D%3D%24&vid=0&q="
    #ps_scraper = PartsouqScraper(partsouq_url, output_dir="output/partsouq")
    #await ps_scraper.scrape()

    # 2. EPC-Data - exemple Modus
    epc_model = "/modus/16198/"
    epc_scraper = EpcDataScraper(epc_model, output_dir="output/epcdata")
    await epc_scraper.scrape()

    # 3. Fusionner tous les PDF en un seul (optionnel)
    all_pdfs = []
    for root, _, files in os.walk("output"):
        for f in files:
            if f.endswith(".pdf"):
                all_pdfs.append(os.path.join(root, f))
    if all_pdfs:
        merger = PdfMerger()
        for pdf in sorted(all_pdfs):
            merger.append(pdf)
        merger.write("catalogue_complet.pdf")
        merger.close()
        print(f"Catalogue fusionné : catalogue_complet.pdf ({len(all_pdfs)} planches)")

if __name__ == "__main__":
    print("Démarrage du scraping...")
    print("Ouvrez le navigateur, résolvez le captcha si nécessaire, puis laissez tourner.")
    asyncio.run(main())
