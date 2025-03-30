from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.routes import router as auth_router
from app.comments.routes import router as comments_router
from app.user.routes import router as user_router
from app.video.routes import router as video_router

app = FastAPI(
    title="SkufTube",
    description="API for lulz",
    version="0.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(video_router, prefix="/api/video", tags=["video"])
app.include_router(user_router, prefix="/api/user", tags=["user"])
app.include_router(comments_router, prefix="/api/comments", tags=["comments"])

@app.get("/")
async def root():
    return {"message": "SkufTube, altooshka - for only you"}