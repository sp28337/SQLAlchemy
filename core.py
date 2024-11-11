from sqlalchemy import select, text, literal_column

from core_models import *
from database import get_db_engine

engine = get_db_engine()

stmt = select(text("'test'"), user_table.c.name).group_by(user_table.c.name)

with engine.connect() as conn:
    print(conn.execute(stmt).all())

print("-" * 60)

stmt = select(literal_column("'some phrase'").label("p"), user_table.c.name).order_by(
    user_table.c.name)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.p}, {row.name}")
