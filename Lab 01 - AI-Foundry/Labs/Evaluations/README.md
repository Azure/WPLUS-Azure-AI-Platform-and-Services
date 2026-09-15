# Evaluations with Microsoft Foundry

## Introduction

This lab is completed by running the `1-evaluation.ipynb` Jupyter notebook. The notebook creates a small health and fitness dataset, evaluates it locally, and submits a separate cloud evaluation to Microsoft Foundry.

## Objectives

By completing the notebook, you will:

- Create evaluation data in JSONL format
- Run an F1 Score evaluation locally
- Optionally run an AI-assisted Relevance evaluation
- Upload the dataset to a Microsoft Foundry project
- Submit a cloud evaluation and locate its results

## Estimated Time 

45 minutes

## Prerequisites

Before opening the notebook, confirm that:

- You completed the environment setup from the previous lab.
- A Microsoft Foundry project has been provisioned.
- Your account has the **Foundry User** role for the project. See [Microsoft Foundry RBAC documentation](https://learn.microsoft.com/azure/foundry/concepts/rbac-foundry).
- The Python environment contains the packages from the repository-root `requirements.txt` file, including `azure-ai-projects>=2.6.0,<3.0.0`.
- The repository-root `.env` file contains `AI_FOUNDRY_PROJECT_ENDPOINT` for cloud evaluation.
- To enable the optional local Relevance evaluator, `.env` also contains `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `MODEL_DEPLOYMENT_NAME`, and `MODEL_API_VERSION`.
- You are signed in to Azure CLI. In the VS Code terminal, run:

   ```powershell
   az login --use-device-code
   ```

   Open the displayed URL, enter the device code, sign in with your lab credentials, and select the default subscription when prompted.

## Run the Notebook

1. Open `1-evaluation.ipynb` in this folder using VS Code.
2. Select the Python kernel that contains the packages from `requirements.txt`.
3. Run the notebook cells in order from top to bottom.
4. Review each code cell's output before continuing.

Running cells out of order can leave required variables or generated files unavailable. Restart the kernel and run all cells again if the notebook state becomes inconsistent.

## Code Cell Guide

### Cell 5 - Load Configuration and Create Evaluation Data

Loads the repository-root `.env` file and reports which Foundry and Azure OpenAI settings are available. It then creates three sample question, context, response, and ground-truth records and writes them to `health_fitness_eval_data.jsonl`.

Cloud evaluation is skipped later if `AI_FOUNDRY_PROJECT_ENDPOINT` is missing. Local F1 evaluation does not require Azure OpenAI configuration.

Expected result: confirmation that three samples were written to a JSONL file.

### Cell 7 - Run the Local Evaluation

Configures `F1ScoreEvaluator` and maps each generated response to its ground-truth answer. When the Azure OpenAI settings are available, it also adds `RelevanceEvaluator` to assess how relevant each response is to its query.

The cell runs `evaluate`, prints the aggregate metrics, and saves detailed results to `local_evaluation_results.json`.

Expected result: a completed local evaluation with one or more metric values. Without complete Azure OpenAI configuration, only F1 Score is reported.

### Cell 9 - Submit the Cloud Evaluation

Uses `DefaultAzureCredential` and `AIProjectClient` to connect to the configured Microsoft Foundry project. It uploads the JSONL dataset, defines a built-in F1 Score criterion, creates an evaluation, and submits a JSONL evaluation run.

The cell prints the evaluation ID, run ID, and initial status, then saves the submission details to `cloud_evaluation_results.json`. The clients and credential are closed when processing finishes.

Expected result: a submitted cloud evaluation that can be viewed in Microsoft Foundry under **Evaluation**. If `AI_FOUNDRY_PROJECT_ENDPOINT` is missing, this cell skips cloud submission.

## Troubleshooting

- **`.env` not found:** Complete the environment setup and place `.env` in the repository root.
- **Relevance evaluator is not included:** Verify all four Azure OpenAI variables listed in Prerequisites.
- **Authentication failed:** Run `az login --use-device-code`, confirm the active subscription, and rerun Cell 9.
- **Permission denied:** Confirm that your account has the **Foundry User** role on the project.
- **Project not found:** Verify that `AI_FOUNDRY_PROJECT_ENDPOINT` uses the project endpoint format shown in Microsoft Foundry.
- **Storage error:** Confirm that the Foundry project has a connected storage account and that the project identity has access to it.

## Expected Results

After running the complete notebook, you should have:

- A generated health and fitness JSONL dataset
- Local F1 Score results in `local_evaluation_results.json`
- Local Relevance results when Azure OpenAI is configured
- Cloud evaluation submission details in `cloud_evaluation_results.json`
- A cloud evaluation run visible in the Microsoft Foundry portal

## Additional Resources

- [Azure AI Evaluation SDK](https://learn.microsoft.com/python/api/azure-ai-evaluation/azure.ai.evaluation)
- [Evaluating Generative AI Applications](https://learn.microsoft.com/azure/foundry/observability/how-to/evaluate-generative-ai-app)

