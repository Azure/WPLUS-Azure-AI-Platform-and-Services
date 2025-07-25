# AI Frameworks - Semantic Kernel and AutoGen

## Overview

In this laboratory, you will explore advanced frameworks for building intelligent applications: **Semantic Kernel** and **AutoGen** with Azure OpenAI. You'll learn how to create conversational agents, orchestrate multiple agents, implement custom plugins, and develop complex automation workflows.

**Semantic Kernel** is Microsoft's open-source SDK that enables integrating AI models (like Azure OpenAI) with conventional programming languages, offering features like plugins, planning, and memory management.

**AutoGen** is Microsoft's framework for creating multi-agent applications where different agents can collaborate to solve complex problems through structured conversation.

## Objectives

- ✅ Master Semantic Kernel for AI orchestration and plugin development
- ✅ Understand AutoGen for multi-agent conversational systems
- ✅ Create custom plugins and specialized agents
- ✅ Implement complex workflows with both frameworks
- ✅ Compare when to use each framework for different scenarios
- ✅ Build a practical product analysis system combining both technologies

## Prerequisites

- Azure account with access to Azure OpenAI Service
- Environment variables configured in the `.env` file at repository root
- Basic Python knowledge
- Completion of previous labs (recommended)
- Understanding of async programming concepts

## Laboratory Content

### Exercise 1 - Initial Setup and Semantic Kernel

**Framework Installation and Configuration:**
- Install Semantic Kernel and AutoGen dependencies
- Configure Azure OpenAI credentials
- Initialize clients and test connectivity

**Semantic Kernel Fundamentals:**
- Kernel initialization and AI service configuration
- Creating simple functions with prompt templates
- Understanding KernelArguments and function parameters
- Basic function execution and result handling

### Exercise 2 - Plugins and Advanced Features

**Working with Built-in Plugins:**
- Using TextPlugin for text manipulation
- Understanding plugin architecture and capabilities
- Function chaining and orchestration

**Creating Custom Plugins:**
- Developing specialized plugins for mathematical operations
- Using decorators and annotations for function definition
- Parameter typing and validation
- Error handling in plugin functions

**Practical Example:**
- MathPlugin with average calculation and maximum finding
- Integration with kernel and function execution
- Testing and validation of custom functionality

### Exercise 3 - Introduction to AutoGen

**AutoGen Core Concepts:**
- Understanding agents, conversations, and roles
- Agent specialization and system message configuration
- Conversation flow and termination conditions
- Group chat and multi-agent collaboration

**Basic Configuration:**
- Setting up Azure OpenAI model client (v0.6+ API)
- Creating AssistantAgent with specialized roles
- Configuring model parameters and behavior
- Understanding the new AutoGen API structure

**Simple Conversation Example:**
- Creative assistant agent for idea generation
- Task-based conversation execution
- Result handling and message processing

### Exercise 4 - Framework Comparison and Best Practices

**When to Use Semantic Kernel vs AutoGen:**

**Semantic Kernel is ideal for:**
- AI orchestration with traditional code
- Creating reusable plugins and functions
- Applications needing automatic planning
- Integration with existing systems
- Single-agent applications with complex functionality

**AutoGen is ideal for:**
- Complex multi-agent systems
- Discussion and brainstorming simulations
- Workflows involving multiple perspectives
- Distributed decision-making systems
- Collaborative automation processes

**Practical Use Cases:**

1. **Customer Service System**
   - Semantic Kernel: Plugins for order queries, product information, etc.
   - AutoGen: Specialized agents (triage, sales, technical support)

2. **Corporate Document Analysis**
   - Semantic Kernel: Functions for text extraction and processing
   - AutoGen: Reviewer, analyst, and domain expert agents

3. **Project Planning**
   - Semantic Kernel: Plugins for schedule and resource calculations
   - AutoGen: Agents representing different stakeholders

4. **Recommendation System**
   - Semantic Kernel: Functions for filtering and similarity calculation
   - AutoGen: Agents with different recommendation criteria

### Exercise 5 - Practical System: Product Analysis

**Complete Implementation:**
Build a product analysis system that combines both frameworks:

**Semantic Kernel Components:**
- Sentiment analysis plugin for customer feedback
- Mathematical operations for score calculations
- Text processing utilities

**AutoGen Components:**
- Creative assistant agent for idea generation
- Multi-agent product review discussions
- Collaborative decision-making processes

**System Features:**
- Automated sentiment analysis of product reviews
- Multi-perspective analysis through different agents
- Integration between custom plugins and agent conversations
- Practical business intelligence application

## Execution Instructions

1. **Environment Setup**:
   - Ensure Azure OpenAI Service is configured in `.env`
   - Install required dependencies for both frameworks
   - Verify async execution environment

2. **Progressive Learning**:
   - Start with Semantic Kernel basics and simple functions
   - Progress to custom plugin development
   - Move to AutoGen concepts and agent creation
   - Combine both frameworks in practical examples

3. **Hands-on Practice**:
   - Execute all code examples and observe results
   - Modify parameters and configurations to understand impact
   - Create your own plugins and agents
   - Test different conversation flows and scenarios

4. **Experimentation**:
   - Try different agent personalities and roles
   - Experiment with various plugin functionalities
   - Test integration between frameworks
   - Explore advanced features and capabilities

## Expected Results

Upon completing this laboratory, you will be able to:
- Design and implement custom Semantic Kernel plugins
- Create specialized AutoGen agents for different roles
- Choose the appropriate framework based on requirements
- Orchestrate complex workflows with multiple AI components
- Integrate traditional programming with AI capabilities
- Build production-ready multi-agent systems
- Apply best practices for framework selection and implementation

## Advanced Topics Covered

**Semantic Kernel Advanced Features:**
- Custom plugin development with proper typing
- Function orchestration and chaining
- Error handling and validation patterns
- Integration with external APIs and services

**AutoGen Advanced Concepts:**
- Agent specialization and role definition
- Conversation flow management
- Multi-agent collaboration patterns
- New API features and improvements (v0.6+)

**Integration Patterns:**
- Combining plugins with agents
- Hybrid architectures using both frameworks
- Performance optimization strategies
- Scalability considerations

## Additional Resources

- [Semantic Kernel Documentation](https://learn.microsoft.com/semantic-kernel/)
- [AutoGen Framework](https://github.com/microsoft/autogen)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)
- [Multi-Agent Systems Design](https://learn.microsoft.com/azure/architecture/guide/ai/multi-agent-systems)
- [Plugin Development Best Practices](https://learn.microsoft.com/semantic-kernel/concepts-ai/plugins)

## Next Steps

After completing this laboratory, you will be prepared to build sophisticated AI applications using advanced frameworks. You'll be ready to proceed to Lab 5, where you'll explore RAG (Retrieval-Augmented Generation) implementations for creating knowledge-grounded AI applications.
