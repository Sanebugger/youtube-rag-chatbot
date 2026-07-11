# from src.database.vectordb import (
#     load_vector_store,
# )
# from src.retrieval.retriever import (
#     create_retriever,
# )
# from src.chains.rag_chain import (
#     create_rag_chain,
# )


# def create_chat_session(video_id: str):
#     """
#     Create a chat session
#     for an existing video.
#     """

#     vector_store = load_vector_store(video_id)

#     retriever = create_retriever(vector_store)

#     rag_chain = create_rag_chain(retriever)

#     return rag_chain


from urllib import response

from src.database.vectordb import load_vector_store
from src.retrieval.retriever import create_retriever
from src.chains.rag_chain import create_rag_chain


class ChatService:
    """
    Handles chatting with a single indexed YouTube video.
    """

    def __init__(self, video_id: str):

        self.video_id = video_id

        self.vector_store = load_vector_store(video_id)

        self.retriever = create_retriever(
            self.vector_store
        )

        self.rag_chain = create_rag_chain(
            self.retriever
        )
        
    # def ask(self, question: str):
    #     response = self.rag_chain.invoke(question)

    #     return response
    
    def ask(self, question: str) -> str:
        """
        Ask a question about the indexed video.

        Returns:
        The answer as a plain string.
        """

        response = self.rag_chain.invoke(question)

        return response.content
    


