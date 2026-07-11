from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI


from src.config import (
    LLM_PROVIDER,
    MODEL_NAME,
    TEMPERATURE,
    GEMINI_API_KEY,
    MISTRAL_API_KEY,
)

def create_llm():

    if LLM_PROVIDER == "gemini":
        return ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            google_api_key=GEMINI_API_KEY
        )
    elif LLM_PROVIDER == "mistral":
        return ChatMistralAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            mistral_api_key=MISTRAL_API_KEY
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {LLM_PROVIDER}")


llm = create_llm()