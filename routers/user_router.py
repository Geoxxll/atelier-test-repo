# 定义用户注册的 API 路由
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.user_service import UserService
from schemas.user import UserCreate
from database.db import get_db

router = APIRouter()

@router.post('/register')
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService()
    return user_service.create_user(db=db, user=user)
