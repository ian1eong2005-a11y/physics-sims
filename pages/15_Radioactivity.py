import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.radioactivity import QUESTIONS

APPLETS = [
    dict(name="Decay Lab", file="radioactivity", height=820,
         blurb="Three modes. **Nuclide**: build a nucleus from protons and neutrons and read its notation. **Half-life**: 400 nuclei decay at random while the graph draws itself. **α β γ**: fire one radiation, or a mixture, at paper, aluminium or lead and watch the ionisation and the detector count, including background with no source. Then try the **Mystery source**: from the counts alone, decide which radiations it gives out.",
         tasks=[
             "**Predict:** carbon-12 → add two neutrons. Same element or not? Now add one proton instead.",
             "Half-life 4 s: how many are left at 4 s, 8 s, 12 s? Run it three times and compare.",
             "Tick the smooth halving curve. Why does the real (red) curve wobble around it?",
             "α β γ: which source gets through paper? Through aluminium? Through lead?",
             "Unpick all three sources (no source). Why does the detector still count? List the sources of background radiation.",
             "Pick α and γ together. Add paper, then aluminium, then lead. Why does the count drop in steps?",
             "**Mystery source:** measure the count with no barrier, paper, aluminium and lead. Decide which radiations are in it, then Check. Can you get three right in a row?",
         ]),
]

chapter_page("Ch 16 · Radioactivity", "16a–16h", APPLETS, QUESTIONS, key="rad")
