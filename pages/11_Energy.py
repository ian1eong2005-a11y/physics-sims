import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.energy import QUESTIONS

APPLETS = [
    dict(name="Energy Coaster", file="energy-coaster", height=800,
         blurb="**Coaster**: a car runs along a track while bars show the gravitational potential, kinetic, thermal and total energy. **Crane**: lift a crate at steady speed and read off the force, the work done and the power.",
         tasks=[
             "**Predict:** with no friction, how high will the car get on the far hill? Watch the dashed start line.",
             "Pause at the top and in the first valley. Compare the Ep and Ek bars. What does the total bar do?",
             "Untick Show numbers. Estimate the speed in the valley from the height drop, then tick to check (½mv² = mgh).",
             "Turn friction on. Which bar grows? Does the total change? Why does each hill get lower?",
             "Crane: keep the crate and height, halve the time. Which readout changes and which does not?",
         ]),
]

chapter_page("Ch 6 · Energy", "6a–6e", APPLETS, QUESTIONS, key="en")
