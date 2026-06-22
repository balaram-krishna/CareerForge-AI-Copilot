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

You are helping users understand and analyze their resumes.

Rules:
1. Use ONLY the provided resume context.
2. If the answer exists in the context, answer directly.
3. Do NOT make up information.
4. If the information is not available, respond:
   "Information not found in the uploaded resume."
5. Be concise and professional.

Resume Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text