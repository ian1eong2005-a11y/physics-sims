import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "🏁 Toy car race", "file": "force-car", "inq": True,
     "try": ["Race all three cars. Which line on the graph is steepest?", "Run the **bus**. What does the flat part of its line mean?", "Work out each average speed yourself, then check."]},
    {"name": "🏎️ Speeding up", "file": "force-accel", "inq": True,
     "try": ["Small push: by how much does the speed go up each second?", "Big push: what is the speed after 5 s? What is the acceleration?"]},
    {"name": "🔧 Turning effect", "file": "force-turn", "inq": True,
     "try": ["Push near the nut, then far from the nut. Which needs the smaller force?", "Why is a door handle far from the hinges?"]},
    {"name": "💪 Effects of a force", "file": "force-effects", "height": 860,
     "try": ["Sort all 11 cards. Can you get them all right first time?"]},
]

QUESTIONS = [
    dict(type="mcq", pic="⏱️", q="Which instrument measures a time interval?",
         options=["ruler", "digital stopwatch", "measuring tape", "electronic balance"], answer=1,
         why="A digital stopwatch measures time. A ruler and a measuring tape measure length."),
    dict(type="mcq", pic="🧽", q="You squeeze a sponge. The force changes the sponge's…",
         options=["shape", "colour", "mass"], answer=0,
         why="A force can change the shape or size of an object."),
    dict(type="mcq", pic="🎾", q="A player hits a tennis ball back over the net. The force changes the ball's…",
         options=["direction", "colour", "mass"], answer=0,
         why="A force can change the direction (and the speed) of a moving object."),
    dict(type="num", pic="🚗", q="A car travels 100 m in 20 s. What is its average speed?", answer=5, unit="m/s",
         why="Average speed = total distance ÷ total time = 100 m ÷ 20 s = 5 m/s."),
    dict(type="num", pic="🏃", q="A boy runs at an average speed of 4 m/s for 10 s. How far does he run?", answer=40, unit="m",
         why="Distance = speed × time = 4 m/s × 10 s = 40 m."),
    dict(type="mcq", pic="📈", q="On a distance-time graph, a flat (horizontal) line means the object is…",
         options=["moving fast", "not moving", "speeding up"], answer=1,
         why="The distance is not changing, so the object is at rest."),
    dict(type="mcq", pic="📈", q="On a distance-time graph, a steeper line means…",
         options=["a slower speed", "a faster speed", "the object has stopped"], answer=1,
         why="A steeper line covers more distance in each second."),
    dict(type="num", pic="🏎️", q="A car's speed goes from 0 m/s to 20 m/s in 5 s. What is its acceleration?", answer=4, unit="m/s²",
         why="Acceleration = change in speed ÷ time = 20 m/s ÷ 5 s = 4 m/s²."),
    dict(type="mcq", pic="⏩", q="Acceleration tells us…",
         options=["how far an object moves", "how quickly the speed changes", "how heavy an object is"], answer=1,
         why="Acceleration = change in speed ÷ time taken."),
    dict(type="mcq", pic="🚪", q="A door is easiest to open when you push…",
         options=["near the hinges", "in the middle", "far from the hinges"], answer=2,
         why="The turning effect is bigger when the force is further from the pivot."),
    dict(type="mcq", pic="🔧", q="The turning effect of a force is called its…",
         options=["speed", "moment", "power", "frequency"], answer=1,
         why="The moment of a force is its turning effect."),
]

topic_page(4, "Effects of Force", "🏎️", "G1 Science K123 · 1.4 Effects of Force: what forces do, speed, acceleration, distance-time graphs, turning effect", APPLETS, QUESTIONS, key="nt4")
