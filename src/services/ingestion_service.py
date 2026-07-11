from src.loaders.transcript import (
    load_youtube_document,
    get_video_id
)

from src.processing.chunker import split_document

from src.database.vectordb import (
    create_vector_store
)


def ingest_video(url: str):
    """
    Download a YouTube transcript,
    split it into chunks,
    and create a vector database.
    """

    video_id = get_video_id(url)

    document = load_youtube_document(url)

    chunks = split_document(document)

    create_vector_store(
        chunks=chunks,
        video_id=video_id
    )

    return video_id