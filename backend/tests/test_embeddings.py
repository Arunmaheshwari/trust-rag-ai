from retrieval.embeddings import EmbeddingService


embedding_service = EmbeddingService()

result = embedding_service.embed_query(
    "What is Retrieval Augmented Generation?"
)

print(len(result))