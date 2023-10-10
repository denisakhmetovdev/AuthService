from pydantic import BaseModel, EmailStr
from typing import Optional, Union


class UserRequestSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str = None


class UserResponseSchema(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str = None
    is_admin: bool
    is_verify: bool
    is_active: bool
