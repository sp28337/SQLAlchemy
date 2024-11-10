from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db', echo=True)


def get_db_engine():
    return engine
