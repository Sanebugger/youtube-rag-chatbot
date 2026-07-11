# from langchain_core.documents import Document

# doc = Document(

#     page_content="""
#     Machine Learning is a field of Artificial Intelligence.
#     """
#     ,

#     metadata={
#         "source":"youtube",
#         "title":"ML Course"
#     }

# )

# # print(doc)
# # print(doc.page_content)
# print(doc.metadata)
# # print(doc.metadata["title"])

# from src.transcript import get_video_id

# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# video_id = get_video_id(url)

# print(video_id)




# from src.transcript import (
#     get_video_id,
#     download_transcript
# )

# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# video_id = get_video_id(url)

# transcript = download_transcript(video_id)

# print(type(transcript))
# print(len(transcript))
# print()
# print(transcript[0])

from src.loaders.transcript import load_youtube_document

url = input("Enter YouTube URL: ")

document = load_youtube_document(url)

print("="*80)

print(document.page_content[:500])

print()

print(document.metadata)