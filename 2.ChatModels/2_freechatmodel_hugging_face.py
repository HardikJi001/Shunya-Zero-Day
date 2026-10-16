from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-8B", 
    task="text-generation"
    
)

model = ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of India")

print(result.content)

# NOTE THAT at times these models no longer work as they may be not supported by the Hugging face servers. That's why use the method from 3rd and 4th file


# import inspect
# from langchain_huggingface import ChatHuggingFace

# print(inspect.signature(ChatHuggingFace))


# from dotenv import load_dotenv
# import os

# load_dotenv()

# print(os.getenv("HF_TOKEN"))

# from dotenv import find_dotenv

# print(find_dotenv())