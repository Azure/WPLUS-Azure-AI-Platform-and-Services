# AI Language Service with Agents Lab

## Introduction 

In this lab you will interact with the Azure AI language cognitive service API using the Logic App low code workflow designer. 
You will create 2 low code Logic Apps:

(1) for PII removal

(2) for Language detection and translation

For advanced/bonus content you will use these Logic Apps to create AI agents that work together to prepare data. 


## Objectives 

The objectives in this lab we will be:

-	Learn how to call the Azure AI langugage cognitive service API for different tasks 
- Process data via the API as part of a business workflow

## Estimated Time 

60 minutes 

## Scenario

You work for Contoso, a multinational e-commerce company that receives thousands of customer feedback messages daily in various languages. These messages often contain sensitive personal identifying information (PII) and your company wants to ensure all messages have the language detected, PII removed to ensure privacy compliance, translation to English for centralized analytics. 

## Pre-requisites

Note: This Low Code lab requires access to:

- Azure subscription
- A Microsoft Foundry Project
-	The AI Language Service in Azure AI Foundry
-	Access to provision Logic Apps and resources in Azure
-	Azure OpenAI (bonus/advanced only for Agent creation)

_Note: See [Prequisite - AI Foundry Resource Creation](../Lab%2000%20-%20Prequisite%20-%20AI%20Foundry%20Resource%20Creation/01-Create-Azure-Foundry-Project.md) folder to ensure Microsoft Foundry Project is correctly set up._

## Overview

In this lab, you will interact with the Azure AI language cognitive service API using the Logic App low code workflow designer.  
You will create **2 low code Logic Apps**:

1. **PII removal**
1. **Language detection and translation**

For advanced/bonus content, you can use these Logic Apps to create AI agents.

## Copy the Access Language API Key and Endpoint URL

1. [ ] Login to Azure AI Foundry: https://ai.azure.com/. 
  _Note: Make sure you are logged in the MS Foundry project created in the prereqs_
1. [ ] Go to the Overview page, check the **API Key** and **Azure AI Services** endpoint URL.
![Alt text](./Images/SaveEndpointAPIKey.png)

1. [ ] Store these values:  
   - [ ] **API Key**
   - [ ] **Azure AI Services endpoint**
1. [ ] You will use these details to connect to the Language Service.

---

## Create a PII Redaction Logic App

This Logic App receives text input and outputs the text with PII redacted. It creates an endpoint callable from other applications.

1. [ ] In https://portal.azure.com/, navigate to **+ Create a resource** and search for _Logic App_, then click **Add**. 
1. [ ] Under plan, choose **Multi-tenant** under Consumption, then click **Select**.
1. [ ] Select the same Resource Group as your AI Foundry project and follow the prompts to create a Logic App resource. For name for the Azure Logic App resource. Please use this name as the lab environment will not let you use another name - +++**logiapp1-@lab.LabInstance.Id**+++ (eg logiapp1-53439517).![Alt text](./Images/CreateLogicApp.png). 
1. [ ] Once provisioned, select **Go to Resource** in the Azure Portal to open the new Logic App.
1. [ ] Expand Development tools and open **Logic App Designer**. Select **Add a trigger**.

 ![Alt text](./Images/AddTrigger.png)
 ![Alt text](./Images/RequestIsReceived.png)

1. [ ] Search triggers for “When a HTTP request is received” and select it.
1. [ ] Under Request Body JSON Schema, add:
   
 ```json
    {
      "type": "object",
      "properties": {
        "HTTP_URI": {
          "description": "URI for HTTP Request",
          "type": "string"
        },
        "HTTP_request_content": {
          "description": "Content or Body of the HTTP Request",
          "type": "string"
        }
      }
    }
  ```
    
1. [ ] In the description field, add:  
   _When a request is received, review the message for PII data and redact it with ******._
   ![Alt text](./Images/DescFieldRequestRecieved.png)
1. [ ] Click the plus sign to add an action, then **select Add an action**. 

![Alt text](./Images/AddAnAction.png)

1. [ ] Search for _Parse JSON_ and select the option under Data operations. 

![Alt text](./Images/ParseJSON.png)

1. [ ] Under Content, select the Dynamic content lightning bolt, and under When a HTTP request is received, select Body.

