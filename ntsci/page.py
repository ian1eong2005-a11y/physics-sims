"""Shared layout for one topic of the G1 / N(T) Science applets: Explore, Investigate, Quiz.

Links such as  /energy?applet=energy-swing&mode=investigate  open one applet straight in its investigation
(used by the QR codes on the printed inquiry worksheets).
"""
import streamlit as st

from ntsci.embed import show
from ntsci.quiz import quiz

MODES = ["🔬 Explore", "🧪 Investigate", "✅ Quiz"]
MODE_KEYS = {"explore": 0, "investigate": 1, "quiz": 2}


def _pick(applets, key):
    names = [a["name"] for a in applets]
    want = st.query_params.get("applet")
    if want and key not in st.session_state:
        hit = next((a["name"] for a in applets if a["file"] == want), None)
        if hit:
            st.session_state[key] = hit
    if len(names) == 1:
        return applets[0]
    pick = st.radio("Applet", names, horizontal=True, key=key, label_visibility="collapsed")
    return next(a for a in applets if a["name"] == pick)


def topic_page(num, title, emoji, los, applets, questions, key):
    """applets: list of {"name", "file", "inq" (has an investigation), "try": [short prompts], "height"}"""
    st.set_page_config(page_title=f"Topic {num}: {title}", page_icon=emoji, layout="wide")
    st.title(f"{emoji} Topic {num}: {title}")
    st.caption(los)
    st.markdown("<style>div[role=radiogroup] label p{font-size:1.1rem;font-weight:600}</style>", unsafe_allow_html=True)

    mkey = key + "_mode"
    want = MODE_KEYS.get((st.query_params.get("mode") or "").lower())
    if want is not None and mkey not in st.session_state:
        st.session_state[mkey] = MODES[want]
    mode = st.radio("Mode", MODES, horizontal=True, key=mkey, label_visibility="collapsed")

    if mode == MODES[0]:
        a = _pick(applets, key + "_applet")
        show(a["file"], a.get("height", 800))
        if a.get("try"):
            st.subheader("Try this")
            for i, t in enumerate(a["try"], 1):
                st.markdown(f"{i}. {t}")
    elif mode == MODES[1]:
        st.markdown("**Be a scientist:** make a guess, plan a fair test, record your results, then say what you found.")
        a = _pick([x for x in applets if x.get("inq")], key + "_iapplet")
        opts = {"inq": 1}
        k = st.query_params.get("inq") or ""
        if k.isdigit() and st.query_params.get("applet") == a["file"]:   # ?inq=1 opens the applet's second investigation
            opts["start"] = int(k)
        show(a["file"], a.get("height", 800) + 140, opts)
    else:
        left, right = st.columns([1.2, 1], gap="large")
        with left:
            quiz(questions, key + "_quiz")
        with right:
            st.info("Stuck? Go back to **Explore** or **Investigate** and try the applet.")
