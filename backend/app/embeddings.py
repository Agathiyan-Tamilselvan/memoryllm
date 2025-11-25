from sentence_transformers import SentenceTransformer
import numpy as np
import os

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings_store = {}  # In-memory for simplicity; use a vector DB like FAISS in production

def generate_embedding(text: str) -> np.ndarray:
    return model.encode(text)

def search_similar(query: str, top_k: int = 5) -> list:
    query_emb = generate_embedding(query)
    similarities = {}
    for mem_id, emb in embeddings_store.items():
        sim = np.dot(query_emb, emb) / (np.linalg.norm(query_emb) * np.linalg.norm(emb))
        similarities[mem_id] = sim
    sorted_ids = sorted(similarities, key=similarities.get, reverse=True)[:top_k]
    return sorted_ids