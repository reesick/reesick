"""
the numbers card. runs daily from .github/workflows/numbers.yml.

pulls the last year of public contributions through github's graphql api
(GITHUB_TOKEN is enough), then draws them on the same field as everything
else. no third party stat service, so nothing goes down and nothing looks
borrowed. without a token it draws from seed.json instead.
"""
import datetime as dt
import json, os, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import THEMES, Doc, field, svg, save, width, W, PAD, WM, PM  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LOGIN = os.environ.get("GH_LOGIN", "reesick")

Q = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{date contributionCount}}}}}}"""


def fetch():
    tok = os.environ.get("GITHUB_TOKEN")
    if not tok or os.environ.get("NUMBERS_OFFLINE"):
        with open(os.path.join(HERE, "seed.json")) as f:
            return json.load(f)
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": Q, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {tok}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        cal = json.load(r)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    days = [[d["date"], d["contributionCount"]] for w in cal["weeks"] for d in w["contributionDays"]]
    data = {"login": LOGIN, "total": cal["totalContributions"], "days": days}
    with open(os.path.join(HERE, "seed.json"), "w") as f:
        json.dump(data, f)
    return data


def streaks(days):
    counts = [c for _, c in days]
    best = run = 0
    for c in counts:
        run = run + 1 if c else 0
        best = max(best, run)
    # today still counts as alive until it ends, so start from yesterday if today is empty
    i = len(counts) - 1
    if counts and counts[i] == 0:
        i -= 1
    cur = 0
    while i >= 0 and counts[i]:
        cur += 1
        i -= 1
    return cur, best


def busiest(days):
    return max(days, key=lambda d: d[1])


def fmt(date):
    d = dt.date.fromisoformat(date)
    return f"{d.day} {d.strftime('%b').lower()} {d.year}"


def levels(days):
    """github's own quartiles, roughly: 0, then four steps up to the max"""
    mx = max((c for _, c in days), default=0) or 1
    return lambda c: 0 if c == 0 else min(4, 1 + int(3.999 * c / mx))


def card(tn, th, data, phone=False):
    days = data["days"]
    cur, best = streaks(days)
    top = busiest(days)
    lv = levels(days)
    Wd, P = (WM, PM) if phone else (W, PAD)
    weeks_shown = 26 if phone else 53
    doc = Doc()
    H = 352 if phone else 326
    defs, bg, css = field(Wd, H, th, oy=.36, uid="n", vh=Wd * (1.25 if phone else .5625))
    b = [bg]

    # three figures, serif italic in the accent, the only place a number gets colour
    figs = [(f"{data['total']}", "contributions", "last 12 months"),
            (f"{cur}", "day streak", "right now"),
            (f"{best}", "longest streak", "this year")]
    col = (Wd - 2 * P) / 3
    fs, ls = (40, 11.5) if phone else (60, 13)
    fy = 86 if phone else 104
    for i, (n, l1, l2) in enumerate(figs):
        x = P + i * col
        b.append(f'<g filter="url(#sh)">' + doc.text(x, fy, fs, [doc.run(n, "si")], th["accent"], extra=' class="num"') + '</g>')
        if phone:
            b.append(doc.text(x, fy + 24, ls, [doc.run(l1, "t")], th["ink2"]))
            b.append(doc.text(x, fy + 40, ls, [doc.run(l2, "t")], th["ink3"]))
        else:
            b.append(doc.text(x, fy + 28, ls, [doc.run(l1 + ", ", "t", th["ink2"]), doc.run(l2, "t")], th["ink3"], extra=' letter-spacing=".15"'))

    # the year, as a grid of cells
    gy = 168 if phone else 166
    gw = Wd - 2 * P
    step = gw / weeks_shown
    cell = step * .78
    first = dt.date.fromisoformat(days[0][0])
    # align to github's grid: columns are weeks starting sunday
    start_col = (first.weekday() + 1) % 7
    grid = []
    for idx, (date, c) in enumerate(days):
        k = idx + start_col
        wk, dow = divmod(k, 7)
        grid.append((wk, dow, c, date))
    last_wk = grid[-1][0]
    op = [.09, .32, .55, .78, 1]
    for wk, dow, c, date in grid:
        rel = wk - (last_wk - weeks_shown + 1)
        if rel < 0:
            continue
        x = P + rel * step
        y = gy + dow * step
        fill = th["accent"] if date == top[0] and c else th["ink"]
        o = 1 if fill == th["accent"] else op[lv(c)]
        b.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell:.1f}" height="{cell:.1f}" rx="{cell * .22:.1f}" fill="{fill}" fill-opacity="{o}"/>')
    gb = gy + 7 * step

    # legend + a dry note
    ly = gb + (26 if phone else 30)
    note = f"busiest day was {fmt(top[0])}, {top[1]} contributions deep."
    if phone:
        b.append(doc.text(P, ly, 11.5, [doc.run("last 6 months", "t")], th["ink3"]))
        b.append(doc.text(P, ly + 26, 15, [doc.run(note, "si")], th["ink2"]))
        b.append(doc.text(Wd - P, ly, 11.5, [doc.run(f"as of {fmt(days[-1][0])}", "t")], th["ink3"], anchor="end"))
    else:
        b.append(doc.text(P, ly, 17, [doc.run(note, "si")], th["ink2"]))
        b.append(doc.text(Wd - P, ly, 12.5, [doc.run(f"as of {fmt(days[-1][0])}", "t")], th["ink3"], anchor="end", extra=' letter-spacing=".15"'))
    title = f"{data['total']} contributions in the last year, {cur} day streak, longest {best}."
    save(f"numbers{'-m' if phone else ''}-{tn}.svg", svg(Wd, H, defs, "".join(b), css, doc, title))


if __name__ == "__main__":
    data = fetch()
    for tn, th in THEMES.items():
        card(tn, th, data)
        card(tn, th, data, phone=True)
