"""Printable version of each topic's app quiz (student pages, then '-----Answers-----' pages).

Questions are read straight from ntsci/t*_*.py, so the paper quiz matches the app.
Usage: python quizsheet.py [topic numbers]   ->  out/3NT Topic N Quiz - <title> w answers (2027).docx
"""
import ast
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
NTSCI = HERE.parents[1]
sys.path.insert(0, str(HERE))
import wsinq  # noqa: E402
from wsinq import WD_ALIGN_PARAGRAPH, _pfmt, _runs  # noqa: E402

LETTERS = "ABCDEFGH"


def load(path):
    """APPLETS, QUESTIONS and the topic_page(...) arguments from a topic page, without running Streamlit."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    ns = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and node.targets[0].id in ("APPLETS", "QUESTIONS"):
            exec(compile(ast.Module([node], []), str(path), "exec"), ns)
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and getattr(node.value.func, "id", "") == "topic_page":
            ns["num"], ns["title"] = ast.literal_eval(node.value.args[0]), ast.literal_eval(node.value.args[1])
    return ns


def blocks(q):
    """One quiz question -> (stem, items) for wsinq.WS.q."""
    t = q["type"]
    stem = [q["q"]]
    if t == "mcq":
        return stem + ["  Tick one."], [("ticklist", q["options"], [q["answer"]])], None
    if t == "multi":
        return stem + ["  Tick ", ("b", "all"), " the correct ones."], [("ticklist", q["options"], q["answer"])], None
    if t == "num":
        unit = q.get("unit", "")
        return stem, [("calc", 2, f"answer = ……………………… {unit}", [q["why"]])], None
    if t == "match":
        rights = sorted({r for _, r in q["pairs"]})
        bank = "Choose from:  " + "   ·   ".join(rights)
        rows = [[a, None] for a, _ in q["pairs"]]
        ans = [[a, b] for a, b in q["pairs"]]
        return stem + ["  Write the matching words in the table."], [("text", [("i", bank)]), ("table", ["", "matches"], rows, ans, [5.0, 9.6])], None
    raise ValueError(t)


def build(path, out_dir):
    ns = load(path)
    num, title = ns["num"], ns["title"]
    label = f"Topic {num}: Quiz"
    spec = [("title", f"Topic {num} Quiz: {title}")]
    for i, q in enumerate(ns["QUESTIONS"], 1):
        stem, items, _ = blocks(q)
        spec.append(("q", i, stem, items))
    name = f"3NT Topic {num} Quiz - {title} w answers (2027).docx"
    ws = wsinq.WS(label, key=False)
    ws.title(spec[0][1])
    p = ws.d.add_paragraph(); _pfmt(p, after=4)
    _runs(p, ["Answer every question. You can check yourself afterwards with the ", ("b", "Quiz"), " tab in the app (qtss-g1-science.streamlit.app)."])
    wsinq._emit(ws, spec[1:])
    p = ws.d.add_paragraph(); _pfmt(p, after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    p.paragraph_format.page_break_before = True
    _runs(p, [("b", "-------------------------------------------------Answers-------------------------------------------------")])
    ws.key = True
    wsinq._emit(ws, spec, answers=True)
    # never split a question across two pages
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    for t in ws.d.tables:
        for r in t.rows:
            e = OxmlElement("w:cantSplit"); e.set(qn("w:val"), "true"); r._tr.get_or_add_trPr().append(e)
    ws.save(str(out_dir / name))
    return name, len(ns["QUESTIONS"])


if __name__ == "__main__":
    out = HERE / "out"; out.mkdir(exist_ok=True)
    want = set(sys.argv[1:])
    for f in sorted(NTSCI.glob("t*_*.py"), key=lambda f: int(f.name[1:].split("_")[0])):
        n = f.name[1:].split("_")[0]
        if want and n not in want:
            continue
        print("built", *build(f, out))
