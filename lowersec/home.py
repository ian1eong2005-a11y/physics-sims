import streamlit as st

st.set_page_config(page_title="Lower Sec Science Applets", page_icon="🔬", layout="wide")
st.title("Lower Sec Science Applets")
st.markdown(
    "Interactive models for Lower Secondary Science (2021 syllabus). Each chapter has an **Explore** tab "
    "(play, predict, test), a **Guided** tab (step-by-step: do this, look for this, quick check) "
    "and a **Quiz** tab (self-checking questions you answer with the applet open)."
)
st.caption("Parts marked **G3** go beyond the G2 syllabus.")

CHAPTERS = [
    ("lowersec/14_digestion.py", "Ch 14 · Human Digestive System", "Journey of food, enzyme test tube, blood glucose"),
    ("lowersec/15_transport_humans.py", "Ch 15 · Transport in Humans", "Heart and blood vessels, diffusion, why we need a transport system"),
    ("lowersec/15_transport_plants.py", "Ch 15 · Transport in Plants", "Xylem and phloem, root hairs and osmosis, leaf gases"),
    ("lowersec/16_reproduction.py", "Ch 16 · Human Sexual Reproductive System", "Parts and functions, menstrual cycle, fertilisation and birth control"),
]
cols = st.columns(2)
for i, (path, name, blurb) in enumerate(CHAPTERS):
    with cols[i % 2].container(border=True):
        st.subheader(name)
        st.caption(blurb)
        st.page_link(path, label="Open", icon="▶")

st.divider()
st.caption("Built for Queenstown Secondary School Science. Models are simplified on purpose: they show the idea, not every detail.")
