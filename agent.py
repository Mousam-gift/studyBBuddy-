import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

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
def smart_agent(message: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            genai.types.Content(role="user", parts=[genai.types.Part(text=SYSTEM_PROMPT + "\n\n" + message)])
        ],
    )
    return response.text