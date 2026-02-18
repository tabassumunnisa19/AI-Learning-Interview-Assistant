import streamlit as st
from PIL import Image

from models import load_model
from prompt import build_prompt
from assistant import generate_response
from evaluator import extract_json

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="AI Learning Assistant",
    layout="wide"
)

# ----------------------------------------------------
# Cover Image Section
# ----------------------------------------------------
import os
from PIL import Image

image_path = os.path.join(os.path.dirname(__file__), "Image.png")
image = Image.open(image_path)

# Resize image to reduce vertical height
width, height = image.size
new_height = int(height * 0.5)  # reduce to 50% height
resized_image = image.resize((width, new_height))

st.image(resized_image, use_container_width=True)

# Optional spacing
st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------
# Title Section
# ----------------------------------------------------
st.title("🎓 AI Learning & Interview Assistant")
st.markdown("Empowering personalized learning and intelligent interview preparation using Generative AI.")

# ----------------------------------------------------
# User Inputs
# ----------------------------------------------------
topic = st.text_input("Enter topic", "Python for Data Analysis")
level = st.selectbox("Your level", ["Beginner", "Intermediate", "Advanced"])
goal = st.text_area("Your goal", "Prepare for data analyst interviews")

# ----------------------------------------------------
# Generate Button
# ----------------------------------------------------
if st.button("Generate Learning Plan"):
    with st.spinner("Thinking... Generating your personalized roadmap..."):
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
