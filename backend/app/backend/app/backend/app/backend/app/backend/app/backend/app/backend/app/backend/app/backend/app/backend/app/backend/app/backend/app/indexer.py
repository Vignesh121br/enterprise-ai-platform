from app.document_loader import document_loader
from app.text_splitter import text_splitter
from app.embeddings import embedding_service
from app.vector_store import vector_store


class DocumentIndexer:

    def build(self, directory):

        documents = document_loader.load(directory)

        total = 0

        for doc in documents:

            chunks = text_splitter.split(
                doc["content"]
            )

            embeddings = []

            for chunk in chunks:

                embeddings.append(
                    embedding_service.encode(chunk)
                )

            vector_store.add(embeddings)

            total += len(chunks)

        return {
            "documents": len(documents),
            "chunks": total
        }


indexer = DocumentIndexer()
