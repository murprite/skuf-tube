from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def getComments():
    return {"status": "fulfilled"}