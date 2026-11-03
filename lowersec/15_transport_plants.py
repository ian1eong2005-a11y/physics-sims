import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.lss_transport_plants import QUESTIONS

APPLETS = [
    dict(name="Plant Transport Lab", file="plant-transport", height=860,
         blurb="Three modes. **Whole plant**: water travels up the xylem and leaves through the stomata; food travels in the phloem. Stand the plant in red dye and cut across the stem. **Root hair and osmosis (G3)**: change the salt in the soil water. **Leaf gases**: carbon dioxide and oxygen diffuse through the stomata in light and in the dark.",
         tasks=[
             "**Predict:** if the plant stands in red-dyed water, which tissue in the stem will turn red? Tick the dye and wait.",
             "Close the stomata. What happens to the water in the xylem? Why?",
             "Switch the light off. Which tube slows down, and why?",
             "Root hair: find the salt level where there is no net movement of water. What happens to the plant in very salty soil?",
             "Leaf gases: in bright light, which way do carbon dioxide and oxygen move? Switch to dark and compare.",
         ]),
]

chapter_page("Ch 15 · Transport in Plants", "15.2, 15.3*, 15.4* (* = G3)", APPLETS, QUESTIONS, key="lspla", syllabus="2021 LSS")
