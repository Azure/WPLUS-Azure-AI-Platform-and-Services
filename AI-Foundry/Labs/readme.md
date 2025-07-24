# Azure AI Foundry Workshop

This repository contains a comprehensive series of hands-on laboratories designed to explore and master Azure AI services, with a special focus on Azure AI Foundry and its ecosystem. The workshop provides a complete learning journey from basic concepts to advanced AI implementations.

## Workshop Overview

This comprehensive workshop offers a complete journey through the latest capabilities of Azure AI Foundry, from fundamental concepts to advanced AI implementations. Each laboratory is carefully designed to build knowledge progressively, enabling you to master essential tools and techniques for modern AI development.

The workshop covers 6 progressive laboratories that explore everything from basic Azure OpenAI connections to complex multi-agent systems, RAG implementations, and advanced observability patterns. Each lab includes practical exercises, real examples, and hands-on activities to consolidate learning.

## Laboratory Structure

### [Lab 1: Connection and First Steps with Azure OpenAI](lab1/)
**Fundamentals and API Mastery**

Learn the fundamentals of Azure OpenAI through hands-on practice:
- Azure OpenAI Service configuration and connection
- Basic and advanced API calls with chat completions
- Detailed analysis of API responses and metadata
- Generation and comparison of text embeddings for semantic analysis
- Image processing with multimodal models (computer vision)
- Exploration of other LLM models available in Azure AI Foundry Model Catalog
- 5 practical activities to consolidate learning

**Key Topics Covered:**
- Client configuration and authentication
- Important parameters (temperature, top_p, frequency_penalty, presence_penalty)
- Token usage analysis and cost optimization  
- Embeddings and their practical applications
- Multimodal prompts with images
- Other models via azure-ai-inference library

**Advanced Features Presented:**
- Responses API, Reasoning Models, Computer Use, Model Router
- Function Calling, Predicted Outputs, Prompt Caching
- Structured Outputs, Vision-enabled Chats, JSON Mode

### [Lab 2: Azure AI Services Ecosystem](lab2/)
**Complete Suite of AI Services**

Deep exploration of Azure AI services beyond OpenAI:
- **Azure AI Speech**: Speech-to-text, text-to-speech, audio translation
- **Azure AI Language + Translator**: Sentiment analysis, NER, key phrase extraction, translation
- **Azure AI Vision + Document**: OCR, image analysis, object detection, document processing
- **Azure AI Content Safety**: Text and image content moderation

**Practical Examples:**
- Continuous speech recognition from audio files
- Sentiment analysis with confidence scores
- Complete image analysis with multiple features
- Document intelligence for structured data extraction
- Content safety for text and image moderation

**Real Use Cases:**
- Call center transcription and analysis
- Multi-language content processing
- Document automation for business processes
- Content moderation systems

### [Lab 3: Prompt Engineering Mastery](lab3/)
**Advanced Prompt Engineering Techniques**

Master the art and science of prompt engineering:
- **Zero-Shot Prompting**: Creating effective prompts without examples
- **Few-Shot Prompting**: Quality improvement with targeted examples  
- **Chain-of-Thought Prompting**: Encouraging step-by-step reasoning
- **Meta Prompting**: Instructions on how to approach different tasks
- **Prompt Chaining**: Breaking complex tasks into focused sequences
- **Tree of Thoughts (ToT)**: Exploring multiple reasoning paths
- **Retrieval Augmented Generation (RAG)**: Combining external information
- **Active-Prompt**: Dynamically adapting prompts based on context

**Structure and Content:**
- Complete theoretical explanation of each technique
- Practical examples with Azure OpenAI
- Comparison of results between different approaches
- Hands-on exercises and experiments
- Best practices and common pitfalls

**Best Practices Covered:**
- Specificity and clarity in instructions
- Effective use of examples and analogies  
- Importance of order and structure
- Fallback strategies and error handling

### [Lab 4: AI Frameworks - Semantic Kernel and AutoGen](lab4/)
**Building with Specialized Frameworks**

Explore powerful frameworks for advanced AI applications:
- **Semantic Kernel**: Microsoft's SDK for LLM integration with conventional code
- **AutoGen**: Framework for multi-agent conversational AI systems

