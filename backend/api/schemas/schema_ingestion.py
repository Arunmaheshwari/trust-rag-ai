from pydantic import BaseModel


class IngestionRequest(BaseModel):
    source: str
    source_type: str