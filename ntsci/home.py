import streamlit as st

st.set_page_config(page_title="G1 Science Applets", page_icon="🔬", layout="wide")
st.title("🔬 G1 Science Applets (Sec 3 N(T))")
st.markdown(
    "Simple applets for Upper Secondary G1 / N(T) Science (syllabus K123). Each topic has three parts:  \n"
    "**🔬 Explore** (play with it) · **🧪 Investigate** (guess, fair test, record, what I found) · **✅ Quiz** (check yourself)"
)

TOPICS = [
    ("Machines Around Us", [
        ("ntsci/t1_energy.py", "⚡", "1 · Energy", "Swinging bottle, heaters, hot and cold, power station"),
        ("ntsci/t2_electricity.py", "🔋", "2 · Electricity", "Series and parallel, resistors, cost of electricity"),
        ("ntsci/t3_wave.py", "〰️", "3 · Wave", "Rope waves, uses of waves"),
        ("ntsci/t4_force.py", "🏎️", "4 · Effects of Force", "Speed, speeding up, turning effect"),
    ]),
    ("Food Matters", [
        ("ntsci/t5_food.py", "🌱", "5 · Sources of Food", "What plants need, fertiliser, ripening, farming methods"),
        ("ntsci/t6_chem.py", "🧪", "6 · Food Chemistry", "Separating mixtures, pH, neutralisation, acid reactions, rusting"),
        ("ntsci/t7_safety.py", "🥫", "7 · Food Safety", "Microbes, keeping food fresh, food additives"),
    ]),
    ("Our Body and Health", [
        ("ntsci/t8_health.py", "💪", "8 · Staying Healthy", "Germ killers, antibiotics, BMI, diet, bones and joints"),
        ("ntsci/t9_digestion.py", "🍽️", "9 · Digestion", "Digestive system, enzymes, a healthy gut"),
        ("ntsci/t10_breathing.py", "🫁", "10 · Breathing", "Breathing system, inhaled and exhaled air, smoking"),
        ("ntsci/t11_blood.py", "❤️", "11 · Blood Circulation", "Pulse and exercise, heart and lungs, blood, plaque"),
    ]),
]
for section, items in TOPICS:
    st.subheader(section)
    cols = st.columns(3)
    for i, (path, emoji, name, blurb) in enumerate(items):
        with cols[i % 3].container(border=True):
            st.markdown(f"<div style='font-size:3rem;line-height:1.1'>{emoji}</div>", unsafe_allow_html=True)
            st.markdown(f"**{name}**")
            st.caption(blurb)
            st.page_link(path, label="Open", icon="▶")

st.divider()
st.caption("Built for Queenstown Secondary School Science. The applets are simple models: they show the idea, not every detail.")
