import math
from collections import Counter


# Sample documents
documents = [
    "machine learning is a branch of artificial intelligence",
    "deep learning is a subset of machine learning",
    "natural language processing works with text data",
    "python is widely used in data science"
]


# Tokenize documents
tokenized_docs = [doc.split() for doc in documents]
N = len(tokenized_docs)


# BM25 parameters
k1 = 1.5
b = 0.75


# Document lengths
doc_lens = [len(doc) for doc in tokenized_docs]
avg_doc_len = sum(doc_lens) / N


# Document frequency for each term
df = {}
for doc in tokenized_docs:
    for word in set(doc):
        df[word] = df.get(word, 0) + 1


# IDF calculation
idf = {}
for word, freq in df.items():
    idf[word] = math.log((N - freq + 0.5) / (freq + 0.5) + 1)


# Query
query = "machine learning".split()


# Score each document
scores = []
for i, doc in enumerate(tokenized_docs):
    score = 0
    tf = Counter(doc)


    for term in query:
        if term in tf:
            term_freq = tf[term]
            numerator = term_freq * (k1 + 1)
            denominator = term_freq + k1 * (1 - b + b * (doc_lens[i] / avg_doc_len))
            score += idf.get(term, 0) * (numerator / denominator)


    scores.append(score)


# Rank documents
ranked_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)


# Print results
print("Query:", " ".join(query))
print("\nTop Results:")
for idx in ranked_indices:
    print(f"{documents[idx]} (score: {scores[idx]:.4f})")
