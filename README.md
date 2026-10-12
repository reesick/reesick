<a href="https://shreeviraj.studio"><picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/hero-m-green.svg"><source media="(max-width: 600px)" srcset="assets/hero-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/hero-green.svg"><img src="assets/hero-blue.svg" alt="Shreeviraj Matale. creative director who codes." width="100%"></picture></a>

<a href="mailto:shreeviraj5387@gmail.com"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-hire-green.svg"><img src="assets/pill-hire-blue.svg" alt="email me" height="38"></picture></a> <a href="https://shreeviraj.studio"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-site-green.svg"><img src="assets/pill-site-blue.svg" alt="shreeviraj.studio" height="38"></picture></a> <a href="https://x.com/shreeviraj_dev"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-x-green.svg"><img src="assets/pill-x-blue.svg" alt="x" height="38"></picture></a> <a href="https://linkedin.com/in/shreeviraj"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-linkedin-green.svg"><img src="assets/pill-linkedin-blue.svg" alt="linkedin" height="38"></picture></a> <a href="https://instagram.com/1cr.sri"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-instagram-green.svg"><img src="assets/pill-instagram-blue.svg" alt="instagram" height="38"></picture></a>

i'm **sri**. i build agents, memory systems and audit pipelines. mostly for hackathons, sometimes for clients, occasionally because something annoyed me. i also art direct, which is why this page looks the way it does.

EY techathon semi-finalist · top 10 at india innovates · three hackathon wins · 451 contributions last year, a third of them private

> keep the ai part invisible so the work gets judged as work.

<br>

<picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/sec-things-ive-built-m-green.svg"><source media="(max-width: 600px)" srcset="assets/sec-things-ive-built-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/sec-things-ive-built-green.svg"><img src="assets/sec-things-ive-built-blue.svg" alt="Things i've built. the ones worth opening." width="100%"></picture>

### agents & automation
*things that decide, act, and keep running when i log off.*

