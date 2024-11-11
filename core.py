from sqlalchemy import update, select

from core_models import user_table, address_table
from database import get_db_engine

engine = get_db_engine()


# Оператор UPDATE может использовать строки в других таблицах с помощью коррелированного подзапроса.
# Подзапрос может использоваться в любом месте, где может быть размещено выражение столбца:

scalar_subq = (
    select(address_table.c.email_address)
    .where(address_table.c.user_id == user_table.c.id)
    .order_by(address_table.c.id)
    .limit(1)
    .scalar_subquery()
)
print(scalar_subq)

print("-" * 60)

update_stmt = update(user_table).values(fullname=scalar_subq)
print(update_stmt)
