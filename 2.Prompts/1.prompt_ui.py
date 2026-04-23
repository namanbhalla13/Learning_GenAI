from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model= ChatOpenAI(model='gpt-4o')

template= PromptTemplate(
    template="""Write an essay on the topic: "{topic}".

The essay should:
- Be exactly {num_lines} lines long
- Be written in {language}
- Be clear, well-structured, and easy to understand

Start directly with the essay.
""",
input_variables=["topic","num_lines","language"])

topic= input("enter the topic")
num_lines= input("enter the number of lines you wnat to wants eassy")
language= input("in whihc langaugs e you want yor repsosne")

prompt= template.invoke(
    {
        'topic': topic,
        'num_lines': num_lines,
        'language': language
    }
)

result= model.invoke(prompt)

print(result)
