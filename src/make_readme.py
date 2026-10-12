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


def skill(ids, alt):
    a = f"https://skillicons.dev/icons?i={ids}&perline=12"
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{a}&theme=dark">'
            f'<img src="{a}&theme=light" alt="{alt}" height="44"></picture>')


PILLS = [
    ("hire", "email me", "mailto:shreeviraj5387@gmail.com"),
    ("site", "shreeviraj.studio", "https://shreeviraj.studio"),
    ("x", "x", "https://x.com/shreeviraj_dev"),
    ("linkedin", "linkedin", "https://linkedin.com/in/shreeviraj"),
    ("instagram", "instagram", "https://instagram.com/1cr.sri"),
]

AGENTS = [
    ("jqp", None, "private",
     "instagram carousel publishing and comment to dm automation, on official meta apis only",
     "typescript · supabase · bullmq · redis",
     "a crash resumable state machine. a publish that dies halfway picks up where it stopped"),
    ("requirements agent", None, "private",
     "turns gmail threads and meet transcripts into a requirements doc",
     "langgraph · gemini · supabase",
     "the meeting ends, the spec is already written"),
    ("Sahayak ops console", f"{GH}/paytmhacks", None,
     "paytm hackathon. an agent that resolves merchant issues, in hindi, over voice",
     "react · vite",
     "it does the work but stops at a human approval gate before touching money"),
    ("ABTalks agent", f"{GH}/abtalkshackathon", None,
     "finds ai/ml topics, judges them against a persona, writes and posts",
     "python · fastapi · flora",
     "ran 48 hours unattended. nobody touched it"),
    ("Excel Bot", f"{GH}/Excel-bot", None,
     "telegram bot. send any messy spreadsheet, get an excel dashboard and a deck back",
     "python · claude files api · code execution",
     "claude is the analyst. nobody tells it which columns matter"),
    ("ClipFarm", None, "private",
     "repost pipeline for clipping programs. reframes, brands, de-dupes and checks a clip before it goes up",
     "python · ffmpeg · flask",
     "fully offline, no accounts, no api keys. it tells you if the post will get approved"),
    ("daily motivator", f"{GH}/motivator", None,
     "telegram bot that writes one thought a day and sends it at 7 am",
     "python · gemini · apscheduler",
     "checks its own history first, so it never says the same thing twice"),
]
MEMORY = [
    ("MemoryOS", f"{GH}/memos", None,
     "open memory middleware for llm apps. put it in front of any chatbot",
     "python · knowledge graph · hybrid retrieval",
     "not plain rag. it extracts facts, settles conflicts and recalls across three stores at once"),
    ("memos v2", f"{GH}/memos-v2", None,
     "local first memory workspace, with a dashboard to browse what it remembers",
     "typescript · next.js · sqlite",
     "runs on synthetic embeddings, so you can try it without a single api key"),
    ("edi-5", None, "private",
     "multi domain rag assistant. started on cricket, now does finance and general knowledge too",
     "fastapi · groq · chroma · react",
     "it routes before it retrieves. live, historical and analytical questions each get their own path"),
]
FINANCE = [
    ("COVENANT", f"{GH}/COVENANT", None,
     f"audit grade covenant compliance testing for private credit. EY techathon semi-finalist. research in [ey-research]({GH}/ey-research)",
     "python · sympy · faiss · pdfplumber",
     "zero floats. exact rational maths, and every run is hash chained and timestamped"),
    ("SAR-mvp", f"{GH}/SAR-mvp", None,
     "anti money laundering. writes the suspicious activity report for an analyst",
     "langgraph · fastapi · pgvector · ollama",
     "seven agents and a local mistral. nothing leaves the machine"),
    ("ESG greenwashing agent", "https://github.com/Pragati-1-7/Automated_ESG_Greenwashing_agent", "collab",
     "reads a sustainability report and checks every claim against filings, regulators and news",
     "python · agents · pdf parsing",
     "every claim ends as align, contradict or insufficient, with an audit trail and a 0 to 100 risk score"),
]
ML = [
    ("ml-challenge", None, "private",
     "amazon ml challenge 2026. business entity resolution across three sources, three countries",
     "python · pruner + matcher · macro f0.5",
     "0.972 on local validation, 0.885 on the leaderboard. hunting the gap"),
    ("face detection, deployed", f"{GH}/nhai", None,
     "scrfd face detection packaged to run anywhere, with a quantisation study",
     "pytorch · onnx runtime · scrfd",
     "quantised it to int8, measured it, shipped fp32 anyway. 30 fps on a plain cpu"),
    ("CLINDerm", f"{GH}/clinderm", None,
     "three face photos in, an annotated skin health report out",
     "yunet · mediapipe · segformer · yolov8",
     "four vision models, all running locally on a laptop 4050"),
    ("threat forecasting", f"{GH}/cybersec-ind", None,
     "forecasts cyber threats and the tech that counters them",
     "python · bayesian gnn · nvd · gdelt",
     "a 2025 paper rebuilt end to end, with honest fallbacks when the apis say no"),
]
CIVIC = [
    ("PS-CRM", f"{GH}/pscrm", None,
     "civic intelligence layer on top of delhi’s grievance systems. top 10 at india innovates",
     "fastapi · next.js · langgraph · gemini · supabase",
     "every complaint becomes a signal about a real asset: a drain, a streetlight, a road"),
    ("drone swarm", "https://github.com/tusharsingh-spring/drone_swarm", "collab",
     "flood and fire response simulator for pune and pcmc",
     "python · websockets · 3d map",
     "up to 100 modelled drones working alongside real pcmc ground units"),
    ("career recommender", f"{GH}/sihreccadv", None,
     f"smart india hackathon. a personality test goes in, careers come out. first cut in [SIHreccomender]({GH}/SIHreccomender)",
     "fastapi · faiss · sentence transformers · supabase",
     "big five and riasec scores turned into a semantic search over careers"),
    ("crop contracts", f"{GH}/agribc", None,
     "contract farming marketplace. farmers list, buyers propose, both sign",
     "fastapi · supabase · gemini",
     "the contract pdf writes itself once both sides agree"),
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
     "a cleaner client for my college’s classroom platform",
     "next.js · prisma · cron",
     "emails you 48 hours before an assignment is due. the original never did"),
    ("QR attendance", f"{GH}/asepqr-genration", None,
     "attendance by qr code, one google sheet per session",
     "react · typescript · google sheets",
     "the code changes every 5 seconds and checks where you are, so no forwarding it to a friend"),
    ("AI free focus", f"{GH}/focuscode", None,
     "chrome extension that blocks ai coding assistants while you code",
     "javascript · manifest v3",
     "an ai blocker, built by someone who builds ai"),
    ("focus pursuit trainer", None, "private",
     "desktop app. a dot drifts across every monitor and you follow it",
     "javascript · desktop overlay",
     "your own desktop is the distraction layer"),
    ("the great machine", f"{GH}/blog-mdm", None,
     "a scroll story through industry 1.0 to 5.0",
     "html · css · javascript",
     "the one where the art director won"),
]

