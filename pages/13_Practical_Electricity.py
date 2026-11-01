import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.practical_electricity import QUESTIONS

APPLETS = [
    dict(name="Home Electricity", file="home-electricity", height=820,
         blurb="**Toaster fault**: a real toaster (or its circuit diagram) with the current drawn as moving dots. Make the live wire touch the metal case and follow where the current goes, with and without the earth wire and the fuse, and with someone touching the case. Also: **wiring a plug**, a **switch in the live or neutral** wire, and **appliances & cost**.",
         tasks=[
             "Toaster fault: follow the dots in normal use. Then make the fault happen. Where does the current go? What happens to the fuse?",
             "Untick the earth and repeat. What is the case at now? Tick Someone touches the case: where does the current go?",
             "Tick earth, untick the fuse. Is the person safe? Is the toaster safe?",
             "Switch on the neutral wire, OFF. Is the lamp safe to touch? Why not?",
             "**Predict:** which appliances need a 13 A fuse? Check each one.",
             "Find the appliance that costs most per day at 2 hours, and the one that costs least. What decides it?",
             "Explain to a partner why heating appliances draw such large currents (use I = P/V).",
         ]),
]

chapter_page("Ch 14 · Practical Electricity", "14a–14i", APPLETS, QUESTIONS, key="pe")
