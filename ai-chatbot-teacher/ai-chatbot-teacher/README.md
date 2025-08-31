# 🎓 AI Chatbot Teacher

A simple multilingual teacher-style chatbot built with Python. It:
- Understands multiple languages (tested with **English, Hindi, Telugu**; many others may work too).
- **Responds in the same language** as the input.
- Gives **structured, educational** answers (Definition → Explanation → Examples → Key Points → Quick Quiz).
- Comes with a **Streamlit web UI** and a **CLI**.

> ✅ Uses the OpenAI API under the hood. Any recent chat-capable model should work. Default: `gpt-4o-mini` (set via `MODEL` env var).

---

## 🚀 Quick Start

### 1) Clone & Install
```bash
git clone <your-repo-url>.git
cd ai-chatbot-teacher
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Set API Key
```bash
# macOS/Linux
export OPENAI_API_KEY="your_key_here"

# Windows PowerShell
setx OPENAI_API_KEY "your_key_here" && set OPENAI_API_KEY="your_key_here"
```

(Optional) Pick a model:
```bash
export MODEL="gpt-4o-mini"   # or gpt-4o, gpt-4o-mini-transcribe, etc.
```

### 3A) Run the Web App (Streamlit)
```bash
streamlit run app.py
```

### 3B) Run the CLI
```bash
python cli.py --question "What is photosynthesis?"
# Or interactive mode:
python cli.py
```

---

## 🧠 How It Works (Design Notes)

- **Language detection**: We use `langdetect` to *hint* the reply language (English/Hindi/Telugu, etc.). If the language is unknown, the model is instructed to mirror the user's language automatically.
- **Teacher persona**: A structured **system prompt** enforces a teacher-like style and headings in the reply.
- **Model calls**: The code supports both the **new** OpenAI SDK (`openai.OpenAI`) and the **legacy** SDK (`openai.ChatCompletion`) for convenience.
- **Separation of concerns**: `teacher_bot.py` contains the core logic; `app.py` is the Streamlit UI; `cli.py` is a terminal interface.

---

## ✅ Requirements Met

- Python + ML/NLP library (OpenAI API) ✅
- At least 3 languages (English/Hindi/Telugu demonstrated) ✅
- Teacher-style, structured answers ✅
- Basic CLI + Streamlit UI ✅

---

## 📹 2–4 min Screen Recording (What to Cover)

Use any screen recorder. Suggested outline/script:

1. **Intro (20s)**  
   - “This is the AI Chatbot Teacher. It understands questions in English, Hindi, and Telugu, and replies in the same language with a teacher-like structure.”

2. **How it Works (60–90s)**  
   - Show `teacher_bot.py`: system prompt enforcing sections and language mirroring.  
   - Mention `langdetect` and how it hints the language.  
   - Show the OpenAI call and fallback to legacy SDK.  
   - Explain extensibility (add more languages or deploy).

3. **Demo (60–90s)**  
   - Ask one question in English (e.g., “Explain Newton’s First Law”).  
   - Ask one in Hindi (e.g., “प्रकाशसंश्लेषण क्या है?”).  
   - Ask one in Telugu.  
   - Show the structured sections in answers.

4. **Wrap-up (15s)**  
   - Mention repo link and usage steps from README.

---

## 🧪 Example Prompts

- **English**: *“Explain Newton’s First Law with a simple example.”*  
- **Hindi**: *“प्रकाशसंश्लेषण क्या है?”*  
- **Telugu**: *“ఫోటోసింథసిస్ అంటే ఏమిటి? ఉదాహరణతో చెప్పండి.”*

---

## 🧰 Troubleshooting

- **`OPENAI_API_KEY is not set`**: Make sure you exported the key in your terminal/session.
- **Firewall/Network issues**: Ensure you have internet access; the app calls the OpenAI API.
- **Wrong/unknown model**: Set `MODEL` env var to a valid chat model.
- **Language not mirrored**: The system prompt enforces mirroring. If you still see issues, include a short example of your desired tone style in the prompt.

---

## 📦 Project Structure

```
ai-chatbot-teacher/
├─ app.py              # Streamlit web UI
├─ cli.py              # Command-line interface
├─ teacher_bot.py      # Core logic: prompt + OpenAI call
├─ requirements.txt
└─ README.md
```

---

## 🔒 Notes on Data & Safety

- This project sends your questions to the OpenAI API for processing. Do not input sensitive personal data.
- The app is for **educational** purposes and may produce mistakes. Verify important facts.

---

## 🛫 Optional: Deploy

- **Streamlit Cloud**: Push to GitHub, add `OPENAI_API_KEY` as a secret, click “Deploy”.  
- **Railway/Render/Heroku**: Use `requirements.txt`, set env vars, run `streamlit run app.py` as the start command.

---

## 📄 License

MIT
