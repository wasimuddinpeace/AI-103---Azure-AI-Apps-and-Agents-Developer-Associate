from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition,WebSearchTool

# AIProjectClient is needed for prompt agent 
# also it needs Project endpoint from foundry and credential to login to MSFT foundry
#AgentName and Deployment name
PROJECT_ENDPOINT="https://foundaryai103.services.ai.azure.com/api/projects/AI-103"
AGENT_NAME="web-search-lab-agent"
DEPLOYMENT_NAME="gpt-5-mini"


client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

#client.agents.create_version agent_name, promptAgentDefinition, instructions and tools
agent = client.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=DEPLOYMENT_NAME,
        instructions=
            "You are a helpful assistant. Use web search to answer questions that require current information."
        ,tools=[WebSearchTool()]
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")