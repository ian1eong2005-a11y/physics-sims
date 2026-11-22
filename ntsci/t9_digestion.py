import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "🍽️ Digestive system", "file": "dig-organs", "height": 900,
     "try": ["Tap each number to see what that part does.", "Follow the burger from the mouth to the anus.", "Press **Test me**."]},
    {"name": "🧪 Enzymes at work", "file": "dig-enzyme", "inq": True, "height": 860,
     "try": ["Try every pH. At which pH are there the most bubbles?", "Change to **Temperature**. What happens at 70 °C?"]},
    {"name": "🥦 Healthy gut", "file": "dig-health", "height": 860,
     "try": ["Sort all 8 cards."]},
]

QUESTIONS = [
    dict(type="mcq", pic="🍔", q="Why do we need to digest food?",
         options=["to break big food molecules into small ones that can be absorbed", "to make food bigger", "to make food taste better"], answer=0,
         why="Only small molecules can pass into the blood."),
    dict(type="match", pic="🫃", q="Match each organ to its job.",
         pairs=[("Stomach", "mixes food with acid"), ("Small intestine", "absorbs digested food"), ("Large intestine", "absorbs water"), ("Liver", "makes bile")],
         why="Each organ has its own job."),
    dict(type="mcq", pic="🟢", q="Where is bile stored?",
         options=["gall bladder", "pancreas", "rectum"], answer=0,
         why="The liver makes bile; the gall bladder stores it."),
    dict(type="mcq", pic="🧪", q="Enzymes…",
         options=["speed up digestion", "slow down digestion", "are a kind of food"], answer=0,
         why="Enzymes speed up the rate of digestion."),
    dict(type="mcq", pic="🌡️", q="An enzyme works fastest at its…",
         options=["optimum temperature and pH", "highest temperature", "lowest pH"], answer=0,
         why="Each enzyme has an optimum temperature and pH."),
    dict(type="mcq", pic="🔥", q="At 70 °C an enzyme stops working because…",
         options=["it is destroyed by the heat", "it falls asleep", "it gets bigger"], answer=0,
         why="High temperatures destroy enzymes."),
    dict(type="mcq", pic="📈", q="An enzyme gives the most bubbles at pH 7 and fewer at pH 2 and pH 10. Its optimum pH is…",
         options=["2", "7", "10"], answer=1,
         why="The optimum is where the enzyme works fastest."),
    dict(type="multi", pic="🚽", q="How can constipation be prevented?",
         options=["eat more fibre", "drink plenty of water", "eat less fibre", "drink less water"], answer=[0, 1],
         why="Fibre and water keep faeces soft and moving."),
    dict(type="mcq", pic="🍺", q="Too much alcohol for many years can cause…",
         options=["a damaged liver or liver cancer", "stronger bones", "better eyesight"], answer=0,
         why="Excessive alcohol damages the liver."),
    dict(type="multi", pic="🍩", q="Which raise the risk of diabetes?",
         options=["a diet high in sugar", "little physical activity", "regular exercise", "eating vegetables"], answer=[0, 1],
         why="Diet and level of physical activity affect the risk of diabetes."),
]

topic_page(9, "Digestion", "🍽️", "G1 Science K123 · 3.2 Digestion: the digestive system, enzymes, problems of the digestive system", APPLETS, QUESTIONS, key="nt9")
