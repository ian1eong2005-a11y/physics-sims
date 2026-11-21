"""Contact sheet of harness snapshots: python ntsci/tools/sheet.py <prefix> [cols]  ->  .harness/shots/<prefix>_sheet.jpg"""
import pathlib, sys
from PIL import Image
d = pathlib.Path(__file__).resolve().parents[2] / ".harness" / "shots"
prefix = sys.argv[1]; cols = int(sys.argv[2]) if len(sys.argv) > 2 else 3
fs = sorted(d.glob(prefix + "_[0-9]*.jpg"), key=lambda f: int(f.stem.rsplit("_", 1)[1]))
ims = [Image.open(f) for f in fs]
w, h = ims[0].size; w2, h2 = w * 2 // 3, h * 2 // 3
rows = (len(ims) + cols - 1) // cols
out = Image.new("RGB", (w2 * cols, h2 * rows), "white")
for i, im in enumerate(ims):
    out.paste(im.resize((w2, h2)), ((i % cols) * w2, (i // cols) * h2))
out.save(d / f"{prefix}_sheet.jpg", quality=85)
print(len(ims), "shots ->", d / f"{prefix}_sheet.jpg")
