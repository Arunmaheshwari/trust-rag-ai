from fastapi import FastAPI
from api.routes.ingestion import router as ingestion_router

app = FastAPI()

app.include_router(ingestion_router, prefix="/api")