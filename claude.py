import json 
import boto3

prompt = """
Act like Shakespeare and compose a poem about Generative AI.
"""
bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "prompt": "Human:\n\n" + prompt + "\n\nAssistant:",
    "max_tokens_to_sample": 512, 
    "temperature": 0.8,
    "top_p": 0.8
}

body = json.dumps(payload)
model_id = "anthropic.claude-v2" 

response = bedrock.invoke_model(
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
    body=body
)


response_body = json.loads(response.get("body").read())
response_text = response_body.get("completion")
print(response_text)