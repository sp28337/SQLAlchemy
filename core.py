from sqlalchemy import update, select
from sqlalchemy.dialects import mysql

from core_models import user_table, address_table
from database import get_db_engine

engine = get_db_engine()


# Некоторые базы данных, такие как PostgreSQL и MySQL, поддерживают синтаксис «UPDATE FROM», где дополнительные
# таблицы могут быть указаны непосредственно в специальном предложении FROM. Этот синтаксис будет сгенерирован неявно,
# когда дополнительные таблицы находятся в предложении WHERE оператора:

update_stmt = (
    update(user_table)
    .where(user_table.c.id == address_table.c.user_id)
    .where(address_table.c.email_address == "patrick@aol.com")
    .values(fullname="Pat")
)
print(update_stmt)

print("-" * 60)
# Также есть синтаксис MySQL, который может ОБНОВЛЯТЬ несколько таблиц. Для этого требуется, чтобы мы ссылались
# на Table объекты в предложении VALUES, чтобы ссылаться на дополнительные таблицы:

update_stmt = (
    update(user_table)
    .where(user_table.c.id == address_table.c.user_id)
    .where(address_table.c.email_address == "patrick@aol.com")
    .values(
        {
            user_table.c.fullname: "Pat",
            address_table.c.email_address: "pat@aol.com",
        }
    )
)
print(update_stmt.compile(dialect=mysql.dialect()))
