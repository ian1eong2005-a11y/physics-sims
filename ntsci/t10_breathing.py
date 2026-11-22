import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "🫁 Breathing system", "file": "breath-lungs", "height": 880,
     "try": ["Tap each number to see what that part does.", "Watch the diaphragm. Does it move up or down when we breathe in?", "Choose **Choking**. Why can no air reach the lungs?"]},
    {"name": "🌬️ Inhaled and exhaled air", "file": "breath-air", "inq": True,
     "try": ["Bubble inhaled air, then exhaled air, through the limewater. Which turns milky faster?", "What happens to the cobalt chloride paper?"]},
    {"name": "🚭 Smoking", "file": "breath-smoke", "height": 880,
     "try": ["Sort all 8 cards."]},
]

QUESTIONS = [
    dict(type="match", pic="🫁", q="Match each part to its job.",
         pairs=[("Windpipe", "carries air to the bronchi"), ("Lungs", "oxygen goes into the blood"), ("Diaphragm", "muscle that helps us breathe"), ("Ribcage", "protects the lungs")],
         why="Each part of the breathing system has its own job."),
    dict(type="mcq", pic="⚡", q="What is respiration?",
         options=["using oxygen in our cells to release energy from food", "moving air in and out of the lungs", "digesting food"], answer=0,
         why="Breathing brings in oxygen; respiration uses it to release energy."),
    dict(type="mcq", pic="😮‍💨", q="Compared with inhaled air, exhaled air has…",
         options=["more carbon dioxide and less oxygen", "more oxygen and less carbon dioxide", "exactly the same gases"], answer=0,
         why="Our cells use oxygen and make carbon dioxide."),
    dict(type="mcq", pic="🥛", q="Which test shows carbon dioxide?",
         options=["limewater turns milky", "cobalt chloride paper turns pink", "litmus turns red"], answer=0,
         why="Limewater tests for carbon dioxide."),
    dict(type="mcq", pic="🩷", q="Blue cobalt chloride paper turns pink. This shows…",
         options=["water vapour", "carbon dioxide", "oxygen"], answer=0,
         why="Cobalt chloride paper tests for water vapour."),
    dict(type="mcq", pic="🍬", q="Choking is dangerous because…",
         options=["the windpipe is blocked, so no air reaches the lungs", "the stomach is full", "the heart stops pumping"], answer=0,
         why="Food blocking the windpipe stops air reaching the lungs."),
    dict(type="multi", pic="🚬", q="Which can be caused by smoking?",
         options=["bronchitis", "lung cancer", "stronger lungs"], answer=[0, 1],
         why="Smoking damages the breathing system."),
    dict(type="mcq", pic="👶", q="Passive smoking means…",
         options=["breathing in other people's cigarette smoke", "smoking only a little", "smoking outdoors"], answer=0,
         why="Non-smokers are harmed by breathing in other people's smoke."),
]

topic_page(10, "Breathing", "🫁", "G1 Science K123 · 3.3 Breathing: the respiratory system, inhaled and exhaled air, effects of smoking", APPLETS, QUESTIONS, key="nt10")
