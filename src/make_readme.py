"""writes ../README.md. light github gets the blue field, dark github gets the green."""
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


def card(slug, alt, href=None):
    return pic(f"card-{slug}", alt, width="100%", phone=True, href=href)


def table(rows):
    out = ["| what | with what | the twist |", "| --- | --- | --- |"]
    for i, (name, link, tag, what, stack, twist) in enumerate(rows, 1):
        n = f"**[{name}]({link})**" if link else f"**{name}**"
        if tag:
            n += f" `{tag}`"
        out.append(f"| {n}<br>{what} | {stack} | *{twist}* |")
    return "\n".join(out)


PILLS = [
    ("hire", "email me", "mailto:shreeviraj5387@gmail.com"),
    ("site", "shreeviraj.studio", "https://shreeviraj.studio"),
    ("x", "x", "https://x.com/shreeviraj_dev"),
    ("linkedin", "linkedin", "https://linkedin.com/in/shreeviraj"),
    ("instagram", "instagram", "https://instagram.com/1cr.sri"),
]

AGENTS = [
    ("ABTalks agent", f"{GH}/abtalkshackathon", None,
     "finds ai/ml topics, judges them against a persona, writes and posts",
     "python · fastapi · flora",
     "ran 48 hours unattended. nobody touched it"),
    ("Excel Bot", f"{GH}/Excel-bot", None,
     "telegram bot. send any messy spreadsheet, get an excel dashboard and a deck back",
     "python · claude files api · code execution",
     "claude is the analyst. nobody tells it which columns matter"),
    ("edi-5", None, "private",
     "multi domain rag assistant. started on cricket, now does finance and general knowledge too",
     "fastapi · groq · chroma · react",
     "it routes before it retrieves. live, historical and analytical questions each get their own path"),
    ("requirements agent", None, "private",
     "turns gmail threads and meet transcripts into a requirements doc",
     "langgraph · gemini 2.5 flash · supabase pgvector",
     "the meeting ends, the spec is already written"),
]
FINANCE = [
    ("SAR-mvp", f"{GH}/SAR-mvp", None,
     "anti money laundering: writes the suspicious activity report for an analyst",
     "langgraph · fastapi · pgvector · ollama",
     "seven agents and a local mistral. nothing leaves the machine"),
    ("ESG greenwashing agent", "https://github.com/Pragati-1-7/Automated_ESG_Greenwashing_agent", "collab",
     "with pragati. reads a sustainability report and checks every claim against filings, regulators and news",
     "python · agents · layout aware pdf parsing",
     "every claim ends as align, contradict or insufficient, with an audit trail and a 0 to 100 risk score"),
    ("ml-challenge", None, "private",
     "amazon ml challenge 2026. business entity resolution across three sources, three countries",
     "python · blocking · pruner + matcher",
     "0.972 on local validation, 0.885 on the leaderboard. hunting the gap"),
]
CIVIC = [
    ("drone swarm", "https://github.com/tusharsingh-spring/drone_swarm", "collab",
     "with tushar. a flood and fire response simulator for pune and pcmc",
     "python · websockets · 3d map",
     "up to 100 modelled drones working alongside real pcmc ground units"),
    ("PS-CRM", f"{GH}/pscrm", None,
     "civic grievance crm for delhi mcd, built as team blackhaze",
     "fastapi · next.js · langgraph · gemini · postgis",
     "every complaint is a point on a map, and an agent decides where it goes"),
    ("CLINDerm", f"{GH}/clinderm", None,
     "three face photos in, an annotated skin health report out",
     "yunet · mediapipe · segformer · yolov8",
     "four vision models, all running locally on a laptop 4050"),
    ("threat forecasting", f"{GH}/cybersec-ind", None,
     "forecasts cyber threats and the tech that counters them",
     "python · bayesian gnn · nvd · gdelt",
     "a 2025 paper rebuilt end to end, with honest fallbacks when the apis say no"),
]
LEARN = [
    ("Avinya", f"{GH}/avinya", None,
     "personalised video learning with a hybrid recommender",
     "react · fastapi · supabase · lightfm",
     "three recommenders blended: content, collaborative and knowledge based"),
    ("algo visualiser", f"{GH}/edai-3-f1", None,
     "algorithm visualiser with an ai tutor that watches how you learn",
     "react · go · python · gemini",
     "pause too long and it slows down. hit replay and it gets technical"),
    ("Better VOLP", None, "private",
     "a cleaner client for my college's classroom platform",
     "next.js · prisma · cron",
     "emails you 48 hours before an assignment is due. the original never did"),
]

md = f"""{pic("hero", "Shreeviraj Matale. creative director who codes.", width="100%", href="https://shreeviraj.studio", phone=True)}

{" ".join(pic("pill-" + n, a, height="38", href=h) for n, a, h in PILLS)}

<br>

{band("hey", "Hey. the short version.")}

i'm **sree**. i build agents, memory systems and audit pipelines. mostly for hackathons, sometimes for clients, occasionally because something annoyed me. i also art direct, which is why this page looks the way it does.

EY techathon semi-finalist · top 10 at india innovates · three hackathon wins · judged cybersecurity at fusion 2k26 · 451 contributions last year, a third of them private

**currently** building antAi for smart india hackathon 2026, which catches voice clone scams before the money moves. open to freelance: agents, pipelines, automation.

python and typescript mostly. go and kotlin when the problem asks for it.

> keep the ai part invisible so the work gets judged as work.

<br>

{band("worth-opening", "Worth opening. if you open three things, open these.")}

{card("covenant", "COVENANT. audit grade covenant compliance testing for private credit.", f"{GH}/COVENANT")}

<sub>the research and golden test set behind it: [ey-research]({GH}/ey-research)</sub>

{card("memoryos", "MemoryOS. open memory middleware for llm apps.", f"{GH}/memos")}

<sub>and a local first dashboard for it: [memos-v2]({GH}/memos-v2)</sub>

{card("jqp", "jqp. instagram publishing and comment to dm automation on official meta apis. private.")}

<br>

{band("everything-else", "Everything else. by domain.")}

### agents & retrieval
*things that decide, route, and keep running when i log off.*

{table(AGENTS)}

### finance & compliance
*where a rounding error is a wrong answer.*

{table(FINANCE)}

### civic, health & security
*maps, faces and threat graphs.*

{table(CIVIC)}

### learning & small fixes
*software that teaches back, and one that fixes college.*

{table(LEARN)}

<sub>`private` means named, not linked. ask and i'll walk you through it. `collab` means a team repo i build in.</sub>

<br>

{pic("footer", "Say hello. shreeviraj5387@gmail.com", width="100%", href="mailto:shreeviraj5387@gmail.com", phone=True)}
"""

with open(os.path.join(os.path.dirname(HERE), "README.md"), "w", encoding="utf-8") as f:
    f.write(md)
print("README.md", len(md), "chars")
