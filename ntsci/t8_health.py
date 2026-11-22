import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "🧫 Germ killers", "file": "health-germs", "inq": True,
     "try": ["Which plate has the most colonies? Which has the fewest?", "Why do we need the plate with water only?"]},
    {"name": "💊 Antibiotic course", "file": "health-antibiotic", "inq": True,
     "try": ["Stop the antibiotic after 3 days. What happens to the bacteria after that?", "Now take the full 7-day course."]},
    {"name": "⚖️ BMI", "file": "health-bmi", "inq": True, "height": 860,
     "try": ["Set a mass of 50 kg and a height of 1.60 m. Work out the BMI yourself, then check.", "Find a mass that is in the healthy range for a height of 1.70 m."]},
    {"name": "🥗 Balanced diet", "file": "health-diet", "height": 900,
     "try": ["Match all 7 nutrients to their jobs."]},
    {"name": "🦴 Bones and joints", "file": "health-joints", "height": 900,
     "try": ["Match all 7 words."]},
]

QUESTIONS = [
    dict(type="multi", pic="💪", q="Which are ways to keep good physical health?",
         options=["an active lifestyle", "a balanced diet", "enough rest", "good hygiene", "skipping meals to lose weight"], answer=[0, 1, 2, 3],
         why="Undereating and over-exercising to lose weight are health risks."),
    dict(type="mcq", pic="🥗", q="A balanced diet means…",
         options=["eating all the nutrients in the right amounts", "eating only vegetables", "eating as little as possible"], answer=0,
         why="It has carbohydrates, fats, proteins, fibre, minerals, vitamins and water in the right amounts."),
    dict(type="match", pic="🍽️", q="Match each nutrient to its job.",
         pairs=[("Carbohydrates", "main source of energy"), ("Proteins", "growth and repair"), ("Dietary fibre", "prevents constipation"), ("Calcium", "strong bones and teeth")],
         why="Each nutrient has its own job."),
    dict(type="num", pic="⚖️", q="A student has a mass of 64 kg and a height of 1.6 m. What is their BMI? (BMI = mass ÷ (height × height))", answer=25, tol=0.05,
         why="64 ÷ (1.6 × 1.6) = 64 ÷ 2.56 = 25."),
    dict(type="mcq", pic="🦴", q="Bones become weak and break easily. This is…",
         options=["osteoporosis", "a sprain", "arthritis"], answer=0,
         why="Too little calcium, vitamin D and exercise raise the risk."),
    dict(type="match", pic="🦵", q="Match each part of a joint to its job.",
         pairs=[("Cartilage", "stops the bones rubbing together"), ("Ligament", "holds the bones together")],
         why="Cartilage covers the ends of bones; ligaments hold them together."),
    dict(type="mcq", pic="🦶", q="A ligament is stretched too far or torn. This is a…",
         options=["sprain", "fracture", "dislocation"], answer=0,
         why="A fracture is a broken bone; a dislocation is a bone pushed out of its joint."),
    dict(type="mcq", pic="🦠", q="Diseases can be caused by…",
         options=["bacteria or viruses", "vitamins", "exercise"], answer=0,
         why="Bacteria and viruses can cause diseases."),
    dict(type="mcq", pic="🧴", q="Antiseptics and disinfectants…",
         options=["reduce the growth of microbes", "help microbes grow", "are vitamins"], answer=0,
         why="They are antimicrobial agents."),
    dict(type="mcq", pic="💊", q="Why must you finish the whole course of antibiotics?",
         options=["so that no bacteria are left alive to multiply again", "because the tablets taste nice", "because antibiotics kill viruses"], answer=0,
         why="Stopping early leaves some bacteria alive, and they multiply again."),
    dict(type="mcq", pic="💉", q="Diseases caused by bacteria and viruses may be prevented by…",
         options=["vaccinations", "eating more sugar", "skipping sleep"], answer=0,
         why="Vaccinations help prevent these diseases."),
    dict(type="multi", pic="🧬", q="Which of these are hereditary (passed on from parents)?",
         options=["sickle cell disease", "thalassemia", "colour deficiency", "a cold"], answer=[0, 1, 2],
         why="A cold is caused by a virus."),
    dict(type="mcq", pic="🏥", q="What is a limitation of an organ transplant?",
         options=["the body may reject the new organ", "it always works perfectly", "it needs no medicine"], answer=0,
         why="Tissue rejection is a limitation. Kidney dialysis needs lifelong treatment."),
]

topic_page(8, "Staying Healthy", "💪", "G1 Science K123 · 3.1 Staying Healthy: good physical health, BMI, bones and joints, microbes and disease", APPLETS, QUESTIONS, key="nt8")
