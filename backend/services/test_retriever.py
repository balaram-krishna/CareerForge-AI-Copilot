from retriever import retrieve_context

query = """
What cloud technologies does this candidate know?
"""

results = retrieve_context(query)

print("\nRetrieved Chunks:\n")

for chunk in results:
    print("-" * 50)
    print(chunk[:300])