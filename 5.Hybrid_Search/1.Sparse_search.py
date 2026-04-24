from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# List of documents (corpus)
# Add actual text documents here instead of an empty string
documents = [
    "Machine learning is a field of artificial intelligence",
    "Deep learning is a subset of machine learning",
    "Natural language processing involves text analysis"
]


# Query string (note: typo 'mahcine' will affect results)
query = "mahcine learning"


# Create TF-IDF vectorizer
vector = TfidfVectorizer()


# Learn vocabulary + compute TF-IDF matrix for documents
doc_vector = vector.fit_transform(documents)


# Transform query into the same TF-IDF space
query_vector = vector.transform([query])


# Compute cosine similarity between query and all documents
similarities = cosine_similarity(query_vector, doc_vector)


# Get indices of documents sorted by similarity (highest first)
rank_indices = similarities.argsort()[0][::-1]


# Print results
print("Query:", query)
print("\nTop Results:")


for idx in rank_indices:
    print(f"{documents[idx]} (score: {similarities[0][idx]:.4f})")
