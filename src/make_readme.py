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
    # five per line keeps every icon the same size on desktop and phone
    n = len(ids.split(","))
    w = min(n, 5) * 48 - 8
    a = f"https://skillicons.dev/icons?i={ids}&perline=5"
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{a}&theme=dark">'
            f'<img src="{a}&theme=light" alt="{alt}" width="{w}"></picture>')


PILLS = [
    ("hire", "email me", "mailto:shreeviraj5387@gmail.com"),
    ("site", "shreeviraj.studio", "https://shreeviraj.studio"),
    ("x", "x", "https://x.com/shreeviraj_dev"),
    ("linkedin", "linkedin", "https://linkedin.com/in/shreeviraj"),
    ("instagram", "instagram", "https://instagram.com/1cr.sri"),
]

AGENTS = [
    ('DAKSHA', 'https://github.com/officialayush23/DAKSHA', 'collab', 'EY techathon semi-finalist. a full commerce platform run by 8 specialist agents, from browsing to returns', 'langgraph · fastapi · gemini · postgres · react', 'a policy gate checks every action before it runs, and anything risky waits for a human'),
    ('jqp', None, 'private', 'instagram carousel publishing and comment to dm automation, on official meta apis only', 'next.js · typescript monorepo · supabase · bullmq · redis · sharp', 'a crash resumable state machine. a publish that dies halfway picks up where it stopped'),
    ('requirements agent', None, 'private', 'code apex 2.0, 2nd place. turns gmail threads and meet transcripts into a requirements doc', 'langgraph · gemini · instructor · gmail api · fastapi · react', 'the meeting ends, the spec is already written'),
    ('Sahayak ops console', 'https://github.com/reesick/paytmhacks', None, 'paytm hackathon. an agent that resolves merchant issues, in hindi, over voice', 'react · vite', 'it does the work but stops at a human approval gate before touching money'),
    ('ABTalks agent', 'https://github.com/reesick/abtalkshackathon', None, 'finds ai/ml topics, judges them against a persona, writes and posts', 'langgraph · aws bedrock · mcp · fastapi · apscheduler', 'ran 48 hours unattended. nobody touched it'),
    ('Excel Bot', 'https://github.com/reesick/Excel-bot', None, 'built for my father’s automobile business. send any messy spreadsheet on telegram, get an excel dashboard and a deck back', 'anthropic sdk · pandas · xlsxwriter · matplotlib · fastapi', 'one person’s weekly job, now a telegram message. claude is the analyst'),
    ('ClipFarm', None, 'private', 'repost pipeline for clipping programs. reframes, brands, de-dupes and checks a clip before it goes up', 'python · ffmpeg · flask · pillow', 'fully offline, no accounts, no api keys. it tells you if the post will get approved'),
    ('daily motivator', 'https://github.com/reesick/motivator', None, 'telegram bot that writes one thought a day and sends it at 7 am', 'python telegram bot · gemini · asyncpg · apscheduler', 'checks its own history first, so it never says the same thing twice'),
]

MEMORY = [
    ('MemoryOS', 'https://github.com/reesick/memos', None, 'open memory middleware for llm apps. put it in front of any chatbot', 'fastapi · kuzu · faiss · sentence transformers · ollama', 'not plain rag. fact extraction, conflict resolution, a knowledge graph. fully local, p95 retrieval under 300 ms'),
    ('memos v2', 'https://github.com/reesick/memos-v2', None, 'local first memory workspace, with a dashboard to browse what it remembers', 'typescript · next.js · sqlite · postgres · mcp sdk', 'runs on synthetic embeddings, so you can try it without a single api key'),
    ('edi-5', None, 'private', 'multi domain rag assistant. started on cricket, now does finance and general knowledge too', 'fastapi · langchain · chroma · groq · react', 'it routes before it retrieves. live, historical and analytical questions each get their own path'),
]

FINANCE = [
    ('COVENANT', 'https://github.com/reesick/COVENANT', None, 'audit grade covenant compliance testing for private credit. research in [ey-research](https://github.com/reesick/ey-research)', 'fastapi · sympy · z3 · docling · faiss · react', 'zero floats. exact rational maths, and every run is hash chained and timestamped'),
    ('SAR-mvp', 'https://github.com/reesick/SAR-mvp', None, 'anti money laundering. writes the suspicious activity report for an analyst', 'langgraph · fastapi · postgres + pgvector · ollama · react', 'seven agents and a local mistral. nothing leaves the machine'),
    ('ESG greenwashing agent', 'https://github.com/Pragati-1-7/Automated_ESG_Greenwashing_agent', 'collab', 'reads a sustainability report and checks every claim against filings, regulators and news', 'langgraph · groq · pdfplumber · bm25 · mcp · fastapi', 'every claim ends as align, contradict or insufficient, with an audit trail and a 0 to 100 risk score'),
]

ML = [
    ('ml-challenge', None, 'private', 'amazon ml challenge 2026. business entity resolution across three sources, three countries', 'lightgbm · rapidfuzz · polars · transformers', '0.972 on local validation, 0.885 on the leaderboard. hunting the gap'),
    ('face detection, deployed', 'https://github.com/reesick/nhai', None, 'scrfd face detection for an on device pipeline, built with tushar. pruned and quantised from about 4 mb to 880 kb', 'onnx runtime · opencv · scrfd · pytorch', 'tested the whole insightface family first, then benchmarked int8 against fp32 before picking'),
    ('CLINDerm', 'https://github.com/reesick/clinderm', None, 'three face photos in, an annotated skin health report out', 'fastapi · mediapipe · opencv · segformer · yolov8', 'four vision models, all running locally on a laptop 4050'),
    ('threat forecasting', 'https://github.com/reesick/cybersec-ind', None, 'forecasts cyber threats and the tech that counters them', 'pytorch geometric · statsmodels · networkx · fastapi', 'a 2025 paper rebuilt end to end, with honest fallbacks when the apis say no'),
]

