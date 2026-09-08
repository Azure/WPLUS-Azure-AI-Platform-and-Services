# Quick Start Guide - Microsoft Foundry

## Introduction 

This lab provides a hands-on introduction to Microsoft Foundry. You'll learn the fundamentals of working with Foundry projects, from authentication to creating intelligent agents with computational capabilities.

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
- Signed in to Azure from the lab VM:
  - [ ] Open a terminal in VS Code (**Terminal** → **New Terminal**)
  - [ ] Run `az login --use-device-code`
  - [ ] Open the displayed URL in the browser, enter the device code, and sign in with your Azure Username and Temporary Access Pass
  - [ ] When prompted, select the default subscription
- **azure-ai-projects** package version 2.6.0 or greater (`azure-ai-projects>=2.6.0,<3.0.0`)
- **Foundry User role** assigned to your account for the Microsoft Foundry project
  - See [Microsoft Foundry RBAC documentation](https://learn.microsoft.com/azure/foundry/concepts/rbac-foundry) for more details on role assignments
- `.env` file configured with AI_FOUNDRY_PROJECT_ENDPOINT and MODEL_DEPLOYMENT_NAME
- Microsoft Foundry project already provisioned

## Tasks





### Task 1 - Import Required Libraries and Setup

Configure authentication and import necessary Azure SDK libraries:
- [ ] Import Azure SDK libraries (azure.identity, azure.ai.projects)
- [ ] Import standard Python libraries for environment variables and JSON handling
- [ ] Initialize Azure credentials using DefaultAzureCredential with tenant-specific authentication
- [ ] Create a robust credential chain with fallbacks for authentication
- [ ] Load environment variables from `.env` file

### Task 2 - Initialize AI Project Client

Create and configure the AI Project client:
- [ ] Load the project endpoint from environment variables
- [ ] Create AIProjectClient using the project endpoint and credentials
- [ ] Establish connection to your Microsoft Foundry project
- [ ] Handle authentication errors and provide troubleshooting guidance

Key steps:
- [ ] Copy `.env.example` file to `.env` in the root directory
- [ ] Update the project endpoint in your `.env` file
- [ ] Ensure you have a Foundry Project already provisioned in Azure AI Foundry
- [ ] Find your project endpoint in [Microsoft Foundry](https://ai.azure.com) under **Manage > Project details**

### Task 3 - Create a Simple Completion

Make your first chat completion request:
- [ ] Get Azure OpenAI client from the AI Project client
- [ ] Use the MODEL_DEPLOYMENT_NAME from your `.env` file
- [ ] Create a simple chat completion request
- [ ] Handle responses and error scenarios
- [ ] Understand the difference between different model providers (Azure OpenAI, Microsoft models, etc.)

The example demonstrates:
- Basic message structure with user role
- Simple health-related question for testing
- Error handling and troubleshooting tips

### Task 4 - Create a Simple Agent

Explore Microsoft Foundry Agent Service capabilities:
- [ ] Learn about Microsoft Foundry Agent Service as a fully managed service
- [ ] Create an agent with code interpreter tool capabilities
- [ ] Configure agent instructions and behaviors
- [ ] Create OpenAI conversations for multi-turn interactions
- [ ] Process agent requests through the Responses API

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
- Conversation and response handling
- Project endpoint validation

## Execution Instructions

1. **Initial Setup**:
   - [ ] Ensure you have completed the environment setup from the previous notebook
   - [ ] Configure environment variables in the `.env` file at repository root
   - [ ] Run `az login --use-device-code` in a terminal and complete sign-in before running any cells
   - [ ] Verify your Foundry User role assignment

2. **Execution**:
   - [ ] Open the `setup and quick_start.ipynb` notebook in Azure AI Foundry or VS Code
   - [ ] Execute cells sequentially, following the authentication flow
   - [ ] Test the simple completion example
   - [ ] Create and interact with the BMI calculator agent

3. **Troubleshooting**:
   - [ ] Verify your AI_FOUNDRY_PROJECT_ENDPOINT is correctly set
   - [ ] Ensure MODEL_DEPLOYMENT_NAME matches your deployed model
   - [ ] Check your Foundry User role permissions
   - [ ] Review authentication error messages for guidance

## Expected Results

Upon completing this laboratory, you will:
- Successfully authenticate with Microsoft Foundry
- Understand the AI Project client initialization patterns
- Make basic chat completion requests
- Create and interact with AI agents
- Handle common error scenarios
- Save generated files and visualizations locally

## Additional Resources

- [Microsoft Foundry Documentation](https://learn.microsoft.com/azure/foundry/)
- [Microsoft Foundry RBAC](https://learn.microsoft.com/azure/foundry/concepts/rbac-foundry)
- [Azure AI Projects SDK](https://learn.microsoft.com/python/api/azure-ai-projects/)
- [Microsoft Foundry Agent Service](https://learn.microsoft.com/azure/foundry/agents/overview)
- [Authentication with Azure SDK](https://learn.microsoft.com/python/api/azure-identity/)

## Next Steps

After completing this laboratory, you will be prepared to advance to more specialized Microsoft Foundry labs, including advanced agent scenarios, tool integration, and multi-modal capabilities.
