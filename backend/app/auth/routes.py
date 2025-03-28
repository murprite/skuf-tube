from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel
from app.auth.utils import create_token, verify_token, refresh_token_store
from app.config import ACCESS_TOKEN_EXPIRE, REFRESH_TOKEN_EXPIRE
from datetime import timedelta

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(request: LoginRequest, response: Response):
    if request.email != "user@example.com" or request.password != "pass123":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    user_id = "user_id_123"

    access_token = create_token({"sub": user_id}, timedelta(minutes=ACCESS_TOKEN_EXPIRE), "access")
    refresh_token = create_token({"sub": user_id}, timedelta(days=REFRESH_TOKEN_EXPIRE), "refresh")

    jti = jwt.decode(refresh_token, JWT_SECRET_KEY, algorithms=[ALGORITHM])["jti"]
    refresh_token_store[jti] = {"user_id": user_id, "expires": datetime.utcnow() + timedelta(days=7)}

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        max_age=REFRESH_TOKEN_EXPIRE * 86400,
    )

    return {"access_token": access_token, "expires_in": ACCESS_TOKEN_EXPIRE}