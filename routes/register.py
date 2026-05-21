from fastapi import APIRouter
from services.user_registration_service import UserRegistrationService

router = APIRouter()

@router.post("/register")
async def register(user: User):
    service = UserRegistrationService()
    service.register_user(user)
    return {"message": "User registered successfully"}
