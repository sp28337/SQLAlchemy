from sqlalchemy import select, func

from core_models import *
from database import get_db_engine

engine = get_db_engine()


# Предыдущие примеры JOIN иллюстрировали, что Select конструкция может объединять две таблицы и автоматически создавать
# предложение ON. Это происходит в этих примерах, поскольку объекты user_table и address_table Table
# включают одно ForeignKey Constraint определение, которое используется для формирования этого предложения ON.
#
# Если левые и правые цели соединения не имеют такого ограничения или есть несколько ограничений,
# нам нужно указать предложение ON напрямую. Оба Select.join() и Select.join_from() принимают дополнительный
# аргумент для предложения ON, который указывается с использованием той же механики SQL Expression,
# которую мы видели в предложении WHERE :

print(
    select(address_table.c.email_address)
    .select_from(user_table)
    .join(address_table, user_table.c.id == address_table.c.user_id)
)

# Совет по ORM — есть другой способ сгенерировать предложение ON при использовании сущностей ORM,
# которые используют конструкцию relationship()
