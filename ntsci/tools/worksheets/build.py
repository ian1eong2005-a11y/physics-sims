"""One-page applet inquiry worksheets for 3NT (G1 Science K123), Topics 1-5.

Content (question, guesses, table, answers, sentence) comes from wsdata.json, exported from the applets themselves,
so each sheet matches its applet exactly.  Usage: python build.py [code ...]
"""
import json
import pathlib
import sys

import qrcode

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import wsinq  # noqa: E402  (the QTSS one-page inquiry builder, patched for N(T): bigger type, tick lists, circle-the-word)

SITE = "qtss-g1-science.streamlit.app"
DATA = json.load(open(HERE / "wsdata.json", encoding="utf-8"))
TOPIC = {1: ("energy", "Energy"), 2: ("electricity", "Electricity"), 3: ("wave", "Wave"), 4: ("force", "Effects of Force"), 5: ("food", "Sources of Food"),
         6: ("food-chemistry", "Food Chemistry"), 7: ("food-safety", "Food Safety"), 8: ("staying-healthy", "Staying Healthy"), 9: ("digestion", "Digestion"),
         10: ("breathing", "Breathing"), 11: ("blood", "Blood Circulation")}
# code, applet, investigations on the sheet, short title, name of the applet button in the app
SHEETS = [
    ("1.1", "energy-swing", [0], "Swinging bottle", "Swinging bottle"),
    ("1.2", "energy-heater", [0], "Which heater is faster?", "Heater power"),
    ("1.3", "energy-hotcold", [0], "Hot meets cold", "Hot meets cold"),
    ("1.4", "energy-grid", [0], "Why use a high voltage?", "Power station"),
    ("2.1", "elec-meters", [0, 1], "Current in series and parallel", "Current and voltage"),
    ("2.2", "elec-meters", [2, 3], "Voltage in series and parallel", "Current and voltage"),
    ("2.3", "elec-home", [0, 1], "Adding more lamps", "Lamps: series or parallel"),
    ("2.4", "elec-home", [2], "One lamp blows", "Lamps: series or parallel"),
    ("2.5", "elec-resistors", [0, 1], "Adding resistors", "Adding resistors"),
    ("2.6", "elec-cost", [0], "What does it cost to run?", "Cost of electricity"),
    ("3.1", "wave-rope", [0, 1], "Waves on a rope", "Rope waves"),
    ("4.1", "force-car", [0], "Toy car race", "Toy car race"),
    ("4.2", "force-accel", [0], "Speeding up", "Speeding up"),
    ("4.3", "force-turn", [0], "Turning effect", "Turning effect"),
    ("5.1", "food-needs", [0], "What does a plant need?", "What plants need"),
    ("5.2", "food-fertiliser", [0], "Does fertiliser help?", "Fertiliser"),
    ("5.3", "food-banana", [0], "Ripening bananas", "Ripening bananas"),
    ("5.4", "food-farm", [0], "More food from the farm", "Farm and pond"),
    ("6.1", "chem-chroma", [0], "One dye or a mixture?", "Chromatography"),
    ("6.2", "chem-ph", [0], "Acid, neutral or alkali?", "pH"),
    ("6.3", "chem-neutral", [0], "Neutralisation", "Neutralisation"),
    ("6.4", "chem-acid", [0], "What do acids react with?", "Acid reactions"),
    ("6.5", "chem-rust", [0], "What makes iron rust?", "Rusting"),
    ("7.1", "safe-bread", [0], "Protect my bread", "Protect my bread"),
    ("7.2", "safe-milk", [0], "Can heat keep milk fresh?", "Heat and milk"),
    ("8.1", "health-germs", [0], "Germ killers", "Germ killers"),
    ("8.2", "health-antibiotic", [0], "Finish the antibiotic course", "Antibiotic course"),
    ("9.1", "dig-enzyme", [0], "Enzymes and pH", "Enzymes at work"),
    ("9.2", "dig-enzyme", [1], "Enzymes and temperature", "Enzymes at work"),
    ("10.1", "breath-air", [0], "Inhaled and exhaled air", "Inhaled and exhaled air"),
    ("11.1", "blood-pulse", [0], "Exercise and pulse rate", "Exercise and pulse"),
    ("11.2", "blood-plaque", [0], "Plaque and heart disease", "Plaque"),
]
W = 15.07


