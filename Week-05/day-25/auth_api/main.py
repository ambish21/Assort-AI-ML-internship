from fastapi import FastAPI
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Authentication API is working!"
    }


@app.post("/register")
def register(password: str):
    hashed_password = hash_password(password)

    return {
        "message": "User registered successfully",
        "hashed_password": hashed_password
    }


@app.post("/login")
def login(password: str, hashed_password: str):
    if not verify_password(password, hashed_password):
        return {
            "message": "Invalid password"
        }

    token = create_access_token({
        "user": "student"
    })

    return {
        "message": "Login successful",
        "access_token": token
    }


@app.get("/protected")
def protected_route(token: str):
    payload = decode_access_token(token)

    if payload is None:
        return {
            "message": "Invalid or expired token"
        }

    return {
        "message": "Access granted",
        "user": payload.get("user")
    }