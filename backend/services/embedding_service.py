import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_embedding(text):

    response = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text,
        task_type="retrieval_document"
    )

    return response["embedding"]


if __name__ == "__main__":

    vector = generate_embedding(
        "Python FastAPI Docker AWS"
    )

    print("Vector Length:", len(vector))
    print(vector[:10])