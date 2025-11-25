from .embeddings import generate_embedding, embeddings_store

def index_memory(memory_id: int, text: str):
    emb = generate_embedding(text)
    embeddings_store[memory_id] = emb