from sqlalchemy.orm import Session

from . import models, schemas
from .schemas import RestaurantCreate


def get_restaurants(db: Session):
    return db.query(models.Restaurant).all()


def get_restaurant(db: Session, id: int):
    return db.query(models.Restaurant).filter(models.Restaurant.id == id).first()


def get_restaurant_by_name(db: Session, name: str):
    return db.query(models.Restaurant).filter(models.Restaurant.name == name).first()


def create_restaurant(db: Session, restaurant: RestaurantCreate):
    db_restaurant = models.Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant
