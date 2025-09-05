# 🧮 Maths Agent

Maths Agent is an intelligent assistant designed to **answer math queries for students**.  
Unlike traditional LLM-based agents, this project ensures that **all calculations are handled by tools** (not the LLM).  
The LLM is responsible only for **decision-making and context understanding**, while mathematical operations are executed deterministically through MCP tools.

---

## 🚀 Features
- ✅ Context-aware agent powered by `pydantic-ai`
- ✅ Tools integration using MCP (`@agent.tool`) for math operations
- ✅ LLM **does not** perform calculations — only reasoning/decision-making
- ✅ Supports custom math functions for flexible problem-solving
- ✅ Integrated with **Logfire** for debugging and observability
- ✅ Token usage optimized by offloading calculations to tools

---

## 🏗️ Architecture
1. **Agent Layer** – Uses LLM for context understanding and tool selection.  
2. **MCP Tools** – Define and handle math operations (`add`, `subtract`, `multiply`, etc.).  
3. **Execution Flow**  
   - Agent receives student query  
   - Decides which tool to call  
   - Calls MCP tool for calculation  
   - Returns final numeric result to the student  
4. **Logfire Integration** – Tracks execution, debugging, and helps reduce token usage.

---

## 📂 Project Structure
MathsAgent/
├── agent.py # Main entry point for the agent
├── tools/ # MCP tools for calculations
├── requirements.txt # Python dependencies
└── README.md # Documentation

---

## 🛠️ Tech Stack
1. Python
2. pydantic-ai (for agent + MCP integration)
3. Groq LLM (for context & decision making)
4. Logfire (for debugging and observability)


