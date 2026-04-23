from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model= ChatOpenAI(model='gpt-4o')

parser= JsonOutputParser()

template= PromptTemplate(
    template="Give me the name, age and city of the fiction person {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

"""
Approach-1 without chain
prompt= template.format()
result= model.invoke(prompt)
final_result= parser.parse(result.content)
print(result.content)
print("=========================")
print(final_result)
"""
#with chain

chain= template | model | parser

print(chain.invoke({}))