![Alt text](./Images/DynamicContentLightningBolt.png)
![Alt text](./Images/SelectBody.png)

1. [ ] Under the Schema box, paste in:

    ```json
    {
      "type": "object",
      "properties": {
        "description": {
          "type": "string"
        }
      }
    }
    ```

1. [ ] The final screen should look like the screenshot below:

![Alt text](./Images/FinalScreenshot.png)  

1. [ ] Select **Save** on the canvas.
1. [ ] Click the plus sign to add an action, then **select Add an action**.

![Alt text](./Images/AddAnAction2.png)

1. [ ] Search for _Azure Language_ and then click **See more**.

![Alt text](./Images/Seemore.png)

1. [ ] Select **Detect Personal Information (V3.1)**.

![Alt text](./Images/DetectPersonalInformation.png)

1. [ ] Select Authentication Type as **Api Key** and add the API Key and Endpoint (Target) you saved earlier.
![Alt text](./Images/SaveEndpointAPIKey.png)
![Alt text](./Images/AfterDetectPersonalInformation.png)

1. [ ] Select the Detect Personal Information action. 
Under Parameters, search for the Documents heading. Select **+ Add new item**.  

![Alt text](./Images/AddaNewItem.png)

Insert:
- [ ] Id-1 = 1
- [ ] Text-1 = Insert expression (fx)

![Alt text](./Images/InsertExpression.png)

1. [ ] In the pop-up expression window, paste:  
    ```
    body('Parse_JSON')['description']
    ```
![Alt text](./Images/BodyParseJSONDesc.png)
    Click Add

1. [ ] Click the plus sign to add the final action, then **select Add an action**.

![Alt text](./Images/AddAnAction.png)

1. [ ] Search for _Response_ and select the option under Request.

![Alt text](./Images/RequestResponse.png)

1. [ ] Fill in the parameters for the Response, leaving Status Code as 200.
1. [ ] In the Body, select the expression using the fx icon and paste:
    ```
    body('Detect_Personal_Information_(V3.1)')['documents'][0]['redactedText']
    ```
    Click Add
![Alt text](./Images/fx.png)

![Alt text](./Images/PasteExpression.png)

1. [ ] Save your Logic App.

1. [ ] Select the arrow next to Run, then **Run with payload**.

![Alt text](./Images/RunwithPayload.png)

1. [ ] In the Body of the Run with payload pane, paste:
    ```json
    {
      "description": "My phone number is (04) 12 345 678"
    }
    ```

1. [ ] Confirm that the output displays the redacted phone number.

![Alt text](./Images/RunwithPayloadoutput.png)

1. [ ] The final completed flow should look like the image below:

![Alt text](./Images/PIIRedactionFlow.png)

---

## Create a Translation Logic App

This Logic App receives text, detects the language, and outputs the text in English.

1. [ ] In https://portal.azure.com/, search for _Logic Apps_ and select the option.

![Alt text](./Images/LogicApp.png)

![Alt text](./Images/LogicAppsAdd.png)

1. [ ] Click **+ Add** to add a new Logic App and choose Multi-tenant under Consumption, then click **Select**.
1. [ ] Ensure you are selecting the same region and resource group as your Foundry project. Name your Logic App `EnglishTranslation`.
1. [ ] Review and create the Logic App, then select **Go to resource** once provisioned.
1. [ ] Under development tools, select **Logic app designer** and then **Add a trigger**.

![Alt text](./Images/AddaTrigger2.png)

1. [ ] Search triggers for “When a HTTP request is received” and select it.
1. [ ] Under Request Body JSON Schema, add:

```json
{
    "type": "object",
    "properties": {
      "HTTP_URI": {
        "description": "URI for HTTP Request",
        "type": "string"
      },
      "HTTP_request_content": {
        "description": "Content or Body of the HTTP Request",
        "type": "string"
      }
    }
}
```

1. [ ] In the description field, add:  
   _Receives an HTTP request in the description field of some text. Then translates that text to English._

![Alt text](./Images/DescFieldRequestRecieved2.png)

1. [ ] Select **Save**.
1. [ ] Click the plus sign to add an action, then **select Add an action**.

![Alt text](./Images/AddAnAction.png)

1. [ ] Search for _Parse JSON_ and select the option under Data operations.

