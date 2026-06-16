# Workshop Review — Consolidated Report
## WPLUS Azure AI Platform and Services

**Review date:** 2026-06-09
**Scope:** Full workshop — Lab 00 through Lab 10 plus the Optional Lab (AI Fundamentals)
**Orchestrated by:** Workshop Review Orchestrator

**Subagents run**
| Subagent | Status | Source report |
|----------|--------|---------------|
| Lab Content Evaluator | ✅ Completed | [evaluation/lab-content-evaluation.md](lab-content-evaluation.md) |
| Foundry Feature Advisor | ✅ Completed | [evaluation/foundry-feature-suggestions.md](foundry-feature-suggestions.md) |

This consolidated report reproduces the Evaluator's complete per-lab detail and folds in the Advisor's per-lab feature recommendations, so it can be acted on without opening the two source reports. All Microsoft Learn citations from both reports are preserved.

---

## 1. Executive Summary

The workshop is **broadly healthy and well-structured** — every lab follows a consistent, professional template (Objectives, Scenario, Prerequisites, Tasks, Execution, Expected Results, Resources) and covers a strong, current breadth of Azure AI / Microsoft Foundry topics. The labs that are closest to code (Lab 09 Security) are the most current; the labs anchored to a **pinned beta SDK** (Lab 01) and to **hard-coded local paths** (Labs 06, 07) carry the most risk.

**One blocking, workshop-wide issue dominates the priority list:** Lab 01 pins the **beta** `azure-ai-projects>=1.0.0b12`, but the package is **GA at v2.2.0** (Microsoft Foundry SDK, updated 2026-06-01). The b12 → 2.x gap is breaking (agents surface, `get_openai_client()`, Responses API) and the labs still teach the **deprecated `PROJECT_CONNECTION_STRING`** auth instead of the **Foundry project endpoint URL + Entra ID** pattern. Fixing this unblocks correct, durable patterns across Labs 01, 02, and 09.

The biggest forward-looking opportunities are to modernize the **agents** story (connected/multi-agent, MCP, Bing grounding, tracing), the **RAG** story (Azure AI Search agentic retrieval alongside GraphRAG), and **prompting/fine-tuning** (reasoning models; DPO/RFT/distillation).

### Summary table

| Lab | Evaluator rating | Headline issue | Top feature opportunity | Combined priority |
|-----|:---:|----------------|-------------------------|:---:|
| Lab 00 – Prerequisites | ⚠️ | Legacy `ada-002`; "Prequisite" typo; no Entra-ID note | Model router deploy + Entra ID auth | Medium |
| Lab 01 – AI Foundry | ❌ | **Beta SDK pin (b12); GA is 2.2.0**; deprecated conn-string auth | Foundry SDK v2.x + Responses API | **High** |
| Lab 02 – Agents | ⚠️ | Tool imports vs GA SDK; dated `gpt-4o-mini` | Connected/multi-agent + MCP + Bing + tracing | High |
| Lab 03 – AI Language | ⚠️ | API-key flow; portal/Logic Apps screenshot drift | Keyless (Entra ID) auth option | Medium |
| Lab 04 – AI Vision | ⚠️ | Face Limited Access; Image Analysis 4.0; VI churn | LLM-vision vs Image Analysis 4.0 note | Medium |
| Lab 05 – Fine-Tuning | ⚠️ | SFT-only; portal drift | DPO / RFT / distillation | Medium |
| Lab 06 – Prompt Engineering | ⚠️ | Hard-coded `C:/Users/Admin/...` path | Reasoning-model prompting | High |
| Lab 07 – Responsible AI | ⚠️ | Hard-coded local path; portal nav drift | Continuous/online eval + Content Safety in code | High |
| Lab 08 – RAG (GraphRAG) | ⚠️ | DRIFT "not working v2.7.0"; `ada-002`; pinned api-version | Azure AI Search agentic retrieval | Medium |
| Lab 09 – Security | ✅ | Minor typos ("attach"/"stragies") | Content Safety SDK guardrails | Low |
| Lab 10 – Vector DB | ⚠️ | Thin READMEs; verify GA vector paths | Azure AI Search integrated vectorization | Medium |
| Optional – AI Fundamentals | ⚠️ | AutoGen superseded; "proceed to Lab 5" mis-ref | Microsoft Agent Framework | Medium |

