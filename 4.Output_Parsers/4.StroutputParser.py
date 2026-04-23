from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model= ChatOpenAI(model='gpt-4o')

template_1= PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

template_2= PromptTemplate(
    template="Write a 5 line summary of given text \n {text}",
    input_variables=['text']
)

parser= StrOutputParser()

chain= template_1 | model | parser | template_2 | model | parser

result= chain.invoke({'topic':'black hole'})

print(result)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="""
Give me 3 facts about {topic}.

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

prompt = template.format(topic="India")

result = model.invoke(prompt)

output = parser.parse(result.content)

print(output)
