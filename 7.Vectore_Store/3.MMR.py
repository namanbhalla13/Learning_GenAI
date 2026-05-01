
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma


load_dotenv()


embedding_model = OpenAIEmbeddings()


vectorstore = Chroma(
    persist_directory="chroma_db",
    collection_name="sample",
    embedding_function=embedding_model
)



retriever = vectorstore.as_retriever(
    search_type='mmr',
    search_kwargs={'k': 2,'lambda_mult':1}) #lambda_mult--> relevance-diveristy balance


query = "who is consistent batsmen player?"


# retrieve docs
results = retriever.invoke(query)


# print results
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)   
    print(doc.metadata)