CIVIC = [
    ('PS-CRM', 'https://github.com/reesick/pscrm', None, 'civic intelligence layer on top of delhi’s grievance systems. top 10 at india innovates', 'fastapi · langgraph · gemini · supabase · next.js · maplibre', 'every complaint becomes a signal about a real asset: a drain, a streetlight, a road'),
    ('drone swarm', 'https://github.com/tusharsingh-spring/drone_swarm', 'collab', 'flood and fire response simulator for pune and pcmc', 'python · websockets · 3d map viewer', 'up to 100 modelled drones working alongside real pcmc ground units'),
    ('career recommender', 'https://github.com/reesick/sihreccadv', None, 'smart india hackathon. a personality test goes in, careers come out. first cut in [SIHreccomender](https://github.com/reesick/SIHreccomender)', 'fastapi · faiss · sentence transformers · supabase', 'big five and riasec scores turned into a semantic search over careers'),
    ('crop contracts', 'https://github.com/reesick/agribc', None, 'contract farming marketplace. farmers list, buyers propose, both sign', 'fastapi · supabase · gemini · reportlab', 'the contract pdf writes itself once both sides agree'),
]

LEARN = [
    ('Avinya', 'https://github.com/reesick/avinya', None, 'personalised video learning with a hybrid recommender', 'react · fastapi · supabase · scikit-learn · xgboost', 'three recommenders blended: content, collaborative and knowledge based'),
    ('algo visualiser', 'https://github.com/reesick/edai-3-f1', None, 'algorithm visualiser with an ai tutor that watches how you learn', 'react · monaco · go websockets · fastapi · gemini', 'pause too long and it slows down. hit replay and it gets technical'),
    ('Better VOLP', None, 'private', 'a cleaner client for my college’s classroom platform', 'next.js · prisma · nodemailer · shadcn', 'emails you 48 hours before an assignment is due. the original never did'),
    ('QR attendance', 'https://github.com/reesick/asepqr-genration', None, 'attendance by qr code, one google sheet per session', 'react · typescript · radix ui · google sheets api', 'the code changes every 5 seconds and checks where you are, so no forwarding it to a friend'),
    ('AI free focus', 'https://github.com/reesick/focuscode', None, 'chrome extension that blocks ai coding assistants while you code', 'chrome manifest v3 · declarativeNetRequest', 'an ai blocker, built by someone who builds ai'),
    ('focus pursuit trainer', None, 'private', 'desktop app. a dot drifts across every monitor and you follow it', 'electron', 'your own desktop is the distraction layer'),
    ('the great machine', 'https://github.com/reesick/blog-mdm', None, 'a scroll story through industry 1.0 to 5.0', 'html · css · javascript', 'the one where the art director won'),
]


md = f"""{pic("hero", "Shreeviraj Matale. creative director who codes.", width="100%", href="https://shreeviraj.studio", phone=True)}

{" ".join(pic("pill-" + n, a, height="38", href=h) for n, a, h in PILLS)}

i'm **sri**. i build agents, memory systems and audit pipelines. mostly for hackathons, sometimes for clients, occasionally because something annoyed me. i also art direct, which is why this page looks the way it does.

six hackathon wins · fourteen finals · 451 contributions last year, a third of them private

> **GOAL:** keep the ai part invisible so the work gets judged as work.

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

{band("record", "Record. wins and finals, mostly as team kala dhua.")}

- **1st overall**, hacker occupied pune. *an agentic supply chain and distribution system, built in 24 hours.*
- **best innovation**, hackmatrix by pccoe’s aimsa.
- **top team**, curious parc, vit pune. *came with an internship offer from s2p robotics.*
- **2nd place**, code apex 2.0. *the requirements agent.*
- **top 10**, india innovates. *PS-CRM.*
- **semi-finalist**, EY techathon. *DAKSHA, an agentic commerce platform.*

<br>

{band("stack", "Stack. what the work gets built with.")}

<table>
<tr><td><b>languages</b></td><td>{skill("python,ts,js,go,cpp,html,css", "python, typescript, javascript, go, c++, html, css")}</td></tr>
<tr><td><b>web &amp; apps</b></td><td>{skill("react,nextjs,vite,nodejs,fastapi,flask,tailwind,electron", "react, next.js, vite, node, fastapi, flask, tailwind, electron")}</td></tr>
<tr><td><b>data</b></td><td>{skill("supabase,postgres,redis,sqlite,prisma", "supabase, postgres, redis, sqlite, prisma")}</td></tr>
<tr><td><b>ml &amp; vision</b></td><td>{skill("pytorch,sklearn,opencv", "pytorch, scikit-learn, opencv")}</td></tr>
<tr><td><b>llms &amp; agents</b></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack-ai-green.svg"><img src="assets/stack-ai-blue.svg" alt="langchain, ollama, gemini, claude, openai, llama, hugging face, onnx" width="232"></picture></td></tr>
<tr><td><b>cloud &amp; tools</b></td><td>{skill("aws,docker,vercel,cloudflare,git,github,githubactions,vscode,postman", "aws, docker, vercel, cloudflare, git, github, github actions, vs code, postman")}</td></tr>
<tr><td><b>no logo, still used</b></td><td>langgraph · crewai · faiss · chroma · kuzu · pgvector · lightgbm · sentence transformers · mediapipe · onnx runtime</td></tr>
</table>

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
