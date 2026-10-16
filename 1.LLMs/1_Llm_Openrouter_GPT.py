import os 
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm= OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ['OPENROUTER_API_KEY'],
)

response = llm.chat.completions.create(
  model="openai/gpt-oss-120b",
  messages=[
          {
            "role": "user",
            "content": "What is the capital of India?"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

print(response)