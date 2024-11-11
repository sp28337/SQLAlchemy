from sqlalchemy import delete

from core_models import user_table

# Функция delete() генерирует новый экземпляр Delete, представляющий оператор DELETE в SQL,
# который удаляет строки из таблицы.
#
# С точки зрения API оператор delete() очень похож на конструкцию update(), традиционно не возвращающую строк,
# но допускающую вариант RETURNING на некоторых бэкэндах баз данных.

stmt = delete(user_table).where(user_table.c.name == "patrick")
print(stmt)

