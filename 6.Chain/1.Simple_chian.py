from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


prompt= PromptTemplate(
    template="Generate 5 interesting facts about{topic}",
    input_variables=['topic']
)


model= ChatOpenAI(model='gpt-4o')


praser= StrOutputParser()


chain= prompt | model | praser


result= chain.invoke({'topic':'cricket'})


chain.get_graph().print_ascii()


print(result)