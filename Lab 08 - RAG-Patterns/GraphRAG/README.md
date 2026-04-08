# Lab 08 - RAG-Patterns - Graph RAG

## Introduction 

>**The following tasks are intended to be executed inside Cloud Shell via the Azure portal at [https://portal.azure.com](https://portal.azure.com).
>Use the credentials provided to you in the Resources tab. You may have to instantiate a Cloud Shell (bash) instance if using for the first time.**

### GraphRAG

Please reference the [GraphRAG Getting Started instructions here](https://microsoft.github.io/graphrag/get_started/). The VBD closely follows these instructions and the library changes frequently. 
These instructions will fast-follow library releases, but for the latest guides you should refer to Getting Started instructions.

### GraphRAG Accelerator

The GraphRAG Accelerator is, as of FY26, a [public archived repository](https://github.com/Azure-Samples/graphrag-accelerator).

It is the reference implementation for GraphRAG deployments at scale using APIM and AKS, but it is no longer receiving updates or support.

CSAs delivering this VBD should determine with their customers whether the Accelerator is appropriate to cover and how it needs to be tailored to the outcomes and goals of the customer.
The final module of the VBD covering the Accelerator is intended to be entirely driven by the CSA in accordance with their customer's goals, to include not covering it at all.


## Objectives 
 List the objectives
In this lab we will:
-	Install graphrag from Pypi
-	Index a data source
-	Understand and execute Global, Local, and DRIFT queries.
-	Start to inspect Prompt tuning

## Estimated Time 

30 minutes 

## Pre-requisites

- Python 3.10 to 3.12 environment
- Azure OpenAI Service resource (provided for you in the Resources tab)
- Deploy these models at https://ai.azure.com using your Azure OpenAI Service resource.
- Text embedding model: `text-embedding-ada-002` or `text-embedding-3-small`
- LLM: `gpt-4o-mini`

## Tasks

### Installation & Setup

```bash
# Create working directory
mkdir graphrag && cd graphrag

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install GraphRAG
pip install graphrag

```

## Initialize and Explore GraphRAG Workspace

```bash

# Initialize workspace
mkdir -p ragtest/input
graphrag init --root ragtest

# List files
find ./ragtest
```

Expected files:

- `settings.yaml`
- `.env`
- `prompts/` (contains prompt templates)

### Get Source Data

```bash
# Download sample text
curl -L https://aka.ms/dickens/xmas -o ./ragtest/input/book.txt

# Verify download
wc ./ragtest/input/book.txt

```

### Configure .env using your preferred Cloud Shell text editor

```bash
## Copy the following command, change <your_api_key> to be your key from AI Foundry, and run it in its entirety.

sed -i '/^GRAPHRAG_API_KEY=/d' ragtest/.env \
  && echo "GRAPHRAG_API_KEY=<your_api_key>" >> ragtest/.env
```

### Update settings.yaml

1. [ ] Copy, update (with Azure OpenAI endpoint instance), and execute the following command in Cloud Shell.

```bash
export AZURE_OPENAI_ENDPOINT=<instance>.openai.azure.com
```

2. [ ] Then run the following in Cloudshell

```bash

# Use sed to update settings.yaml with correct values for Azure.

sed -i '/api_key:/a\    api_base: ${AZURE_OPENAI_ENDPOINT}' ragtest/settings.yaml
sed -i '/api_base:/a\    api_version: 2024-05-01-preview' ragtest/settings.yaml

sed -i \
  -e 's/model_provider: openai/model_provider: azure/g' \
  -e 's/graphml: false/graphml: true/' \
  ragtest/settings.yaml
  
```


### Run first index

```bash

# Run indexing pipeline
graphrag index --root ./ragtest

```

```bash
# Review output
ls ./ragtest/output

```

### Run first queries

#### Global Query

```bash
graphrag query \
  --root ./ragtest \
  --method global \
  --query "What are the top themes in this story?"
```

#### Local Query

```bash
graphrag query \
  --root ./ragtest \
  --method local \
  --query "Who is Scrooge and what are his main relationships?"

```


#### DRIFT Query (not working as of GraphRAG v2.7.0)

```bash
# graphrag query \
#  --root ./ragtest \
#  --method drift \
#  --query "Who is Scrooge and what are his main relationships?"

```

### Introduce Domain Expertise with Auto-tuning of the Indexing Prompts

```bash
graphrag prompt-tune \
 --root ./ragtest \
 --config ./ragtest/settings.yaml \
 --output ./ragtest/prompts-tuned \
 --domain "Literary Analyst"
```

```bash
# Inspect updated prompts

more ragtest/prompts-tuned/extract_graph.txt

more ragtest/prompts-tuned/summarize_descriptions.txt 
```

#### (Optionally) Reindex and rerun your queries to see how they've changed (not working as of GraphRAG v2.7.0)

```bash
# Move previous index to backup directory
# mv ragtest/output ragtest/output-default

# Re-index
# graphrag index --root ./ragtest --no-cache

# Run a Global query
# graphrag query \
#  --root ./ragtest \
#  --method global \
#  --query "What are the top themes in this story?"

```
