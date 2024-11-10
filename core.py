from sqlalchemy import select

from core_models import *
from database import get_db_engine

engine = get_db_engine()


print(select(user_table))
print()
# ------------------------------------------------------------------------------------
# Чтобы выполнить `SELECT` из отдельных столбцов с использованием подхода `Core`,
# `Column` доступ к объектам осуществляется из `Table.c` метода доступа,
# и их можно отправлять напрямую; предложение `FROM` будет выведено как набор всех `Table`
# и других `FromClause` объектов, представленных этими столбцами:

print(select(user_table.c.name, user_table.c.fullname))
print()
# -------------------------------------------------------------------------------------
# В качестве альтернативы при использовании `FromClause.c` коллекции `any`, `FromClause`
# например `Table`, можно указать несколько столбцов для a `select()` с помощью списка имен строк:

print(select(user_table.c["name", "fullname"]))
