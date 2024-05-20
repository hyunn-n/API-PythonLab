from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.event import Event


# 회원 가입 모델
class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = None


    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@test.pri",
                "password": "test123",
                "events": []
            }
        }

# 로그인 모델
class UserSingIn(BaseModel):
    email: EmailStr
    password: str   # 보안상 결함있으나 향후 토큰으로 대체할 예정임


    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@test.pri",
                "password": "test123"
            }
        }
