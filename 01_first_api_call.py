from openai import OpenAI

endpoint = "https://foundaryai103.services.ai.azure.com/openai/v1" #this is our msft foundary project endpoint
deployment_name = "gpt-5-mini"
# Authorize this program to use our model deployed in Msft Foundary 
api_key = "3K1WrJwDuWivtrmQqWIKgHTspeY4IyfIB4LPHQ6Ztj6izSn6qJeEJQQJ99CKACHYHv6XJ3w3AAAAACOGES3I"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input="Tell me about waseem uddin who works for Anonymousand is a team lead linkedin",
)

print(f"answer: {response.output_text}")
