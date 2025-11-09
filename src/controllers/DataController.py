from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):

    def __init__(self):
        super().__init__()

        self.MB_SIZE = 1024 * 1024

    def validate_file(self, file: UploadFile):
        """Check file type and size"""
        file_type = file.content_type
        file_size = file.size

        if file_type not in self.app_settings.ALLOWED_FILE_TYPE:
            return False, "invalid type"
        
        if file_size > self.app_settings.MAX_FILE_SIZE_MB * self.MB_SIZE:
            return False, "size is bigger than 25mb"
        
        return True, "File Is Valid"