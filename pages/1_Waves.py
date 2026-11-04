import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from core.page import chapter_page
from quizzes.waves import QUESTIONS

APPLETS = [
    dict(name="Wave Graph Mapper", file="wave-graphs", height=760,
         blurb="A wave on a rope with its two graphs. The **displacement–distance** graph is a photo of the whole rope now; the **displacement–time** graph is the diary of the one particle you choose. Click any particle to follow it.",
         tasks=[
             "**Frozen time axis:** choose 'trace moves →'. The pen only moves up and down. Why does the trace look like the wave on the rope?",
             "**Look behind:** for a wave moving right, which neighbour tells you where a particle goes next? Use 'Step a little' to check, then reverse the wave.",
             "**Predict:** if you click a different particle, which graph will change, the left one or the right one? Test it.",
             "Pause the wave. Use the scrub slider to move time forward by exactly one period. What happens to the whole rope? What happens to your particle?",
             "Double the frequency without touching the wavelength. What happens to T? to the wave speed? Find the rule.",
             "Switch to **Longitudinal**. The spring no longer looks like the graph. What does the graph plot for a longitudinal wave?",
         ]),
    dict(name="Sound Lab", file="sound-lab", height=760,
         blurb="A loudspeaker pushing the air. Watch compressions and rarefactions travel while each particle only vibrates on the spot. Echo mode times a clap reflecting off a wall.",
         tasks=[
             "**Predict:** which slider will make the particles swing further from their rest positions: Loudness or Pitch? Test it, then play the tone.",
             "Set the simulation speed to 0.3× and follow one particle with your finger. Does it travel to the right side of the box?",
             "Tick **Remove the air**. The cone still moves. Explain to your partner why no sound would be heard.",
             "Echo mode: set the wall to 170 m and clap. Before the stopwatch stops, predict the time. Then try 340 m: does the time double?",
         ]),
    dict(name="Ripple Tank", file="ripple-tank", height=760,
         blurb="A ripple tank seen from above. Bright lines are wavefronts. The cork shows that the water bobs but is not carried along.",
         tasks=[
             "**Predict:** if you raise the frequency, will the wavefronts get closer together or further apart? Test it and read the λ readout.",
             "Does the wave speed change when you change the frequency? Why do you think the speed stays fixed in a ripple tank?",
             "Switch between the point dipper and the bar. Describe the shape of the wavefronts in each case.",
             "Watch the cork in the side view for 10 seconds. Where does it end up?",
         ]),
]

chapter_page("Ch 9 · General Wave Properties", "9a–9i", APPLETS, QUESTIONS, key="waves")
