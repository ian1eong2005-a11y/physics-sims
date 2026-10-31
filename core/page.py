"""Shared layout for a chapter page: Explore, Guided and Quiz tabs."""
import streamlit as st

from core.embed import show_sim
from core.guides import GUIDES
from core.quiz import quiz


def _pick_applet(applets, key):
    names = [a["name"] for a in applets]
    if len(names) == 1:
        return applets[0]
    pick = st.radio("Applet", names, horizontal=True, key=key, label_visibility="collapsed")
    return next(x for x in applets if x["name"] == pick)


def _guided(a, key):
    """Step-by-step walkthrough: do this, look for this, quick check, next.

    a["guide"] is a list of steps: {"do", "see", "check": {"q", "options", "answer", "why"}} (check optional).
    a["controls"] is an optional list of one-line descriptions of the controls.
    """
    g = GUIDES.get(a["file"], {})
    steps = a.get("guide") or g.get("steps") or []
    controls = a.get("controls") or g.get("controls")
    skey = f"{key}_g_{a['file']}_step"
    i = st.session_state.get(skey, 0)
    n = len(steps) + 1
    i = max(0, min(i, n - 1))

    st.progress(i / (n - 1) if n > 1 else 1.0, text=f"Step {i + 1} of {n}")

    can_next = True
    if i == 0:
        st.markdown(f"#### Meet the applet: {a['name']}")
        st.markdown(a["blurb"])
        if controls:
            st.markdown("**What the controls do**")
            for c in controls:
                st.markdown(f"- {c}")
        st.caption("Press **Next** and the guide will tell you what to try and what to look for. Keep the applet on the left in view.")
    else:
        step = steps[i - 1]
        st.markdown(f"#### Step {i}")
        st.markdown(f"**Do this.** {step['do']}")
        st.markdown(f"**Look for.** {step['see']}")
        chk = step.get("check")
        if chk:
            ckey = f"{skey}_c{i}"
            st.markdown(f"**Quick check.** {chk['q']}")
            choice = st.radio("Quick check", chk["options"], index=None, key=ckey + "_r", label_visibility="collapsed")
            if st.button("Check my answer", key=ckey + "_b", use_container_width=True):
                st.session_state[ckey + "_res"] = (choice is not None and chk["options"].index(choice) == chk["answer"])
            res = st.session_state.get(ckey + "_res")
            if res is True:
                st.success("Yes. " + chk.get("why", ""))
            elif res is False:
                st.warning("Not yet. Look at the applet again and change your answer, or press **Show me**.")
                if st.button("Show me", key=ckey + "_show", use_container_width=True):
                    st.session_state[ckey + "_res"] = None
                    st.session_state[ckey + "_shown"] = True
                    st.rerun()
            if st.session_state.get(ckey + "_shown"):
                st.info(f"**Answer:** {chk['options'][chk['answer']]}. {chk.get('why', '')}")
            can_next = res is True or bool(st.session_state.get(ckey + "_shown"))
        if i == n - 1:
            st.success("You have finished this guide. Try the **Quiz** tab, or go back to **Explore** and test your own ideas.")

    back, nxt = st.columns(2)
    if back.button("◀ Back", key=skey + "_back", disabled=i == 0, use_container_width=True):
        st.session_state[skey] = i - 1
        st.rerun()
    if nxt.button("Next ▶", key=skey + "_next", disabled=(i >= n - 1) or not can_next, use_container_width=True):
        st.session_state[skey] = i + 1
        st.rerun()
    if not can_next:
        st.caption("Answer the quick check (or press Show me) to unlock Next.")


def chapter_page(title: str, los: str, applets: list, questions: list, key: str):
    """applets: list of {"name", "file", "height", "blurb", "tasks": [prompts], "guide": [...], "controls": [...]}"""
    st.set_page_config(page_title=title, page_icon="⚛", layout="wide")
    st.title(title)
    st.caption(f"5086 learning outcomes {los}")

    explore, guided, quiz_tab = st.tabs(["Explore", "Guided", "Quiz"])

    with explore:
        a = _pick_applet(applets, key + "_applet")
        st.markdown(a["blurb"])
        show_sim(a["file"], a.get("height", 720))
        st.subheader("Try this: predict, then test")
        for i, p in enumerate(a["tasks"], 1):
            st.markdown(f"{i}. {p}")

    with guided:
        st.caption("Working alone? This tab walks you through the applet one step at a time.")
        left, right = st.columns([1.15, 1], gap="medium")
        with left:
            a = _pick_applet(applets, key + "_gapplet")
            show_sim(a["file"], a.get("height", 720))
        with right:
            if a.get("guide") or GUIDES.get(a["file"]):
                _guided(a, key)
            else:
                st.info("No guide for this applet yet. Use the Explore tab.")

    with quiz_tab:
        left, right = st.columns([1.15, 1], gap="medium")
        with left:
            a = _pick_applet(applets, key + "_qapplet")
            show_sim(a["file"], a.get("height", 720))
        with right:
            quiz(questions, key)
