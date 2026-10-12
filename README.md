<a href="https://shreeviraj.studio"><picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/hero-m-green.svg"><source media="(max-width: 600px)" srcset="assets/hero-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/hero-green.svg"><img src="assets/hero-blue.svg" alt="Shreeviraj Matale. creative director who codes." width="100%" loading="eager"></picture></a>

<a href="mailto:shreeviraj5387@gmail.com"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-hire-green.svg"><img src="assets/pill-hire-blue.svg" alt="email me" height="38" loading="eager"></picture></a> <a href="https://shreeviraj.studio"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-site-green.svg"><img src="assets/pill-site-blue.svg" alt="shreeviraj.studio" height="38" loading="eager"></picture></a> <a href="https://x.com/shreeviraj_dev"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-x-green.svg"><img src="assets/pill-x-blue.svg" alt="x" height="38" loading="eager"></picture></a> <a href="https://linkedin.com/in/shreeviraj"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-linkedin-green.svg"><img src="assets/pill-linkedin-blue.svg" alt="linkedin" height="38" loading="eager"></picture></a> <a href="https://instagram.com/1cr.sri"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-instagram-green.svg"><img src="assets/pill-instagram-blue.svg" alt="instagram" height="38" loading="eager"></picture></a>

i'm **sri**. i build agents, memory systems and audit pipelines. mostly for hackathons, sometimes for clients, occasionally because something annoyed me. i also art direct, which is why this page looks the way it does.

six hackathon wins · fourteen finals · 451 contributions last year, a third of them private

> **GOAL:** keep the ai part invisible so the work gets judged as work.

<br>

<picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/sec-things-ive-built-m-green.svg"><source media="(max-width: 600px)" srcset="assets/sec-things-ive-built-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/sec-things-ive-built-green.svg"><img src="assets/sec-things-ive-built-blue.svg" alt="Things i've built. the ones worth opening." width="100%" loading="eager"></picture>

### <picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-dom-agents--automation-green.svg"><img src="assets/pill-dom-agents--automation-blue.svg" alt="agents & automation" height="38" loading="eager"></picture>
*things that decide, act, and keep running when i log off.*

