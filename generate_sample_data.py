# generate_sample_data.py
import pandas as pd
import random
from datetime import datetime, timedelta
import os

SAMPLE_TITLES = [
    'Mid-century Boucle Armchair', 'Scandi Oak Coffee Table',
    'Rattan Accent Chair', 'Velvet Sofa with Curves',
    'Industrial Metal Bookshelf', 'Minimalist Platform Bed'
]
SITES = ['West Elm']
CATEGORIES = ['Seating', 'Tables', 'Storage', 'Beds']
COLORS = ['#D99A6C','#E6AACE','#544C3F','#F2E8D5','#7B3F00','#C6D8D3']
TAGS = ['mid-century, boucle, accent','scandi, oak, natural','rattan, boho, sustainable','velvet, luxe, curved','industrial, metal, rustic']

def ensure_sample_data(path='sample_data.csv'):
    if os.path.exists(path):
        return
    rows = []
    now = datetime.utcnow()
    for i in range(40):
        rows.append({
            'product_id': f'P{i+1}',
            'site': random.choice(SITES),
            'title': random.choice(SAMPLE_TITLES),
            'category': random.choice(CATEGORIES),
            'price': round(random.uniform(49,1299),2),
            'currency': 'USD',
            'url': '',
            'image_url': '',
            'dominant_color': random.choice(COLORS),
            'tags': random.choice(TAGS),
            'scraped_at': (now - timedelta(days=random.randint(0,7))).isoformat(),
            'trend_score': random.uniform(0,100)
        })
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    print("Sample data generated at", path)
