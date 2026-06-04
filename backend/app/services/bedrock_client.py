import boto3

from app.config.settings import settings


class BedrockClient:
    def __init__(self):
        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

    def invoke(self, prompt: str) -> str:
        response = self.client.converse(
            modelId=settings.BEDROCK_MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            inferenceConfig={
                "maxTokens": 1024,
                "temperature": 0.2,
            },
        )

        return response["output"]["message"]["content"][0]["text"]


bedrock_client = BedrockClient()