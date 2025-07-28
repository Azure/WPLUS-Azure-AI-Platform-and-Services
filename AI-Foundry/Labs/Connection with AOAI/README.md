# Connection and First Steps with Azure OpenAI

## Overview

In this lab, you will take the first steps with Azure OpenAI Service, learning from initial configuration to advanced practical tasks. The lab covers API calls, detailed response analysis, embedding generation, image processing with multimodal models, and exploration of other LLM models available in Azure AI Foundry.

## Objectives

- ✅ Configure and connect with Azure OpenAI Service
- ✅ Perform basic and advanced calls to the chat completions API
- ✅ Analyze API responses and metadata in detail
- ✅ Generate and work with text embeddings for semantic analysis
- ✅ Process images using multimodal models (computer vision)
- ✅ Explore other LLM models available in Azure AI Foundry
- ✅ Complete practical activities to consolidate learning

## Prerequisites

- Azure account with access to Azure OpenAI Service
- Environment variables configured in the `.env` file at project root
- Basic Python knowledge
- Access to Azure AI Foundry

## Laboratory Content

### Exercise 1 - API Call

Configure the Azure OpenAI client and make your first API call:
- Import necessary libraries (openai, dotenv)
- Load credentials from `.env` file
- Initialize Azure OpenAI client
- Structure messages with different roles (system, user, assistant)
- Execute chat completion calls with context

### Exercise 2 - Analyzing the Response

Explore in detail the complete structure of the API response:
- Metadata analysis (ID, model, timestamp)
- Detailed token usage information
- Content filtering and security evaluations
- Prompt and completion token counters
- Reasoning token details for advanced models
- Structured JSON response formatting

Experiment with important parameters:
- **max_completion_tokens**: Control response size
- **temperature**: Adjust creativity (0.0 = deterministic, 1.0 = creative)
- **top_p**: Control diversity via nucleus sampling
- **frequency_penalty**: Penalization for frequency-based repetition
- **presence_penalty**: Penalization for repetition independent of frequency

### Exercise 3 - Embeddings

Learn to work with embeddings for semantic analysis:
- Generate embeddings from text using Azure OpenAI
- Understand vectorial representations of semantic meaning
- Use cases for semantic search, classification, and similarity analysis
- Compare similarity between related words

Explore embedding storage options in Azure:
- Azure AI Search (vector search)
- Azure Cosmos DB (MongoDB vCore, NoSQL, PostgreSQL)
- Azure SQL Database (vector search)
- Azure Cache for Redis (vector similarity)
- Azure Database for PostgreSQL (pgvector)
- Microsoft Fabric Eventhouse (vector database)
### Exercise 4 - Image Processing

Learn to work with multimodal models for computer vision:
- Send images via public URL
- Encode local images to base64
- Combine text and images in multimodal prompts
- Automatic description and detailed image analysis
- Process different types of visual content

### Exercise 5 - Other Models in Azure AI Foundry

Explore the diversity of models available through the Model Catalog:
- **Microsoft Models**: OpenAI, Meta, Mistral AI, Deepseek, xAI, Black Forest Labs
- **Partner Models**: Nixtla, AI21, NTT Data, Core42, NVIDIA NIM, Stability AI
- Configuration of different client libraries (azure-ai-inference)
- Practical example with Phi-4 model
- Different deployment and availability modes

### 🎯 Practical Activities Included

The laboratory includes 5 practical activities to consolidate learning:

1. **Temperature Testing**: Experiment how different temperature values affect creativity
2. **Embedding Comparison**: Analyze similarity between related words
3. **Image Analysis with Different Prompts**: Test various types of questions for the same image
4. **Token Counter**: Understand how prompt size affects consumption
5. **Persona Testing**: Explore how different system messages create distinct personalities

### Advanced Features Presented

The laboratory presents other advanced Azure OpenAI functionalities:
- **Responses API**: Multiple response alternatives
- **Reasoning Models**: Models with reasoning capability (o1)
- **Computer Use**: User interface interaction
- **Model Router**: Intelligent routing between models
- **Function Calling**: External function calling
- **Predicted Outputs**: Completion optimization
- **Prompt Caching**: Prompt caching for efficiency
- **Structured Outputs**: Structured format outputs
- **Vision-enabled Chats**: Conversations with image support
- **JSON Mode**: Structured JSON responses
- **Reproducible Output**: Consistent results

## Execution Instructions

1. **Initial Setup**:
   - Configure environment variables in the `.env` file at repository root
   - Ensure you have access to Azure OpenAI Service

2. **Execution**:
   - Open the `lab1.ipynb` notebook in Azure AI Foundry or VS Code
   - Execute cells sequentially, observing examples and results
   - Experiment with modifying parameters to understand their impact

3. **Experimentation**:
   - Test with your own custom prompts
   - Experiment with different images (URLs or local)
   - Modify parameters in practical activities

## Expected Results

Upon completing this laboratory, you will be able to:
- Connect and use Azure OpenAI Service effectively
- Analyze and interpret detailed API responses
- Generate and compare embeddings for semantic analysis
- Process images with multimodal models
- Choose and configure different models from Azure AI Foundry
- Apply basic prompt engineering techniques

## Additional Resources

- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [How to work with embeddings](https://learn.microsoft.com/azure/ai-services/openai/how-to/embeddings)
- [Azure AI Foundry Model Catalog](https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview)
- [Chat Completions API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt)
- [Function Calling](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling)
- [Structured Outputs](https://learn.microsoft.com/azure/ai-services/openai/how-to/structured-outputs)
- [Vision-enabled Chats](https://learn.microsoft.com/azure/ai-services/openai/how-to/gpt-with-vision)

## Next Steps

After completing this laboratory, you will be prepared to advance to Lab 2, where you will explore the comprehensive Azure AI Services ecosystem beyond OpenAI.
