import os
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider

import logfire

# configure logfire
logfire.configure(token='logfire_api_key')
logfire.instrument_pydantic_ai()

api_key = os.getenv("GROQ_API_KEY", "API_KEY_value")
# MCP Math Server wrapper unchanged
mcp_server = MCPServerStdio(
    'uv',
    args=[
        "run","main.py"
    ]
)

system_prompt = (
    "You are a strict math tutor agent. Follow these rules exactly:\n"
    "1. ALWAYS execute the correct MCP tool for every math calculation.\n"
    "2. NEVER output function signatures, JSON, or tool call schemas.\n"
    "3. NEVER output explanations, sentences, or extra words.\n"
    "4. AFTER the tool executes, return ONLY the final numeric result as plain text (e.g., '25').\n"
    "5. If no tool matches the question, reply EXACTLY with: 'Sorry, I can only help with math calculations.'\n"
    "6. Do NOT skip tool execution. Do NOT invent answers.\n"
    "Failure to follow these rules is not allowed."
)

# Set your Groq API key (replace with your actual key or set in env variable)
# Initialize Groq Model with Provider and API key
groq_model = GroqModel(
    "llama-3.3-70b-versatile",  # valid Groq model name
    provider=GroqProvider(api_key=api_key)
)
agent = Agent(
    groq_model,
    toolsets=[mcp_server],
    system_prompt=system_prompt,
     
)
if __name__ == "__main__":
    print("Math Agent with Groq Model Ready. Type math questions or 'quit' to exit.\n")
    while True:
        query = input("Ask: ")
        if query.lower() in {"quit", "exit"}:
            break
        try:
            result = agent.run_sync(query)
            print("Answer:", result.output)  # use .output not .data
        except Exception as e:
            error_msg = str(e)
            if ("tool call validation failed" in error_msg or 
                "tool_use_failed" in error_msg or 
                "Failed to call a function" in error_msg):
                print("Answer: Sorry, I can only help with math calculations.")
            else:
                print("Error:", e)


