from backend.services.vector_store import collection

print("Before:", collection.count())

all_docs = collection.get()

if all_docs["ids"]:
    collection.delete(ids=all_docs["ids"])

print("After:", collection.count())