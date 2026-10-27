"""
Web-search AI agent example in Python.

This agent searches the web for a topic and returns a short summary with sources.
It demonstrates:
- Tool use (web search)
- Basic ReAct loop
- Source citation in the final answer

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
]


# --- Tool implementation (mocked) -------------------------------------------

def execute_tool(name: str, arguments: dict):
    """Run a tool by name with the given arguments."""
    if name == "web_search":
        query = arguments["query"]
        return (
            f"[Mock search results for: {query}]\n"
            f"1. https://example.com/result1 - Overview of {query}\n"
            f"2. https://example.com/result2 - Latest news on {query}\n"
            f"3. https://example.com/result3 - Expert guide to {query}"
        )
    return f"Unknown tool: {name}"


# --- Agent loop -------------------------------------------------------------

def run_agent(user_message: str, max_steps: int = 5) -> str:
    """Run the web-search agent loop."""
    system_prompt = (
        "You are a research assistant. Your job is to search the web for "
        "information and return a concise summary with citations. "
        "Always cite your sources using the URLs from search results. "
        "Use the web_search tool when you need information."
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

        if not message.tool_calls:
            return message.content or "No answer produced."

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
        answer = run_agent("What are the latest developments in AI agents?")
        print(answer)