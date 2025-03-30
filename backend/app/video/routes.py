from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import aiofiles
import os

router = APIRouter()

@router.get("/{filename}")
async def stream_video(filename: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    video_dir = os.path.join(current_dir, "..", "..", f"static/videos/{filename}.mp4")
    video_path = os.path.normpath(video_dir)

    if not os.path.exists(video_path):
        return {"error": "File is not found"}

    async def video_streamer():
        async with aiofiles.open(video_path, 'rb') as video_file:
            while True:
                # 1 Mb
                chunk = await video_file.read(1024 * 1024)
                if not chunk:
                    break
                yield chunk

    headers = {
        "Accept-Ranges": "bytes",
    }
    return StreamingResponse(
        video_streamer(),
        media_type="video/mp4",
        headers=headers
    )
