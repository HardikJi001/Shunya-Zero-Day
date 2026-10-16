from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id='-------',
    task='text-generation',
    pipeline_kwargs=dict(
        temperatue=0.5,
        max_new_tokens=100
    )
)

model= ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result)

# DONT RUN THIS FILE AS IF YOU RUN IT DOWNLOAD THE MODEL WHICH IS IN GB AND THEN RUN THAT MODEL