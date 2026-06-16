# Lab Content Evaluation — WPLUS Azure AI Platform and Services

**Evaluation date:** 2026-06-09
**Reviewer:** Lab Content Evaluator (subagent)
**Scope:** Full workshop — Lab 00 through Lab 10 plus the Optional Lab (AI Fundamentals)

> Authoritative sources consulted: `learn.microsoft.com` (Microsoft Foundry / Azure AI Foundry docs, Azure AI Projects SDK reference v2.2.0, Azure AI Evaluation SDK, Foundry Agent Service, Foundry Models catalog), `microsoft.github.io/graphrag`. Citations appear inline per finding.

---

## Executive Summary

| Lab | Rating | Headline issue |
|-----|--------|----------------|
| Lab 00 – Prerequisites / Foundry Resource Creation | ⚠️ Needs minor updates | Legacy `text-embedding-ada-002` deployed; "Prequisite" folder typo; no Entra-ID-only auth guidance |
| Lab 01 – AI Foundry (Connection + Evaluations) | ❌ Needs significant rework | Pins beta SDK `azure-ai-projects==1.0.0b12`; GA is **2.2.0**. Mixes deprecated `PROJECT_CONNECTION_STRING` with endpoint auth |
| Lab 02 – Agents | ⚠️ Needs minor updates | Uses `azure-ai-projects.agents`; agents now have a dedicated GA path/tool catalog; model `gpt-4o-mini` dated |
| Lab 03 – AI Language | ⚠️ Needs minor updates | API key + endpoint flow; hard-coded local file paths; Logic Apps tool screenshots may drift |
| Lab 04 – AI Vision | ⚠️ Needs minor updates | Face API gated/limited-access; Video Indexer API churn; verify current SDK names |
| Lab 05 – Fine-Tuning | ⚠️ Needs minor updates | Portal-only steps drift; missing newer methods (DPO/RFT); GPT-4.1-mini base ok but expand |
| Lab 06 – Prompt Engineering | ⚠️ Needs minor updates | Hard-coded `C:/Users/Admin/...` path; no reasoning-model guidance; Prompt Flow link aging |
| Lab 07 – Responsible AI (RAI) | ⚠️ Needs minor updates | Hard-coded local paths; portal navigation ("Guardrails + controls", "Protect and govern") drifts |
| Lab 08 – RAG Patterns (GraphRAG) | ⚠️ Needs minor updates | DRIFT query "not working as of v2.7.0"; `text-embedding-ada-002`; api-version `2024-05-01-preview` |
| Lab 09 – Security (AI Red Teaming) | ✅ Up to date | Solid; minor typos ("attach"/"stragies"); `2024-12-01-preview` API version will age |
| Lab 10 – Vector DB (Cosmos/PostgreSQL/SQL) | ⚠️ Needs minor updates | Thin READMEs; logic lives in notebooks; confirm embedding model + DiskANN guidance |
| Optional Lab – AI Fundamentals (RAG, SK & AutoGen) | ⚠️ Needs minor updates | AutoGen superseded by Microsoft Agent Framework; "proceed to Lab 5" mis-reference |

**Cross-cutting issues**
- **Beta SDK pinning.** Lab 01 pins `azure-ai-projects>=1.0.0b12`. The package is **GA at v2.2.0** (Microsoft Foundry SDK, last updated 2026-06-01). Beta pins risk breakage and teach deprecated patterns. Source: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- **Deprecated connection-string auth.** Several labs reference `PROJECT_CONNECTION_STRING`. The current SDK uses a **Foundry project endpoint URL** (`https://<account>.services.ai.azure.com/api/projects/<project>`) with **Entra ID (DefaultAzureCredential)** — "Entra ID is the only authentication method currently supported by the client." Source: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- **Hard-coded local paths.** `C:/Users/Admin/Desktop/...` appears in Labs 06 and 07 (and a notebook output in Lab 01), which won't match the learner's environment.
- **Legacy embedding model.** `text-embedding-ada-002` recurs (Lab 00, Lab 08). Prefer `text-embedding-3-small`/`-large`.
- **Naming/spelling inconsistencies.** Folder "Prequisite", "Lab 07- RAI" spacing, "attach strategies"/"stragies" typos.

