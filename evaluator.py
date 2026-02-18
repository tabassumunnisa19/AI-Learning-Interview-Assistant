import json
import re

REQUIRED_KEYS = [
    "topic",
    "learning_plan",
    "entry_level_questions",
    "interview_questions",
    "checkpoint"
]

def extract_json(text):
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON found in model output")

    data = json.loads(match.group())

    for key in REQUIRED_KEYS:
        if key not in data:
            raise ValueError(f"Missing key: {key}")

    return data
