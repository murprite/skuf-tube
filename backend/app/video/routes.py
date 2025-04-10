from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pathlib import Path
import sqlite3
import os

DB_URL = os.environ.get('DB_URL')
router = APIRouter()

con = sqlite3.connect(DB_URL)
cur = con.cursor()

@router.get("/{filename}")
async def stream_video(filename: str):
    # potential sql injection
    video_path = Path(cur.execute(f"select * from videos where thumbnail_url = '{filename}'").fetchone()[1])

    print(cur.execute(f"select * from videos where thumbnail_url = '{filename}'").fetchone(), 'asdasd')
    print(video_path.resolve())
    filesize = video_path.stat().st_size

    async def video_streamer():
        with open(video_path, 'rb') as video_file:
            while True:
                # 1 Mb
                chunk = video_file.read(1024 * 1024)
                if not chunk:
                    print("End of chunks")
                    break
                yield chunk

    headers = {
        "content-type": "video/mp4",
        "Accept-Ranges": "bytes",
        "content-encoding": "identity",
        "content-length": str(filesize),
        'Content-Range': f'bytes 0-{filesize}/{filesize}',

    }
    return StreamingResponse(
        content=video_streamer(),
        media_type="video/mp4",
        headers=headers,
    )
