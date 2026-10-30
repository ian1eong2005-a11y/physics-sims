import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.forces import QUESTIONS

APPLETS = [
    dict(name="Resultant Force Trolley", file="resultant-force", height=820,
         blurb="Push a trolley against friction. Arrows show every force; the purple arrow is the resultant. Watch the velocity–time graph, especially when the resultant becomes zero.",
         tasks=[
             "**Predict:** the trolley is moving and you press 'Balance the forces'. Will it stop, keep going at the same speed, or speed up? Test it.",
             "Set friction to 0 ('No friction') and let go of the push (F = 0). What does the trolley do? Why does it never happen on a real road?",
             "Tick 'Air resistance'. Why does the speed stop increasing even though you are still pushing? What is the resultant force then?",
             "Make the trolley decelerate. What must be true about the forces?",
         ]),
    dict(name="Moments See-saw", file="moments-seesaw", height=800,
         blurb="Drag weights onto a pivoted beam. Each weight gives a moment = weight × distance. The beam balances only when clockwise and anticlockwise totals match.",
         tasks=[
             "**Predict:** a 10 N weight at 20 cm on the right. Where must a 5 N weight go on the left to balance it? Test it.",
             "Find three different ways to balance a 10 N weight at 30 cm using the weights in the tray.",
             "Press 'New mystery weight'. Balance it with known weights and work out its value before you press Reveal.",
             "Tick 'Pivot off-centre'. With no weights the beam tips. Where must the beam's own weight be acting?",
         ]),
]

chapter_page("Ch 4–5 · Dynamics and Turning Effect of Forces", "4a–4d, 5a–5e", APPLETS, QUESTIONS, key="forces")
