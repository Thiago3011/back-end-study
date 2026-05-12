from models.login_request import LoginRequest
from database import users
from services.security import verify_password
from fastapi import HTTPException

def get_user_by_email(login_data: LoginRequest):
    for user in users:
        if login_data.email == user.email:
            if verify_password(login_data.password, user.password):
                return {"message": "Login successful"}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")
            