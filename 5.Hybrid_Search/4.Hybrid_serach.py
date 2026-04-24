import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain.retrievers.ensemble import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever


load_dotenv()


# 2. Sample documents (you can replace with your own corpus)
documents = [
    "BM25 is a sparse retrieval algorithm based on term frequency and inverse document frequency.",
    "Dense retrieval uses embeddings to capture semantic meaning between queries and documents.",
    "Hybrid search combines sparse retrieval like BM25 with dense vector similarity search.",
    "FAISS is a library for efficient vector similarity search and nearest neighbor lookup.",
    "OpenAI embedding models can be used to power semantic search systems.",
    "Keyword search is strong for exact term matching, while dense search is strong for semantic similarity."
]


#intial the embedding
emeddding= OpenAIEmbeddings(
    model="text-embedding-3-large"  # or text-embedding-3-small
)
#create vector databse
vectorstores= FAISS.from_texts(documents,emeddding)
dense_retervier= vectorstores.as_retriever(search_kwargs={"k": 3})


#BM25 reteriver
bm25_retriver= BM25Retriever.from_texts(documents)
bm25_retriver.k=3


#hybrid search
hybrid_rertiver=EnsembleRetriever(
    retrievers=[bm25_retriver, dense_retervier],
    weights=[0.4, 0.6]
)


#query
query = "How does hybrid retrieval work?"


#Perform dense similarity search
results = hybrid_rertiver.invoke(query)


#Print results
print("\nTop hybrid results:\n")
for i, doc in enumerate(results, 1):
    print(f"{i}. {doc.page_content}")