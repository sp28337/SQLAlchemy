from sqlalchemy import select

from core_models import user_table
from database import get_db_engine

engine = get_db_engine()


# Теперь, когда мы выбираем из нескольких таблиц и используем соединения, мы быстро сталкиваемся со случаем,
# когда нам нужно ссылаться на одну и ту же таблицу несколько раз в предложении FROM оператора.
# Мы делаем это с помощью псевдонимов SQL , которые представляют собой синтаксис, предоставляющий
# альтернативное имя таблице или подзапросу, из которого на него можно ссылаться в операторе.
#
# В языке выражений SQLAlchemy эти «имена» представлены FromClause объектами, известными как Alias,
# которые создаются в Core с помощью FromClause.alias() метода. Alias похож на Table тем,
# что у него также есть пространство имен Column объектов в Alias.c.collection.
# Например, оператор SELECT ниже возвращает все уникальные пары имен пользователей:

user_alias_1 = user_table.alias()
user_alias_2 = user_table.alias()
print(
    select(user_alias_1.c.name, user_alias_2.c.name).join_from(
        user_alias_1, user_alias_2, user_alias_1.c.id > user_alias_2.c.id
    )
)