![Alt text](./Images/ParseJSON.png)

1. [ ] Under Content, select the Dynamic content lightning bolt, and under When a HTTP request is received, select Body.

![Alt text](./Images/DynamicContentLightningBolt.png)

![Alt text](./Images/SelectBody.png)

1. [ ] Under the Schema box, paste in:

```json
{
    "type": "object",
    "properties": {
        "description": {
          "type": "string"
        }
    }
}
```

1. [ ] The final screen should look like the screenshot below:

![Alt text](./Images/FinalScreenshot2.png)

1. [ ] Select **Save** on the canvas.
        
1. [ ] Click the plus sign to add an action, then **select Add an action**.

![Alt text](./Images/AddAnAction.png)

1. [ ] Search for _Azure Language_ and then click **See more**.(This step is to understand what is available). Once reviewed, go back to main search and follow the steps below.
1. [ ] Search for _Microsoft Translator V3_ and then click **See more**.
1. [ ] Select **Translate Text**. Create the connection using the same API Key and Resource name (not the full Endpoint) from Foundry.

![Alt text](./Images/TranslateText.png)

Note that the Translator Resource Name must be the part highlighted in the screenshot below:

![Alt text](./Images/TranslatorConnectionTranslatorResourceName.png)


1. [ ] Under Parameters, set:
    - [ ] **Source Language:** Auto-detect
    - [ ] **Target Language:** English
    - [ ] **Body Text-1:** Choose expression (fx)  

![Alt text](./Images/TranslateTextfx.png)

In the expression field, paste:  

```
body('Parse_JSON')['description']
```

Then click **Add**

![Alt text](./Images/TranslateTextfx1.png)


1. [ ] Click **Save**.
1. [ ] Click the plus sign to add the final action, then **select Add an action**.

![Alt text](./Images/AddanAction2.png)

1. [ ] Search for _Response_ and select the option under Request.

![Alt text](./Images/RequestResponse.png)

1. [ ] Fill in the parameters for the Response, leaving Status Code as 200.
1. [ ] In the Body, select the expression using the fx icon and paste:
![Alt text](./Images/fx.png)
    ```
    body('Translate_text')[0]['TranslatedText']
    ```
![Alt text](./Images/TranslateTextfx3.png)
![Alt text](./Images/Response.png)

1. [ ] Save your Logic App.
1. [ ] Select the arrow next to Run, then **Run with payload**.
![Alt text](./Images/run.png)

1. [ ] In the Body of the Run with payload pane, paste:
```json
    {
       "description" : "Mi número de teléfono es (04) 12 345 678"
    }
    {
       "HTTP_request_content" : "Mi número de teléfono es (04) 12 345 678"
    }
```

1. [ ] Confirm the output displays the translated text.

![Alt text](./Images/RunwithPayload2.png)

1. [ ] The final completed flow should look like the image below:

![Alt text](./Images/EnglishTranslationFlow.png)

---

## Advanced / Bonus Content

You work for Contoso, a multinational e-commerce company that receives thousands of customer feedback messages daily in various languages. These messages often contain sensitive PII. Your company wants to ensure all messages have the language detected, PII removed, and are translated to English for centralized analytics.

You will create **2 agents** using Azure AI Foundry:

1. **Translation Agent**
1. **PII Redaction Agent**

---

### Update your Logic App flows to accept the format from AI Foundry

