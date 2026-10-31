import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.charge_current import QUESTIONS

APPLETS = [
    dict(name="Charge and Current Lab", file="charge-current", height=800,
         blurb="**Charges**: set two balls to + or − and see whether they attract or repel. **Current in a wire**: a battery drives charge round a loop through a resistance wire whose length and thickness you control. Show the flow as electrons or as conventional current, and watch the charge counter add up Q = I t.",
         tasks=[
             "**Predict:** which way will the electrons go? Then switch to conventional current. Which way now?",
             "Reset the counter and count 10 s. Compare the charge with current × time.",
             "Double the length of the wire. What happens to R, to I and to the speed of the dots?",
             "Find two different wires that give the same resistance (hint: length and thickness can cancel out).",
             "Set the e.m.f. to 0 V. What happens, and why?",
         ]),
]

chapter_page("Ch 12 · Electric Charge and Current of Electricity", "12a–12j", APPLETS, QUESTIONS, key="cc")
