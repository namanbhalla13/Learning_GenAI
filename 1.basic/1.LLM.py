from langchain_openai import OpenAI #it inherit BaseOpenAI
from dotenv import load_dotenv

load_dotenv()

llm= OpenAI(model='gpt-4o')

result= llm.invoke("whta is teh capital of the india?")

print(result)