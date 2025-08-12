# Azure PostgreSQL Lab
 
## Introduction
In this lab you will learn how perform vector search on PostgreSQL.
 
## Objectives
Store and retrieve vector data.
Perform similarity searches using PostgreSQL.
 
## Estimated Time
20 minutes
 
## Scenario
You want to use PostgreSQL for your AI application's backend and need to store and search vectors efficiently. This lab will walk you through the necessary steps.
 
## Pre-requisites
None. The database has been pre-created for you.
 
## Tasks
## Part 1 – Enable Vector Search Extensions in PostgreSQL

1. **Navigate to Server Parameters in Azure Portal**
   - Go to your Azure PostgreSQL server in the Azure Portal.
   - In the left menu, select **Server parameters**.

2. **Enable Required Extensions**
   - Search for `azure.extensions`.
   - Select **AZURE_AI** and **VECTOR**.
   - Click **Save** at the top.

**Result:** The PostgreSQL server is now configured to use Azure AI functions and the `vector` data type for similarity search.

---

## Part 2 – Create and Restore the `books` Database

### Step 1: Set PostgreSQL Password in PowerShell
In a PowerShell terminal:
```powershell
$env:PGPASSWORD = "Password12345!!"
```
This sets your PostgreSQL password for the current session.

---

### Step 2: Connect with `psql` and Create Database
Run:
```powershell
psql -h pgaivector-<server-id>.postgres.database.azure.com -U postgres -d postgres
```
Inside `psql`, create the database:
```sql
create database books;
\q
```

---

### Step 3: Restore Database from Backup
Run:
```powershell
pg_restore -h pgaivector-<server-id>.postgres.database.azure.com -U postgres -d books C:\Path\To\books
```
> Ignore any harmless errors about pre-existing objects.

---

## Part 3 – Connect with pgAdmin and Load the Query Script

1. **Register Server in pgAdmin**
   - Open pgAdmin.
   - Right-click **Servers → Register → Server**.
   - Under **General**, name it `AIWorkshop`.

2. **Enter Connection Details**
   - Host: `pgaivector-<server-id>.postgres.database.azure.com`
   - Port: `5432`
   - Maintenance DB: `postgres`
   - Username: `postgres`
   - Password: `Password12345!!`
   - Save.

3. **Open `books` Database**
   - Expand **Databases** → `books`.
   - Open the query editor.
   - Press `Ctrl+O` and open `VectorQuery.sql`.

---

## Part 4 – Deploy the Embedding Model in Azure OpenAI

1. **Go to Azure OpenAI in the Azure Portal**
   - Open your Azure OpenAI resource.
   - Click **Explore Azure AI Foundry portal**.

2. **Select the Model**
   - Go to **Model catalog**.
   - Search for `embedding`.
   - Click **text-embedding-ada-002**.

3. **Deploy the Model**
   - Click **Use this model**.
   - Enter:
     - Deployment Name: `text-embedding-ada-002`
     - Deployment Type: `Global Standard`
   - Click **Deploy**.

---

## Part 5 – Run Vector Similarity Search in PostgreSQL

With the model deployed and `VectorQuery.sql` loaded in pgAdmin:

1. **Review the Query**
   ```sql
   select azure_ai.set_setting('azure_openai.endpoint', 'https://<your-endpoint>.openai.azure.com/');
   select azure_ai.set_setting('azure_openai.subscription_key', '<your-api-key>');

   WITH params AS (
     SELECT azure_openai.create_embeddings('text-embedding-ada-002', 'trigonometry')::vector(1536) AS qvec
   )
   SELECT
     b.book_id,
     b.title,
     b.desc_embedding <-> params.qvec AS distance
   FROM books AS b
   CROSS JOIN params
   ORDER BY distance
   LIMIT 5;
   ```

2. **Replace placeholders**:
   - `<your-endpoint>` → Your Azure OpenAI endpoint from the Keys & Endpoint page.
   - `<your-api-key>` → Your Azure OpenAI subscription key.

3. **Execute the Query**
   - The results will list the top 5 books most similar in meaning to the search term `"trigonometry"`.

**Result:** You have successfully run a vector similarity search in PostgreSQL using an Azure OpenAI embedding model.

