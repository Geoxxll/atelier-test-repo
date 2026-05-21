from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.user_service import UserService

app = FastAPI()
user_service = UserService()

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

@app.post("/register/")
async def register(user: UserRegister):
    try:
        new_user = user_service.register_user(user.username, user.email, user.password)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))