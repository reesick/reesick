"""
builds every svg the profile readme uses.

same rules as the site: serif is landmark, sans is content, one accent,
and the field is code, not an image. fonts are the site's own woff2 files,
subset per svg to just the glyphs it uses and inlined, so nothing loads
from anywhere and github's image proxy can't break it.

python build.py  ->  assets/*.svg  (a blue and a green of each)
"""
import base64, io, math, os, html
from fontTools.ttLib import TTFont
from fontTools import subset

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets")
os.makedirs(OUT, exist_ok=True)

FONTS = {
    "s":  ("Instrument Serif", "normal", 400, "fonts/instrument-serif-400.woff2"),
    "si": ("Instrument Serif", "italic", 400, "fonts/instrument-serif-400-italic.woff2"),
    "t":  ("Inter", "normal", 400, "fonts/inter-400.woff2"),
    "m":  ("Inter", "normal", 500, "fonts/inter-500.woff2"),
}
_tt = {k: TTFont(os.path.join(HERE, v[3])) for k, v in FONTS.items()}


def width(text, f, size, tracking=0.0):
    t = _tt[f]
    cmap, hmtx, upm = t.getBestCmap(), t["hmtx"], t["head"].unitsPerEm
    w = 0
    for ch in text:
        g = cmap.get(ord(ch))
        w += hmtx[g][0] if g else upm * 0.5
    return w / upm * size + tracking * size * len(text)


def font_css(used):
    out = []
    for k, chars in used.items():
        if not chars:
            continue
        fam, style, wt, path = FONTS[k]
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["kern", "liga", "calt", "tnum"]
        opts.notdef_outline = True
        f = TTFont(os.path.join(HERE, path))
        s = subset.Subsetter(opts)
        s.populate(text="".join(sorted(set(chars))) + " ")
        s.subset(f)
        buf = io.BytesIO()
        f.flavor = "woff2"
        f.save(buf)
        b64 = base64.b64encode(buf.getvalue()).decode()
        out.append(
            f'@font-face{{font-family:"{fam} {k}";font-style:{style};font-weight:{wt};'
            f'src:url(data:font/woff2;base64,{b64}) format("woff2")}}'
            f'.{k}{{font-family:"{fam} {k}","{fam}",{"Georgia,serif" if fam.startswith("Instrument") else "-apple-system,Segoe UI,Helvetica,Arial,sans-serif"};'
            f'font-style:{style};font-weight:{wt}}}'
        )
    return "".join(out)


# ---------- tokens, lifted straight from field.css ----------
THEMES = {
    "blue": dict(
        sweep=["#1A5AFC", "#0C39FB", "#0826F4", "#0519CE", "#030F8E"],
        sweep_at=[0, .30, .58, .82, 1],
        core=[("#DCFEFF", 1), ("#AEF4FE", .9), ("#72D9FD", .6), ("#3CB0FB", .28), ("#1E7CFA", .07), ("#145AFA", 0)],
        streak=[("#9EEBFE", .32), ("#7AD8FD", .20), ("#64CCFD", .15), ("#5CC6FC", .12)],
        dark=[
            ((1.06, 1.16), (.58, .62), [(0, "#010208", .92), (.16, "#020516", .82), (.32, "#030930", .64), (.48, "#040E58", .42), (.66, "#05148C", .2), (.84, "#0826E1", 0)]),
            ((1.04, .62), (.26, .58), [(0, "#020858", .34), (.46, "#030E8C", .14), (.78, "#041ACD", 0)]),
            ((.02, 1.0), (.52, .34), [(0, "#030E82", .2), (.52, "#0416B4", .06), (.82, "#051EDC", 0)]),
        ],
        grain=.92,
        ink="#FFFFFF", ink2="rgba(255,255,255,.82)", ink3="rgba(255,255,255,.60)",
        rule="rgba(255,255,255,.26)", accent="#FFE066", link="#BFE3FF", btn_on="#0A2FF8",
    ),
    "green": dict(
        sweep=["#0E8F62", "#076744", "#04432D", "#02291B", "#01140D"],
        sweep_at=[0, .32, .60, .84, 1],
        core=[("#E9FFF5", 1), ("#B2FCD8", .78), ("#6CF0B4", .46), ("#34CE8C", .2), ("#18A068", .05), ("#108254", 0)],
        streak=[("#B0FCD9", .2), ("#80F4C0", .13), ("#64EAB0", .1), ("#58E2A8", .08)],
        dark=[
            ((1.06, 1.16), (.58, .62), [(0, "#000302", .9), (.18, "#000805", .78), (.36, "#01120C", .56), (.58, "#012015", .3), (.82, "#023C27", 0)]),
            ((.22, .04), (1.2, 1.0), [(0, "#085036", .2), (.5, "#032619", .1), (.82, "#01100B", 0)]),
        ],
        grain=.7,
        ink="#EEFBF4", ink2="rgba(238,251,244,.80)", ink3="rgba(238,251,244,.56)",
        rule="rgba(238,251,244,.22)", accent="#FFD166", link="#BFF3DA", btn_on="#04613E",
    ),
}

