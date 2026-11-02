"""Generate ICPC logo option SVGs (marks + lockups) in light and dark palettes.
Usage: python3 -I gen.py <outdir>
Writes <outdir>/<option>-mark-{light,dark}.svg, <option>-lockup-{light,dark}.svg
and <outdir>/snippets.json with the inline <svg> bodies for the gallery page."""
import sys, os, json, math

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

PAL = {
    "light": dict(brand="#1D5FBF", ink="#0B2A4A", accent="#F0A830", paper="#FFFFFF", onbrand="#FFFFFF", tint="#DCE9F9"),
    "dark":  dict(brand="#6DB1FF", ink="#F3F7FC", accent="#FFC14D", paper="#0E1726", onbrand="#0B2A4A", tint="#1C2E4A"),
}

S = 11  # stroke width for constructed letterforms

def arc_c(cx, cy, r, open_deg=50):
    """C shape: circular arc opening to the right, gap of 2*open_deg degrees."""
    a = math.radians(open_deg)
    x1, y1 = cx + r*math.cos(a), cy - r*math.sin(a)
    x2, y2 = cx + r*math.cos(a), cy + r*math.sin(a)
    return f"M{x1:.2f},{y1:.2f} A{r},{r} 0 1 0 {x2:.2f},{y2:.2f}"

def wordmark_upper(color, gap=9):
    """ICPC in constructed geometric capitals, letters placed by ink extents. Box height 72."""
    h = S/2
    c = 27*math.cos(math.radians(50))  # x-extent of the C's open terminals
    parts = []
    x = h                                    # I: stem centerline
    parts.append(f'<path d="M{x},6 V66"/>')
    right = x + h
    cx = right + gap + h + 27                # C: ink left = cx-27-h
    parts.append(f'<path d="{arc_c(cx, 36, 27)}"/>')
    right = cx + c + h*0.64
    x = right + gap + h                      # P: stem centerline
    parts.append(f'<path d="M{x},66 V6 H{x+18.5} A16,16 0 0 1 {x+18.5},38 H{x}"/>')
    right = x + 18.5 + 16 + h
    cx = right + gap + h + 27                # C
    parts.append(f'<path d="{arc_c(cx, 36, 27)}"/>')
    right = cx + c + h*0.64
    return (f'<g fill="none" stroke="{color}" stroke-width="{S}" stroke-linecap="butt" stroke-linejoin="round">'
            + "".join(parts) + "</g>"), right, 72

def wordmark_lower(color, accent, gap=8):
    """icpc in constructed rounded lowercase, placed by ink extents. Box height 92."""
    h = S/2
    c = 20*math.cos(math.radians(50))
    parts = []
    x = h
    parts.append(f'<path d="M{x},28 V66"/>')                      # i stem
    dot = f'<circle cx="{x}" cy="9" r="7" fill="{accent}"/>'
    right = x + h
    cx = right + gap + h + 20
    parts.append(f'<path d="{arc_c(cx, 46, 20)}"/>')             # c
    right = cx + c + h*0.64
    x = right + gap + h
    parts.append(f'<path d="M{x},26 V86"/><circle cx="{x+20}" cy="46" r="20"/>')  # p
    right = x + 40 + h
    cx = right + gap + h + 20
    parts.append(f'<path d="{arc_c(cx, 46, 20)}"/>')             # c
    right = cx + c + h*0.64
    return (f'<g fill="none" stroke="{color}" stroke-width="{S}" stroke-linecap="round" stroke-linejoin="round">'
            + "".join(parts) + "</g>" + dot), right, 92

# ---------------------------------------------------------------- marks (100x100)
def mark_lens(p):
    return f'''<circle cx="50" cy="50" r="38" fill="none" stroke="{p['brand']}" stroke-width="10"/>
<g stroke-linecap="round" stroke-width="9" fill="none">
  <path d="M31,38 H61" stroke="{p['brand']}"/>
  <path d="M39,50 H69" stroke="{p['accent']}"/>
  <path d="M31,62 H55" stroke="{p['brand']}"/>
</g>'''

def mark_clarity(p):
    rows = []
    specs = [(27, [(22,15),(42.5,15),(63,15)]), (45.5, [(22,25),(53,25)]), (64, [(22,56)])]
    for i, (y, segs) in enumerate(specs):
        col = p['accent'] if i == 2 else p['onbrand']
        for (x, w) in segs:
            rows.append(f'<rect x="{x}" y="{y}" width="{w}" height="11" rx="5.5" fill="{col}"/>')
    return f'<rect x="4" y="4" width="92" height="92" rx="22" fill="{p["brand"]}"/>\n' + "\n".join(rows)