**Semantic Kernel Concepts:**
- Kernel configuration and AI service integration
- Creating and using plugins (built-in and custom)
- Function orchestration and planning
- Prompt templates and argument handling

**AutoGen Features:**
- Creating specialized conversational agents
- Multi-agent collaboration and group chats
- Agent roles and conversation flows
- Practical examples with Azure OpenAI

**Practical System:**
- Complete product analysis system implementation
- Integration between Semantic Kernel and AutoGen
- When to use each framework
- Architecture and deployment considerations

**Real Examples:**
- Custom math plugin creation
- Sentiment analysis plugin
- Creative assistant agents
- Multi-agent product review system

### [Lab 5: RAG Implementation with Azure AI Search](lab5/)
**Retrieval-Augmented Generation Patterns**

Complete implementation of RAG systems:
- Fundamental RAG concepts and architecture
- Azure OpenAI and Azure AI Search configuration
- Knowledge base creation and indexing
- Complete RAG pipeline implementation
- Quality comparison: with vs. without RAG

**Implementation Components:**
- Document preparation and embedding generation
- Semantic search simulation (cosine similarity)
- Context integration with generation
- Real implementation with Azure AI Search
- Performance optimization and best practices

**Advanced Techniques:**
- Document chunking strategies
- Embedding storage options in Azure
- Semantic filtering and reranking
- Cache and performance optimization
- Quality evaluation metrics

**Expected Results:**
- Understand when and how to use RAG
- Implement production-ready RAG systems
- Integrate multiple Azure services effectively
- Apply best practices for accuracy and performance

### [Lab 6: Azure AI Content Understanding with REST API](lab6/)
**Multimodal Content Analysis and Processing**

Master Azure AI Content Understanding service for extracting structured data from documents, images, audio, and video files using REST API calls with production-ready Python implementations.

**Core Capabilities:**
- **Document Analysis**: Extract text, layout, tables, and structured data from PDFs, Office documents, and web content
- **Image Processing**: Analyze visual content, detect objects, and extract insights from images
- **Audio Analysis**: Process speech, transcription, and audio content classification
- **Video Understanding**: Analyze video content, scene detection, and multimodal insights

**Implementation Features:**
- Secure authentication with environment variables and Azure best practices
- Robust error handling with exponential backoff retry logic
- Production-ready client with proper resource management
- Comprehensive result processing and display utilities
- Support for multiple analyzer types and content formats

**Technical Components:**
- REST API client implementation following Azure SDK patterns
- Asynchronous operation handling with polling mechanisms
- Content validation and pre-flight checks
- Structured data extraction and formatting
- Integration patterns for enterprise workflows

**Advanced Patterns:**
- Multi-analyzer content processing pipelines
- Batch processing strategies for large datasets
- Content safety integration for compliance
- Performance optimization and cost management
- Monitoring and logging for production deployments

**Expected Outcomes:**
- Build production-ready content understanding applications
- Implement secure and scalable document processing workflows
- Extract actionable insights from multimodal content
- Apply Azure development best practices for AI services

### [Lab 7: Observability and Evaluations](lab7-observability-and-evaluations/)
**AI Model Monitoring and Quality Assessment**

Master observability and evaluation techniques for AI applications using Azure AI Foundry's comprehensive monitoring and assessment capabilities.

**Core Components:**
- **1-Observability.ipynb**: Comprehensive tracing and monitoring setup with health & fitness themed examples
- **2-evaluation.ipynb**: AI model quality and safety evaluations with practical datasets
- **Sample Data**: Health and fitness evaluation datasets (evaluate_test_data.jsonl, health_fitness_eval_data.jsonl)

**Observability Features:**
- **OpenTelemetry Integration**: Complete tracing setup for AI applications using azure-ai-projects and azure-ai-inference
- **Azure Monitor Connection**: Send traces to Application Insights for visualization in Azure AI Foundry
- **Multi-Agent Tracing**: Monitor complex multi-agent system interactions and workflows
- **Real-time Monitoring**: Track performance, token usage, response times, and API calls
- **Debug Capabilities**: Trace message flows, identify bottlenecks, and troubleshoot issues

