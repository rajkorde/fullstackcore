import pathlib
from typing import List, Union

from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STRING: str = "/api/v1"
    OPENAI_API_KEY: str

    BACKEND_CORS_ORIGIN: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8001"
    ]

    # @validator("BACKEND_CORS_ORIGINS", pre=True)
    # def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
    #     if isinstance(v, str) and not v.startswith("["):
    #         return [i.strip() for i in v.split(",")]
    #     elif isinstance(v, (list, str)):
    #         return v
    #     raise ValueError(v)

settings = Settings()