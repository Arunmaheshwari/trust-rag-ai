from fastapi import APIRouter
from ingestion.ingestion_service import IngestionService
from api.schemas.schema_ingestion import IngestionRequest

router = APIRouter()
service = IngestionService()


@router.post("/ingest")
def ingest_document(payload: IngestionRequest):

    service = IngestionService()

    result = service.ingest(
        source=payload.source,
        source_type=payload.source_type,
    )

    return {
        "status": "success",
        "message": result,
    }