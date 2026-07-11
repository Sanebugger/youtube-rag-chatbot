from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.config import GEMINI_API_KEY, EMBEDDING_MODEL

embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    google_api_key=GEMINI_API_KEY
)

def embed_query(query: str):
    """Generate an embedding for a user query."""
    return embeddings.embed_query(query)

def embed_documents(texts: list[str]):
    """Generate embeddings for multiple document chunks."""
    return embeddings.embed_documents(texts)