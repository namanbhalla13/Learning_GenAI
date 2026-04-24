import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv


load_dotenv()


# 2. Sample documents (you can replace with your own corpus)
documents = [
    "BM25 is a sparse retrieval method based on term frequency.",
    "Dense retrieval uses embeddings to capture semantic meaning.",
    "FAISS is a library for efficient similarity search.",
    "OpenAI provides powerful embedding models for semantic search."
]


#intial the embedding
emeddding= OpenAIEmbeddings(
    model="text-embedding-3-large"  # or text-embedding-3-small
)
#create vector databse
vectorstores= FAISS.from_texts(documents,emeddding)


#query
query = "What is dense retrieval?"


# 6. Perform dense similarity search
results = vectorstores.similarity_search(query, k=2)


# 7. Print results
print("\nTop results:\n")
for i, doc in enumerate(results):
    print(f"{i+1}. {doc.page_content}")
