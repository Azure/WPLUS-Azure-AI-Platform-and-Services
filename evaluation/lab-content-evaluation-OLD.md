# Lab Content Evaluation — WPLUS Azure AI Platform and Services

- **Evaluation date:** 2026-06-09
- **Reviewer:** Lab Content Evaluator
- **Scope:** Lab 00 → Lab 10 (all instructional labs)
- **Primary references:** Microsoft Learn (Azure AI Foundry / Microsoft Foundry, Azure OpenAI models, evaluation metrics), GraphRAG docs.

> **Theme of this review:** The lab content is technically sound and pedagogically well organized, but it predates the **Azure AI Foundry → Microsoft Foundry** rebrand and the move from the classic **Assistants/Agents** pattern to the **Responses API / Agent Framework**. The dominant issues across the repo are (1) branding drift, (2) SDK version lag (pinned betas / `1.x` vs. current `2.x`), (3) the RBAC role rename (**Azure AI User → Foundry User**), (4) hard-coded local VM paths, and (5) naming/spelling inconsistencies. Most labs need only minor updates; a few are exemplary and current.

---

## Executive Summary

| Lab | Rating | Headline issue |
|-----|--------|----------------|
| Lab 00 — Prerequisite: AI Foundry Resource Creation | ⚠️ Needs minor updates | Branding ("Microsoft Foundry"); `images/dummy.md` placeholder; "Prequisite" typo; deploys legacy `ada-002` |
| Lab 01 — AI-Foundry | ⚠️ Needs minor updates | README uses deprecated connection-string pattern + beta SDK pins; notebooks use correct endpoint |
| Lab 02 — Agents | ⚠️ Needs minor updates | Classic Assistants/threads pattern; Responses API + Agent Framework now recommended |
| Lab 03 — AI-Language | ⚠️ Needs minor updates | Solid Logic Apps flow; "cognitive service" dated; Language Studio retires 2027-03-20 |
| Lab 04 — AI-Vision | ✅ Up to date | Accurate, dated deprecation notices; model lab for the others |
| Lab 05 — Fine-Tuning | ⚠️ Needs minor updates | Hard-coded `C:/Users/Admin/...` paths; model-name typos; DPO region not stated |
| Lab 06 — Prompt Engineering | ✅ Up to date | Clear and model-agnostic; only minor branding refresh |
| Lab 07 — RAI | ⚠️ Needs minor updates | Hub/Management-center navigation now "Foundry classic"; hard-coded paths |
| Lab 08 — RAG-Patterns (GraphRAG) | ✅ Up to date | Honestly pinned GraphRAG `v2.7.0`; embedding suggestion slightly dated |
| Lab 09 — Security (AI Red Teaming) | ✅ Up to date | Current `azure-ai-evaluation[redteam]` + PyRIT |
| Lab 10 — Vector-DB | ⚠️ Needs minor updates | Broken cross-link, copy-paste objective errors, plaintext password, `ada-002` |

### Cross-cutting themes
1. **Branding drift** — "Azure AI Foundry" / "Azure AI Studio" / "Hub" should be refreshed to **Microsoft Foundry** terminology and current portal navigation.
2. **SDK version lag** — Pinned beta/`1.x` packages should move to current `azure-ai-projects` **2.x** and the endpoint-based `AIProjectClient`.
3. **RBAC rename** — "Azure AI User" → **Foundry User** (and related role renames).
4. **Hard-coded VM paths** — `C:/Users/Admin/Desktop/LABS/...` style absolute paths reduce portability (Labs 05, 06, 07, 10).
5. **Naming / spelling** — "Prequisite", folder spacing "Lab 07- RAI", and an `index.md` link bug.

---

## Lab 00 — Prerequisite: AI Foundry Resource Creation

**Files reviewed**
- `01-Create-Azure-Foundry-Project.md`
- `02-Deploy-Models.md`
- `03-Connect-to-Bing-Resources.md`
- `04-Connect-to-Azure-AI-Search.md`
- `05-Setup-(dot)env-file.md`
- `06-Run-requirements.md`, `06-pip-install-requirements.ipynb`
- `Optional-01-Create-Bing-resource.md`, `Optional-02-Create-Azure-AI-Search.md`
- `images/dummy.md` (placeholder) and ~55 screenshots

