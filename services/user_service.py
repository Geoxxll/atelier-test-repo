# 实现用户注册服务，处理业务逻辑
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate

class UserService:
    def create_user(self, db: Session, user: UserCreate):
        db_user = User(username=user.username, email=user.email, password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
