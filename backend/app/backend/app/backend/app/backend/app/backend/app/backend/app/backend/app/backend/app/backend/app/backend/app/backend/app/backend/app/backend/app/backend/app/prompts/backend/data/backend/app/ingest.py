from app.indexer import indexer


class IngestionService:

    def ingest(self, directory: str):

        result = indexer.build(directory)

        return {
            "status": "completed",
            "documents": result["documents"],
            "chunks": result["chunks"]
        }


ingestion_service = IngestionService()
