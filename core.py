from sqlalchemy import select, cast, String, JSON

from core_models import user_table
from database import get_db_engine

engine = get_db_engine()

# В SQL нам часто требуется явно указать тип данных выражения, либо чтобы сообщить базе данных,
# какой тип ожидается в иначе неоднозначном выражении, либо в некоторых случаях, когда мы хотим преобразовать
# подразумеваемый тип данных выражения SQL во что-то другое. Для этой задачи используется ключевое слово SQL CAST,
# которое в SQLAlchemy предоставляется функцией cast(). Эта функция принимает выражение столбца и объект типа
# данных в качестве аргументов, как показано ниже, где мы создаем выражение SQL из объекта столбца
# :CAST(user_account.id AS VARCHAR)user_table.c.id

stmt = select(cast(user_table.c.id, String))
with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())

print("-" * 60)
# Функция cast() не только отображает синтаксис SQL CAST, она также создает выражение столбца SQLAlchemy,
# которое будет действовать как заданный тип данных на стороне Python. Строковое выражение, которое должно cast()
# получить JSON индекс JSON и операторы сравнения, например:

print(cast("{'a': 'b'}", JSON)["a"])