---

## Lab 00 — Prerequisites: AI Foundry Resource Creation

**Files reviewed:** `01-Create-Azure-Foundry-Project.md`, `02-Deploy-Models.md`, `03-Connect-to-Bing-Resources.md`, `04-Connect-to-Azure-AI-Search.md`, `05-Setup-(dot)env-file.md`, `06-Run-requirements.md`, `images/`.

**Accuracy findings**
- `02-Deploy-Models.md` deploys `text-embedding-ada-002` alongside `text-embedding-3-large`. `ada-002` is a legacy generation; Microsoft recommends the v3 embedding family (`text-embedding-3-small`/`-large`) for new work. Keep `ada-002` only if a later lab specifically requires it (Lab 08 does reference it). Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
- Models list is `GPT-4o`, `GPT-4o-mini`, `text-embedding-3-large`, `text-embedding-ada-002`. The Foundry catalog now leads with GPT-4.1, o-series reasoning models, and GPT-5-class models; consider refreshing the chat models or adding a note that newer models are available. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview
- Portal steps reference "Model catalog" → "Use this model" → "Deploy"; this matches the current Microsoft Foundry portal flow. ✅

**Quality findings**
- Folder name "Prequisite" is misspelled (should be "Prerequisite"); this propagates into many cross-lab relative links. Low risk but unprofessional in a customer-facing asset.
- Clear, well-screenshotted, good time estimates. `05-Setup-(dot)env-file.md` correctly centralizes a root `.env`.

**Relevance findings**
- Bing and Azure AI Search connections are still the recommended grounding connections for agents; aligns with current guidance. ✅
- No mention of **Entra-ID-only auth** or RBAC role assignment as a first-class prerequisite — recommended addition since key-based auth is being phased out in the SDK.

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Replace/annotate `text-embedding-ada-002` → `text-embedding-3-small`/`-large` unless required downstream (it is in Lab 08 — cross-note it). *(Priority: Medium)*
2. Add a short "Assign yourself the Azure AI User / Azure AI Developer role" step and call out Entra ID auth. *(Priority: Medium)*
3. Fix the "Prequisite" folder spelling (coordinate the link updates repo-wide). *(Priority: Low)*

---

## Lab 01 — AI Foundry (Connection with AOAI + Evaluations)

**Files reviewed:** `Labs/Connection with AOAI/README.md`, `Labs/Connection with AOAI/setup and quick_start.ipynb`, `Labs/Evaluations/README.md`, `Labs/Evaluations/1-evaluation.ipynb`.

**Accuracy findings**
- The notebook/README require **`azure-ai-projects>=1.0.0b12`** (a beta). The package is **GA at version 2.2.0** (Microsoft Foundry SDK, last updated 2026-06-01). The b12 → 2.x jump includes breaking changes (agents surface, OpenAI client via `.get_openai_client()`, Responses API). Update the pin and the code patterns. Source: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- The evaluation notebook references `PROJECT_CONNECTION_STRING` and `AI_FOUNDRY_PROJECT_ENDPOINT` interchangeably. Current guidance: construct `AIProjectClient(endpoint=<project endpoint URL>, credential=DefaultAzureCredential())`. Connection-string construction is deprecated. Source: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- The Evaluations notebook uses the `azure-ai-evaluation` SDK with `F1Score` and `Relevance` evaluators and a cloud `Evaluation`/`InputDataset` submission — these APIs are current; verify import paths against the latest `azure-ai-evaluation` release. Source: https://learn.microsoft.com/python/api/azure-ai-evaluation/azure.ai.evaluation
- A notebook output cell embeds an absolute path `C:\Users\Admin\Desktop\WPLUS-...` — cosmetic, but should be cleared from committed outputs.

**Quality findings**
- READMEs are well-structured (Objectives, Scenario, Tasks, Execution, Troubleshooting). Strong. ✅
- `InteractiveBrowserCredential` vs `DefaultAzureCredential` is presented as a fallback chain — good, but align with the SDK's documented `DefaultAzureCredential` default.
- Committed notebook outputs (emoji status logs) inflate the file and leak a local path; clear outputs before shipping.

