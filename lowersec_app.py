"""Lower Secondary Science applets (2021 LSS). Deploy on Streamlit Cloud with main file lowersec_app.py.

Uses st.navigation, so the physics pages/ folder is not picked up by this app.
"""
import streamlit as st

PAGES = [
    st.Page("lowersec/home.py", title="Home", icon="🏠", default=True),
    st.Page("lowersec/12_ecosystems.py", title="Ch 12 · Interactions within Ecosystems", icon="🌿", url_path="ecosystems"),
    st.Page("lowersec/14_digestion.py", title="Ch 14 · Digestive System", icon="🍞", url_path="digestion"),
    st.Page("lowersec/15_transport_humans.py", title="Ch 15 · Transport in Humans", icon="❤️", url_path="transport-humans"),
    st.Page("lowersec/15_transport_plants.py", title="Ch 15 · Transport in Plants", icon="🌱", url_path="transport-plants"),
    st.Page("lowersec/16_reproduction.py", title="Ch 16 · Reproductive System", icon="🧬", url_path="reproduction"),
]
st.navigation(PAGES).run()
