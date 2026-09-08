import asyncio
import json
import os
import sys
from contextlib import AsyncExitStack
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FunctionTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from openai.types.responses.response_input_param import FunctionCallOutput, ResponseInputParam


os.system("cls" if os.name == "nt" else "clear")

load_dotenv(Path(__file__).resolve().parents[2] / ".env")
project_endpoint = (
    os.getenv("AI_FOUNDRY_PROJECT_ENDPOINT")
    or os.getenv("PROJECT_CONNECTION_STRING")
    or os.getenv("AZURE_AI_PROJECT_ENDPOINT")
    or os.getenv("PROJECT_ENDPOINT")
)
model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

print(f"Project Endpoint: {project_endpoint}")
print(f"Model Deployment: {model_deployment}")

if not project_endpoint:
    print("Error: No project endpoint found. Check your .env file.")
    sys.exit(1)
if not model_deployment:
    print("Error: No model deployment found. Check your .env file.")
    sys.exit(1)


async def connect_to_server(exit_stack: AsyncExitStack) -> ClientSession:
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(Path(__file__).with_name("server.py"))],
        env=None,
    )

    stdio_transport = await exit_stack.enter_async_context(stdio_client(server_params))
    stdio, write = stdio_transport
    session = await exit_stack.enter_async_context(ClientSession(stdio, write))
    await session.initialize()

    response = await session.list_tools()
    print(f"Connected to server with tools: {[tool.name for tool in response.tools]}")
    return session


def build_function_tools(mcp_tools) -> list[FunctionTool]:
    return [
        FunctionTool(
            name=tool.name,
            description=tool.description or f"Call the {tool.name} MCP tool.",
            parameters=tool.inputSchema,
            strict=False,
        )
        for tool in mcp_tools
    ]


def mcp_result_to_text(result) -> str:
    if result.structuredContent is not None:
        return json.dumps(result.structuredContent)

    content = []
    for block in result.content:
        if block.type == "text":
            content.append(block.text)
        else:
            content.append(block.model_dump_json(by_alias=True))
    return "\n".join(content)


async def invoke_agent(session, openai_client, conversation_id, agent, user_input):
    agent_reference = {
        "agent_reference": {
            "name": agent.name,
            "type": "agent_reference",
        }
    }
    response = openai_client.responses.create(
        conversation=conversation_id,
        input=user_input,
        extra_body=agent_reference,
    )

    for _ in range(10):
        tool_outputs: ResponseInputParam = []

        for item in response.output:
            if item.type != "function_call":
                continue

            arguments = json.loads(item.arguments) if item.arguments else {}
            print(f"Calling MCP tool: {item.name}({arguments})")
            result = await session.call_tool(item.name, arguments)
            output = mcp_result_to_text(result)

            if result.isError:
                output = f"MCP tool returned an error: {output}"

            tool_outputs.append(
                FunctionCallOutput(
                    type="function_call_output",
                    call_id=item.call_id,
                    output=output,
                )
            )

        if not tool_outputs:
            return response

        response = openai_client.responses.create(
            conversation=conversation_id,
            input=tool_outputs,
            extra_body=agent_reference,
        )

    raise RuntimeError("Agent exceeded the maximum number of MCP tool-call rounds.")


async def chat_loop(session: ClientSession) -> None:
    project_client = AIProjectClient(
        endpoint=project_endpoint,
        credential=DefaultAzureCredential(),
    )
    openai_client = project_client.get_openai_client()

    tools_response = await session.list_tools()
    function_tools = build_function_tools(tools_response.tools)

    agent = project_client.agents.create_version(
        agent_name="inventory-agent",
        definition=PromptAgentDefinition(
            model=model_deployment,
            instructions="""
            You are an inventory assistant. Follow these guidelines:
            - Recommend restock if item inventory < 10 and weekly sales > 15.
            - Recommend clearance if item inventory > 20 and weekly sales < 5.
            Use the available inventory and weekly sales tools before making recommendations.
            """,
            tools=function_tools,
        ),
    )
    conversation = openai_client.conversations.create()

    try:
        while True:
            user_input = input(
                "Enter a prompt for the inventory agent. Use 'quit' to exit.\nUSER: "
            ).strip()
            if user_input.lower() == "quit":
                print("Exiting chat.")
                break

            response = await invoke_agent(
                session,
                openai_client,
                conversation.id,
                agent,
                user_input,
            )
            print(f"AGENT:\n{response.output_text}\n")
    finally:
        print("Cleaning up agent:")
        try:
            project_client.agents.delete_version(
                agent_name=agent.name,
                agent_version=agent.version,
            )
        finally:
            openai_client.close()
            project_client.close()
        print("Deleted inventory agent version.")


async def main() -> None:
    async with AsyncExitStack() as exit_stack:
        session = await connect_to_server(exit_stack)
        await chat_loop(session)


if __name__ == "__main__":
    asyncio.run(main())
