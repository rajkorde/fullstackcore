import pathlib

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STRING: str = "/api/v1"

settings = Settings()

settings.API_V1_STRING