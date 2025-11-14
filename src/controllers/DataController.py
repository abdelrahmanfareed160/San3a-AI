from .BaseController import BaseController
from fastapi import UploadFile, status
from models import ResponseSignal
from models import FunctionsMap
import pandas as pd

class DataController(BaseController):

    def __init__(self):
        super().__init__()

        self.MB_SIZE = 1024 * 1024

    def validate_file(self, file: UploadFile):
        """Check file type and size"""
        file_type = file.content_type
        file_size = file.size

        if file_type not in self.app_settings.ALLOWED_FILE_TYPE:
            return False, ResponseSignal.FILE_TYPE_INVALID.value, status.HTTP_400_BAD_REQUEST
        
        if file_size > self.app_settings.MAX_FILE_SIZE_MB * self.MB_SIZE:
            return False, ResponseSignal.FILE_SIZE_INVALID.value, status.HTTP_400_BAD_REQUEST
        
        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value, status.HTTP_200_OK
    
    
    def embedd_data(self, file: UploadFile):
        """Convert data into embeddings and upload it on qdrant"""
    
