# browser.py
import asyncio
from time import sleep
from playwright.async_api import async_playwright

USER_DATA_DIR = "./browser_profile"

async def get_browser_context(headless=False):
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=headless,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
        ],
        viewport={"width": 1920, "height": 1080}
    )
    return browser, playwright

async def prepare_browser_for_site(page, site_home_url, site_name="le site"):
    """Navigue vers la page d'accueil, demande à l'utilisateur de résoudre le captcha."""
    await page.goto(site_home_url, wait_until="domcontentloaded", timeout=30000)
    print(f"\n=== {site_name} ===")
    print("Résolvez le captcha dans la fenêtre du navigateur,")
    sleep(10)
    # Attendre un peu que la page se stabilise
    await page.wait_for_timeout(2000)