### Cross-cutting issues (span multiple labs)
- **Beta SDK & deprecated auth** — `azure-ai-projects` beta pin and `PROJECT_CONNECTION_STRING` (Labs 01, 02, 09). GA is v2.2.0 with Entra-ID-only auth via the project endpoint URL. Source: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- **Hard-coded local paths** — `C:/Users/Admin/Desktop/...` (Labs 06, 07; a leaked path in a Lab 01 notebook output).
- **Legacy embedding model** — `text-embedding-ada-002` (Labs 00, 08); prefer `text-embedding-3-small`/`-large`.
- **Dated default model** — `gpt-4o-mini` default (Labs 02, 08, 09); refresh to `gpt-4.1-mini` or model router.
- **Naming/spelling** — "Prequisite" folder, "Lab 07- RAI" spacing, "attach/stragies" typos.
- **Portal-UI drift** — image-heavy portal labs (03, 04, 05, 07) need "verified on <date>" callouts.

---

## 2. Per-Lab Detailed Sections

### Lab 00 — Prerequisites: AI Foundry Resource Creation

**Files reviewed:** `01-Create-Azure-Foundry-Project.md`, `02-Deploy-Models.md`, `03-Connect-to-Bing-Resources.md`, `04-Connect-to-Azure-AI-Search.md`, `05-Setup-(dot)env-file.md`, `06-Run-requirements.md`, `images/`.

**Accuracy findings**
- Deploys `text-embedding-ada-002` alongside `text-embedding-3-large`. `ada-002` is legacy; prefer the v3 family unless required downstream (Lab 08 references it). Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
- Chat models are `GPT-4o` / `GPT-4o-mini`; the catalog now leads with GPT-4.1, o-series, and GPT-5-class models. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview
- Portal flow (Model catalog → Use this model → Deploy) matches the current Foundry UI. ✅

**Quality findings**
- "Prequisite" folder is misspelled and propagates into cross-lab links. Otherwise clear, well-screenshotted, good time estimates; root `.env` is well centralized.

**Relevance findings**
- Bing + Azure AI Search connections remain the recommended grounding connections. ✅
- No first-class **Entra-ID auth / RBAC role assignment** step — recommended since key auth is being phased out in the SDK.

**Feature enhancement opportunities (Advisor)**
- **Model router (GA)** — add a "Deploy model router" step so later labs can target it for automatic cost/quality optimization. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/model-router

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Replace/annotate `ada-002` → `text-embedding-3-small`/`-large` (cross-note Lab 08). *(Evaluator — Medium)*
2. Add an "assign Azure AI User / Developer role; use Entra ID" step. *(Evaluator — Medium)*
3. Add a "Deploy model router" optional step. *(Advisor — Medium)*
4. Fix the "Prequisite" folder spelling and dependent links. *(Evaluator — Low)*

---

### Lab 01 — AI Foundry (Connection with AOAI + Evaluations)

**Files reviewed:** `Labs/Connection with AOAI/README.md`, `Labs/Connection with AOAI/setup and quick_start.ipynb`, `Labs/Evaluations/README.md`, `Labs/Evaluations/1-evaluation.ipynb`.

**Accuracy findings**
- Requires **`azure-ai-projects>=1.0.0b12`** (beta). GA is **v2.2.0** (Microsoft Foundry SDK, updated 2026-06-01); the gap is breaking (agents surface, `.get_openai_client()`, Responses API). Source: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- Mixes deprecated `PROJECT_CONNECTION_STRING` with `AI_FOUNDRY_PROJECT_ENDPOINT`. Current pattern: `AIProjectClient(endpoint=<project endpoint URL>, credential=DefaultAzureCredential())` — "Entra ID is the only authentication method currently supported by the client." Source: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- Evaluations notebook uses `azure-ai-evaluation` (`F1Score`, `Relevance`, cloud `Evaluation`/`InputDataset`) — current; verify import paths against the latest release. Source: https://learn.microsoft.com/python/api/azure-ai-evaluation/azure.ai.evaluation
- A committed notebook output embeds an absolute path `C:\Users\Admin\Desktop\WPLUS-...` — clear it.

**Quality findings**
- READMEs are well-structured (Objectives, Scenario, Tasks, Execution, Troubleshooting). ✅
- `InteractiveBrowserCredential`/`DefaultAzureCredential` fallback chain is reasonable — align with the documented `DefaultAzureCredential` default.
- Committed notebook outputs inflate files and leak a local path.

