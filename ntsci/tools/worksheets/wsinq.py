"""Build the Ch 9 one-page applet inquiry worksheets (student page + answer page) on the QTSS worksheet template.

Spec blocks:
  ('title', text)
  ('intro', qr_png, pic_png, [text lines])          QR | how to open | screenshot
  ('part', text)                                    bold part heading
  ('q', label, stem, [items], opts)                 one numbered question (borderless 2-col table)
items:
  ('ticks', [opt, ...], [answer indexes])           ☐ options on one line
  ('lines', n, answer_text_or_list)                 dotted writing lines; answers in blue on the key
  ('calc', n, 'quantity = ……… unit', answer_list)    working lines + right-aligned result line
  ('frame', [str | ('blank', answer)])              sentence with gaps
  ('vars', [(label, answer), ...])                  2-col plan table
  ('table', header, rows, answers)                  rows: list of cells (None = student fills); answers: same shape
  ('text', str)
opts: {'marks': n, 'star': bool, 'g3': bool}
"""
import copy
import os
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

TEMPLATE = r"C:\Users\pirat\.claude\skills\qtss-WS-quiz-template-skill\templates\ws_base.docx"
BLUE = RGBColor(0x00, 0x70, 0xC0)
TEXT_W = 15.92  # cm
FS = 11.5


def _font(run, size=FS, bold=None, color=None, italic=None):
    run.font.name = 'Arial'
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.insert(0, rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        rf.set(qn(a), 'Arial')
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color is not None:
        run.font.color.rgb = color


def _pfmt(p, after=2, before=0, line=None, align=None, exact=None):
    pf = p.paragraph_format
    pf.space_after = Pt(after); pf.space_before = Pt(before)
    if exact:
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(exact)
    else:
        pf.line_spacing = line or 1.0
    if align is not None:
        p.alignment = align


import re as _re


def _nb(t):
    """Keep numbers and their units together: 40 000 J, 0.000 001 m2."""
    t = _re.sub(r'(\d) (?=\d{3}\b)', r'\1 ', t)
    return _re.sub(r'(\d) (?=(m²|m/s|m|N|J|kJ|kg|Pa|MPa|s|mm²|cm²)(\W|$))', r'\1 ', t)


def _runs(p, parts, size=FS, color=None):
    """parts: str or list of str / ('b', text) / ('blue', text) / ('i', text)."""
    if isinstance(parts, str):
        parts = [parts]
    for x in parts:
        if isinstance(x, str):
            _font(p.add_run(_nb(x)), size, color=color)
        else:
            kind, t = x
            r = p.add_run(_nb(t))
            _font(r, size, bold=kind in ('b', 'bblue'), italic=kind == 'i' or None,
                  color=BLUE if kind in ('blue', 'bblue') else color)


def _borders(tbl, on=True, color='808080', size=4):
    tblPr = tbl._element.tblPr
    b = tblPr.find(qn('w:tblBorders'))
    if b is not None:
        tblPr.remove(b)
    b = OxmlElement('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{side}')
        e.set(qn('w:val'), 'single' if on else 'nil')
        if on:
            e.set(qn('w:sz'), str(size)); e.set(qn('w:color'), color); e.set(qn('w:space'), '0')
        b.append(e)
    tblPr.append(b)


def _widths(tbl, cms):
    tbl.autofit = False
    tblPr = tbl._element.tblPr
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    grid = tbl._element.tblGrid
    for gc, w in zip(grid.findall(qn('w:gridCol')), cms):
        gc.set(qn('w:w'), str(int(w / 2.54 * 1440)))
    for row in tbl.rows:
        for c, w in zip(row.cells, cms):
            c.width = Cm(w)


def _cell_margins(tbl, left=0.08, right=0.08, top=0.02, bottom=0.02):
    tblPr = tbl._element.tblPr
    m = OxmlElement('w:tblCellMar')
    for side, v in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement(f'w:{side}'); e.set(qn('w:w'), str(int(v / 2.54 * 1440))); e.set(qn('w:type'), 'dxa'); m.append(e)
    tblPr.append(m)


def _shade(cell, fill):
    tcPr = cell._element.get_or_add_tcPr()
    s = OxmlElement('w:shd'); s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), fill); tcPr.append(s)


def _valign(cell, v='center'):
    tcPr = cell._element.get_or_add_tcPr()
    e = OxmlElement('w:vAlign'); e.set(qn('w:val'), v); tcPr.append(e)


def _first_par(cell):
    return cell.paragraphs[0]


def _dotted(container, width_cm, answer=None, key=False, exact=23):
    p = container.add_paragraph()
    _pfmt(p, after=0, exact=exact)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(width_cm - 0.05), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    if key and answer:
        _runs(p, [('blue', answer)])
    else:
        _font(p.add_run('\t'), FS)
    return p


