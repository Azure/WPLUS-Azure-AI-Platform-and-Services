# Microsoft Foundry Feature Suggestions — WPLUS Azure AI Platform and Services

**Report date:** 2026-06-09
**Author:** Foundry Feature Advisor (subagent)
**Scope:** Full workshop — Lab 00 through Lab 10 plus the Optional Lab (AI Fundamentals)

> Goal: identify the newest, most relevant Microsoft Foundry capabilities (models, agents, RAG, RAI/security, fine-tuning, platform/SDK) and map each to the single best lab. Status is flagged **GA / Preview / Announced**. Citations are inline.

---

## Top Recommendations

| # | Feature | Target lab | Status | Priority | One-line benefit |
|---|---------|-----------|--------|----------|------------------|
| 1 | Upgrade to **Foundry SDK `azure-ai-projects` v2.x** (Responses API via `get_openai_client()`) | Lab 01 | GA | High | Teaches the supported, non-beta SDK and the Responses API |
| 2 | **Model router** (auto-selects best/cheapest model per prompt) | Lab 00 / Lab 01 | GA | High | Cost/quality optimization without code changes |
| 3 | **Reasoning models (o-series / GPT-5 reasoning)** + prompting guidance | Lab 06 | GA | High | Modern prompting for models that reason internally |
| 4 | **Connected / multi-agent (agent orchestration)** | Lab 02 | GA/Preview | High | Real-world multi-agent patterns beyond a single agent |
| 5 | **MCP tool** for agents (Model Context Protocol) | Lab 02 | Preview | High | Standard way to connect agents to external tools/data |
| 6 | **Agentic retrieval / knowledge sources** (Azure AI Search) | Lab 08 | Preview/GA | High | First-party, query-planning RAG vs. hand-rolled GraphRAG |
| 7 | **Grounding with Bing Search** as an agent tool | Lab 02 | GA | Medium | Live web grounding inside agents |
| 8 | **Agent evaluators + continuous (online) evaluation** | Lab 01 / Lab 07 | GA/Preview | Medium | Evaluate agent trajectories and monitor in production |
| 9 | **RFT (reinforcement) & DPO fine-tuning + distillation** | Lab 05 | Preview/GA | Medium | Modern tuning methods beyond SFT |
| 10 | **Microsoft Agent Framework** (AutoGen + SK convergence) | Optional Lab | GA/Preview | Medium | Go-forward multi-agent framework |
| 11 | **Foundry observability / tracing (OpenTelemetry)** | Lab 02 / Lab 01 | GA/Preview | Medium | Production debugging of agents and chains |
| 12 | **Content Safety: Prompt Shields + Groundedness detection** in code | Lab 07 / Lab 09 | GA | Medium | Programmatic guardrails, not just portal demos |
| 13 | **Multimodal (GPT-4o/4.1 vision) vs. classic Vision** note | Lab 04 | GA | Low | Help learners choose LLM vision vs. Image Analysis 4.0 |
| 14 | **Azure AI Search integrated vectorization** as a 4th store | Lab 10 | GA | Low | Completes the vector-store comparison |

---

## 1. Foundry SDK `azure-ai-projects` v2.x + Responses API

- **What it is:** The unified Microsoft Foundry SDK is GA at **v2.2.0**. `AIProjectClient` connects via the project endpoint URL with Entra ID; `.get_openai_client()` exposes the **Responses API** (stateful, `previous_response_id`), plus Agents, Evaluations, Files, and Fine-Tuning.
- **Why add it:** Lab 01 currently pins beta `1.0.0b12` and teaches connection-string auth. Moving to v2.x teaches the supported surface and the Responses API that underpins agents.
- **Target lab:** Lab 01 (and ripple into Labs 02, 09).
- **Status & availability:** GA (v2.2.0, updated 2026-06-01).
- **Citation:** https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- **Suggested change:** Update `requirements`, swap to `AIProjectClient(endpoint=..., credential=DefaultAzureCredential())`, add a Responses API cell.

## 2. Model Router

