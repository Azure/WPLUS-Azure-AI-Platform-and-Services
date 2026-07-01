# Deploy models into the Microsoft Foundry Project

## Introduction 

This lab walks you through the steps to deploy various models into the **Microsoft Foundry** project.

## Objectives 

In this lab we will deploy the following models:

- text-embedding-3-large
- GPT-5.1
- GPT-5-mini	
- text-embedding-ada-002

## Estimated Time 

5 - 10 minutes 

## Scenario

You are deploying models that will be utilized later in the labs for several modules in this workshop.

## Pre-requisites

Make sure you are using the legacy Microsoft Foundry UI.

- If this is the first Portal view in the **Foundry Portal**, then click **firstProject** inside the **All resources** section.
    ![New Foundry UI](images/ai_foundry_new_ui_3.png)

- If the following Microsoft Foundry UI(User Interface) is shown:
    ![New Foundry UI](images/ai_foundry_new_ui.png)

- Change the UI to the legacy UI by clicking the **New Foundry** switch:
    ![New Foundry UI](images/ai_foundry_new_ui_2.png)

- If the feedback popups is displayed, click **Continue without feedback**.

## 🛠️ Tasks

### 1. Ensure that you are on the Microsoft Foundry – Overview page

### 2. Deploy gpt-5.1 model

- [ ] In the left side menu, Click **Model catalog**
- [ ] At the center, scroll down and search +++gpt-5.1+++
- [ ] Right Click on **gpt-5.1** and click **Open link in new tab**
![Find gpt-4o models](images/findgpt4omodels.png)

- [ ] Go to the newly opened tab for gpt-5.1
- [ ] Click **Use this model** button
![Use this model](images/usethismodel.png)

- [ ] For this lab, keep all defaults
- [ ] (Optional) Click **Customize** to review additional details
- [ ] Click **Deploy** button 
![Deploy gpt-4o](images/deploygpt4o.png)

- [ ] After deployment completes, close the browser tab.

### 3. Deploy gpt-5-mini model

- [ ] Repeat the steps above to deploy the +++**gpt-5-mini**+++ model.

### 4. Deploy embedding model

- [ ] Repeat the steps above to deploy the +++**text-embedding-3-large**+++ model.

### 5. Deploy text-embedding-ada-002 model

- [ ] Repeat the steps above to deploy the +++**text-embedding-ada-002**+++ model.

## ✅ Completed. Verify models deployment

- [ ] In the left side menu, scroll down to the bottom, Click **Models + endpoints**
- [ ] You can see list of models deployed

![List models deployed](images/msfoundry_listofmodelsdeployed.png)
