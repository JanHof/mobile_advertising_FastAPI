from passlib.context import CryptContext
import os
from bcrypt import hashpw, checkpw, gensalt
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from pydantic import ValidationError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import HTTPException
from config import conn, SECRET_KEY, ALGORITHM


ACCESS_TOKEN_EXPIRE_MINUTES = 30



# Create a password context for hashing and verification
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")



# Generate JWT token
def generate_token(user: dict) -> str:
    payload = {
        "user_id": str(user["_id"]),
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# Verify JWT token
def verify_token(token: str) -> bool:
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except jwt.exceptions.ExpiredSignatureError:
        return False
    except jwt.exceptions.JWTError:
        return False


# Hash the password
def hash_password(password: str) -> str:
    salt = gensalt()
    hashed_password = hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")

# Verify the password
def verify_password(password: str, hashed_password: str) -> bool:
    return checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

#login user service
async def login_user_service(form_data: OAuth2PasswordRequestForm):
    user = await conn["azul"]["user"].find_one({"name": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        return None
    access_token = generate_token(user)
    return access_token