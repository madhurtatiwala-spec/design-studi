# preview_crawler.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

def fetch_westelm_data():
    url = "https://www.westelm.com/shop/furniture/new/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        products = soup.select(".product-card")
        data = []
        for prod in products[:10]:  # limit to 10 products for preview
            title = prod.select_one(".product-card-title")
            price = prod.select_one(".product-card-price")
            link = prod.select_one("a")
            img = prod.select_one("img")
            data.append({
                "title": title.get_text(strip=True) if title else "No title",
                "price": float(price.get_text(strip=True).replace("$","").replace(",","")) if price else random.randint(100,1000),
                "url": "https://www.westelm.com" + link.get("href") if link else "",
                "image_url": img.get("src") if img else "",
                "dominant_color": random.choice(["#D99A6C","#E6AACE","#544C3F","#F2E8D5","#7B3F00","#C6D8D3"]),
                "tags": random.choice(["mid-century, boucle, accent","scandi, oak, natural","rattan, boho, sustainable","velvet, luxe, curved","industrial, metal, rustic"]),
                "trend_score": random.uniform(0,100)
            })
        return pd.DataFrame(data)
    except Exception as e:
        print("Crawler failed:", e)
        return pd.DataFrame()
