from sqlalchemy import select, func

from core_models import address_table, user_table
from database import get_db_engine

engine = get_db_engine()

# Распространенной функцией, используемой с оконными функциями, является row_number() функция,
# которая просто подсчитывает строки. Мы можем разделить это количество строк на имя пользователя,
# чтобы подсчитать адреса электронной почты отдельных пользователей:

stmt = (
    select(
        func.row_number().over(partition_by=user_table.c.name),
        user_table.c.name,
        address_table.c.email_address,
    )
    .select_from(user_table)
    .join(address_table)
)
print(stmt)
print("-" * 60)

with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())

# Выше FunctionElement.over.partition_by параметр используется для того, чтобы предложение было отображено внутри
# предложения OVER. Мы также можем использовать предложение,
# используя :PARTITION BY ORDER BY FunctionElement.over.order_by
print("-" * 60)

stmt = (
    select(
        func.count().over(order_by=user_table.c.name),
        user_table.c.name,
        address_table.c.email_address,
    )
    .select_from(user_table)
    .join(address_table)
)
with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())