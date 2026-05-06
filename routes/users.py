from fastapi import APIRouter, HTTPException
from models.user_model import BaseModel as User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

users = []

@router.get("/users")
def get_users():
    return users

@router.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:           
            return user
        
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/users")
async def register_user(new_user: User):
    
    for user in users:
        if user.email == new_user.email:
            raise HTTPException(status_code=409, detail="Email already registered")
        
    new_user.id = len(users) + 1
    users.append(new_user)

    return new_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": f"User {user.id} deleted!"}
        
    raise HTTPException(status_code=404, detail="User not found")