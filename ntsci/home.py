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
st.caption("Topics 6 to 11 (Food Chemistry, Food Safety, Staying Healthy, Digestion, Breathing, Blood Circulation) are coming soon. "
           "Built for Queenstown Secondary School Science. The applets are simple models: they show the idea, not every detail.")
