from src.models.embeddings import embeddings

# vector = embeddings.embed_query(
#     "Machine Learning"
# )

# print(type(vector))

# print()

# print(len(vector))

# print()

# print(vector[:10])

vector1 = embeddings.embed_query("Dog")

vector2 = embeddings.embed_query("Canine")

print(len(vector1))
print(len(vector2))