from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from src.config import CHUNK_SIZE, CHUNK_OVERLAP

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

def split_document(document: Document):
    """
    Split a LangChain Document into smaller Documents.
    """

    chunks = text_splitter.split_documents([document])

    return chunks