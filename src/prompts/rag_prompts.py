from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Answer the question ONLY using the provided context.

If the answer is not present in the context,
reply:

"I couldn't find that information in the video transcript."

Context:
{context}

Question:
{question}

Answer:
"""
)