**Evaluation Capabilities:**
- **AI Quality Metrics**: Groundedness, relevance, coherence, fluency, GPT similarity assessments
- **NLP Metrics**: F1 score, ROUGE, BLEU, GLEU, METEOR scores for comprehensive text analysis
- **Risk and Safety**: Violence, sexual content, self-harm, hate/unfairness, protected material detection
- **Local vs Cloud**: Run evaluations locally or submit jobs to Azure AI Foundry for scalable processing
- **Batch Processing**: Scale evaluations across large datasets with cloud infrastructure

**Technical Implementation:**
- Tracing setup with fallback mechanisms and error handling
- Robust authentication patterns (DefaultAzureCredential, InteractiveBrowserCredential)
- Comprehensive error handling, retry logic, and graceful degradation
- Integration with Azure AI Foundry portal for trace visualization and analysis
- Support for custom evaluators, metrics, and evaluation workflows

**Practical Applications:**
- Monitor AI agent performance and behavior in production environments
- Evaluate model quality, safety, and compliance before deployment
- Assess risk and safety requirements for enterprise AI applications
- Debug complex multi-agent workflows and conversation flows
- Optimize AI system performance, costs, and resource utilization

**Health & Fitness Theme:**
- Educational examples using health and fitness scenarios for engaging learning
- Sample conversations and data related to wellness, nutrition, and fitness advice
- Demonstrates real-world AI applications while maintaining educational focus
- Includes proper disclaimers for health-related AI content

**Expected Outcomes:**
- Implement comprehensive AI observability solutions for production systems
- Build quality assessment pipelines for AI applications and models
- Monitor and optimize AI system performance, costs, and reliability
- Ensure safety, compliance, and responsible AI practices in deployments
- Debug and troubleshoot complex AI workflows and multi-agent systems

## Prerequisites

### Required
- Azure subscription with access to Azure OpenAI Service
- Python 3.8 or higher
- Basic knowledge of programming and APIs
- Access to Azure AI Foundry

### Recommended
- Visual Studio Code with Azure and Python extensions
- Azure CLI for command-line interactions
- Git for version control
- Basic understanding of machine learning concepts

## Initial Setup

### 1. Environment Preparation
```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
# Edit .env with your Azure credentials

# Verify setup
python check_environment.py
```

### 2. Azure Services Required
- Azure OpenAI Service (required for all labs)
- Azure AI Speech (Lab 2)
- Azure AI Language (Lab 2)  
- Azure AI Vision (Lab 2)
- Azure AI Content Safety (Lab 2)
- Azure AI Search (Lab 5)
- Azure AI Foundry Project (Lab 7 - Observability and Evaluations)

### 3. Environment Variables Configuration
Complete template available in `.env.example`. Key variables:

```env
# Azure OpenAI (required)
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
API_VERSION=2024-02-01

# Additional services as needed per lab
AZURE_LANGUAGE_ENDPOINT=...
AZURE_VISION_ENDPOINT=...
AZURE_SEARCH_ENDPOINT=...
AZURE_AI_ENDPOINT=...  # Lab 6: Content Understanding
AZURE_AI_KEY=...       # Lab 6: Content Understanding
PROJECT_CONNECTION_STRING=...  # Lab 7: Azure AI Foundry Project for observability and evaluations
```

## Recommended Progression

1. **Beginners**: Start with Lab 1 to understand fundamentals, then proceed sequentially
2. **Intermediate**: Labs 1-3 provide a solid foundation in generative AI and prompt engineering
3. **Advanced**: Labs 4-5 address complex architectures, frameworks, and RAG patterns
4. **Enterprise**: Labs 6-7 focus on production deployment, monitoring, and quality assurance
5. **Specialization**: Focus on specific laboratories based on your project needs

**Estimated Time:**
- Lab 1: 2-3 hours (foundations)
- Lab 2: 2-3 hours (AI services)
- Lab 3: 1-2 hours (prompt engineering)
- Lab 4: 2-3 hours (frameworks)
- Lab 5: 2-3 hours (RAG implementation)
- Lab 6: 2-3 hours (content understanding)
- Lab 7: 2-3 hours (observability and evaluations)

