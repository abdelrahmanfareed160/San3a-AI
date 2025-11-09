from fastapi import APIRouter, Depends, status, UploadFile
from fastapi.responses import JSONResponse
from helpers import get_settings, Settings
from controllers import DataController


data_router = APIRouter(
    prefix=("/ai/v1"),
    tags=['data']
)

@data_router.post("/data/{project_id}")
async def upload_file(project_id: str, file: UploadFile,
                      app_settings: Settings=Depends(get_settings)):
    
    # عايزين هنا نتاكد ان الفايل مطابق المواصفات وبعد كدههنعدل على اسمه ونرفعه 
    # اللوجيك في الكنترولر
    # الثوابت في الموديلز
    # الملفات في الاسيتس
    pass