**Accuracy findings**
- Model deployment guidance centers on **`text-embedding-ada-002`** and older GPT deployments. Recommend leading with **`text-embedding-3-large`** (or `-3-small` for cost) and a current GPT model (e.g., `gpt-4.1`). `ada-002` is now legacy. — https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
- Portal/resource naming should reflect the **Microsoft Foundry** rebrand (project/resource creation flow). — https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry

**Quality findings**
- Folder name misspelled **"Prequisite"** → "Prerequisite".
- `images/dummy.md` is a placeholder committed into the images folder; remove it.
- `05-Setup-(dot)env-file.md` would benefit from a table of the exact `.env` keys consumed by later labs (endpoint, deployment names, search endpoint/key, Bing connection).

**Relevance findings**
- The step-by-step screenshots are valuable but will need re-capture after the portal rebrand; flag them for refresh.

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Update embedding deployment guidance to `text-embedding-3-large` / `-3-small`; add a current GPT model.
2. Rename folder to "Prerequisite"; delete `images/dummy.md`.
3. Add an explicit `.env` key reference table.
4. Refresh branding/screenshots to Microsoft Foundry.

---

## Lab 01 — AI-Foundry

**Files reviewed**
- `Labs/Connection with AOAI/README.md`, `setup and quick_start.ipynb`
- `Labs/Evaluations/README.md`, `1-evaluation.ipynb`, `evaluate_test_data.jsonl`, `health_fitness_eval_data.jsonl`

**Accuracy findings**
- The README references the **connection-string** initialization pattern. The current, recommended pattern is the **endpoint-based `AIProjectClient`** (project endpoint URL). — https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview
- SDK packages are **pinned to beta/`1.x`** versions; move to current **`azure-ai-projects` 2.x** and align package versions across the two READMEs.
- RBAC instructions reference **"Azure AI User"**, now renamed **"Foundry User"**. — https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry

**Quality findings**
- The notebooks already use the correct endpoint approach, so README and notebook are inconsistent — align them.
- Evaluation dataset files are well-formed; the evaluation README is clear.

**Relevance findings**
- The built-in evaluators referenced are still current. — https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-metrics-built-in

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Replace connection-string initialization with endpoint-based `AIProjectClient` in the README.
2. Bump pinned SDKs to current `2.x` and unify versions across READMEs.
3. Update RBAC role name to "Foundry User".

---

## Lab 02 — Agents

**Files reviewed**
- `README.md`, `guidelines.md`
- `1-basics.ipynb`, `2-code_interpreter.ipynb`, `3-file-search.ipynb`, `4-bing_grounding.ipynb`, `5-agents-aisearch.ipynb`, `6-multi-agent-solution.ipynb`
- `agents-with-mcp/README.md`, `client.py`, `server.py`

**Accuracy findings**
- The notebooks use the **classic Assistants/Agents** model (explicit `threads`/`messages`/`runs`). Microsoft now recommends the **Responses API (Agents v2)** and the **Microsoft Agent Framework / Hosted agents** for new work. Add a signpost and, ideally, a v2 path. — https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview
- `agents-with-mcp/README.md` uses `PROJECT_CONNECTION_STRING`, inconsistent with the endpoint pattern elsewhere; the clone path in the instructions omits the `Lab 02 -` segment.
- Python prerequisite states **3.8**; the current SDKs require **3.10+**.

**Quality findings**
- `guidelines.md` appears to be an escaped/export data artifact rather than readable guidance — replace with a clean markdown file.
- The multi-agent notebook is a strong capstone but should reference the Agent Framework orchestration model.

**Relevance findings**
- Bing grounding and AI Search tool integrations remain valid concepts; the SDK surface is what's dated.

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add a clear note that new agents should use the **Responses API / Agent Framework**; optionally provide a v2 example.
2. Fix `agents-with-mcp` README: endpoint var name and clone path.
3. Bump Python prerequisite to 3.10+.
4. Replace the corrupted `guidelines.md`.

---

## Lab 03 — AI-Language

**Files reviewed**
- `README.md` (Logic Apps + Azure AI Language flow), `Images/`

**Accuracy findings**
- Terminology uses **"cognitive service"**; update to **Azure AI Language** / Microsoft Foundry Tools branding. — https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview
- **Language Studio retires 2027-03-20**; add a forward-looking note pointing users to the Foundry experience. — https://learn.microsoft.com/en-us/azure/ai-services/language-service/
- The Logic Apps connectors and flow steps remain valid.
- Repo `index.md` link to this lab/Bing uses `../` where it should be `./` (broken relative link).

