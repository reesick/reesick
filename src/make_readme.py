"""writes README.md. light github gets the blue field, dark github gets the green."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
GH = "https://github.com/reesick"


PHONE = "(max-width: 600px)"


def pic(name, alt, width=None, height=None, href=None, phone=False):
    size = (f' width="{width}"' if width else "") + (f' height="{height}"' if height else "")
    m = ""
    if phone:  # a re-set cut for narrow screens, so the type never drops below readable
        m = (f'<source media="(prefers-color-scheme: dark) and {PHONE}" srcset="assets/{name}-m-green.svg">'
             f'<source media="{PHONE}" srcset="assets/{name}-m-blue.svg">')
    p = (f'<picture>{m}<source media="(prefers-color-scheme: dark)" srcset="assets/{name}-green.svg">'
         f'<img src="assets/{name}-blue.svg" alt="{alt}"{size}></picture>')
    return f'<a href="{href}">{p}</a>' if href else p


def band(slug, alt):
    return pic(f"sec-{slug}", alt, width="100%", phone=True)


def table(rows):
    out = ["|    | what | with what | the twist |", "| --- | --- | --- | --- |"]
    for i, (name, link, what, stack, twist) in enumerate(rows, 1):
        n = f"**[{name}]({link})**" if link else f"**{name}**"
        out.append(f"| `{i:02d}` | {n}<br>{what} | {stack} | *{twist}* |")
    return "\n".join(out)


def skill(ids, alt):
    a = f"https://skillicons.dev/icons?i={ids}&perline=12"
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{a}&theme=dark">'
            f'<img src="{a}&theme=light" alt="{alt}" height="44"></picture>')


def stats():
    # drawn by src/statscard.py, refreshed daily by the workflow
    return pic("numbers", "contribution numbers for reesick", width="100%", phone=True)


PILLS = [
    ("hire", "hire me", "mailto:shreeviraj5387@gmail.com"),
    ("site", "shreeviraj.studio", "https://shreeviraj.studio"),
    ("studio", "jacquard studio", "https://jacquard.shreeviraj.studio"),
    ("x", "x", "https://x.com/shreeviraj_dev"),
    ("linkedin", "linkedin", "https://linkedin.com/in/shreeviraj"),
    ("instagram", "instagram", "https://instagram.com/1cr.sri"),
]

AGENTS = [
    ("MemoryOS", f"{GH}/memos", "open memory middleware for any llm app",
     "python · knowledge graph · hybrid retrieval",
     "not plain rag. it extracts facts, settles conflicts and recalls across three stores at once"),
    ("memos v2", f"{GH}/memos-v2", "local first memory workspace with a dashboard to browse it",
     "typescript · next.js · sqlite",
     "runs on synthetic embeddings, so you can try it without a single api key"),
    ("ABTalks agent", f"{GH}/abtalkshackathon", "finds topics, judges them against a persona, writes and posts",
     "python · fastapi · flora",
     "left alone for 48 hours. nobody touched it"),
    ("Excel Bot", f"{GH}/Excel-bot", "telegram bot. send any messy file, get an excel dashboard and a deck back",
     "python · claude code execution · telegram",
     "claude is the analyst. no picking columns, no questions asked"),
]
AUDIT = [
    ("COVENANT", f"{GH}/COVENANT", "audit grade covenant compliance testing for private credit",
     "python · sympy · faiss · pdfplumber",
     "zero floats. exact rational maths, and every run is hash chained and timestamped"),
    ("ey research", f"{GH}/ey-research", "the research and golden test set behind it, built for the EY techathon",
     "sec edgar · xbrl · python",
     "two fake borrowers with planted errors. one of them is quietly in breach"),
]
CIVIC = [
    ("PS-CRM", f"{GH}/pscrm", "smart public service crm for delhi mcd grievances",
     "fastapi · langgraph · gemini · postgis · maplibre",
     "every complaint is a point on a map, and an agent decides where it goes"),
    ("CLINDerm", f"{GH}/clinderm", "ai facial skin health screening",
     "yunet · mediapipe · segformer · yolov8",
     "four vision models chained into one screening pass"),
    ("threat forecasting", f"{GH}/cybersec-ind", "forecasts cyber threats and the tech that counters them",
     "python · bayesian gnn · nvd · gdelt",
     "a 2025 paper rebuilt end to end, with synthetic fallbacks for when the apis say no"),
]
LEARN = [
    ("Avinya", f"{GH}/avinya", "personalised video learning with a hybrid recommender",
     "react · fastapi · supabase · lightfm",
     "three recommenders blended: content, collaborative and knowledge based"),
    ("algo visualiser", f"{GH}/edai-3-f1", "algorithm visualiser with an ai tutor that watches how you learn",
     "react · go · python · gemini",
     "pause too long and it slows down. hit replay and it gets technical"),
]
STUDIO = [
    ("JaCquard Studio", "https://jacquard.shreeviraj.studio", "ai led visual production for fashion, lifestyle and ecommerce brands",
     "image + video models · custom pipelines",
     "the ai part stays invisible, so the work gets judged as work"),
    ("HyperFuel", None, "streetwear label with an ai campaign pipeline behind every drop",
     "nano banana pro · higgsfield",
     "a full lookbook, no shoot day"),
]

md = f"""{pic("hero", "Shreeviraj Matale. creative director who codes.", width="100%", href="https://shreeviraj.studio", phone=True)}

