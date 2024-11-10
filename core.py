from sqlalchemy import insert, select, bindparam

from core_models import *
from database import get_db_engine

engine = get_db_engine()

scalar_subq = (
    select(user_table.c.id)
    .where(user_table.c.name is bindparam("username"))
    .scalar_subquery()
)

with engine.connect() as conn:
    result = conn.execute(
        insert(address_table).values(user_id=scalar_subq),
        [
            {
                "username": "spongebob",
                "email_address": "spongebob@sqlalchemy.org",
            },
            {
                "username": "sandy",
                "email_address": "sandy@sqlalchemy.org"
            },
            {
                "username": "sandy",
                "email_address": "sandy@squirrelpower.org"},
        ],
    )
    # conn.commit()

# print(insert(user_table).values().compile(engine)) - insert default values