**Relevance findings**
- Local + cloud evaluation is the current recommended Foundry observability pattern. ✅
- Missing newer evaluators (Groundedness Pro, agentic/intent-resolution, risk & safety).

**Feature enhancement opportunities (Advisor)**
- **Foundry SDK v2.x + Responses API (GA)** — adopt `get_openai_client()` + Responses (`previous_response_id`). Source: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- **Model router (GA)** — use the router deployment instead of a hard-coded model. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/model-router
- **Agent evaluators + continuous/online evaluation (GA/Preview)** — evaluate trajectories and monitor deployed apps. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/online-evaluation

**Overall rating:** ❌ Needs significant rework

**Recommended actions**
1. Bump to **`azure-ai-projects==2.2.0`** and migrate to endpoint + `DefaultAzureCredential` + `get_openai_client()`. *(Both — High)*
2. Remove all `PROJECT_CONNECTION_STRING` usage. *(Evaluator — High)*
3. Add a Responses API cell and (optionally) target the model router. *(Advisor — High)*
4. Add agent + online evaluation examples. *(Advisor — Medium)*
5. Clear committed notebook outputs / leaked local path; verify `azure-ai-evaluation` imports. *(Evaluator — Low/Medium)*

---

### Lab 02 — Agents

**Files reviewed:** `README.md`, `1-basics.ipynb`, `3-file-search.ipynb` (and sibling notebooks), `Files/`.

**Accuracy findings**
- `project_client.agents.create_agent(...)` is current under the Foundry Agent Service, but the GA SDK (2.x) expanded the agents surface and tool catalog — verify `FileSearchTool`/`CodeInterpreterTool` import paths against v2.2.0. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview
- Default `gpt-4o-mini` is dated; consider GPT-4.1-mini / model router. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview
- Vector store + `FileSearchTool` usage is valid; confirm the creation call signature in the GA SDK.

**Quality findings**
- Strong domain framing, clear disclaimers, good RBAC notes (Azure AI Developer, Storage Blob Data Contributor, Cognitive Search Data Contributor). ✅
- "Next Steps" point to OpenTelemetry/Azure Monitor and function calling — good.

**Relevance findings**
- Single-agent + tools is a solid foundation but omits multi-agent/connected agents and newer tools (MCP, Bing grounding, Logic Apps/OpenAPI) now central to the Agent Service.

**Feature enhancement opportunities (Advisor)**
- **Connected / multi-agent orchestration (GA/Preview)** — add `4-connected-agents.ipynb` (triage→specialist). Source: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/connected-agents
- **MCP tool (Preview)** — connect an agent to an external MCP server. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/model-context-protocol
- **Grounding with Bing Search (GA)** — live web grounding using the Lab 00 Bing connection. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/bing-grounding
- **Tracing / observability (GA/Preview)** — a concrete OpenTelemetry trace cell. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Re-verify all agent/tool imports against `azure-ai-projects` 2.2.0. *(Evaluator — High)*
2. Add a connected/multi-agent notebook + MCP and Bing grounding examples. *(Advisor — High)*
3. Refresh default model to GPT-4.1-mini or model router. *(Both — Medium)*
4. Add a tracing-enabled run shown in the portal. *(Advisor — Medium)*

---

### Lab 03 — AI Language

**Files reviewed:** `README.md`, `Images/`, advanced translation + PII Logic Apps sections.

**Accuracy findings**
- Uses Language resource **API key + endpoint** from the Foundry Overview page — supported, but Microsoft steers toward Entra ID / keyless auth; add a keyless note. Source: https://learn.microsoft.com/en-us/azure/ai-services/authentication
- Translation/PII via **Logic Apps as an agent tool** is a valid current pattern; portal/Logic Apps screenshots drift. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/logic-apps

**Quality findings**
- Long but well-sequenced checklist; image-heavy (higher maintenance). Helpful same-subscription/resource-group troubleshooting note.

**Relevance findings**
- PII detection/redaction and translation remain core Language scenarios. ✅ Consider adding conversational PII/summarization skills.

**Feature enhancement opportunities (Advisor)**
- **Keyless (Entra ID) auth option** — align with the workshop-wide auth modernization. Source: https://learn.microsoft.com/en-us/azure/ai-services/authentication

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add a keyless (Entra ID) auth option alongside the API key flow. *(Both — Medium)*
2. Add an image "last verified" date / UI-drift callout. *(Evaluator — Low)*

