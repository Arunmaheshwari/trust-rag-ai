from pathlib import Path
from typing import List

from langchain_community.vectorstores import FAISS

from retrieval.embeddings import EmbeddingService


class VectorStoreManager:

    def __init__(self, index_path: str = "vectorstore/faiss_index"):
        self.index_path = Path(index_path)
        self.embedding_service = EmbeddingService()
        self.vectorstore = None

    # -------------------------
    # CREATE NEW INDEX
    # -------------------------
    def create_index(self, texts: List[str]):
        """
        Create FAISS index from documents
        """
        self.vectorstore = FAISS.from_texts(
            texts=texts,
            embedding=self.embedding_service.embeddings,
        )

        self.save()

        return self.vectorstore

    # -------------------------
    # LOAD EXISTING INDEX
    # -------------------------
    def load(self):
        """
        Load FAISS index from disk
        """
        if not self.index_path.exists():
            raise FileNotFoundError("FAISS index not found. Create it first.")

        self.vectorstore = FAISS.load_local(
            str(self.index_path),
            self.embedding_service.embeddings,
            allow_dangerous_deserialization=True,
        )

        return self.vectorstore

    # -------------------------
    # ADD NEW DOCUMENTS
    # -------------------------
    def add_documents(self, texts: List[str]):
        """
        Add new documents to existing index
        """
        if self.vectorstore is None:
            self.load()

        self.vectorstore.add_texts(texts)
        self.save()

    # -------------------------
    # SEARCH SIMILAR CHUNKS
    # -------------------------
    def similarity_search(self, query: str, k: int = 4):
        """
        Retrieve top-k similar chunks
        """
        if self.vectorstore is None:
            self.load()

        return self.vectorstore.similarity_search(query, k=k)

    # -------------------------
    # SAVE INDEX
    # -------------------------
    def save(self):
        """
        Persist FAISS index locally
        """
        self.index_path.parent.mkdir(parents=True, exist_ok=True)

        self.vectorstore.save_local(str(self.index_path))