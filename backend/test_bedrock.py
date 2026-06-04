from app.services.bedrock_client import bedrock_client


response = bedrock_client.invoke(
    "Explain what Retrieval Augmented Generation is in 3 lines."
)

print(response)