"""Build the Pride Epoxy scheme letter (HTML + PDF).
Drop the product photo at pride-scheme/pride.jpg (or .png/.webp) and re-run: python3 build.py"""
import base64, pathlib, mimetypes
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
SIZES = [("0.5 L", 126, 269), ("1 L", 233, 499), ("4 L", 925, 1999), ("20 L", 4360, 8999)]
SLABS = [("Up to 100 Litres", 7.0), ("100 – 200 Litres", 9.5), ("200 – 300 Litres", 12.0),
         ("300 – 500 Litres", 14.2), ("500 – 1000+ Litres", 15.8)]

def money(x): return f"{x:,.2f}"

photo = next((p for p in HERE.glob("pride.*") if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")), None)
if photo:
    uri = f"data:{mimetypes.guess_type(photo.name)[0]};base64,{base64.b64encode(photo.read_bytes()).decode()}"
    photo_html = f'<img src="{uri}" alt="Pride Epoxy">'
else:
    photo_html = '<div class="ph">PRIDE EPOXY<br><small>product photo</small></div>'

# Summary: landing per pack across slabs
summary_rows = ""
for name, dpl, mrp in SIZES:
    cells = "".join(f"<td>₹{round(dpl*(1-d/100)*1.18):,}</td>" for _, d in SLABS)
    summary_rows += f"<tr><th>{name}</th><td>₹{dpl:,}</td>{cells}<td class='mrp'>₹{mrp:,}</td></tr>"

detail = ""
for slab, d in SLABS:
    rows = ""
    for name, dpl, mrp in SIZES:
        disc = dpl*d/100; net = dpl-disc; gst = net*0.18
        rows += (f"<tr><th>{name}</th><td>{dpl:,}</td><td>{money(disc)}</td><td>{money(net)}</td>"
                 f"<td>{money(gst)}</td><td class='land'>₹{round(net+gst):,}</td><td>₹{mrp:,}</td></tr>")
    detail += f"""<div class="slab"><div class="sh"><span>{slab}</span><b>{d}% In-Bill Discount</b></div>
<table><thead><tr><th>Pack</th><th>DPL</th><th>Discount</th><th>Net DPL</th><th>GST 18%</th><th>Landing</th><th>MRP</th></tr></thead>
<tbody>{rows}</tbody></table></div>"""

slab_cols = "".join(f"<th>{s}<br><b>{d}%</b></th>" for s, d in SLABS)

html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Pride Epoxy Scheme</title>
<style>
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
body {{ margin:0; font-family: 'Segoe UI', Arial, sans-serif; color:#1d2433; font-size:11.5px }}
.page {{ width:210mm; min-height:297mm; padding:14mm 15mm 12mm; position:relative; page-break-after:always }}
.page:last-child {{ page-break-after:auto }}
header {{ display:flex; justify-content:space-between; align-items:flex-end; border-bottom:3px solid #1f3fa8; padding-bottom:8px }}
.brand {{ font-size:26px; font-weight:800; letter-spacing:1px; color:#1f3fa8 }}
.brand small {{ display:block; font-size:10px; color:#5a6272; letter-spacing:2px; font-weight:600 }}
.meta {{ text-align:right; color:#5a6272; font-size:10.5px; line-height:1.6 }}
.hero {{ display:flex; gap:18px; margin:16px 0 12px; align-items:center;
  background:linear-gradient(120deg,#0d1b4f,#1f3fa8); color:#fff; border-radius:10px; padding:16px 20px }}
.hero img, .ph {{ width:190px; height:190px; object-fit:cover; background:#fff; border-radius:8px; flex:none }}
.ph small {{ display:block; font-weight:500 }}
.ph {{ display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; color:#1f3fa8;
  font-weight:800; border:2px dashed #1f3fa8 }}
.hero h1 {{ margin:0 0 4px; font-size:28px; letter-spacing:.5px }}
.hero p {{ margin:0; color:#d6defa; font-size:13px }}
.hero .tag {{ display:inline-block; margin-top:10px; background:#ffd400; color:#1d2433; font-weight:800;
  padding:5px 12px; border-radius:20px; font-size:13px }}
p.body {{ line-height:1.6; margin:8px 0 }}
h2 {{ font-size:13px; color:#1f3fa8; text-transform:uppercase; letter-spacing:1px; margin:16px 0 6px }}
table {{ width:100%; border-collapse:collapse; font-size:11px }}
th, td {{ border:1px solid #d5d9e0; padding:5px 6px; text-align:right }}
thead th {{ background:#1d2433; color:#fff; text-align:center; font-weight:600 }}
tbody th {{ text-align:left; background:#f5f6f8 }}
.sum td {{ font-weight:700 }}
.sum td.mrp, .land {{ background:#fff6c2; font-weight:700 }}
.slabs {{ display:grid; grid-template-columns:1fr; gap:8px }}
.slab {{ border:1px solid #d5d9e0; border-radius:8px; overflow:hidden }}
.slab table th, .slab table td {{ border-left:0; border-right:0 }}
.sh {{ display:flex; justify-content:space-between; background:#1f3fa8; color:#fff; padding:6px 10px; font-weight:600 }}
.sh b {{ background:#fff; color:#1f3fa8; border-radius:12px; padding:0 8px }}
ol {{ margin:4px 0 0 16px; padding:0; line-height:1.6 }}
.sign {{ display:flex; justify-content:space-between; margin-top:26px }}
.sign div {{ border-top:1px solid #1d2433; padding-top:4px; width:180px; text-align:center; font-weight:600 }}
footer {{ position:absolute; bottom:8mm; left:15mm; right:15mm; text-align:center; font-size:9.5px; color:#5a6272;
  border-top:1px solid #d5d9e0; padding-top:4px }}
</style></head><body>

<section class="page">
<header><div class="brand">TURBOLUX PAINTS<small>EXCELLENCE IN EVERY COAT</small></div>
<div class="meta">Ref: TLX/SCH/PRIDE/____<br>Date: ____________</div></header>

<div class="hero">{photo_html}
<div><h1>PRIDE EPOXY</h1><p>Volume-Slab In-Bill Discount Scheme</p>
<span class="tag">Up to 15.8% IN-BILL DISCOUNT</span></div></div>

<p class="body">To,<br><b>All Dealers &amp; Distributors</b></p>
<p class="body"><b>Subject: Volume scheme on Pride Epoxy – in-bill discount and landing price</b></p>
<p class="body">Dear Partner,<br>We are pleased to announce a volume-based scheme on <b>Pride Epoxy</b>.
The more litres you buy, the higher your in-bill discount: from <b>7%</b> up to <b>15.8%</b> off DPL.
The discount is given directly on the invoice, so you get the benefit right away.</p>

<h2>Discount slabs</h2>
<table class="sum"><thead><tr><th>Purchase volume</th>{"".join(f"<th>{s}</th>" for s,_ in SLABS)}</tr></thead>
<tbody><tr><th>In-bill discount</th>{"".join(f"<td style='text-align:center'>{d}%</td>" for _,d in SLABS)}</tr></tbody></table>

<h2>Landing price per pack (incl. 18% GST)</h2>
<table class="sum"><thead><tr><th>Pack</th><th>DPL</th>{slab_cols}<th>MRP</th></tr></thead>
<tbody>{summary_rows}</tbody></table>

<h2>Terms &amp; conditions</h2>
<ol>
<li>The slab is decided by the total Pride Epoxy litres in a single order. All pack sizes count.</li>
<li>The discount is given in-bill on DPL. GST at 18% is charged on the price after discount.</li>
<li>Landing prices are rounded to the nearest rupee. Please sell at or below the printed MRP.</li>
<li>Scheme period: ____________ to ____________.</li>
<li>Turbolux Paints may change or withdraw this scheme without prior notice. The management's decision is final.</li>
</ol>
<p class="body">For orders and details, please contact your Turbolux sales representative.</p>
<div class="sign"><div>Sales Manager</div><div>For Turbolux Paints</div></div>
<footer>www.turboluxpaints.com &nbsp;·&nbsp; customercare@turboluxpaints.com</footer>
</section>

<section class="page">
<header><div class="brand">TURBOLUX PAINTS<small>PRIDE EPOXY – SLAB-WISE WORKING</small></div>
<div class="meta">Annexure A</div></header>
<h2>Detailed working for each slab (₹)</h2>
<div class="slabs">{detail}</div>
<p class="body" style="margin-top:12px">Net DPL = DPL – in-bill discount. Landing = Net DPL + 18% GST.</p>
<footer>www.turboluxpaints.com &nbsp;·&nbsp; customercare@turboluxpaints.com</footer>
</section>
</body></html>"""

(HERE / "Pride_Epoxy_Scheme_Letter.html").write_text(html, encoding="utf-8")
with sync_playwright() as p:
    exe = "/opt/pw-browsers/chromium"; b = p.chromium.launch(executable_path=exe) if pathlib.Path(exe).exists() else p.chromium.launch(); pg = b.new_page()
    pg.set_content(html); pg.pdf(path=str(HERE / "Pride_Epoxy_Scheme_Letter.pdf"), format="A4", print_background=True)
    pg.set_viewport_size({"width": 794, "height": 1123}); pg.screenshot(path=str(HERE / "preview.png"), full_page=True)
    b.close()
print("photo:", photo)
