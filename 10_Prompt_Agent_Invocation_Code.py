from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

PROJECT_ENDPOINT="https://foundaryai103.services.ai.azure.com/api/projects/AI-103"
AGENT_NAME="IT-HelpDesk-Agent"

#authenticate to MFT foundary using AIPROJECT client libraray and
#azure.identity library.
client=AIProjectClient(
    endpoint = PROJECT_ENDPOINT,
    credential= DefaultAzureCredential()
)

#intantitate open Ai client and use open ai respone API to invoke
#To invoke prompt agent from code
openai = client.get_openai_client()

response = openai.responses.create(
    extra_body={"agent_reference":{"name":AGENT_NAME,"type":"agent_reference"}},
    input="How do I reset my company password?"
)

print(response.output_text)