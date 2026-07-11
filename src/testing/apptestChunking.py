from src.loaders.transcript import load_youtube_document
from src.processing.chunker import split_document

url = input("Enter YouTube URL: ")

document = load_youtube_document(url)

chunks = split_document(document)

# print(f"\nTotal Chunks: {len(chunks)}\n")

# print("=" * 80)

# print(chunks[0].page_content)
# print(chunks[0].metadata)

# print("=" * 80)

# print(chunks[1].page_content)
# print(chunks[1].metadata)

# print(chunks[2].metadata)

for i, chunk in enumerate(chunks):

    print("=" * 80)

    print(f"Chunk {i+1}")

    print(f"Characters : {len(chunk.page_content)}")

    print(chunk.page_content[:200])

    print()