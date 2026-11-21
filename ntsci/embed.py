"""Embed one of the G1 / N(T) applets (nt/sims/*.html) in a Streamlit page."""
import json
from pathlib import Path

import streamlit.components.v1 as components

SIMS = Path(__file__).resolve().parent / "sims"

WRAPPER = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{css}</style>
<script>{kit}</script>
</head><body><script>window.SIM_OPTS={opts};</script>{fragment}</body></html>"""


def build(name: str, opts: dict | None = None) -> str:
    """The full HTML page for one applet (also used by the test harness)."""
    return WRAPPER.format(
        css=(SIMS / "_nt.css").read_text(encoding="utf-8"),
        kit=(SIMS / "_nt.js").read_text(encoding="utf-8"),
        opts=json.dumps(opts or {}),
        fragment=(SIMS / f"{name}.html").read_text(encoding="utf-8"),
    )


def show(name: str, height: int = 760, opts: dict | None = None) -> None:
    """opts {"inq": 1} opens the applet with its step-by-step investigation panel."""
    components.html(build(name, opts), height=height, scrolling=True)
