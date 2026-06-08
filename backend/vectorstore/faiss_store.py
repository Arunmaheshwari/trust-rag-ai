import faiss
import numpy as np
import pickle
import os


class FaissStore:

    def __init__(
        self,
        dimension=1024
    ):

        self.dimension = dimension

        self.index_path = (
            "vectorstore/faiss_index/index.faiss"
        )

        self.metadata_path = (
            "vectorstore/faiss_index/metadata.pkl"
        )

        self.documents = []

        self._load_or_create()

    def _load_or_create(self):

        if os.path.exists(self.index_path):

            self.index = faiss.read_index(
                self.index_path
            )

            print(
                f"Loaded FAISS index with "
                f"{self.index.ntotal} vectors"
            )

        else:

            self.index = faiss.IndexFlatL2(
                self.dimension
            )

            print(
                "Created new FAISS index"
            )

        if os.path.exists(
            self.metadata_path
        ):

            with open(
                self.metadata_path,
                "rb"
            ) as f:

                self.documents = pickle.load(
                    f
                )

        else:

            self.documents = []

    def save(self):

        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(
            self.metadata_path,
            "wb"
        ) as f:

            pickle.dump(
                self.documents,
                f
            )

    def add_vector(
        self,
        embedding,
        text,
    ):

        vector = np.array(
            [embedding],
            dtype="float32"
        )

        self.index.add(
            vector
        )

        self.documents.append(
            text
        )

    def search(
        self,
        query_embedding,
        k=5
    ):

        if self.index.ntotal == 0:
            return []

        query_vector = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = (
            self.index.search(
                query_vector,
                k
            )
        )

        results = []

        for idx in indices[0]:

            if (
                idx >= 0
                and idx < len(
                    self.documents
                )
            ):

                results.append(
                    self.documents[idx]
                )

        return results