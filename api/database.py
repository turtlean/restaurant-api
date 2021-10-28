from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from pydantic import PostgresDsn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import func
from fastapi.encoders import jsonable_encoder

from config import settings

SQLALCHEMY_DATABASE_URL = PostgresDsn.build(
    scheme="postgresql",
    host=settings.POSTGRES_HOST,
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    path=f"/{settings.POSTGRES_DB}",
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
