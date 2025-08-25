# Evaluations with Azure AI Foundry

## Introduction 

This lab provides hands-on experience with Azure AI Foundry's evaluation capabilities. You'll learn how to evaluate model performance using both local and cloud-based evaluators with health & fitness themed examples.

## Objectives 
In this lab we will:
- Perform local evaluations using F1 Score and AI-assisted evaluators
- Submit evaluation jobs to Azure AI Foundry for scalable processing
- Analyze evaluation results and metrics in the Azure AI Foundry portal

## Estimated Time 

45 minutes 

## Scenario

You are an AI developer responsible for evaluating AI applications in production. You need to ensure quality through systematic evaluation of model outputs using health and fitness domain examples.

## Pre-requisites

- Completed environment setup from previous notebook
- Azure credentials configured
- **azure-ai-projects** package version 1.1.0b2 or greater (`azure-ai-projects>=1.1.0b2`)
- **Azure AI User role** assigned to your account for the Azure AI Foundry project
  - See [Azure AI Foundry RBAC documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry?pivots=fdp-project) for more details on role assignments
- `.env` file configured with PROJECT_CONNECTION_STRING and MODEL_DEPLOYMENT_NAME
- Azure AI Foundry project already provisioned

## Tasks

### Task 1 - Environment Setup and Basic Configuration

Configure evaluation environment and test basic AI operations:
- Load environment variables and initialize AIProjectClient with browser-based authentication
- Perform basic LLM calls using Azure OpenAI client
- List and inspect project connections (Azure OpenAI, Azure AI Services)
- Verify model deployments and connectivity

Key components:
- Interactive browser credential authentication
- Project client initialization with health & fitness themed examples
- Connection validation and troubleshooting

### Task 2 - Local Evaluation Setup

Perform local model evaluations using built-in metrics:
- Create synthetic health & fitness Q&A evaluation data
- Configure F1Score evaluator for precision-recall analysis
- Set up AI-assisted Relevance evaluator (when Azure OpenAI is available)
- Run local evaluations with error handling and fallbacks
- Generate comprehensive evaluation reports

Evaluation features:
- NLP-based metrics (F1 Score) for basic quality assessment
- AI-assisted evaluators for relevance and coherence
- Robust error handling for missing dependencies
- Health and fitness domain-specific test data

### Task 3 - Cloud-based Evaluation

Submit evaluations to Azure AI Foundry for scalable processing:
- Configure Azure AI Project client for cloud evaluations
- Upload evaluation data and results to Azure AI Foundry
- Monitor evaluation jobs in the Azure AI Foundry portal
- Access advanced metrics and visualization capabilities
- Compare local vs. cloud evaluation results

Cloud evaluation advantages:
- Scalability for large datasets
- Advanced visualization in Azure AI Foundry portal
- Support for all built-in and custom evaluators
- Integration with Azure AI Foundry project workflows

### Laboratory Features

**Evaluation Framework:**
- Multiple evaluation types: NLP metrics and AI-assisted evaluators
- Quality metrics: F1 Score, Relevance, Groundedness, Coherence, Fluency
- Risk and safety evaluators for responsible AI practices
- Local and cloud evaluation workflows

**Error Handling and Resilience:**
- Comprehensive error handling for authentication failures
- Fallback mechanisms for missing services or credentials
- Clear troubleshooting guidance and status reporting
- Graceful degradation when cloud services are unavailable

## Execution Instructions

1. **Initial Setup**:
   - Ensure you have completed the environment setup from previous notebooks
   - Configure environment variables in the `.env` file at repository root
   - Verify your Azure AI User role assignment

2. **Evaluation Execution**:
   - Open the `1-evaluation.ipynb` notebook in Azure AI Foundry or VS Code
   - Execute data creation and local evaluation cells
   - Test cloud evaluation submission (requires proper Azure AI Foundry setup)
   - Review evaluation results and metrics

3. **Troubleshooting**:
   - Verify your PROJECT_CONNECTION_STRING is correctly set
   - Check Azure AI User role permissions for evaluation operations
   - Review authentication error messages for guidance

## Expected Results

Upon completing this laboratory, you will:
- Perform both local and cloud-based evaluations of AI models
- Analyze evaluation metrics and interpret quality assessments
- Implement production-ready evaluation workflows

## Additional Resources

- [Azure AI Evaluation SDK](https://learn.microsoft.com/python/api/azure-ai-evaluation/azure.ai.evaluation)
- [Evaluating Generative AI Applications](https://learn.microsoft.com/azure/ai-foundry/how-to/evaluate-generative-ai-app)

## Next Steps

After completing this laboratory, you will be prepared to implement production-ready evaluation systems for AI applications, including custom evaluators and enterprise-scale evaluation workflows.
