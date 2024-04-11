from pathlib import Path

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api_v1.api import api_router


app = FastAPI(title="Simple API", openapi_url=f"{settings.API_V1_STRING}/openapi.json")

root_router = APIRouter()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGIN:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGIN,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

@root_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET content
    """
    return {"msg": "Hello World"}

app.include_router(api_router, prefix=settings.API_V1_STRING)
app.include_router(root_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")