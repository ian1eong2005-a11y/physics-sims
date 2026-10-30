import streamlit as st

st.set_page_config(page_title="5086 Physics Applets", page_icon="⚛", layout="wide")
st.title("5086 Physics Applets")
st.markdown(
    "Interactive models for G3 Science (Physics). Each chapter has an **Explore** tab "
    "(play, predict, test) and a **Quiz** tab (self-checking questions you answer with the applet open)."
)

CHAPTERS = [
    ("pages/1_Waves.py", "Ch 9 · General Wave Properties", "Wave graphs, sound, ripple tank"),
    ("pages/2_EM_Spectrum.py", "Ch 10 · Electromagnetic Spectrum", "Order, uses and hazards"),
    ("pages/3_Light.py", "Ch 11 · Light", "Reflection, refraction, converging lens"),
    ("pages/4_Internal_Energy.py", "Ch 7 · Kinetic Particle Model", "Heating through melting and boiling"),
    ("pages/5_Kinematics.py", "Ch 2 · Kinematics", "Speed–time and distance–time graphs"),
    ("pages/6_Thermal_Processes.py", "Ch 8 · Thermal Processes", "Conduction and convection"),
    ("pages/7_Forces.py", "Ch 4–5 · Dynamics and Moments", "Resultant force, principle of moments"),
    ("pages/8_Circuits.py", "Ch 13 · D.C. Circuits", "Series, parallel and mixed"),
]

from pathlib import Path
HERE = Path(__file__).resolve().parent
CHAPTERS = [c for c in CHAPTERS if (HERE / c[0]).exists()]

cols = st.columns(2)
for i, (path, name, blurb) in enumerate(CHAPTERS):
    with cols[i % 2].container(border=True):
        st.subheader(name)
        st.caption(blurb)
        st.page_link(path, label="Open", icon="▶")

st.divider()
st.caption("Built for Queenstown Secondary School Physics. Models are simplified on purpose: they show the idea, not every detail.")
