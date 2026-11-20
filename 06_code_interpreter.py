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
    instructions="You are a data analyst. Use Python to calculate precisely.",
    input="What is the compound interest on \$10,000 at 5 percent annual rate over 10 years?",
    tools=[{"type": "code_interpreter", "container": {"type": "auto"}}],
    # optional: tool_choice="auto"  
)

# Inspect response items for code_interpreter calls and messages
for item in response.output:          # response.output is typically a list of items
    # item.type may be "code_interpreter_call" when model produced code to run
    if getattr(item, "type", "") == "code_interpreter_call":
        print("=== Python code the model wrote ===")
        # some SDKs expose the code as item.code or item.prompt; try common fields:
        code = getattr(item, "code", None) or getattr(item, "program", None) or item
        print(code)
        print("\n--- Output from execution ---")
        # execution outputs often appear in item.outputs or item.execution_result
        print(getattr(item, "outputs", getattr(item, "execution_result", None)))
    elif getattr(item, "type", "") == "message":
        print("\n=== Final Answer ===")
        # common convenience property:
        try:
            print(response.output_text)
        except Exception:
            # fallback: print the message content directly
            content = getattr(item, "content", None)
            print(content)

print(f"answer: {response.output_text}")