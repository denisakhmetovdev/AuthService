from fastapi import FastAPI
from src.routers import user_router


api = FastAPI()


api.include_router(user_router)
