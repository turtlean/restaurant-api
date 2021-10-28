from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from . import crud
from .schemas import RestaurantCreate, Restaurant

router = APIRouter()


@router.get("/restaurants/")
def get_restaurants(db: Session = Depends(get_db)):
    return {"restaurants": []}


@router.post("/restaurant/", response_model=Restaurant)
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return crud.create_restaurant(db, restaurant)
