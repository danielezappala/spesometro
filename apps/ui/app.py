import os
import requests
import streamlit as st

st.set_page_config(page_title="Spesometro", layout="centered")
st.title("Spesometro (MVP)")

api_url = os.getenv("SPESOMETRO_API_URL", "http://localhost:8000")

st.caption(f"API: {api_url}")

if st.button("Check API"):
    try:
        r = requests.get(f"{api_url}/health", timeout=3)
        st.success(r.json())
    except Exception as e:
        st.error(f"API non raggiungibile: {e}")

st.divider()
st.subheader("Upload scontrino (placeholder)")
st.file_uploader("Carica una foto dello scontrino", type=["jpg", "jpeg", "png"])
