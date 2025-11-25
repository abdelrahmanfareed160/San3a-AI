from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    
    MODEL_NAME: str

    QDRANT_API_URL: str
    QDRANT_API_KEY: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
