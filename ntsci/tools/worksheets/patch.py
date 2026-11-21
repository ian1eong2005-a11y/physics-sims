"""Patch the copied wsinq.py for the 3NT sheets: bigger type, Sec 3 G1 header, tick lists, circle-the-word."""
import pathlib

p = pathlib.Path(__file__).resolve().parent / "wsinq.py"
s = p.read_text(encoding="utf-8")


def sub(a, b):
    global s
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)


sub("FS = 10.5", "FS = 11.5")
sub("def _dotted(container, width_cm, answer=None, key=False, exact=19):", "def _dotted(container, width_cm, answer=None, key=False, exact=23):")
# header: Sec 3 G1 class line
sub("        self._relabel(footer_label)\n", "        self._relabel(footer_label)\n        self._klass()\n")
sub("    # ---------------------------------------------------------------- blocks\n",
    "    def _klass(self):\n"
    "        old, new = 'Sec 2 TG___ (G2/G3)', 'Sec 3 ______ (G1)  '\n"
    "        for p in self.d.sections[0].first_page_header.paragraphs:\n"
    "            runs = list(p.runs); full = ''.join(r.text for r in runs); i = full.find(old)\n"
    "            if i < 0:\n"
    "                continue\n"
    "            pos, done = 0, False\n"
    "            for r in runs:\n"
    "                a, b = pos, pos + len(r.text); pos = b\n"
    "                if b <= i or a >= i + len(old):\n"
    "                    continue\n"
    "                keep_l, keep_r = r.text[:max(0, i - a)], r.text[max(0, i + len(old) - a):]\n"
    "                r.text = keep_l + ('' if done else new) + keep_r\n"
    "                done = True\n\n"
    "    # ---------------------------------------------------------------- blocks\n")
# tick list: one option per line
sub("            elif kind == 'lines':\n",
    "            elif kind == 'ticklist':\n"
    "                for k, o in enumerate(it[1]):\n"
    "                    p = c1.add_paragraph(); _pfmt(p, after=1)\n"
    "                    hit = self.key and k in it[2]\n"
    "                    _runs(p, [('bblue', '☑   ' + o)] if hit else ['☐   ' + o])\n"
    "            elif kind == 'lines':\n")
# circle the word
sub("                    if isinstance(seg, str):\n                        _runs(p, seg)\n",
    "                    if isinstance(seg, str):\n                        _runs(p, seg)\n"
    "                    elif seg[0] == 'pick':\n"
    "                        _runs(p, [('b', '( ')])\n"
    "                        for k, o in enumerate(seg[1]):\n"
    "                            if k:\n"
    "                                _runs(p, [('b', '  /  ')])\n"
    "                            _runs(p, [('bblue', o)] if (self.key and k == seg[2]) else [('b', o)])\n"
    "                        _runs(p, [('b', ' )')])\n")
sub("                p = c1.add_paragraph(); _pfmt(p, after=2, line=1.3)\n", "                p = c1.add_paragraph(); _pfmt(p, after=2, line=1.5)\n")
p.write_text(s, encoding="utf-8")
print("patched")
