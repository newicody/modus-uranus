# scraper_partsouq.py (version finale sans clics)
import asyncio
import os
import re
import base64
import pandas as pd
from urllib.parse import urljoin
from playwright.async_api import TimeoutError as PlaywrightTimeout
from browser import get_browser_context, prepare_browser_for_site
from pdf_generator import create_a4_plate

class PartsouqScraper:
    def __init__(self, start_url, output_dir="output/partsouq"):
        self.start_url = start_url
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs("temp", exist_ok=True)
        self.all_parts_data = []

    async def scrape(self):
        context, playwright = await get_browser_context(headless=False)
        self.page = await context.new_page()
        try:
            await prepare_browser_for_site(self.page, "https://partsouq.com/fr/", "Partsouq")
            await self.page.goto(self.start_url, wait_until="domcontentloaded", timeout=60000)

            # Gestion CAPTCHA initial
            if await self.page.locator("text=Vérification").count() > 0:
                print("🛡️ CAPTCHA Cloudflare détecté.")
                print("👉 Résolvez-le manuellement, puis Entrée.")
                input()
                await self.page.wait_for_timeout(2000)

            # Attente du menu
            print("Attente du chargement du menu...")
            await self.page.wait_for_selector("table.tree-open", timeout=60000)
            print("Menu chargé.")

            # Collecte des URLs de catégories
            detail_urls = await self.collect_all_detail_urls_corrected()
            print(f"\n✅ {len(detail_urls)} planches uniques trouvées.")

            for idx, url in enumerate(detail_urls):
                print(f"\n[{idx+1}/{len(detail_urls)}] {url[:80]}...")
                try:
                    await self.process_detail_page(context, url)
                except Exception as e:
                    print(f"  Erreur : {e}")
                    continue
                await asyncio.sleep(2)

            # Export CSV
            if self.all_parts_data:
                master_df = pd.concat(self.all_parts_data, ignore_index=True)
                csv_path = os.path.join(self.output_dir, "parts_positions.csv")
                master_df.to_csv(csv_path, index=False, encoding='utf-8-sig')
                print(f"\nExport CSV : {csv_path} ({len(master_df)} lignes)")

        finally:
            await context.close()
            await playwright.stop()

    async def collect_all_detail_urls_corrected(self):
        """Collecte toutes les URLs des planches sans cliquer dans l'arborescence."""
        all_detail_urls = set()
        category_urls = set()

        # Récupérer tous les liens de catégorie depuis la table du menu
        print("📁 Récupération de tous les liens de catégorie...")
        category_links = await self.page.locator("table.tree-open tbody tr td a").all()
        for link in category_links:
            href = await link.get_attribute("href")
            if href and "vehicle?" in href:   # Filtrer les vraies catégories
                full_url = urljoin("https://partsouq.com", href)
                category_urls.add(full_url)

        print(f"🔗 {len(category_urls)} catégories uniques trouvées.")

        # Parcourir chaque catégorie
        for idx, cat_url in enumerate(category_urls):
            print(f"🌐 [{idx+1}/{len(category_urls)}] Catégorie : {cat_url[:80]}...")
            try:
                await self.page.goto(cat_url, wait_until="domcontentloaded", timeout=30000)

                # Vérifier CAPTCHA
                content = await self.page.content()
                if "Just a moment..." in content or "Vérification" in content:
                    print("   ☁️ CAPTCHA détecté, résolution manuelle nécessaire.")
                    input("   Appuyez sur Entrée après résolution...")
                    await self.page.wait_for_timeout(2000)

                # Extraire les planches
                urls = await self.get_visible_detail_urls()
                avant = len(all_detail_urls)
                all_detail_urls.update(urls)
                nouvelles = len(all_detail_urls) - avant
                print(f"   ✅ +{nouvelles} planches (total unique: {len(all_detail_urls)})")

                await asyncio.sleep(1)  # Politesse
            except Exception as e:
                print(f"   ⚠️ Erreur : {e}")
                continue

        print(f"\n📊 STATS FINALES: {len(all_detail_urls)} planches uniques")
        return list(all_detail_urls)

    async def get_visible_detail_urls(self):
        """Récupère les URLs des planches sur la page courante."""
        urls = set()
        try:
            await self.page.wait_for_selector("div.thumbnail-col h5 a", timeout=5000)
            links = self.page.locator("div.thumbnail-col h5 a")
            count = await links.count()
            for i in range(count):
                href = await links.nth(i).get_attribute("href")
                if href and 'unit?' in href:
                    full_url = urljoin("https://partsouq.com", href)
                    urls.add(full_url)
        except PlaywrightTimeout:
            pass  # Pas de planches, ce n'est pas grave
        except Exception as e:
            print(f"  Warning get_visible_detail_urls: {e}")
        return urls

    async def process_detail_page(self, context, url):
        # Identique à votre version existante (je ne le répète pas pour la lisibilité)
        # ... (conservez votre méthode process_detail_page inchangée)
        pass  # À remplacer par votre code existant
