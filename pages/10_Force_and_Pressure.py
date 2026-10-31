import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.force_pressure import QUESTIONS

APPLETS = [
    dict(name="Weight, Density and Pressure Bench", file="force-pressure", height=780,
         blurb="Three modes. **Weight**: hang a mass on a newton meter on different worlds. **Density**: pick a material and a volume, then drop the block in water. **Pressure**: press a block into foam with a chosen force and contact area.",
         tasks=[
             "**Predict:** take the 5 kg mass to Jupiter. Which readout changes, which stays the same?",
             "Density: double the volume of the aluminium block. What happens to mass? To density? To floating or sinking?",
             "Find every material that floats. What do they have in common? Where is the dividing line?",
             "Pressure: keep 100 N and go from 500 cm² to 10 cm². By what factor does the pressure change? Watch the dent.",
             "A person's weight is about 700 N on two feet (≈ 0.05 m²). What pressure is that? Try to match it in the applet.",
         ]),
]

chapter_page("Ch 3 · Force and Pressure", "3a–3i", APPLETS, QUESTIONS, key="fp")
