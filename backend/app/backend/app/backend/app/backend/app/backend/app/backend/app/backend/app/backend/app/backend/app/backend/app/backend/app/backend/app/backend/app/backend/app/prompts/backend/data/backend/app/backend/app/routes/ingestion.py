from fastapi import APIRouter

from app.ingest import ingestion_service

router = APIRouter(prefix="/ingestion", tags=["Ingestion"])


@router.post("/documents")
async def ingest_documents():

    return ingestion_service.ingest(
        "backend/data"
    )
