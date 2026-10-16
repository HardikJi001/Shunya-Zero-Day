import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

model= OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

response = model.chat.completions.create(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    stream= "true",
  messages=[
          {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

# print(response.choices[0].message)
print(response)