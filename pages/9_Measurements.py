import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.measurements import QUESTIONS

APPLETS = [
    dict(name="Measuring Lab", file="measurements", height=780,
         blurb="Two tools. **Scale of things** walks along powers of ten from an atom to the Earth, with the prefix for each step. **Which instrument?** lets you pick an instrument for a job and checks its range and its precision against the reading.",
         tasks=[
             "**Predict:** how many powers of ten separate an ant from the Earth? Slide between them and count.",
             "Find the prefix for 10⁻⁶ m. Name something about that size.",
             "Which instrument? → thickness of a coin. Try every instrument. Which ones have the range? Which have the precision?",
             "Time for ONE swing versus 20 swings with the hand stopwatch: why does the percentage change so much?",
             "Internal diameter of a cup: why do the calipers win over the micrometer here?",
         ]),
]

chapter_page("Ch 1 · Measurements", "1a–1f", APPLETS, QUESTIONS, key="meas")
