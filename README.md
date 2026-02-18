# 🎓 AI Learning & Interview Assistant  
### GenAI-Powered Personalized Learning & Career Preparation System

🔗 **Live Demo:** https://your-streamlit-app-link.streamlit.app  
📂 **GitHub Repository:** https://github.com/tabassumunnisa19/AI-Learning-Assistant-GenAI-Powered-Teaching-Companion

---

## 🚀 Overview

AI Learning & Interview Assistant is a Generative AI-powered educational system designed to:

- Generate structured learning plans
- Create entry-level and advanced interview questions
- Provide career-focused preparation checkpoints
- Adapt responses based on user level and goals

This project demonstrates modular GenAI architecture, prompt engineering, structured JSON extraction, and interactive deployment using Streamlit.

---

## 🎯 Key Features

✅ Personalized Learning Plan Generation  
✅ Entry-Level Concept Questions  
✅ Role-Based Interview Question Generation  
✅ AI-Generated Checkpoints & Roadmap  
✅ Structured JSON Output Extraction  
✅ Modular Code Architecture  
✅ Streamlit-Based Interactive UI  

---

## 🧠 How It Works

1. User enters:
   - Topic
   - Skill Level
   - Career Goal

2. The system:
   - Builds a structured prompt
   - Sends it to the language model
   - Extracts structured JSON from model output
   - Displays formatted learning roadmap and questions

---

## 🏗️ System Architecture

```
User Input (Streamlit UI)
        ↓
Prompt Builder (prompt.py)
        ↓
Model Loader (models.py)
        ↓
Response Generator (assistant.py)
        ↓
JSON Extraction (evaluator.py)
        ↓
Formatted Output (Streamlit UI)
```

---

## 📂 Project Structure

```
AI-Learning-Assistant-GenAI-Powered-Teaching-Companion/
│
├── app.py
│   └── Streamlit UI & Main App Logic
│
├── assistant.py
│   └── Model response generation logic
│
├── models.py
│   └── Model loading & tokenizer setup
│
├── prompt.py
│   └── Prompt engineering module
│
├── evaluator.py
│   └── JSON extraction & parsing
│
├── requirements.txt
│   └── Project dependencies
│
├── .gitignore
│
└── README.md
```

---

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit
- Transformers / LLM backend
- Prompt Engineering
- JSON Structured Output Parsing
- Git & GitHub
- Streamlit Cloud Deployment

---

## 🧩 Core Modules Explained

### 🔹 app.py
Handles:
- UI layout
- User inputs
- Model invocation
- Display formatting

### 🔹 prompt.py
Responsible for:
- Structured prompt building
- Context-aware generation

### 🔹 models.py
Handles:
- Model loading
- Tokenizer setup

### 🔹 assistant.py
Manages:
- Model inference
- Text generation logic

### 🔹 evaluator.py
Extracts:
- Structured JSON from LLM output
- Ensures reliable formatted output

---

## 💡 Sample Output Includes

- 📘 Learning Plan (Step-by-step roadmap)
- 🧠 Entry-Level Questions
- 💼 Interview-Level Questions
- ✅ Final Checkpoint Summary

---

## 🖥️ Running Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/tabassumunnisa19/AI-Learning-Assistant-GenAI-Powered-Teaching-Companion.git
cd AI-Learning-Assistant-GenAI-Powered-Teaching-Companion

----

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Streamlit App

streamlit run app.py


The app will open at:

http://localhost:8501


☁️ Deployment
This project is deployed using Streamlit Community Cloud.
To deploy:
Push project to GitHub
Connect repository in Streamlit Cloud
Select app.py as entry file
Add API keys in Secrets Manager (if required)
🔐 Environment Variables
If using API-based models:
Add secrets in:

.streamlit/secrets.toml

Example:

OPENAI_API_KEY = "your_key_here"

📈 Future Improvements
Add conversational memory
Add scoring & evaluation engine
Add multi-role modes (Student / Interview Mode)
Add model selection feature
Convert into SaaS platform
Add user authentication
Add analytics dashboard

🎓 Use Cases

Students preparing for interviews
Self-paced learners
Career transition professionals
Interview preparation coaching
Academic assistance systems


👩‍💻 Author

Tabassum Unnisa
AI & Data Science Enthusiast
Building real-world ML & GenAI systems.


⭐ If You Found This Useful

Give this repository a ⭐ and connect with me!



---



## 🏗️ System Architecture

