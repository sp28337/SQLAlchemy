from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine('sqlite:///database.db', echo=True)


class Base(DeclarativeBase):
    pass


class ORMBase(DeclarativeBase):
    pass


def get_db_engine():
    return engine


def get_db_session():
    return Session(bind=engine)