---

### Lab 04 — AI Vision

**Files reviewed:** `README.md` (Exercises 1–5: provisioning, Face analysis, OCR, Image Analysis, Video Indexer).

**Accuracy findings**
- **Face API** features are under **Limited Access / gated** approval; state the gating and application requirement. Source: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/identity-limited-access
- OCR/Image Analysis should use **Image Analysis 4.0** (Read + captioning/tags); confirm it isn't legacy v3.x. Source: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis
- **Video Indexer** API surface changes periodically; verify endpoints/account-access-token flow. Source: https://learn.microsoft.com/en-us/azure/azure-video-indexer/

**Quality findings**
- Good exercise progression; ensure each exercise names the exact package/endpoint.

**Relevance findings**
- Vision remains relevant; multimodal LLM vision (GPT-4o) now overlaps classic OCR/Image Analysis.

**Feature enhancement opportunities (Advisor)**
- **LLM-vision vs Image Analysis 4.0 decision note (GA)** — help learners choose by cost/structure/gating. Source: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add the Face **Limited Access** gating note + application link. *(Evaluator — Medium)*
2. Confirm Image Analysis **4.0** usage; update legacy v3.x calls. *(Evaluator — Medium)*
3. Re-verify the Video Indexer auth/endpoint flow. *(Evaluator — Medium)*
4. Add an "LLM vision vs Image Analysis 4.0" note. *(Advisor — Low)*

---

### Lab 05 — Fine-Tuning

**Files reviewed:** `README.md`, `Advance Fine-Tuning/README.MD`.

**Accuracy findings**
- Targets fine-tuning **GPT-4.1-mini** in the Foundry portal — a currently supported SFT base. ✅ Verify the portal "Fine-tuning" entry point. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning
- Teaches only **SFT**; Foundry also supports **DPO** and **RFT** — accurate but incomplete. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/fine-tuning-considerations

**Quality findings**
- Clear portal flow (sign in → portal → start → configure → review → deploy/test). Portal labs drift; add "verified on <date>".

**Relevance findings**
- Adding DPO/RFT and **distillation** would modernize the lab.

**Feature enhancement opportunities (Advisor)**
- **DPO / RFT / distillation (Preview/GA)** — add an "Advanced methods" section with selection guidance. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/fine-tuning-considerations

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add an optional **DPO / RFT / distillation** section. *(Advisor — Medium)*
2. Re-verify portal navigation; add a "verified on" date. *(Evaluator — Low)*

---

### Lab 06 — Prompt Engineering

**Files reviewed:** `README.md`, `Prompt Engineering.ipynb`.

**Accuracy findings**
- README launches the notebook from a hard-coded `C:/Users/Admin/Desktop/LABS/Lab 06 - Prompt Engineering` — use a relative path.
- "Additional Resources" link to `ai-services/openai/concepts/prompt-engineering`; the docs moved under `ai-foundry/openai/` — re-verify. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering
- The 8 techniques (zero/few-shot, CoT, meta, chaining, ToT, RAG, active-prompt) are accurate. ✅

**Quality findings**
- Strong conceptual content with clear "when to use" guidance. Replace the absolute path; otherwise high quality.

**Relevance findings**
- No coverage of **reasoning models** prompting (where explicit CoT can hurt) — a meaningful gap.

**Feature enhancement opportunities (Advisor)**
- **Reasoning models (o-series / GPT-5 reasoning) prompting (GA)** — add a side-by-side section. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reasoning

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Replace the hard-coded `C:/Users/Admin/...` path with a relative path. *(Evaluator — High, usability)*
2. Add a "Prompting reasoning models" section. *(Advisor — Medium)*
3. Re-verify the Microsoft Learn links (docs moved under `ai-foundry/openai`). *(Evaluator — Low)*

---

### Lab 07 — Responsible AI (RAI)

**Files reviewed:** `README.md` (Evaluations, Manual & Automated Evaluation, Content Safety, PII, Prompt Shields, System Message), `rai_md_img/`, `Files/Evaluations/automated_evaluation.jsonl`.

**Accuracy findings**
- Hard-coded local path `C:/Users/Admin/Desktop/LABS/Lab 07- RAI/Files/Evaluations` — use a relative path.
- Portal nav ("Protect and govern" → "Evaluation"; "Guardrails + controls" → "Try it out") matches the current Foundry portal but is drift-prone; verify and date. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach
- Risk & safety evaluators (Groundedness, Hateful/unfair, Self-harm, Sexual, Protected material, Indirect attack) match the current catalog. ✅ Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-metrics-built-in
- Prompt Shields (jailbreak/indirect attack) is current Content Safety functionality. ✅ Source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection

