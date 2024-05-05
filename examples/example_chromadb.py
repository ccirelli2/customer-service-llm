"""
Getting Started
- https://docs.trychroma.com/getting-started
How to persist data
- https://docs.trychroma.com/usage-guide
"""
import chromadb


# Create Client
chroma_client = chromadb.Client()

# Create a Collection
collection = chroma_client.create_collection("my_collection")

# Add some text documents
embeddings = [[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]]
documents = ["This is a document", "This is another document", "Today is a good day to code"]
metadata = [{"author": "John Doe"}, {"author": "Jane Doe"}, {"author": "John Doe"}]
ids = ["doc1", "doc2", "doc3"]


collection.add(
    documents=documents,
    metadatas=metadata,
    ids=ids,
    # embeddings=embeddings
)

# Query Documents
query_results = collection.query(
    query_texts=["I like coding"],
    n_results=1
)
print(query_results)