import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.lss_transport_humans import QUESTIONS

APPLETS = [
    dict(name="Human Transport Lab", file="circulation", height=860,
         blurb="Three modes. **Circulation**: the heart pumps blood to the lungs and round the body; watch it pick up and drop off oxygen, carbon dioxide and digested food. **Diffusion close-up**: what crosses the capillary wall in the lungs, a muscle and the small intestine. **Why a transport system? (G3)**: surface area, volume and diffusion distance.",
         tasks=[
             "**Predict:** where does the blood turn from blue to red? Where does it turn back? Check by following one blood cell.",
             "Tick 'Exercising'. What happens to the heart rate, and why do the muscles need it?",
             "Read the pulse after 15 s and multiply by 4. Does it match the heart rate slider?",
             "Show the cross-sections. Why does an artery need a thick, muscular wall but a capillary only one cell?",
             "Diffusion close-up: in the muscle, which way does oxygen move? Carbon dioxide? Tick 'use supplies faster': what changes?",
             "Why a transport system: what happens to SA ÷ volume as the cube grows?",
         ]),
]

chapter_page("Ch 15 · Transport in Humans", "15.1, 15.2, 15.6* (* = G3)", APPLETS, QUESTIONS, key="lshum", syllabus="2021 LSS")
