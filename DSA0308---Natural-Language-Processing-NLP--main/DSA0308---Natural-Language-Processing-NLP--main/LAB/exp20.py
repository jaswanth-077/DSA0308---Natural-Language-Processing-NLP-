from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Document collection
documents = [
    "Natural language processing deals with human language.",
    "Machine learning is used in natural language processing.",
    "Deep learning improves many NLP applications.",
    "Information retrieval finds relevant documents.",
    "Natural language processing is used in search engines."
]

# User query
query = input("Enter your search query: ")

# Create TF-IDF representation
vectorizer = TfidfVectorizer()

# Combine documents and query
all_text = documents + [query]

tfidf_matrix = vectorizer.fit_transform(all_text)

# Query vector
query_vector = tfidf_matrix[-1]

# Document vectors
document_vectors = tfidf_matrix[:-1]

# Calculate cosine similarity
scores = cosine_similarity(query_vector, document_vectors)[0]

# Rank documents
ranking = sorted(
    enumerate(scores),
    key=lambda x: x[1],
    reverse=True
)

# Display results
print("\nDocument Ranking:")
print("----------------------------")

for rank, (index, score) in enumerate(ranking, start=1):
    print(
        f"Rank {rank}: Document {index + 1} "
        f"(Score = {score:.4f})"
    )
    print(documents[index])
    print()