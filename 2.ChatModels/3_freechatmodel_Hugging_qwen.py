import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="Qwen/Qwen3-0.6B:featherless-ai",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of India?"
        }
    ],
)

print(completion.choices[0].message)