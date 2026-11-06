"""Embed one of the HTML/JS simulations in a Streamlit page."""
from pathlib import Path

import streamlit.components.v1 as components

SIMS = Path(__file__).resolve().parent.parent / "sims"

WRAPPER = """<!doctype html>
<html data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap" media="print" onload="this.media='all'">
<style>{shared}
html,body{{margin:0;background:#eef1f4}} body{{padding:6px 8px !important}}</style>
</head><body>{fragment}<script>{shared_js}</script></body></html>"""


def show_sim(name: str, height: int = 720) -> None:
    """Render sims/<name>.html inside the page at the given pixel height."""
    fragment = (SIMS / f"{name}.html").read_text(encoding="utf-8")
    shared = (SIMS / "_shared.css").read_text(encoding="utf-8")
    shared_js = (SIMS / "_shared.js").read_text(encoding="utf-8")
    components.html(WRAPPER.format(fragment=fragment, shared=shared, shared_js=shared_js), height=height, scrolling=True)
