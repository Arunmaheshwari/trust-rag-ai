from retrieval.embeddings import EmbeddingService
from vectorstore.faiss_store import FaissStore


class RetrievalService:

    def __init__(self):

        self.embedder = EmbeddingService()

        self.vectorstore = FaissStore()

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