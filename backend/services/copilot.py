from backend.services.retriever import retrieve_context
from backend.services.llm_service import generate_response


def ask_copilot(question):

    context_chunks = retrieve_context(question)

    context = "\n\n".join(context_chunks)

    answer = generate_response(
        question,
        context
    )

    return answer