from sqlalchemy import text

from src.database.models import User
from src.schemas import UserRequestSchema, UserResponseSchema
from src.database.connect import async_session


async def get_user_query():
    ...


async def create_user_query(user_data: UserRequestSchema):# -> UserResponseSchema:
    async with async_session() as asession:
        asession.add(user_data)
        await asession.commit()
        new_user = await asession.refresh(user_data)
    return new_user


async def get_all_users():
    async with async_session() as asession:
        users = asession.execute(text("SELECT * FROM users"))
        user_list = [
            UserResponseSchema(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                phone=user.phone,
                is_admin=user.is_admin,
                is_verify=user.is_verify,
                is_active=user.is_active
            ) for user in users
        ]
    return user_list
