import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.internal_energy import QUESTIONS

APPLETS = [
    dict(name="Heating Curve Lab", file="internal-energy", height=840,
         blurb="Heat a substance from solid to gas. Watch the particles, the KE and PE bars, and the temperature–time graph at the same time. The point to see: at the plateaus the heater is still on but the temperature stops rising.",
         tasks=[
             "**Predict:** when the ice reaches 0 °C, will the temperature keep rising as the heater stays on? Watch the graph and the bars to test it.",
             "Pause during melting. Which bar is growing? Which bar is frozen? Explain to your partner where the heater's energy is going.",
             "Let it boil. Compare the two plateaus: which one lasts longer? What does that tell you about separating particles completely versus loosening them?",
             "Switch to **Cooling** from the gas. Describe what happens to temperature and PE during condensation.",
             "Change the substance to wax. What stays the same about the shape of the curve, and what changes?",
         ]),
]

chapter_page("Ch 7 · Kinetic Particle Model of Matter", "7a–7e", APPLETS, QUESTIONS, key="ke")
