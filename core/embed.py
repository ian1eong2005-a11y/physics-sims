"""Embed one of the HTML/JS simulations in a Streamlit page."""
from pathlib import Path

import streamlit.components.v1 as components

SIMS = Path(__file__).resolve().parent.parent / "sims"

WRAPPER = """<!doctype html>
<html data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>html,body{{margin:0;background:#eef1f4}} body{{padding:6px 8px !important}}</style>
</head><body>{fragment}</body></html>"""


def show_sim(name: str, height: int = 720) -> None:
    """Render sims/<name>.html inside the page at the given pixel height."""
    fragment = (SIMS / f"{name}.html").read_text(encoding="utf-8")
    components.html(WRAPPER.format(fragment=fragment), height=height, scrolling=True)
