from fastapi import APIRouter
from services import user_services 
from models.user_model import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def get_users():
    return user_services.get_users()

@router.get("/{user_id}")
def get_user(user_id: int):
    return user_services.get_user(user_id)

@router.post("/")
def register_user(new_user: User):
    return user_services.register_user(new_user)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return user_services.delete_user(user_id)

@router.patch("/{user_id}")
def update_user(user_id: int):
    return user_services.update_user(user_id)