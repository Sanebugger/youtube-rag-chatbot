# from langchain_chroma import Chroma

# from src.embeddings import embeddings
# from langchain_core.documents import Document
# from src.config import CHROMA_DB_PATH

# def create_vector_store(chunks: list[Document]):
#     """
#     Create a Chroma vector database
#     from LangChain Documents.
#     """

#     vector_store = Chroma.from_documents(

#         documents=chunks,

#         embedding=embeddings,

#         persist_directory=CHROMA_DB_PATH

#     )

#     return vector_store

# def create_retriever(vector_store):
#     """
#     Create a retriever from the vector database.
#     """

#     retriever = vector_store.as_retriever(
#         search_kwargs={"k": 3}
#     )

#     return retriever

from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document

from src.models.embeddings import embeddings
from src.config import CHROMA_DB_PATH


def get_db_path(video_id: str) -> str:
    """
    Return the database path for a video.
    """

    db_path = Path(CHROMA_DB_PATH) / video_id

    return str(db_path)

def create_vector_store(
    chunks: list[Document],
    video_id: str
):
    """
    Create a Chroma database
    for one YouTube video.
    """

    db_path = get_db_path(video_id)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_path
    )

    return vector_store

def load_vector_store(video_id: str):
    """
    Load an existing Chroma database.
    """

    db_path = get_db_path(video_id)

    vector_store = Chroma(
        persist_directory=db_path,
        embedding_function=embeddings
    )

    return vector_store

# def create_retriever(vector_store):

#     retriever = vector_store.as_retriever(
#         search_kwargs={"k": 3}
#     )

#     return retriever

def database_exists(video_id: str) -> bool:
    """
    Returns True if the vector database
    already exists for this video.
    """

    db_path = Path(get_db_path(video_id))

    return db_path.exists()