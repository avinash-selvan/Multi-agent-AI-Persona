# 🧠 Personal Growth AI System

A modular AI-powered reflection system where your thoughts are met with insights from a council of AI personas — the Warrior, the Monk, and the Millionaire — all moderated by a Life Coach agent. This project simulates a rich inner dialogue to help users grow mentally, emotionally, and strategically.

---

## 🚀 How It Works

```
User Input → Life Coach → Persona Chain → Summary
```

- **User Logs**: Hourly reflections written by the user.
- **Life Coach Agent**: Routes input, manages agent flow, summarizes final insights.
- **Persona Agents**:
  - 🛡️ Warrior: Tough love and discipline.
  - 🧘 Monk: Detachment and spirituality.
  - 💰 Millionaire: Leverage and focus.
- **Memory**: Personal context from `user_profile.json` and past `logs.json`.

---

## 📁 Project Structure

```
/ai_persona_project/
├── agents/                   # All AI persona logic
│   ├── base_agent.py         # Base class for all agents
│   ├── warrior_agent.py
│   ├── monk_agent.py
│   └── millionaire_agent.py
│
├── controller/               # Life Coach logic
│   └── life_coach_agent.py
│
├── memory/                   # Manages logs and user profile
│   ├── user_profile_manager.py
│   └── log_manager.py
│
├── utils/                    # Templates and shared functions
│   └── prompt_templates.py
│
├── main.py                   # Entrypoint to run the system
├── user_profile.json         # Stores personal details
└── logs.json                 # Stores historical reflections
```

---

## 🛠️ Tech Stack

- **Python**
- **Ollama - Mistral**
- **LangChain**
- **JSON-based memory**

---

## 🧭 How to Use

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/ai_persona_project.git
   cd ai_persona_project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. # Set environment variable to use local Ollama with Mistral
```bash
export OLLAMA_MODEL="mistral"
```

4. **Run the app**
   ```bash
   python main.py
   ```

---

## 🧠 Sample Persona Behavior

| Persona     | Description                          | Example Response |
|-------------|--------------------------------------|------------------|
| **Warrior** | Pushes you with discipline and grit  | "Get up. You’ve done harder things before." |
| **Monk**    | Seeks calm and perspective           | "Detach from the noise. Reflect instead of react." |
| **Millionaire** | Focuses on clarity and leverage | "Time is your highest ROI tool. Use it well." |

---

## 📌 Future Improvements

- 🔄 Reordering persona chains dynamically
- 🧠 Smarter memory recall
- 📊 Reflection analytics
- 🖼️ Streamlit-based UI (optional)

---

## 🙏 Credits

Inspired by the idea of turning inner dialogue into an intelligent, guided growth experience using AI.

Built with 💻 and 🧘 by [Your Name].
