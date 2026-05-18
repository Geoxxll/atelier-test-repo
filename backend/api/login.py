from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post('/login')
async def login(request: LoginRequest):
    # 这里添加用户验证逻辑
    return {'message': 'Login successful'}