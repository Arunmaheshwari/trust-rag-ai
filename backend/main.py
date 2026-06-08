from fastapi import FastAPI
from api.routes.ingestion import router as ingestion_router
from api.routes.query import router as query_router
from api.routes.chat import router as chat_router

app = FastAPI()

app.include_router(ingestion_router, prefix="/api")
app.include_router(query_router)
app.include_router(chat_router)