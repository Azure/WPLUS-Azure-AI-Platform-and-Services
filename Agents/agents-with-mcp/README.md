git clone <repository-url>
# MCP Inventory Management Agent Lab

## Introduction
This lab demonstrates how to connect Azure AI Agents to external tools via the **Model Context Protocol (MCP)**. You will build an intelligent inventory management assistant for a cosmetics retailer that automatically discovers and invokes MCP-provided tools to analyze stock levels and produce actionable recommendations.

## Objectives
In this lab you will:
- Understand the MCP architecture (client/server, stdio transport)
- Launch an MCP server that exposes inventory & sales tools
- Run an Azure AI Agent that auto-discovers and calls those tools
- Interactively query inventory health and receive recommendations
- Extend & troubleshoot the integration

## Estimated Time
30–40 minutes

## Scenario
A cosmetics retailer needs proactive visibility into inventory velocity and stock risks. Instead of manually exporting reports, an AI Agent should dynamically call tool endpoints (inventory & weekly sales) and synthesize restock, clearance, and insight recommendations in natural language.

## Pre-requisites
- Azure AI Foundry project with a deployed model (e.g. `gpt-4o`)
- Root `.env` in repository configured with:
  - `PROJECT_CONNECTION_STRING`
  - `MODEL_DEPLOYMENT_NAME`
  - `TENANT_ID`
- Python 3.10+
- (Optional) Azure CLI authenticated: `az login`

## Tasks (High-Level)
1. Environment setup
2. Configure authentication
3. Run MCP client (auto-starts server)
4. Interact with the agent
5. Explore architecture & code
6. Troubleshoot & extend

---

## Architecture Overview
```
┌─────────────────┐    MCP Protocol    ┌─────────────────┐
│   Azure AI      │ ◄─────────────────► │   MCP Server    │
│   Agent Client  │   (stdio transport) │   (server.py)   │
│   (client.py)   │                     │                 │
└─────────────────┘                     └─────────────────┘
         │                                       │
         │ Calls tools automatically             │ Provides tools:
         │ based on user queries                 │ • get_inventory_levels
         └───────────────────────────────────────│ • get_weekly_sales
```

---
## Exercise 1: Environment Setup
1. Clone repository & create virtual environment:
   ```bash
   git clone <repository-url>
   cd WPLUS-Azure-AI-Platform-and-Services/Agents/agents-with-mcp
   python -m venv .venv
   # Windows
   .venv\\Scripts\\activate
   # macOS/Linux
   source .venv/bin/activate
   pip install -r ../requirements.txt
   ```
2. Confirm `.env` exists two levels up (root). Do not duplicate local secrets.

---
## Exercise 2: Configure Authentication
Use tenant-scoped interactive browser auth (recommended):
```bash
az login
```
The client uses environment variables from the root `.env`. No extra per-script config required.

---
## Exercise 3: Run the MCP Demo
Run the client (it launches the server automatically):
```bash
python client.py
```
Expected initial output:
```
Project Endpoint: https://<project>.services.ai.azure.com/api/projects/<name>
Model Deployment: gpt-4o
Connected to server with tools: ['get_inventory_levels', 'get_weekly_sales']
Enter a prompt for the inventory agent. Use 'quit' to exit.
```

---
## Exercise 4: Interact with the Agent
Try queries:
```
Please analyze our current inventory and provide recommendations
What items need restocking urgently?
Which products should we put on clearance sale?
Show me all inventory levels and sales data
What's our overall inventory health?
```
Type `quit` to exit.

---
## Exercise 5: How It Works
### Server (`server.py`)
- FastMCP-based stdio server
- Tools: `get_inventory_levels`, `get_weekly_sales`
- Returns structured JSON-like payloads consumed by agent

### Client (`client.py`)
- Spawns server subprocess (stdio transport)
- Discovers tools dynamically (no hardcoded schema)
- Wraps tools as callable Python functions
- Creates Azure AI Agent with automatic tool invocation
- Maintains conversation & aggregates responses

### Key Features
1. Automatic tool discovery
2. Intelligent recommendation synthesis
3. Real-time aggregation of sales + inventory
4. Structured, rationale-driven output
5. Resilient error handling

---
## Exercise 6: Sample Interaction
```
USER: Please analyze our current inventory and provide recommendations

🔧 Agent is calling MCP tools...
📊 Calling tool: get_inventory_levels
📊 Calling tool: get_weekly_sales

AGENT:
<Restock / clearance / insight recommendations>
```

---
## Exercise 7: Troubleshooting
| Issue | Resolution |
|-------|------------|
| ModuleNotFoundError: mcp | Activate venv & install deps: `pip install -r ../requirements.txt` |
| Authentication failed | Ensure `az login` and correct `.env` values |
| Server connection failed | Confirm `server.py` present; run from directory; venv active |
| Agent creation failed | Verify model deployment, permissions, and env vars |

Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---
## Exercise 8: Extend the Lab
Enhancements:
- Add supplier lead-time tool
- Add purchase order projection tool
- Persist historical runs
- Integrate cost / margin analytics
- Deploy server to Azure Container Apps

---
## Learning Objectives Recap
You now understand:
- MCP protocol & stdio transport pattern
- Dynamic tool discovery & invocation
- Azure AI Agent integration flow
- Designing data-driven recommendations
- Strategies for extension & production hardening

---
## Next Steps
| Path | Description |
|------|-------------|
| Add Tools | Introduce forecasting, anomaly detection |
| Production Hardening | Observability, retries, auth, rate limiting |
| Multi-Agent Expansion | Add pricing or marketing agent tools |
| Visualization | Feed results into dashboard / BI system |

---
## Resources
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Azure AI Foundry](https://ai.azure.com/)
- [Azure AI Agents SDK](https://learn.microsoft.com/en-us/python/api/azure-ai-agents/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP Framework](https://github.com/jlowin/fastmcp)

## Support
| Area | Link |
|------|------|
| Azure AI Services | https://azure.microsoft.com/support/ |
| MCP Community | https://modelcontextprotocol.io/community/ |
| Repository Issues | Open an issue in this repo |

---
**🎉 Happy Building!** Leverage MCP + Azure AI Agents to operationalize intelligent, tool-aware assistants.
