# Azure AI Vision – Lab

## Introduction

Azure AI Vision is a cloud-based service from Microsoft that uses advanced algorithms to analyze images and extract valuable information. It includes capabilities like face detection, Optical Character Recognition (OCR), image analysis, and video indexing.

> **Note:** The Azure Vision Studio portal now only displays the **Face** feature. OCR, Image Analysis, and Video Indexer capabilities are still accessible through their respective **SDKs and REST APIs**. This lab covers Face Analysis through the portal and provides SDK/API-based exercises for the other services via the accompanying notebook.

## Objectives

In this lab we will walk through:
- Face Analysis (via Vision Studio portal)
- OCR (via SDK/API)
- Image Analysis (via SDK/API)

## Estimated Time

30 minutes

## Scenario

Explore Azure AI Vision services: use the Vision Studio portal for Face Analysis, and the SDK/REST APIs for OCR, Image Analysis, and Video Indexer.

## Pre-requisites

Complete the pre-requisite instructions.

## Tasks

---

## Exercise 1: Provision Azure Resources

1. [ ] Go to +++https://portal.azure.com+++ .
1. [ ] In the top search bar, type **"Microsoft Foundry"**
1. [ ] Select **Microsoft Foundry** from the search results    
    ![Search Microsoft Foundry](/Lab%2000%20-%20Prequisite%20-%20AI%20Foundry%20Resource%20Creation/images/search_ai_foundry.png)
    

1. [ ] In the left panel, inside the **More services** section, click **Computer Vision**.
1. [ ] Click the **Create** button inside the Computer Vision resource. 
    ![Alt text](./Images/create_resource.png).
1. [ ] Inside the **Create Computer Vision** section, use the following values to create the resource:
    - Region: _select a supported region._ You may check the service availability in the [Product Availability by Region - Search for **Azure Vision**](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/table)
    - Name: ++**cv-@lab.LabInstance.Id**+++ (eg cv-53439517) _Ensure to use this name (++**cv-@lab.LabInstance.Id**+++), you will not be able to use a different name to create the resource. The screen shot provided is just for reference, do not use the name provided in the screenshot below._
    - Pricing Tier:  **Standard S1**
    - Click the policy checkbox.
    - Click **Review + create**
    ![Alt text](./Images/create_resource_2.png)

