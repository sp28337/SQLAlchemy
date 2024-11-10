from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine('sqlite:///database.db', echo=True)


class Base(DeclarativeBase):
    pass


class ORMBase(DeclarativeBase):
    pass


def get_db_engine():
    return engine
