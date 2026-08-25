"""Crop diagram regions out of the lecture decks for use as reader figures."""
import subprocess, glob, os
from PIL import Image

DPI = 150
OUT = "../reader/figures"
os.makedirs(OUT, exist_ok=True)

# (deck pdf, page, output name, crop box in inches (l, t, r, b))
FIGS = [
    ("../lecture-01/output/L1-*.pdf", 14, "fig1-1-measurement-chain",   (0.5, 1.95, 12.9, 6.55)),
    ("../lecture-01/output/L1-*.pdf", 15, "fig1-2-chain-with-numbers",  (0.5, 1.95, 12.9, 5.95)),
    ("../lecture-01/output/L1-*.pdf", 21, "fig1-3-inside-accelerometer",(0.5, 1.95, 12.9, 5.45)),
    ("../lecture-01/output/L1-*.pdf", 39, "fig1-4-aliasing",            (0.5, 1.95, 12.9, 6.65)),
    ("../lecture-02/output/L2-*.pdf",  4, "fig2-1-two-front-pages",     (0.5, 1.85, 12.9, 6.85)),
    ("../lecture-02/output/L2-*.pdf",  8, "fig2-2-accuracy-precision",  (0.5, 1.95, 12.9, 5.60)),
    ("../lecture-02/output/L2-*.pdf", 14, "fig2-3-conditions-block",    (0.5, 1.95, 12.9, 5.85)),
]

for pattern, page, name, (l, t, r, b) in FIGS:
    pdf = glob.glob(pattern)[0]
    tmp = f"/tmp/_fig_{name}"
    subprocess.run(["pdftoppm", "-png", "-r", str(DPI), "-f", str(page), "-l", str(page),
                    pdf, tmp], check=True)
    src = glob.glob(tmp + "*.png")[0]
    im = Image.open(src)
    im.crop((int(l*DPI), int(t*DPI), int(r*DPI), int(b*DPI))).save(f"{OUT}/{name}.png")
    os.remove(src)
    print(f"{name}.png")