**Quality findings**
- Comprehensive RAI coverage; the system-message authoring guide is a plus. Replace hard-coded paths; date the screenshots.

**Relevance findings**
- Strong alignment with current RAI tooling; could add continuous/online evaluation and agent evaluators.

**Feature enhancement opportunities (Advisor)**
- **Continuous / online evaluation (GA/Preview)** — monitor a deployed app. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/online-evaluation
- **Content Safety in code — Prompt Shields + groundedness detection (GA)** — programmatic guardrails beyond the portal. Source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Replace hard-coded `C:/Users/Admin/...` dataset path with a relative path. *(Evaluator — High, usability)*
2. Add an SDK Content Safety (Prompt Shields + groundedness) cell. *(Advisor — Medium)*
3. Add an optional continuous/online evaluation section. *(Advisor — Medium)*
4. Date/verify portal navigation labels. *(Evaluator — Low)*

---

### Lab 08 — RAG Patterns (GraphRAG)

**Files reviewed:** `GraphRAG/README.md` (install, init, index, global/local/DRIFT queries, prompt-tuning, Accelerator notes).

**Accuracy findings**
- Embedding options `text-embedding-ada-002` or `text-embedding-3-small`; lead with v3. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
- `api_version: 2024-05-01-preview` is hard-coded into `settings.yaml`; will age — call out using a current version.
- **DRIFT query and reindex are flagged "not working as of GraphRAG v2.7.0"** — honestly disclosed but leaves the lab partially non-functional; track the upstream fix. Source: https://microsoft.github.io/graphrag/
- Correctly notes the **GraphRAG Accelerator is a public archived repo (FY26)**, CSA-driven. ✅ Source: https://github.com/Azure-Samples/graphrag-accelerator

**Quality findings**
- Clear Cloud Shell flow; reproducible `sed` commands; honest "not working" callouts. Pins are loose (`pip install graphrag`) — pin a known-good version.

**Relevance findings**
- GraphRAG is relevant but omits **Azure AI Search agentic retrieval / knowledge sources**, now Microsoft's first-party RAG direction.

**Feature enhancement opportunities (Advisor)**
- **Agentic retrieval / knowledge sources (Preview/GA)** — add a first-party RAG section contrasted with GraphRAG. Source: https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-concept

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Pin a known-good `graphrag` version; revisit DRIFT/reindex when upstream-fixed. *(Evaluator — Medium)*
2. Add an **Azure AI Search agentic retrieval** comparison. *(Advisor — Medium)*
3. Lead with `text-embedding-3-small`; parameterize the API version. *(Evaluator — Low)*

---

### Lab 09 — Security (AI Red Teaming Agent)

**Files reviewed:** `README.md`, red-teaming notebook(s).

**Accuracy findings**
- Uses `pip install azure-ai-evaluation[redteam]` + the `RedTeam` functionality with **PyRIT** strategies — current and correct. ✅ Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent
- Risk & safety categories align with built-in evaluators. ✅ Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-metrics-built-in
- `MODEL_API_VERSION="2024-12-01-preview"` / `gpt-4o-mini` are functional but will age — parameterize.

**Quality findings**
- Excellent structure (objective, risk categories, attack strategies, complexity levels, analysis features). Typos: "attach strategies"/"stragies".

**Relevance findings**
- Among the most current labs; reflects the live AI Red Teaming Agent direction. ✅

**Feature enhancement opportunities (Advisor)**
- **Content Safety SDK guardrails (GA)** — tie red-teaming findings to programmatic Prompt Shields/groundedness mitigations. Source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection

**Overall rating:** ✅ Up to date

**Recommended actions**
1. Fix "attach/stragies" typos. *(Evaluator — Low)*
2. Parameterize API version / model name. *(Evaluator — Low)*
3. Add a Content Safety SDK mitigation example. *(Advisor — Low)*

---

### Lab 10 — Vector DB (Cosmos DB / PostgreSQL / SQL)

**Files reviewed:** `Cosmos DB/Readme.md` + `Python-Samples.ipynb`, `PostgreSQL/Readme.md`, `SQL/Readme.md` (+ notebooks).

