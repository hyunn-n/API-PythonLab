from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str  # 이미지 위치 작성
    description: str
    tags: List[str]     # 예 ["전자", "중고", "삼성"]
    location: str       # 예 => 'gasan branch', 'on-line mall'


    class Config:
        json_schema_extra = {
            "example": {
                "title": "test title",
                "image": "http://www.test.pri/a.png",
                "description": "간단한 설명 추가",
                "tags": ["python", "fastapi", "study"],
                "location": "online"
            }
        }
