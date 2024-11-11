from sqlalchemy import delete
from sqlalchemy.dialects import mysql

from core_models import user_table, address_table

# Как и Update, Delete поддерживает использование коррелированных подзапросов в предложении WHERE,
# а также специфичные для бэкэнда многотабличные синтаксисы, например, в MySQL:DELETE FROM..USING

delete_stmt = (
    delete(user_table)
    .where(user_table.c.id == address_table.c.user_id)
    .where(address_table.c.email_address == "patrick@aol.com")
)

print(delete_stmt.compile(dialect=mysql.dialect()))
