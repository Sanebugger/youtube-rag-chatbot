from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Application
APP_NAME = os.getenv("APP_NAME")

# LLM Provider
LLM_PROVIDER = os.getenv("LLM_PROVIDER")

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Mistral
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Model
MODEL_NAME = os.getenv("MODEL_NAME")
TEMPERATURE = float(os.getenv("TEMPERATURE"))

# Text Splitting
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))

# Embedding Model
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# Vector Database
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")