**Relevance findings**
- Local + cloud evaluation is exactly the current recommended Foundry observability pattern; strong relevance. ✅
- Missing newer evaluators (Groundedness Pro, Agentic/Intent-resolution, risk & safety) that are now part of the Foundry evaluation catalog — opportunity (see Advisor).

**Overall rating:** ❌ Needs significant rework (driven by the beta SDK pin and deprecated auth)

**Recommended actions**
1. Bump to **`azure-ai-projects==2.2.0`** (or latest) and migrate code: `AIProjectClient(endpoint=..., credential=DefaultAzureCredential())`, use `.get_openai_client()` for chat/Responses. *(Priority: High)*
2. Remove all `PROJECT_CONNECTION_STRING` usage; standardize on the Foundry project endpoint URL + Entra ID. *(Priority: High)*
3. Clear committed notebook outputs (and the leaked local path). *(Priority: Low)*
4. Verify `azure-ai-evaluation` import paths against the latest release. *(Priority: Medium)*

---

## Lab 02 — Agents

**Files reviewed:** `README.md`, `1-basics.ipynb`, `3-file-search.ipynb` (and sibling agent notebooks), `Files/`.

**Accuracy findings**
- Agents are created via `project_client.agents.create_agent(model=..., name=..., instructions=...)`. This pattern is current under the Foundry Agent Service, but with the GA SDK (2.x) the agents surface and tool catalog have expanded; verify `FileSearchTool`/`CodeInterpreterTool` import paths against v2.2.0. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview
- Default model `os.environ.get("MODEL_DEPLOYMENT_NAME", "gpt-4o-mini")` — functional but dated; consider GPT-4.1-mini / model router as default. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview
- Vector store + `FileSearchTool` usage is valid; confirm the vector-store creation call signature in the GA SDK.

**Quality findings**
- Strong domain framing (health/fitness), clear disclaimers, good role/RBAC notes ("Azure AI Developer", "Storage Blob Data Contributor", "Cognitive Search Data Contributor"). ✅
- "Next Steps" suggest OpenTelemetry/Azure Monitor and function calling — good forward pointers.

**Relevance findings**
- Single-agent + tools is the right foundation, but the workshop does not yet teach **multi-agent / connected agents** or newer tools (MCP, Bing grounding tool, Logic Apps/OpenAPI) which are now central to the Agent Service. Opportunity (see Advisor).

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Re-verify all agent/tool imports against `azure-ai-projects` 2.2.0; update any moved symbols. *(Priority: High)*
2. Refresh default model to GPT-4.1-mini or introduce **model router**. *(Priority: Medium)*
3. Add a short "what's next: connected/multi-agent + MCP tool" teaser. *(Priority: Low)*

---

## Lab 03 — AI Language

**Files reviewed:** `README.md`, `Images/`, advanced/bonus translation + PII Logic Apps sections.

**Accuracy findings**
- Uses Language resource **API key + endpoint** copied from the Foundry Overview page. Functional and still supported, but flag that Microsoft is steering toward Entra ID / keyless auth for AI services; add a keyless option note. Source: https://learn.microsoft.com/en-us/azure/ai-services/authentication
- Translation/PII via **Logic Apps as an agent tool** is a valid current pattern (OpenAPI/Logic Apps tools in the Agent Service). Screenshots of the Foundry/Logic Apps UI are prone to drift. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/logic-apps

**Quality findings**
- Long but well-sequenced checklist format; image-heavy (good for a portal lab, but increases maintenance).
- Note text references staying within the same subscription/resource group as Foundry — helpful troubleshooting.

**Relevance findings**
- PII detection/redaction and translation remain core Language scenarios; aligned. ✅
- Consider adding the newer **conversational language understanding / PII for conversations** or summarization skills as optional extensions.

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add a keyless (Entra ID) auth option alongside the API key flow. *(Priority: Medium)*
2. Add an image "last verified" date or callout that the portal UI may differ. *(Priority: Low)*

---

## Lab 04 — AI Vision

**Files reviewed:** `README.md` (Exercises 1–5: provisioning, Face analysis, OCR, Image Analysis, Video Indexer).

