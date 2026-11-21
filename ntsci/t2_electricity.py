import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "🔋 Current and voltage", "file": "elec-meters", "inq": True, "height": 860,
     "try": ["Series: put the meter at P, Q, then R. What do you notice?", "Parallel: add the readings at Q and R. Compare with P.", "Change the meter to **Voltage** and test the battery and each lamp."]},
    {"name": "💡 Lamps: series or parallel", "file": "elec-home", "inq": True, "height": 860,
     "try": ["Series: add lamps one at a time. What happens to the brightness?", "Parallel: add lamps. What happens to the brightness now?", "Make **lamp 1 blow**. Which circuit keeps the other lamps on?"]},
    {"name": "🎚️ Adding resistors", "file": "elec-resistors", "inq": True,
     "try": ["Add resistors in series. Does the reading go up or down?", "Now join them in parallel. Up or down?"]},
    {"name": "💰 Cost of electricity", "file": "elec-cost", "inq": True, "height": 900,
     "try": ["Which appliance costs the most for 10 hours?", "Halve the hours. What happens to the cost?", "Find the **voltage** and the **power** on the label."]},
]

QUESTIONS = [
    dict(type="mcq", pic="🔁", q="In a series circuit, the current is…",
         options=["biggest near the battery", "the same at every point", "zero after the first lamp"], answer=1,
         why="There is only one path, so the same current flows through every part."),
    dict(type="num", pic="🔀", q="Parallel circuit: one branch has 0.6 A and the other has 0.3 A. What is the current from the battery?", answer=0.9, unit="A",
         why="The current from the battery is the sum of the branch currents: 0.6 + 0.3 = 0.9 A."),
    dict(type="num", pic="🔋", q="Series circuit: a 6 V battery and two lamps. One lamp has 2 V across it. What is the voltage across the other lamp?", answer=4, unit="V",
         why="In series the voltages add up to the battery voltage: 6 − 2 = 4 V."),
    dict(type="mcq", pic="💡", q="In a parallel circuit, each branch gets…",
         options=["half the battery voltage", "the full battery voltage", "no voltage"], answer=1,
         why="The voltage is the same across every branch of a parallel circuit."),
    dict(type="mcq", pic="🎚️", q="You connect more resistors in SERIES. The total resistance…",
         options=["increases", "decreases", "stays the same"], answer=0,
         why="The current has to go through every resistor, one after another."),
    dict(type="mcq", pic="🎚️", q="You connect more resistors in PARALLEL. The total resistance…",
         options=["increases", "decreases", "stays the same"], answer=1,
         why="There are more paths for the current."),
    dict(type="multi", pic="🏠", q="Why are home appliances connected in parallel?",
         options=["Each one can be switched on and off on its own", "If one breaks, the others still work", "Each one gets the full voltage", "They use no electricity"], answer=[0, 1, 2],
         why="These are the three advantages of connecting appliances in parallel."),
    dict(type="mcq", pic="🫖", q="A kettle label says 230 V, 2000 W. What does 2000 W tell you?",
         options=["its voltage rating", "its power rating", "its current", "its cost"], answer=1,
         why="W (watt) is the unit of power. 230 V is the voltage rating."),
    dict(type="num", pic="🔌", q="An iron uses 230 V and a current of 4 A. What is its power?", answer=920, unit="W",
         why="Power = current × voltage = 4 A × 230 V = 920 W."),
    dict(type="num", pic="♨️", q="A 2 kW heater is used for 3 hours. How much energy does it use?", answer=6, unit="kWh",
         why="Energy = power × time = 2 kW × 3 h = 6 kWh."),
    dict(type="num", pic="💰", q="1 kWh costs $0.30. What is the cost of 6 kWh?", answer=1.8, tol=0.001, unit="$",
         why="Cost = 6 kWh × $0.30 = $1.80."),
    dict(type="mcq", pic="🌍", q="Which of these reduces the wastage of electrical energy?",
         options=["leaving the TV on when nobody is watching", "switching off appliances that are not in use", "opening the fridge door often", "using old lamps instead of LED lamps"], answer=1,
         why="Switch off what you are not using, and choose energy-efficient appliances."),
    dict(type="mcq", pic="📟", q="Which instrument measures current, voltage and resistance?",
         options=["stopwatch", "multimeter", "measuring cylinder", "thermometer"], answer=1,
         why="A multimeter can be set to measure current (A), voltage (V) or resistance (Ω)."),
]

topic_page(2, "Electricity", "🔋", "G1 Science K123 · 1.2 Electricity: series and parallel circuits, electric power and energy", APPLETS, QUESTIONS, key="nt2")
