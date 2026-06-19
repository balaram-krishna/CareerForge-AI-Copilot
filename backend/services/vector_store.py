import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="resumes"
)


def add_document(doc_id, document, embedding):

    collection.add(
        ids=[doc_id],
        documents=[document],
        embeddings=[embedding]
    )


def search_documents(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


def clear_collection():

    try:
        all_docs = collection.get()

        if all_docs["ids"]:
            collection.delete(
                ids=all_docs["ids"]
            )

    except Exception as e:
        print("Clear Error:", e)