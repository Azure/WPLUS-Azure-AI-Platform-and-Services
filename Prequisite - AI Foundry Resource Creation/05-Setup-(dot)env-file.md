# Setup .env file

## Introduction 

This lab walks you through the steps to setup the .env file as a mandatory step for getting ready for executing the LAB exercises. Note that while this .env file can be setup in a code-first approach using REST API or SDKS, this LAB wants you to do the setup in an interactive way for a learning experiece. 

## Objectives 
 List the objectives
In this lab we will:
-	


## Estimated Time 

30 minutes 

## Scenario


## Pre-requisites

## 🛠️ Tasks

### 1. Copy .env.example as .env
- Find the .env.example file that is supplied as the template
- Copy .env.example to save as .env in the same folder location
- Edit .env to provide the actual value from your environment by following the steps
- Do not modify the section that is marked for not to modify


### 2. Go to the default Project

- Go to [https://ai.azure.com](https://ai.azure.com/) and sign in with your Azure credentials.
- Click **Azure AI Foundry** at the top left
- Click Your AI Foundry (eg ai-foundry-53439517)

![Go to resource](images/aifoundryfromaifoundryportal.png)


### 3. Set value for AZURE_AI_FOUNDRY_PROJECT_ENDPOINT

- At  the center of the **Overview** section, you can find the Azure AI Foundry project endpoint as shown below
- Copy and paste into .env file as the value for AZURE_AI_FOUNDRY_PROJECT_ENDPOINT
![Go to project](images/AZURE_AI_FOUNDRY_PROJECT_ENDPOINT.png)


### 4. Set value for AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY and more

- Scroll to the bottom on the left side menu
- Click **Models + endpoints** in the My assets section 
- You can view list of Model deployments on the right side
- Click on each name to get details
![Go to project](images/modelapikey1.png)

- As shown in the screenshot Copy Endpoint Target URI and paste into .env file as the value for AZURE_OPENAI_ENDPOINT
- Copy Key and paste into .env file as the value for AZURE_OPENAI_API_KEY
![Go to project](images/modelapikey2.png)

- The Endpoint Target URI is in the form of https://<AI-FOUNDRY-NAME>.cognitiveservices.azure.com/openai/deployments/<MODEL-DEPLOYMENT-NAME>/chat/completions?api-version=<MODEL-API-VERSION>
- Copy corresponding string from the URI and paste into .env file as the value for MODEL_DEPLOYMENT_NAME and MODEL_API_VERSION
![Go to project](images/modelapikey3.png)

### 5. Set value for AZURE_OPENAI_EMBEDDING_ENDPOINT and more

- Similar steps as above 
- Click on embeddding model name to get details
- As shown in the screenshot Copy Endpoint Target URI and paste into .env file as the value for AZURE_OPENAI_ENDPOINT
- Copy Key and paste into .env file as the value for AZURE_OPENAI_EMBEDDING_API_KEY
![Go to project](images/modelapikey2e.png)

- The Endpoint Target URI is in the form of https://<AI-FOUNDRY-NAME>.cognitiveservices.azure.com/openai/deployments/<MODEL-DEPLOYMENT-NAME>/chat/completions?api-version=<MODEL-API-VERSION>
- Copy corresponding string from the URI and paste into .env file as the value for EMBEDDING_MODEL_DEPLOYMENT_NAME and EMBEDDING_MODEL_API_VERSION


### 6. Set value for GROUNDING_WITH_BING_CONNECTION_NAME

- At the top left, Click **Azure AI Foundry**
- Click Your AI Foundry (eg ai-foundry-53439517)
![Go to resource](images/aifoundryfromaifoundryportal.png)
- Left side, in the **Management center**, in the Resource section, Click **Connected resources**
- You can see list of connected resources
![List models deployed](images/gwbingconnectedinlist.png)
- Copy the "Name" of the "Grounding with Bing Search" connection (Corresponding Target columns is https://api.bing.microsoft.com/) and paste into .env file as the value for GROUNDING_WITH_BING_CONNECTION_NAME




### ?. Set value for TENANT_ID

- Go to [https://portal.azure.com](https://portal.azure.com) and sign into the Azure portal with your Azure credentials.
- In the top search bar, type **entra id**
- Select **Microsoft Entra ID** from the search results
![Go to project](images/tenantid1.png)

- In the Overview section, find **Tenant ID** as shown in the screenshot
- Copy Tenant ID and paste into .env file as the value for TENANT_ID
![Go to project](images/tenantid2.png)



## ✅ Completed. 

- WIP