**Quality findings**
- README is clear and well structured; deploys a current GPT model (`gpt-4.1`), which is good.

**Relevance findings**
- The integration pattern (Logic Apps + Language) is still a recommended low-code approach.

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Modernize "cognitive service" terminology.
2. Add the Language Studio 2027 retirement note.
3. Fix the `index.md` relative link bug.

---

## Lab 04 — AI-Vision

**Files reviewed**
- `README.md`, `Images/`
- `LabFiles/AI_vision_services_lab.ipynb`, `LabFiles/images/`

**Accuracy findings**
- This lab is **exemplary**: it includes accurate, dated deprecation notices — OCR/Image Analysis 4.0 lifecycle (read API retires **2028-09-25**), legacy Computer Vision **v1–v3.1 retire 2026-09-13**, and Azure Media Services / Video Indexer retirement (**June 2024**). — https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview
- Verify the exact SKU/resource names match current portal labels post-rebrand.

**Quality findings**
- Clear structure, good use of the notebook for hands-on practice; should be used as the **model template** for the other labs' currency notices.

**Relevance findings**
- Reflects current Vision service guidance and lifecycle accurately.

**Overall rating:** ✅ Up to date

**Recommended actions**
1. Spot-check SKU/resource display names against the current portal; otherwise keep as the reference standard.

---

## Lab 05 — Fine-Tuning

**Files reviewed**
- `README.md`, `training_set_10samples.jsonl`, `validation_set_10samples.jsonl`
- `Advance Fine-Tuning/README.MD`, `gpt-4_o_dpo_ft.ipynb`, `data/`, `images/`

**Accuracy findings**
- Models referenced are fine-tunable, but the README does not state the **regional constraint** for fine-tuning (e.g., specific regions such as North Central US / Sweden Central). Add the supported-region note. — https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning
- DPO (Direct Preference Optimization) availability/region is not called out in the Advanced lab.

**Quality findings**
- **Hard-coded path** `C:/Users/Admin/Desktop/LABS/...` should be relativized.
- Model-name typos: **"GPT-4.o"**, **"GPT-4-o-mini"** → `gpt-4o`, `gpt-4o-mini`.
- A leftover template line **"List the objectives"** remains in the README.

**Relevance findings**
- Fine-tuning (SFT) and DPO are current, supported customization techniques.

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Add fine-tuning region constraints (SFT and DPO).
2. Fix model-name typos and the leftover template line.
3. Replace hard-coded absolute paths with workspace-relative paths.

---

## Lab 06 — Prompt Engineering

**Files reviewed**
- `README.md`, `Prompt Engineering.ipynb`

**Accuracy findings**
- Content is model-agnostic and durable. Add a one-line note that **Azure OpenAI is part of Microsoft Foundry**. — https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry
- Note that **reasoning models** use different parameters (e.g., `max_completion_tokens`, no `temperature`) if learners try them.

**Quality findings**
- Clear, well-paced notebook. One **hard-coded path** should be de-hard-coded.

**Relevance findings**
- Prompt-engineering principles remain current best practice.

**Overall rating:** ✅ Up to date

**Recommended actions**
1. Add a brief Microsoft Foundry branding note.
2. De-hard-code the local path.
3. (Optional) Note reasoning-model parameter differences.

---

## Lab 07 — RAI

**Files reviewed**
- `README.md`
- `Files/Content_Safety/`, `Files/Contoso/`, `Files/Evaluations/`
- `rai_md_img/`

**Accuracy findings**
- Navigation references the **Hub / Management center** flow, now positioned as **"Foundry (classic)"**; refresh to the current portal navigation. — https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry
- The RAI **evaluators** referenced (content safety, groundedness, etc.) remain current. — https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-metrics-built-in

**Quality findings**
- **Hard-coded paths** present; relativize them.
- Folder name spacing inconsistent: **"Lab 07- RAI"** (missing space) vs. other labs.

**Relevance findings**
- Responsible AI content (content safety + evaluations) aligns with current guidance.

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Update portal navigation to the current (non-classic) Foundry experience.
2. Fix hard-coded paths and the folder-name spacing.

---

## Lab 08 — RAG-Patterns (GraphRAG)

**Files reviewed**
- `GraphRAG/README.md`

