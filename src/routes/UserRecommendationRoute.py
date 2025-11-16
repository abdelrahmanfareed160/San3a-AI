from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

user_recommendation_router = APIRouter(
    prefix="/api/AI/user",
    tags=["AI", 'user']
)

@user_recommendation_router.post("/recommendation")
async def user_recommendation():
    pass