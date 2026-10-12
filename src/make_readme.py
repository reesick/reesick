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
    ("requirements agent", None, "private",
     "turns gmail threads and meet transcripts into a requirements doc",
     "langgraph · gemini · supabase",
     "the meeting ends, the spec is already written"),
    ("ABTalks agent", f"{GH}/abtalkshackathon", None,
     "finds ai/ml topics, judges them against a persona, writes and posts",
     "python · fastapi · flora",
     "ran 48 hours unattended. nobody touched it"),
    ("ClipFarm", None, "private",
     "repost pipeline for clipping programs. reframes, brands, de-dupes and checks a clip before it goes up",
     "python · ffmpeg · flask",
     "fully offline, no accounts, no api keys. it tells you if the post will get approved"),
]
VISION = [
    ("face detection, deployed", f"{GH}/nhai", None,
     "scrfd face detection packaged to run anywhere, with a quantisation study",
     "pytorch · onnx runtime · scrfd",
     "quantised it to int8, measured it, shipped fp32 anyway. 30 fps on a plain cpu"),
    ("threat forecasting", f"{GH}/cybersec-ind", None,
     "forecasts cyber threats and the tech that counters them",
     "python · bayesian gnn · nvd · gdelt",
     "a 2025 paper rebuilt end to end, with honest fallbacks when the apis say no"),
    ("career recommender", f"{GH}/sihreccadv", None,
     "smart india hackathon. a personality test goes in, careers come out",
     "fastapi · faiss · sentence transformers · supabase",
     "big five and riasec scores turned into a semantic search over careers"),
]
LEARN = [
    ("memos v2", f"{GH}/memos-v2", None,
     "local first memory workspace for llm apps, with a dashboard to browse what it remembers",
     "typescript · next.js · sqlite",
     "runs on synthetic embeddings, so you can try it without a single api key"),
    ("algo visualiser", f"{GH}/edai-3-f1", None,
     "algorithm visualiser with an ai tutor that watches how you learn",
     "react · go · python · gemini",
     "pause too long and it slows down. hit replay and it gets technical"),
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

{card("jqp", "jqp. instagram publishing and comment to dm automation on official meta apis. private.")}

{card("ml-challenge", "ml-challenge. amazon ml challenge 2026, business entity resolution. private.")}

{card("pscrm", "PS-CRM. civic intelligence layer for delhi mcd. top 10 at india innovates.", f"{GH}/pscrm")}

<br>

{band("everything-else", "Everything else. by domain.")}

### agents & automation
*things that decide, and keep running when i log off.*

{table(AGENTS)}

### vision & forecasting
*faces, threats, and people’s futures. no pressure.*

{table(VISION)}

### memory & learning
*software that remembers, and software that teaches back.*

{table(LEARN)}

<sub>`private` means named, not linked. ask and i'll walk you through it.</sub>

<br>

{pic("footer", "Say hello. shreeviraj5387@gmail.com", width="100%", href="mailto:shreeviraj5387@gmail.com", phone=True)}
"""

with open(os.path.join(os.path.dirname(HERE), "README.md"), "w", encoding="utf-8") as f:
    f.write(md)
print("README.md", len(md), "chars")
