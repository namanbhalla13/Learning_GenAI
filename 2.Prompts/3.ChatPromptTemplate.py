from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model= ChatOpenAI(model='gpt-4o')

chat_template= ChatPromptTemplate(
    [
        ('system',"You are a helpful {domain} expert"),
        ('human',"Explain in the simple terms, what is {topic}")
        #SystemMessage(content="You are a helpful {domain} expert"),
        #HumanMessage(content="Explain in the simple terms, what is {topic}")
    ]
)

prompt= chat_template.invoke({'domain':'computer','topic':'c-type'})

result= model.invoke(prompt)

print(prompt)
print(result.content)