## Learning Outcomes

Upon completing this workshop, you will be able to:

✅ **Master Azure AI Foundry**: Navigate the platform and use all major features effectively
✅ **Develop Complete AI Solutions**: Build end-to-end AI applications with Azure services  
✅ **Apply Advanced Prompt Engineering**: Optimize interactions with language models using proven techniques
✅ **Implement RAG Patterns**: Combine retrieval and generation for precise, knowledge-grounded responses
✅ **Use Specialized Frameworks**: Choose and implement Semantic Kernel, AutoGen based on requirements
✅ **Integrate Multiple AI Services**: Combine speech, vision, language, and content safety services
✅ **Process Multimodal Content**: Extract insights from documents, images, audio, and video files
✅ **Monitor and Evaluate AI Systems**: Implement comprehensive observability and quality assessment
✅ **Follow Best Practices**: Implement proper security, governance, and optimization patterns
✅ **Handle Real-World Scenarios**: Build production-ready AI solutions with monitoring and evaluation

## Additional Resources

### Official Documentation
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Services](https://learn.microsoft.com/azure/ai-services/)
- [Azure AI Search](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)
- [AutoGen Framework](https://github.com/microsoft/autogen)

### Tutorials and Guides
- [Prompt Engineering Guide](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- [RAG Patterns and Best Practices](https://learn.microsoft.com/azure/architecture/pattern/ai/retrieval-augmented-generation-pattern)
- [Responsible AI Guidelines](https://www.microsoft.com/ai/responsible-ai)
- [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)

### Community and Support
- [Microsoft Learn - AI Learning Paths](https://learn.microsoft.com/training/browse/?products=azure-cognitive-services)
- [Azure AI Tech Community](https://techcommunity.microsoft.com/category/azure-ai)
- [GitHub - Azure AI Samples](https://github.com/Azure-Samples/azure-ai-samples)

## Troubleshooting

### Common Issues
- **Access denied errors**: Verify Azure subscription permissions and Azure AI Foundry access
- **Quota limits**: Check Azure quotas for AI services in your region  
- **Network connectivity**: Ensure proper firewall and network configuration
- **Environment variables**: Use `python check_environment.py` to verify setup

### Getting Help
- Check the troubleshooting section in each laboratory README
- Review Azure AI Foundry documentation for service-specific issues
- Use the `check_environment.py` script to diagnose setup problems
- Check `SETUP.md` for detailed configuration instructions

## File Structure

```
├── requirements.txt          # All dependencies for the workshop
├── .env.example             # Environment variables template  
├── SETUP.md                 # Detailed setup instructions
├── check_environment.py     # Environment verification script
├── samples/                 # Sample files for exercises
└── labs/
    ├── english/
    │   ├── readme.md        # This file
    │   ├── lab1/            # Azure OpenAI fundamentals
    │   ├── lab2/            # Azure AI Services
    │   ├── lab3/            # Prompt Engineering
    │   ├── lab4/            # Semantic Kernel & AutoGen
    │   ├── lab5/            # RAG Implementation
    │   ├── lab6/            # Content Understanding
    │   └── lab7-observability-and-evaluations/  # AI Observability and Evaluations
    └── portuguese/          # Portuguese version
```

## Next Steps

After completing this workshop, consider:

- **Azure AI Certifications**: Explore AI-102 (Azure AI Engineer) and AI-900 (Azure AI Fundamentals)
- **Production Deployment**: Implement your solutions in real-world scenarios using Azure Container Apps or App Service
- **Advanced Topics**: Explore Azure Machine Learning, MLOps, and custom model training
- **Community Engagement**: Join AI developer communities and contribute to open-source projects
- **Continuous Learning**: Stay updated with the latest Azure AI innovations and features

---

*This workshop provides hands-on experience with the latest Azure AI technologies through a structured, progressive learning approach. Each laboratory builds upon previous knowledge while introducing new concepts and practical applications.*

**Ready to begin your Azure AI journey?** Start with [Lab 1](lab1/) and explore the foundations of Azure OpenAI!
