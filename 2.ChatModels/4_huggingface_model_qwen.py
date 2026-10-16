import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
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