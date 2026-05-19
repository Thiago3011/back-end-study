from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from database import users
from fastapi import HTTPException, Depends

SECRET_KEY = "chave_secreta"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(user_id):
    return jwt.encode({"user_id": user_id}, key=SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token):
    return jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])

def get_current_user_with_token(token: str = Depends(oauth2_scheme)):
    token_decoded = decode_access_token(token)
    user_id_decoded = token_decoded["user_id"]
    for user in users:
        if user.id == user_id_decoded:
            return {"id": user.id, "email": user.email}
    raise HTTPException(detail="User is not with a valid token", status_code=401)