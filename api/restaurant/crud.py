from sqlalchemy.orm import Session

from . import models, schemas
from .schemas import RestaurantCreate, RestaurantUpdate


def get_restaurants(db: Session):
    return db.query(models.Restaurant).all()


def get_restaurant(db: Session, id: int):
    return db.query(models.Restaurant).get(id)


def get_restaurant_by_name(db: Session, name: str):
    return db.query(models.Restaurant).filter(models.Restaurant.name == name).first()


def create_restaurant(db: Session, restaurant: RestaurantCreate):
    db_restaurant = models.Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


def update_restaurant(db: Session, id: int, restaurant: RestaurantUpdate):
    db_restaurant = get_restaurant(db, id)
    if (db_restaurant.name) != restaurant.name:
        db_restaurant.name = restaurant.name
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
    return db_restaurant


def delete_restaurant(db: Session, id: int):
    db_restaurant = get_restaurant(db, id)
    db.delete(db_restaurant)
    db.commit()
    return db_restaurant