def mark_monogram(p):
    # 2x2 grid of stroke letters inside a rounded square; letters scaled 0.36 of the 72-box
    s = 0.5
    g = f'<g fill="none" stroke="{p["onbrand"]}" stroke-width="13" stroke-linecap="butt" stroke-linejoin="round">'
    # top-left I, top-right C, bottom-left P, bottom-right C  (each drawn in a 72x72 cell-space then scaled)
    cell = lambda tx, ty, body: f'<g transform="translate({tx},{ty}) scale({s})">{body}</g>'
    I = '<path d="M36,6 V66"/>'
    C = f'<path d="{arc_c(36,36,27)}"/>'
    P = '<path d="M17,66 V6 H37 A16,16 0 0 1 37,38 H17"/>'
    inner = cell(11,11,I) + cell(49,11,C) + cell(11,51,P) + cell(49,51,C)
    return (f'<rect x="4" y="4" width="92" height="92" rx="22" fill="{p["brand"]}"/>\n' + g + inner + '</g>')

def mark_heritage(p):
    # compact pill badge with the lowercase wordmark
    wm, w, h = wordmark_lower(p['onbrand'], p['accent'])
    sc = 72 / w
    return (f'<rect x="2" y="26" width="96" height="48" rx="24" fill="{p["brand"]}"/>\n'
            f'<g transform="translate(14,{50 - (h*sc)/2 + 2}) scale({sc:.4f})">{wm}</g>')

def mark_graph(p):
    nodes = [(50,20),(28,48),(72,48),(16,78),(40,78),(62,78),(84,78)]
    edges = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
    e = "".join(f'<path d="M{nodes[a][0]},{nodes[a][1]} L{nodes[b][0]},{nodes[b][1]}"/>' for a,b in edges)
    n = "".join(f'<circle cx="{x}" cy="{y}" r="{7 if i else 10}" fill="{p["accent"] if i==0 else p["brand"]}"/>' for i,(x,y) in enumerate(nodes))
    return f'<g stroke="{p["brand"]}" stroke-width="5" fill="none" stroke-linecap="round">{e}</g>\n{n}'

OPTIONS = {
    "lens":     ("A", "Lens",     mark_lens,     "Code seen through a lens: three lines of code inside a ring, with the line being understood lit in amber. Reads as careful looking rather than searching."),
    "clarity":  ("B", "Clarity",  mark_clarity,  "Fragments resolving into a whole, top to bottom. Comprehension as the moment scattered pieces become one clear line."),
    "monogram": ("C", "Monogram", mark_monogram, "The four letters set as a tight grid in a rounded tile. Restrained and institutional, with no metaphor to age."),
    "heritage": ("D", "Heritage", mark_heritage, "A direct descendant of the original lowercase icpc wordmark: upright, rounded, geometric, with the dot of the i as the single accent."),
    "graph":    ("E", "Structure",mark_graph,    "A small syntax tree with its root lit. Program comprehension as understanding structure, from the root down."),
}

def svg(body, w, h, extra=""):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"{extra}>\n{body}\n</svg>\n'

def lockup(key, p):
    mark = OPTIONS[key][2](p)
    if key == "heritage":
        wm, ww, wh = wordmark_lower(p['brand'], p['accent'])
        # wordmark only lockup, with tagline beneath
        body = f'<g transform="translate(0,0)">{wm}</g>'
        tag_y = wh + 26
        body += (f'<text x="0" y="{tag_y}" font-family="Manrope, Helvetica Neue, Arial, sans-serif" font-size="17" '
                 f'font-weight="600" letter-spacing="0.5" fill="{p["ink"]}">IEEE International Conference on Program Comprehension</text>')
        return svg(body, 560, tag_y + 10)
    wm, ww, wh = wordmark_upper(p['brand'])
    # mark at 92px tall, wordmark to its right, tagline beneath wordmark
    body = f'<g transform="translate(0,0)">{mark}</g>'
    body += f'<g transform="translate(118,10)">{wm}</g>'
    body += (f'<text x="120" y="110" font-family="Manrope, Helvetica Neue, Arial, sans-serif" font-size="15.5" '
             f'font-weight="600" letter-spacing="0.4" fill="{p["ink"]}">IEEE International Conference on Program Comprehension</text>')
    return svg(body, 118 + 470, 122)

snips = {}
for key, (letter, name, fn, blurb) in OPTIONS.items():
    snips[key] = {"letter": letter, "name": name, "blurb": blurb}
    for theme, p in PAL.items():
        m = fn(p)
        with open(os.path.join(OUT, f"{letter}-{key}-mark-{theme}.svg"), "w") as f:
            f.write(svg(m, 100, 100))
        with open(os.path.join(OUT, f"{letter}-{key}-lockup-{theme}.svg"), "w") as f:
            f.write(lockup(key, p))
        snips[key][f"mark_{theme}"] = m
        snips[key][f"lockup_{theme}"] = lockup(key, p)
# shared wordmarks for the gallery
for theme, p in PAL.items():
    wm, w, h = wordmark_upper(p['brand'])
    snips[f"wordmark_{theme}"] = svg(wm, w, h)
with open(os.path.join(OUT, "snippets.json"), "w") as f:
    json.dump(snips, f, indent=1)
print("wrote", len(os.listdir(OUT)), "files to", OUT)
