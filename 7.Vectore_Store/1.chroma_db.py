from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document


load_dotenv()


# Create documents
doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history.",
    metadata={"team": "Royal Challengers Bangalore"}
)


doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history.",
    metadata={"team": "Mumbai Indians"}
)


doc3 = Document(
    page_content="MS Dhoni is a legendary captain known for finishing matches.",
    metadata={"team": "Chennai Super Kings"}
)


doc4 = Document(
    page_content="KL Rahul is a stylish top-order batsman.",
    metadata={"team": "Lucknow Super Giants"}
)


doc5 = Document(
    page_content="Andre Russell is a powerful all-rounder.",
    metadata={"team": "Kolkata Knight Riders"}
)


doc6 = Document(
    page_content="Hardik Pandya is a dynamic all-rounder.",
    metadata={"team": "Gujarat Titans"}
)


docs = [doc1, doc2, doc3, doc4, doc5, doc6]


#Correct embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


# Correct Chroma import
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_db",
    collection_name="sample"
)


# Add documents
result= vector_store.add_documents(docs)


print(result)


print("Documents stored successfully!")


#view the documents
print(vector_store.get(include=['embeddings', 'documents', 'metadatas']))


#search documents
result= vector_store.similarity_search(
    query="Who among these are bowler",
    k=2
)
print(result)


#search documents
result= vector_store.similarity_search_with_score(
    query="Who among these are bowler",
    k=2
)
print(result)


#metadata filtering
result= vector_store.similarity_search_with_score(
    query="",
    filter={'team':"chennai super kings"}
   
)
print(result)


#update the documents
update_doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. IS very aggressive player in the history",
    metadata={"team": "Royal Challengers Bangalore"}
)


vector_store.update_document(document_id='5933c9b1-a03b-4e41-8b2e-e58c6d8e22d8', document=update_doc1)


#view the documents
print(vector_store.get(include=['embeddings', 'documents', 'metadatas']))


#delete the documents
#vector_store.delete(ids=['5933c9b1-a03b-4e41-8b2e-e58c6d8e22d8'])
