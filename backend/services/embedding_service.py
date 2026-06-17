from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text):

    embedding = model.encode(text)

    return embedding.tolist()


if __name__ == "__main__":

    sample_text = """
    Python FastAPI Docker AWS
    """

    vector = generate_embedding(sample_text)

    print("Vector Length:", len(vector))
    print("First 10 Values:")
    print(vector[:10])