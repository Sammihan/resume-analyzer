from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(skills):
    embeddings = model.encode(skills)
    return embeddings
