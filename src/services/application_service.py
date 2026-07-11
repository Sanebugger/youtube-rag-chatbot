# This service will coordinate:
# ingestion
# database checking
# chat creation
# Think of it as the manager.

from src.database.vectordb import database_exists
from src.services.ingestion_service import ingest_video
from src.services.chat_service import ChatService

from src.loaders.transcript import get_video_id


class ApplicationService:

    def __init__(self, url: str):

        self.url = url

        self.video_id = get_video_id(url)

    def initialize(self):

        if database_exists(self.video_id):

            print("\n✓ Existing knowledge base found.")

        else:

            print("\n⏳ Creating knowledge base...")

            ingest_video(self.url)

            print("\n✓ Video indexed successfully.")

        return ChatService(self.video_id)