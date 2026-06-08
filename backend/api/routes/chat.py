from fastapi import APIRouter

from api.schemas.schema_chat import ChatRequest

from retrieval.retriever import RetrievalService
from llm.bedrock_service import BedrockLLMService


router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)


@router.post("/chat")
def chat(
    payload: ChatRequest
):

    retriever = RetrievalService()

    llm = BedrockLLMService()

    chunks = retriever.retrieve(
        payload.query,
        payload.top_k
    )

    context = "\n\n".join(
        chunks["retrieved_chunks"]
    )

    answer = llm.generate_answer(
        question=payload.query,
        context=context
    )

    return {
        "question": payload.query,
        "answer": answer,
        "sources_found": len(
            chunks["retrieved_chunks"]
        )
    }