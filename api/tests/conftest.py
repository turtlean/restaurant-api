import pytest

from fastapi.testclient import TestClient
from sqlalchemy.engine import Connection

from database import engine, SessionLocal
from main import app
from restaurant import models


def clean_db(conn=Connection(engine)):
    for tbl in reversed(models.BaseModel.metadata.sorted_tables):
        engine.execute(tbl.delete())


@pytest.fixture(autouse=True)
def setup():
    clean_db()
    client = TestClient(app)
    session = SessionLocal()
    yield {
        "app": client,
        "db": session,
    }
    session.close()
