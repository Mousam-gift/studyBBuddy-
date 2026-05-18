import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("Gemini_API_KEY"))

SYSTEM_PROMPT = """
you are an AI assistant that works in 3 areas:
1. Education
2. Health information (no digonosis)
3. Sustainability

Always mention which domain you are using.
keep responses concise.
"""
def smart_agent(message, history):
    contents = []
    contents.append({
        "role": "user",
        "parts": [
            {
                "text": SYSTEM_PROMPT
            }
        ]
    })
    for msg in history:
        role = msg["role"]
        if role == "assistant":
            role = "model"
        contents.append({
            "role": role,
            "parts": [{"text": msg["content"]}]
        })
    contents.append({
        "role": "user",
        "parts": [
            {
                "text": message
            }
        ]
    })
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents
    )
    return response.text