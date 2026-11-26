#create Prompt Agent
#This  file is to spin up agent infoundary using AIProjectCLient and PromptAgentDefinition libraraies

from azure.identity import AzureCliCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

PROJECT_ENDPOINT = "https://foundaryai103.services.ai.azure.com/api/projects/AI-103"

SYSTEM_PROMPT = """
You are a customer support assistant for WhiteGoldUS Technology Services.

Answer the customer's question using ONLY the provided sources.

After your answer, cite the source URL you used.

If the sources do not contain the answer, say:
"I don't have that information in the available knowledge base."

Then suggest contacting support@WhiteGoldUS.com.

Never invent policies, prices, refund rules, or timelines.
"""

#create project client for authenticating to the foundary and the project using our own credentials

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=AzureCliCredential()
)


#On that client we will create an agetns with create_version api and PromptAgentDefitnion
agent = project.agents.create_version(
    agent_name="WhiteGoldUS-support-rag-agent",
    definition=PromptAgentDefinition(
        model="gpt-5-mini",
        instructions=SYSTEM_PROMPT,
    ),
)