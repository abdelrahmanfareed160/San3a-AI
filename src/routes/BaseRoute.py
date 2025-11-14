from fastapi import APIRouter, Depends
from helpers import get_settings, Settings

base_router = APIRouter()

@base_router.get("/")
async def check_base(app_settings: Settings=Depends(get_settings)):
    return{
        "App name":app_settings.APP_NAME,
        "App version":app_settings.APP_VERSION
    }

