from models.login_request import LoginRequest
from database import users
from services.security import verify_password
from fastapi import HTTPException
from services.auth_handler import create_access_token 

def get_user_by_email(login_data: LoginRequest):
    for user in users:
        if login_data.email == user.email:
            if verify_password(login_data.password, user.password):
                access_token = create_access_token(user.id)
                token_type = "bearer"

                return {"message": "Login successful", "access_token": access_token, "token_type": token_type}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")
            