from retrieval.vector_store import VectorStoreManager

vs = VectorStoreManager()

vs.create_index([
    "RAG stands for Retrieval Augmented Generation",
    "FAISS is a vector database for similarity search"
])

print(vs.similarity_search("What is RAG?", k=1))