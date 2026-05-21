from fastapi import APIRouter
from services.registration_service import RegistrationService

router = APIRouter()

@router.post("/api/register")
async def register_user(user: User):
    service = RegistrationService()
    service.register_user(user)
    return {"message": "User registered successfully"}
