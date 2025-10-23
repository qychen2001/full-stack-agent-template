from fastapi import FastAPI

from app import register_routers
from settings import settings

app = FastAPI()

register_routers(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level,
    )
