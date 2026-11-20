from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, FunctionTool

#Declare prokect endpoint and agent name and deploument name
PROJECT_ENDPOINT="https://foundaryai103.services.ai.azure.com/api/projects/AI-103"
AGENT_NAME="IT-HelpDesk-Agent-Customtools"
DEPLOYMENT_NAME = "gpt-5-mini"

client=AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

# function tool i.e. tool functions which are defined by us are custom
#note we are not returing anything yet as we did in open _ai custom functions
#where we returned string, we will do it next

#declaring tools array with custom functions with parameters and stricts 
tools = [
    FunctionTool(
        name="get_password_reset_steps",
        description="Get the company password reset steps.",
        parameters={
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        strict=True,
    ),
    FunctionTool(
        name="get_vpn_troubleshooting_steps",
        description="Get troubleshooting steps for VPN connection issues.",
        parameters={
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        strict=True,
    ),
    FunctionTool(
        name="get_software_install_guide",
        description="Get installation instructions for a supported software package.",
        parameters={
            "type": "object",
            "properties": {
                "software_name": {
                    "type": "string",
                    "description": "The software name, for example Slack, Zoom, or VS Code."
                }
            },
            "required": ["software_name"],
            "additionalProperties": False,
        },
        strict=True,

    ),
]


#pass the tools we declared above in here.
agent=client.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=DEPLOYMENT_NAME,
        instructions=(
            "You are an IT support assistant for a company. "
            "Help users with password resets, VPN issues, and software installation. "
            "Give clear, step-by-step answers. "
            "If the question is outside IT support topics, politely say so."
        ),
        tools=tools
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")