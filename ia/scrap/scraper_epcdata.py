# scraper_epcdata.py - Version avec gestion 429, 502, rechargements
import asyncio
import os
import re
import base64
import random
import pandas as pd
from urllib.parse import urljoin
from playwright.async_api import TimeoutError as PlaywrightTimeout, Error as PlaywrightError
from browser import get_browser_context
from pdf_generator import create_a4_plate
from googletrans import Translator

class EpcDataScraper:
    def __init__(self, model_url, output_dir="output/epcdata", max_retries=50, delay=0.5):
        self.base = "https://renault.epc-data.com"
        self.model_url = model_url.rstrip('/') + '/'
        self.output_dir = output_dir
        self.max_retries = max_retries
        self.delay = delay  # délai de base entre les requêtes
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs("temp", exist_ok=True)
        self.all_parts_data = []
        self.translator = Translator()
        self.visited_urls = set()
        self.scheme_urls = set()
        self.detail_urls = set()

    # ------------------------------------------------------------
    #  Requêtes robustes avec gestion des codes HTTP
    # ------------------------------------------------------------
    async def safe_goto(self, url, retry=0):
        if retry >= self.max_retries:
            print(f"❌ Abandon après {self.max_retries} tentatives : {url}")
            return False
        try:
            response = await self.page.goto(url, wait_until="domcontentloaded", timeout=30000)
            if response:
                status = response.status
                if status == 429:
                    wait = 10 * (retry + 1)
                    print(f"⚠️ HTTP 429 (Too Many Requests) sur {url} - attente {wait}s (tentative {retry+1})")
                    await asyncio.sleep(wait)
                    return await self.safe_goto(url, retry + 1)
                elif status >= 500:
                    wait = 5 * (retry + 1)
                    print(f"⚠️ HTTP {status} sur {url} - attente {wait}s (tentative {retry+1})")
                    await asyncio.sleep(wait)
                    return await self.safe_goto(url, retry + 1)

            await self.page.wait_for_load_state("networkidle", timeout=10000)
            content = await self.page.content()
            if any(err in content for err in ["502 Bad Gateway", "504 Gateway Timeout", "429 Too Many Requests"]):
                wait = 5 * (retry + 1)
                print(f"⚠️ Erreur détectée dans le contenu - attente {wait}s (tentative {retry+1})")
                await asyncio.sleep(wait)
                return await self.safe_goto(url, retry + 1)
            return True
        except (PlaywrightError, PlaywrightTimeout) as e:
            err = str(e).lower()
            if any(x in err for x in ["502", "504", "429", "gateway", "timeout"]):
                wait = 5 * (retry + 1)
                print(f"⚠️ Exception {url} - attente {wait}s (tentative {retry+1}) : {e}")
                await asyncio.sleep(wait)
                return await self.safe_goto(url, retry + 1)
            else:
                raise

    async def extract_links(self, selector):
        try:
            await self.page.wait_for_selector(selector, timeout=10000)
        except PlaywrightTimeout:
            return set()
        elements = await self.page.query_selector_all(selector)
        urls = set()
        for el in elements:
            href = await el.get_attribute("href")
            if href and self.model_url in href and not href.startswith("#"):
                urls.add(urljoin(self.base, href))
        return urls

    # ------------------------------------------------------------
    #  Exploration principale
    # ------------------------------------------------------------
    async def scrape(self):
        context, playwright = await get_browser_context(headless=False)
        self.page = await context.new_page()
        try:
            full_url = self.base + self.model_url + "?lang=fr"
            if not await self.safe_goto(full_url):
                return
            if await self.is_captcha_present():
                print("🛡️ CAPTCHA sur la page d'accueil. Attente automatique...")
                await self.wait_for_captcha_solve()

            main_nodes = await self.get_main_nodes()
            print(f"🎯 {len(main_nodes)} grands groupes trouvés.")
            for node_name, node_url in main_nodes:
                print(f"\n📁 Exploration du groupe : {node_name}")
                await self.collect_urls(node_url)

            all_pages = self.scheme_urls.union(self.detail_urls)
            print(f"\n📊 {len(all_pages)} pages uniques à traiter.")
            for idx, url in enumerate(list(all_pages)):
                print(f"   [{idx+1}/{len(all_pages)}] Traitement...")
                await self.extract_page_data(url)
                # Délai aléatoire pour éviter le 429
                await asyncio.sleep(self.delay + random.uniform(0.5, 1.5))

            if self.all_parts_data:
                master_df = pd.concat(self.all_parts_data, ignore_index=True)
                print("📊 Traduction du CSV...")
                master_df = await self.translate_dataframe(master_df)
                csv_path = os.path.join(self.output_dir, "epc_parts.csv")
                master_df.to_csv(csv_path, index=False, encoding='utf-8-sig')
                print(f"✅ Export CSV : {csv_path} ({len(master_df)} lignes)")

        finally:
            await context.close()
            await playwright.stop()

    async def is_captcha_present(self):
        content = await self.page.content()
        return "Just a moment..." in content or "Vérification" in content

    async def wait_for_captcha_solve(self, timeout=30):
        for _ in range(timeout):
            await asyncio.sleep(1)
            if not await self.is_captcha_present():
                return
        print("⚠️ CAPTCHA non résolu automatiquement. Intervention manuelle nécessaire.")
        input("👉 Résolvez-le manuellement dans le navigateur, puis appuyez sur Entrée...")

    async def get_main_nodes(self):
        possible = ["div.content ul li a", "ul li a"]
        for sel in possible:
            try:
                await self.page.wait_for_selector(sel, timeout=5000)
                elements = await self.page.query_selector_all(sel)
                nodes = []
                for el in elements:
                    href = await el.get_attribute("href")
                    text = await el.inner_text()
                    if href and any(x in href for x in ["mechanical", "exterior", "interior"]):
                        nodes.append((text.strip(), urljoin(self.base, href)))
                if nodes:
                    return nodes
            except:
                continue
        print("⚠️ Catégories par défaut")
        return [
            ("Mechanical", self.base + self.model_url + "mechanical/"),
            ("Exterior", self.base + self.model_url + "exterior/"),
            ("Interior", self.base + self.model_url + "interior_and_electric/")
        ]

    async def collect_urls(self, url):
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)
        print(f"   🔍 Analyse : {url}")
        if not await self.safe_goto(url):
            return
        if await self.is_captcha_present():
            await self.wait_for_captcha_solve()

        if re.search(r'/\d{8}/', url):
            self.scheme_urls.add(url)
            return
        if re.search(r'/\d{8}/\d+/?$', url):
            self.detail_urls.add(url)
            return

        selectors = [
            "ul.detail_list li a",
            "div.floatleft ul li a",
            "div.content ul li a",
            "ul:not(.path) li a",
            "a[href*='/']"
        ]
        links = set()
        for sel in selectors:
            links = await self.extract_links(sel)
            if links:
                break
        if not links:
            print(f"      ⚠️ Aucun lien trouvé, sauvegarde HTML")
            with open(f"debug_{abs(hash(url))}.html", "w") as f:
                f.write(await self.page.content())
            return

        for link in links:
            if link not in self.visited_urls:
                await self.collect_urls(link)
                await asyncio.sleep(self.delay)

    # ------------------------------------------------------------
    #  Extraction des données (image + tableau)
    # ------------------------------------------------------------
    async def extract_page_data(self, url):
        print(f"      📄 Extraction : {url}")
        if not await self.safe_goto(url):
            return
        if await self.is_captcha_present():
            await self.wait_for_captcha_solve()

        # Titre traduit
        title_raw = "schéma"
        try:
            h2 = await self.page.query_selector("h2")
            if h2:
                title_raw = await h2.inner_text()
            else:
                bread = await self.page.query_selector("div.path span:last-child")
                if bread:
                    title_raw = await bread.inner_text()
        except:
            pass
        title_fr = await self.translate_text(title_raw)
        title_fr = re.sub(r'[\\/*?:"<>|]', "", title_fr)[:100]

        # Image (uniquement si usemap)
        image_path = None
        img_element = await self.page.query_selector("img[usemap]")
        if img_element:
            img_src = await img_element.get_attribute("src")
            if img_src:
                full_img_url = urljoin(self.base, img_src)
                try:
                    img_data = await self.page.evaluate(f"""
                        async () => {{
                            const resp = await fetch('{full_img_url}');
                            const blob = await resp.blob();
                            return new Promise(resolve => {{
                                const reader = new FileReader();
                                reader.onloadend = () => resolve(reader.result.split(',')[1]);
                                reader.readAsDataURL(blob);
                            }});
                        }}
                    """)
                    image_bytes = base64.b64decode(img_data)
                    if len(image_bytes) > 1024:
                        ext = img_src.split('.')[-1].split('?')[0]
                        if ext.lower() not in ('png', 'jpg', 'jpeg', 'gif'):
                            ext = 'png'
                        temp_path = f"temp/epc_img_{abs(hash(url))}.{ext}"
                        with open(temp_path, 'wb') as f:
                            f.write(image_bytes)
                        image_path = temp_path
                except Exception as e:
                    print(f"         ⚠️ Erreur image : {e}")

        # Tableau des pièces
        df = await self.extract_table()
        if not df.empty:
            df['Schéma'] = title_fr
            df['URL'] = url
            self.all_parts_data.append(df)

        pdf_path = os.path.join(self.output_dir, f"{title_fr}_{abs(hash(url))}.pdf")
        create_a4_plate(image_path, df, pdf_path, title=title_fr)
        print(f"         ✅ PDF : {pdf_path} (pièces : {len(df)})")

        if image_path and os.path.exists(image_path):
            os.remove(image_path)

    async def extract_table(self):
        """Extrait le tableau de pièces, en ajoutant les balises manquantes si besoin."""
        df = pd.DataFrame()
        table_element = await self.page.query_selector("div.btable table, table.btable")
        if table_element:
            table_html = await table_element.inner_html()
            if table_html.strip().startswith("<tbody"):
                table_html = f"<table>{table_html}</table>"
            try:
                tables = pd.read_html(table_html)
                if tables:
                    df = tables[0]
                    df.columns = [str(c).strip() for c in df.columns]
                    df = await self.translate_dataframe(df)
            except Exception as e:
                print(f"         ⚠️ Erreur parsing tableau : {e}")
        else:
            simple_table = await self.page.query_selector("table")
            if simple_table:
                table_html = await simple_table.inner_html()
                try:
                    tables = pd.read_html(f"<tr>{table_html}</table>")
                    if tables:
                        df = tables[0]
                        df.columns = [str(c).strip() for c in df.columns]
                        df = await self.translate_dataframe(df)
                except Exception as e:
                    print(f"         ⚠️ Erreur parsing simple table : {e}")
        return df

    # ------------------------------------------------------------
    #  Traduction
    # ------------------------------------------------------------
    async def translate_text(self, text, src='ru', dest='fr'):
        if not text or not isinstance(text, str) or len(text.strip()) == 0:
            return text
        try:
            translation = await asyncio.to_thread(self.translator.translate, text, src=src, dest=dest)
            return translation.text
        except Exception as e:
            return text

    async def translate_dataframe(self, df):
        if df.empty:
            return df
        text_cols = [c for c in df.columns if any(k in c.lower() for k in ['name', 'nom', 'description', 'title'])]
        if not text_cols:
            text_cols = [c for c in df.columns if df[c].dtype == 'object']
        for col in text_cols:
            translated = []
            for val in df[col]:
                if isinstance(val, str) and val.strip():
                    translated.append(await self.translate_text(val))
                else:
                    translated.append(val)
            df[col] = translated
        return df
