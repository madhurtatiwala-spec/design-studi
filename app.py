# app.py
import streamlit as st
from preview_crawler import fetch_westelm, fetch_wayfair

st.title("Design Studi — Live Furniture Preview")

st.header("West Elm New Arrivals")
westelm_products = fetch_westelm()
for p in westelm_products:
    st.image(p.get("image") or "https://via.placeholder.com/150", width=200)
    st.markdown(f"[{p['name']}]({p['url']}) - {p.get('currency','USD')} {p['price']}")

st.header("Wayfair New Arrivals")
wayfair_products = fetch_wayfair()
for p in wayfair_products:
    st.image(p.get("image") or "https://via.placeholder.com/150", width=200)
    st.markdown(f"[{p['name']}]({p['url']}) - {p.get('currency','USD')} {p['price']}")
