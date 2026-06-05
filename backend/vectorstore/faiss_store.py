import faiss
import numpy as np


class FaissStore:

    def __init__(self, dimension=1024):
        self.index = faiss.IndexFlatL2(dimension)

        self.documents = []

    def add_vector(
        self,
        embedding,
        text,
    ):
        vector = np.array(
            [embedding],
            dtype="float32"
        )

        self.index.add(vector)

        self.documents.append(text)

    def search(
        self,
        query_embedding,
        k=5,
    ):
        query_vector = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_vector,
            k
        )

        results = []

        for idx in indices[0]:

            if idx < len(self.documents):

                results.append(
                    self.documents[idx]
                )

        return results