md = f"""{pic("hero", "Shreeviraj Matale. creative director who codes.", width="100%", href="https://shreeviraj.studio", phone=True)}

{" ".join(pic("pill-" + n, a, height="38", href=h) for n, a, h in PILLS)}

i'm **sri**. i build agents, memory systems and audit pipelines. mostly for hackathons, sometimes for clients, occasionally because something annoyed me. i also art direct, which is why this page looks the way it does.

EY techathon semi-finalist · top 10 at india innovates · three hackathon wins · 451 contributions last year, a third of them private

> keep the ai part invisible so the work gets judged as work.

<br>

{band("things-ive-built", "Things i've built. the ones worth opening.")}

### agents & automation
*things that decide, act, and keep running when i log off.*

{table(AGENTS)}

### memory & retrieval
*getting an llm to remember the right thing, and find it again.*

{table(MEMORY)}

### finance & compliance
*where a rounding error is a wrong answer.*

{table(FINANCE)}

### ml & vision
*models that had to hold up outside the notebook.*

{table(ML)}

### civic & public good
*maps, farms, floods and careers.*

{table(CIVIC)}

### learning & small tools
*software that teaches back, and a few things that fixed my own days.*

{table(LEARN)}

<sub>`private` means named, not linked. ask and i'll walk you through it. `collab` means a team repo i build in.</sub>

<br>

{band("right-now", "Right now. what's on the desk this month.")}

- **antAi** for smart india hackathon 2026. catches voice clone scams by fusing voice, video, text and intent into one 0 to 100 risk score. *then it logs, verifies, or freezes.*
- **ml-challenge**, closing the gap between 0.885 and the top of the amazon ml challenge leaderboard. *france is the suspect.*
- **jqp**, publishing and dms on official meta apis. *boring on purpose.*
- open to freelance: agents, pipelines, automation. *dms are open.*

<br>

{band("stack", "Stack. what the work gets built with.")}

**languages**<br>
{skill("python,ts,js,cpp,kotlin,go,html,css", "python, typescript, javascript, c++, kotlin, go, html, css")}

**web & backend**<br>
{skill("react,nextjs,nodejs,fastapi,tailwind,supabase,postgres,redis", "react, next.js, node, fastapi, tailwind, supabase, postgres, redis")}

**ai & ml**<br>
{skill("pytorch,tensorflow,opencv,sklearn", "pytorch, tensorflow, opencv, scikit-learn")}

**tools**<br>
{skill("git,github,docker,vercel,vscode,postman", "git, github, docker, vercel, vs code, postman")}

<br>

**i also**

```
art direct campaigns
prompt until it looks shot
ship at 2am
chronically online
```

*the commit graph has a sleep schedule. i don't.*

<br>

{pic("footer", "Say hello. shreeviraj5387@gmail.com", width="100%", href="mailto:shreeviraj5387@gmail.com", phone=True)}
"""

with open(os.path.join(os.path.dirname(HERE), "README.md"), "w", encoding="utf-8") as f:
    f.write(md)
print("README.md", len(md), "chars")
