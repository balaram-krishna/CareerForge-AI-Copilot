from rag_pipeline import ingest_resume

chunks = ingest_resume(
    "data/resume (1).pdf"
)

print(
    f"Stored {chunks} chunks in ChromaDB"
)