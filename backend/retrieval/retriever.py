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

        if not query.strip():
            raise ValueError(
                "Query cannot be empty"
            )

        query_embedding = (
            self.embedder.embed_query(
                query
            )
        )

        results = self.vectorstore.search(
            query_embedding=query_embedding,
            k=top_k
        )

        return {
            "query": query,
            "retrieved_chunks": results,
            "retrieved_count": len(results)
        }