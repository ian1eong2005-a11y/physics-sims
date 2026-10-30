"""Self-checking quiz engine.

A question is a dict with:
  id, level (1-3), type, q (the question text), hint (how to use the applet), and per type:
  mcq      options, answer (index), explain
  multi    options, answer (list of indexes), explain
  order    items, answer (items in the correct order), explain
  numeric  answer, tol, unit, explain
  explain  keys (list of {"label", "any": [substrings]}), model
"""
import re

import streamlit as st

LEVELS = {1: "Level 1 · recall", 2: "Level 2 · apply", 3: "Level 3 · explain"}


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def check_explain(text: str, keys):
    t = _norm(text)
    hit, miss = [], []
    for k in keys:
        (hit if any(s in t for s in k["any"]) else miss).append(k["label"])
    return hit, miss


def _render_question(q, prefix):
    k = f"{prefix}_{q['id']}"
    res_key = k + "_res"
    st.markdown(f"**{q['q']}**")
    if q.get("hint"):
        st.caption("Use the applet: " + q["hint"])

    typ = q["type"]
    if typ == "mcq":
        choice = st.radio("Choose one", q["options"], index=None, key=k, label_visibility="collapsed")
    elif typ == "multi":
        choice = st.multiselect("Choose all that apply", q["options"], key=k, label_visibility="collapsed")
    elif typ == "order":
        choice = st.multiselect("Click the items in the correct order", q["items"], key=k)
    elif typ == "numeric":
        choice = st.number_input(f"Answer / {q.get('unit', '')}", key=k, value=None, step=None, format="%g")
    else:
        choice = st.text_area("Your answer (one or two sentences)", key=k, height=90)

    if st.button("Check", key=k + "_btn", use_container_width=True):
        st.session_state[res_key] = _grade(q, choice)
    if typ == "explain" and st.button("Show model answer", key=k + "_model", use_container_width=True):
        st.session_state[res_key + "_model"] = True

    res = st.session_state.get(res_key)
    if res is not None:
        ok, msg = res
        (st.success if ok else st.warning)(msg)
        if ok is not None and q.get("explain") and typ != "explain":
            st.info(q["explain"])
    if st.session_state.get(res_key + "_model"):
        st.info("**Model answer.** " + q["model"])
    return res


def _grade(q, choice):
    typ = q["type"]
    if choice in (None, [], ""):
        return (None, "Give an answer first.")
    if typ == "mcq":
        ok = q["options"].index(choice) == q["answer"]
        return (ok, "Correct." if ok else "Not quite. Try the applet again and have another go.")
    if typ == "multi":
        ok = sorted(q["options"].index(c) for c in choice) == sorted(q["answer"])
        return (ok, "Correct." if ok else "Not all right yet. Check each option against the applet.")
    if typ == "order":
        ok = list(choice) == list(q["answer"])
        if ok:
            return (True, "Correct order.")
        first_wrong = next((i for i, (a, b) in enumerate(zip(choice, q["answer"])) if a != b), None)
        where = f" The first slip is at position {first_wrong + 1}." if first_wrong is not None else " You have not placed every item."
        return (False, "Not in the right order yet." + where)
    if typ == "numeric":
        ok = abs(float(choice) - q["answer"]) <= q.get("tol", 0)
        return (ok, "Correct." if ok else f"Not within range. Read the applet more carefully and try again.")
    hit, miss = check_explain(choice, q["keys"])
    if not miss:
        return (True, "You covered every key idea: " + "; ".join(hit) + ".")
    found = ("You mentioned: " + "; ".join(hit) + ". ") if hit else ""
    return (False, found + "Still missing: " + "; ".join(miss) + ". Use the applet, then add these to your answer.")


def quiz(questions, prefix: str):
    """Render a quiz with a level filter and a running score."""
    level = st.radio("Show", ["All levels", LEVELS[1], LEVELS[2], LEVELS[3]], horizontal=True, key=prefix + "_lvl")
    shown = [q for q in questions if level == "All levels" or LEVELS[q["level"]] == level]

    score_box = st.empty()   # filled after the questions so a click counts straight away

    for i, q in enumerate(shown, 1):
        with st.container(border=True):
            st.caption(f"Q{i} · {LEVELS[q['level']]}")
            _render_question(q, prefix)

    attempted = sum(1 for q in shown if st.session_state.get(f"{prefix}_{q['id']}_res", (None,))[0] is not None)
    correct = sum(1 for q in shown if st.session_state.get(f"{prefix}_{q['id']}_res", (None,))[0] is True)
    score_box.progress(correct / len(shown) if shown else 0, text=f"Score: {correct} / {len(shown)} correct · {attempted} attempted")

    if st.button("Reset this quiz", key=prefix + "_reset"):
        for key in list(st.session_state.keys()):
            if key.startswith(prefix + "_") and not key.endswith("_lvl"):
                del st.session_state[key]
        st.rerun()