**Accuracy findings**
- **Face API** features (analysis/recognition) are under **Limited Access / gated** approval. The lab should state the Responsible AI gating and that some capabilities require an application. Source: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/identity-limited-access
- OCR/Image Analysis should use **Image Analysis 4.0** (Read + captioning/tags). Confirm the lab uses the 4.0 API/SDK, not legacy v3.x `Computer Vision` calls. Source: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis
- **Video Indexer** API surface changes periodically; verify the endpoints/account-access-token flow against the current docs. Source: https://learn.microsoft.com/en-us/azure/azure-video-indexer/

**Quality findings**
- Good exercise progression; ensure each exercise lists the exact package/endpoint used.

**Relevance findings**
- Vision scenarios remain relevant, but multimodal LLMs (GPT-4o vision) now overlap with classic OCR/Image Analysis; a note comparing the two would add value (see Advisor).

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add the Face **Limited Access** gating note and link the application process. *(Priority: Medium)*
2. Confirm Image Analysis **4.0** usage and update any legacy v3.x calls. *(Priority: Medium)*
3. Re-verify the Video Indexer auth/endpoint flow. *(Priority: Medium)*

---

## Lab 05 — Fine-Tuning

**Files reviewed:** `README.md`, `Advance Fine-Tuning/README.MD`.

**Accuracy findings**
- Targets fine-tuning **GPT-4.1-mini** in the Foundry portal — a currently supported base for SFT. ✅ Verify the portal navigation ("Fine-tuning" entry point) matches the current Foundry UI. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning
- The lab teaches only supervised fine-tuning (SFT). Foundry now also supports **DPO (preference)** and **RFT (reinforcement fine-tuning)** methods; the lab is accurate but incomplete vs current capability. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/fine-tuning-considerations

**Quality findings**
- Step-by-step portal flow is clear (sign in → portal → start → configure → review → deploy/test).
- Portal-only labs drift quickly with UI changes; add "verified on <date>".

**Relevance findings**
- Fine-tuning remains relevant; adding DPO/RFT and **distillation** would modernize it (see Advisor).

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add an overview/optional section on **DPO** and **RFT** methods and when to use each. *(Priority: Medium)*
2. Re-verify the portal fine-tuning navigation and add a "verified on" date. *(Priority: Low)*

---

## Lab 06 — Prompt Engineering

**Files reviewed:** `README.md`, `Prompt Engineering.ipynb`.

**Accuracy findings**
- README instructs launching the notebook from a hard-coded path `C:/Users/Admin/Desktop/LABS/Lab 06 - Prompt Engineering` — will not match the learner's checkout. Use a relative path. 
- "Additional Resources" links to `ai-services/openai/concepts/prompt-engineering` and `advanced-prompt-engineering` — verify these still resolve (the Azure OpenAI docs have been reorganized under `ai-foundry/openai/`). Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering
- The 8 techniques (zero/few-shot, CoT, meta, chaining, ToT, RAG, active-prompt) are accurate and well described. ✅

**Quality findings**
- Strong conceptual content; clear "when to use" guidance per technique.
- Replace the absolute path; otherwise high quality.

**Relevance findings**
- No coverage of **reasoning models (o-series)** prompting differences (where CoT is internalized and explicit CoT can hurt) — a meaningful current gap (see Advisor).

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Replace the hard-coded `C:/Users/Admin/...` path with a relative path. *(Priority: High — usability)*
2. Add a short section on prompting **reasoning models** (o-series / GPT-5 reasoning). *(Priority: Medium)*
3. Re-verify the Microsoft Learn links (docs moved under `ai-foundry/openai`). *(Priority: Low)*

---

## Lab 07 — Responsible AI (RAI)

**Files reviewed:** `README.md` (Evaluations, Manual & Automated Evaluation, Content Safety, PII, Prompt Shields, System Message), `rai_md_img/`, `Files/Evaluations/automated_evaluation.jsonl`.

