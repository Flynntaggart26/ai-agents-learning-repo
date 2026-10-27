/**
 * Multi-agent pipeline example in JavaScript (Node.js).
 *
 * This demonstrates a content team pipeline:
 *   Researcher -> Writer -> Editor -> Publisher
 *
 * Each agent is a separate LLM call with its own system prompt.
 * The output of one agent becomes the input of the next.
 *
 * Requirements:
 *   npm install openai dotenv
 *
 * Environment:
 *   export OPENAI_API_KEY="sk-..."
 */

require("dotenv").config();
const { OpenAI } = require("openai");

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// --- Agent configurations ---------------------------------------------------

const AGENTS = [
  {
    name: "Researcher",
    systemPrompt:
      "You are a research assistant. Find key facts and sources about the topic. " +
      "Return a bulleted list of findings with source URLs (use example URLs if needed).",
  },
  {
    name: "Writer",
    systemPrompt:
      "You are a content writer. Turn the research findings into a clear, engaging " +
      "article draft. Keep it concise but informative.",
  },
  {
    name: "Editor",
    systemPrompt:
      "You are an editor. Review the article draft for clarity, tone, and accuracy. " +
      "Return the improved version with a brief summary of changes.",
  },
  {
    name: "Publisher",
    systemPrompt:
      "You are a publisher. Format the final article with a title, introduction, " +
      "body, conclusion, and sources section. Ready for publication.",
  },
];

// --- LLM call helper --------------------------------------------------------

async function callAgent(systemPrompt, inputText) {
  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: inputText },
    ],
    temperature: 0.7,
  });
  return response.choices[0].message.content || "";
}

// --- Pipeline runner --------------------------------------------------------

async function runPipeline(topic) {
  console.log(`\n=== Multi-Agent Pipeline: "${topic}" ===\n`);

  let content = topic;

  for (const agent of AGENTS) {
    console.log(`--- ${agent.name} working... ---`);
    content = await callAgent(agent.systemPrompt, content);
    console.log(content);
    console.log("\n");
  }

  console.log("=== Pipeline complete ===");
  return content;
}

// --- Example usage ----------------------------------------------------------

(async () => {
  if (!process.env.OPENAI_API_KEY) {
    console.log("Please set OPENAI_API_KEY before running.");
    console.log("Example: export OPENAI_API_KEY='sk-...'");
    process.exit(1);
  }

  await runPipeline("The future of remote work in 2026");
})();