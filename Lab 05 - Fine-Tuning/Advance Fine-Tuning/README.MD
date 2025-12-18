# Fine Tuning - Advance Lab

## Introduction

In this section you will find **advance Fine Tuning** laboratories using **Microsoft Foundry** and different **training techniques**.

## Objectives

In this lab we will:

- Fine-tune a model using the Direct Preference Optimization (DPO) technique with a designated training and test dataset. This session will guide you through programmatically fine-tuning a model while applying best practices in data science.

## Estimated Time

120 minutes

## Scenario

Fine tune a model using the training technique DPO (Direct preference optimization) with a given training and test dataset. The configuration will be done using a Jupyter notebook and Python SDK.

## Pre-requisites

Complete the pre-requisites labs

- Azure subscription
- A Microsoft Foundry Project
- Python 3.8 or higher
- VS Code with Jupyter Notebook extension
- **Azure AI User role** assigned to your account for the Azure AI Foundry project
  - See [Azure AI Foundry RBAC documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry?pivots=fdp-project) for more details on role assignments

## Tasks

Navigate to the `C:/Users/Admin/Desktop/LABS/Lab 05 - Fine-Tuning/Advance Fine-Tuning/` folder. You’ll find:

- `gpt-4_o_dpo_ft.ipynb` - Jupyter notebook with detailed lab instructions
- `gpt4o_generated_qa_dpo_train_10_samples.jsonl` – your training dataset  
- `gpt4o_generated_qa_dpo_validation_10_samples.jsonl` – your validation dataset  

> ⚠️ **Note:** Each dataset contains only 10 samples. The goal of this lab is not to outperform the base model, but to **walk through the fine-tuning workflow** using Microsoft Foundry Fine-Tuning Python SDK.

---