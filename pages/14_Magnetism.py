import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.magnetism import QUESTIONS

APPLETS = [
    dict(name="Magnet and Motor Lab", file="magnetism", height=820,
         blurb="Four modes. **Bar magnets**: field lines and a compass you can drag; one magnet, or two facing N–S or N–N. **Field of a current**: a straight wire or a solenoid. **Force on a wire**: flip the current or the field and watch the force; Fleming's left-hand rule is drawn for you. **Iron or steel?**: induced magnetism, temporary versus permanent.",
         tasks=[
             "**Predict:** drag the compass to the N pole. Which way does the red end point? Now the S pole.",
             "N facing N: find the point between the magnets where the compass needle has no preferred direction.",
             "Straight wire: increase the current, then reverse it. Describe the two changes.",
             "Force on a wire: hide the force arrow, predict with your left hand, then reveal. Try all four combinations.",
             "Iron or steel: magnetise both bars, move the magnet away. Which bar could you use to make a compass needle?",
         ]),
]

chapter_page("Ch 15 · Magnetism and Electromagnetism", "15a–15i", APPLETS, QUESTIONS, key="mag")