**Accuracy findings**
- Hard-coded local path `C:/Users/Admin/Desktop/LABS/Lab 07- RAI/Files/Evaluations` — replace with a relative path.
- Portal navigation uses "Protect and govern" → "Evaluation" and "Guardrails + controls" → "Try it out". These labels match the current Foundry portal but are UI-drift-prone; verify and date them. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach
- Risk & safety evaluators (Groundedness, Hateful/unfair, Self-harm, Sexual, Protected material, Indirect attack) match the current Foundry catalog. ✅ Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-metrics-built-in
- Prompt Shields (jailbreak/indirect attack) is current Content Safety functionality. ✅ Source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection

**Quality findings**
- Comprehensive coverage of RAI surface; the system-message authoring guide is a nice touch.
- Mix of portal screenshots + JSONL datasets; replace hard-coded paths and date the screenshots.

**Relevance findings**
- Strong alignment with current Responsible AI tooling. Could add **continuous online evaluation** and **agent evaluators** (see Advisor).

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Replace hard-coded `C:/Users/Admin/...` dataset path with a relative path. *(Priority: High — usability)*
2. Date/verify portal navigation labels. *(Priority: Low)*
3. Add optional **continuous/online evaluation** section. *(Priority: Medium)*

---

## Lab 08 — RAG Patterns (GraphRAG)

**Files reviewed:** `GraphRAG/README.md` (install, init, index, global/local/DRIFT queries, prompt-tuning, Accelerator notes).

**Accuracy findings**
- Embedding model options are `text-embedding-ada-002` or `text-embedding-3-small`; prefer leading with `text-embedding-3-small`. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
- `api_version: 2024-05-01-preview` is hard-coded into `settings.yaml`; this will age — call out that learners should use a current API version. 
- **DRIFT query and reindex are flagged "not working as of GraphRAG v2.7.0."** This is honestly disclosed but leaves the lab partially non-functional; track the upstream fix and re-enable. Source: https://microsoft.github.io/graphrag/
- The lab correctly notes the **GraphRAG Accelerator is a public archived repo (FY26)** and CSA-driven — accurate and appropriately caveated. ✅ Source: https://github.com/Azure-Samples/graphrag-accelerator

**Quality findings**
- Clear Cloud Shell-based flow; `sed` commands are reproducible. The honest "not working" callouts are good practice.
- Pins are loose (`pip install graphrag`); pin a known-good version to avoid the DRIFT breakage moving target.

**Relevance findings**
- GraphRAG is relevant, but the workshop does not cover **Azure AI Search agentic retrieval / knowledge sources**, now Microsoft's first-party RAG direction. Opportunity (see Advisor).

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Pin a known-good `graphrag` version and revisit DRIFT/reindex once upstream-fixed. *(Priority: Medium)*
2. Lead with `text-embedding-3-small`; parameterize the API version. *(Priority: Low)*
3. Add a comparison/option for **Azure AI Search agentic retrieval**. *(Priority: Medium)*

---

## Lab 09 — Security (AI Red Teaming Agent)

**Files reviewed:** `README.md`, red-teaming notebook(s).

**Accuracy findings**
- Uses `pip install azure-ai-evaluation[redteam]` and the `RedTeam` functionality with **PyRIT** attack strategies — current and correct. ✅ Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent
- Risk & safety categories (violence, hate/unfairness, sexual, self-harm) align with the built-in evaluators. ✅ Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-metrics-built-in
- `MODEL_API_VERSION="2024-12-01-preview"` and `MODEL_DEPLOYMENT_NAME="gpt-4o-mini"` are functional but will age; parameterize.
- `aka.ms/airedteamingagent-howtodoc` / `-conceptdoc` redirect links are fine.

**Quality findings**
- Excellent structure (objective, risk categories, attack strategies, complexity levels, analysis features).
- Typos: "attach strategies"/"stragies" (should be "attack strategies"), "givean" in Lab 07 (shared author voice). Low impact, but fix for polish.

**Relevance findings**
- Among the most current labs; reflects the live AI Red Teaming Agent direction. ✅

**Overall rating:** ✅ Up to date

**Recommended actions**
1. Fix "attach/stragies" typos. *(Priority: Low)*
2. Parameterize the API version / model name. *(Priority: Low)*

---

## Lab 10 — Vector DB (Cosmos DB / PostgreSQL / SQL)

