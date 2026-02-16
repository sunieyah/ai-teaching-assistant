def explanation_prompt(topic):
    return f"""
You are a computer science teaching assistant.
Explain the topic "{topic}" clearly for undergraduate students.
Include:
- Definition
- Key points
- Simple example
"""

def mcq_prompt(topic):
    return f"""
Generate 5 multiple-choice questions on "{topic}".
Each question should have 4 options and clearly indicate the correct answer.
"""

def short_questions_prompt(topic):
    return f"""
Generate 5 short-answer exam questions on "{topic}" for CS students.
"""
