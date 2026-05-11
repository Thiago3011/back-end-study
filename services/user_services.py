from models.user_model import User
from fastapi import HTTPException
from services.security import hash_password

users = [
    {"id": 1, "name": "Thiago", "email": "thiago@teste.com"}
]

def get_users():
    return users

def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:           
            return user
        
    raise HTTPException(status_code=404, detail="User not found")

def register_user(new_user: User):
    
    for user in users:
        if user["email"] == new_user.email:
            raise HTTPException(status_code=409, detail="Email already registered")
        
    new_user.id = len(users) + 1
    new_user.password = hash_password(new_user.password)
    users.append(new_user)

    return new_user

def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": f"User {user["id"]} deleted!"}
        
    raise HTTPException(status_code=404, detail="User not found")
    