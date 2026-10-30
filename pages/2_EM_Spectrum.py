import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.em_spectrum import QUESTIONS

APPLETS = [
    dict(name="EM Spectrum Explorer", file="em-spectrum", height=820,
         blurb="Slide along the spectrum or click a band. The card shows the wavelength range, the uses the syllabus lists, and the hazard. The race shows every region travelling at the same speed in a vacuum.",
         tasks=[
             "**Predict:** which end of the spectrum is more dangerous? Slide across and read the hazard lines to test your idea.",
             "Watch the speed race for a while. Does any wave get ahead? What is the only difference between the three waves?",
             "Tick **Hide names**. Press *Random region* and work out which region it is from the uses alone. Then untick to check.",
             "Find the two regions whose hazard is heating, and the three that are ionising. What do the ionising ones have in common?",
         ]),
]

chapter_page("Ch 10 · Electromagnetic Spectrum", "10a–10d", APPLETS, QUESTIONS, key="em")
