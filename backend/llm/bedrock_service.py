from langchain_aws import ChatBedrock

from app.config.settings import settings


class BedrockLLMService:

    def __init__(self):

        self.llm = ChatBedrock(
            region_name=settings.AWS_REGION,
            model_id=settings.BEDROCK_MODEL_ID,
        )

    def generate_answer(
        self,
        question: str,
        context: str,
    ):

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

"I could not find this information in the knowledge base."

Context:
{context}

Question:
{question}
"""

        response = self.llm.invoke(
            prompt
        )

        return response.content