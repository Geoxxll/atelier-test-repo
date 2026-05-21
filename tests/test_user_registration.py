import pytest
from services.user_registration_service import UserRegistrationService

@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password_hash": "hashed_password"
    }

def test_register_user(user_data):
    service = UserRegistrationService()
    result = service.register_user(user_data)
    assert result is not None