**Accuracy findings**
- Cosmos DB teaches full-text, vector, and hybrid search — aligns with **Cosmos DB for NoSQL vector search (DiskANN)**; confirm GA vector indexing + a v3 embedding model. Source: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/vector-search
- PostgreSQL should use **`pgvector` / DiskANN on Flexible Server**; verify extension enablement. Source: https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-use-pgvector
- SQL should use the **native `VECTOR` type / vector functions** in Azure SQL. Source: https://learn.microsoft.com/en-us/sql/relational-databases/vectors/vectors-sql-server

**Quality findings**
- READMEs are very thin ("open the notebook"); add prerequisites, embedding model, and expected outputs per README. State the hosted-environment assumption ("database pre-created").

**Relevance findings**
- Three stores is a strong comparison. ✅ Mention **Azure AI Search** as the integrated fourth option.

**Feature enhancement opportunities (Advisor)**
- **Azure AI Search integrated vectorization (GA)** — optional 4th store with built-in chunking + embedding. Source: https://learn.microsoft.com/en-us/azure/search/vector-search-integrated-vectorization

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Flesh out each README (prereqs, embedding model, expected results). *(Evaluator — Medium)*
2. Verify each notebook uses GA vector paths + a v3 embedding model. *(Evaluator — Medium)*
3. Add an optional Azure AI Search integrated-vectorization notebook. *(Advisor — Low)*
4. Note the hosted-environment assumption for self-paced users. *(Evaluator — Low)*

---

### Optional Lab — AI Fundamentals (RAG; Semantic Kernel & AutoGen)

**Files reviewed:** `RAG/RAG.ipynb`, `SK and AutoGen/README.md`, `SK and AutoGen/SK and AutoGen.ipynb`.

**Accuracy findings**
- **AutoGen** (v0.6+ API) is presented as the multi-agent framework; Microsoft has since converged AutoGen + Semantic Kernel into the **Microsoft Agent Framework** — note the convergence. Source: https://learn.microsoft.com/en-us/agent-framework/
- The RAG notebook's "Foundry launched 2024 / 200+ models" is in-notebook sample text — ensure it isn't read as current product fact (catalog is now 11,000+). Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview
- Semantic Kernel content (kernel init, plugins, `KernelArguments`) is accurate. ✅ Source: https://learn.microsoft.com/en-us/semantic-kernel/

**Quality findings**
- Rich SK-vs-AutoGen comparison with concrete use cases. ✅
- **Broken cross-reference:** "Next Steps" says "proceed to Lab 5, where you'll explore RAG" — RAG is in this Optional Lab; Lab 05 is Fine-Tuning.

**Relevance findings**
- Multi-agent fundamentals remain relevant; reframing around the Agent Framework modernizes it.

**Feature enhancement opportunities (Advisor)**
- **Microsoft Agent Framework (GA/Preview)** — add a closing section mapping SK/AutoGen concepts onto it. Source: https://learn.microsoft.com/en-us/agent-framework/

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add a note that AutoGen + SK converge in the **Microsoft Agent Framework**; link it. *(Both — Medium)*
2. Fix the "proceed to Lab 5" mis-reference. *(Evaluator — Low)*
3. Clarify the in-notebook "200 models / launched 2024" text is sample data. *(Evaluator — Low)*

---

## 3. Feature Enhancement Opportunities (Consolidated)

### Top Recommendations

| Feature | Target lab | Status | Priority | One-line benefit |
|---------|-----------|--------|----------|------------------|
| Foundry SDK `azure-ai-projects` v2.x + Responses API | Lab 01 | GA | High | Supported, non-beta SDK + Responses API |
| Model router | Lab 00 / Lab 01 | GA | High | Auto cost/quality optimization |
| Reasoning models (o-series / GPT-5) + prompting | Lab 06 | GA | High | Correct prompting for internally-reasoning models |
| Connected / multi-agent orchestration | Lab 02 | GA/Preview | High | Real-world multi-agent patterns |
| MCP tool for agents | Lab 02 | Preview | High | Standard external tool/data integration |
| Agentic retrieval / knowledge sources | Lab 08 | Preview/GA | High | First-party RAG vs hand-rolled GraphRAG |
| Grounding with Bing Search (agent tool) | Lab 02 | GA | Medium | Live web grounding in agents |
| Agent evaluators + continuous evaluation | Lab 01 / Lab 07 | GA/Preview | Medium | Trajectory eval + production monitoring |
| RFT/DPO fine-tuning + distillation | Lab 05 | Preview/GA | Medium | Modern tuning beyond SFT |
| Microsoft Agent Framework | Optional Lab | GA/Preview | Medium | Go-forward multi-agent framework |
| Foundry observability / tracing (OTel) | Lab 02 / Lab 01 | GA/Preview | Medium | Production agent debugging |
| Content Safety in code (Prompt Shields + groundedness) | Lab 07 / Lab 09 | GA | Medium | Programmatic guardrails |
| Multimodal vision vs classic Vision note | Lab 04 | GA | Low | Tool-selection guidance |
| Azure AI Search integrated vectorization | Lab 10 | GA | Low | Completes the store comparison |