def qr(url, path):
    q = qrcode.QRCode(border=1, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data(url); q.make(fit=True)
    q.make_image().save(path)


def _h(t):
    h = 7
    for ch in t:
        h = (h * 31 + ord(ch)) % 9973
    return h


def shuffled(options, ans):
    """A fixed mixed order, so the right answer is not always printed first."""
    order = sorted(range(len(options)), key=lambda i: _h(options[i] + str(i)))
    return [options[i] for i in order], order.index(ans)


def found(inq):
    """The 'what I found' sentence with circle-the-word choices."""
    out, k = [], 0
    for part in inq["found"]:
        if isinstance(part, str):
            out.append(part)
        else:
            opts, a = shuffled(part, inq["foundAns"][k]); out.append(("pick", opts, a)); k += 1
    return out


def table(inq):
    head = [inq["changeLabel"]] + inq["heads"]
    rows = [[r[0]] + [None] * (len(r) - 1) for r in inq["rows"]]
    n = len(head)
    longest = max(len(str(r[0])) for r in inq["rows"])
    first = min(6.6, max(3.2, 0.22 * longest + 1.0, 0.2 * len(head[0]) + 0.9))
    if n == 2:
        cw = [first, min(6.5, W - first)]
    else:
        lens = [max(max(len(str(r[j])) for r in inq["rows"]), 0.75 * len(head[j])) + 4 for j in range(1, n)]
        rest = W - first
        cw = [first] + [rest * v / sum(lens) for v in lens]
    return ("table", head, rows, inq["rows"], cw)


def guess(q):
    """Short options go on one line; long ones get a line each."""
    kind = "ticks" if sum(len(o) for o in q["guess"]) <= 52 else "ticklist"
    opts, a = shuffled(q["guess"], q["guessAns"])
    return (kind, opts, [a])


def test_stem(inq, short=False):
    if short:
        return [("b", "Test. "), "Record each reading in the applet. Copy the readings here."]
    go = f"press {inq['go']}, then " if inq["go"] else ""
    return [("b", "Test. "), f"Choose each one in the applet, {go}press Record. Copy the readings into the table."]


def spec_for(code, sim, ks, short, button):
    d = DATA[sim]
    topic = int(code.split(".")[0])
    page = TOPIC[topic][0]
    url = f"https://{SITE}/{page}?applet={sim}&mode=investigate" + (f"&inq={ks[0]}" if ks[0] else "")
    qr_path = HERE / "img" / f"qr_{code}.png"
    qr(url, qr_path)
    inqs = [d["inq"][k] for k in ks]
    lines = [
        [("b", "Open the applet: "), "scan the QR code, or go to ", ("b", SITE), f" → Topic {topic} → Investigate → ", ("b", button), "."],
        ["Do the 4 steps on the screen. Write your answers on this sheet."],
    ]
    spec = [("title", f"Applet Inquiry {code}: {short}"), ("intro", str(qr_path), str(HERE / "img" / f"ws_{sim}_{ks[0]}.jpg"), lines, 5.6 if len(ks) == 1 else 4.2)]
    if len(inqs) == 1:
        q = inqs[0]
        spec += [
            ("q", 1, [("b", "My guess. "), q["q"], " Tick one."], [guess(q)]),
            ("q", 2, [("b", "Fair test. "), "Fill in the table."], [("vars", [("I change", q["change"]), ("I measure", q["measure"]), ("I keep the same (write two things)", "; ".join(q["same"][:2]))])]),
            ("q", 3, test_stem(q), [table(q)]),
            ("q", 4, [("b", "What I found. "), "Circle the correct words."], [("frame", found(q))]),
            ("q", 5, [("b", "The science idea. "), "Was my guess right?   ☐ Yes    ☐ No.    Copy the science idea from the last step of the applet."], [("lines", 3, q["why"])]),
        ]
    else:
        a, b = inqs
        same_plan = a["change"] == b["change"] and a["measure"] == b["measure"]
        if same_plan:
            spec.append(("q", 1, [("b", "Fair test. "), "Fill in the table. It is the same for Part A and Part B."],
                         [("vars", [("I change", a["change"]), ("I measure", a["measure"]), ("I keep the same (write two things)", "; ".join(a["same"][:2]))])]))
        n = 2 if same_plan else 1
        for letter, q in zip("AB", inqs):
            extra = "" if letter == "A" else "  (tap it at the top of the box in the applet)"
            spec.append(("part", f"Part {letter}: {q['name']}{extra}"))
            spec.append(("q", n, [("b", "My guess. "), q["q"], " Tick one."], [guess(q)])); n += 1
            if not same_plan:
                spec.append(("q", n, [("b", "Fair test. "), "I change ", ("lblank", q["change"]), ".  I measure ", ("lblank", q["measure"]), "."], [])); n += 1
            spec.append(("q", n, test_stem(q, True), [table(q)])); n += 1
            spec.append(("q", n, [("b", "What I found. "), "Circle the correct words."], [("frame", found(q))])); n += 1
    return spec


def main(codes):
    out = HERE / "out"; out.mkdir(exist_ok=True)
    for code, sim, ks, short, button in SHEETS:
        if codes and code not in codes:
            continue
        topic = int(code.split(".")[0])
        name = f"3NT Topic {topic} Applet Inquiry {code} - {short.replace('?', '')} w answers (2027).docx"
        wsinq.build(spec_for(code, sim, ks, short, button), f"Topic {topic}: Applet Inquiry {code}", str(out / name))
        print("built", name)


if __name__ == "__main__":
    main(sys.argv[1:])
