# 🤖 Automated Gmail Reply Assistant using LangGraph & LLMs

This project is an intelligent Gmail automation tool that:
- Reads unread emails
- Uses an LLM to decide if a reply is required
- Automatically generates and drafts the reply (if needed)
- Marks the email thread as read

---

## ✨ Features

- 📩 **Reads Gmail inbox** (unread messages)
- 🧠 **LLM-based decision making**: Is a reply required?
- 💬 **Reply generation** using LLM
- ✍️ **Drafts replies** with correct headers (`In-Reply-To`, `References`)
- 📬 **Marks thread as read** once done

---

## 🧱 Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph) - for graph-based logic
- [LangChain](https://github.com/langchain-ai/langchain) - tool & agent orchestration
- [Google Gemini Flash](https://ai.google.dev/gemini-api/docs/get-started/python) - fast LLM
- [Gmail API](https://developers.google.com/gmail/api) - for interacting with email
- [Google Auth / OAuth2](https://developers.google.com/identity) - for access control

---


---

## 🔄 Workflow (LangGraph Nodes)

1. **Email Fetcher**: Get latest unread email
2. **Mail Analyst**: LLM determines if reply is needed
3. **Reply Generator**: Generate response if necessary
4. **Mail Drafting**: Compose and draft the email
5. **Mark as Read**: Remove UNREAD label

---

## ⚙️ Setup

### 1. Enable Gmail API

- Go to https://console.cloud.google.com/
- Create a project and enable Gmail API
- Create OAuth2 client credentials (desktop app)
- Save both `credentials.json`in your root directory

### 2. Clone and Install

```bash
git clone https://github.com/harjasdt/Agentic_projects.git
cd langgraph_email_agent
pip install -r requirements.txt
```

### 3. Run!
```bash
python main.py
```

