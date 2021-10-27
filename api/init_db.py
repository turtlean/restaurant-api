import sqlalchemy

from config import settings

engine = sqlalchemy.create_engine(
    f"postgresql://{settings.POSTGRES_USER}"
    f":{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}/postgres"
)
connection = engine.connect()
connection.execute("commit")

# Query for existing databases
existing_databases = connection.execute("SELECT datname FROM pg_database;")
# Results are a list of single item tuples, so unpack each tuple
existing_databases = [
    d[0]
    for d in existing_databases
    # avoid trying to delete templates & default postgres db
    if d[0] != "postgres" and "template" not in d[0]
]

if not existing_databases:
    connection.execute(f"CREATE DATABASE {settings.POSTGRES_DB}")
    connection.execute("commit")
    print(f"Created database {settings.POSTGRES_DB}")