1. [ ] In the Azure Portal (https://portal.azure.com/) first open your EnglishTranslation flow, in edit mode click on the **Translate Text** box and click the cross next to the dynamic input, _Body Description_ to remove it.

![Alt text](./Images/ChangeInputEnglishTranslationBefore.png)

1. [ ] Put the cursor after the "Text": and then click on the _fx_ function option that appears. In the Dynamic Content box select Http_request_content then click Add. Click outside of the flow and press save. Ensure you have saved the changes to the flow. 

![Alt text](./Images/ChangeInputEnglishTranslationAfter.png)

1. [ ] Repeat this step for your PII Redaction flow , in edit mode click on the **Detect Personal Information (V3.1)** box and click the cross next to the dynamic input, _Body Description_ to remove it.

![Alt text](./Images/PIIRedactionFlowBefore.png)

1. [ ] Put the cursor after the "Text": and then click on the _fx_ function option that appears. In the Dynamic Content box select Http_request_content then click Add. Click outside of the flow and press save. Ensure you have saved the changes to the flow. 

![Alt text](./Images/PIIRedactionFlowAfter.png)

---

### Deploy an Azure OpenAI Resource for Your Project

1. [ ] In your Azure AI Foundry (https://ai.azure.com/) project, click on **Agents**.

![Alt text](./Images/Agents.png)

1. [ ] If the Deploy a Model doesn’t pop up, select **Deploy model**.
1. [ ] Ensure you select a model that supports agents in your region:  
   https://learn.microsoft.com/en-us/azure/ai-services/agents/concepts/model-region-support
1. [ ] Search for **gpt-4.1** and select **Confirm**.
![Alt text](./Images/confirmgpt4.1.png)
1. [ ] The Agent screen should open with your first agent automatically created.
![Alt text](./Images/createdagent.png)

---

### Create a Translation Agent

1. [ ] Select the Agent checkbox and rename the Agent to **EnglishTranslationAgent**.
![Alt text](./Images/TranslationAgent.png)
1. [ ] In the Instructions, paste:
    > Send all incoming messages that are not in English to the EnglishTranslation action. If the entry is already in English, return the original text unchanged. Ensure the output maintains the structure and formatting of the input data.
1. [ ] In the Description, paste:
    > This agent uses the AI Language Services to translate incoming information to English for downstream analytics.
1. [ ] Next to Actions, select **+ Add**.

1. [ ] In the pop-up modal window, select **Azure Logic Apps Your Actions**.

![Alt text](./Images/AddAction.png)

1. [ ] Your Logic Apps from part one should appear. Select **English Translation**.  
   _Note: If your Logic App does not appear, ensure it is in the same subscription and resource group as Foundry, the Logic App HTTP request description is in place, and the workflow contains a Request Trigger and ends with a Response Action._
![Alt text](./Images/EnglishTranslation.png)
1. [ ] On the Resource screen, click **Next**, then on the Schema screen, click **Create**.
1. [ ] On the Agent Setup screen, select **Try in playground**.
1. [ ] Try a sentence in English, then in Spanish:  
   - [ ] `Hello, how are you today?`  
   - [ ] `Hola ¿cómo estás hoy?`
![Alt text](./Images/RunWithEnglishAgent.png)

1. [ ] Click on View Run Info to show that the translation ran with the Logic App action to support the translation:

![Alt text](./Images/RunWithLogicApps.png)

1. [ ] **NOTE:** If you see a gateway error you may need to try again as services complete deployment 

---

### Add a PII Redaction Agent

1. [ ] Update the agent instructions to :
    - [ ] **Instructions:**  
      > Send all messages to the PIIRedaction action to have personal information removed. 
Then send all incoming messages with the personal information remoed that are not in English to the EnglishTranslation action. If the entry is already in English, return the original text unchanged. Ensure the output maintains the structure and formatting of the input data.

1. [ ] Next to Actions, click **+ Add** then **Azure Logic Apps**.
1. [ ] Select Azure Logic Apps and choose your PIIRedaction flow
1. [ ] On the basic information screen, add:
    - [ ] **Action Description:**  
      > For any text provided, replace any sensitive or personal identifying information (PII) with *********
1. [ ] On the setup screen, select **Try in playground** and paste in:
    ```
    Hola, me llamo Mateo Gómez. Perdí mi tarjeta de crédito el 17 de agosto y quisiera solicitar su cancelación. Mi última compra fue un plato de pollo a la parmesana en el Restaurante Contoso, cerca del Museo de Hollywood, por $40. A continuación, se detallan mis datos personales para su validación: Profesión: Contador. Número de Seguro Social: 123-45-6788. Fecha de nacimiento: 9-9-1989. Número de teléfono: 949-555-0110. Dirección personal: 1234 Hollywood Boulevard, Los Ángeles, CA. Correo electrónico vinculado: mateo@contosorestaurant.com. Código Swift: CHASUS33XXX.
    ```

1. [ ] The output should look similar to the below:  
 ![Alt text](./Images/FinalOutputBothAgents.png)

1. [ ] Click on View Run Info to show that the translation ran with both the Logic App actions to support the translation: 
 ![Alt text](./Images/FinalOutputFlowRuns.png)
