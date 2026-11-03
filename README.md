# 5086 Physics Applets

Interactive models with self-checking quizzes for G3 Science (Physics), syllabus 5086. Built for Queenstown Secondary School.

Each chapter page has three tabs: **Explore** (the applet plus predict-then-test prompts), **Guided** (a step-by-step walkthrough for students working alone: do this, look for this, quick check before the next step) and **Quiz** (levels 1–3, self-checking, with the applet alongside).

| Page | Chapter | Applets |
|---|---|---|
| Waves | Ch 9 General Wave Properties | Wave Graph Mapper, Sound Lab, Ripple Tank |
| EM Spectrum | Ch 10 | EM Spectrum Explorer |
| Light | Ch 11 | Ray Box, Lens Bench |
| Internal Energy | Ch 7 Kinetic Particle Model | Heating Curve Lab |
| Kinematics | Ch 2 | Kinematics Graph Matcher |
| Thermal Processes | Ch 8 | Conduction Lab, Convection Tank, Radiation Lab |
| Forces | Ch 4–5 | Resultant Force Trolley, Moments See-saw |
| Circuits | Ch 13 | Series and Parallel Bench |
| Measurements | Ch 1 | Measuring Lab |
| Force and Pressure | Ch 3 | Weight, Density and Pressure Bench |
| Energy | Ch 6 | Energy Coaster |
| Charge and Current | Ch 12 | Charge and Current Lab |
| Practical Electricity | Ch 14 | Home Electricity |
| Magnetism | Ch 15 | Magnet and Motor Lab |
| Radioactivity | Ch 16 | Decay Lab |

**Live app:** https://ian1eong2005-a11y-physics-sims-app-rk6zvk.streamlit.app/

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (Streamlit Community Cloud)

Repository: https://github.com/ian1eong2005-a11y/physics-sims

1. Sign in at https://share.streamlit.io with the GitHub account that owns this repo.
2. Open https://share.streamlit.io/deploy?repository=ian1eong2005-a11y/physics-sims&branch=main&mainModule=app.py
   (or choose **Create app**, then repo `ian1eong2005-a11y/physics-sims`, branch `main`, main file `app.py`).
3. Optionally pick a custom subdomain, e.g. `qtss-physics.streamlit.app`, then **Deploy**.
4. Share the app URL with students. No login is needed to use it.

Every push to `main` redeploys the app automatically.

## Lower Secondary Science app (2021 LSS)

A second app in the same repo, for Sec 1–2, with the same Explore / Guided / Quiz layout. Main file: `lowersec_app.py` (pages in `lowersec/`, quiz banks `quizzes/lss_*.py`).

| Page | Chapter | Applet |
|---|---|---|
| Digestive System | Ch 14 | Digestion Lab: journey of food, enzyme test tube, blood glucose |
| Transport in Humans | Ch 15 | Human Transport Lab: circulation, diffusion close-up, why a transport system (G3) |
| Transport in Plants | Ch 15 | Plant Transport Lab: xylem and phloem with dye, root hair and osmosis (G3), leaf gases |
| Reproductive System | Ch 16 | Reproduction Lab: parts and functions, menstrual cycle, fertilisation and birth control |

Deploy it as its own Streamlit Cloud app: https://share.streamlit.io/deploy?repository=ian1eong2005-a11y/physics-sims&branch=main&mainModule=lowersec_app.py

Run locally: `streamlit run lowersec_app.py`

## Layout

- `sims/*.html` – one HTML/JS canvas simulation per applet (embedded with `st.components.v1.html`; `_shared.css` is inlined by the embed helper).
- `quizzes/*.py` – question banks: `mcq`, `multi`, `order`, `numeric`, `explain` (key-idea checking with a model answer).
- `core/` – embed helper, quiz engine, guided-mode walkthroughs (`guides.py`), shared page layout.
- `pages/` – one Streamlit page per chapter.
- `BRIEF.md` – the design brief the applets follow.

Scope: every control and question maps to a 5086 learning outcome. Nothing from 6091 Pure Physics.
