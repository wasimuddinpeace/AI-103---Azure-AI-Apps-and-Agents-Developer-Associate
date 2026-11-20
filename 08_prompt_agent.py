from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition 

# Building Prompt agent leveraging foundary ecosystem
PROJECT_ENDPOINT = "https://foundaryai103.services.ai.azure.com/api/projects/AI-103"
AGENT_NAME = "IT-HelpDesk-Agent"
DEPLOYMENT_NAME = "gpt-5-mini"

#Establish a client connection on MSFT foundary project
# we need some way to authenticate against our azure account
#in foundary since you are logged in you can create a prompt agent with that
#but in code we will use Azure CLI to connect AZUre
client = AIProjectClient (
    endpoint = PROJECT_ENDPOINT,
    credential = DefaultAzureCredential()
)

# Define and create a prompt agent

agent = client.agents.create_version(
    agent_name = AGENT_NAME,
    definition = PromptAgentDefinition(
        model =DEPLOYMENT_NAME,
        instructions=(
            "You are an IT support assistant for a company. "
            "Help users with password resets, VPN issues, and software installation. "
            "Give clear, step-by-step answers. "
            "If the question is outside IT support topics, politely say so."
        )
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")

