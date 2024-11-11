from sqlalchemy import select, func, desc

from database import get_db_engine
from orm_models import Address

engine = get_db_engine()


# Важной методикой, в частности, в некоторых бэкэндах баз данных, является возможность ORDER BY или GROUP BY выражения,
# которое уже указано в предложении columns, без повторного указания выражения в предложении ORDER BY или GROUP BY
# и вместо этого использования имени столбца или помеченного имени из предложения COLUMNS.
# Эта форма доступна путем передачи строкового текста имени в метод Select.order_by() or Select.group_by().
# Переданный текст не отображается напрямую; вместо этого имя, данное выражению в предложении columns,
# отображается как имя этого выражения в контексте, вызывая ошибку, если совпадение не найдено.
# Унарные модификаторы asc() and desc() также могут использоваться в этой форме:

stmt = (
    select(Address.user_id, func.count(Address.id).label("num_addresses"))
    .group_by("user_id")
    .order_by("user_id", desc("num_addresses"))
)
print(stmt)
