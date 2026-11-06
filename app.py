import streamlit as st

st.set_page_config(page_title="5086 Physics Applets", page_icon="⚛", layout="wide")
st.title("5086 Physics Applets")
st.markdown(
    "Interactive models for G3 Science (Physics). Each chapter has an **Explore** tab "
    "(play, predict, test), a **Guided** tab (step-by-step: do this, look for this, quick check), an **Inquiry** tab (predict, plan a fair test, record, conclude) "
    "and a **Quiz** tab (self-checking questions you answer with the applet open)."
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
    ("pages/9_Measurements.py", "Ch 1 · Measurements", "Prefixes, orders of magnitude, choosing an instrument"),
    ("pages/10_Force_and_Pressure.py", "Ch 3 · Force and Pressure", "Weight, density, pressure"),
    ("pages/11_Energy.py", "Ch 6 · Energy", "Energy stores, conservation, work and power"),
    ("pages/12_Charge_and_Current.py", "Ch 12 · Charge and Current", "Charges, Q = It, V = IR, resistance of a wire"),
    ("pages/13_Practical_Electricity.py", "Ch 14 · Practical Electricity", "Power, kWh cost, fuses, earthing, the plug"),
    ("pages/14_Magnetism.py", "Ch 15 · Magnetism and Electromagnetism", "Field patterns, solenoids, force on a wire"),
    ("pages/15_Radioactivity.py", "Ch 16 · Radioactivity", "Nuclides, half-life, α β γ, background"),
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
