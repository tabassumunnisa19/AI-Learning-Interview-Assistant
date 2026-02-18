import streamlit as st
import os
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
image_path = os.path.join(os.path.dirname(__file__), "Image.png")

if os.path.exists(image_path):
    image = Image.open(image_path)

    # Reduce vertical height to 50%
    width, height = image.size
    resized_image = image.resize((width, int(height * 0.5)))

    st.image(resized_image, use_container_width=True)
else:
    st.warning("Cover image not found.")


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

        try:
            model, tokenizer = load_model()
            prompt = build_prompt(topic, level, goal)
            raw_output = generate_response(model, tokenizer, prompt)

            # DEBUG output
            st.subheader("🔍 Raw Model Output (Debug)")
            st.code(raw_output)

            data = extract_json(raw_output)

        except Exception as e:
            st.error("❌ Error occurred while generating response.")
            st.error(str(e))
            st.stop()

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
