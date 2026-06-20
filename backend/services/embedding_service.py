from sentence_transformers import SentenceTransformer

print("EMBEDDING FILE IMPORT STARTED")

print("LOADING MODEL")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("MODEL LOADED")


def generate_embedding(text):

    embedding = model.encode(text)

    return embedding.tolist()