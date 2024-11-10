from sqlalchemy import insert, select, bindparam

from core_models import *
from database import get_db_engine

engine = get_db_engine()

insert_stmt = insert(address_table).returning(
    address_table.c.id, address_table.c.email_address
)
print(insert_stmt)