**Files reviewed:** `Cosmos DB/Readme.md` + `Python-Samples.ipynb`, `PostgreSQL/Readme.md`, `SQL/Readme.md` (+ notebooks).

**Accuracy findings**
- Cosmos DB lab teaches full-text, vector, and hybrid search — aligns with the current **Cosmos DB for NoSQL vector search (DiskANN)** capability. Confirm the notebook uses the GA vector indexing path and a v3 embedding model. Source: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/vector-search
- PostgreSQL lab should use **`pgvector` / DiskANN on Azure Database for PostgreSQL flexible server**; verify extension enablement steps. Source: https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-use-pgvector
- SQL lab: confirm it uses the **native `VECTOR` type / vector functions** in Azure SQL (now GA/preview depending on tier). Source: https://learn.microsoft.com/en-us/sql/relational-databases/vectors/vectors-sql-server

**Quality findings**
- READMEs are very thin ("open the notebook and follow the steps"); most instruction lives in notebooks. Add at least the prerequisites, embedding model, and expected outputs to each README for skimmability.
- "Pre-requisites: None. The database has been pre-created for you" assumes a hosted lab environment — state that explicitly for self-paced learners.

**Relevance findings**
- Covering three stores (Cosmos/PostgreSQL/SQL) is a strong, current comparison. ✅ Mention **Azure AI Search** as the fourth, integrated option for completeness.

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Flesh out each README (prereqs, embedding model, expected results). *(Priority: Medium)*
2. Verify each notebook uses GA vector paths + a v3 embedding model. *(Priority: Medium)*
3. Note the hosted-environment assumption for self-paced users. *(Priority: Low)*

---

## Optional Lab — AI Fundamentals (RAG; Semantic Kernel & AutoGen)

**Files reviewed:** `RAG/RAG.ipynb`, `SK and AutoGen/README.md`, `SK and AutoGen/SK and AutoGen.ipynb`.

**Accuracy findings**
- **AutoGen** is presented as Microsoft's multi-agent framework (v0.6+ API). Microsoft has since converged AutoGen and Semantic Kernel into the **Microsoft Agent Framework**. AutoGen still works, but the lab should note the convergence and point to the Agent Framework as the go-forward path. Source: https://learn.microsoft.com/en-us/agent-framework/
- The RAG notebook describes "Azure AI Foundry ... Launched in 2024 ... Model Catalog with over 200 pre-trained models" as in-notebook sample data — fine as sample text, but ensure it isn't presented as current product fact (the catalog is now 11,000+ models). Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview
- Semantic Kernel content (kernel init, plugins, `KernelArguments`) is accurate for current SK. ✅ Source: https://learn.microsoft.com/en-us/semantic-kernel/

**Quality findings**
- Rich, well-structured comparison of SK vs AutoGen with concrete use cases. ✅
- **Broken cross-reference:** "Next Steps" says "proceed to Lab 5, where you'll explore RAG" — but RAG is in this Optional Lab and Lab 05 is Fine-Tuning. Fix the forward pointer.

**Relevance findings**
- Multi-agent fundamentals remain relevant; reframing around the **Microsoft Agent Framework** would modernize it (see Advisor).

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add a note that AutoGen + SK now converge in the **Microsoft Agent Framework**; link it. *(Priority: Medium)*
2. Fix the "proceed to Lab 5" mis-reference. *(Priority: Low)*
3. Clarify the in-notebook "200 models / launched 2024" text is sample data. *(Priority: Low)*

---

## Appendix — Sources

- Azure AI Projects client library (Python) v2.2.0 — https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- Microsoft Foundry Models overview — https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview
- Foundry Agent Service overview — https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview
- Azure AI Evaluation SDK — https://learn.microsoft.com/python/api/azure-ai-evaluation/azure.ai.evaluation
- Built-in evaluation metrics — https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-metrics-built-in
- AI Red Teaming Agent — https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent
- Fine-tuning in Azure AI Foundry — https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning
- GraphRAG getting started — https://microsoft.github.io/graphrag/
- Cosmos DB vector search — https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/vector-search
- Microsoft Agent Framework — https://learn.microsoft.com/en-us/agent-framework/
