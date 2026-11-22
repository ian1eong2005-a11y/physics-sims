import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "⚗️ Separating mixtures", "file": "chem-separate", "height": 860,
     "try": ["Watch each method. What is left behind, and what comes through?", "Which method gives you pure water from seawater?"]},
    {"name": "🎨 Chromatography", "file": "chem-chroma", "inq": True,
     "try": ["Test each food colouring. Which ones are mixtures?", "Which dye travels furthest up the paper?"]},
    {"name": "🧪 Choose the method", "file": "chem-choose", "height": 900,
     "try": ["Sort all 8 cards. Can you get them all right first time?"]},
    {"name": "🌈 pH", "file": "chem-ph", "inq": True,
     "try": ["Test every liquid. Which are acidic, neutral and alkaline?", "What happens to blue and red litmus paper each time?"]},
    {"name": "💊 Neutralisation", "file": "chem-neutral", "inq": True,
     "try": ["How many antacid tablets make the acid neutral?", "What colour is the indicator at pH 7?"]},
    {"name": "🫧 Acid reactions", "file": "chem-acid", "inq": True,
     "try": ["Which ones fizz? Which gas is made each time?"]},
    {"name": "🔩 Rusting", "file": "chem-rust", "inq": True,
     "try": ["Which nail rusts? What does it have that the others do not?", "Why does the tin-plated nail not rust?"]},
]

QUESTIONS = [
    dict(type="mcq", pic="🍵", q="Which method removes tea leaves from a cup of tea?",
         options=["filtration", "evaporation", "distillation", "chromatography"], answer=0,
         why="The leaves are too big to pass through the strainer."),
    dict(type="mcq", pic="🧂", q="Which method gets salt from salt water?",
         options=["filtration", "evaporation", "chromatography"], answer=1,
         why="The water evaporates and the salt is left behind."),
    dict(type="mcq", pic="🚰", q="Which method gets pure drinking water from seawater?",
         options=["filtration", "distillation", "chromatography"], answer=1,
         why="Distillation boils the water and cools the steam back into pure water."),
    dict(type="mcq", pic="🎨", q="A green food colouring gives two spots in paper chromatography. It is…",
         options=["a single dye", "a mixture of two dyes", "not a dye"], answer=1,
         why="Each spot is a different dye."),
    dict(type="mcq", pic="🍳", q="A chemical reaction is a change that…",
         options=["makes new products", "only changes the shape", "can always be undone easily"], answer=0,
         why="Cooking food, burning fuel and rusting all make new substances."),
    dict(type="match", pic="🐢", q="How can each change be slowed down?",
         pairs=[("Decaying of food", "food preservation"), ("Burning of fuel", "reduce the oxygen or fuel supply"), ("Rusting of iron cans", "tin-plating")],
         why="Each everyday chemical reaction can be slowed down."),
    dict(type="mcq", pic="🔩", q="An iron nail rusts only when it touches…",
         options=["water only", "air only", "both air and water"], answer=2,
         why="Rusting needs both air (oxygen) and water."),
    dict(type="mcq", pic="🍋", q="Lemon juice has a pH of 2. It is…",
         options=["acidic", "neutral", "alkaline"], answer=0,
         why="Below 7 is acidic."),
    dict(type="mcq", pic="🧼", q="Soap solution turns red litmus paper blue. Soap is…",
         options=["an acid", "an alkali", "neutral"], answer=1,
         why="Alkalis turn red litmus blue; acids turn blue litmus red."),
    dict(type="mcq", pic="💧", q="Pure water has a pH of…",
         options=["1", "7", "14"], answer=1,
         why="pH 7 is neutral."),
    dict(type="mcq", pic="🧁", q="Baking soda (a carbonate) reacts with an acid. Which gas is made?",
         options=["oxygen", "hydrogen", "carbon dioxide"], answer=2,
         why="Acid + carbonate → salt + water + carbon dioxide."),
    dict(type="mcq", pic="🔩", q="An acid reacts with a metal. Which gas is made?",
         options=["hydrogen", "carbon dioxide", "no gas"], answer=0,
         why="Acid + metal → salt + hydrogen."),
    dict(type="mcq", pic="💊", q="An antacid neutralises stomach acid. The products are…",
         options=["salt and water", "salt and hydrogen", "acid and gas"], answer=0,
         why="Acid + base → salt + water. This is neutralisation."),
    dict(type="mcq", pic="🧪", q="Which instrument measures volume of a liquid?",
         options=["measuring cylinder", "spring balance", "thermometer"], answer=0,
         why="A measuring cylinder measures the volume of a liquid."),
]

topic_page(6, "Food Chemistry", "🧪", "G1 Science K123 · 2.2 Food Chemistry: separation techniques, chemical reactions, acids and bases", APPLETS, QUESTIONS, key="nt6")
