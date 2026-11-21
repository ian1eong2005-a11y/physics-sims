import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "🪴 What plants need", "file": "food-needs", "inq": True,
     "try": ["Take away **light**. What does the plant look like after 14 days?", "Take away each thing in turn. Which is the worst for the plant?"]},
    {"name": "🌱 Fertiliser", "file": "food-fertiliser", "inq": True,
     "try": ["Grow the plant with no fertiliser, then with 2 spoons. Compare the heights.", "Look at the colour of the leaves."]},
    {"name": "🍌 Ripening bananas", "file": "food-banana", "inq": True,
     "try": ["How many days does the green banana take on its own?", "Put a ripe banana in the bag. What is different?"]},
    {"name": "🚜 Farm and pond", "file": "food-farm", "inq": True, "height": 840,
     "try": ["Use **fertiliser**. What happens to the crop? What happens to the pond?", "Use **pesticide**. What happens to the bird?", "Use **ladybirds**. Why is this better for the environment?"]},
    {"name": "🌾 Farming methods", "file": "food-problems", "height": 860,
     "try": ["Sort all 10 cards. Can you get them all right first time?"]},
]

QUESTIONS = [
    dict(type="multi", pic="🪴", q="What do plants need for photosynthesis and growth?",
         options=["light", "water", "air", "nutrients", "the right pH", "a dark cupboard"], answer=[0, 1, 2, 3, 4],
         why="Plants need air, light, water, nutrients and an appropriate pH."),
    dict(type="mcq", pic="🌍", q="Why do we need to improve food production?",
         options=["The world population is growing, but the space to grow food is limited", "People are eating less food", "There is too much farmland"], answer=0,
         why="More people need more food, but there is only limited land."),
    dict(type="mcq", pic="🧪", q="Fertilisers help crops because they…",
         options=["kill insects", "add nutrients to the soil", "kill weeds", "give shade"], answer=1,
         why="Fertilisers add nutrients that plants need to grow well."),
    dict(type="match", pic="☠️", q="What does each one kill?",
         pairs=[("Pesticide", "pests such as insects"), ("Herbicide", "weeds")],
         why="Pesticides kill pests. Herbicides kill weeds."),
    dict(type="mcq", pic="🟢", q="Too much fertiliser is washed into a pond. What happens?",
         options=["The water becomes cleaner", "Algae and water weeds grow too much", "The fish grow bigger", "Nothing happens"], answer=1,
         why="Fertiliser in the water makes algae and water weeds grow too much."),
    dict(type="mcq", pic="🐦", q="A bird never touches the pesticide spray. How can the pesticide still harm it?",
         options=["Harmful substances pass along the food chain", "Birds are afraid of farmers", "The pesticide makes the sun too hot"], answer=0,
         why="The bird eats pests that have pesticide in them."),
    dict(type="multi", pic="🔥", q="Which problems are caused by slash-and-burn farming?",
         options=["haze that makes it hard to breathe", "soil erosion after the trees are gone", "too many trees", "cleaner air"], answer=[0, 1],
         why="Burning causes haze. Cutting down the forest (deforestation) leads to soil erosion."),
    dict(type="mcq", pic="🐞", q="Biological control means…",
         options=["spraying more pesticide", "using a predator to eat the pests", "burning the field", "adding more fertiliser"], answer=1,
         why="Predators control the pests, so less pesticide is needed."),
    dict(type="mcq", pic="🍌", q="Ripe fruit gives off a plant hormone. What does it do to other fruit nearby?",
         options=["makes it ripen faster", "makes it ripen more slowly", "makes it turn green"], answer=0,
         why="Plant hormones are used to control the ripening of fruits."),
    dict(type="multi", pic="🌿", q="What are plant hormones used for?",
         options=["as weed killers", "to control the ripening of fruits", "to control the growth of plants", "to make haze"], answer=[0, 1, 2],
         why="Plant hormones are used as weed killers, and to regulate growth and ripening."),
    dict(type="mcq", pic="🐔", q="Intensive farming means…",
         options=["producing a lot of food from a small space", "growing food only for one family", "leaving the land empty"], answer=0,
         why="Intensive farming of crops and farm animals (such as chickens and fish) produces more food from limited space."),
]

topic_page(5, "Sources of Food", "🌱", "G1 Science K123 · 2.1 Sources of Food: what plants need, growing more food, problems and better ways", APPLETS, QUESTIONS, key="nt5")