### High-priority features — detail

- **Foundry SDK v2.x + Responses API (GA).** Adopting `azure-ai-projects` v2.2.0 with `AIProjectClient(endpoint=..., credential=DefaultAzureCredential())` and `.get_openai_client()` lets learners use the stateful Responses API (`previous_response_id`) that underpins modern agents. This is also the fix for Lab 01's blocking beta pin. Source: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- **Model router (GA).** A single router deployment auto-selects the best/cheapest model per prompt — a frequent customer cost lever — with no app changes. Learners stop hard-coding `gpt-4o-mini`. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/model-router
- **Reasoning models + prompting (GA).** o-series / GPT-5 reasoning models reason internally; forcing explicit CoT can hurt. A Lab 06 section teaches when to use reasoning models and how their prompting differs. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reasoning
- **Connected / multi-agent orchestration (GA/Preview).** A primary agent delegating to specialists is the dominant production pattern; a `4-connected-agents.ipynb` is a natural progression from Lab 02's single agent. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/connected-agents
- **MCP tool (Preview).** Teaching the Model Context Protocol tool future-proofs the agents lab against the emerging standard integration layer. Source: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/model-context-protocol
- **Agentic retrieval / knowledge sources (Preview/GA).** Azure AI Search agentic retrieval decomposes queries into parallel subqueries and returns grounded results — Microsoft's first-party, lower-maintenance RAG path to contrast with GraphRAG. Source: https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-concept

### Proposed new labs
- **Agentic RAG with Azure AI Search** — first-party counterpart to GraphRAG (could nest under Lab 08).
- **Multi-Agent Orchestration** — connected agents + MCP + tracing, building on Lab 02.

---

## 4. Unified Action Plan

| # | Action | Target lab | Source | Priority | Effort |
|---|--------|-----------|--------|----------|--------|
| 1 | Bump `azure-ai-projects` b12 → **2.2.0** and migrate to endpoint + `DefaultAzureCredential` + `get_openai_client()` | Lab 01 | Both | High | Med |
| 2 | Remove all `PROJECT_CONNECTION_STRING` usage (endpoint + Entra ID only) | Labs 01, 02, 09 | Evaluator | High | Med |
| 3 | Replace hard-coded `C:/Users/Admin/...` paths with relative paths | Labs 06, 07 | Evaluator | High | Low |
| 4 | Re-verify agent/tool imports vs GA SDK; refresh default model to GPT-4.1-mini / model router | Lab 02 | Both | High | Med |
| 5 | Add connected/multi-agent notebook (+ MCP, Bing grounding) | Lab 02 | Advisor | High | High |
| 6 | Add Responses API cell; optionally target model router | Lab 01 | Advisor | High | Med |
| 7 | Add reasoning-model prompting section | Lab 06 | Advisor | High | Med |
| 8 | Add Azure AI Search agentic retrieval section/comparison | Lab 08 | Advisor | Medium | High |
| 9 | Add agent + continuous/online evaluation examples | Labs 01, 07 | Advisor | Medium | Med |
| 10 | Add Content Safety SDK guardrails (Prompt Shields + groundedness) | Labs 07, 09 | Advisor | Medium | Med |
| 11 | Add DPO / RFT / distillation section | Lab 05 | Advisor | Medium | Med |
| 12 | Add "Deploy model router" step + Entra ID/RBAC step | Lab 00 | Both | Medium | Low |
| 13 | Add keyless (Entra ID) auth option | Lab 03 | Both | Medium | Low |
| 14 | Face Limited Access note; confirm Image Analysis 4.0; verify Video Indexer flow | Lab 04 | Evaluator | Medium | Med |
| 15 | Pin known-good `graphrag`; lead with v3 embeddings; parameterize api-version | Lab 08 | Evaluator | Medium | Low |
| 16 | Flesh out Vector-DB READMEs; verify GA vector paths + v3 embeddings | Lab 10 | Evaluator | Medium | Med |
| 17 | Note AutoGen/SK → Microsoft Agent Framework convergence; fix "Lab 5" mis-ref | Optional Lab | Both | Medium | Low |
| 18 | Replace legacy `text-embedding-ada-002` with v3 family | Labs 00, 08 | Evaluator | Medium | Low |
| 19 | Clear committed notebook outputs / leaked local path | Lab 01 | Evaluator | Low | Low |
| 20 | Fix typos ("Prequisite", "attach/stragies"); date portal screenshots | Labs 00, 03, 04, 05, 07, 09 | Evaluator | Low | Low |
| 21 | Add LLM-vision vs Image Analysis 4.0 note | Lab 04 | Advisor | Low | Low |
| 22 | Add Azure AI Search integrated vectorization notebook | Lab 10 | Advisor | Low | Med |
| 23 | Add tracing/observability run | Lab 02 | Advisor | Medium | Med |

