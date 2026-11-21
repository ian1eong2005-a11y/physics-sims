"""Render out/*.docx to pdf/, report page counts, and make contact sheets of the student pages (page 1) and answer pages."""
import glob, os, subprocess, sys
import fitz
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
docs = sorted(glob.glob(os.path.join(here, 'out', '*.docx')))
only = sys.argv[1:]
if only: docs = [d for d in docs if any(('Inquiry ' + c + ' ') in d for c in only)]
subprocess.run([sys.executable, r"C:\Users\pirat\.claude\skills\qtss-WS-quiz-template-skill\tools\office_pdf.py", os.path.join(here, 'pdf')] + docs, check=True, stdout=subprocess.DEVNULL)
pages = {}
for d in docs:
    pdf = os.path.join(here, 'pdf', os.path.splitext(os.path.basename(d))[0] + '.pdf')
    doc = fitz.open(pdf); code = os.path.basename(d).split('Inquiry ')[1].split(' ')[0]
    pages[code] = doc.page_count
    for i in range(min(doc.page_count, 3)):
        doc[i].get_pixmap(dpi=70).save(os.path.join(here, 'pdf', f'p_{code}_{i+1}.png'))
print(' '.join(f'{c}:{n}' for c, n in pages.items()))
print('NOT 2 PAGES:', [c for c, n in pages.items() if n != 2])
