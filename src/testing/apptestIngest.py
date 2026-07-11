from src.services.ingestion_service import ingest_video

url = input("Enter YouTube URL: ")

video_id = ingest_video(url)

print()

print("=" * 60)

print("Video indexed successfully!")

print(f"Video ID : {video_id}")

print("=" * 60)