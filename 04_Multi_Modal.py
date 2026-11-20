from openai import OpenAI
import base64

endpoint = "https://foundaryai103.services.ai.azure.com/openai/v1" #this is our msft foundary project endpoint
deployment_name = "gpt-5-mini"
# Authorize this program to use our model deployed in Msft Foundary 
api_key = "3K1WrJwDuWivtrmQqWIKgHTspeY4IyfIB4LPHQ6Ztj6izSn6qJeEJQQJ99CKACHYHv6XJ3w3AAAAACOGES3I"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

image_path="types of agents.png"
with open(image_path,"rb") as image_file:
    image_data= base64.b64encode(image_file.read()).decode("utf-8")

response = client.responses.create(
    model=deployment_name,
    #sysytem prompt
    instructions="you are a helpful assistant that reads and extract information from images",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    # Provide inline data URL containing the base64 image
                    "image_url": f"data:image/png;base64,{image_data}"
                },
                {
                    "type": "input_text",
                    "text": "Extract all the text from this image and present it in a structured JSON with fields: 'lines' (array of text lines) and 'summary' (short summary)."
                }
            ]
        }
    ]
)

# Print text output (there may also be structured output fields depending on model response)
print("Raw response object:")
print(response)
print(f"answer: {response.output_text}")