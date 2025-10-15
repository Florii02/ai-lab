# My AI/Context Engineering Notebook
This repo contains a collection of knowledge on IT topics, with a strong focus on AI, Data Analythics and Data Communication Pipelines

# 🚀 14‑Day “Sellable Skills” AI & Context Engineering Sprint

---

## Day 1: Workspace Setup + Git Workflow
- Install VSCode, Git, Python (via Anaconda or pyenv).
- Set up VSCode extensions: Python, GitLens, Markdown All In One.
- Initialize personal GitHub repo (“ai-lab-notes”).
- Learn: `git clone` → `git add/commit/push` → `pull` → `branch` → `reset`.
- 📓 Document: *“My Setup Log Day 1”* in repo.

---

## Day 2: Python Refresher (AI-Assisted)
- Use AI (Abacus/GPT) to auto‑condense *Automate the Boring Stuff*:
  - Scripts: loops, lists, dicts, functions.
  - File handling: CSV/Excel read/write.
  - Simple automation (rename files / scrape / API call).
- Run all scripts in VSCode with terminal → see input/output.
- 📓 Document: *"Python cheatsheet in Markdown"* (snippets, explanation).

---

## Day 3: ETL + Power Query (EU‑first)
- Learn what ETL = Extract, Transform, Load.
- Hands‑on:
  - Pull data from CSV into Python pandas.
  - Push into Excel.
  - Open Excel → PowerQuery → model and transform.
- Emphasize GDPR‑safe local datasets.
- 📓 Document: *“ETL basics with pandas + PowerQuery”*.

---

## Day 4: APIs & Webhooks Foundations
- Learn REST basics: GET, POST, headers, tokens.
- Use Python `requests` to call e.g. EU weather API.
- Push results to local CSV or Google Sheets.
- Learn webhooks in Make.com: create “catch webhook → write to Sheets”.
- 📓 Document: *API + Webhook patterns (with example code)*.

---

## Day 5: Deployment First – FastAPI + Docker
- Create very simple Python FastAPI endpoint: “Hello from EU AI App”.
- Containerize with Docker.
- Host lean: HuggingFace Spaces (EU hosting) OR Hetzner/Scaleway instance.
- 📓 Document: *“FastAPI + Docker deployment guide”*.

---

## Day 6: Automation Platforms (Make.com, n8n)
- Make.com: Trigger (webhook or Gmail) → Action (Sheets, Slack).
- n8n: same but test EU self‑host option (Docker).
- Connect to your FastAPI endpoint → trigger API in automation flow.
- 📓 Document: *One end‑to‑end webhook → API → automation flow*.

---

## Day 7–8: Context Engineering Basics
- Markdown “Prompt Book”:
  - Persona + Task.
  - Chain‑of‑thought.
  - Debugging (re‑prompt / refine context).
- Hands‑on: Build structured prompt templates in Markdown.
- Test with Abacus models → log differences.
- 📓 Document: *Prompt Framework v1*.

---

## Day 9: Embeddings + RAG (Applied)
- Ingest text (company manuals / compliance docs).
- Vectorize: ChromaDB / FAISS local.
- Build minimal retrieval pipeline.
- Expose via your FastAPI deployment so it plugs into Make.com.
- 📓 Document: *“RAG integration pipeline EU‑safe”*.

---

## Day 10: APIs + Automations with AI in Loop
- Extend yesterday: webhook → query vector store → return answer.
- Wrap in Make.com automation (query knowledge base).
- GDPR note: ensure local/EU‑only storage.
- 📓 Document: *“AI‑as‑a‑Service with ETL + Automations in 1 flow”*.

---

## Day 11: Advanced Automations
- Integrate LLM → Salesforce‑like CRM data (mock if real not available).
- Flow: Email → AI‑tag sentiment (FastAPI) → logged in Sheet/DB.
- Add Slack notifications for team.
- 📓 Document: *Real sellable business automation use case*.

---

## Day 12: Power BI + AI Output Integration
- Automate data push into Power BI via APIs (if corporate safe).
- Alternative: Local EU dashboards (Metabase free + EU VM).
- Add AI‑powered insights summary → feed into dashboard text fields.
- 📓 Document: *“Analytics + AI storytelling dashboards”*.

---

## Day 13: System Integration Practice
- Combine:
  - ETL (data from API).
  - AI context pipeline (embeddings or summarization).
  - BI visualization.
  - Automations (n8n/Make sending alerts).
- You now have an end‑to‑end pipeline a company could use.
- 📓 Document: *Case Study: "From data → AI → dashboard → alert"*.

---

## Day 14: Wrap‑Up + Portfolio Packaging
- Polish Markdown repo → structured like a knowledgebase/manual.
- Record key *“Sellable Use Cases”* logs:
  - GDPR‑compliant Q&A bot.
  - Business data alert automation.
  - AI‑driven dashboard pipeline.
- Bonus: Deploy repo/docs with MkDocs or GitHub Pages → shareable *“playbook”*.