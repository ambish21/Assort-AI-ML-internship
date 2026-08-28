from datetime import datetime, timedelta, timezone

import jwt

from app.config.settings import settings


def create_access_token(username: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )

    payload = {
        "sub": username,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )


def verify_user(username: str, password: str) -> bool:
    # Temporary user for Day 26 practice
    return username == "admin" and password == "1234"