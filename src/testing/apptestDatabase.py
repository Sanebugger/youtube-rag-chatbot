##############################################################
# TEST DATABASE CREATION AND STORING CHUNKS
##############################################################

# from src.transcript import load_youtube_document

# from src.chunker import split_document

# from src.database.vectordb import create_vector_store


# url = input("Enter YouTube URL: ")

# document = load_youtube_document(url)

# chunks = split_document(document)

# vector_store = create_vector_store(chunks)

# print()

# print("Vector database created successfully!")

# print(f"Stored {len(chunks)} chunks.")





########################################################################
# TEST DATABASE CREATION AND STORING CHUNKS
# TEST RETRIEVER
########################################################################
from src.loaders.transcript import load_youtube_document
from src.processing.chunker import split_document

from src.database.vectordb import (
    create_vector_store,
    create_retriever
)

url = input("Enter YouTube URL: ")

document = load_youtube_document(url)

chunks = split_document(document)

vector_store = create_vector_store(chunks)

retriever = create_retriever(vector_store)

question = input("\nAsk a question: ")

results = retriever.invoke(question)

print()

print("=" * 80)

print(f"Retrieved {len(results)} chunks.\n")

for i, doc in enumerate(results):

    print(f"Chunk {i+1}")

    print("-"*80)

    print(doc.page_content[:400])

    print()