---

## 5. Overlaps & Conflicts

**Reinforcing overlaps (fix-it meets add-it):**
- **Lab 01 SDK.** Evaluator flags the beta pin/deprecated auth; Advisor recommends adopting Foundry SDK v2.x + Responses API. **Same change** — do the upgrade once and it satisfies both. *(Highest-value single action.)*
- **Lab 02 model & imports.** Evaluator wants imports re-verified and the dated `gpt-4o-mini` refreshed; Advisor wants multi-agent/MCP/Bing built on the GA SDK. Sequence: fix the SDK/model first, then layer the new agent features.
- **Lab 00 auth.** Evaluator wants an Entra ID/RBAC step; Advisor wants model router. Both land in the same "modernize prerequisites" edit.
- **Lab 07/09 safety.** Evaluator notes portal-only RAI demos; Advisor recommends Content Safety in code — together they upgrade RAI from demo to production-ready.
- **Lab 08 RAG.** Evaluator flags broken DRIFT + legacy embeddings; Advisor adds agentic retrieval — keep GraphRAG but position agentic retrieval as the first-party alternative.

**Conflicts (and resolutions):**
- **Keep vs replace GraphRAG.** No true conflict: **keep** GraphRAG (it teaches graph-based concepts) and **add** agentic retrieval as a complementary, lower-maintenance path. Recommendation: present both, label GraphRAG's DRIFT limitation.
- **Embedding model in Lab 08.** Evaluator says lead with `text-embedding-3-small`, but Lab 00 still deploys `ada-002` for compatibility. Resolution: deploy a v3 embedding model in Lab 00 and use it in Lab 08; retain `ada-002` only if a specific dependency requires it, with a note.
- **`gpt-4o-mini` vs model router as default.** Resolution: introduce model router in Lab 00/01 as the recommended default, but keep an explicit model option for labs that need deterministic model behavior (e.g., red teaming in Lab 09).

---

## 6. Quick Wins (low-effort, high-value)

- Bump SDK pin `azure-ai-projects>=1.0.0b12` → `==2.2.0`. *(Lab 01)*
- Replace hard-coded `C:/Users/Admin/...` paths with relative paths. *(Labs 06, 07)*
- Refresh default model `gpt-4o-mini` → `gpt-4.1-mini` (or model router). *(Labs 02, 08, 09)*
- Lead with `text-embedding-3-small`/`-large`; retire/annotate `ada-002`. *(Labs 00, 08)*
- Fix typos: "Prequisite", "attach strategies"/"stragies". *(Labs 00, 09)*
- Fix the Optional Lab "proceed to Lab 5" mis-reference. *(Optional Lab)*
- Add a one-line "model router available" note. *(Lab 00)*
- Add a Face **Limited Access** gating note. *(Lab 04)*
- Note AutoGen/SK → Microsoft Agent Framework convergence. *(Optional Lab)*
- Clear committed notebook outputs / leaked local path. *(Lab 01)*

---

## 7. Source Reports

- Lab Content Evaluator — [evaluation/lab-content-evaluation.md](lab-content-evaluation.md)
- Foundry Feature Advisor — [evaluation/foundry-feature-suggestions.md](foundry-feature-suggestions.md)
