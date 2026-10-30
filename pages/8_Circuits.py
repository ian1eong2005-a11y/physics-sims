import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.circuits import QUESTIONS

APPLETS = [
    dict(name="Series and Parallel Bench", file="circuits", height=900,
         blurb="Build a series, parallel or mixed circuit with 1–4 resistors. Yellow charges move faster where the current is larger. Every branch has an ammeter and every resistor a voltmeter; quiz mode hides the readings.",
         tasks=[
             "**Predict:** in series, will the current be bigger before R1 or after R3? Watch the dot speeds, then read the ammeter.",
             "Series: add up the three voltmeter readings. Now change the e.m.f. Does the rule still hold?",
             "Parallel: which branch has the fastest dots? Change that resistor's value and watch the dots and the ammeter.",
             "Parallel: switch R3 off. What happens to the other branches? What happens to the battery current?",
             "Mixed: untick nothing, but work out every reading on paper first, then compare.",
         ]),
]

chapter_page("Ch 13 · D.C. Circuits", "12i, 13b–13g", APPLETS, QUESTIONS, key="circ")
