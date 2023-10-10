from uuid import uuid4

from sqlalchemy import UUID, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid4)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    phone: Mapped[str] = mapped_column(String(14), unique=True, nullable=True)
    # role: Mapped[str] = mapped_column(String(25))
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verify: Mapped[bool] = mapped_column(Boolean, default=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
