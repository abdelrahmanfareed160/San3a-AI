from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):

    def __init__(self):
        super().__init__()


    def validate_file(self, file: UploadFile):
        """Check file type and size"""
        pass