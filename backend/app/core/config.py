import pathlib

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STRING: str = "/api/v1"
    OPENAI_API_KEY: str

settings = Settings()