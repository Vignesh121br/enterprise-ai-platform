from app.embeddings import embedding_service
from app.vector_store import vector_store


class Retriever:

    def search(
        self,
        query,
        k=5
    ):

        embedding = embedding_service.encode(query)

        distances, indices = vector_store.search(
            embedding,
            k
        )

        return {
            "distances": distances.tolist(),
            "indices": indices.tolist()
        }


retriever = Retriever()
