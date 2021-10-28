from fastapi import FastAPI

from database import engine
from restaurant import router, models

app = FastAPI()

models.BaseModel.metadata.create_all(bind=engine)

app.include_router(router.router, prefix="/api", tags=["restaurant"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
