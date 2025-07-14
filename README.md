# 🧠 Agentic AI Projects

Welcome to the **Agentic AI Projects** repository — a collection of hands-on projects built using various **agentic AI frameworks** like **CrewAI**, **OpenAI Agents SDK**, **LangGraph**, and **AutoGen**.

The goal is to explore, build, and share real-world applications of multi-agent LLM systems — from planning and decision-making to tool usage and automation.

---

## 📁 Project Structure

Each project in this repo is self-contained with its own `README.md`, dependencies, and usage instructions.


---

## ✅ Project 1: GymTrainer (CrewAI)

A multi-agent fitness planner that uses **CrewAI** to coordinate agents for:
- 🏋️ Exercise planning  
- 🥗 Diet recommendation  
- 📝 Summarization (HTML formatted)  
- 📬 Email delivery

### 🔧 Tech Stack
- **CrewAI (Open Source Framework)**
- `litellm` for LLM inference
- `uv` for environment management
- `Gradio` for UI

### 📦 Features
- Custom fitness plans based on user profile and goals
- Email notifications with HTML summaries
- Fully agent-driven logic using `crew` and `flows`

## ✅ Project 2: Gmail Auto-Reply Agent (LangGraph)

An intelligent, graph-driven email assistant using **LangGraph** that:
- 📥 Reads unread emails  
- 🧠 Decides if a reply is needed (LLM-based)  
- ✍️ Generates and drafts replies  
- 📬 Marks emails as read

### 🔧 Tech Stack
- **LangGraph** for graph logic  
- `langchain` for tools & LLM orchestration  
- **Google Gemini Flash** for fast LLM inference  
- Gmail API (OAuth 2.0) for email operations

### 📦 Features
- Auto-reply for actionable emails  
- Multi-step flow: fetch → analyze → reply → mark read  
- Conditional branching via LangGraph  
- Logging and error handling built-in

---

## 🔜 Coming Soon

| Framework         | Project Idea                        | Status     |
|------------------|-------------------------------------|------------|
| OpenAI Agents SDK| AI Email Assistant                  | 🛠️ In progress |
| LangGraph        | AI Travel Planner                   | ⏳ Planned |
| AutoGen          | Research Assistant (PDF + web)      | ⏳ Planned |

---

## 🚀 Goals of This Repo

- Learn and document how to build agentic apps across frameworks
- Compare features, performance, and DX (Developer Experience)
- Share templates and real-world examples for the community

---

## 📬 Stay Connected

If you're building something with agents or curious about these frameworks — feel free to connect!

---


