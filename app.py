# from src.llm import llm

# response = llm.invoke("Introduce yourself in one sentence.")

# # print(response.content)
# print(type(response))
# print(response)

# #########################################################################
# Using a simple string like invoke("what is capital of india?") works for basic questions, but it fails in real-world applications for three main reasons: read later
# The Solution: The Message Array
# from langchain_core.messages import (
#     HumanMessage,
#     SystemMessage
# )

# from src.llm import llm

# messages = [

#     SystemMessage(
#         content="You are a strict Machine Learning professor."
#     ),

#     HumanMessage(
#         content="Explain overfitting."
#     )

# ]

# response = llm.invoke(messages)

# # print(response.content)
# print(type(response))



##################################################################################
# implemented a prompt template to make the code more structured and reusable
# also added a prompt.py file to store the prompt template
# also implemented chain to connect the prompt template and llm together
# The chain automatically passes the output of one component into the next.No manual work.

# from src.llm import llm
# from src.prompt import prompt

# chain = prompt | llm

# response = chain.invoke({
#     "question": "What is Machine Learning?"
# })

# print(response.content)

# from src.chains import basic_chain

# response = basic_chain.invoke(
#     {
#         "question":"What is Deep Learning?"
#     }
# )

# print(response.content)

# from src.transcript import load_youtube_document
# from src.chunker import split_document
# from src.database.vectordb import (
#     create_vector_store,
#     create_retriever,
# )

# from src.chains.rag_chain import create_rag_chain

# url = input("Enter YouTube URL: ")

# document = load_youtube_document(url)

# chunks = split_document(document)

# vector_store = create_vector_store(chunks)

# retriever = create_retriever(vector_store)

# rag_chain = create_rag_chain(retriever)

# while True:

#     question = input("\nAsk: ")

#     if question.lower() == "exit":
#         break

#     response = rag_chain.invoke(question)

#     print("\nAnswer:\n")

#     print(response.content)

#######################################FINALY#############################

from src.services.application_service import ApplicationService

print("=" * 60)
print("🎥 YouTube Transcript RAG Chatbot")
print("=" * 60)

url = input("\nEnter YouTube URL: ")

app = ApplicationService(url)

chat = app.initialize()

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    try:

        response = chat.ask(question)

        print("\nAnswer:\n")

        print(response.content)

    except Exception as e:

        print("\nSomething went wrong.\n")

        print(e)