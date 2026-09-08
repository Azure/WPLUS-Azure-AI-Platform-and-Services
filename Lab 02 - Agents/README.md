# Microsoft Foundry Agents Tutorial Collection

## Introduction

This lab is a hands-on introduction to Microsoft Foundry Agent Service with the current `azure-ai-projects` SDK. You will create versioned prompt agents, invoke them through the OpenAI Responses API, maintain multi-turn state with Conversations, and add tools for code execution, document retrieval, web grounding, enterprise search, and client-side orchestration.

The health and fitness samples are educational demonstrations only and are not substitutes for professional medical advice.

## Objectives

- Initialize a Foundry project client and its OpenAI client.
- Create and delete versioned prompt agents.
- Use Responses and Conversations for single-turn and multi-turn interactions.
- Add Code Interpreter, File Search, Bing Grounding, and Azure AI Search tools.
- Build a multi-agent ticket triage flow with client-side function tools.
- Connect a prompt agent to locally hosted MCP tools.

## Estimated Time

120 minutes (2 hours)

## Prerequisites

- Azure subscription with Microsoft Foundry resources enabled.
- Python 3.10 or later.
- VS Code or Jupyter Notebook.
- `azure-ai-projects>=2.6.0,<3.0.0`.
- **Foundry User** role assigned on the Foundry project.
  - See [Microsoft Foundry RBAC](https://learn.microsoft.com/azure/foundry/concepts/rbac-foundry).
- A root `.env` file containing `AI_FOUNDRY_PROJECT_ENDPOINT`, `MODEL_DEPLOYMENT_NAME`, and `TENANT_ID`.
- A provisioned Foundry project and model deployment.

## Exercises

### Exercise 1: Agent Basics

Use [1-basics.ipynb](./1-basics.ipynb) to create a health advisor prompt-agent version, start a Conversation, and send multiple requests through the Responses API.

### Exercise 2: Code Interpreter

Use [2-code_interpreter.ipynb](./2-code_interpreter.ipynb) to upload a CSV through the OpenAI client, configure `CodeInterpreterTool`, perform calculations, create visualizations, and download generated container files.

### Exercise 3: File Search

Use [3-file-search.ipynb](./3-file-search.ipynb) to create a vector store, upload and index health resources, configure `FileSearchTool`, and inspect file citations in Responses output.

### Exercise 4: Bing Grounding

Use [4-bing_grounding.ipynb](./4-bing_grounding.ipynb) to retrieve a project connection, configure `BingGroundingTool`, ask current-information questions, and display `url_citation` annotations.

### Exercise 5: Azure AI Search

Use [5-agents-aisearch.ipynb](./5-agents-aisearch.ipynb) to create a sample Azure AI Search index, connect it with `AzureAISearchTool`, query it through a prompt agent, and clean up the index.

### Exercise 6: Multi-Agent Triage

Use [6-multi-agent-solution.ipynb](./6-multi-agent-solution.ipynb) to create three specialist prompt-agent versions and an orchestrator with client-side `FunctionTool` definitions. The client invokes specialists and submits `FunctionCallOutput` items back to the orchestrator Conversation.

For a pro-code MCP scenario, continue to [agents-with-mcp](./agents-with-mcp/README.md).

## Resources

- [Microsoft Foundry Agent Service quickstart](https://learn.microsoft.com/azure/foundry/agents/quickstart?view=foundry)
- [Azure AI Projects Python API](https://learn.microsoft.com/python/api/azure-ai-projects/)
- [Foundry agent tools](https://learn.microsoft.com/azure/foundry/agents/how-to/tools/overview)
