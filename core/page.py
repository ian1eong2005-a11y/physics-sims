"""Shared layout for a chapter page: Explore, Guided, Inquiry and Quiz tabs."""
import pandas as pd
import streamlit as st

from core.embed import show_sim
from core.guides import GUIDES
from core.inquiries import INQUIRIES
from core.quiz import check_explain, quiz


def _pick_applet(applets, key):
    names = [a["name"] for a in applets]
    if len(names) == 1:
        return applets[0]
    # A link or QR code such as ?applet=energy-coaster opens that applet first (used by the printed worksheets and slides).
    want = st.query_params.get("applet")
    if want and key not in st.session_state:
        hit = next((x["name"] for x in applets if x["file"] == want), None)
        if hit:
            st.session_state[key] = hit
    pick = st.radio("Applet", names, horizontal=True, key=key, label_visibility="collapsed")
    return next(x for x in applets if x["name"] == pick)


def _guided(a, key):
    """Step-by-step walkthrough: do this, look for this, quick check, next."""
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
            st.success("You have finished this guide. Try the **Inquiry** or **Quiz** tab, or go back to **Explore** and test your own ideas.")

    back, nxt = st.columns(2)
    if back.button("◀ Back", key=skey + "_back", disabled=i == 0, use_container_width=True):
        st.session_state[skey] = i - 1
        st.rerun()
    if nxt.button("Next ▶", key=skey + "_next", disabled=(i >= n - 1) or not can_next, use_container_width=True):
        st.session_state[skey] = i + 1
        st.rerun()
    if not can_next:
        st.caption("Answer the quick check (or press Show me) to unlock Next.")


def _inquiry(a, key):
    """A short investigation: question, prediction, plan, results table, pattern, conclusion."""
    invs = a.get("inquiry") or INQUIRIES.get(a["file"]) or []
    if not invs:
        st.info("No investigation for this applet yet. Try the Guided tab.")
        return
    titles = [v["title"] for v in invs]
    pick = st.selectbox("Investigation", titles, key=f"{key}_inq_{a['file']}_pick") if len(titles) > 1 else titles[0]
    inv = next(v for v in invs if v["title"] == pick)
    k = f"{key}_inq_{a['file']}_{titles.index(pick)}"

    st.markdown(f"#### {inv['title']}")
    st.markdown(f"**The question.** {inv['question']}")

    st.markdown("**1 · Predict**")
    st.text_area("My prediction", key=k + "_pred", placeholder=inv["predict"], height=70, label_visibility="collapsed")

    st.markdown("**2 · Plan**")
    st.markdown(f"- I will change: **{inv['change']}**\n- I will measure or observe: **{inv['measure']}**")
    chosen = st.multiselect("To make it a fair test I must keep the same:", inv["keep_options"], key=k + "_keep")
    if st.button("Check my plan", key=k + "_keepb", use_container_width=True):
        want, got = set(inv["keep"]), set(chosen)
        if got == want:
            st.session_state[k + "_keepres"] = "✅ That is a fair test."
        else:
            wrong = [c for c in chosen if c not in want]
            missing = [c for c in inv["keep"] if c not in got]
            msg = []
            if missing:
                msg.append("still need to keep: " + ", ".join(missing))
            if wrong:
                msg.append("not these (they are the variables you change or measure): " + ", ".join(wrong))
            st.session_state[k + "_keepres"] = "⚠️ " + "; ".join(msg)
    if st.session_state.get(k + "_keepres"):
        st.caption(st.session_state[k + "_keepres"])

    st.markdown("**3 · Test and record**")
    st.caption(inv["how"])
    df = pd.DataFrame([[""] * len(inv["cols"]) for _ in range(4)], columns=inv["cols"])
    st.data_editor(df, key=k + "_tbl", num_rows="dynamic", use_container_width=True, hide_index=True)

    st.markdown("**4 · Find the pattern**")
    txt = st.text_area("Describe the pattern in your results", key=k + "_pat", height=80, placeholder="As I increased …, the … ", label_visibility="collapsed")
    c1, c2 = st.columns(2)
    if c1.button("Check my pattern", key=k + "_patb", use_container_width=True):
        hit, miss = check_explain(txt or "", inv["pattern_keys"])
        st.session_state[k + "_patres"] = (hit, miss)
    if c2.button("Show the model pattern", key=k + "_patshow", use_container_width=True):
        st.session_state[k + "_patshown"] = True
    res = st.session_state.get(k + "_patres")
    if res:
        hit, miss = res
        if not miss:
            st.success("You found it: " + "; ".join(hit) + ".")
        else:
            st.warning(("You mentioned: " + "; ".join(hit) + ". " if hit else "") + "Look again for: " + "; ".join(miss) + ".")
    if st.session_state.get(k + "_patshown"):
        st.info("**Model pattern.** " + inv["model_pattern"])

    st.markdown("**5 · Conclude**")
    verdict = st.radio("My prediction was…", ["supported by the results", "partly right", "not supported"], horizontal=True, key=k + "_verdict", index=None)
    if verdict:
        st.success("**Conclusion.** " + inv["conclusion"])
        st.markdown("**Go further.** " + inv["extend"])


def chapter_page(title: str, los: str, applets: list, questions: list, key: str, syllabus: str = "5086"):
    """applets: list of {"name", "file", "height", "blurb", "tasks": [prompts], "guide", "controls", "inquiry"}"""
    st.set_page_config(page_title=title, page_icon="⚛", layout="wide")
    st.title(title)
    st.caption(f"{syllabus} learning outcomes {los} · Tip: Ctrl + scroll (or pinch) zooms any applet; Space pauses; R resets.")

    explore, guided, inquiry, quiz_tab = st.tabs(["Explore", "Guided", "Inquiry", "Quiz"])

    with explore:
        a = _pick_applet(applets, key + "_applet")
        st.markdown(a["blurb"])
        show_sim(a["file"], a.get("height", 720), a.get("opts"))
        st.subheader("Try this: predict, then test")
        for i, p in enumerate(a["tasks"], 1):
            st.markdown(f"{i}. {p}")

    with guided:
        st.caption("Working alone? This tab walks you through the applet one step at a time.")
        left, right = st.columns([1.15, 1], gap="medium")
        with left:
            a = _pick_applet(applets, key + "_gapplet")
            show_sim(a["file"], a.get("height", 720), a.get("opts"))
        with right:
            if a.get("guide") or GUIDES.get(a["file"]):
                _guided(a, key)
            else:
                st.info("No guide for this applet yet. Use the Explore tab.")

    with inquiry:
        st.caption("Be the scientist: predict, plan a fair test, collect results in the applet, find the pattern, conclude.")
        left, right = st.columns([1.15, 1], gap="medium")
        with left:
            a = _pick_applet(applets, key + "_iapplet")
            show_sim(a["file"], a.get("height", 720), a.get("opts"))
        with right:
            _inquiry(a, key)

    with quiz_tab:
        left, right = st.columns([1.15, 1], gap="medium")
        with left:
            a = _pick_applet(applets, key + "_qapplet")
            show_sim(a["file"], a.get("height", 720), a.get("opts"))
        with right:
            quiz(questions, key)
