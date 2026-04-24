from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda


load_dotenv()


model = ChatOpenAI(model='gpt-4o')


class Feedback(BaseModel):
    sentiments: Literal['Pos', 'Neg'] = Field(
        description="Classify the customer feedback as positive or negative. Use Pos for positive and Neg for negative."
    )


parser_feedback = PydanticOutputParser(pydantic_object=Feedback)
parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="""
Classify the customer feedback as positive or negative.


Customer feedback: {feedback}


{format_instructions}
""",
    input_variables=['feedback'],
    partial_variables={
        'format_instructions': parser_feedback.get_format_instructions()
    }
)


prompt_pos = PromptTemplate(
    template="Write an appropriate response for positive feedback: {feedback}",
    input_variables=['feedback']
)


prompt_neg = PromptTemplate(
    template="Write an appropriate response for negative feedback: {feedback}",
    input_variables=['feedback']
)


chain_feedback = prompt1 | model | parser_feedback


chain = (
    RunnableLambda(
        lambda x: {
            "feedback": x["feedback"],
            "sentiment": chain_feedback.invoke({"feedback": x["feedback"]}).sentiments
        }
    )
    | RunnableBranch(
        (
            lambda x: x["sentiment"] == "Pos",
            RunnableLambda(lambda x: {"feedback": x["feedback"]}) | prompt_pos | model | parser
        ),
        (
            lambda x: x["sentiment"] == "Neg",
            RunnableLambda(lambda x: {"feedback": x["feedback"]}) | prompt_neg | model | parser
        ),
        RunnableLambda(lambda x: "could not find sentiment")
    )
)


result = chain.invoke({"feedback": "very bad phone"})


print(result)
chain.get_graph().print_ascii()
