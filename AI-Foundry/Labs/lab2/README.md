# Lab 2: Azure AI Services Ecosystem

## Overview

In this laboratory, you will explore the comprehensive AI services available in Azure Foundry, learning to integrate advanced artificial intelligence capabilities into your applications. The lab covers four essential service categories with practical examples: Speech, Language + Translator, Vision + Document, and Content Safety.

## Objectives

- ✅ Understand and utilize all major AI services in Azure Foundry
- ✅ Implement speech recognition and audio processing
- ✅ Explore natural language processing and translation capabilities
- ✅ Work with computer vision and document intelligence
- ✅ Apply content safety to detect and filter harmful content
- ✅ Integrate multiple services in practical scenarios

## Prerequisites

- Azure account with access to AI services
- Environment variables configured in the `.env` file at project root
- Basic Python knowledge
- Completion of Lab 1 (recommended)

## Laboratory Content

### Exercise 1 - Speech Service

Explore Azure AI Speech Service capabilities for audio processing:

**Key Features:**
- **Audio transcription**: Convert speech to text with high accuracy
- **Voice synthesis**: Produce natural voices from text-to-speech
- **Audio translation**: Translate spoken audio in real-time
- **Speaker recognition**: Identify different speakers in conversations
- **Custom voice**: Create personalized voices and vocabularies

**Practical Examples:**
- Continuous speech recognition from audio files
- Processing audio with silence handling
- Multi-language support and region configuration
- Real-time transcription capabilities

**Common Use Cases:**
- **Caption generation**: Subtitle synchronization with audio input
- **Audio content creation**: Audiobooks, voice assistants, navigation systems
- **Call center**: Real-time call transcription and batch processing
- **Language learning**: Pronunciation feedback and remote learning support
- **Voice assistants**: Natural, human-like conversational interfaces

**Required Environment Variables:**
- `SPEECH_ENDPOINT` - Azure Speech service endpoint
- `SPEECH_KEY` - Authentication key
- `SPEECH_REGION` - Azure region

### Exercise 2 - Language + Translator Services

Explore Azure AI Language Service, which unifies Text Analytics, QnA Maker, and LUIS capabilities:

**Core Text Analysis Features:**
- **Named Entity Recognition (NER)**: Identifies and categorizes entities in text
- **Personal and health information detection**: Identifies sensitive data (PII/PHI)
- **Language detection**: Recognizes diverse languages and dialects
- **Sentiment analysis and opinion mining**: Determines positive/negative sentiments and links to specific elements
- **Summarization**: Condenses information from text and conversations (extractive and abstractive)
- **Key phrase extraction**: Identifies main concepts in unstructured text
- **Entity linking**: Connects entities to Wikipedia for disambiguation
- **Text analytics for health**: Extracts relevant medical information from unstructured text

**Practical Examples:**
- Sentiment analysis with confidence scores
- Key phrase extraction from multiple documents
- Language detection for multilingual content
- Entity recognition and classification

**Custom Capabilities:**
- **Custom text classification**: Build models for document classification
- **Custom NER**: Create custom entity categories for domain-specific needs
- **Conversational Language Understanding (CLU)**: Build custom intent prediction models
- **Orchestration workflow**: Connect CLU, Q&A, and LUIS applications
- **Question answering**: Create custom Q&A systems from your knowledge base

**Required Environment Variables:**
- `AZURE_LANGUAGE_ENDPOINT` - Language service endpoint
- `AZURE_LANGUAGE_KEY` - Authentication key

### Exercise 3 - Vision + Document Intelligence

Explore Azure AI Vision Service for advanced image and document processing:

**Core Vision Features:**
- **OCR (Optical Character Recognition)**: Extract printed and handwritten text from images
- **Image Analysis**: Detect objects, faces, adult content, and generate automatic descriptions
- **Face API**: Detect, recognize, and analyze human faces in images
- **Video Retrieval**: Create searchable video indexes with natural language

**Practical Examples:**
- Complete image analysis with multiple visual features
- OCR text extraction from local and remote images
- Object detection with bounding boxes
- Smart cropping suggestions for different aspect ratios
- Comprehensive document layout analysis

**Document Intelligence:**
- **Prebuilt models**: Process invoices, receipts, business cards, ID documents
- **Layout analysis**: Extract tables, paragraphs, and key-value pairs
- **Custom models**: Train models for specific document types
- **Form recognition**: Structured data extraction from forms