{" ".join(pic("pill-" + n, a, height="38", href=h) for n, a, h in PILLS)}

<br>

{band("hey", "Hey. the short version.")}

i'm **sree**. half of me runs [jacquard studio](https://jacquard.shreeviraj.studio), an ai led visual studio for fashion and ecommerce brands. the other half writes agents, memory systems and audit pipelines. usually for a hackathon, sometimes for a client, occasionally just to see if it works.

b.tech cse (ai/ml) at [vit pune](https://www.vit.edu). EY techathon semi-finalist. top 10 at india innovates.

> keep the ai part invisible so the work gets judged as work.

> ship something a hundred thousand people use.

<br>

{band("things-ive-built", "Things i've built. the ones worth opening.")}

### agents & memory
*things that remember, decide, and keep running when i log off.*

{table(AGENTS)}

### audit & finance
*where a rounding error is a bug, not a detail.*

{table(AUDIT)}

### civic, health, security
*maps, faces and threat graphs.*

{table(CIVIC)}

### learning
*software that teaches back.*

{table(LEARN)}

### studio
*not on github, but it's where the code goes to work.*

{table(STUDIO)}

<br>

{band("right-now", "Right now. what's on the desk this month.")}

- **antAi** for smart india hackathon 2026. fuses voice, video, text and intent into one 0 to 100 risk score to catch voice clone scams. *then it logs, verifies, or freezes.*
- **jacquard studio**, taking on fashion and ecommerce brands. *dms are open.*
- **hyperfuel**, the next drop and its campaign. *still no shoot day.*
- judged the cybersecurity track at **fusion 2k26**. *turns out judging is harder than pitching.*

<br>

{band("stack", "Stack. what the work gets built with.")}

**languages**<br>
{skill("python,ts,js,cpp,kotlin,go,html,css", "python, typescript, javascript, c++, kotlin, go, html, css")}

**web & backend**<br>
{skill("react,nextjs,nodejs,fastapi,tailwind,supabase,postgres,sqlite", "react, next.js, node, fastapi, tailwind, supabase, postgres, sqlite")}

**ai & ml**<br>
{skill("pytorch,tensorflow,opencv,sklearn", "pytorch, tensorflow, opencv, scikit-learn")}

**tools**<br>
{skill("git,github,docker,vercel,vscode,postman", "git, github, docker, vercel, vs code, postman")}

<br>

**i also**

```
art direct campaigns
prompt until it looks shot
judge hackathons · ship at 2am
chronically online
```

*the commit graph has a sleep schedule. i don't.*

<br>

{band("numbers", "Numbers. the graph doesn't lie, it just rounds up.")}

{stats()}

<br>

{pic("footer", "Say hello. shreeviraj5387@gmail.com", width="100%", href="mailto:shreeviraj5387@gmail.com", phone=True)}
"""

with open(os.path.join(os.path.dirname(HERE), "README.md"), "w", encoding="utf-8") as f:
    f.write(md)
print("README.md", len(md), "chars")
