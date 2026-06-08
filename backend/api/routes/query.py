from fastapi import APIRouter

from api.schemas.schema_query import QueryRequest

from retrieval.retriever import RetrievalService

router = APIRouter(
    prefix="/api",
    tags=["Query"]
)


@router.post("/query")
def query_documents(
    payload: QueryRequest
):

    service = RetrievalService()

    results = service.retrieve(
        payload.query,
        payload.top_k
    )

    return {
        "query": payload.query,
        "retrieved_chunks": results
    }