**Real-World Applications:**
- Document automation for business processes
- Visual content analysis for e-commerce
- Accessibility features with automatic alt-text generation
- Content moderation and classification

**Required Environment Variables:**
- `AZURE_VISION_ENDPOINT` - Vision service endpoint
- `AZURE_VISION_KEY` - Authentication key
- `DOC_INTELLIGENCE_ENDPOINT` - Document Intelligence endpoint
- `DOC_INTELLIGENCE_KEY` - Document Intelligence key

### Exercise 4 - Content Safety

Implement Azure AI Content Safety for comprehensive content moderation:

**Content Safety Features:**
- **Prompt Shields**: Detects and prevents prompt injection attacks on LLMs
- **Grounding detection**: Verifies if LLM responses are grounded in provided source materials
- **Protected material detection**: Identifies known copyrighted text content
- **Custom categories (standard)**: Train custom content classification models
- **Custom categories (rapid)**: Define patterns for emerging harmful content
- **Text analysis API**: Examines text for sexual, violence, hate, and self-harm content
- **Image analysis API**: Examines images for harmful visual content

**Practical Examples:**
- Text content analysis with severity levels
- Image content moderation with confidence scores
- Comprehensive safety assessment for multiple content types
- Real-time content filtering for user-generated content

**Content Categories:**
- **Hate**: Attacks or uses discriminatory language
- **Self-harm**: Content promoting self-injury
- **Sexual**: Sexually explicit or suggestive content
- **Violence**: Content depicting violence or threats

**Severity Levels:**
- Level 0: Safe content
- Level 2: Low risk content
- Level 4: Medium risk content  
- Level 6: High risk content

**Required Environment Variables:**
- `CONTENT_SAFETY_ENDPOINT` - Content Safety service endpoint
- `CONTENT_SAFETY_KEY` - Authentication key

## Execution Instructions

1. **Environment Setup**:
   - Configure all necessary environment variables in the `.env` file
   - Ensure you have access to the respective Azure AI services

2. **Execution**:
   - Open the `lab2.ipynb` notebook in Azure AI Foundry or VS Code
   - Execute cells sequentially for each exercise
   - Observe the different service capabilities and outputs

3. **Experimentation**:
   - Test services with your own audio files, images, and text
   - Explore different configuration parameters
   - Try various content types to understand service capabilities

## Required Environment Variables

Configure the following variables in the `.env` file:

```bash
# Azure Speech Service
SPEECH_ENDPOINT=https://your-speech-service.cognitiveservices.azure.com/
SPEECH_KEY=your-speech-key
SPEECH_REGION=your-region

# Azure Language Service  
AZURE_LANGUAGE_ENDPOINT=https://your-language-service.cognitiveservices.azure.com/
AZURE_LANGUAGE_KEY=your-language-key

# Azure Vision Service
AZURE_VISION_ENDPOINT=https://your-vision-service.cognitiveservices.azure.com/
AZURE_VISION_KEY=your-vision-key

# Azure Document Intelligence
DOC_INTELLIGENCE_ENDPOINT=https://your-doc-intelligence.cognitiveservices.azure.com/
DOC_INTELLIGENCE_KEY=your-doc-intelligence-key

# Azure Content Safety
CONTENT_SAFETY_ENDPOINT=https://your-content-safety.cognitiveservices.azure.com/
CONTENT_SAFETY_KEY=your-content-safety-key
```

## Expected Results

Upon completing this laboratory, you will be able to:
- Implement speech recognition and text-to-speech functionality
- Perform comprehensive text analysis including sentiment, entities, and key phrases
- Analyze images and extract text using computer vision
- Process and understand document structure and content
- Implement content safety measures for text and images
- Choose the appropriate AI service for specific use cases

## Additional Resources

- [Azure AI Speech Service Documentation](https://learn.microsoft.com/azure/ai-services/speech-service/)
- [Azure AI Language Service Documentation](https://learn.microsoft.com/azure/ai-services/language-service/)
- [Azure AI Vision Service Documentation](https://learn.microsoft.com/azure/ai-services/computer-vision/)
- [Azure AI Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/)
- [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Azure AI Foundry Portal](https://ai.azure.com/)

## Next Steps

After completing this laboratory, you will be prepared to advance to Lab 3, where you will explore advanced prompt engineering techniques to optimize your interactions with AI models and create more effective AI-powered applications.
