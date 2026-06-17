from resume_parser import extract_text_from_pdf
from chunker import chunk_text
from embedding_service import generate_embedding
from vector_store import add_document


def ingest_resume(pdf_path):

    text = extract_text_from_pdf(pdf_path)

    chunks = chunk_text(text)

    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        add_document(
            f"resume_chunk_{index}",
            chunk,
            embedding
        )

    return len(chunks) 