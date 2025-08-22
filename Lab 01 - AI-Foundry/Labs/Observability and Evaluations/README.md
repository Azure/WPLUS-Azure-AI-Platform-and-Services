# Observability & Evaluations with Azure AI Foundry

## Introduction 

This lab provides hands-on experience with Azure AI Foundry's observability and evaluation capabilities. You'll learn how to implement comprehensive tracing for AI applications and evaluate model performance using both local and cloud-based evaluators with health & fitness themed examples.

## Objectives 
In this lab we will:
- Set up observability and tracing for Azure AI applications
- Configure OpenTelemetry instrumentation for AI inference calls
- Connect traces to Azure Monitor (Application Insights)
- Create and monitor AI agents with file search capabilities
- Perform local evaluations using F1 Score and AI-assisted evaluators
- Submit evaluation jobs to Azure AI Foundry for scalable processing
- Analyze evaluation results and metrics in the Azure AI Foundry portal

## Estimated Time 

60 minutes 

## Scenario

You are an AI developer responsible for monitoring and evaluating AI applications in production. You need to implement comprehensive observability to track AI model performance, troubleshoot issues, and ensure quality through systematic evaluation of model outputs using health and fitness domain examples.

## Pre-requisites

- Completed environment setup from previous notebook
- Azure credentials configured
- **azure-ai-projects** package version 1.0.0b12 or greater (`azure-ai-projects>=1.0.0b12`)
- **Azure AI User role** assigned to your account for the Azure AI Foundry project
  - See [Azure AI Foundry RBAC documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry?pivots=fdp-project) for more details on role assignments
- `.env` file configured with PROJECT_CONNECTION_STRING and MODEL_DEPLOYMENT_NAME
- Azure AI Foundry project already provisioned
- Application Insights resource connected to your Azure AI Foundry project

## Tasks


### Task 1 - Observability Setup and Basic LLM Calls

Configure observability infrastructure and test basic AI operations:
- Load environment variables and initialize AIProjectClient with browser-based authentication
- Perform basic LLM calls using Azure OpenAI client
- List and inspect project connections (Azure OpenAI, Azure AI Services)
- Verify model deployments and connectivity

Key components:
- Interactive browser credential authentication
- Project client initialization with health & fitness themed examples
- Connection validation and troubleshooting

### Task 2 - OpenTelemetry Instrumentation and Local Tracing

Enable comprehensive tracing for AI operations:
- Install and configure OpenTelemetry packages (`azure-monitor-opentelemetry`, `opentelemetry-instrumentation-openai-v2`)
- Set up environment variables for content recording (`OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT`)
- Configure Azure SDK tracing implementation
- Instrument Azure AI Inference and OpenAI SDK calls
- Set up console tracing for local debugging

Instrumentation features:
- Capture prompt and completion contents in traces
- Enable OpenAI v2 instrumentation using Microsoft's recommended approach
- Console span exporter for local trace visualization

### Task 3 - Azure Monitor Integration

Connect traces to Azure Monitor for cloud-based observability:
- Retrieve Application Insights connection string from Azure AI Foundry project
- Configure Azure Monitor with OpenTelemetry using `configure_azure_monitor()`
- Create custom spans with health-themed attributes
- Test traced AI operations with metadata collection
- Verify traces appear in Azure AI Foundry portal

Features demonstrated:
- Manual Azure Monitor setup with explicit provider creation
- Custom span attributes for operation categorization
- Token usage and model metadata tracking
- Integration with Azure AI Foundry tracing interface

### Task 4 - Agent-based Tracing with File Search

Implement advanced tracing for AI agents with document search:
- Create sample health resource files (recipes, dietary guidelines)
- Set up vector store with file uploads for semantic search
- Create Health Resource Agent with file search capabilities
- Implement enhanced tracing spans for agent operations
- Monitor multi-turn conversations with detailed attributes

Agent capabilities:
- File search tool integration for health and nutrition documents
- Thread and message management with tracing context
- Citation and reference system implementation
- Resource cleanup and lifecycle management

### Task 5 - Local Evaluation Setup

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

### Task 6 - Cloud-based Evaluation

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

**Observability Capabilities:**
- End-to-end tracing from local development to production
- Custom span creation with domain-specific attributes
- Integration with Azure Monitor and Application Insights
- Console and cloud-based trace visualization

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
   - Verify your Azure AI User role assignment and Application Insights connection

2. **Observability Execution**:
   - Open the `1-Observability.ipynb` notebook in Azure AI Foundry or VS Code
   - Execute cells sequentially, following the tracing setup process
   - Test basic LLM calls and verify console tracing output
   - Configure Azure Monitor integration and verify traces in portal
   - Create and interact with the Health Resource Agent

3. **Evaluation Execution**:
   - Open the `2-evaluation.ipynb` notebook
   - Execute data creation and local evaluation cells
   - Test cloud evaluation submission (requires proper Azure AI Foundry setup)
   - Review evaluation results and metrics

4. **Troubleshooting**:
   - Verify your PROJECT_CONNECTION_STRING is correctly set
   - Ensure Application Insights resource is connected to your project
   - Check Azure AI User role permissions for evaluation operations
   - Review authentication error messages for guidance

## Expected Results

Upon completing this laboratory, you will:
- Successfully implement comprehensive observability for AI applications
- Understand OpenTelemetry instrumentation patterns for Azure AI services
- Monitor AI operations through Azure Monitor and Azure AI Foundry portal
- Create and trace AI agents with advanced tool capabilities
- Perform both local and cloud-based evaluations of AI models
- Analyze evaluation metrics and interpret quality assessments
- Implement production-ready monitoring and evaluation workflows

## Additional Resources

- [Azure AI Foundry Observability Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability)
- [Azure AI Evaluation SDK](https://learn.microsoft.com/python/api/azure-ai-evaluation/azure.ai.evaluation)
- [OpenTelemetry for Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/develop/trace-your-app)
- [Azure Monitor Integration](https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry)
- [Evaluating Generative AI Applications](https://learn.microsoft.com/azure/ai-foundry/how-to/evaluate-generative-ai-app)

## Next Steps

After completing this laboratory, you will be prepared to implement production-ready observability and evaluation systems for AI applications, including advanced monitoring scenarios, custom evaluators, and enterprise-scale evaluation workflows.
