# GraphRAG Hands-on Setup Guide

## Prerequisites

- Python 3.10 to 3.12 environment
- Azure OpenAI Service resource
- Text embedding model: `text-embedding-ada-002`
- LLM: `gpt-4o-mini`

---

## Installation & Setup

```bash
# Create working directory
mkdir graphrag && cd graphrag

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install GraphRAG
pip install graphrag

# Initialize workspace
mkdir -p ragtest/input
graphrag init --root ragtest
```

## Explore Initialized Workspace

```bash

# List files
find -f ./ragtest
```

Expected files:

- `settings.yaml`
- `.env`
- `prompts/` (contains prompt templates)

## Get Source Data

```bash
# Download sample text
curl -L https://aka.ms/dickens/xmas -o ./ragtest/input/book.txt

# Verify download
wc ./ragtest/input/book.txt
```

## Configure .env

```bash
# Edit .env file
vi ragtest/.env

# Add your Azure OpenAI API key
GRAPHRAG_API_KEY=<your_api_key>
```

## Update settings.yaml

```yaml

llm:
  type: azure_openai_chat
  model: gpt-4o-mini
  api_base: https://<instance>.openai.azure.com
  api_version: 2024-02-15-preview
  deployment_name: gpt-4o-mini

embeddings:
  type: azure_openai_chat
  model: text-embedding-ada-002
  api_base: https://<instance>.openai.azure.com
  api_version: 2024-02-15-preview
  deployment_name: text-embedding-ada-002

snapshots:
  graphml: true

```

## Run first index

```bash

# Run indexing pipeline
graphrag index --root ./ragtest

# Review output
ls ./ragtest/output

```

## Run first queries

### Global Query

```bash
graphrag query \
  --root ./ragtest \
  --method global \
  --query "What are the top themes in this story?"
```

### Local Query

```bash
graphrag query \
  --root ./ragtest \
  --method local \
  --query "Who is Scrooge and what are his main relationships?"

```


### DRIFT Query

```bash
graphrag query \
  --root ./ragtest \
  --method drift \
  --query "Who is Scrooge and what are his main relationships?"

```

## Introduce Domain Expertise with Auto-tuning of the Indexing Prompts

```bash
graphrag prompt-tune \
  --root ./ragtest \
  --config ./ragtest/settings.yaml \
  --output ./ragtest/prompts \
  --domain "Literary Analyst"
```

