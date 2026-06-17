from embedding_service import generate_embedding
from vector_store import (
    add_document,
    search_documents
)

sample_text = """
Python FastAPI Docker AWS
"""

embedding = generate_embedding(sample_text)

add_document(
    "doc1",
    sample_text,
    embedding
)

query_embedding = generate_embedding(
    "Looking for Python backend developer"
)

results = search_documents(query_embedding)

print(results)