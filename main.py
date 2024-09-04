from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

# token_provider = get_bearer_token_provider(
#     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
# )

client = AzureOpenAI(
    api_version="2024-02-15-preview",
    azure_endpoint="https://xxxx.openai.azure.com/",
    api_key="xxxx",
    # azure_ad_token_provider=token_provider
)

response = client.chat.completions.create(
    model="gpt-4o", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response.choices[0].message.content)