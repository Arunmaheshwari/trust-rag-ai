from ingestion.loaders.pdf_loader import PDFLoader
from ingestion.loaders.txt_loader import TXTLoader
from ingestion.loaders.web_loader import WebLoader

from ingestion.chunker import DocumentChunker
from retrieval.embeddings import EmbeddingService

from vectorstore.faiss_store import FaissStore

from database.connection import get_db
from database.models.document import Document


class IngestionService:
    """
    Loader -> Chunker -> Embedding -> Vector Store -> PostgreSQL
    """

    def __init__(self):
        self.embedder = EmbeddingService()
        self.vectorstore = FaissStore()
        self.chunker = DocumentChunker()

    def get_loader(self, source_type: str):

        loaders = {
            "pdf": PDFLoader,
            "txt": TXTLoader,
            "web": WebLoader,
        }

        if source_type not in loaders:
            raise ValueError(
                f"Unsupported source type: {source_type}"
            )

        return loaders[source_type]()

    def ingest(
        self,
        source: str,
        source_type: str,
    ):

        # -------------------------
        # Load Documents
        # -------------------------

        loader = self.get_loader(source_type)

        documents = loader.load(source)

        # documents format:
        #
        # [
        #   {
        #       "content": "...",
        #       "metadata": {...}
        #   }
        # ]

        all_chunks = []

        # -------------------------
        # Chunk Documents
        # -------------------------

        for document in documents:

            chunks = self.chunker.chunk_text(
                document["content"]
            )

            for chunk in chunks:

                all_chunks.append(
                    {
                        "content": chunk,
                        "metadata": document["metadata"],
                    }
                )

        # -------------------------
        # Database Session
        # -------------------------

        db = next(get_db())

        try:

            # -------------------------
            # Process Chunks
            # -------------------------

            for chunk_doc in all_chunks:

                chunk_text = chunk_doc["content"]

                metadata = chunk_doc["metadata"]

                # Generate Embedding
                embedding = self.embedder.embed_query(
                    chunk_text
                )

                # Store in Vector Store
                self.vectorstore.add_vector(
                    embedding,
                    chunk_text,
                )

                # Store Metadata in PostgreSQL
                db_document = Document(
                    title=metadata.get(
                        "file_name",
                        source,
                    ),
                    content=chunk_text,
                    source_url=(
                        source
                        if source_type == "web"
                        else None
                    ),
                )

                db.add(db_document)

            db.commit()

            return {
                "message": "Ingestion successful",
                "chunks_created": len(all_chunks),
            }

        except Exception:

            db.rollback()
            raise

        finally:

            db.close()