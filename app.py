# app.py
import streamlit as st
import pandas as pd
from preview_crawler import fetch_westelm_data
from generate_sample_data import ensure_sample_data
from PIL import Image
import requests
from io import BytesIO
from collections import Counter

st.set_page_config(page_title="Design Studi", layout="wide")
st.title("Design Studi — Furniture Trend Monitor (West Elm Preview)")

# Sidebar
st.sidebar.header("Options")
use_live = st.sidebar.checkbox("Fetch live West Elm data", value=True)

# Load data
if use_live:
    df = fetch_westelm_data()
    if df.empty:
        st.warning("Live fetch failed, using sample data.")
        ensure_sample_data("sample_data.csv")
        df = pd.read_csv("sample_data.csv")
else:
    ensure_sample_data("sample_data.csv")
    df = pd.read_csv("sample_data.csv")

# Show top trending products
st.subheader("Top Products (preview)")
top_products = df.sort_values("trend_score", ascending=False).head(6)
cols = st.columns(3)
for i, (_, p) in enumerate(top_products.iterrows()):
    c = cols[i % 3]
    with c:
        st.markdown(f"**{p['title']}**")
        st.write(f"${p['price']}")
        st.write(p['url'])
        if pd.notna(p.get('image_url','')) and p['image_url']:
            try:
                response = requests.get(p['image_url'])
                img = Image.open(BytesIO(response.content))
                st.image(img, width=200)
            except:
                st.markdown("[Image load failed]")
        else:
            st.markdown("[No image]")

# Color palette analysis
st.subheader("Dominant Colors")
colors = df['dominant_color'].dropna().tolist()
color_counts = Counter(colors)
for color, count in color_counts.most_common(6):
    st.markdown(f"{color} — {count} items")
    st.markdown(f"<div style='width:120px;height:30px;background:{color};border:1px solid #ddd'></div>", unsafe_allow_html=True)

# Trend tags
st.subheader("Trending Design Tags")
tags_list = df['tags'].dropna().tolist()
all_tags = []
for t in tags_list:
    all_tags.extend([tag.strip() for tag in t.split(",")])
tag_counts = Counter(all_tags)
for tag, count in tag_counts.most_common(10):
    st.write(f"{tag} — {count}")

# Export weekly digest
st.subheader("Download Weekly Digest")
st.download_button("Download CSV digest", data=df.to_csv(index=False), file_name="weekly_digest.csv")
