from pathlib import Path

from langchain_community.vectorstores import FAISS

from retrieval.embeddings import EmbeddingService


class VectorStoreManager:
    INDEX_PATH = "vectorstore/faiss_index"

    def __init__(self):
        self.embedding_service = EmbeddingService()

    def create_index(self, chunks: list[str]):
        vectorstore = FAISS.from_texts(
            texts=chunks,
            embedding=self.embedding_service.embeddings,
        )

        Path(self.INDEX_PATH).mkdir(
            parents=True,
            exist_ok=True,
        )

        vectorstore.save_local(self.INDEX_PATH)

        return vectorstore

    def load_index(self):
        return FAISS.load_local(
            self.INDEX_PATH,
            self.embedding_service.embeddings,
            allow_dangerous_deserialization=True,
        )