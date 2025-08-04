# Quick Start Guide - Azure AI Foundry

## Introduction 

This lab provides a hands-on introduction to Azure AI Foundry. You'll learn the fundamentals of working with Azure AI projects, from authentication to creating intelligent agents with computational capabilities.

## Objectives 
In this lab we will:
- Initialize the AI Project client with proper authentication
- List available models in your Azure AI project
- Create simple chat completion requests
- Create a basic AI agent with code interpreter capabilities
- Handle basic error scenarios and troubleshooting

## Estimated Time 

30 minutes 

## Scenario

You are a developer getting started with Azure AI Foundry. You need to establish connectivity, understand the basic SDK usage patterns, and create your first intelligent agent that can perform calculations and generate visualizations.

## Pre-requisites

- Completed environment setup from previous notebook
- Azure credentials configured
- **azure-ai-projects** package version 1.0.0b12 or greater (`azure-ai-projects>=1.0.0b12`)
- **Azure AI User role** assigned to your account for the Azure AI Foundry project
  - See [Azure AI Foundry RBAC documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry?pivots=fdp-project) for more details on role assignments
- `.env` file configured with PROJECT_CONNECTION_STRING and MODEL_DEPLOYMENT_NAME
- Azure AI Foundry project already provisioned

## Tasks





### Task 1 - Import Required Libraries and Setup

Configure authentication and import necessary Azure SDK libraries:
- Import Azure SDK libraries (azure.identity, azure.ai.projects)
- Import standard Python libraries for environment variables and JSON handling
- Initialize Azure credentials using DefaultAzureCredential with tenant-specific authentication
- Create a robust credential chain with fallbacks for authentication
- Load environment variables from `.env` file

### Task 2 - Initialize AI Project Client

Create and configure the AI Project client:
- Load project connection string from environment variables
- Create AIProjectClient using the connection string and credentials
- Establish connection to your Azure AI Foundry project
- Handle authentication errors and provide troubleshooting guidance

Key steps:
- Copy `.env.example` file to `.env` in the root directory
- Update the project connection string in your `.env` file
- Ensure you have a Foundry Project already provisioned in Azure AI Foundry
- Find your project connection string in [Azure AI Foundry](https://ai.azure.com) under project settings

### Task 3 - Create a Simple Completion

Make your first chat completion request:
- Get Azure OpenAI client from the AI Project client
- Use the MODEL_DEPLOYMENT_NAME from your `.env` file
- Create a simple chat completion request
- Handle responses and error scenarios
- Understand the difference between different model providers (Azure OpenAI, Microsoft models, etc.)

The example demonstrates:
- Basic message structure with user role
- Simple health-related question for testing
- Error handling and troubleshooting tips

### Task 4 - Create a Simple Agent

Explore Azure AI Agent Service capabilities:
- Learn about Azure AI Agent Service as a fully managed service
- Create an agent with code interpreter tool capabilities
- Configure agent instructions and behaviors
- Create conversation threads for multi-turn interactions
- Process agent requests and handle responses

Agent capabilities demonstrated:
- BMI calculation using US metrics
- Data visualization creation
- File generation and saving
- Agent cleanup and resource management

The example shows how agents can:
- Answer questions using natural language understanding
- Perform computational tasks through code interpreter
- Generate visualizations and save them as files
- Combine language understanding with computational capabilities

### Laboratory Features

**Authentication Patterns:**
- Tenant-specific authentication setup
- Credential chain creation with fallbacks
- Azure CLI and Interactive Browser authentication
- Environment variable management

**Error Handling:**
- Comprehensive error messages and troubleshooting guidance
- Authentication failure recovery
- Missing configuration detection
- Model deployment verification

**Resource Management:**
- Proper agent cleanup after use
- File saving and management
- Thread and message handling
- Connection string validation

## Execution Instructions

1. **Initial Setup**:
   - Ensure you have completed the environment setup from the previous notebook
   - Configure environment variables in the `.env` file at repository root
   - Verify your Azure AI User role assignment

2. **Execution**:
   - Open the `setup and quick_start.ipynb` notebook in Azure AI Foundry or VS Code
   - Execute cells sequentially, following the authentication flow
   - Test the simple completion example
   - Create and interact with the BMI calculator agent

3. **Troubleshooting**:
   - Verify your PROJECT_CONNECTION_STRING is correctly set
   - Ensure MODEL_DEPLOYMENT_NAME matches your deployed model
   - Check your Azure AI User role permissions
   - Review authentication error messages for guidance

## Expected Results

Upon completing this laboratory, you will:
- Successfully authenticate with Azure AI Foundry
- Understand the AI Project client initialization patterns
- Make basic chat completion requests
- Create and interact with AI agents
- Handle common error scenarios
- Save generated files and visualizations locally

## Additional Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure AI Foundry RBAC](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry)
- [Azure AI Projects SDK](https://learn.microsoft.com/python/api/azure-ai-projects/)
- [Azure AI Agent Service](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-agents)
- [Authentication with Azure SDK](https://learn.microsoft.com/python/api/azure-identity/)

## Next Steps

After completing this laboratory, you will be prepared to advance to more specialized Azure AI Foundry labs, including advanced agent scenarios, tool integration, and multi-modal capabilities.
