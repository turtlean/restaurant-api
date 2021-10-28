from sqlalchemy.orm import Session

from . import models, schemas
from .schemas import RestaurantCreate


def get_restaurants(db: Session):
    return db.query(models.Restaurant).all()


def create_restaurant(db: Session, restaurant: RestaurantCreate):
    db_restaurant = models.Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant
