import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    dict(name="🧴 Swinging bottle", file="energy-swing", inq=True,
         **{"try": ["Let go from **High**. Does the bottle come back higher than the start?", "Watch the two energy bars. When is the kinetic energy biggest?", "Now **give it a push**. Why does it come back higher?"]}),
    dict(name="♨️ Heater power", file="energy-heater", inq=True,
         **{"try": ["Which heater boils the water fastest?", "Look at **Energy used**. Is it the same every time?"]}),
    dict(name="🌡️ Hot meets cold", file="energy-hotcold", inq=True,
         **{"try": ["Which way do the red arrows point: from hot to cold, or cold to hot?", "When do the arrows stop?"]}),
    dict(name="🏭 Power station", file="energy-grid", inq=True, height=900,
         **{"try": ["Tap each number to see what the part does.", "Switch the power lines to **Low** voltage. What happens to the lamp at home?", "Press **Test me**."]}),
    dict(name="⚡ Forms of energy", file="energy-forms", height=860,
         **{"try": ["Sort all 10 cards. Can you get them all right first time?"]}),
]
QUESTIONS = [
    dict(type="mcq", pic="🔋", q="What form of energy is stored in a battery?",
         options=["chemical potential energy", "kinetic energy", "sound energy", "light energy"], answer=0,
         why="Batteries, food and fuels store chemical potential energy."),
    dict(type="mcq", pic="🏹", q="A stretched rubber band stores…",
         options=["gravitational potential energy", "elastic potential energy", "thermal energy", "electrical energy"], answer=1,
         why="Stretched or squashed things store elastic potential energy."),
    dict(type="mcq", pic="🥄", q="A hot spoon is put into cold water. Which way does thermal energy move?",
         options=["from the water to the spoon", "from the spoon to the water", "it does not move"], answer=1,
         why="Thermal energy moves from the hotter place to the colder place."),
    dict(type="mcq", pic="🌡️", q="When does the thermal energy stop moving?",
         options=["when the spoon is hotter than the water", "when both are at the same temperature", "after exactly one minute"], answer=1,
         why="It stops when both reach the same temperature."),
    dict(type="mcq", pic="♻️", q="Complete the sentence: Energy cannot be created or ______.",
         options=["changed", "destroyed", "moved"], answer=1,
         why="This is the principle of conservation of energy. Energy only changes from one form to another."),
    dict(type="mcq", pic="🧴", q="A swinging bottle is at its lowest point and moving fastest. Here it has the most…",
         options=["kinetic energy", "gravitational potential energy", "chemical potential energy"], answer=0,
         why="At the bottom the potential energy has changed into kinetic energy."),
    dict(type="num", pic="♨️", q="A heater changes 6000 J of energy in 3 s. What is its power?", answer=2000, unit="W",
         why="Power = energy ÷ time = 6000 J ÷ 3 s = 2000 W."),
    dict(type="num", pic="💡", q="A 100 W lamp is on for 10 s. How much energy does it change?", answer=1000, unit="J",
         why="Energy = power × time = 100 W × 10 s = 1000 J."),
    dict(type="match", pic="🏭", q="In a fossil fuel power station, which form of energy is in each part?",
         pairs=[("Fuel (coal, oil, gas)", "chemical potential"), ("Hot steam from the boiler", "thermal"), ("Spinning turbine", "kinetic"), ("Out of the generator", "electrical")],
         why="Chemical → thermal → kinetic → electrical."),
    dict(type="mcq", pic="🗼", q="Why is electricity sent through the power lines at a very high voltage?",
         options=["so that it travels faster", "so that less energy is wasted as heat", "so that it is safer to touch", "so that more fuel is used"], answer=1,
         why="High voltage means less energy is lost as heat in the lines."),
    dict(type="mcq", pic="🏠", q="A step-down transformer near your home…",
         options=["makes the voltage higher", "makes the voltage lower", "stores electricity", "makes electricity"], answer=1,
         why="Step-down transformers lower the voltage so that it is safer to use."),
]

topic_page(1, "Energy", "⚡", "G1 Science K123 · 1.1 Energy: forms of energy, conservation of energy, power, generating and sending electricity", APPLETS, QUESTIONS, key="nt1")
