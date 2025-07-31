# Title of the lab

## Introduction 

This lab shows <provide intro>.

## Objectives 
 List the objectives
In this lab we will:
-	


## Estimated Time 

30 minutes 

## Scenario


## Pre-requisites

## Tasks






# Azure AI Agents Tutorial Collection 🤖

This repository contains a comprehensive collection of Azure AI Agent tutorials that demonstrate various capabilities and integration patterns using Azure AI Foundry SDKs.

## 📋 Prerequisites

- Azure subscription with Azure AI services enabled
- Python 3.8 or higher
- VS Code or Jupyter Notebook environment

## 🚀 Quick Setup

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

## 📚 Tutorial Notebooks

### [1-basics.ipynb](./1-basics.ipynb)
**Learn the fundamentals of Azure AI Agents**

- Initialize Azure AI projects using `azure-ai-projects` SDK
- Create a specialized health and fitness advisor agent
- Manage conversation threads and message handling
- Implement OpenTelemetry logging and tracing
- Apply safety disclaimers and best practices

**Key Concepts:**
- Agent creation and configuration
- Thread management for conversations
- Basic interaction patterns
- Telemetry and monitoring

### [2-code_interpreter.ipynb](./2-code_interpreter.ipynb)
**Add computational capabilities to your agents**

- Create agents with code interpreter tools
- Upload and process files for calculations
- Handle complex health and fitness computations
- Manage file attachments at message level
- Demonstrate mathematical analysis capabilities

**Key Concepts:**
- Code interpreter tool integration
- File upload and processing
- Mathematical computations
- Error handling in code execution

### [3-file-search.ipynb](./3-file-search.ipynb)
**Enable document search and knowledge retrieval**

- Upload documents to Azure AI Agent service
- Create agents with file search capabilities
- Search through uploaded health resources
- Implement citation and reference systems
- Clean up resources and manage file lifecycle

**Key Concepts:**
- File upload for agent knowledge base
- Document search and retrieval
- Citation management
- Resource cleanup patterns

### [4-bing_grounding.ipynb](./4-bing_grounding.ipynb)
**Connect agents to real-time web information**

- Configure Bing Search integration
- Create web-grounded health and fitness agents
- Access current information and trends
- Handle real-time queries with web context
- Compare responses with and without grounding

**Key Concepts:**
- Bing Search integration
- Real-time information retrieval
- Grounding vs. non-grounded responses
- External data source integration

### [5-agents-aisearch.ipynb](./5-agents-aisearch.ipynb)
**Advanced search integration with Azure AI Search**

- Set up Azure AI Search indexes
- Create agents with Azure AI Search tool integration
- Implement sophisticated search queries
- Handle fitness equipment and knowledge searches
- Demonstrate enterprise search patterns

**Key Concepts:**
- Azure AI Search integration
- Custom search tool creation
- Enterprise knowledge base queries
- Advanced search patterns

## 🛡️ Important Notes

- **Resource Management**: Remember to clean up Azure resources after tutorials to avoid unnecessary charges
- **Environment Security**: Never commit your `.env` file with actual credentials to version control

## 🔗 Additional Resources

For more examples, please visit:
**[Azure AI Agents Labs](https://github.com/Azure/azure-ai-agents-labs)**
