import pathlib
from typing import List, Union

from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STRING: str = "/api/v1"
    OPENAI_API_KEY: str

    BACKEND_CORS_ORIGIN: List[str] = [
        "http://localhost:3000",
        "http://localhost:8001"
    ]

settings = Settings()