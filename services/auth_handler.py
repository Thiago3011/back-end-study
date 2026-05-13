from jose import jwt

SECRET_KEY = "chave_secreta"
ALGORITHM = "HS256"

def create_access_token(user_id):
    return jwt.encode({"user_id": user_id}, key=SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token):
    return jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
