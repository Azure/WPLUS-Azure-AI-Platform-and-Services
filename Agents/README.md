# Azure AI Agents Tutorial Collection

## Introduction 

This lab provides a comprehensive hands-on introduction to Azure AI Agents using Azure AI Foundry SDKs. You'll learn how to build, deploy, and manage intelligent agents that can perform various tasks from basic conversations to complex multi-agent orchestration systems with health and fitness themed examples.

## Objectives 
In this lab we will:
- Initialize Azure AI projects and create specialized health and fitness advisor agents
- Implement agents with computational capabilities using code interpreter tools
- Enable document search and knowledge retrieval through file search
- Connect agents to real-time web information using Bing Search integration
- Integrate agents with enterprise search using Azure AI Search
- Build sophisticated multi-agent systems for ticket triage and orchestration
- Implement comprehensive observability and tracing for multi-agent workflows

## Estimated Time 

120 minutes (2 hours)

## Scenario

You are an AI developer tasked with building a comprehensive agent ecosystem for a health and fitness platform. Starting with basic conversational agents, you'll progressively add computational capabilities, knowledge retrieval, real-time information access, and finally orchestrate multiple agents to work together in complex workflows.

## Pre-requisites

- Azure subscription with Azure AI services enabled
- Python 3.8 or higher
- VS Code or Jupyter Notebook environment
- **azure-ai-projects** package version 1.0.0b12 or greater (`azure-ai-projects>=1.0.0b12`)
- **Azure AI User role** assigned to your account for the Azure AI Foundry project
  - See [Azure AI Foundry RBAC documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry?pivots=fdp-project) for more details on role assignments
- `.env` file configured with PROJECT_CONNECTION_STRING and MODEL_DEPLOYMENT_NAME
- Azure AI Foundry project already provisioned

## Tasks

---

## Exercise 1: Agent Basics
**Learn the fundamentals of Azure AI Agents using [1-basics.ipynb](./1-basics.ipynb)**

1. Initialize Azure AI projects using `azure-ai-projects` SDK
2. Create a specialized health and fitness advisor agent with safety disclaimers
3. Manage conversation threads and message handling
4. Implement OpenTelemetry logging and tracing for monitoring
5. Apply best practices for agent creation and configuration

**Key Learning Outcomes:**
- Agent creation and configuration patterns
- Thread management for multi-turn conversations
- Basic interaction patterns and message handling
- Telemetry and monitoring implementation

---

## Exercise 2: Code Interpreter Integration
**Add computational capabilities to your agents using [2-code_interpreter.ipynb](./2-code_interpreter.ipynb)**

1. Create agents with code interpreter tools for mathematical computations
2. Upload and process files for complex health and fitness calculations
3. Handle BMI calculations, nutritional analysis, and fitness metrics
4. Manage file attachments at message level for data processing
5. Demonstrate mathematical analysis capabilities with visualizations

**Key Learning Outcomes:**
- Code interpreter tool integration and configuration
- File upload and processing workflows
- Mathematical computations and data analysis
- Error handling in code execution environments

---

## Exercise 3: File Search and Knowledge Retrieval
**Enable document search and knowledge retrieval using [3-file-search.ipynb](./3-file-search.ipynb)**

1. Upload health and nutrition documents to Azure AI Agent service
2. Create agents with file search capabilities for knowledge retrieval
3. Search through uploaded health resources with semantic queries
4. Implement citation and reference systems for source tracking
5. Clean up resources and manage file lifecycle effectively

**Key Learning Outcomes:**
- File upload for agent knowledge base creation
- Document search and retrieval mechanisms
- Citation management and source tracking
- Resource cleanup patterns and lifecycle management

---

## Exercise 4: Bing Search Grounding
**Connect agents to real-time web information using [4-bing_grounding.ipynb](./4-bing_grounding.ipynb)**

1. Configure Bing Search integration for real-time information access
2. Create web-grounded health and fitness agents with current data
3. Access current health trends, research, and fitness information
4. Handle real-time queries with web context and fact-checking
5. Compare responses with and without grounding to understand benefits

**Key Learning Outcomes:**
- Bing Search integration and configuration
- Real-time information retrieval patterns
- Grounding vs. non-grounded response comparison
- External data source integration strategies

---

## Exercise 5: Azure AI Search Integration
**Advanced search integration with Azure AI Search using [5-agents-aisearch.ipynb](./5-agents-aisearch.ipynb)**

1. Set up Azure AI Search indexes for enterprise knowledge bases
2. Create agents with Azure AI Search tool integration
3. Implement sophisticated search queries for fitness equipment and knowledge
4. Handle complex search scenarios with filtering and ranking
5. Demonstrate enterprise search patterns and best practices

**Key Learning Outcomes:**
- Azure AI Search integration and configuration
- Custom search tool creation and deployment
- Enterprise knowledge base queries and management
- Advanced search patterns and optimization techniques

---

## Exercise 6: Multi-Agent Solution
**Build sophisticated multi-agent systems using [6-multi-agent-solution.ipynb](./6-multi-agent-solution.ipynb)**

1. Design and implement a multi-agent ticket triage system
2. Create three specialist agents for priority, team assignment, and effort estimation
3. Build an orchestrator agent that coordinates specialist agents
4. Use connected agent tools for seamless agent-to-agent communication
5. Process complex support tickets through automated triage workflows

**Key Learning Outcomes:**
- Multi-agent system architecture and design
- Agent specialization and role definition
- Agent orchestration and coordination patterns
- Connected agent tools implementation

---

## Exercise 7: Multi-Agent Solution with Tracing
**Advanced multi-agent systems with comprehensive observability using [7-multi-agent-solution-with-tracing.ipynb](./7-multi-agent-solution-with-tracing.ipynb)**

1. Implement the same multi-agent ticket triage system with full tracing
2. Configure OpenTelemetry instrumentation for multi-agent workflows
3. Monitor agent interactions and communication patterns
4. Track performance metrics and troubleshoot agent behaviors
5. Visualize multi-agent execution flows in Azure Monitor

**Key Learning Outcomes:**
- Advanced observability for multi-agent systems
- OpenTelemetry configuration for complex workflows
- Performance monitoring and optimization
- Troubleshooting multi-agent interactions

---

## � Quick Setup

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` file with your Azure credentials:
   ```bash
   PROJECT_CONNECTION_STRING=<your-project-connection-string-from-azure-ml-workspace>
   MODEL_DEPLOYMENT_NAME=<your-model-deployment-name>
   EMBEDDING_MODEL_DEPLOYMENT_NAME=<your-embedding-model-deployment-name>
   TENANT_ID=<your-tenant-id-from-azure-portal>
   GROUNDING_WITH_BING_CONNECTION_NAME=<your-bing-search-connection-name>
   AZURE_AI_SEARCH_ENDPOINT=<your-azure-ai-search-endpoint>
   AZURE_AI_SEARCH_API_KEY=<your-azure-ai-search-api-key>
   ```

## �🛡️ Important Notes

- **Resource Management**: Remember to clean up Azure resources after tutorials to avoid unnecessary charges
- **Environment Security**: Never commit your `.env` file with actual credentials to version control
- **Progressive Learning**: Complete exercises in order as they build upon previous concepts
- **Health Disclaimers**: All health and fitness examples are for educational purposes only

## 🔗 Additional Resources

For more examples, please visit:
**[Azure AI Agents Labs](https://github.com/Azure/azure-ai-agents-labs)**

For pro-code advanced scenarios, explore the `agents-with-mcp/` directory for Model Context Protocol integration examples.
