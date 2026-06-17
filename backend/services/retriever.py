from backend.services.embedding_service import generate_embedding
from backend.services.vector_store import search_documents


def retrieve_context(query, top_k=3):

    query_embedding = generate_embedding(query)

    results = search_documents(
        query_embedding,
        top_k
    )

    return results["documents"][0]