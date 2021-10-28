from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from . import crud
from .schemas import RestaurantCreate, Restaurant, RestaurantUpdate

router = APIRouter()


@router.get("/restaurants/", response_model=List[Restaurant])
def get_restaurants(db: Session = Depends(get_db)):
    return crud.get_restaurants(db)


@router.get("/restaurants/{restaurant_id}", response_model=Restaurant)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@router.post("/restaurants/", response_model=Restaurant)
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant_by_name(db, name=restaurant.name)
    if db_restaurant:
        raise HTTPException(status_code=400, detail="Restaurant already registered")
    return crud.create_restaurant(db, restaurant)


@router.put("/restaurants/{restaurant_id}", response_model=Restaurant)
def update_restaurant(
    restaurant_id: int, restaurant: RestaurantUpdate, db: Session = Depends(get_db)
):
    db_restaurant = crud.get_restaurant(db, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return crud.update_restaurant(db, restaurant_id, restaurant)


@router.delete("/restaurants/{restaurant_id}", response_model=Restaurant)
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return crud.delete_restaurant(db, restaurant_id)
