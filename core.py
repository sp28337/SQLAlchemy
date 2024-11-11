from sqlalchemy import update, bindparam

from core_models import user_table
from database import get_db_engine

engine = get_db_engine()


# Базовое ОБНОВЛЕНИЕ выглядит так:

stmt = (
    update(user_table)
    .where(user_table.c.name == "patrick")
    .values(fullname="Patrick the Star")
)
print(stmt)

# Метод Update.values() управляет содержимым элементов SET оператора UPDATE. Это тот же метод, который используется
# конструкцией Insert. Параметры обычно можно передавать с использованием имен столбцов в качестве ключевых аргументов.
print("-" * 60)
# UPDATE поддерживает все основные формы SQL UPDATE, включая обновления по выражениям,
# где мы можем использовать Column выражения:

stmt = update(user_table).values(fullname="Username: " + user_table.c.name)
print(stmt)

print("-" * 60)
# Для поддержки UPDATE в контексте «executemany», где для одного и того же оператора будет вызываться множество
# наборов параметров, bindparam() можно использовать конструкцию для настройки связанных параметров;
# они заменяют места, где обычно располагаются литеральные значения:

stmt = (
    update(user_table)
    .where(user_table.c.name == bindparam("oldname"))
    .values(name=bindparam("newname"))
)
with engine.begin() as conn:
    conn.execute(
        stmt,
        [
            {"oldname": "jack", "newname": "ed"},
            {"oldname": "wendy", "newname": "mary"},
            {"oldname": "jim", "newname": "jake"},
        ],
    )
