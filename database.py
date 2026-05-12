from models.user_model import User
from services.security import hash_password

users = [
    User(
        id=1,
        name="Thiago",
        email="thiago@teste.com",
        password=hash_password("123")
    )
]