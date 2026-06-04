import faiss
import numpy as np


class FaissStore:

    def __init__(
        self,
        dimension=1024
    ):
        self.index = faiss.IndexFlatL2(
            dimension
        )

    def add_vectors(
        self,
        vectors
    ):
        vectors = np.array(
            vectors,
            dtype="float32"
        )

        self.index.add(vectors)

    def search(
        self,
        query_vector,
        k=5
    ):
        query_vector = np.array(
            [query_vector],
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_vector,
            k
        )

        return indices[0]