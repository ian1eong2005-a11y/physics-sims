import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ntsci.page import topic_page  # noqa: E402

APPLETS = [
    {"name": "〰️ Rope waves", "file": "wave-rope", "inq": True, "height": 860,
     "try": ["Watch the ribbon. Does it travel along the rope, or only go up and down?", "Shake **Fast**. What happens to the wavelength?", "Make a **Big shake**. What happens to the amplitude?"]},
    {"name": "📡 Uses of waves", "file": "wave-uses", "height": 900,
     "try": ["Match all 11 uses. Can you get them all right first time?"]},
]

QUESTIONS = [
    dict(type="mcq", pic="🪢", q="How do you make a wave on a rope?",
         options=["hold it still", "shake one end (a vibration)", "cut the rope", "pull it tight and wait"], answer=1,
         why="Waves are made by vibrations."),
    dict(type="mcq", pic="🎀", q="A wave travels along a rope. What does the wave carry from one end to the other?",
         options=["the rope", "energy", "air", "water"], answer=1,
         why="Waves transfer energy. The rope itself only moves up and down."),
    dict(type="match", pic="📏", q="Match each wave word to its meaning.",
         pairs=[("Amplitude", "biggest distance from the rest position"), ("Wavelength", "length of one complete wave"), ("Frequency", "number of waves made each second")],
         why="Amplitude, wavelength and frequency are used to describe a wave."),
    dict(type="mcq", pic="🐇", q="You shake the rope faster. The frequency…",
         options=["goes up", "goes down", "stays the same"], answer=0,
         why="More waves are made each second."),
    dict(type="mcq", pic="🐇", q="You shake the same rope faster. The wavelength becomes…",
         options=["longer", "shorter", "the same"], answer=1,
         why="The waves are closer together."),
    dict(type="mcq", pic="🔢", q="What is the unit of frequency?",
         options=["metre (m)", "hertz (Hz)", "second (s)", "watt (W)"], answer=1,
         why="Frequency is measured in hertz (Hz)."),
    dict(type="mcq", pic="🎮", q="Which wave does a TV remote control use?",
         options=["infrared", "X-rays", "gamma rays", "ultraviolet"], answer=0,
         why="Remote-controlled devices use infrared."),
    dict(type="mcq", pic="🦴", q="Which wave is used to check for a broken bone?",
         options=["radio waves", "microwaves", "X-rays", "light"], answer=2,
         why="X-rays pass through flesh but not through bone."),
    dict(type="match", pic="📡", q="Match each use to the wave.",
         pairs=[("Radio and TV broadcasts", "radio waves"), ("Satellite communication", "microwaves"), ("Optical fibres", "light"), ("Sunbeds and sterilising", "ultraviolet")],
         why="Each type of wave has its own uses."),
    dict(type="mcq", pic="🏥", q="Which wave is used in medical treatment (for example, to treat cancer)?",
         options=["gamma rays", "infrared", "radio waves", "light"], answer=0,
         why="Gamma rays are used in medical treatment."),
]

topic_page(3, "Wave", "🌊", "G1 Science K123 · 1.3 Wave: making waves, amplitude, frequency and wavelength, uses of waves", APPLETS, QUESTIONS, key="nt3")
