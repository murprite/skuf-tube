from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def getUser():

    return {"status": "fulfilled"}