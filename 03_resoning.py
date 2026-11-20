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
    #sysytem prompt
    instructions="""A ditributed e-commerce application is experiencing intermittent failures during peak hours, the failures
    appears random, .""",
    max_output_tokens=100,
    temperature = 2,
    input="What are the best practives fopr securing an azure storage account?",
    reasoning={ "effort": "high"}
)
print(f"answer: {response.output_text}")