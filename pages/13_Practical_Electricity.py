import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.practical_electricity import QUESTIONS

APPLETS = [
    dict(name="Home Electricity", file="home-electricity", height=820,
         blurb="**Appliances & cost**: pick an appliance, see the current it draws, choose a fuse, and work out the energy in kWh and the cost. **Plug & safety**: wire a 3-pin plug, see what happens when a live wire touches a metal case with and without earthing, and compare a switch in the live wire with one in the neutral.",
         tasks=[
             "**Predict:** which appliances need a 13 A fuse? Check each one.",
             "Find the appliance that costs most per day at 2 hours, and the one that costs least. What decides it?",
             "Plug & safety: untick the earth. What is the case at? Tick earth, untick fuse. Is that safe?",
             "Switch on the neutral wire, OFF. Is the lamp safe to touch? Why not?",
             "Explain to a partner why heating appliances draw such large currents (use I = P/V).",
         ]),
]

chapter_page("Ch 14 · Practical Electricity", "14a–14i", APPLETS, QUESTIONS, key="pe")
