from fastapi import APIRouter
from models.login_request import LoginRequest
from services import auth_services

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
def login(login_data: LoginRequest):
    return auth_services.get_user_by_email(login_data)