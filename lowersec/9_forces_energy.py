import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import re
from core.page import chapter_page
from core.guides import GUIDES
from core.inquiries import INQUIRIES
from quizzes.lss_forces_energy import QUESTIONS


def _sec2(x, key=None):
    """Sec 2 words for the shared Energy Coaster guide and inquiries: GPE, KE and the internal store (as on the applet)."""
    if isinstance(x, str):
        x = re.sub(r"\bEp\b", "GPE", x)
        x = re.sub(r"\bEk\b", "KE", x)
        return x.replace("thermal store", "internal store").replace("thermal", "internal")
    if isinstance(x, dict):
        return {k: _sec2(v, k) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        out = [_sec2(v) for v in x]
        if key == "any":   # answer keys: accept both the old and the Sec 2 words
            out = list(dict.fromkeys(list(x) + out))
        return type(x)(out) if isinstance(x, tuple) else out
    return x


_COASTER_GUIDE = GUIDES.get("energy-coaster", {})

APPLETS = [
    dict(name="Pressure Lab", file="pressure-lab", height=820,
         blurb="**Bed of nails**: a person lies on 1 to 400 nails. The weight never changes, so watch what happens to the force on each nail and the pressure on the skin. Put your own face on the person if you like (the photo stays on your device). **Sharp or blunt?**: the same force on a point and on a flat surface: drawing pin, knife, stiletto, snowshoes, elephant.",
         tasks=[
             "**Predict:** how many nails are needed before it stops hurting? Then slide and find out.",
             "Keep 400 nails and raise the weight. At what weight does it start to hurt? Explain with p = F ÷ A.",
             "Sharp or blunt: for each pair, say which side has the bigger pressure BEFORE you look at the numbers.",
             "A person on a stiletto heel versus an elephant: who puts more pressure on the floor? Check.",
             "Why do camels have wide feet and why do knives need sharpening? Use the word pressure in both answers.",
         ]),
    dict(name="Energy Coaster", file="energy-coaster", height=800, opts={"sec2": True},
         guide=_sec2(_COASTER_GUIDE.get("steps")), controls=_sec2(_COASTER_GUIDE.get("controls")),
         inquiry=_sec2(INQUIRIES.get("energy-coaster")),
         blurb="**Coaster**: a car runs along a track while bars show the energy in the gravitational potential store (GPE), the kinetic store (KE), the internal store and the total. **Crane**: lift a crate at steady speed and read off the force, the work done and the power.",
         tasks=[
             "**Predict:** with no friction, how high will the car get on the far hill? Watch the dashed start line.",
             "Look at the bars before you press Release the car, then pause in the first valley. Compare GPE and KE. What does the total bar do?",
             "Turn friction on. Which bar grows? Does the total change? Where has the energy gone?",
             "Crane: keep the crate and height, halve the time. Which readout changes and which does not?",
         ]),
    dict(name="Moments See-saw", file="moments-seesaw", height=800,
         blurb="Drag weights onto a beam and balance it. Each weight's turning effect (moment = force × distance from the pivot) is shown; the beam balances when the clockwise and anticlockwise moments are equal.",
         tasks=[
             "**Predict:** where must a 2 N weight go to balance a 4 N weight at 20 cm? Test it.",
             "Put a small weight far out and a big weight close in. Can they balance? What is the same on both sides?",
             "Try the mystery challenge and work out the unknown weight from the moments.",
         ]),
]

chapter_page("Ch 9 · Application of Forces and Transfer of Energy", "9.2–9.6 (pressure, turning effect, energy, work)", APPLETS, QUESTIONS, key="lsfe", syllabus="2021 LSS")
