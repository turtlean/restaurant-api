from fastapi import FastAPI

from database import engine
from restaurant import router, models

app = FastAPI()

models.BaseModel.metadata.create_all(bind=engine)

app.include_router(router.router, prefix="/api", tags=["Restaurants"])


@app.get(
    "/",
    name="Info",
    description="Basic info about **Restaurants API**",
    tags=["Root"],
)
async def root():
    return {
        "name": "Restaurants API",
        "description": "Simple CRUD API for Restaurants",
        "version": "1.0.0",
    }
