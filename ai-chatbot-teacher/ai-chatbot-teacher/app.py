
import os
import streamlit as st
from teacher_bot import generate_answer

st.set_page_config(page_title="AI Chatbot Teacher", page_icon="🎓")

st.title("🎓 AI Chatbot Teacher")
st.caption("Type your question in English, Hindi, Telugu (or many other languages). The bot will answer in the same language with a teacher-like structure.")

with st.sidebar:
    st.header("Settings")
    st.write("This app uses OpenAI's API under the hood.")
    st.code("export OPENAI_API_KEY=your_key_here", language="bash")
    st.text_input("Model", key="model", value=os.getenv("MODEL", "gpt-4o-mini"), help="Override by setting MODEL env var before running.")

prompt = st.text_area("Ask me anything to learn:", height=120, placeholder="e.g., What is photosynthesis? | प्रकाशसंश्लेषण क्या है? | ఫోటోసింథసిస్ అంటే ఏమిటి?")
go = st.button("Teach me ✨")

if go and prompt.strip():
    with st.spinner("Thinking like a teacher..."):
        try:
            answer = generate_answer(prompt)
            st.markdown(answer)
        except Exception as e:
            st.error(str(e))

st.markdown("---")
st.subheader("Try these:")
cols = st.columns(3)
examples = [
    "Explain Newton's First Law with a simple example.",
    "प्रकाशसंश्लेषण क्या है?",
    "తెలంగాణా రాష్ట్రం యొక్క రాజధాని ఏమిటి? వివరంగా చెప్పండి."
]
for i, ex in enumerate(examples):
    if cols[i].button(ex):
        st.session_state["example"] = ex
        st.experimental_rerun()
if "example" in st.session_state:
    st.text_area("Selected example:", value=st.session_state["example"], height=100)
