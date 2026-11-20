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
    instructions="""you are a helpful research assistant. Always cite your sources.""",
    #user prompt
    input="What are the latest developments in AI regulation in the europian union?",
    #the model has access to a tool from open ai called web search
    #model will decide wether  to use tool or not
    #if it decided to use the tool, the web earch tool will go to the internet and return the results to the model
    tools=[{"type": "web_search"}],
    tool_choice="auto"
)

print(f"answer: {response.output_text}")