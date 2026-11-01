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
         blurb="A tank of fluid heated from outside, under one part of the floor. The particles never get bigger: warm ones move faster and spread apart, so the warm patch is less dense and rises as a group while cooler, denser fluid sinks. Count the particles in boxes A and B to compare densities.",
         tasks=[
             "**Predict:** where will the traced particle go after it passes over the heater? Watch it for 30 s.",
             "Compare the particle counts in boxes A and B. Which region is less dense? Turn on the density map to check.",
             "Move the heater to the top. Wait 30 s. Does a current form? Explain why heaters are placed low in a room.",
             "Watch the first 10 seconds closely: what happens to the spacing of the particles above the heater BEFORE they start to rise?",
             "Switch to Gas. Does a convection current still form? Why can it not happen in a solid?",
         ]),
    dict(name="Radiation Lab", file="radiation", height=860,
         blurb="Two cans next to a radiant heater, or two hot cans cooling down. Choose each can's surface and surface area, remove the air, and compare the temperature–time graphs. Infrared radiation needs no medium.",
         tasks=[
             "**Predict:** dull black or shiny silver, which can warms up faster next to the heater? Test it.",
             "Remove the air. Do the cans still warm up? What does that tell you about radiation?",
             "Emitting: which surface cools fastest? Is the best absorber also the best emitter?",
             "Give one can fins. Explain why car radiators and computer heat sinks have fins.",
             "Start one can at 95 °C and one at 50 °C (same surface). Which loses temperature faster at first?",
         ]),
]

chapter_page("Ch 8 · Thermal Processes", "8a–8e", APPLETS, QUESTIONS, key="therm")
