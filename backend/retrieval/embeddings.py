from langchain_aws import BedrockEmbeddings

from app.config.settings import settings


class EmbeddingService:
    def __init__(self):
        self.embeddings = BedrockEmbeddings(
            region_name=settings.AWS_REGION,
            model_id=settings.BEDROCK_EMBEDDING_MODEL_ID,
        )

    def embed_documents(self, texts: list[str]):
        return self.embeddings.embed_documents(texts)

    def embed_query(self, query: str):
        return self.embeddings.embed_query(query)