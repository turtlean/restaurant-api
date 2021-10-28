from sqlalchemy.orm import Session
from restaurant import models, schemas


def create_restaurant(setup: Session, restaurant: schemas.RestaurantBase):
    db_restaurant = models.Restaurant(**restaurant.dict())
    setup["db"].add(db_restaurant)
    setup["db"].commit()
    setup["db"].refresh(db_restaurant)
    return db_restaurant


def test_get_restaurants(setup):
    create_restaurant(setup, schemas.RestaurantCreate(name="Tasty food"))

    response_json = setup["app"].get("/api/restaurants/").json()

    assert len(response_json) == 1 and response_json[0]["name"] == "Tasty food"


def test_create_restaurant(setup):
    data = {"name": "New restaurant"}

    response_json = setup["app"].post("/api/restaurants/", json=data).json()

    db_restaurants = setup["db"].query(models.Restaurant).all()
    assert len(db_restaurants) == 1 and db_restaurants[0].name == "New restaurant"
    assert response_json["name"] == "New restaurant"


def test_get_error_when_restaurant_already_registered(setup):
    data = {"name": "New restaurant"}
    create_restaurant(setup, schemas.RestaurantCreate(**data))

    response = setup["app"].post("/api/restaurants/", json=data)

    assert response.status_code == 400


def test_get_restaurant(setup):
    db_restaurant = create_restaurant(
        setup, schemas.RestaurantCreate(name="Tasty food")
    )
    response_json = setup["app"].get(f"/api/restaurants/{db_restaurant.id}").json()

    assert (
        response_json["id"] == db_restaurant.id
        and response_json["name"] == "Tasty food"
    )


def test_get_error_when_restaurant_is_not_registered(setup):
    response = setup["app"].get(f"/api/restaurants/1")

    assert response.status_code == 404
