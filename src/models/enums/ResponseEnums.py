from enum import Enum

class ResponseSignal(Enum):

    # unsucccess
    FILE_SIZE_INVALID = "File Size exceeded the maximum size"
    FILE_TYPE_INVALID = "Invalid file type"
    FILE_UPLOAD_FAIL = "File uploading failed"

    # success
    FILE_IS_VALID = "File is valid"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"