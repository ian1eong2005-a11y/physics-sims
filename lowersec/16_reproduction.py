import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.lss_reproduction import QUESTIONS

APPLETS = [
    dict(name="Reproduction Lab", file="reproduction", height=860,
         blurb="Four modes. **Parts and functions**: click each organ of the female or male system; hide the names to test yourself. **Menstrual cycle**: step through the 28 days and watch the uterus lining and the egg. **Fertilisation and birth control**: choose the day and the birth control methods, run the month, and see whether pregnancy happens and why. **Heredity and variation (G3)**: each child gets a unique mix of genetic information from both parents.",
         tasks=[
             "**Predict:** where does fertilisation happen? Follow the egg and the sperm to check.",
             "Hide the names and click each organ. Say its job before you read the card.",
             "Menstrual cycle: on which days is the lining thickest? When does ovulation happen?",
             "Tick 'The egg is fertilised'. What changes in the lining and in the next period?",
             "Fertilisation: try day 5, day 13 and day 20. Explain why only one leads to pregnancy.",
             "Birth control: for each method, say which step it blocks before you test it.",
             "Heredity (G3): make four children. Why are siblings not identical?",
         ]),
]

chapter_page("Ch 16 · Human Sexual Reproductive System", "16.1–16.6", APPLETS, QUESTIONS, key="lsrep", syllabus="2021 LSS")
