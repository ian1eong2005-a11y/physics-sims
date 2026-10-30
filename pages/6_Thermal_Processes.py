import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.thermal import QUESTIONS

APPLETS = [
    dict(name="Conduction Lab", file="conduction", height=820,
         blurb="A rod of atoms heated from one end. Atoms vibrate more and bump their neighbours; in metals free electrons carry energy too. The graph shows temperature along the rod.",
         tasks=[
             "**Predict:** will the right-hand end of a copper rod warm up faster or slower than a glass rod? Test both with the same heater power.",
             "Untick 'Show free electrons' and watch copper for 20 s. Do the atoms themselves travel along the rod?",
             "Put ice on the cold end. What happens to the temperature graph? Does energy ever flow from cold to hot?",
             "Set the heater to 'Both' ends. Where is the coolest point? Why?",
         ]),
    dict(name="Convection Tank", file="convection", height=820,
         blurb="A tank of fluid heated at one spot. Hot particles spread out, become less dense and rise; cooler fluid sinks. Count the particles in the two boxes to compare densities.",
         tasks=[
             "**Predict:** where will the traced particle go after it passes over the heater? Watch it for 30 s.",
             "Compare the particle counts in boxes A and B. Which region is less dense? Turn on the density map to check.",
             "Move the heater to the top. Wait 30 s. Does a current form? Explain why heaters are placed low in a room.",
             "Switch to Gas and turn the expansion slider up. Does the current get stronger or weaker?",
         ]),
]

chapter_page("Ch 8 · Thermal Processes", "8a–8c, 8e", APPLETS, QUESTIONS, key="therm")
