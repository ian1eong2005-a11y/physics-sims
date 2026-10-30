# 5086 Physics Applets

Interactive models with self-checking quizzes for G3 Science (Physics), syllabus 5086. Built for Queenstown Secondary School.

Each chapter page has an **Explore** tab (the applet plus predict-then-test prompts) and a **Quiz** tab (levels 1–3, self-checking, with the applet alongside).

| Page | Chapter | Applets |
|---|---|---|
| Waves | Ch 9 General Wave Properties | Wave Graph Mapper, Sound Lab, Ripple Tank |
| EM Spectrum | Ch 10 | EM Spectrum Explorer |
| Light | Ch 11 | Ray Box, Lens Bench |
| Internal Energy | Ch 7 Kinetic Particle Model | Heating Curve Lab |
| Kinematics | Ch 2 | Kinematics Graph Matcher |
| Thermal Processes | Ch 8 | Conduction Lab, Convection Tank |
| Forces | Ch 4–5 | Resultant Force Trolley, Moments See-saw |
| Circuits | Ch 13 | Series and Parallel Bench |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (Streamlit Community Cloud)

1. Push this folder to a public GitHub repository.
2. At share.streamlit.io choose **New app**, pick the repo, branch `main`, main file `app.py`.
3. Share the app URL with students. No login is needed to use it.

## Layout

- `sims/*.html` – one self-contained HTML/JS canvas simulation per applet (embedded with `st.components.v1.html`).
- `quizzes/*.py` – question banks: `mcq`, `multi`, `order`, `numeric`, `explain` (key-idea checking with a model answer).
- `core/` – embed helper, quiz engine, shared page layout.
- `pages/` – one Streamlit page per chapter.
- `BRIEF.md` – the design brief the applets follow.

Scope: every control and question maps to a 5086 learning outcome. Nothing from 6091 Pure Physics.
