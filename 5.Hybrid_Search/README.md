# 🔍 Hybrid Search Notes (Sparse + Dense)

---

## 🧠 What is Search?

Search = Finding relevant documents for a query

👉 Example:
Query: "machine learning"
Goal: Find most relevant text

---

## ⚡ 1. Sparse Search (Keyword Based)

### 📌 TF-IDF (Sparse_search.py)

- Based on:
  - Term Frequency (TF)
  - Inverse Document Frequency (IDF)

👉 Works on **exact words**

### ✅ Pros
- Fast
- Simple
- No API needed

### ❌ Cons
- Fails on typos ("mahcine")
- No semantic understanding

---

### 📌 BM25 (BM25.py)

- Improved version of TF-IDF
- Uses:
  - Term frequency
  - Document length normalization

👉 Used in:
- Elasticsearch
- Google (earlier systems)

### ✅ Pros
- Better ranking than TF-IDF
- Industry standard

### ❌ Cons
- Still keyword-based
- No semantic meaning

---

## ⚡ 2. Dense Search (Semantic Search)

### 📌 Dense_search.py

- Uses:
  - OpenAI Embeddings
  - FAISS (vector DB)

👉 Converts text → vectors

### 🧠 Key Idea:
Similar meaning → similar vectors

---

### ✅ Pros
- Understands meaning
- Works on paraphrases
- Handles typos better

### ❌ Cons
- Needs API (cost)
- Slower than sparse

---

## ⚡ 3. Hybrid Search (Best of Both)

### 📌 Hybrid_serach.py

👉 Combines:
- BM25 (keyword)
- Dense (semantic)

Using:
- EnsembleRetriever

---

### 🔥 Why Hybrid?

| Problem | Solution |
|--------|---------|
| Exact match needed | BM25 |
| Meaning needed | Dense |
| Want best result | Hybrid |

---

### ⚖️ Weights

```python
weights=[0.4, 0.6]