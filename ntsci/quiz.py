"""A very simple quiz for the G1 / N(T) applets: one question at a time, tap to answer, instant feedback, stars.

A question is a dict: q (text), pic (emoji, optional), why (one-line explanation) and one of
  type "mcq"    options, answer (index)
  type "multi"  options, answer (list of indexes): tick all the correct ones
  type "num"    answer, tol (default 0), unit
  type "match"  pairs: list of (left, right); pick the right partner for each left item
"""
import streamlit as st

CSS = """<style>
div[role=radiogroup] label p, div[data-testid=stCheckbox] label p {font-size:1.12rem}
.ntq {font-size:1.45rem;font-weight:700;line-height:1.35;margin:.2rem 0 .6rem}
.ntpic {font-size:4rem;line-height:1.1}
</style>"""


def _widget(q, k):
    """Draw the answer widget; return (answered?, correct?, the right answer as text)."""
    typ = q["type"]
    if typ == "mcq":
        pick = st.radio("Choose one", q["options"], index=None, key=k, label_visibility="collapsed")
        return pick is not None, pick == q["options"][q["answer"]], q["options"][q["answer"]]
    if typ == "multi":
        st.caption("Tick ALL the correct ones.")
        got = [i for i, o in enumerate(q["options"]) if st.checkbox(o, key=f"{k}_{i}")]
        return bool(got), sorted(got) == sorted(q["answer"]), "; ".join(q["options"][i] for i in q["answer"])
    if typ == "num":
        val = st.number_input(f"Answer ({q.get('unit', '')})", value=None, key=k, placeholder="type a number")
        right = f"{q['answer']:g} {q.get('unit', '')}"
        return val is not None, val is not None and abs(val - q["answer"]) <= q.get("tol", 0) + 1e-9, right
    if typ == "match":
        rights = sorted({r for _, r in q["pairs"]})
        ok, done = True, True
        for j, (left, right) in enumerate(q["pairs"]):
            pick = st.selectbox(left, rights, index=None, key=f"{k}_{j}", placeholder="choose…")
            done = done and pick is not None
            ok = ok and pick == right
        return done, ok, "; ".join(f"{a} → {b}" for a, b in q["pairs"])
    raise ValueError(typ)


def quiz(questions, key):
    st.markdown(CSS, unsafe_allow_html=True)
    ss = st.session_state
    n = len(questions)
    i = ss.setdefault(key + "_i", 0)
    stars = ss.setdefault(key + "_stars", 0)

    if i >= n:
        st.balloons()
        st.success(f"### Quiz finished!  ⭐ {stars} of {n} right on the first try")
        st.markdown("Try again and see if you can beat your score." if stars < n else "Perfect score. Well done!")
        if st.button("↺ Try the quiz again", key=key + "_again", use_container_width=True):
            for name in [x for x in ss if str(x).startswith(key + "_")]:
                del ss[name]
            st.rerun()
        return

    q = questions[i]
    k = f"{key}_q{i}"
    st.progress(i / n, text=f"Question {i + 1} of {n}   ·   ⭐ {stars}")
    if q.get("pic"):
        st.markdown(f"<div class='ntpic'>{q['pic']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ntq'>{q['q']}</div>", unsafe_allow_html=True)

    solved, tries = ss.get(k + "_ok", False), ss.get(k + "_tries", 0)
    answered, correct, right = _widget(q, k)

    if not solved and tries < 2:
        if st.button("Check", key=k + "_check", type="primary", use_container_width=True):
            if not answered:
                st.warning("Choose an answer first.")
            else:
                ss[k + "_tries"] = tries + 1
                if correct:
                    ss[k + "_ok"] = True
                    if tries == 0:
                        ss[key + "_stars"] = stars + 1
                st.rerun()
        if tries == 1:
            st.warning("Not yet. Look again and have one more try.")
    if solved:
        st.success("✅ Correct! " + q.get("why", ""))
    elif tries >= 2:
        st.info(f"The answer is: **{right}**. " + q.get("why", ""))
    if solved or tries >= 2:
        if st.button("Next ▶" if i < n - 1 else "Finish ▶", key=k + "_next", type="primary", use_container_width=True):
            ss[key + "_i"] = i + 1
            st.rerun()
