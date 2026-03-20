# Fine Tuning

## Introduction 

In this lab, you’ll explore the fine-tuning process for **GPT models** using the **Azure AI Foundry Dashboard**. 

## Objectives 
 List the objectives
In this lab we will:
-	Fine tune a model with given training and test dataset


## Estimated Time 

30 minutes 

## Scenario
Fine tuning a model with given training and test dataset

## Pre-requisites
Completed the pre-requisites labs
- Create Azure AI Foundry Project

## Tasks

Navigate to the `C:/Users/Admin/Desktop/LABS/Lab 05 - Fine-Tuning/` folder. You’ll find:

- `training_set_10samples.jsonl` – your training dataset  
- `validation_set_10samples.jsonl` – your validation dataset  

> ⚠️ **Note:** Each dataset contains only 10 samples. The goal of this lab is not to outperform the base model, but to **walk through the fine-tuning workflow** using Azure AI Foundry Fine-Tuning UI Dashboard.

---

# 🛠️ Steps: Fine-Tuning the GPT-4.1-mini Model

### 1. Sign in to Azure Portal  
Go to [https://portal.azure.com](https://portal.azure.com)

---
### 2. Open the Azure AI Foundry Portal  
Launch the Azure AI Foundry Resource created in the pre-requisites lab.

---

### 3. Start Fine-Tuning  
- [ ] Navigate to the **Fine-tuning** section.  
- [ ] Click **+ Fine-tune model**.
- [ ] Here choose GPT-4.1-mini or GPT-4-o-mini or GPT-4.o

---

### 4. Configure Fine-Tuning Job
- [ ] Select **Supervised** method  
- [ ] Upload both the **training** and **validation** files. By navigating to `C:/Users/Admin/Desktop/LABS/Lab 05 - Fine-Tuning`
  - [ ] `training_set_10samples.jsonl` – your training dataset  
  - [ ] `validation_set_10samples.jsonl` – your validation dataset 
- [ ] Add a **suffix name** for your model  
- [ ] Leave **hyperparameters** as default  
- [ ] Click **Submit**  
  - [ ] ⏱️ Estimated time: **50–90 minutes**

---

### 5. Review Results
- [ ] Once complete, go to the **Metrics** tab  
- [ ] Click **Use this model to deploy**

---

### 6. Deploy and Test
- [ ] After deployment, locate your model under:  
  `My assets > Models + endpoints`
- [ ] Review **Details** (URI, API keys, etc.)  
- [ ] Click **Open in playground** to interact with your fine-tuned model



