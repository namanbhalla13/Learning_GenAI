from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()


prompt1 = PromptTemplate(
    template="Write a detailed report on the below mentioned topic:\n{topic}",
    input_variables=['topic']
)


prompt2= PromptTemplate(
    template="Write a 5 ver import point from the below detailed report \n {report}",
    input_variables=['report']
)


model= ChatOpenAI(model='gpt-4o')


parser= StrOutputParser()


chain= prompt1 | model | parser | prompt2 | model | parser


result= chain.invoke({'topic':'CBI'})


chain.get_graph().print_ascii()
print(result)
