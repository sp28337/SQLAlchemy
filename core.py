from sqlalchemy import update

from core_models import user_table
from database import get_db_engine

engine = get_db_engine()

# Оба Update и Delete поддерживают возможность возвращать количество сопоставленных строк после выполнения оператора
# для операторов, которые вызываются с помощью Core Connection, т. е Connection.execute(). Согласно указанным ниже
# предостережениям, это значение доступно из CursorResult.rowcount атрибута:

with engine.begin() as conn:
    result = conn.execute(
        update(user_table)
        .values(fullname="Patrick McStar")
        .where(user_table.c.name == "patrick")
    )
    print(result.rowcount)
