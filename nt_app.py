"""G1 / N(T) Science applets (syllabus K123). Deploy on Streamlit Cloud with main file nt_app.py.

Uses st.navigation, so the physics pages/ folder is not picked up by this app.
"""
import streamlit as st

PAGES = [
    st.Page("ntsci/home.py", title="Home", icon="🏠", default=True),
    st.Page("ntsci/t1_energy.py", title="1 · Energy", icon="⚡", url_path="energy"),
    st.Page("ntsci/t2_electricity.py", title="2 · Electricity", icon="🔋", url_path="electricity"),
    st.Page("ntsci/t3_wave.py", title="3 · Wave", icon="🌊", url_path="wave"),
    st.Page("ntsci/t4_force.py", title="4 · Effects of Force", icon="🏎️", url_path="force"),
    st.Page("ntsci/t5_food.py", title="5 · Sources of Food", icon="🌱", url_path="food"),
]
st.navigation(PAGES).run()
