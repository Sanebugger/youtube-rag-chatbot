from langchain_core.runnables import RunnablePassthrough

from src.models.llm import llm

from src.prompts.rag_prompts import rag_prompt

from src.utils.formatter import format_docs


def create_rag_chain(retriever):

    chain = (

        {

            "context": retriever | format_docs,

            "question": RunnablePassthrough(),

        }

        | rag_prompt

        | llm

    )

    return chain