EASE = "cubic-bezier(.45,0,.55,1)"


def field(W, H, th, oy=0.0, uid="f", radius=16, drift=True, vh=None, light=True):
    """the four layers of .bg, as svg. oy picks which slice of a 16:9 field
    this panel shows, so the bands down the page don't all look identical."""
    VH = vh or W * 0.5625
    y0 = -oy * VH
    # 1. sweep, css 202deg
    a = math.radians(202)
    dx, dy = math.sin(a), -math.cos(a)
    L = abs(W * dx) + abs(VH * dy)
    cx, cy = W / 2, VH / 2 + y0
    sx1, sy1, sx2, sy2 = cx - dx * L / 2, cy - dy * L / 2, cx + dx * L / 2, cy + dy * L / 2
    stops = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in zip(th["sweep_at"], th["sweep"]))
    d = [f'<linearGradient id="{uid}sw" gradientUnits="userSpaceOnUse" x1="{sx1:.1f}" y1="{sy1:.1f}" x2="{sx2:.1f}" y2="{sy2:.1f}">{stops}</linearGradient>']
    # 2. light: the core, on a plane turned -34deg (vmax = W)
    lx, ly = W / 2 + .0172 * W, VH / 2 - .532 * W + y0
    rx, ry = 1.008 * W, .552 * W
    cs = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o, (c, op) in zip([0, .15, .33, .53, .73, .88], th["core"]))
    d.append(f'<radialGradient id="{uid}co" gradientUnits="userSpaceOnUse" cx="0" cy="0" r="1" gradientTransform="translate({lx:.1f} {ly:.1f}) rotate(-34) scale({rx:.1f} {ry:.1f})">{cs}</radialGradient>')
    # the streaks that run with it
    ca, sa = math.cos(math.radians(-34)), math.sin(math.radians(-34))
    hp = 1.2 * W
    p1 = (W / 2 - (-hp) * sa, VH / 2 + (-hp) * ca + y0)
    p2 = (W / 2 - (hp) * sa, VH / 2 + (hp) * ca + y0)
    s0 = th["streak"][0][0]
    pattern = [(.14, None), (.215, 0), (.29, None), (.34, None), (.405, 1), (.47, None), (.54, None), (.60, 2), (.66, None), (.72, None), (.775, 3), (.84, None)]
    ss = ""
    for o, i in pattern:
        if i is None:
            ss += f'<stop offset="{o}" stop-color="{s0}" stop-opacity="0"/>'
        else:
            c, op = th["streak"][i]
            ss += f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>'
    d.append(f'<linearGradient id="{uid}st" gradientUnits="userSpaceOnUse" x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}">{ss}</linearGradient>')
    # 3. the dark corner
    darks = []
    for i, ((fx, fy), (frx, fry), st) in enumerate(th["dark"]):
        s = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o, c, op in st)
        d.append(f'<radialGradient id="{uid}d{i}" gradientUnits="userSpaceOnUse" cx="0" cy="0" r="1" gradientTransform="translate({fx * W:.1f} {fy * VH + y0:.1f}) scale({frx * W:.1f} {fry * VH:.1f})">{s}</radialGradient>')
        darks.append(f'<rect x="-40" y="-40" width="{W + 80}" height="{H + 80}" fill="url(#{uid}d{i})"/>')
    # 4. grain
    d.append(f'<filter id="{uid}gr" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".62" numOctaves="3" stitchTiles="stitch"/></filter>')
    d.append(f'<clipPath id="{uid}cl"><rect width="{W}" height="{H}" rx="{radius}"/></clipPath>')
    body = (
        f'<g clip-path="url(#{uid}cl)">'
        f'<rect width="{W}" height="{H}" fill="url(#{uid}sw)"/>'
        + (f'<g class="{"drift" if drift else ""}"><rect x="-80" y="-80" width="{W + 160}" height="{H + 160}" fill="url(#{uid}co)"/>'
           f'<rect x="-80" y="-80" width="{W + 160}" height="{H + 160}" fill="url(#{uid}st)"/></g>' if light else "")
        + ("".join(darks) if light else "") +
        f'<rect width="{W}" height="{H}" filter="url(#{uid}gr)" opacity="{th["grain"]}" style="mix-blend-mode:overlay"/>'
        f'</g>'
    )
    css = (
        "@keyframes drift{0%{transform:translate(-1.4%,-1%) scale(1.02)}50%{transform:translate(1.2%,1.6%) scale(1.05)}100%{transform:translate(-.6%,2.2%) scale(1.02)}}"
        f".drift{{transform-origin:50% 0;animation:drift 46s {EASE} infinite alternate}}"
        "@media (prefers-reduced-motion:reduce){.drift{animation:none}}"
    )
    return "".join(d), body, css


