
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

# Load documents
documents = SimpleDirectoryReader("app/data").load_data()

# Embedding model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# ChromaDB setup
chroma_client = chromadb.Client()
vector_store = ChromaVectorStore(chroma_collection=chroma_client.get_or_create_collection("zoeta_docs"))

# Build index
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model, vector_store=vector_store)
query_engine = index.as_query_engine()

def query_llama_index(question: str):
    response = query_engine.query(question)
    return str(response), "https://zoeta-dogsoul.com"