| what | with what | the twist |
| --- | --- | --- |
| **[DAKSHA](https://github.com/officialayush23/DAKSHA)** `collab`<br>EY techathon semi-finalist. a full commerce platform run by 8 specialist agents, from browsing to returns | langgraph · fastapi · gemini · postgres · react | *a policy gate checks every action before it runs, and anything risky waits for a human* |
| **jqp** `private`<br>instagram carousel publishing and comment to dm automation, on official meta apis only | next.js · typescript monorepo · supabase · bullmq · redis · sharp | *a crash resumable state machine. a publish that dies halfway picks up where it stopped* |
| **requirements agent** `private`<br>code apex 2.0, 2nd place. turns gmail threads and meet transcripts into a requirements doc | langgraph · gemini · instructor · gmail api · fastapi · react | *the meeting ends, the spec is already written* |
| **[Sahayak ops console](https://github.com/reesick/paytmhacks)**<br>paytm hackathon. an agent that resolves merchant issues, in hindi, over voice | react · vite | *it does the work but stops at a human approval gate before touching money* |
| **[ABTalks agent](https://github.com/reesick/abtalkshackathon)**<br>finds ai/ml topics, judges them against a persona, writes and posts | langgraph · aws bedrock · mcp · fastapi · apscheduler | *ran 48 hours unattended. nobody touched it* |
| **[Excel Bot](https://github.com/reesick/Excel-bot)**<br>built for my father’s automobile business. send any messy spreadsheet on telegram, get an excel dashboard and a deck back | anthropic sdk · pandas · xlsxwriter · matplotlib · fastapi | *one person’s weekly job, now a telegram message. claude is the analyst* |
| **ClipFarm** `private`<br>repost pipeline for clipping programs. reframes, brands, de-dupes and checks a clip before it goes up | python · ffmpeg · flask · pillow | *fully offline, no accounts, no api keys. it tells you if the post will get approved* |
| **[daily motivator](https://github.com/reesick/motivator)**<br>telegram bot that writes one thought a day and sends it at 7 am | python telegram bot · gemini · asyncpg · apscheduler | *checks its own history first, so it never says the same thing twice* |

### <picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-dom-memory--retrieval-green.svg"><img src="assets/pill-dom-memory--retrieval-blue.svg" alt="memory & retrieval" height="38" loading="eager"></picture>
*getting an llm to remember the right thing, and find it again.*

| what | with what | the twist |
| --- | --- | --- |
| **[MemoryOS](https://github.com/reesick/memos)**<br>open memory middleware for llm apps. put it in front of any chatbot | fastapi · kuzu · faiss · sentence transformers · ollama | *not plain rag. fact extraction, conflict resolution, a knowledge graph. fully local, p95 retrieval under 300 ms* |
| **[memos v2](https://github.com/reesick/memos-v2)**<br>local first memory workspace, with a dashboard to browse what it remembers | typescript · next.js · sqlite · postgres · mcp sdk | *runs on synthetic embeddings, so you can try it without a single api key* |
| **edi-5** `private`<br>multi domain rag assistant. started on cricket, now does finance and general knowledge too | fastapi · langchain · chroma · groq · react | *it routes before it retrieves. live, historical and analytical questions each get their own path* |

### <picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-dom-finance--compliance-green.svg"><img src="assets/pill-dom-finance--compliance-blue.svg" alt="finance & compliance" height="38" loading="eager"></picture>
*where a rounding error is a wrong answer.*

| what | with what | the twist |
| --- | --- | --- |
| **[COVENANT](https://github.com/reesick/COVENANT)**<br>audit grade covenant compliance testing for private credit. research in [ey-research](https://github.com/reesick/ey-research) | fastapi · sympy · z3 · docling · faiss · react | *zero floats. exact rational maths, and every run is hash chained and timestamped* |
| **[SAR-mvp](https://github.com/reesick/SAR-mvp)**<br>anti money laundering. writes the suspicious activity report for an analyst | langgraph · fastapi · postgres + pgvector · ollama · react | *seven agents and a local mistral. nothing leaves the machine* |
| **[ESG greenwashing agent](https://github.com/Pragati-1-7/Automated_ESG_Greenwashing_agent)** `collab`<br>reads a sustainability report and checks every claim against filings, regulators and news | langgraph · groq · pdfplumber · bm25 · mcp · fastapi | *every claim ends as align, contradict or insufficient, with an audit trail and a 0 to 100 risk score* |

### <picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-dom-ml--vision-green.svg"><img src="assets/pill-dom-ml--vision-blue.svg" alt="ml & vision" height="38" loading="eager"></picture>
*models that had to hold up outside the notebook.*

| what | with what | the twist |
| --- | --- | --- |
| **ml-challenge** `private`<br>amazon ml challenge 2026. business entity resolution across three sources, three countries | lightgbm · rapidfuzz · polars · transformers | *0.972 on local validation, 0.885 on the leaderboard. hunting the gap* |
| **[face detection, deployed](https://github.com/reesick/nhai)**<br>scrfd face detection for an on device pipeline, built with tushar. pruned and quantised from about 4 mb to 880 kb | onnx runtime · opencv · scrfd · pytorch | *tested the whole insightface family first, then benchmarked int8 against fp32 before picking* |
| **[CLINDerm](https://github.com/reesick/clinderm)**<br>three face photos in, an annotated skin health report out | fastapi · mediapipe · opencv · segformer · yolov8 | *four vision models, all running locally on a laptop 4050* |
| **[threat forecasting](https://github.com/reesick/cybersec-ind)**<br>forecasts cyber threats and the tech that counters them | pytorch geometric · statsmodels · networkx · fastapi | *a 2025 paper rebuilt end to end, with honest fallbacks when the apis say no* |

### <picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-dom-civic--public-good-green.svg"><img src="assets/pill-dom-civic--public-good-blue.svg" alt="civic & public good" height="38" loading="eager"></picture>
*maps, farms, floods and careers.*

| what | with what | the twist |
| --- | --- | --- |
| **[PS-CRM](https://github.com/reesick/pscrm)**<br>civic intelligence layer on top of delhi’s grievance systems. top 10 at india innovates | fastapi · langgraph · gemini · supabase · next.js · maplibre | *every complaint becomes a signal about a real asset: a drain, a streetlight, a road* |
| **[drone swarm](https://github.com/tusharsingh-spring/drone_swarm)** `collab`<br>flood and fire response simulator for pune and pcmc | python · websockets · 3d map viewer | *up to 100 modelled drones working alongside real pcmc ground units* |
| **[career recommender](https://github.com/reesick/sihreccadv)**<br>smart india hackathon. a personality test goes in, careers come out. first cut in [SIHreccomender](https://github.com/reesick/SIHreccomender) | fastapi · faiss · sentence transformers · supabase | *big five and riasec scores turned into a semantic search over careers* |
| **[crop contracts](https://github.com/reesick/agribc)**<br>contract farming marketplace. farmers list, buyers propose, both sign | fastapi · supabase · gemini · reportlab | *the contract pdf writes itself once both sides agree* |

### <picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-dom-learning--small-tools-green.svg"><img src="assets/pill-dom-learning--small-tools-blue.svg" alt="learning & small tools" height="38" loading="eager"></picture>
*software that teaches back, and a few things that fixed my own days.*

| what | with what | the twist |
| --- | --- | --- |
| **[Avinya](https://github.com/reesick/avinya)**<br>personalised video learning with a hybrid recommender | react · fastapi · supabase · scikit-learn · xgboost | *three recommenders blended: content, collaborative and knowledge based* |
| **[algo visualiser](https://github.com/reesick/edai-3-f1)**<br>algorithm visualiser with an ai tutor that watches how you learn | react · monaco · go websockets · fastapi · gemini | *pause too long and it slows down. hit replay and it gets technical* |
| **Better VOLP** `private`<br>a cleaner client for my college’s classroom platform | next.js · prisma · nodemailer · shadcn | *emails you 48 hours before an assignment is due. the original never did* |
| **[QR attendance](https://github.com/reesick/asepqr-genration)**<br>attendance by qr code, one google sheet per session | react · typescript · radix ui · google sheets api | *the code changes every 5 seconds and checks where you are, so no forwarding it to a friend* |
| **[AI free focus](https://github.com/reesick/focuscode)**<br>chrome extension that blocks ai coding assistants while you code | chrome manifest v3 · declarativeNetRequest | *an ai blocker, built by someone who builds ai* |
| **focus pursuit trainer** `private`<br>desktop app. a dot drifts across every monitor and you follow it | electron | *your own desktop is the distraction layer* |
| **[the great machine](https://github.com/reesick/blog-mdm)**<br>a scroll story through industry 1.0 to 5.0 | html · css · javascript | *the one where the art director won* |

<sub>`private` means named, not linked. ask and i'll walk you through it. `collab` means a team repo i build in.</sub>

<br>

<picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/sec-record-m-green.svg"><source media="(max-width: 600px)" srcset="assets/sec-record-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/sec-record-green.svg"><img src="assets/sec-record-blue.svg" alt="Record. wins and finals, mostly as team kala dhua." width="100%" loading="eager"></picture>

- **1st overall**, hacker occupied pune. *an agentic supply chain and distribution system, built in 24 hours.*
- **best innovation**, hackmatrix by pccoe’s aimsa.
- **top team**, curious parc, vit pune. *came with an internship offer from s2p robotics.*
- **2nd place**, code apex 2.0. *the requirements agent.*
- **top 10**, india innovates. *PS-CRM.*
- **semi-finalist**, EY techathon. *DAKSHA, an agentic commerce platform.*

<br>

<picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/sec-stack-m-green.svg"><source media="(max-width: 600px)" srcset="assets/sec-stack-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/sec-stack-green.svg"><img src="assets/sec-stack-blue.svg" alt="Stack. what the work gets built with." width="100%" loading="eager"></picture>

<table>
<tr><td><b>languages</b></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/python-d.svg"><img src="assets/chips/python.svg" height="20" alt="python"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/typescript-d.svg"><img src="assets/chips/typescript.svg" height="20" alt="typescript"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/javascript-d.svg"><img src="assets/chips/javascript.svg" height="20" alt="javascript"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/go-d.svg"><img src="assets/chips/go.svg" height="20" alt="go"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/c-d.svg"><img src="assets/chips/c.svg" height="20" alt="c++"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/html-d.svg"><img src="assets/chips/html.svg" height="20" alt="html"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/css-d.svg"><img src="assets/chips/css.svg" height="20" alt="css"></picture></td></tr>
<tr><td><b>web &amp; apps</b></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/react-d.svg"><img src="assets/chips/react.svg" height="20" alt="react"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/next-js-d.svg"><img src="assets/chips/next-js.svg" height="20" alt="next.js"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/vite-d.svg"><img src="assets/chips/vite.svg" height="20" alt="vite"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/node-js-d.svg"><img src="assets/chips/node-js.svg" height="20" alt="node.js"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/fastapi-d.svg"><img src="assets/chips/fastapi.svg" height="20" alt="fastapi"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/flask-d.svg"><img src="assets/chips/flask.svg" height="20" alt="flask"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/tailwind-d.svg"><img src="assets/chips/tailwind.svg" height="20" alt="tailwind"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/electron-d.svg"><img src="assets/chips/electron.svg" height="20" alt="electron"></picture></td></tr>
<tr><td><b>data</b></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/supabase-d.svg"><img src="assets/chips/supabase.svg" height="20" alt="supabase"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/postgres-d.svg"><img src="assets/chips/postgres.svg" height="20" alt="postgres"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/redis-d.svg"><img src="assets/chips/redis.svg" height="20" alt="redis"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/sqlite-d.svg"><img src="assets/chips/sqlite.svg" height="20" alt="sqlite"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/prisma-d.svg"><img src="assets/chips/prisma.svg" height="20" alt="prisma"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/pgvector-d.svg"><img src="assets/chips/pgvector.svg" height="20" alt="pgvector"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/faiss-d.svg"><img src="assets/chips/faiss.svg" height="20" alt="faiss"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/chroma-d.svg"><img src="assets/chips/chroma.svg" height="20" alt="chroma"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/kuzu-d.svg"><img src="assets/chips/kuzu.svg" height="20" alt="kuzu"></picture></td></tr>
<tr><td><b>ml &amp; vision</b></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/pytorch-d.svg"><img src="assets/chips/pytorch.svg" height="20" alt="pytorch"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/scikit-learn-d.svg"><img src="assets/chips/scikit-learn.svg" height="20" alt="scikit-learn"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/opencv-d.svg"><img src="assets/chips/opencv.svg" height="20" alt="opencv"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/pandas-d.svg"><img src="assets/chips/pandas.svg" height="20" alt="pandas"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/numpy-d.svg"><img src="assets/chips/numpy.svg" height="20" alt="numpy"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/onnx-d.svg"><img src="assets/chips/onnx.svg" height="20" alt="onnx"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/hugging-face-d.svg"><img src="assets/chips/hugging-face.svg" height="20" alt="hugging face"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/lightgbm-d.svg"><img src="assets/chips/lightgbm.svg" height="20" alt="lightgbm"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/mediapipe-d.svg"><img src="assets/chips/mediapipe.svg" height="20" alt="mediapipe"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/sentence-transformers-d.svg"><img src="assets/chips/sentence-transformers.svg" height="20" alt="sentence transformers"></picture></td></tr>
<tr><td><b>llms &amp; agents</b></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/langchain-d.svg"><img src="assets/chips/langchain.svg" height="20" alt="langchain"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/ollama-d.svg"><img src="assets/chips/ollama.svg" height="20" alt="ollama"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/gemini-d.svg"><img src="assets/chips/gemini.svg" height="20" alt="gemini"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/claude-d.svg"><img src="assets/chips/claude.svg" height="20" alt="claude"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/openai-d.svg"><img src="assets/chips/openai.svg" height="20" alt="openai"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/llama-d.svg"><img src="assets/chips/llama.svg" height="20" alt="llama"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/langgraph-d.svg"><img src="assets/chips/langgraph.svg" height="20" alt="langgraph"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/crewai-d.svg"><img src="assets/chips/crewai.svg" height="20" alt="crewai"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/mcp-d.svg"><img src="assets/chips/mcp.svg" height="20" alt="mcp"></picture></td></tr>
<tr><td><b>cloud &amp; tools</b></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/aws-d.svg"><img src="assets/chips/aws.svg" height="20" alt="aws"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/docker-d.svg"><img src="assets/chips/docker.svg" height="20" alt="docker"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/vercel-d.svg"><img src="assets/chips/vercel.svg" height="20" alt="vercel"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/cloudflare-d.svg"><img src="assets/chips/cloudflare.svg" height="20" alt="cloudflare"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/git-d.svg"><img src="assets/chips/git.svg" height="20" alt="git"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/github-d.svg"><img src="assets/chips/github.svg" height="20" alt="github"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/github-actions-d.svg"><img src="assets/chips/github-actions.svg" height="20" alt="github actions"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/postman-d.svg"><img src="assets/chips/postman.svg" height="20" alt="postman"></picture> &nbsp; <picture><source media="(prefers-color-scheme: dark)" srcset="assets/chips/telegram-d.svg"><img src="assets/chips/telegram.svg" height="20" alt="telegram"></picture></td></tr>
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

<a href="mailto:shreeviraj5387@gmail.com"><picture><source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/footer-m-green.svg"><source media="(max-width: 600px)" srcset="assets/footer-m-blue.svg"><source media="(prefers-color-scheme: dark)" srcset="assets/footer-green.svg"><img src="assets/footer-blue.svg" alt="Say hello. shreeviraj5387@gmail.com" width="100%" loading="eager"></picture></a>