class WS:
    def __init__(self, footer_label, key=False):
        self.d = Document(TEMPLATE)
        self.key = key
        body = self.d.element.body
        for el in list(body):
            if el.tag != qn('w:sectPr'):
                body.remove(el)
        self._relabel(footer_label)
        self._klass()

    def _relabel(self, label):
        s = self.d.sections[0]
        old = 'Chapter 10: Assignment 1'
        extra = len(label) - len(old)
        for hf in (s.first_page_header, s.first_page_footer, s.footer, s.header):
            for p in hf.paragraphs:
                runs = list(p.runs)
                full = ''.join(r.text for r in runs)
                i = full.find(old)
                if i < 0:
                    continue
                pos, done, hit = 0, False, None
                for k, r in enumerate(runs):
                    a, b = pos, pos + len(r.text)
                    pos = b
                    if b <= i:
                        continue
                    if not done:
                        r.text = r.text[:max(0, i - a)] + label
                        done, hit = True, k
                    else:
                        r.text = ''
                # shorten the space padding before the label so it stays on one line
                for k in range(hit - 1, -1, -1):
                    t = runs[k].text
                    if t.strip() == '' and len(t) > extra + 2:
                        runs[k].text = t[:len(t) - extra - 2]
                        break
                else:
                    t = runs[hit].text
                    lead = len(t) - len(t.lstrip(' '))
                    if lead > extra + 2:
                        runs[hit].text = t[extra + 2:]

    def _klass(self):
        old, new = 'Sec 2 TG___ (G2/G3)', 'Sec 3 ______ (G1)  '
        for p in self.d.sections[0].first_page_header.paragraphs:
            runs = list(p.runs); full = ''.join(r.text for r in runs); i = full.find(old)
            if i < 0:
                continue
            pos, done = 0, False
            for r in runs:
                a, b = pos, pos + len(r.text); pos = b
                if b <= i or a >= i + len(old):
                    continue
                keep_l, keep_r = r.text[:max(0, i - a)], r.text[max(0, i + len(old) - a):]
                r.text = keep_l + ('' if done else new) + keep_r
                done = True

    # ---------------------------------------------------------------- blocks
    def title(self, text):
        p = self.d.add_paragraph()
        _pfmt(p, after=4)
        _runs(p, [('b', text)], size=13)

    def part(self, text):
        p = self.d.add_paragraph()
        _pfmt(p, after=1, before=3)
        _runs(p, [('b', text)], size=FS + 0.5)

    def intro(self, qr, pic, lines, pic_cm=5.0):
        t = self.d.add_table(rows=1, cols=3)
        _borders(t, True, 'A0A0A0', 6)
        qr_cm = 2.05
        _widths(t, [qr_cm + 0.3, TEXT_W - qr_cm - 0.3 - pic_cm - 0.3, pic_cm + 0.3])
        _cell_margins(t, 0.12, 0.12, 0.08, 0.08)
        c0, c1, c2 = t.rows[0].cells
        for c in (c0, c1, c2):
            _valign(c)
        _shade(c1, 'F2F7EC')
        p = _first_par(c0); _pfmt(p, after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        p.add_run().add_picture(qr, width=Cm(qr_cm))
        p = c0.add_paragraph(); _pfmt(p, after=0, align=WD_ALIGN_PARAGRAPH.CENTER); _runs(p, 'scan me', size=8)
        p = _first_par(c1); _pfmt(p, after=2)
        for k, ln in enumerate(lines):
            if k:
                p = c1.add_paragraph(); _pfmt(p, after=2)
            _runs(p, ln, size=FS - 0.5)
        p = _first_par(c2); _pfmt(p, after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        p.add_run().add_picture(pic, width=Cm(pic_cm))
        self._gap(3)

    def _gap(self, pt):
        p = self.d.add_paragraph(); _pfmt(p, after=0, exact=pt)

    def q(self, label, stem, items, opts=None):
        opts = opts or {}
        t = self.d.add_table(rows=1, cols=2)
        _borders(t, False)
        numw = 0.85
        _widths(t, [numw, TEXT_W - numw])
        _cell_margins(t, 0.02, 0.05, 0.0, 0.0)
        c0, c1 = t.rows[0].cells
        p = _first_par(c0); _pfmt(p, after=0)
        _runs(p, [('b', str(label))])
        p = _first_par(c1); _pfmt(p, after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
        pre = []
        if opts.get('g3'):
            pre.append(('b', '(G3) '))
        if opts.get('star'):
            pre.append('★ ')
        stem = stem if isinstance(stem, list) else [stem]
        stem = [(('bblue', x[1]) if self.key else '…' * (6 if x[0] == 'blank' else 11)) if (isinstance(x, tuple) and x[0] in ('blank', 'lblank')) else x for x in stem]
        tail = [f"  [{opts['marks']}]"] if opts.get('marks') else []
        _runs(p, pre + stem + tail)
        W = TEXT_W - numw - 0.1
        for it in items:
            kind = it[0]
            if kind == 'text':
                p = c1.add_paragraph(); _pfmt(p, after=2); _runs(p, it[1])
            elif kind == 'ticks':
                p = c1.add_paragraph(); _pfmt(p, after=2, before=1)
                for k, o in enumerate(it[1]):
                    mark = '☑' if (self.key and k in it[2]) else '☐'
                    _runs(p, [('bblue', mark) if (self.key and k in it[2]) else mark, ' ' + o + '        '])
            elif kind == 'ticklist':
                for k, o in enumerate(it[1]):
                    p = c1.add_paragraph(); _pfmt(p, after=1)
                    hit = self.key and k in it[2]
                    _runs(p, [('bblue', '☑   ' + o)] if hit else ['☐   ' + o])
            elif kind == 'lines':
                n, ans = it[1], it[2]
                ans = ans if isinstance(ans, list) else [ans]
                if self.key:
                    for a in ans:
                        p = c1.add_paragraph(); _pfmt(p, after=1); _runs(p, [('blue', a)])
                else:
                    for _ in range(n):
                        _dotted(c1, W)
            elif kind == 'calc':
                n, result, ans = it[1], it[2], it[3]
                if self.key:
                    for a in ans:
                        p = c1.add_paragraph(); _pfmt(p, after=1); _runs(p, [('blue', a)])
                else:
                    for _ in range(n):
                        p = c1.add_paragraph(); _pfmt(p, after=0, exact=18)
                    p = c1.add_paragraph(); _pfmt(p, after=2, align=WD_ALIGN_PARAGRAPH.RIGHT); _runs(p, result)
            elif kind == 'frame':
                p = c1.add_paragraph(); _pfmt(p, after=2, line=1.5)
                for seg in it[1]:
                    if isinstance(seg, str):
                        _runs(p, seg)
                    elif seg[0] == 'pick':
                        _runs(p, [('b', '( ')])
                        for k, o in enumerate(seg[1]):
                            if k:
                                _runs(p, [('b', '  /  ')])
                            _runs(p, [('bblue', o)] if (self.key and k == seg[2]) else [('b', o)])
                        _runs(p, [('b', ' )')])
                    else:
                        _runs(p, [('bblue', seg[1])] if self.key else '…' * 16)
            elif kind == 'vars':
                tt = c1.add_table(rows=len(it[1]), cols=2)
                _borders(tt, True)
                _widths(tt, [6.3, W - 6.3])
                _cell_margins(tt, 0.1, 0.1, 0.03, 0.03)
                for r, (lab, ans) in zip(tt.rows, it[1]):
                    _shade(r.cells[0], 'F2F2F2')
                    p = _first_par(r.cells[0]); _pfmt(p, after=0); _runs(p, lab, size=FS - 0.5)
                    p = _first_par(r.cells[1]); _pfmt(p, after=0, exact=17)
                    if self.key:
                        _runs(p, [('blue', ans)], size=FS - 0.5)
                p = c1.paragraphs[-1]; _pfmt(p, after=0, exact=4)
            elif kind == 'table':
                head, rows, answers = it[1], it[2], it[3]
                cw = it[4] if len(it) > 4 else [W / len(head)] * len(head)
                tt = c1.add_table(rows=1 + len(rows), cols=len(head))
                _borders(tt, True)
                _widths(tt, cw)
                _cell_margins(tt, 0.06, 0.06, 0.02, 0.02)
                tt.alignment = WD_TABLE_ALIGNMENT.CENTER
                for c, h in zip(tt.rows[0].cells, head):
                    _shade(c, 'F2F2F2'); _valign(c)
                    p = _first_par(c); _pfmt(p, after=0, align=WD_ALIGN_PARAGRAPH.CENTER); _runs(p, [('b', h)], size=FS - 1)
                for r, vals, avals in zip(tt.rows[1:], rows, answers):
                    for c, v, a in zip(r.cells, vals, avals):
                        p = _first_par(c); _pfmt(p, after=0, exact=16, align=WD_ALIGN_PARAGRAPH.CENTER)
                        if v is not None:
                            _runs(p, str(v), size=FS - 0.5)
                        elif self.key:
                            _runs(p, [('bblue', str(a))], size=FS - 0.5)
                p = c1.paragraphs[-1]; _pfmt(p, after=0, exact=4)
        self._gap(1)

    def save(self, path):
        self.d.save(path)


def build(spec, footer_label, out_student_key):
    """One file: the student page, a page break, '-----Answers-----', then the same page with answers."""
    ws = WS(footer_label, key=False)
    _emit(ws, spec)
    # page break + answers built by a second pass into the same document
    p = ws.d.add_paragraph(); _pfmt(p, after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    p.paragraph_format.page_break_before = True
    _runs(p, [('b', '-------------------------------------------------Answers-------------------------------------------------')], size=FS)
    ws.key = True
    _emit(ws, spec, answers=True)
    ws.save(out_student_key)


def _emit(ws, spec, answers=False):
    for blk in spec:
        k = blk[0]
        if k == 'title':
            ws.title(blk[1] + (' (answers)' if answers else ''))
        elif k == 'intro':
            if not answers:
                ws.intro(*blk[1:])
        elif k == 'part':
            ws.part(blk[1])
        elif k == 'q':
            ws.q(*blk[1:])
