import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "🍞 Protect my bread", "file": "safe-bread", "inq": True,
     "try": ["Leave the bread on the table for 7 days. What grows on it?", "Try each method. Which thing does each one take away from the microbes?"]},
    {"name": "🥛 Heat and milk", "file": "safe-milk", "inq": True,
     "try": ["Compare unheated milk with pasteurised milk after 5 days.", "Why does spoilt milk have a lower pH?"]},
    {"name": "🥫 Preservation methods", "file": "safe-methods", "height": 900,
     "try": ["Sort all 10 foods. Can you get them all right first time?"]},
    {"name": "🧂 Food additives", "file": "safe-additives", "height": 860,
     "try": ["Sort all 8 additives."]},
]

QUESTIONS = [
    dict(type="mcq", pic="🦠", q="Microbes are…",
         options=["very small living things, such as bacteria and fungi", "tiny pieces of dust", "chemicals added to food"], answer=0,
         why="Microbes are living things too small to see without a microscope."),
    dict(type="match", pic="🍞", q="Which microbe causes each change?",
         pairs=[("Milk turns sour", "bacteria"), ("Bread grows fluffy patches", "mould (a fungus)")],
         why="Bacteria spoil milk. Mould grows on bread."),
    dict(type="mcq", pic="🛑", q="How can we stop food from spoiling?",
         options=["stop or slow down the microbes", "add more microbes", "keep it warm and wet"], answer=0,
         why="Stopping or reducing microbial activity prevents food spoilage."),
    dict(type="multi", pic="🧫", q="What do microbes need to grow quickly?",
         options=["water", "oxygen", "warmth", "freezing cold"], answer=[0, 1, 2],
         why="Take one of these away and the microbes slow down or stop."),
    dict(type="match", pic="🥫", q="How does each method stop the microbes?",
         pairs=[("Pickling in vinegar", "lowers the pH"), ("Vacuum packaging", "reduces oxygen"), ("Drying", "reduces water"), ("Canning", "high temperature"), ("Freezing", "low temperature")],
         why="Each method takes away something the microbes need, or kills them."),
    dict(type="mcq", pic="🥛", q="Pasteurisation keeps milk fresh because it…",
         options=["heats the milk to kill most microbes", "freezes the milk", "adds sugar"], answer=0,
         why="Pasteurisation uses high temperature to reduce microbial activity."),
    dict(type="mcq", pic="🍓", q="Why is a lot of sugar added to jam?",
         options=["as a preservative", "as a nutritional supplement", "as a food colouring"], answer=0,
         why="Salt, sugar, vinegar and sulfur dioxide are preservatives."),
    dict(type="mcq", pic="🥣", q="Vitamins added to breakfast cereal are…",
         options=["preservatives", "nutritional supplements", "texture modifiers"], answer=1,
         why="Minerals and vitamins are nutritional supplements."),
    dict(type="mcq", pic="🍬", q="Food colouring in sweets is added to…",
         options=["stop microbes", "change how the food looks", "add vitamins"], answer=1,
         why="Colourings and starch are texture and appearance modifiers."),
    dict(type="mcq", pic="🍞", q="In the bread investigation, why do we keep one slice on the table?",
         options=["it is the control, to compare with", "it is the tastiest", "it stops mould"], answer=0,
         why="The control shows what happens with no preservation."),
]

topic_page(7, "Food Safety", "🥫", "G1 Science K123 · 2.3 Food Safety: microbes and food spoilage, food preservation, food additives", APPLETS, QUESTIONS, key="nt7")
