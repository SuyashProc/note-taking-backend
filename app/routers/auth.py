from fastapi import APIRouter, HTTPException

from app.core.security import create_access_token
from app.schemas.auth import TokenResponse, LoginRequest
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import create_user, authenticate_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/signup",
    response_model=UserResponse,
    status_code=201
)   
async def signup(user_data: UserCreate):
    try:
        return await create_user(user_data)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse
)
async def login(login_data: LoginRequest):
    user = await authenticate_user(
        login_data.email,
        login_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(user.id)

    return TokenResponse(
        access_token=access_token,
        token_type="bearer"
    )

