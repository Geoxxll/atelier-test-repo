# 定义用户注册请求的输入验证模式
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
