from sqlalchemy import select, func

from core_models import address_table, user_table
from database import get_db_engine

engine = get_db_engine()

# Ключевое слово SQL EXISTS — это оператор, который используется со скалярными подзапросами для возврата
# логического значения true или false в зависимости от того, вернет ли оператор SELECT строку.
# SQLAlchemy включает вариант объекта, ScalarSelect называемый Exists, который будет генерировать
# подзапрос EXISTS и наиболее удобно генерируется с помощью SelectBase.exists() метода.
# Ниже мы создаем EXISTS, чтобы мы могли возвращать user_account строки, которые имеют более одной связанной
# строки в address:

subq = (
    select(func.count(address_table.c.id))
    .where(user_table.c.id == address_table.c.user_id)
    .group_by(address_table.c.user_id)
    .having(func.count(address_table.c.id) > 1)
).exists()
with engine.connect() as conn:
    result = conn.execute(select(user_table.c.name).where(subq))
    print(result.all())

print("-" * 60)
# Конструкция EXISTS чаще всего используется как отрицание, например NOT EXISTS, поскольку она обеспечивает
# SQL-эффективную форму поиска строк, для которых в связанной таблице нет строк. Ниже мы выбираем имена пользователей,
# у которых нет адресов электронной почты; обратите внимание на бинарный оператор отрицания ( ~), используемый внутри
# второго предложения WHERE:

subq = (
    select(address_table.c.id).where(user_table.c.id == address_table.c.user_id)
).exists()
with engine.connect() as conn:
    result = conn.execute(select(user_table.c.name).where(~subq))
    print(result.all())