from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document

def get_video_id(url: str) -> str:
    """
    Extract the YouTube video ID from a URL.

    Supports:
    - https://www.youtube.com/watch?v=...
    - https://youtu.be/...
    """

    parsed_url = urlparse(url)

    # Case 1: youtube.com/watch?v=...
    if "youtube.com" in parsed_url.netloc:
        query_params = parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]

    # Case 2: youtu.be/...
    if "youtu.be" in parsed_url.netloc:
        return parsed_url.path.lstrip("/")

    raise ValueError("Invalid YouTube URL")

def download_transcript(video_id: str):
    """
    Download the transcript for a YouTube video.

    Returns:
        List of transcript segments.
    """

    transcript = YouTubeTranscriptApi().fetch(video_id)

    return transcript

def transcript_to_document(transcript, video_id: str) -> Document:
    """
    Convert transcript segments into a LangChain Document.
    """

    full_text = " ".join(
        segment.text for segment in transcript
    )

    document = Document(
        page_content=full_text,
        metadata={
            "source": "youtube",
            "video_id": video_id
        }
    )

    return document

# now finally we can use the above functions to get the transcript of a youtube video in the form of a langchain document(page_content and metadata).
# This document can be used for further processing, such as question answering or summarization.




def load_youtube_document(url: str) -> Document:
    """
    Complete pipeline.

    URL
        ↓
    Video ID
        ↓
    Transcript
        ↓
    Document
    """

    video_id = get_video_id(url)

    transcript = download_transcript(video_id)

    document = transcript_to_document(
        transcript,
        video_id
    )

    return document