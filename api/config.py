from pydantic import (
    BaseSettings,
)


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_DB_TEST: str


settings = Settings()
