import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.lss_ecosystems import QUESTIONS

APPLETS = [
    dict(name="Ecosystem Lab", file="ecosystems", height=880,
         blurb="Four modes. **Food web**: click an organism, make its population increase or decrease, and follow the effects one step at a time; trace every food chain. **Energy and nutrients**: 90% of the energy is lost as heat at each stage; switch the decomposers off (G3). **Relationships**: predator–prey, mutualism and parasitism. **Habitats and adaptations**: physical factors, data logger probes (G3), structural and behavioural adaptations, and climate change.",
         tasks=[
             "**Predict:** if the snake population decreases, what happens to the frogs? To the hawks? Then test it.",
             "Trace every food chain. How many are there? Which organism is in the most chains?",
             "Energy: how much of the grass's energy reaches the snake? Why are food chains short?",
             "Switch off the decomposers. Predict what happens to the soil and the plants, then watch.",
             "Predator–prey: which population peaks first? Explain why.",
             "Habitats: pick an organism, name one structural and one behavioural adaptation, then add warming. Which organism is affected first?",
         ]),
]

chapter_page("Ch 12 · Interactions within Ecosystems", "12 (* data loggers, decomposers, sustainable living = G3)", APPLETS, QUESTIONS, key="lseco", syllabus="2021 LSS")
