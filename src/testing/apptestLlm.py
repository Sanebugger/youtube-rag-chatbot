from src.models.llm import llm

response = llm.invoke(
    "who are you?"
)

print(response.content)