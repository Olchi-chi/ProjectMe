from fastapi import APIRouter

from users import router as user_router

api = APIRouter()

api.include_router(user_router)