1. [ ] Click **Create**
1. [ ] Access the Vision Studio at [https://portal.vision.cognitive.azure.com/](https://portal.vision.cognitive.azure.com/)
1. [ ] Click the **Sign in** button in the top right section.
1. [ ] You should be inside the Azure Vision Studio (Computer Vision Studio)
    ![Alt text](./Images/vision_studio.png)

---

## Exercise 2: Face Analysis

This exercise demonstrates how to use the Azure AI Vision Faces features to detect and analyse human faces in images. 

1. [ ] Inside the **Vision Studio** Portal.
1. [ ] Click on the **Detect faces in an image**.
1. [ ] Click the **Acknowledge** checkbox.
1. [ ] Click the **Please select a resource** link 
    ![Alt text](./Images/face_studio.png)

1. [ ] Select the **Subscription** and click **Create a new resource**

    ![Alt text](./Images/selectfaceresource.png)

1. [ ] Inside the **Create a new resource**, select the following values:
    - **Name**:  +++**faceresource-@lab.LabInstance.Id**+++ (eg faceresource-53439517). Ensure to use this name, you will not be able to use a different name to create the resource.
    - **Subscription**: _existing subscription_
    - **Resource Group**: _existing resource group_
    - **Location**: _select a region_
    - **Price tier**: S0
    - Click **Create resource**

    ![Alt text](./Images/selectfaceresource_2.png)

1. [ ] Click **Confirm**

1. [ ] Select an image and cthen click **JSON** to see the face attributes.
1. [ ] Iteratively click the samples to the right of the box.
    ![Alt text](./Images/vision2.png)
1. [ ] Close the Azure vision portal and continue with the lab

---

## Exercise 3: Optical Character Recognition (OCR) via SDK/API

> Warning: **Deprecation Notice:** The Image Analysis 4.0 OCR service is deprecated and will be **retired on September 25, 2028**. Legacy Computer Vision API versions (v1.0-v3.1) will be **retired on September 13, 2026**. Consider migrating to:
> - [Azure AI Document Intelligence - Read model](https://learn.microsoft.com/azure/ai-services/document-intelligence/prebuilt/read) (optimized for documents)
> - [Azure Content Understanding](https://learn.microsoft.com/azure/ai-services/content-understanding/overview) (managed generative solution)

While the OCR feature is no longer available in the Vision Studio portal, the **REST API and SDKs** remain fully functional until the retirement dates above.

The OCR API extracts printed and handwritten text from images such as posters, street signs, product labels, business documents, invoices, and receipts. It supports multiple languages and works with text on various surfaces and backgrounds.

### Set the Azure Computer Vision (Azure AI Vision) variables in the .ENV file

1. [ ] Go to +++https://portal.azure.com+++ 
1. [ ] In the top search bar, type **"Microsoft Foundry"**
1. [ ] Select **Microsoft Foundry** from the search results
    ![Search Microsoft Foundry](/Lab%2000%20-%20Prequisite%20-%20AI%20Foundry%20Resource%20Creation/images/search_ai_foundry.png)

1. [ ] In the left panel, inside the **More services**, click **Computer Vision**.
1. [ ] Click the **Computer resource** ++**cv-@lab.LabInstance.Id**+++
1. [ ] In the left panel, inside **Resource Management**, click **Keys and EndPoint**
1. [ ] Copy the values **KEY 1** and **Endpoint**
    ![Alt text](./Images/computer_resource_ke.png)

1. [ ] Inside Visual Studio Code, open the **.env** file
1. [ ] Set the following values:
    - **COMPUTER_VISION_API_KEY**: _Paste the **KEY 1** value_
    - **COMPUTER_VISION_ENDPOINT**: _Paste the **Endpoint** value_

1. [ ] Open the **Hands-on exercise:** Open the notebook at [`LabFiles/AI_vision_services_lab.ipynb`](./LabFiles/AI_vision_services_lab.ipynb)
1. [ ] Complete **Section 02 - Extract Text from Images** to call the OCR API programmatically.

---

## Exercise 4: Image Analysis via SDK/API

> :warning: **Deprecation Notice:** The Image Analysis 4.0 service is deprecated and will be **retired on September 25, 2028**. Consider migrating to:
> - [GPT models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview) (flexible custom vision solutions)
> - [Azure Content Understanding](https://learn.microsoft.com/azure/ai-services/content-understanding/overview) (managed generative solution for images, documents, audio, and video)

While Image Analysis is no longer available in the Vision Studio portal, the **REST API and SDKs** remain fully functional until the retirement date above.

The Image Analysis API provides capabilities including:
- **Caption generation** - Generate natural language descriptions of images
- **Dense captions** - Detailed captions for multiple regions within an image
- **Tagging** - Extract common tags and objects detected in images
- **Smart cropping** - Intelligently crop images around areas of interest
- **Image retrieval** - Search photos using natural language queries

**Hands-on exercise:** Open the notebook at [`LabFiles/AI_vision_services_lab.ipynb`](./LabFiles/AI_vision_services_lab.ipynb) and complete **Sections 03-07** (Image Retrieval, Dense Captions, Captions, Tags, Smart Crop) to explore these capabilities via the API.

---

## Exercise 5: Video Indexer via API

Azure AI Video Indexer is a cloud-based service that extracts insights from videos using AI models for speech, vision, and natural language processing. The service is **actively supported** with no announced retirement date.

> **Note:** Azure Media Services (AMS)-based Video Indexer accounts were retired in June 2024. All new accounts are AMS-less. If migrating from an older account, see the [AMS migration guide](https://learn.microsoft.com/azure/azure-video-indexer/create-account).

The Video Indexer API enables you to:
- Upload and index videos programmatically
- Extract insights including people detection, topics, keywords, labels, named entities, and scenes
- Generate transcriptions, captions, and multi-modal video summaries
- Perform face redaction and object detection

**Hands-on exercise:** Open the notebook at [`LabFiles/AI_vision_services_lab.ipynb`](./LabFiles/AI_vision_services_lab.ipynb) and complete **Section 08 - Video Indexer** to upload and index a video via the API.

---
