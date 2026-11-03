import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.lss_digestion import QUESTIONS

APPLETS = [
    dict(name="Digestion Lab", file="digestion", height=860,
         blurb="Three modes. **Journey of food**: follow a meal from the mouth to the anus and watch large food molecules being broken down and absorbed. **Enzyme test tube**: change the temperature and pH and test samples with iodine each minute. **Blood glucose**: compare a healthy person with a person with diabetes after a meal.",
         tasks=[
             "**Predict:** where does the digestion of starch start? Of protein? Of fat? Choose each food and watch the bars.",
             "Untick the names and click each part. Can you name it before the card tells you?",
             "Where are the digested food molecules absorbed into the blood? What does the large intestine absorb?",
             "Enzyme test tube: find the temperature where the iodine turns brown fastest. Then try 70 °C and cool it back down. What happened?",
             "Protease: what pH works best? Why does that make sense for the stomach?",
             "Blood glucose: compare the sugary drink with the wholemeal meal for both people.",
         ]),
]

chapter_page("Ch 14 · Human Digestive System", "14.1–14.6 (* = G3)", APPLETS, QUESTIONS, key="lsdig", syllabus="2021 LSS")
