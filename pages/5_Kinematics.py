import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.kinematics import QUESTIONS

APPLETS = [
    dict(name="Kinematics Graph Matcher", file="kinematics-graphs", height=800,
         blurb="Pick a type of motion or drag your own speed–time graph. The car drives it while the distance–time graph draws itself. Hide the distance–time graph to make a prediction first.",
         tasks=[
             "**Predict:** choose 'Uniform acceleration' and hide the distance–time graph. Sketch what it will look like, then show it. Were you right? Why is it not a straight line?",
             "Switch between 'Uniform', 'Increasing' and 'Decreasing' acceleration. Watch the dashed tangent. Write one sentence for each about how the gradient changes.",
             "Choose 'Speed up, cruise, slow down'. Before pressing Play, work out the total distance from the areas. Then play to the end and check.",
             "Custom: drag the points to make a journey where the car travels exactly 100 m in 20 s. How many different graphs can your group find?",
         ]),
]

chapter_page("Ch 2 · Kinematics", "2c–2h", APPLETS, QUESTIONS, key="kin")
