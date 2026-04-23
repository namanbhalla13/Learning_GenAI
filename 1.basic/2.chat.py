from langchain_openai import ChatOpenAI  #it inherit BaseChatModel
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model='gpt-4o', temperature=0.4, max_completion_tokens=100)

result= model.invoke("what is the capital of india?")

print(result.content)
