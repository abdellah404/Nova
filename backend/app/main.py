from fastapi import FastAPI

from database import Base, engine
from models.field import Field
from routers.fields import router as fields_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AgriWater AI API",
    version="0.1.0",
    docs_url=None,
redoc_url=None,
openapi_url=None
)


app.include_router(fields_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "agriwater-api",
    }