class Doc:
    def __init__(self):
        self.used = {k: set() for k in FONTS}

    def run(self, text, f="t", fill=None, extra=""):
        self.used[f].update(text)
        fl = f' fill="{fill}"' if fill else ""
        return f'<tspan class="{f}"{fl}{extra}>{html.escape(text)}</tspan>'

    def text(self, x, y, size, runs, fill, anchor="start", extra=""):
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}"{a}{extra}>{"".join(runs)}</text>'


def arrow(x, y, s, color, sw=1.3):
    """the site's ne arrow, drawn, because neither face has the glyph"""
    return (f'<path d="M{x:.1f} {y + s:.1f} L{x + s:.1f} {y:.1f} M{x + s * .3:.1f} {y:.1f} L{x + s:.1f} {y:.1f} L{x + s:.1f} {y + s * .7:.1f}" '
            f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')


def svg(W, H, defs, body, css, doc, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{html.escape(title)}">'
        f'<title>{html.escape(title)}</title>'
        f'<defs>{defs}<filter id="sh" x="-20%" y="-50%" width="140%" height="200%"><feDropShadow dx="0" dy="1" stdDeviation="16" flood-color="#000A28" flood-opacity=".34"/></filter></defs>'
        f'<style>{font_css(doc.used)}{css}text{{font-kerning:normal;font-feature-settings:"kern","liga","calt"}}.num{{font-feature-settings:"tnum" 1}}</style>'
        f'{body}</svg>'
    )


def save(name, s):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(s)
    print(f"{name:28s} {len(s) / 1024:6.1f} KB")


# ---------------------------------------------------------------------------
W = 880
PAD = 52


def hero(tn, th):
    H = 468
    doc = Doc()
    defs, bg, css = field(W, H, th, oy=0, uid="h")
    hi = lambda s: doc.run(s, "si", th["accent"], ' font-size="1.16em"')
    t = lambda s, c=None: doc.run(s, "t", c)
    b = [bg]
    # masthead
    b.append(f'<g filter="url(#sh)">' + doc.text(PAD, 150, 86, [doc.run("Shreeviraj ", "s"), doc.run("Matale", "si")], th["ink"], extra=' letter-spacing="-1.5"') + '</g>')
    # place line, with the 3px dot
    place = "(Pune/+5:30GMT)"
    pw = width(place, "t", 13.5, .015)
    b.append(doc.text(PAD, 190, 13.5, [t(place)], th["ink3"], extra=' letter-spacing=".2"'))
    b.append(f'<circle cx="{PAD + pw + 11:.1f}" cy="185.5" r="1.6" fill="{th["ink3"]}"/>')
    b.append(doc.text(PAD + pw + 22, 190, 13.5, [t("github/reesick")], th["ink3"], extra=' letter-spacing=".2"'))
    # lede
    b.append(doc.text(PAD, 254, 21, [t("creative director who codes. i build "), hi("agents"), t(", "), hi("pipelines")], th["ink2"]))
    b.append(doc.text(PAD, 290, 21, [t("and the occasional app that actually "), hi("ships"), t(".")], th["ink2"]))
    b.append(doc.text(PAD, 332, 21, [t("b.tech cse (ai/ml) at vit pune. founder of jacquard studio.")], th["ink3"]))
    # toolbar rule
    b.append(f'<line x1="{PAD}" y1="368.5" x2="{W - PAD}" y2="368.5" stroke="{th["rule"]}" stroke-width="1"/>')
    # right now, cycling
    b.append(doc.text(PAD, 414, 13.5, [t("right now")], th["ink3"], extra=' letter-spacing=".2"'))
    lines = [
        "building antAi for smart india hackathon 2026",
        "running jacquard studio, ai visuals for fashion brands",
        "dropping hyperfuel with an ai campaign pipeline",
        "taking on freelance: brand visuals, products, or both",
    ]
    n, per = len(lines), 4.5
    dur = n * per
    k = 100 / n
    css += (f"@keyframes cyc{{0%{{opacity:0;transform:translateY(8px)}}{k * .12:.2f}%{{opacity:1;transform:none}}"
            f"{k * .86:.2f}%{{opacity:1;transform:none}}{k:.2f}%{{opacity:0;transform:translateY(-6px)}}100%{{opacity:0}}}}"
            f".cy{{opacity:0;animation:cyc {dur}s cubic-bezier(.22,1,.36,1) infinite}}"
            "@media (prefers-reduced-motion:reduce){.cy{animation:none}.cy0{opacity:1}}")
    for i, ln in enumerate(lines):
        b.append(f'<g class="cy cy{i}" style="animation-delay:{i * per}s">' +
                 doc.text(PAD + 98, 415, 23, [doc.run(ln, "si")], th["accent"]) + '</g>')
    # site, top right
    site = "shreeviraj.studio"
    sw = width(site, "t", 13.5, .015)
    b.append(doc.text(W - PAD - 14, 58, 13.5, [t(site)], th["ink2"], anchor="end", extra=' letter-spacing=".2"'))
    b.append(arrow(W - PAD - 8, 49, 7, th["ink2"]))
    b.append(f'<line x1="{W - PAD - 14 - sw:.1f}" y1="63" x2="{W - PAD - 14:.1f}" y2="63" stroke="{th["rule"]}"/>')
    save(f"hero-{tn}.svg", svg(W, H, defs, "".join(b), css, doc, "Shreeviraj Matale. creative director who codes. agents, pipelines, and apps that ship."))


def band(tn, th, idx, total, title, note, oy):
    H = 132
    doc = Doc()
    uid = f"b{idx}"
    defs, bg, css = field(W, H, th, oy=oy, uid=uid, radius=14)
    b = [bg]
    b.append(f'<g filter="url(#sh)">' + doc.text(PAD - 8, 76, 48, [doc.run(title, "s")], th["ink"], extra=' letter-spacing="-.6"') + '</g>')
    b.append(doc.text(PAD - 8, 108, 19, [doc.run(note, "si")], th["ink3"]))
    b.append(doc.text(W - PAD + 8, 40, 13, [doc.run(f"{idx:02d}", "m", th["ink2"]), doc.run(f" / {total:02d}", "t")], th["ink3"], anchor="end", extra=' class="num" letter-spacing=".3"'))
    slug = title.lower().replace(" ", "-").replace("'", "").replace("’", "")
    save(f"sec-{slug}-{tn}.svg", svg(W, H, defs, "".join(b), css, doc, f"{title}. {note}"))
    return slug


def footer(tn, th):
    H = 300
    doc = Doc()
    defs, bg, css = field(W, H, th, oy=.42, uid="ft")
    b = [bg]
    b.append(f'<g filter="url(#sh)">' + doc.text(PAD, 96, 52, [doc.run("Say hello", "s")], th["ink"], extra=' letter-spacing="-.7"') + '</g>')
    b.append(doc.text(PAD, 130, 19, [doc.run("a product to build, a brand to shoot, or both.", "si")], th["ink3"]))
    mail = "shreeviraj5387@gmail.com"
    mw = width(mail, "s", 36)
    b.append(doc.text(PAD, 192, 36, [doc.run(mail, "s")], th["ink"]))
    b.append(f'<line x1="{PAD}" y1="200.5" x2="{PAD + mw:.1f}" y2="200.5" stroke="{th["accent"]}" stroke-width="1"/>')
    b.append(f'<line x1="{PAD}" y1="242.5" x2="{W - PAD}" y2="242.5" stroke="{th["rule"]}"/>')
    b.append(doc.text(PAD, 270, 13.5, [doc.run("© ", "t"), doc.run("2026", "t"), doc.run(" Shreeviraj", "t")], th["ink3"], extra=' class="num" letter-spacing=".2"'))
    b.append(doc.text(W - PAD, 270, 13.5, [doc.run("chronically online, mostly on x", "t")], th["ink3"], anchor="end", extra=' letter-spacing=".2"'))
    save(f"footer-{tn}.svg", svg(W, H, defs, "".join(b), css, doc, "Say hello. shreeviraj5387@gmail.com"))


# pills live on github's own page colour, not on the field, so they follow
# github's light and dark rather than the field's blue and green
PILL_THEME = {
    "blue": dict(ink="#1F2328", rule="rgba(31,35,40,.22)", bg="rgba(31,35,40,.03)"),
    "green": dict(ink="#E6EDF3", rule="rgba(230,237,243,.26)", bg="rgba(230,237,243,.04)"),
}


def pill(tn, th, name, label, solid=False, ext=True):
    H, size, padx = 40, 14.5, 18
    doc = Doc()
    tw = width(label, "m", size, .005)
    aw = 13 if ext else 0
    Wp = math.ceil(tw + padx * 2 + aw)
    pt = PILL_THEME[tn]
    if solid:
        defs, bg, css = field(Wp, H, th, oy=0, uid="p", radius=H / 2, vh=H, light=False, drift=False)
        ink = "#FFFFFF" if tn == "blue" else th["ink"]
        b = [bg]
    else:
        defs, css = "", ""
        ink = pt["ink"]
        b = [f'<rect x=".5" y=".5" width="{Wp - 1}" height="{H - 1}" rx="{(H - 1) / 2}" fill="{pt["bg"]}" stroke="{pt["rule"]}"/>']
    b.append(doc.text(padx, 25, size, [doc.run(label, "m")], ink, extra=' letter-spacing=".07"'))
    if ext:
        b.append(arrow(padx + tw + 6, 16.5, 6.5, ink, 1.25))
    save(f"pill-{name}-{tn}.svg", svg(Wp, H, defs, "".join(b), css, doc, label))
    return Wp



# ---------- phone cuts: same panels re-set for a 440 wide column ----------
WM, PM = 440, 26


def fit(parts, limit, label):
    w = sum(width(t, f, sz) for t, f, sz in parts)
    assert w <= limit, f"{label} overflows: {w:.0f} > {limit}"


def hero_m(tn, th):
    H = 548
    doc = Doc()
    defs, bg, css = field(WM, H, th, oy=0, uid="hm", vh=WM * 1.25)
    hi = lambda s: doc.run(s, "si", th["accent"], ' font-size="1.16em"')
    t = lambda s: doc.run(s, "t")
    b = [bg]
    site = "shreeviraj.studio"
    sw = width(site, "t", 12.5)
    b.append(doc.text(PM, 46, 12.5, [t(site)], th["ink2"], extra=' letter-spacing=".2"'))
    b.append(arrow(PM + sw + 7, 37.5, 6.5, th["ink2"]))
    b.append(f'<g filter="url(#sh)">' + doc.text(PM, 128, 66, [doc.run("Shreeviraj", "s")], th["ink"], extra=' letter-spacing="-1.2"')
             + doc.text(PM, 188, 66, [doc.run("Matale", "si")], th["ink"], extra=' letter-spacing="-1.2"') + '</g>')
    fit([("Shreeviraj", "s", 66)], WM - 2 * PM, "name")
    place = "(Pune/+5:30GMT)"
    pw = width(place, "t", 12.5, .015)
    b.append(doc.text(PM, 224, 12.5, [t(place)], th["ink3"], extra=' letter-spacing=".2"'))
    b.append(f'<circle cx="{PM + pw + 10:.1f}" cy="219.8" r="1.5" fill="{th["ink3"]}"/>')
    b.append(doc.text(PM + pw + 20, 224, 12.5, [t("github/reesick")], th["ink3"], extra=' letter-spacing=".2"'))
    L = [(274, [t("creative director who codes.")]),
         (304, [t("i build "), hi("agents"), t(", "), hi("pipelines"), t(" and the")]),
         (334, [t("occasional app that actually "), hi("ships"), t(".")])]
    fit([("i build  and the, ", "t", 18), ("agentspipelines", "si", 20.9)], WM - 2 * PM, "lede2")
    fit([("occasional app that actually .", "t", 18), ("ships", "si", 20.9)], WM - 2 * PM, "lede3")
    for y, r in L:
        b.append(doc.text(PM, y, 18, r, th["ink2"]))
    b.append(doc.text(PM, 374, 16.5, [t("b.tech cse (ai/ml) at vit pune.")], th["ink3"]))
    b.append(doc.text(PM, 399, 16.5, [t("founder of jacquard studio.")], th["ink3"]))
    b.append(f'<line x1="{PM}" y1="430.5" x2="{WM - PM}" y2="430.5" stroke="{th["rule"]}"/>')
    b.append(doc.text(PM, 466, 12.5, [t("right now")], th["ink3"], extra=' letter-spacing=".2"'))
    lines = ["antAi for smart india hackathon 2026", "jacquard studio, ai visuals for fashion",
             "the next hyperfuel drop", "open for freelance work"]
    n, per = len(lines), 4.5
    k = 100 / n
    css += (f"@keyframes cyc{{0%{{opacity:0;transform:translateY(8px)}}{k * .12:.2f}%{{opacity:1;transform:none}}"
            f"{k * .86:.2f}%{{opacity:1;transform:none}}{k:.2f}%{{opacity:0;transform:translateY(-6px)}}100%{{opacity:0}}}}"
            f".cy{{opacity:0;animation:cyc {n * per}s cubic-bezier(.22,1,.36,1) infinite}}"
            "@media (prefers-reduced-motion:reduce){.cy{animation:none}.cy0{opacity:1}}")
    for i, ln in enumerate(lines):
        fit([(ln, "si", 22)], WM - 2 * PM, ln)
        b.append(f'<g class="cy cy{i}" style="animation-delay:{i * per}s">' + doc.text(PM, 500, 22, [doc.run(ln, "si")], th["accent"]) + '</g>')
    save(f"hero-m-{tn}.svg", svg(WM, H, defs, "".join(b), css, doc, "Shreeviraj Matale. creative director who codes."))


def band_m(tn, th, idx, total, title, note, oy, slug):
    H = 116
    doc = Doc()
    uid = f"bm{idx}"
    defs, bg, css = field(WM, H, th, oy=oy, uid=uid, radius=12, vh=WM * 1.25)
    fit([(title, "s", 38)], WM - 2 * PM - 50, title)
    fit([(note, "si", 16)], WM - 2 * PM, note)
    b = [bg,
         f'<g filter="url(#sh)">' + doc.text(PM, 64, 38, [doc.run(title, "s")], th["ink"], extra=' letter-spacing="-.5"') + '</g>',
         doc.text(PM, 92, 16, [doc.run(note, "si")], th["ink3"]),
         doc.text(WM - PM, 34, 12, [doc.run(f"{idx:02d}", "m", th["ink2"]), doc.run(f" / {total:02d}", "t")], th["ink3"], anchor="end", extra=' class="num"')]
    save(f"sec-{slug}-m-{tn}.svg", svg(WM, H, defs, "".join(b), css, doc, f"{title}. {note}"))


def footer_m(tn, th):
    H = 312
    doc = Doc()
    defs, bg, css = field(WM, H, th, oy=.3, uid="fm", vh=WM * 1.25)
    mail = "shreeviraj5387@gmail.com"
    fit([(mail, "s", 30)], WM - 2 * PM, "mail")
    mw = width(mail, "s", 30)
    b = [bg,
         f'<g filter="url(#sh)">' + doc.text(PM, 80, 44, [doc.run("Say hello", "s")], th["ink"], extra=' letter-spacing="-.6"') + '</g>',
         doc.text(PM, 110, 16.5, [doc.run("a product to build, a brand to shoot, or both.", "si")], th["ink3"]),
         doc.text(PM, 172, 30, [doc.run(mail, "s")], th["ink"]),
         f'<line x1="{PM}" y1="179.5" x2="{PM + mw:.1f}" y2="179.5" stroke="{th["accent"]}"/>',
         f'<line x1="{PM}" y1="226.5" x2="{WM - PM}" y2="226.5" stroke="{th["rule"]}"/>',
         doc.text(PM, 256, 12.5, [doc.run("© 2026 Shreeviraj", "t")], th["ink3"], extra=' class="num" letter-spacing=".2"'),
         doc.text(PM, 280, 12.5, [doc.run("chronically online, mostly on x", "t")], th["ink3"], extra=' letter-spacing=".2"')]
    save(f"footer-m-{tn}.svg", svg(WM, H, defs, "".join(b), css, doc, "Say hello. shreeviraj5387@gmail.com"))


SECTIONS = [
    ("Hey", "the short version."),
    ("Things i’ve built", "the ones worth opening. the rest are scratch."),
    ("Right now", "what's on the desk this month."),
    ("Stack", "what the work gets built with."),
    ("Numbers", "the graph doesn't lie, it just rounds up."),
]
PILLS = [
    ("hire", "Hire me", True, False),
    ("site", "site", False, True),
    ("studio", "jacquard studio", False, True),
    ("x", "x", False, True),
    ("linkedin", "linkedin", False, True),
    ("instagram", "instagram", False, True),
]

if __name__ == "__main__":
    widths = {}
    for tn, th in THEMES.items():
        hero(tn, th)
        for i, (t, n) in enumerate(SECTIONS, 1):
            slug = band(tn, th, i, len(SECTIONS), t, n, oy=[.1, .3, .5, .2, .4][i - 1])
            band_m(tn, th, i, len(SECTIONS), t, n, [.1, .3, .5, .2, .4][i - 1], slug)
        hero_m(tn, th)
        footer_m(tn, th)
        footer(tn, th)
        for name, label, solid, ext in PILLS:
            widths[name] = pill(tn, th, name, label, solid, ext)
    print("pill widths", widths)
