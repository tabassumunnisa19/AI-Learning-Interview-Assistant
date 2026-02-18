import streamlit as st

from models import load_model
from prompt import build_prompt
from assistant import generate_response
from evaluator import extract_json

st.set_page_config(page_title="AI Learning Assistant", layout="wide")

st.title("🎓 AI Learning & Interview Assistant")

topic = st.text_input("Enter topic", "Python for Data Analysis")
level = st.selectbox("Your level", ["Beginner", "Intermediate", "Advanced"])
goal = st.text_area("Your goal", "Prepare for data analyst interviews")

if st.button("Generate Learning Plan"):
    with st.spinner("Thinking..."):
        model, tokenizer = load_model()
        prompt = build_prompt(topic, level, goal)
        raw_output = generate_response(model, tokenizer, prompt)
        data = extract_json(raw_output)

    st.success("Generated successfully!")

    st.subheader("📘 Learning Plan")
    st.json(data["learning_plan"])

    st.subheader("🧠 Entry-Level Questions")
    for q in data["entry_level_questions"]:
        st.write("- ", q)

    st.subheader("💼 Interview Questions")
    st.json(data["interview_questions"])

    st.subheader("✅ Checkpoint")
    st.info(data["checkpoint"])
