import streamlit as st
import random

st.set_page_config(page_title="Scelta misteriosa", layout="centered")

st.title("🔮 Scelta misteriosa")

# Legge il trucco dal link
params = st.query_params
risposta_segreta = params.get("risposta", None)

if risposta_segreta:
    risposta_segreta = risposta_segreta.lower()

if st.button("Scopri il risultato"):
    if risposta_segreta == "enrico":
        st.success("Enrico")
    elif risposta_segreta == "ferrulli":
        st.success("Ferrulli")
    else:
        st.success(random.choice(["Enrico", "Ferrulli"]))
