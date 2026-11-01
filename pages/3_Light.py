import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.light import QUESTIONS

APPLETS = [
    dict(name="Ray Box", file="ray-box", height=860,
         blurb="A ray box shining at a plane mirror or into a glass block. Angles are always measured from the normal. Record readings to see that sin i ÷ sin r stays constant. Going further: send light from the block into air to find the critical angle and total internal reflection (beyond 5086).",
         tasks=[
             "**Predict:** with the mirror, if i goes up by 10°, what happens to r? Test it.",
             "Switch to the glass block. Set i = 0°, then 20°, 40°, 60°. Record each reading. What stays the same in the table?",
             "Change the material to water. Does the ray bend more or less than in glass? Link this to the speed readout.",
             "Choose the **Mystery block**. Take three readings and work out n before you press Reveal.",
         ]),
    dict(name="Lens Bench", file="lens-bench", height=760,
         blurb="A converging lens. Start with the parallel beam to see the principal focus, then place an object and find the image.",
         tasks=[
             "Parallel beam: make the focal length shorter. Do the rays bend more or less?",
             "**Predict:** object at 30 cm with f = 8 cm: will the image be bigger or smaller than the object? Upright or inverted? Untick 'Describe the image', decide, then check.",
             "Slide the object slowly towards the lens. At what distance does the image become virtual? What is special about that distance?",
             "Set the object at exactly F. What happens to the rays leaving the lens?",
         ]),
]

chapter_page("Ch 11 · Light", "11a–11h", APPLETS, QUESTIONS, key="light")
