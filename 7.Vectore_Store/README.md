# 🧠 LangChain + Chroma Vector Store – README & Notes

This document explains how to:

* Create documents
* Store them in a vector database (Chroma)
* Perform similarity search
* Use metadata filtering
* Update & delete documents
* Use retrievers (including MMR)

---

## ✅ Imports & Environment

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document

load_dotenv()
```

* `load_dotenv()` → loads API keys from `.env`
* `OpenAIEmbeddings` → converts text → vectors
* `Chroma` → vector database

---

# 📄 Step 1: Create Documents

```python
doc1 = Document(
    page_content="Virat Kohli is one of the most successful...",
    metadata={"team": "Royal Challengers Bangalore"}
)
```

## 🧠 Key Concepts

* `page_content` → actual text
* `metadata` → extra info (used for filtering)

---

# 🔢 Step 2: Create Embeddings

```python
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
```

* Converts text → numerical vectors
* Required for similarity search

---

# 🗄️ Step 3: Create Vector Store (Chroma)

```python
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_db",
    collection_name="sample"
)
```

## 🧠 Key Concepts

* `persist_directory` → saves DB locally
* `collection_name` → logical grouping

---

# ➕ Step 4: Add Documents

```python
result = vector_store.add_documents(docs)
print(result)
```

* Stores documents + embeddings
* Returns document IDs

---

# 👀 Step 5: View Stored Data

```python
vector_store.get(include=['embeddings', 'documents', 'metadatas'])
```

---

# 🔍 Step 6: Similarity Search

```python
result = vector_store.similarity_search(
    query="Who among these are bowler",
    k=2
)
```

## 🧠 Notes

* Finds most similar documents
* `k` → number of results

---

# 📊 Step 7: Similarity Search with Score

```python
result = vector_store.similarity_search_with_score(
    query="Who among these are bowler",
    k=2
)
```

* Returns `(document, score)`
* Lower score = better match

---

# 🧾 Step 8: Metadata Filtering

```python
result = vector_store.similarity_search_with_score(
    query="",
    filter={'team': "chennai super kings"}
)
```

## ⚠️ Important

* Filtering is **case-sensitive**
* `"Chennai Super Kings"` ≠ `"chennai super kings"`

---

# 🔄 Step 9: Update Document

```python
vector_store.update_document(
    document_id='YOUR_DOC_ID',
    document=update_doc1
)
```

## 🧠 Notes

* You must use correct `document_id`
* Replaces existing content

---

# ❌ Step 10: Delete Document

```python
vector_store.delete(ids=['YOUR_DOC_ID'])
```

---

# 🔁 Step 11: Retriever (Basic)

```python
retriever = vectorstore.as_retriever(search_kwargs={'k': 2})

results = retriever.invoke(query)
```

## 🧠 Notes

* Simplifies search interface
* Returns relevant documents

---

# 🔀 Step 12: Retriever with MMR (Advanced)

```python
retriever = vectorstore.as_retriever(
    search_type='mmr',
    search_kwargs={'k': 2, 'lambda_mult': 1}
)
```

## 🧠 What is MMR?

**MMR = Maximal Marginal Relevance**

Balances:

* Relevance (similarity)
* Diversity (avoid duplicates)

## ⚙️ `lambda_mult`

| Value | Behavior       |
| ----- | -------------- |
| 0     | More diversity |
| 1     | More relevance |

---

# 📌 Example Output Loop

```python
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
    print(doc.metadata)
```

---


# 🚀 Full Flow Summary

1. Create documents
2. Convert to embeddings
3. Store in Chroma
4. Perform search
5. Filter using metadata
6. Update/delete when needed
7. Use retriever for pipelines

---

# 🧠 Key Concepts to Remember

* Vector DB = semantic search (not keyword search)
* Embeddings = meaning of text
* Metadata = filtering layer
* Retriever = abstraction over search
* MMR = relevance + diversity

