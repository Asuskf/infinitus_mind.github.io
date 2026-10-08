"""Regenerate the Infinitus Mind palette files and the brand cheat-sheet.

Outputs (Tier 2 — never hand-edit, re-run this script instead):
  assets/palette/palette.json                       palette + WCAG contrast figures
  assets/palette/palette.png                        swatch board
  assets/quick-reference/InfinitusMind_Brand_Cheatsheet.html   self-contained (fonts + logo embedded)

Source of truth: assets/tokens/colors_and_type.css (the base palette block).
Usage:  python assets/quick-reference/build_cheatsheet.py   (from the skill directory)
"""
import base64
import json
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SKILL = Path(__file__).resolve().parents[2]
ASSETS = SKILL / "assets"
TOKENS = (ASSETS / "tokens" / "colors_and_type.css").read_text(encoding="utf-8")

GROUPS = {
    "Base": ["void", "night", "ink-blue", "white"],
    "Mind (frío, cognitivo)": ["aqua", "sky", "cobalt", "cyan", "royal", "violet", "cerulean"],
    "Play (cálido, juego)": ["sun", "ember", "coral", "rose"],
    "Holograma": ["holo-blue", "holo-mist", "holo-lilac"],
    "Neutros": ["gray-300", "gray-500", "gray-600"],
}
NAMES = {
    "void": "Void Black", "night": "Night", "ink-blue": "Deep Ink", "white": "White",
    "aqua": "Neuro Aqua", "sky": "Synapse Sky", "cobalt": "Cobalt", "cyan": "Signal Cyan",
    "royal": "Royal Blue", "violet": "Infinite Violet", "cerulean": "Cerulean",
    "sun": "Zoo Sun", "ember": "Ember", "coral": "Coral", "rose": "Gummy Rose",
    "holo-blue": "Holo Blue", "holo-mist": "Holo Mist", "holo-lilac": "Holo Lilac",
    "gray-300": "Gray 300", "gray-500": "Gray 500", "gray-600": "Gray 600",
}


