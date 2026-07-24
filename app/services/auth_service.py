from app.core.security import hash_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate


async def get_user_by_email(email: str) -> User | None:
    return await User.get_or_none(email=email)


async def get_user_by_username(username: str) -> User | None:
    return await User.get_or_none(username=username)


async def create_user(user_data: UserCreate) -> User:
    if await get_user_by_username(user_data.username):
        raise ValueError("Username already exists")

    if await get_user_by_email(user_data.email):
        raise ValueError("Email already exists")

    hashed_password = hash_password(user_data.password)

    user = await User.create(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )

    return user


async def authenticate_user(email: str, password: str) -> User | None:
    user = await get_user_by_email(email)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user