**Accuracy findings**
- The lab **honestly pins GraphRAG `v2.7.0`** with appropriate caveats, which is good practice for a fast-moving package. — https://microsoft.github.io/graphrag/get_started/
- It correctly notes the **GraphRAG Accelerator** repo is archived.
- Embedding guidance leans on `ada-002`; lead with **`text-embedding-3-small` / `-3-large`**. — https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models

**Quality findings**
- Clear setup and execution steps with realistic expectations about cost/runtime.

**Relevance findings**
- GraphRAG remains a current, recommended advanced RAG pattern.

**Overall rating:** ✅ Up to date

**Recommended actions**
1. Update the embedding recommendation to the `text-embedding-3-*` family; otherwise keep as-is.

---

## Lab 09 — Security (AI Red Teaming)

**Files reviewed**
- `README.md`
- `AI_RedTeaming/AI_RedTeaming.ipynb`
- `data/prompts.json`

**Accuracy findings**
- Uses the current **`azure-ai-evaluation[redteam]`** package with **PyRIT**, which is the recommended automated red-teaming approach. — https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/run-scans-ai-red-teaming-agent
- Optionally mention the stable **`/openai/v1/`** inference route for the target model.

**Quality findings**
- Notebook is well organized; `prompts.json` provides a reasonable attack seed set.

**Relevance findings**
- Aligns with current AI Red Teaming Agent guidance.

**Overall rating:** ✅ Up to date

**Recommended actions**
1. (Optional) Reference the stable `/openai/v1/` route; otherwise current.

---

## Lab 10 — Vector-DB

**Files reviewed**
- `Cosmos DB/Readme.md`, `Python-Samples.ipynb`, `data/`
- `PostgreSQL/Readme.md`, `VectorQuery.sql`, `books/`, `images/`
- `SQL/Readme.md`, `1_Setup.sql`, `2_LoadMovieData.py`, `3_UpdateMovieEmbedding.py`, `4_SQLEmbeddings.py`, `5_query.sql`, `movie_quotes.csv`, `images/`

**Accuracy findings**
- Embeddings use **`text-embedding-ada-002`** with `vector(1536)` dimensions; recommend `text-embedding-3-small`/`-3-large` and note the **dimension change** required in DDL. — https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
- SQL `Readme.md` contains a **broken cross-link** (points at an `AugRelease` branch / wrong Cosmos folder).

**Quality findings**
- **Copy-paste objective error:** the SQL lab's objective text says **"PostgreSQL"**.
- **Security smell:** plaintext password **`Password12345!!`** in instructions / `sqlcredentials.txt`; replace with a placeholder and guidance to use a secret.
- Typos: **"numberd"**, file referenced as **`2_LoadMovideData.py`** (vs. actual `2_LoadMovieData.py`).

**Relevance findings**
- Vector search across Cosmos DB, PostgreSQL (`pgvector`), and SQL Server is current and relevant.

**Overall rating:** ⚠️ Needs minor updates

**Recommended actions**
1. Fix the broken SQL `Readme.md` cross-link and the "PostgreSQL" copy-paste objective.
2. Remove the plaintext password; use a placeholder + secret-management note.
3. Correct typos and the `2_LoadMovieData.py` filename reference.
4. Update embeddings to `text-embedding-3-*` and adjust vector dimensions accordingly.

---

## Consolidated Recommended Actions (priority order)

1. **Modernize SDK + branding repo-wide** — endpoint-based `AIProjectClient`, `azure-ai-projects` 2.x, "Microsoft Foundry" terminology, "Foundry User" RBAC role.
2. **De-hard-code local paths** (Labs 05, 06, 07, 10) → workspace-relative paths.
3. **Fix broken links and names** — `index.md` relative link, Lab 10 SQL cross-link, "Prequisite", "Lab 07- RAI" spacing, model-name typos.
4. **Update embeddings guidance** — prefer `text-embedding-3-small` / `-3-large` over `ada-002` (Labs 00, 08, 10).
5. **Signpost the new agent model** (Lab 02) — Responses API / Agent Framework.
6. **Remove placeholder/secret artifacts** — `images/dummy.md`, Lab 10 plaintext password, corrupted `guidelines.md`.
7. **Add forward-looking retirement notes** — Language Studio (2027-03-20), legacy Vision CV (2026-09-13).

---

## Citations Relied Upon

- https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry
- https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview
- https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
- https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-metrics-built-in
- https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry
- https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview
- https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview
- https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning
- https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/run-scans-ai-red-teaming-agent
- https://microsoft.github.io/graphrag/get_started/
