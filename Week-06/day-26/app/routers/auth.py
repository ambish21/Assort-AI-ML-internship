from fastapi import APIRouter, HTTPException

from app.models.user import UserLogin, Token
from app.services.auth_service import create_access_token, verify_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(user: UserLogin):
    if not verify_user(user.username, user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(user.username)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }