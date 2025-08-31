
import os
import sys
import re
from typing import List, Dict, Optional

# Optional language detection to explicitly enforce "respond in same language"
try:
    from langdetect import detect
except Exception:
    detect = None

# Try both the modern and legacy OpenAI Python SDKs for compatibility.
# Set model via env var MODEL (default: gpt-4o-mini). Requires OPENAI_API_KEY.
MODEL = os.getenv("MODEL", "gpt-4o-mini")

def _format_system_prompt(language_hint: Optional[str]) -> str:
    """
    Build a system prompt that enforces a teacher-like style and structured output.
    If a language hint is provided (e.g., 'Hindi', 'English', 'Telugu'), it will
    instruct the model to answer in that language. Otherwise, the model should reply
    in the same language as the user message.
    """
    if language_hint:
        lang_line = f"Respond ONLY in {language_hint}. Mirror the user's language variety and tone."
    else:
        lang_line = "Respond in the SAME language as the user input. Mirror the user's language variety and tone."

    return (
        "You are EduMentor, a helpful, patient teacher chatbot. "
        "Your job is to give clear, structured, and educational answers with friendly tone. "
        f"{lang_line} "
        "Always include concise sections with the following headings (translated to the reply language): "
        "1) Definition/Answer, 2) Explanation, 3) Example(s), 4) Key Points/Bullets, 5) Quick Quiz (1-2 short questions). "
        "Keep it simple but correct. Use short paragraphs and bullet points where helpful."
    )

def _detect_language_name(text: str) -> Optional[str]:
    """
    Best-effort language name for hints. Only returns names for a small set of languages
    to avoid mislabeling; otherwise returns None and lets the model mirror automatically.
    """
    if not text or detect is None:
        return None
    try:
        code = detect(text)
    except Exception:
        return None

    mapping = {
        "en": "English",
        "hi": "Hindi",
        "te": "Telugu",
        "bn": "Bengali",
        "ta": "Tamil",
        "mr": "Marathi",
        "gu": "Gujarati",
        "pa": "Punjabi",
        "ur": "Urdu"
    }
    return mapping.get(code, None)

def _chat_openai(messages: List[Dict[str, str]]) -> str:
    """
    Try new OpenAI SDK first, then legacy as fallback.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Please set it in your environment.")

    # New SDK style
    try:
        from openai import OpenAI  # type: ignore
        client = OpenAI(api_key=api_key)
        resp = client.chat.completions.create(model=MODEL, messages=messages)
        return resp.choices[0].message.content.strip()
    except Exception:
        # Legacy SDK style
        try:
            import openai  # type: ignore
            openai.api_key = api_key
            resp = openai.ChatCompletion.create(model=MODEL, messages=messages)
            return resp["choices"][0]["message"]["content"].strip()
        except Exception as e:
            raise RuntimeError(f"Failed to call OpenAI API: {e}")

def generate_answer(user_text: str) -> str:
    """
    Core function that: (1) detects language (best-effort), (2) builds prompts,
    (3) calls the model, and (4) returns the model's answer.
    """
    if not user_text or not user_text.strip():
        return "Please enter a question or topic to learn about."

    language_hint = _detect_language_name(user_text)
    system_prompt = _format_system_prompt(language_hint)

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": (
                "Act as a teacher. Explain clearly and step-by-step where needed. "
                "Remember to answer in the SAME language as my question and use the required sections.\n\n"
                f"My question: {user_text}"
            ),
        },
    ]

    return _chat_openai(messages)

if __name__ == "__main__":
    # Quick manual test via: python teacher_bot.py "What is photosynthesis?"
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print("Usage: python teacher_bot.py <your question in any supported language>")
        sys.exit(1)
    print(generate_answer(query))
