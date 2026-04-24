from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel


load_dotenv()


model1= ChatOpenAI(model='gpt-4o')
model2= ChatOpenAI(model='gpt-3.5-turbo')


prompt1= PromptTemplate(
    template="Write a detailed notes about the {topic}",
    input_variables=['topic']
)


prompt2= PromptTemplate(
    template="Make 5 qyestion MCQ quiz on the follwing topic \n {topic}",
    input_variables=['topic']
)


prompr3= PromptTemplate(
    template="Merge the notes and quiz into the isngle documents \n notes->{notes} \n quiz->{quiz}",
    input_variables=['notes','quiz']
)


parser= StrOutputParser()


parallel_chain= RunnableParallel({
    'notes': prompt1 |model2 | parser,
    'quiz': prompt2 |model1 | parser}
)


merge_chain= prompr3 | model1 | parser


chain= parallel_chain | merge_chain


result= chain.invoke({'topic':'H2o in chemistry'})


chain.get_graph().print_ascii()
print(result)