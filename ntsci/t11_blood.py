import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "❤️ Exercise and pulse", "file": "blood-pulse", "inq": True,
     "try": ["Try each activity. What happens to the pulse rate and breathing rate?", "Why do the muscles need more blood during exercise?"]},
    {"name": "🫀 Heart and lungs", "file": "blood-heart", "height": 900,
     "try": ["Tap each number to see what that part does.", "Follow the blood: where does it pick up oxygen?", "Press **Test me**."]},
    {"name": "🩸 Parts of the blood", "file": "blood-parts", "height": 860,
     "try": ["Match all 7 jobs."]},
    {"name": "🧈 Plaque", "file": "blood-plaque", "inq": True,
     "try": ["Fast-forward 30 years for each lifestyle. How much of the artery is blocked?"]},
]

QUESTIONS = [
    dict(type="match", pic="🩸", q="Match each part of the blood to its job.",
         pairs=[("Plasma", "carries digested food and carbon dioxide"), ("Red blood cells", "carry oxygen"), ("White blood cells", "destroy bacteria and viruses"), ("Platelets", "help blood to clot")],
         why="Blood transports substances and defends the body."),
    dict(type="mcq", pic="🫁", q="Where does blood pick up oxygen?",
         options=["in the lungs", "in the stomach", "in the body cells"], answer=0,
         why="Blood takes in oxygen and gives out carbon dioxide in the lungs."),
    dict(type="mcq", pic="🫀", q="The left side of the heart pumps blood to…",
         options=["the rest of the body", "the lungs"], answer=0,
         why="The right side pumps to the lungs; the left side pumps to the body."),
    dict(type="match", pic="🩺", q="Match each blood vessel to its feature.",
         pairs=[("Artery", "thick wall, carries blood away from the heart"), ("Vein", "has valves, carries blood back to the heart"), ("Capillary", "wall one cell thick")],
         why="The structure of each vessel suits its job."),
    dict(type="multi", pic="🩺", q="Which can be used to check the condition of the circulatory system?",
         options=["blood pressure", "heart rate", "pulse rate", "hair colour"], answer=[0, 1, 2],
         why="Doctors measure these to check the heart and blood vessels."),
    dict(type="mcq", pic="🏃", q="During exercise, the pulse rate goes up because…",
         options=["the muscles need more oxygen and glucose", "the body is cold", "the muscles need less blood"], answer=0,
         why="The heart pumps faster to deliver more oxygen and glucose, and remove carbon dioxide."),
    dict(type="mcq", pic="🧈", q="Plaque in an artery to the heart can cause…",
         options=["a heart attack", "a broken bone", "constipation"], answer=0,
         why="Plaque narrows or blocks arteries. A blocked artery to the brain causes a stroke."),
    dict(type="multi", pic="🚬", q="Which raise the risk of heart disease and stroke?",
         options=["a diet high in fat", "smoking", "little physical activity", "regular exercise"], answer=[0, 1, 2],
         why="Diet, physical activity and smoking affect the risk."),
]

topic_page(11, "Blood Circulation", "❤️", "G1 Science K123 · 3.4 Blood Circulation: blood, the heart and blood vessels, exercise, heart disease", APPLETS, QUESTIONS, key="nt11")
