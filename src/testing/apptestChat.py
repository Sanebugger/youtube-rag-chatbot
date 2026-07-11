# from src.services.chat_service import create_chat_session

# video_id = input("Enter Video ID: ")

# rag_chain = create_chat_session(video_id)

# while True:

#     question = input("\nAsk: ")

#     if question.lower() == "exit":
#         break

#     try:
#         response = rag_chain.invoke(question)

#         print("\nAnswer:\n")
#         print(response.content)

#     except Exception as e:
#         print("\nSomething went wrong!\n")
#         print(e)

from src.services.chat_service import ChatService


video_id = input("Enter Video ID: ")

chat = ChatService(video_id)

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    try:

        # response = chat.ask(question)

        # print("\nAnswer:\n")

        # print(response.content)
        answer = chat.ask(question)

        print("\nAnswer:\n")

        print(answer)

    except Exception as e:

        print("\nSomething went wrong.\n")

        print(e)