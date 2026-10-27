/**
 * Minimal AI agent example in JavaScript (Node.js).
 *
 * This agent uses OpenAI's function-calling to run a simple ReAct loop.
 *
 * Requirements:
 *   npm install openai dotenv
 *
 * Environment:
 *   export OPENAI_API_KEY="sk-..."
 *   (or create a .env file with OPENAI_API_KEY=sk-...)
 */

require("dotenv").config();
const { OpenAI } = require("openai");

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// --- Tool definitions -------------------------------------------------------

const TOOLS = [
  {
    type: "function",
    function: {
      name: "web_search",
      description: "Search the web for information (mocked).",
      parameters: {
        type: "object",
        properties: {
          query: { type: "string", description: "Search query" },
        },
        required: ["query"],
      },
    },
  },
  {
    type: "function",
    function: {
      name: "calculator",
      description: "Evaluate a simple math expression.",
      parameters: {
        type: "object",
        properties: {
          expression: {
            type: "string",
            description: "Math expression like '2 + 2'",
          },
        },
        required: ["expression"],
      },
    },
  },
];

// --- Tool implementations (mocked) ------------------------------------------

function executeTool(name, arguments) {
  if (name === "web_search") {
    return `[Mock search results for: ${arguments.query}]`;
  }
  if (name === "calculator") {
    try {
      // WARNING: eval() is unsafe in production. Use a safe math parser.
      return String(eval(arguments.expression));
    } catch (err) {
      return `Error: ${err.message}`;
    }
  }
  return `Unknown tool: ${name}`;
}

// --- Agent loop -------------------------------------------------------------

async function runAgent(userMessage, maxSteps = 10) {
  const systemPrompt =
    "You are a helpful assistant with access to tools. " +
    "Use tools when you need information. " +
    "When you have enough information, give a final answer. " +
    "Do not call more than one tool per step unless necessary.";

  const messages = [
    { role: "system", content: systemPrompt },
    { role: "user", content: userMessage },
  ];

  for (let step = 0; step < maxSteps; step++) {
    const response = await client.chat.completions.create({
      model: "gpt-4o-mini",
      messages,
      tools: TOOLS,
      tool_choice: "auto",
    });

    const message = response.choices[0].message;
    messages.push(message);

    // No tool call → final answer
    if (!message.tool_calls || message.tool_calls.length === 0) {
      return message.content || "No answer produced.";
    }

    // Execute requested tools
    for (const toolCall of message.tool_calls) {
      const name = toolCall.function.name;
      const args = JSON.parse(toolCall.function.arguments);
      const result = executeTool(name, args);

      messages.push({
        role: "tool",
        tool_call_id: toolCall.id,
        content: String(result),
      });
    }
  }

  return "Agent reached the maximum number of steps without completing.";
}

// --- Example usage ----------------------------------------------------------

(async () => {
  if (!process.env.OPENAI_API_KEY) {
    console.log("Please set OPENAI_API_KEY before running.");
    console.log("Example: export OPENAI_API_KEY='sk-...'");
    process.exit(1);
  }

  const answer = await runAgent("What is 25 * 4? Use the calculator tool.");
  console.log(answer);
})();