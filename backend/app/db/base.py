from sqlalchemy import create_engine, engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


import os
from sqlalchemy.engine.url import URL

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg2://todo:todo@localhost:5432/todo"
)
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# docker compose -d
