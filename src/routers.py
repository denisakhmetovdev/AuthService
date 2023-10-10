from typing import List

from fastapi import APIRouter, Depends

from src.schemas import UserRequestSchema, UserResponseSchema

from src.database.queries import get_user_query, create_user_query, get_all_users


user_router = APIRouter(prefix="", tags=["register"])


@user_router.post(
    "/register",
    summary="Регистрация пользователей",
    status_code=201
)
async def register(user: UserRequestSchema = Depends(create_user_query)):# -> UserResponseSchema:
    res = await create_user_query(user)
    return res


@user_router.get(
    "/users",
    summary="Получить всех пользователей"
)
async def get_users() -> List[UserResponseSchema]:
    user_list = await get_all_users()
    return user_list
