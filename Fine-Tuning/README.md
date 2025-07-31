# Title of the lab

## Introduction 

This lab shows <provide intro>.

## Objectives 
 List the objectives
In this lab we will:
-	


## Estimated Time 

30 minutes 

## Scenario


## Pre-requisites

## Tasks



# 🔍 Fine Tuning Lab

In this lab, you’ll explore the fine-tuning process for **GPT models** using the **Azure AI Foundry Dashboard**.  

Navigate to the `LABS/Fine-Tuning` folder. You’ll find:

- `training_set_10samples.jsonl` – your training dataset  
- `validation_set_10samples.jsonl` – your validation dataset  

> ⚠️ **Note:** Each dataset contains only 10 samples. The goal of this lab is not to outperform the base model, but to **walk through the fine-tuning workflow** using Azure AI Foundry Fine-Tuning UI Dashboard.

---

# 🛠️ Steps: Fine-Tuning the GPT-4.1-mini Model

### 1. Sign in to Azure Portal  
Go to [https://portal.azure.com](https://portal.azure.com)

---

### 2. Create a Resource Group
- Choose a **region that supports fine-tuning**, e.g., `Sweden Central`.

---

### 3. Deploy Azure AI Foundry
- Create an **Azure AI Foundry** resource inside your Resource Group.  
- Use a **unique name** for the default project to avoid validation errors.

---

### 4. Open the Azure AI Foundry Portal  
Access the portal to begin the fine-tuning process.

---

### 5. Start Fine-Tuning  
- Navigate to the **Fine-tuning** section.  
- Click **+ Fine-tune model**.

---

### 6. Configure Fine-Tuning Job
- Select **Supervised** method  
- Upload both the **training** and **validation** files  
- Add a **suffix name** for your model  
- Leave **hyperparameters** as default  
- Click **Submit**  
  - ⏱️ Estimated time: **50–90 minutes**

---

### 7. Review Results
- Once complete, go to the **Metrics** tab  
- Click **Use this model to deploy**

---

### 8. Deploy and Test
- After deployment, locate your model under:  
  `My assets > Models + endpoints`
- Review **Details** (URI, API keys, etc.)  
- Click **Open in playground** to interact with your fine-tuned model

---

✅ **End of Lab Instructions**
