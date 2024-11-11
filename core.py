from sqlalchemy import update, delete

from core_models import user_table
from database import get_db_engine

engine = get_db_engine()

# Как и Insert конструкция, Updateа Delete также поддерживают предложение RETURNING, которое добавляется с помощью
# методов Update.returning() и Delete.returning(). Когда эти методы используются на бэкэнде, поддерживающем RETURNING,
# выбранные столбцы из всех строк, которые соответствуют критериям WHERE оператора,
# будут возвращены в Result объекте как строки, которые можно итерировать:

update_stmt = (
    update(user_table)
    .where(user_table.c.name == "patrick")
    .values(fullname="Patrick the Star")
    .returning(user_table.c.id, user_table.c.name)
)

print(update_stmt)


delete_stmt = (
    delete(user_table)
    .where(user_table.c.name == "patrick")
    .returning(user_table.c.id, user_table.c.name)
)

print(delete_stmt)
