# 🤖 Collaborative Multi-Agent AI System

> 4 specialized AI agents that communicate, delegate tasks, and collaborate to produce comprehensive, reviewed articles on any topic — built with Python, Streamlit, and Groq API (100% free).

## 🌐 Live Demo
**[🚀 Try the live app → https://multi-agent-ai-system-g6k3.onrender.com](https://multi-agent-ai-system-g6k3.onrender.com)**

## 📌 What Is This Project?
A Collaborative Multi-Agent AI System where multiple specialized AI agents each handle a specific role — they communicate through a Message Bus, share data through Shared Memory, and work together in a pipeline to complete complex tasks automatically.

You enter any topic → 4 agents automatically research, write, review → you get a polished, downloadable article.

## 🎬 How It Works
```
You enter a topic → Planner Agent → Researcher Agent → Writer Agent → Reviewer Agent → Final Article
```

## 🧠 The 4 Agents
| Agent | Role | Output |
|-------|------|--------|
| 🗂️ Planner | Strategic planning | Structured task plan |
| 🔍 Researcher | Information gathering | Research findings |
| ✍️ Writer | Content creation | Full article draft |
| ✅ Reviewer | Quality assurance | Polished final output |

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/uwaiszmuhammed07-hash/multi-agent-ai-system.git
cd multi-agent-ai-system
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free key at https://console.groq.com

### 5. Run the app
```bash
streamlit run app.py
```

## 🛠️ Tech Stack
| Technology | Purpose |
|-----------|---------|
| Python 3.10 | Core language |
| Streamlit | Interactive web UI |
| Groq API | Free LLM inference |
| LLaMA 3.3 70B | AI model powering all agents |
| python-dotenv | Secure API key management |

## 📁 Project Structure
```
multi_agent_system/
├── .env
├── requirements.txt
├── app.py
├── agents/
│   ├── base_agent.py
│   ├── planner_agent.py
│   ├── researcher_agent.py
│   ├── writer_agent.py
│   └── reviewer_agent.py
└── core/
    ├── message_bus.py
    └── memory.py
```

## ✨ Key Features
- ✅ 100% Free — Groq free tier, no credit card needed
- ✅ Modular — Each agent is independent and easy to extend
- ✅ Real-time UI — Live agent activity in Streamlit
- ✅ 4 Output Tabs — Plan, Research, Article, Final Output
- ✅ Download Button — Export final article as text file

## 💡 Use Cases
- 📚 Students — Generate structured research reports
- ✍️ Content Creators — Produce full blog posts automatically
- 📊 Business Analysts — Quick market research reports
- 👨‍💻 Developers — Template for AI pipeline projects

## 👨‍💻 Built By
**Uwais** — March 2026

⭐ Star this repo if you found it useful!
