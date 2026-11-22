"""Render out/*Quiz*.docx to pdf/ and save page PNGs; prints page counts."""
import glob, os, subprocess, sys
import fitz
here = os.path.dirname(os.path.abspath(__file__))
pat = sys.argv[1] if len(sys.argv) > 1 else '*Quiz*'
docs = sorted(glob.glob(os.path.join(here, 'out', pat + '.docx')))
os.makedirs(os.path.join(here, 'pdf'), exist_ok=True)
subprocess.run([sys.executable, r"C:\Users\pirat\.claude\skills\qtss-WS-quiz-template-skill\tools\office_pdf.py", os.path.join(here, 'pdf')] + docs, check=True, stdout=subprocess.DEVNULL)
for d in docs:
    pdf = os.path.join(here, 'pdf', os.path.splitext(os.path.basename(d))[0] + '.pdf')
    doc = fitz.open(pdf); tag = os.path.basename(d).split(' - ')[0].replace('3NT ', '').replace(' ', '')
    print(tag, doc.page_count)
    for i in range(doc.page_count):
        doc[i].get_pixmap(dpi=60).save(os.path.join(here, 'pdf', f'q_{tag}_{i+1}.png'))
