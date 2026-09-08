# MCP Inventory Management Prompt Agent

## Introduction

This lab connects a Microsoft Foundry prompt agent to local tools exposed through the Model Context Protocol (MCP). The client discovers each MCP tool schema, converts it to a current Foundry `FunctionTool`, executes requested calls through the MCP session, and returns `FunctionCallOutput` items to the agent through the Responses API.

## Objectives

- Launch an MCP server over stdio.
- Discover MCP tools dynamically.
- Create a versioned Foundry prompt agent with client-side function tools.
- Maintain an interactive chat with an OpenAI Conversation.
- Execute MCP calls and submit their outputs until the agent produces a final response.
- Delete the prompt-agent version during cleanup.

## Prerequisites

- Microsoft Foundry project with a deployed model.
- Python 3.10 or later.
- `azure-ai-projects>=2.6.0,<3.0.0`.
- **Foundry User** role on the Foundry project.
- Azure authentication, for example `az login`.
- Root `.env` containing:
  - `AI_FOUNDRY_PROJECT_ENDPOINT` (preferred), `AZURE_AI_PROJECT_ENDPOINT`, `PROJECT_ENDPOINT`, or the legacy `PROJECT_CONNECTION_STRING` endpoint value.
  - `MODEL_DEPLOYMENT_NAME`.
  - `TENANT_ID` if required by your authentication environment.

## Architecture

```text
User
  |
  v
Foundry prompt agent (Responses + Conversation)
  |
  | function_call / FunctionCallOutput
  v
Python MCP client ---- stdio ----> FastMCP inventory server
```

The server exposes:

- `get_inventory_levels`
- `get_weekly_sales`

## Setup

From `Lab 02 - Agents\agents-with-mcp`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r ..\..\requirements.txt
```

The client reads the root `.env`; do not copy secrets into this directory.

## Run

```powershell
python client.py
```

Expected startup:

```text
Project Endpoint: https://<resource>.services.ai.azure.com/api/projects/<project>
Model Deployment: <deployment-name>
Connected to server with tools: ['get_inventory_levels', 'get_weekly_sales']
Enter a prompt for the inventory agent. Use 'quit' to exit.
```

Try:

```text
Please analyze our current inventory and provide recommendations.
What items need restocking urgently?
Which products should we put on clearance?
Show me the current inventory and weekly sales.
```

Type `quit` to delete the created agent version and exit.

## How It Works

1. `client.py` starts `server.py` with the active Python interpreter.
2. The MCP client calls `list_tools()` and maps each `inputSchema` to a Foundry `FunctionTool`.
3. The client creates an `inventory-agent` version with `PromptAgentDefinition`.
4. User prompts are sent with `openai_client.responses.create()` in one Conversation.
5. Each returned `function_call` is executed with `session.call_tool()`.
6. Results are submitted as `FunctionCallOutput` items until a final text response is available.
7. The client deletes the agent version in a `finally` block.

## Troubleshooting

| Issue | Resolution |
|---|---|
| `ModuleNotFoundError: mcp` | Activate the virtual environment and install the root requirements. |
| Authentication failed | Run `az login`, verify the endpoint, and confirm the **Foundry User** role. |
| Server connection failed | Run from this directory and confirm `server.py` is present. |
| Agent creation failed | Verify the model deployment and `azure-ai-projects` version. |
| Tool call failed | Inspect the printed MCP tool name and arguments, then run the server tool independently. |

## Resources

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Microsoft Foundry Agent Service quickstart](https://learn.microsoft.com/azure/foundry/agents/quickstart?view=foundry)
- [Azure AI Projects Python API](https://learn.microsoft.com/python/api/azure-ai-projects/)
- [Function calling with Foundry agents](https://learn.microsoft.com/azure/foundry/agents/how-to/tools/function-calling)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
