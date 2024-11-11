from sqlalchemy import select, func

from core_models import address_table, user_table
from database import get_db_engine

engine = get_db_engine()

# функция count(), агрегатная функция, которая подсчитывает количество возвращаемых строк:

print(select(func.count()).select_from(user_table))

print("-" * 60)
# функция lower(), строковая функция, преобразующая строку в нижний регистр:

print(select(func.lower("A String With Much UPPERCASE")))

print("." * 60)
# функция now(), которая предоставляет текущую дату и время; поскольку это общая функция, SQLAlchemy знает,
# как отображать ее по-разному для каждого бэкэнда, в случае SQLite используется функция CURRENT_TIMESTAMP:

stmt = select(func.now())
with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())

print("_" * 60)
# Поскольку большинство бэкендов баз данных содержат десятки, если не сотни различных функций SQL, func
# старается быть максимально либеральным в том, что он принимает. Любое имя, к которому осуществляется доступ
# из этого пространства имен, автоматически считается функцией SQL, которая будет отображаться в общем виде:

print(select(func.some_crazy_function(user_table.c.name, 17)))
