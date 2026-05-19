from fastapi import APIRouter, Depends
from models.login_request import LoginRequest
from services import auth_services, auth_handler

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
def login(login_data: LoginRequest):
    return auth_services.get_user_by_email(login_data)

@router.get("/me")
def get_me(current_user = Depends(auth_handler.get_current_user_with_token)):
    return current_user