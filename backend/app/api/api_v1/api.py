from fastapi import APIRouter

from app.api.api_v1.endpoints import ai

api_router = APIRouter()
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])