from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSingIn


user_router = APIRouter(
        tags=["User"],
)


users = {}


# 회원가입
@user_router.post("/signup") # ("/signup", tags=["User"]) 와 같음
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="이미 가입한 회원입니다"
        )
    users[data.email] = data
    return {
            "message": "가입되었습니다"
            }


# 로그인
@user_router.post("/signin")
async def sign_user_in(user: UserSingIn) -> dict:
    if user.email not in users:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="존재하지 않는 사용자 입니다"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="잘못된 패스워드 입니다"
        )
    return {
            "message": "로그인 되었습니다"
            }
