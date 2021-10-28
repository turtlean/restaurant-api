from pydantic import BaseModel
from datetime import datetime


class RestaurantBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Restaurant(RestaurantBase):
    id: int
    created_at: datetime
    updated_at: datetime


class RestaurantUpdate(RestaurantBase):
    pass


class RestaurantCreate(RestaurantBase):
    pass
