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
    instructions="""you are a senior Azure cloud architect assistant.
    you only aswers questions related to azure cloud services and architecture.
    Always structure your responses with clear headings
    use concise technical langauge suitablebfor an experienced developer audience
    if the question is outside the azure domain politely decline to answer.""",
    max_output_tokens=100,
    temperature = 2,
    input="What are the best practives fopr securing an azure storage account?",
)
print(f"answer: {response.output_text}")