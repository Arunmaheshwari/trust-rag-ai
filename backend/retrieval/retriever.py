from retrieval.embeddings import EmbeddingService
from vectorstore.singleton import faiss_store

class RetrievalService:

    def __init__(self):

        self.embedder = EmbeddingService()

        self.vectorstore = faiss_store

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        query_embedding = (
            self.embedder.embed_query(query)
        )

        results = self.vectorstore.search(
            query_embedding,
            k=top_k
        )

        return results