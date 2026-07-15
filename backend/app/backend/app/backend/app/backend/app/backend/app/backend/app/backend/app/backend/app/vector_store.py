import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.dimension = 768

        self.index = faiss.IndexFlatL2(self.dimension)

    def add(self, embeddings):

        vectors = np.asarray(
            embeddings,
            dtype="float32"
        )

        self.index.add(vectors)

    def search(self, embedding, k=5):

        vector = np.asarray(
            [embedding],
            dtype="float32"
        )

        distances, indices = self.index.search(
            vector,
            k
        )

        return distances, indices


vector_store = VectorStore()
