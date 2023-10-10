from pathlib import Path
from typing import AsyncGenerator
from os import environ

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = Path(BASE_DIR, ".env")

load_dotenv()


DB_USER = environ.get("POSTGRES_USER")
DB_PASSWORD = environ.get("POSTGRES_PASSWORD")
DB_HOST = environ.get("DB_HOST")
DB_PORT = environ.get("POSTGRES_PORT")
DB_NAME = environ.get("POSTGRES_DB")


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_async_engine(url=DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession)  # expire_on_commit=False)


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session() as session:
#         yield session
