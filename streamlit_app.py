import streamlit as st

from src.services.application_service import ApplicationService

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="YouTube RAG",
    page_icon="🎥",
    layout="wide",
)
# hide_streamlit_style = """
# <style>
# #MainMenu {
#     visibility: hidden;
# }

# footer {
#     visibility: hidden;
# }

# header {
#     visibility: hidden;
# }
# </style>
# """

# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "chat" not in st.session_state:
    st.session_state.chat = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🎥 Talk To A YouTube Video")

st.caption(
    "Paste a YouTube URL and chat with its transcript."
)

st.divider()

# --------------------------------------------------
# YouTube URL
# --------------------------------------------------

url = st.text_input(
    "YouTube URL"
)

# --------------------------------------------------
# Load Video
# --------------------------------------------------

if st.button(
    "Load Video",
    use_container_width=True
):

    if not url:

        st.warning("Please enter a YouTube URL.")

    else:

        st.session_state.chat = None

        with st.spinner("Preparing knowledge base..."):

            try:

                app = ApplicationService(url)

                st.session_state.chat = app.initialize()

                # New video → clear previous conversation
                st.session_state.messages = []

                st.success(
                    "Knowledge base is ready. You can start chatting!"
                )

            except Exception as e:

                st.session_state.chat = None

                st.error(
                    f"Failed to load video.\n\n{e}"
                )
                

# --------------------------------------------------
# Display Previous Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask a question...",
    disabled=st.session_state.chat is None
)

# --------------------------------------------------
# Chat Logic
# --------------------------------------------------

if question:

    # Display User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    # Generate Assistant Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # response = st.session_state.chat.ask(question)

            # st.write(response.content)
            answer = st.session_state.chat.ask(question)

            st.write(answer)

    # Save Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            # "content": response.content
            "content": answer
        }
    )