| what | with what | the twist |
| --- | --- | --- |
| **jqp** `private`<br>instagram carousel publishing and comment to dm automation, on official meta apis only | typescript · supabase · bullmq · redis | *a crash resumable state machine. a publish that dies halfway picks up where it stopped* |
| **requirements agent** `private`<br>turns gmail threads and meet transcripts into a requirements doc | langgraph · gemini · supabase | *the meeting ends, the spec is already written* |
| **[Sahayak ops console](https://github.com/reesick/paytmhacks)**<br>paytm hackathon. an agent that resolves merchant issues, in hindi, over voice | react · vite | *it does the work but stops at a human approval gate before touching money* |
| **[ABTalks agent](https://github.com/reesick/abtalkshackathon)**<br>finds ai/ml topics, judges them against a persona, writes and posts | python · fastapi · flora | *ran 48 hours unattended. nobody touched it* |
| **[Excel Bot](https://github.com/reesick/Excel-bot)**<br>telegram bot. send any messy spreadsheet, get an excel dashboard and a deck back | python · claude files api · code execution | *claude is the analyst. nobody tells it which columns matter* |
| **ClipFarm** `private`<br>repost pipeline for clipping programs. reframes, brands, de-dupes and checks a clip before it goes up | python · ffmpeg · flask | *fully offline, no accounts, no api keys. it tells you if the post will get approved* |
| **[daily motivator](https://github.com/reesick/motivator)**<br>telegram bot that writes one thought a day and sends it at 7 am | python · gemini · apscheduler | *checks its own history first, so it never says the same thing twice* |

### memory & retrieval
*getting an llm to remember the right thing, and find it again.*

| what | with what | the twist |
| --- | --- | --- |
| **[MemoryOS](https://github.com/reesick/memos)**<br>open memory middleware for llm apps. put it in front of any chatbot | python · knowledge graph · hybrid retrieval | *not plain rag. it extracts facts, settles conflicts and recalls across three stores at once* |
| **[memos v2](https://github.com/reesick/memos-v2)**<br>local first memory workspace, with a dashboard to browse what it remembers | typescript · next.js · sqlite | *runs on synthetic embeddings, so you can try it without a single api key* |
| **edi-5** `private`<br>multi domain rag assistant. started on cricket, now does finance and general knowledge too | fastapi · groq · chroma · react | *it routes before it retrieves. live, historical and analytical questions each get their own path* |

### finance & compliance
*where a rounding error is a wrong answer.*

| what | with what | the twist |
| --- | --- | --- |
| **[COVENANT](https://github.com/reesick/COVENANT)**<br>audit grade covenant compliance testing for private credit. EY techathon semi-finalist. research in [ey-research](https://github.com/reesick/ey-research) | python · sympy · faiss · pdfplumber | *zero floats. exact rational maths, and every run is hash chained and timestamped* |
| **[SAR-mvp](https://github.com/reesick/SAR-mvp)**<br>anti money laundering. writes the suspicious activity report for an analyst | langgraph · fastapi · pgvector · ollama | *seven agents and a local mistral. nothing leaves the machine* |
| **[ESG greenwashing agent](https://github.com/Pragati-1-7/Automated_ESG_Greenwashing_agent)** `collab`<br>reads a sustainability report and checks every claim against filings, regulators and news | python · agents · pdf parsing | *every claim ends as align, contradict or insufficient, with an audit trail and a 0 to 100 risk score* |

### ml & vision
*models that had to hold up outside the notebook.*

| what | with what | the twist |
| --- | --- | --- |
| **ml-challenge** `private`<br>amazon ml challenge 2026. business entity resolution across three sources, three countries | python · pruner + matcher · macro f0.5 | *0.972 on local validation, 0.885 on the leaderboard. hunting the gap* |
| **[face detection, deployed](https://github.com/reesick/nhai)**<br>scrfd face detection packaged to run anywhere, with a quantisation study | pytorch · onnx runtime · scrfd | *quantised it to int8, measured it, shipped fp32 anyway. 30 fps on a plain cpu* |
| **[CLINDerm](https://github.com/reesick/clinderm)**<br>three face photos in, an annotated skin health report out | yunet · mediapipe · segformer · yolov8 | *four vision models, all running locally on a laptop 4050* |
| **[threat forecasting](https://github.com/reesick/cybersec-ind)**<br>forecasts cyber threats and the tech that counters them | python · bayesian gnn · nvd · gdelt | *a 2025 paper rebuilt end to end, with honest fallbacks when the apis say no* |

### civic & public good
*maps, farms, floods and careers.*

| what | with what | the twist |
| --- | --- | --- |
| **[PS-CRM](https://github.com/reesick/pscrm)**<br>civic intelligence layer on top of delhi’s grievance systems. top 10 at india innovates | fastapi · next.js · langgraph · gemini · supabase | *every complaint becomes a signal about a real asset: a drain, a streetlight, a road* |
| **[drone swarm](https://github.com/tusharsingh-spring/drone_swarm)** `collab`<br>flood and fire response simulator for pune and pcmc | python · websockets · 3d map | *up to 100 modelled drones working alongside real pcmc ground units* |
| **[career recommender](https://github.com/reesick/sihreccadv)**<br>smart india hackathon. a personality test goes in, careers come out. first cut in [SIHreccomender](https://github.com/reesick/SIHreccomender) | fastapi · faiss · sentence transformers · supabase | *big five and riasec scores turned into a semantic search over careers* |
| **[crop contracts](https://github.com/reesick/agribc)**<br>contract farming marketplace. farmers list, buyers propose, both sign | fastapi · supabase · gemini | *the contract pdf writes itself once both sides agree* |

### learning & small tools
*software that teaches back, and a few things that fixed my own days.*

| what | with what | the twist |
| --- | --- | --- |
| **[Avinya](https://github.com/reesick/avinya)**<br>personalised video learning with a hybrid recommender | react · fastapi · supabase · lightfm | *three recommenders blended: content, collaborative and knowledge based* |
| **[algo visualiser](https://github.com/reesick/edai-3-f1)**<br>algorithm visualiser with an ai tutor that watches how you learn | react · go · python · gemini | *pause too long and it slows down. hit replay and it gets technical* |
| **Better VOLP** `private`<br>a cleaner client for my college’s classroom platform | next.js · prisma · cron | *emails you 48 hours before an assignment is due. the original never did* |
| **[QR attendance](https://github.com/reesick/asepqr-genration)**<br>attendance by qr code, one google sheet per session | react · typescript · google sheets | *the code changes every 5 seconds and checks where you are, so no forwarding it to a friend* |
| **[AI free focus](https://github.com/reesick/focuscode)**<br>chrome extension that blocks ai coding assistants while you code | javascript · manifest v3 | *an ai blocker, built by someone who builds ai* |
| **focus pursuit trainer** `private`<br>desktop app. a dot drifts across every monitor and you follow it | javascript · desktop overlay | *your own desktop is the distraction layer* |
| **[the great machine](https://github.com/reesick/blog-mdm)**<br>a scroll story through industry 1.0 to 5.0 | html · css · javascript | *the one where the art director won* |

<sub>`private` means named, not linked. ask and i'll walk you through it. `collab` means a team repo i build in.</sub>

<br>

<picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/sec-right-now-m-green.svg"><source media="(max-width: 600px)" srcset="assets/sec-right-now-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/sec-right-now-green.svg"><img src="assets/sec-right-now-blue.svg" alt="Right now. what's on the desk this month." width="100%"></picture>

- **antAi** for smart india hackathon 2026. catches voice clone scams by fusing voice, video, text and intent into one 0 to 100 risk score. *then it logs, verifies, or freezes.*
- **ml-challenge**, closing the gap between 0.885 and the top of the amazon ml challenge leaderboard. *france is the suspect.*
- **jqp**, publishing and dms on official meta apis. *boring on purpose.*
- open to freelance: agents, pipelines, automation. *dms are open.*

<br>

<picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/sec-stack-m-green.svg"><source media="(max-width: 600px)" srcset="assets/sec-stack-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/sec-stack-green.svg"><img src="assets/sec-stack-blue.svg" alt="Stack. what the work gets built with." width="100%"></picture>

**languages**<br>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=python,ts,js,cpp,kotlin,go,html,css&perline=12&theme=dark"><img src="https://skillicons.dev/icons?i=python,ts,js,cpp,kotlin,go,html,css&perline=12&theme=light" alt="python, typescript, javascript, c++, kotlin, go, html, css" height="44"></picture>

**web & backend**<br>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=react,nextjs,nodejs,fastapi,tailwind,supabase,postgres,redis&perline=12&theme=dark"><img src="https://skillicons.dev/icons?i=react,nextjs,nodejs,fastapi,tailwind,supabase,postgres,redis&perline=12&theme=light" alt="react, next.js, node, fastapi, tailwind, supabase, postgres, redis" height="44"></picture>

**ai & ml**<br>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=pytorch,tensorflow,opencv,sklearn&perline=12&theme=dark"><img src="https://skillicons.dev/icons?i=pytorch,tensorflow,opencv,sklearn&perline=12&theme=light" alt="pytorch, tensorflow, opencv, scikit-learn" height="44"></picture>

**tools**<br>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=git,github,docker,vercel,vscode,postman&perline=12&theme=dark"><img src="https://skillicons.dev/icons?i=git,github,docker,vercel,vscode,postman&perline=12&theme=light" alt="git, github, docker, vercel, vs code, postman" height="44"></picture>

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

<a href="mailto:shreeviraj5387@gmail.com"><picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/footer-m-green.svg"><source media="(max-width: 600px)" srcset="assets/footer-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/footer-green.svg"><img src="assets/footer-blue.svg" alt="Say hello. shreeviraj5387@gmail.com" width="100%"></picture></a>
