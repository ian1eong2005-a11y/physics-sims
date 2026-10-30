"""Shared layout for a chapter page: Explore and Quiz tabs."""
import streamlit as st

from core.embed import show_sim
from core.quiz import quiz


def chapter_page(title: str, los: str, applets: list, questions: list, key: str):
    """applets: list of {"name", "file", "height", "blurb", "tasks": [prompts]}"""
    st.set_page_config(page_title=title, page_icon="⚛", layout="wide")
    st.title(title)
    st.caption(f"5086 learning outcomes {los}")

    explore, quiz_tab = st.tabs(["Explore", "Quiz"])

    with explore:
        names = [a["name"] for a in applets]
        pick = st.radio("Applet", names, horizontal=True, key=key + "_applet", label_visibility="collapsed") if len(names) > 1 else names[0]
        a = next(x for x in applets if x["name"] == pick)
        st.markdown(a["blurb"])
        show_sim(a["file"], a.get("height", 720))
        st.subheader("Try this: predict, then test")
        for i, p in enumerate(a["tasks"], 1):
            st.markdown(f"{i}. {p}")

    with quiz_tab:
        left, right = st.columns([1.15, 1], gap="medium")
        with left:
            names = [a["name"] for a in applets]
            pick = st.radio("Applet to use", names, horizontal=True, key=key + "_qapplet") if len(names) > 1 else names[0]
            a = next(x for x in applets if x["name"] == pick)
            show_sim(a["file"], a.get("height", 720))
        with right:
            quiz(questions, key)
