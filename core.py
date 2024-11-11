from sqlalchemy import select

from core_models import *
from database import get_db_engine, get_db_session
from orm_models import User, Address

engine = get_db_engine()


with get_db_session() as session:

    # Метод ColumnElement.label(), а также одноименный метод, доступный в атрибутах ORM, предоставляет label
    # SQL столбца или выражения, позволяя ему иметь определенное имя в результирующем наборе.
    # Это может быть полезно при ссылке на произвольные выражения SQL в строке результата по имени:

    stmt = select(
        ("Username: " + user_table.c.name).label("username"),
    ).order_by(user_table.c.name)
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(f"{row.username}")
