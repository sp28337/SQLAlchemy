from sqlalchemy import select, func

from core_models import address_table, user_table
from database import get_db_engine

engine = get_db_engine()


# Использование конструкции CTE в SQLAlchemy практически тоже самое что и использование конструкции Subquery.
# Изменив вызов метода Select.subquery(), чтобы использовать Select.cte() вместо этого, мы можем использовать
# полученный объект как элемент FROM таким же образом, но отображаемый SQL — это совсем другой синтаксис.
# общего табличного выражения:

subq = (
    select(func.count(address_table.c.id).label("count"), address_table.c.user_id)
    .group_by(address_table.c.user_id)
    .cte()
)

stmt = select(user_table.c.name, user_table.c.fullname, subq.c.count).join_from(
    user_table, subq
)

print(stmt)

# Конструкция CTE также может использоваться в «рекурсивном» стиле и в более сложных случаях может быть составлена
# из предложения RETURNING оператора INSERT, UPDATE или DELETE. Строка документации для CTE включает подробности об
# этих дополнительных шаблонах.
#
# В обоих случаях Subquery и CTE были названы на уровне SQL с использованием «анонимного» имени.
# В коде Python нам вообще не нужно предоставлять эти имена. Идентификатор объекта экземпляров Subquery or CTE
# служит синтаксическим идентификатором объекта при рендеринге. Имя, которое будет отображено в SQL, можно предоставить,
# передав его в качестве первого аргумента методов Select.subquery() or Select.cte().
