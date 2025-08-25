# Azure AI Vision – Low Code Lab

## Introduction 

Azure AI Vision is a cloud-based service from Microsoft that uses advanced algorithms to analyze images and extract valuable information. It includes capabilities like Optical Character Recognition (OCR), face detection, image analysis, and video indexing. This lab guides you through low-code exercises.

## Objectives 
 List the objectives
In this lab we will walk through
- OCR
- Face Analysis
- Image Analysis
- Video Indexer


## Estimated Time 

30 minutes 

## Scenario
Walk through OCR, Face Analysis, Image Analysis and Video Indexer

## Pre-requisites
Complete the pre-requisite instructions

## Tasks

---

## Exercise 1: Provision Azure Resources
1. Access the Azure portal and create a Computer Vision resource. ![Alt text](./Images/create_resource.png)
2. Ensure the resource is created in a supported region. ![Alt text](./Images/create_resource_2.png)
3. Access Vision Studio at [https://portal.vision.cognitive.azure.com/](https://portal.vision.cognitive.azure.com/) and select your resource. ![Alt text](./Images/select_resource.png)

---

## Exercise 2: Optical Character Recognition (OCR)
1. Go to [Azure AI Vision Studio](https://portal.vision.cognitive.azure.com/), log in, and select the "Optical character recognition" tab.  ![Alt text](./Images/OCR.png)
2. Click "Extract text from images."  ![Alt text](./Images/extract_text_from_images.png)
3. Browse for a file and select your AI vision resource. ![Alt text](./Images/select_resource_azureResource.png)
4. Review results on the “Detected attributes/JSON” tabs. ![Alt text](./Images/DetectedAttributes.png)

---

## Exercise 3: Face Analysis
This exercise demonstrates how to use Azure AI Vision, Face to detect and analyse human faces in images. Navigate to [Azure AI | Vision Studio](https://portal.vision.cognitive.azure.com/), log in with your Azure 
credentials, and then click on the "Face" tab. 
![Alt text](./Images/vision1.png)
01. Iteratively click the samples to the right of the box.  
![Alt text](./Images/vision2.png)
In order to try the Face liveness detection, feature you need to apply access for the service from your subscription.  

---

## Exercise 4: Image Analysis
This exercise demonstrates how to use Azure AI Vision, Image Analysis to extract meaningful insights from images, including object detection, caption generation, and scene understanding. 
Navigate to [Azure AI | Vision Studio](https://portal.vision.cognitive.azure.com/), log in with your Azure credentials
1. In Vision Studio, select the "Image analysis" tab.![Alt text](./Images/imageanalysis1.png)
2. Search photos with image retrieval. ![Alt text](./Images/imageanalysis2.png)
3. Enter a natural language query to retrieve relevant images. ![Alt text](./Images/imageanalysis3.png)
4. Try generating dense captions for images.![Alt text](./Images/imageanalysis4.png)
5. Extract common tags by choosing the model, language, and clicking samples. ![Alt text](./Images/imageanalysis5.png)

---

## Exercise 5: Video Indexer
1. Go to [Azure AI Video Indexer](https://www.videoindexer.ai/account/login) and log in. ![Alt text](./Images/VideoIndexer1.png)
2. Complete the "Use of facial identification and recognition" form and accept.![Alt text](./Images/VideoIndexer2.png)
3. Click "Upload," then "Browse for files" to select a video.![Alt text](./Images/VideoIndexer3.png)
4. Complete the upload form (file name, privacy, streaming quality, language, etc.).![Alt text](./Images/VideoIndexer4.png)
5. Click "Review + upload," then "Upload + index."![Alt text](./Images/VideoIndexer5.png)
6. Monitor progress; you'll receive an email when processing is complete. ![Alt text](./Images/VideoIndexer6.png). For the purpose of this lab, there won't be an email, so this step may not work for this lab environment. 
7. Click "Watch now >" in the email or view the video in the Video Indexer interface. ![Alt text](./Images/VideoIndexer7.png)
8. Review video insights: playback area, insights panel (person, topic, keywords, labels, named entities, scenes).

---

For pro-code labs, follow the instructions in the provided Jupyter notebook.
