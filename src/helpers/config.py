from pydantic_settings import BaseSettings, SettingsConfigDict

# check env variables data type
class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    ALLOWED_FILE_TYPE: list
    MAX_FILE_SIZE_MB: int

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()