- **What it is:** A deployable router that automatically picks the most suitable underlying model per request to balance quality and cost.
- **Why add it:** Learners currently hard-code `gpt-4o-mini`. Model router demonstrates cost/quality optimization with no app changes — a frequent customer ask.
- **Target lab:** Lab 00 (deploy it) + Lab 01 (use it).
- **Status & availability:** GA in Foundry Models.
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/model-router
- **Suggested change:** Add a "Deploy model router" step in Lab 00 and a Lab 01 cell that calls the router deployment.

## 3. Reasoning models (o-series / GPT-5 reasoning) + prompting guidance

- **What it is:** Reasoning-optimized models (o-series, GPT-5 reasoning tiers) that perform internal chain-of-thought; they take `reasoning_effort`/`max_completion_tokens` and respond differently to explicit CoT.
- **Why add it:** Lab 06 teaches CoT/ToT as if all models behave the same. Reasoning models change the guidance (don't force explicit CoT; use clear goals + constraints).
- **Target lab:** Lab 06 (new section), reinforced in Lab 02.
- **Status & availability:** GA (model-dependent).
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reasoning
- **Suggested change:** Add "Prompting reasoning models" with a side-by-side example vs. a standard chat model.

## 4. Connected / multi-agent orchestration

- **What it is:** Foundry Agent Service supports **connected agents** and multi-agent orchestration where a primary agent delegates to specialized sub-agents.
- **Why add it:** Lab 02 stops at a single agent. Multi-agent is the dominant real-world pattern and a natural progression.
- **Target lab:** Lab 02 (new notebook `4-connected-agents.ipynb`).
- **Status & availability:** GA/Preview (feature-dependent).
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/connected-agents
- **Suggested change:** Add a triage→specialist example reusing the health/fitness domain.

## 5. MCP tool for agents

- **What it is:** Agents can call external tools/data via the **Model Context Protocol** tool.
- **Why add it:** MCP is becoming the standard integration layer; teaching it future-proofs the agents lab.
- **Target lab:** Lab 02.
- **Status & availability:** Preview.
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/model-context-protocol
- **Suggested change:** Add an MCP tool example (e.g., connect to a sample MCP server) as an optional cell.

## 6. Agentic retrieval / knowledge sources (Azure AI Search)

- **What it is:** Azure AI Search **agentic retrieval** decomposes a query into subqueries, runs them in parallel, and returns grounded, ranked results; **knowledge sources** package data for agents.
- **Why add it:** Lab 08 hand-rolls GraphRAG. Agentic retrieval is Microsoft's first-party, lower-maintenance RAG direction and complements GraphRAG.
- **Target lab:** Lab 08 (new section) or a new "Agentic RAG" lab.
- **Status & availability:** Preview/GA (feature-dependent).
- **Citation:** https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-concept
- **Suggested change:** Add an agentic-retrieval walkthrough contrasted with GraphRAG global/local queries.

## 7. Grounding with Bing Search (agent tool)

- **What it is:** A built-in agent tool that grounds responses in live Bing web results.
- **Why add it:** Lab 00 already connects a Bing resource but no lab demonstrates the grounding tool end-to-end in an agent.
- **Target lab:** Lab 02.
- **Status & availability:** GA.
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/bing-grounding
- **Suggested change:** Add a "current info" agent cell using the Bing grounding tool.

## 8. Agent evaluators + continuous (online) evaluation

- **What it is:** Evaluators for agent **trajectories** (intent resolution, tool-call accuracy, task adherence) plus **continuous/online evaluation** that monitors a deployed app.
- **Why add it:** Lab 01 evaluates single responses; agent and online evaluation reflect production practice.
- **Target lab:** Lab 01 (extend) and/or Lab 07.
- **Status & availability:** GA/Preview (evaluator-dependent).
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/online-evaluation
- **Suggested change:** Add an agent-evaluation cell and a short online-evaluation setup section.

## 9. RFT & DPO fine-tuning + distillation

- **What it is:** Beyond SFT, Foundry supports **DPO** (preference tuning) and **Reinforcement Fine-Tuning (RFT)** with graders, plus **distillation** (use a large model's outputs to tune a small one).
- **Why add it:** Lab 05 only covers SFT; these methods are increasingly the recommended path for reasoning/agent tasks.
- **Target lab:** Lab 05.
- **Status & availability:** Preview/GA (method/model-dependent).
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/fine-tuning-considerations
- **Suggested change:** Add an "Advanced methods: DPO, RFT, distillation" section with selection guidance.

## 10. Microsoft Agent Framework (AutoGen + SK convergence)

- **What it is:** Microsoft's unified, open-source agent framework that converges Semantic Kernel and AutoGen.
- **Why add it:** The Optional Lab teaches SK + AutoGen separately; the Agent Framework is the go-forward consolidation.
- **Target lab:** Optional Lab — AI Fundamentals.
- **Status & availability:** GA/Preview.
- **Citation:** https://learn.microsoft.com/en-us/agent-framework/
- **Suggested change:** Add a closing section mapping SK/AutoGen concepts onto the Agent Framework.

## 11. Foundry observability / tracing (OpenTelemetry)

- **What it is:** Built-in tracing for agents/chains via OpenTelemetry, viewable in the Foundry portal and Azure Monitor.
- **Why add it:** Lab 02 mentions OpenTelemetry only as a "next step"; a concrete tracing cell teaches production debugging.
- **Target lab:** Lab 02 (and Lab 01).
- **Status & availability:** GA/Preview.
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability
- **Suggested change:** Add a tracing-enabled agent run and show the trace in the portal.

## 12. Content Safety in code (Prompt Shields + Groundedness detection)

- **What it is:** Programmatic Content Safety APIs — Prompt Shields (jailbreak/indirect-attack) and groundedness detection — beyond the portal "Try it out".
- **Why add it:** Lab 07 demonstrates these in the portal; an SDK example makes them production-ready and ties to Lab 09.
- **Target lab:** Lab 07 (extend) / Lab 09.
- **Status & availability:** GA.
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
- **Suggested change:** Add a small SDK cell calling Prompt Shields + groundedness detection.

## 13. Multimodal vision vs. classic Vision note

- **What it is:** GPT-4o/4.1 multimodal vision overlaps with classic OCR/Image Analysis 4.0.
- **Why add it:** Helps learners pick the right tool (cost, structure, gating).
- **Target lab:** Lab 04.
- **Status & availability:** GA.
- **Citation:** https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis
- **Suggested change:** Add a short "LLM vision vs. Image Analysis 4.0" decision note.

## 14. Azure AI Search integrated vectorization as a 4th store

- **What it is:** Azure AI Search with **integrated vectorization** (built-in chunking + embedding).
- **Why add it:** Completes Lab 10's store comparison with the first-party retrieval service.
- **Target lab:** Lab 10.
- **Status & availability:** GA.
- **Citation:** https://learn.microsoft.com/en-us/azure/search/vector-search-integrated-vectorization
- **Suggested change:** Add an optional Azure AI Search vector notebook alongside Cosmos/PostgreSQL/SQL.

---

## Proposed new labs

- **Agentic RAG with Azure AI Search** — a first-party counterpart to the GraphRAG lab (could live under Lab 08).
- **Multi-Agent Orchestration** — connected agents + MCP + tracing, building on Lab 02.

## Quick wins (low effort, high value)

- Refresh default model names: `gpt-4o-mini` → `gpt-4.1-mini` (or model router). *(Labs 02, 08, 09)*
- Bump SDK pin: `azure-ai-projects>=1.0.0b12` → `==2.2.0`. *(Lab 01)*
- Add a one-line "model router available" note in Lab 00.
- Note AutoGen/SK → Microsoft Agent Framework convergence. *(Optional Lab)*
- Add Face **Limited Access** gating note. *(Lab 04)*

---

## Appendix — Sources

- Azure AI Projects SDK v2.2.0 — https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme
- Foundry Models overview — https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview
- Model router — https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/model-router
- Reasoning models — https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reasoning
- Connected agents — https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/connected-agents
- MCP tool — https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/model-context-protocol
- Agentic retrieval — https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-concept
- Bing grounding tool — https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/bing-grounding
- Online evaluation — https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/online-evaluation
- Fine-tuning considerations (DPO/RFT) — https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/fine-tuning-considerations
- Microsoft Agent Framework — https://learn.microsoft.com/en-us/agent-framework/
- Foundry observability — https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability
- Content Safety jailbreak detection — https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
- Integrated vectorization — https://learn.microsoft.com/en-us/azure/search/vector-search-integrated-vectorization
