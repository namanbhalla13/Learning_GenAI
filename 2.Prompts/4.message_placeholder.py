from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o')

chat_history = []

# Load and convert messages
with open('chat_history.txt') as f:
    for line in f:
        line = line.strip()
        
        if line.startswith("SystemMessage:"):
            content = line.replace("SystemMessage:", "").strip()
            chat_history.append(SystemMessage(content=content))
        
        elif line.startswith("HumanMessage:"):
            content = line.replace("HumanMessage:", "").strip()
            chat_history.append(HumanMessage(content=content))
        
        elif line.startswith("AIMessage:"):
            content = line.replace("AIMessage:", "").strip()
            chat_history.append(AIMessage(content=content))

# Chat template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support assistant for an e-commerce website."),
    MessagesPlaceholder(variable_name='chat_history'),
    ("human", "{query}")
])

prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'What is my refund status?'
})

response = model.invoke(prompt)

print(response.content)