def lum(hex_):
    c = [int(hex_[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = lum(a), lum(b)
    return round((max(la, lb) + 0.05) / (min(la, lb) + 0.05), 2)


def verdict(r):
    if r >= 4.5:
        return "AA texto"
    if r >= 3:
        return "AA texto grande / UI"
    return "solo decorativo"


raw = dict(re.findall(r"--im-([a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})\s*;", TOKENS.split("/* ---- Role tokens")[0]))
void = raw["void"]
palette = []
for group, keys in GROUPS.items():
    for k in keys:
        h = raw[k].upper()
        rgb = tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
        on_void, white_on = ratio(h, void), ratio("#FFFFFF", h)
        palette.append({
            "group": group, "token": f"--im-{k}", "name": NAMES[k], "hex": h, "rgb": rgb,
            "contrast_on_void": on_void, "on_void": verdict(on_void),
            "white_text_on_it": white_on, "white_on": verdict(white_on),
        })

(ASSETS / "palette").mkdir(exist_ok=True)
(ASSETS / "palette" / "palette.json").write_text(json.dumps(palette, indent=2, ensure_ascii=False), encoding="utf-8")

# ---- Swatch board PNG ----
font_path = str(ASSETS / "fonts" / "montserrat.ttf")
body_path = str(ASSETS / "fonts" / "roboto.ttf")
f_title = ImageFont.truetype(font_path, 40)
f_title.set_variation_by_axes([700])
f_name = ImageFont.truetype(font_path, 20)
f_name.set_variation_by_axes([700])
f_meta = ImageFont.truetype(body_path, 16)
cols, sw, sh, pad = 7, 220, 200, 24
rows = sum((len(v) + cols - 1) // cols for v in GROUPS.values())
W = pad + cols * (sw + pad)
H = 120 + rows * (sh + 70) + len(GROUPS) * 40
img = Image.new("RGB", (W, H), void)
d = ImageDraw.Draw(img)
d.text((pad, 36), "Infinitus Mind — Paleta", font=f_title, fill="#FFFFFF")
y = 120
for group, keys in GROUPS.items():
    d.text((pad, y), group.upper(), font=f_meta, fill=raw["gray-500"].upper())
    y += 32
    for i, k in enumerate(keys):
        if i and i % cols == 0:
            y += sh + 70
        x = pad + (i % cols) * (sw + pad)
        h = raw[k].upper()
        d.rounded_rectangle([x, y, x + sw, y + sh], radius=10, fill=h, outline="#2A2A33")
        d.text((x, y + sh + 8), NAMES[k], font=f_name, fill="#FFFFFF")
        d.text((x, y + sh + 36), f"{h} · {ratio(h, void)}:1", font=f_meta, fill=raw["gray-500"].upper())
    y += sh + 78
img.save(ASSETS / "palette" / "palette.png", optimize=True)

# ---- Cheat-sheet HTML (self-contained) ----
def b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


fonts_css = (
    f'@font-face{{font-family:"Montserrat";src:url(data:font/woff2;base64,{b64(ASSETS/"fonts"/"montserrat-latin.woff2")}) format("woff2");font-weight:100 900;font-display:swap}}'
    f'@font-face{{font-family:"Roboto";src:url(data:font/woff2;base64,{b64(ASSETS/"fonts"/"roboto-latin.woff2")}) format("woff2");font-weight:100 900;font-display:swap}}'
)
role_block = TOKENS[TOKENS.index(":root,"):TOKENS.index("/* Light mode")]
logo = f"data:image/svg+xml;base64,{b64(ASSETS/'logos'/'infinitusmind-wordmark-white.svg')}"
mascot = f"data:image/webp;base64,{b64(ASSETS/'mascots'/'gummy-hologram.webp')}"

cards = []
for group, keys in GROUPS.items():
    items = "".join(
        f'<div class="sw"><div class="chip" style="background:{p["hex"]}"></div>'
        f'<b>{p["name"]}</b><code>{p["hex"]}</code><code>{p["token"]}</code>'
        f'<small>{p["contrast_on_void"]}:1 sobre Void · {p["on_void"]}</small></div>'
        for p in palette if p["group"] == group
    )
    cards.append(f'<h3>{group}</h3><div class="grid">{items}</div>')

grads = [("Mind — títulos de sección", "--im-grad-mind"), ("Play — títulos de juego", "--im-grad-play"),
         ("Heart — títulos de servicio", "--im-grad-heart"), ("Action AA — CTA con texto", "--im-grad-action-aa"), ("Action — solo sin texto", "--im-grad-action"),
         ("Icon — discos de íconos", "--im-grad-icon"), ("Holo — banda de contacto", "--im-grad-holo")]
grad_html = "".join(f'<div class="g"><div class="bar" style="background:var({t})"></div><b>{n}</b><code>{t}</code></div>' for n, t in grads)

html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Infinitus Mind Brand</title><style>{fonts_css}{role_block}
*{{box-sizing:border-box}}body{{margin:0;background:var(--im-color-bg);color:var(--im-color-text);font-family:var(--im-font-body);line-height:var(--im-leading-body)}}
main{{max-width:1100px;margin:0 auto;padding:var(--im-space-5) var(--im-space-3)}}
header{{display:flex;align-items:center;justify-content:space-between;gap:var(--im-space-4);flex-wrap:wrap}}
header img.logo{{height:48px;width:auto}}header img.m{{height:180px;width:auto}}
h1,h2,h3{{font-family:var(--im-font-display);font-weight:var(--im-weight-bold);line-height:var(--im-leading-tight)}}
h1{{font-size:var(--im-text-display-sm);text-transform:uppercase;background:var(--im-grad-mind);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}}
h2{{font-size:1.75rem;margin-top:var(--im-space-5);text-transform:uppercase}}h3{{font-size:1rem;color:var(--im-color-text-muted);letter-spacing:var(--im-tracking-caps);text-transform:uppercase}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:var(--im-space-3)}}
.sw{{display:flex;flex-direction:column;gap:2px;font-size:var(--im-text-small)}}.chip{{height:90px;border-radius:var(--im-radius-card);border:1px solid var(--im-color-border);margin-bottom:6px}}
code{{color:var(--im-color-text-muted);font-size:.8rem}}small{{color:var(--im-color-text-muted)}}
.gr{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:var(--im-space-3)}}.g{{display:flex;flex-direction:column;gap:4px}}.bar{{height:56px;border-radius:var(--im-radius-card)}}
.type p{{margin:.25rem 0}}.d{{font-family:var(--im-font-display);font-weight:700;font-size:var(--im-text-hero-sm);text-transform:uppercase}}
.btn{{display:inline-block;padding:1.25rem 2.5rem;border-radius:var(--im-radius-pill);background:var(--im-grad-action-aa);color:var(--im-white);font-family:var(--im-font-display);font-weight:700;text-transform:uppercase;text-decoration:none;text-shadow:0 1px 2px rgba(0,0,0,.45)}}
ul.rules li{{margin:.35rem 0}}
@media print{{body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}}}
</style></head><body><main>
<header><div><img class="logo" src="{logo}" alt="Infinitus Mind"><h1>Brand guidelines</h1>
<p>Videojuegos que evalúan y desarrollan habilidades blandas. Oscuro, luminoso, lúdico, con base científica.</p></div>
<img class="m" src="{mascot}" alt="Gummy, la mascota holográfica de Infinitus Mind"></header>
<h2>Paleta</h2>{''.join(cards)}
<h2>Degradados de firma</h2><div class="gr">{grad_html}</div>
<h2>Tipografía</h2><div class="type"><p class="d">Montserrat Bold — Display</p>
<p style="font-family:var(--im-font-display)">Montserrat 400/700 · títulos, navegación, botones (MAYÚSCULAS)</p>
<p>Roboto 400/700 · cuerpo, subtítulos, descripciones. Cuerpo mínimo 16px.</p></div>
<h2>Botón principal</h2><p><a class="btn" href="#">Quiero saber más</a></p>
<h2>Reglas clave</h2><ul class="rules">
<li>Fondo siempre Void <code>#0A090F</code>; el sitio es oscuro de forma nativa.</li>
<li>Los degradados viven en títulos, CTA y momentos de marca, nunca en texto de párrafo.</li>
<li>Violeta <code>#5640D6</code> y Cobalt <code>#004CEF</code> no van como texto de cuerpo (contraste &lt; 4.5:1).</li>
<li>Logo solo desde archivo (wordmark blanco); nunca redibujar ni recolorear.</li>
<li>Gummy (mascota) humaniza; una aparición por sección como máximo.</li></ul>
</main></body></html>"""
(ASSETS / "quick-reference" / "InfinitusMind_Brand_Cheatsheet.html").write_text(html, encoding="utf-8")
print("palette.json, palette.png, InfinitusMind_Brand_Cheatsheet.html regenerated")
