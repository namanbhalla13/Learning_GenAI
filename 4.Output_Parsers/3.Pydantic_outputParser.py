from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

class FactsSchema(BaseModel):
    fact_1: str = Field(description="Fact 1 about the topic")
    fact_2: str = Field(description="Fact 2 about the topic")
    fact_3: str = Field(description="Fact 3 about the topic")

parser = JsonOutputParser(pydantic_object=FactsSchema)

prompt = PromptTemplate(
    template="""
Give me 3 facts about {topic}.

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

result = chain.invoke({"topic": "India"})

print(result)
