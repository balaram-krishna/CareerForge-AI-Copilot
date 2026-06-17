import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(
    api_key=GEMINI_API_KEY
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_response(question, context):

    prompt = f"""
You are CareerForge AI Copilot.

Use the provided context to answer the user's question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text