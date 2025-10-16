# preview_crawler.py
import requests
from bs4 import BeautifulSoup
import json

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_westelm(limit=3):
    """Fetch a few products from West Elm new arrivals safely."""
    url = "https://www.westelm.com/shop/new/"
    products = []

    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        scripts = soup.find_all("script", type="application/ld+json")

        for s in scripts[:limit]:
            data = json.loads(s.string)
            if isinstance(data, dict) and data.get("@type") == "Product":
                products.append({
                    "name": data.get("name"),
                    "url": data.get("url"),
                    "image": data.get("image"),
                    "price": data.get("offers", {}).get("price"),
                    "currency": data.get("offers", {}).get("priceCurrency")
                })
    except Exception as e:
        print("West Elm fetch failed, using sample data:", e)
        products = [{"name": "Sample Chair", "price": "199", "url": "#", "image": ""}]
    
    return products

def fetch_wayfair(limit=3):
    """Fetch a few products from Wayfair new arrivals safely."""
    url = "https://www.wayfair.com/furniture/cat/new-arrivals-c45974.html"
    products = []

    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        scripts = soup.find_all("script", type="application/ld+json")

        for s in scripts[:limit]:
            data = json.loads(s.string)
            if isinstance(data, dict) and data.get("@type") == "Product":
                products.append({
                    "name": data.get("name"),
                    "url": data.get("url"),
                    "image": data.get("image"),
                    "price": data.get("offers", {}).get("price"),
                    "currency": data.get("offers", {}).get("priceCurrency")
                })
    except Exception as e:
        print("Wayfair fetch failed, using sample data:", e)
        products = [{"name": "Sample Table", "price": "299", "url": "#", "image": ""}]

    return products
