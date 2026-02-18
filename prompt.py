def build_prompt(topic, level, goal):
    return f"""
Create a personalized AI learning assistant response.

STRICT RULES:
- Respond ONLY in valid JSON
- No explanations
- No markdown
- No text outside JSON

JSON Schema:
{{
  "topic": "{topic}",
  "level": "{level}",
  "learning_plan": {{
    "day_1": [string],
    "day_2": [string],
    "day_3": [string]
  }},
  "entry_level_questions": [string],
  "interview_questions": {{
    "basic": [string],
    "intermediate": [string],
    "advanced": [string]
  }},
  "checkpoint": string
}}

User Goal:
{goal}
"""
