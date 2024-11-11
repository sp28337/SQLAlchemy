from sqlalchemy import select

from core_models import *
from database import get_db_engine
from orm_models import User

engine = get_db_engine()


# Предложение ORDER BY строится в терминах конструкций SQL Expression, которые обычно основаны на Column
# или похожих объектах. Select.order_by() Метод принимает одно или несколько из этих выражений позиционно:

print(select(user_table).order_by(user_table.c.name))

print("-" * 60)

# Сортировка по возрастанию/убыванию доступна из модификаторов ColumnElement.asc() и ColumnElement.desc(),
# которые также присутствуют в атрибутах, связанных с ORM:

print(select(User).order_by(User.fullname.desc()))

# Приведенный выше оператор выдаст строки, отсортированные по user_account.fullname столбцу в порядке убывания.
