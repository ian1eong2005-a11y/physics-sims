"""Teacher's guide: every applet in the G1 / N(T) app, by topic, with what to try and QR codes (Explore and Investigate).

Usage: python guide.py  ->  out/3NT Applets - Teacher guide with QR codes (2027).docx
"""
import pathlib
import sys

import qrcode
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from quizsheet import NTSCI, load  # noqa: E402

SITE = "https://qtss-g1-science.streamlit.app"
PAGE = {1: "energy", 2: "electricity", 3: "wave", 4: "force", 5: "food", 6: "food-chemistry", 7: "food-safety",
        8: "staying-healthy", 9: "digestion", 10: "breathing", 11: "blood"}
SECTION = {1: "Machines Around Us", 5: "Food Matters", 8: "Our Body and Health"}
QR = HERE / "img" / "qr"
QR.mkdir(parents=True, exist_ok=True)


def qr(url, name):
    path = QR / f"{name}.png"
    q = qrcode.QRCode(border=1, box_size=8, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data(url); q.make(fit=True); q.make_image().save(path)
    return path


def font(run, size=10, bold=False, color=None):
    run.font.name = "Arial"; run.font.size = Pt(size); run.bold = bold
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    if color:
        run.font.color.rgb = RGBColor.from_string(color)


def shade(cell, fill):
    tc = cell._tc.get_or_add_tcPr(); s = OxmlElement("w:shd")
    s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), fill); tc.append(s)


def para(container, text="", size=10, bold=False, color=None, align=None, after=2):
    p = container.add_paragraph() if hasattr(container, "add_paragraph") else container
    p.paragraph_format.space_after = Pt(after); p.paragraph_format.space_before = Pt(0)
    if align:
        p.alignment = align
    if text:
        font(p.add_run(text), size, bold, color)
    return p


def strip_md(t):
    return t.replace("**", "")


def main():
    d = Document()
    sec = d.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
    for side in ("left_margin", "right_margin"):
        setattr(sec, side, Cm(1.6))
    sec.top_margin = sec.bottom_margin = Cm(1.3)
    fp = sec.footer.paragraphs[0]; font(fp.add_run("Queenstown Secondary School · Department of Science · 3NT G1 Science applets (2027)"), 8, color="6B7785")

    para(d, "3NT G1 Science Applets: Teacher's Guide", 18, True, after=4)
    para(d, f"App: {SITE}   (no login; works on laptops and the projector)", 11, after=2)
    para(d, "Every topic page has three tabs: Explore (play with the applet), Investigate (guess → fair test → record → what I found) and Quiz. "
            "Scan an Explore code to open that applet; scan an Investigate code to open it straight in its investigation. "
            "Printed inquiry worksheets (one page + answers) and a printable quiz for each topic are in the same folder as this guide.", 10, after=8)

    files = sorted(NTSCI.glob("t*_*.py"), key=lambda f: int(f.name[1:].split("_")[0]))
    for f in files:
        ns = load(f)
        n, title = ns["num"], ns["title"]
        if n in SECTION:
            para(d, SECTION[n], 13, True, "1F6FEB", after=2).paragraph_format.keep_with_next = True
        para(d, f"Topic {n}: {title}   ·   {len(ns['QUESTIONS'])} quiz questions   ·   {SITE}/{PAGE[n]}", 12, True, after=3).paragraph_format.keep_with_next = True
        t = d.add_table(rows=1, cols=4)
        t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
        widths = [Cm(5.2), Cm(14.6), Cm(3.0), Cm(3.0)]
        for c, w, h in zip(t.rows[0].cells, widths, ["Applet", "What students do", "Explore", "Investigate"]):
            c.width = w; shade(c, "EEF3F7"); para(c.paragraphs[0], h, 10, True, after=0).paragraph_format.keep_with_next = True
        hdr = t.rows[0]._tr.get_or_add_trPr(); e = OxmlElement("w:tblHeader"); e.set(qn("w:val"), "true"); hdr.append(e)
        for k, a in enumerate(ns["APPLETS"]):
            tr = t.add_row(); cs = OxmlElement("w:cantSplit"); cs.set(qn("w:val"), "true"); tr._tr.get_or_add_trPr().append(cs)
            row = tr.cells
            if k == 0:
                for c in row:
                    c.paragraphs[0].paragraph_format.keep_with_next = True
            for c, w in zip(row, widths):
                c.width = w
            para(row[0].paragraphs[0], a["name"], 11, True, after=0)
            if a.get("inq"):
                para(row[0], "has an investigation", 8, color="2E9E5B", after=0)
            for i, line in enumerate(a.get("try", [])):
                p = row[1].paragraphs[0] if i == 0 else row[1].add_paragraph()
                para(p, f"{i + 1}. {strip_md(line)}", 9.5, after=1)
            url = f"{SITE}/{PAGE[n]}?applet={a['file']}"
            p = row[2].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(str(qr(url, f"{a['file']}_x")), width=Cm(2.3))
            if a.get("inq"):
                p = row[3].paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.add_run().add_picture(str(qr(url + "&mode=investigate", f"{a['file']}_i")), width=Cm(2.3))
            else:
                para(row[3].paragraphs[0], "–", 10, align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
        para(d, "", after=6)

    out = HERE / "out"; out.mkdir(exist_ok=True)
    path = out / "3NT Applets - Teacher guide with QR codes (2027).docx"
    d.save(path)
    print("built", path.name)


if __name__ == "__main__":
    main()
