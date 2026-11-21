# 3NT applet inquiry worksheets

One-page worksheets (plus an answers page) that follow each applet's investigation.

1. Export the investigation data from the applets: start the `nt-harness` preview, open `/nt-runner.html`
   and run `await dump([...applet names...])`. It saves `.harness/shots/wsdata.jpg` (really JSON) and
   `ws_<applet>_<k>.jpg` pictures. Copy them here as `wsdata.json` and `img/`.
2. `python build.py` builds the .docx files into `out/` (QR codes point at the live app,
   `https://qtss-g1-science.streamlit.app/<topic>?applet=<file>&mode=investigate`).
3. `python render.py` makes PDFs through Word and reports any sheet that is not exactly 2 pages.

`wsinq.py` is the QTSS one-page inquiry builder already patched for N(T) (bigger type, Sec 3 G1 header,
tick lists, circle-the-word); `patch.py` records what was changed. To add Topics 6-11, add rows to `SHEETS`
and `TOPIC` in `build.py`.
