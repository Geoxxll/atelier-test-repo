from database.db import SessionLocal, UserModel
from passlib.context import CryptContext

class UserService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password):
        return self.pwd_context.hash(password)

    def register_user(self, username, email, password):
        db = SessionLocal()
        hashed_password = self.hash_password(password)
        new_user = UserModel(username=username, email=email, password_hash=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user