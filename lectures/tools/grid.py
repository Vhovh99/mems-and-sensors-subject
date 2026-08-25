import sys, glob, os, subprocess
from PIL import Image
pptx, prefix, cols = sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv)>3 else 4
per = cols*3
work = prefix+"_w"; os.makedirs(work, exist_ok=True)
subprocess.run(["libreoffice","--headless","--convert-to","pdf","--outdir",work,pptx],
               check=True, capture_output=True, timeout=600)
pdf = glob.glob(work+"/*.pdf")[0]
subprocess.run(["pdftoppm","-jpeg","-r","62",pdf,work+"/p"],check=True)
imgs = sorted(glob.glob(work+"/p-*.jpg"))
for gi in range(0,len(imgs),per):
    chunk = imgs[gi:gi+per]
    im0 = Image.open(chunk[0]); tw,th = im0.size
    pad, lab = 8, 20
    rows = (len(chunk)+cols-1)//cols
    sheet = Image.new("RGB",(cols*(tw+pad)+pad, rows*(th+pad+lab)+pad),(210,210,210))
    from PIL import ImageDraw
    d = ImageDraw.Draw(sheet)
    for i,f in enumerate(chunk):
        r,c = divmod(i,cols)
        x = pad+c*(tw+pad); y = pad+r*(th+pad+lab)
        sheet.paste(Image.open(f),(x,y+lab))
        d.text((x+3,y+4), f"slide {gi+i+1}", fill=(20,20,20))
    out = f"{prefix}-{gi//per+1}.jpg"; sheet.save(out,quality=82)
    print(out, sheet.size)
print("slides:", len(imgs))
