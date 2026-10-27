"""
Minimal AI agent example in Python.

This agent uses OpenAI's function-calling to run a simple ReAct loop:
1. Receive a user message
2. Call the LLM with available tools
3. If the LLM requests a tool, execute it and feed the result back
4. Repeat until a final answer is produced

Requirements:
    pip install openai

Environment:
    export OPENAI_API_KEY="sk-..."
"""

import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# --- Tool definitions -------------------------------------------------------

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for information (mocked).",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a simple math expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression like '2 + 2'",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]


# --- Tool implementations (mocked) ------------------------------------------

def execute_tool(name: str, arguments: dict):
    """Run a tool by name with the given arguments."""
    if name == "web_search":
        return f"[Mock search results for: {arguments['query']}]"
    if name == "calculator":
        # WARNING: eval() is unsafe in production. Use a safe math parser.
        try:
            return str(eval(arguments["expression"], {"__builtins__": {}}, {}))
        except Exception as exc:
            return f"Error: {exc}"
    return f"Unknown tool: {name}"


# --- Agent loop -------------------------------------------------------------

def run_agent(user_message: str, max_steps: int = 10) -> str:
    """Run the agent loop until it produces a final answer."""
    system_prompt = (
        "You are a helpful assistant with access to tools. "
        "Use tools when you need information. "
        "When you have enough information, give a final answer. "
        "Do not call more than one tool per step unless necessary."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    for step in range(max_steps):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )

        message = response.choices[0].message
        messages.append(message)

        # No tool call → final answer
        if not message.tool_calls:
            return message.content or "No answer produced."

        # Execute requested tools
        for tool_call in message.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            result = execute_tool(name, args)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result),
                }
            )

    return "Agent reached the maximum number of steps without completing."


# --- Example usage ----------------------------------------------------------

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY before running.")
        print("Example: export OPENAI_API_KEY='sk-...'")
    else:
        answer = run_agent("What is 25 * 4? Use the calculator tool.")
        print(answer)