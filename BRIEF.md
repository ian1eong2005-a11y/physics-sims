# Brief: 5086 Physics applets with quiz mode

Written 31 Oct 2026 from Ian's spoken instructions. This is the prompt the build follows.

## Who and why
Secondary 3/4 G3 Science (Physics) students, syllabus **5086** (SEAB, first exam 2024). Students do **not** have Claude accounts, so every applet is hosted on **Streamlit Community Cloud** from a public GitHub repo and opens in a browser with no login.

Pedagogy: the applets are used **collaboratively in class while the chapter is being taught** (the scaffold), then again for **self-study and revision**. They must guide students to see what is going on and make connections, never become a crutch. When students later meet worksheets and exam questions they should think "this is what I was doing in the applet".

## Design rules (every applet)
1. **Four modes** (Inquiry added 7 Nov 2026: predict → plan a fair test → record in a table → pattern → conclude, in core/inquiries.py). *Explore* (free play with "predict, then test" prompts), *Guided* (added 1 Nov 2026 for weaker students working alone: the app says what to do, what to look for, and asks a quick check before the next step unlocks) and *Quiz* (self-checking questions, the applet stays on screen so students use it to work out the answer).
2. **Simple.** One applet tackles one or two ideas. Students should be able to find the pattern themselves without being told. Few controls, each one tied to a learning outcome.
3. **A model, not a pedant.** Physically correct, but it is a visualisation. Do not add detail that is outside 5086 or that muddies the picture.
4. **5086 only.** Every control, label and question maps to a learning outcome in `Sec 3 and 4 G3 ScPhysics/knowledge/physics_5086_lo.json`. Nothing from 6091 Pure Physics (no total internal reflection, no resistivity formula, no EM induction, no potential dividers).
5. **Quiz questions** are tagged level 1–3 (recall → apply → explain) and self-check: MCQ, multi-select, put-in-order, numeric with tolerance, and short "explain" answers checked against key ideas with a model answer shown. Questions are written the way SEAB asks them: "describe how…", "explain why…", "state…".
6. **Explain-type questions tell students to use the applet** ("set the heater to the left end and watch the far end; then describe…").

## Build order
1. **Waves (Ch 9)**: wave graph mapper (d–x vs d–t, transverse/longitudinal), sound lab (speaker, compressions and rarefactions, loudness–amplitude, pitch–frequency, echo distance), ripple-tank wavefronts.
2. **EM spectrum (Ch 10)**: spectrum explorer: order by wavelength and frequency, all transverse and same speed in vacuum, the exact uses listed in 10c, hazards in 10d. Quiz levels 1–3 on applications and relative order only; **no v = fλ calculations**.
3. **Light (Ch 11)**: ray box (reflection, refraction, sin i / sin r, n = c/v, mystery block) and lens bench (converging lens action, focal length, image characteristics: real/virtual, magnified/diminished, upright/inverted).
4. **Internal energy (Ch 7)**: heating a substance through melting and boiling, with KE and PE bars: temperature (average KE) stops rising at the plateaus while PE rises.
5. Then the existing applets get quiz modes: kinematics (describe how the acceleration changes from A to B, B to C…), conduction, convection, resultant force, moments, circuits.
6. Then every remaining 5086 chapter (done 1 Nov 2026): measurements, force and pressure, energy, charge and current, practical electricity, magnetism and electromagnetism, radioactivity. One applet per chapter with 2–4 modes, so the whole syllabus is covered.

## Technical
- Each applet is a self-contained HTML/JS canvas simulation in `sims/`, embedded in Streamlit with `st.components.v1.html`. Streamlit handles navigation, the quiz engine and scoring; the HTML handles the animation.
- One page per chapter under `pages/`, tabs for Explore and Quiz. Question banks live in `quizzes/*.py` as plain Python lists.
- Repo: `physics-sims/` → GitHub (public) → Streamlit Cloud. `streamlit run app.py` for local checks.
