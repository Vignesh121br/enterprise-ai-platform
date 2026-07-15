import numpy as np


class EmbeddingService:

    def encode(self, text: str):

        np.random.seed(abs(hash(text)) % (2**32))

        return np.random.rand(768).tolist()


embedding_service = EmbeddingService()
