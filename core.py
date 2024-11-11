from sqlalchemy import select, union_all

from core_models import address_table, user_table
from database import get_db_engine

engine = get_db_engine()

# В SQL операторы SELECT могут быть объединены вместе с помощью операции UNION или UNION ALL SQL,
# которая создает набор всех строк, созданных одним или несколькими операторами вместе.
# Также возможны другие операции над множествами, такие как INTERSECT [ALL] и EXCEPT [ALL].
#
# Конструкция SQLAlchemy Select поддерживает композиции такого рода с использованием таких функций,
# как union(), intersect() и except_(), а также «всех» аналогов union_all(), intersect_all() и except_all().
# Все эти функции принимают произвольное количество подвыбираемых элементов, которые обычно являются
# Select конструкциями, но также могут быть существующей композицией.
#
# Конструкция, созданная этими функциями, — это CompoundSelect, которая используется таким же образом,
# как и Select конструкция, за исключением того, что у нее меньше методов. CompoundSelect Созданная,
# union_all() например, может быть вызвана напрямую с помощью Connection.execute():

stmt1 = select(user_table).where(user_table.c.name == "sandy")
stmt2 = select(user_table).where(user_table.c.name == "spongebob")
u = union_all(stmt1, stmt2)
with engine.connect() as conn:
    result = conn.execute(u)
    print(result.all())

print("---" * 20)
# Чтобы использовать CompoundSelect в качестве подзапроса, как и в Select случае с SelectBase.subquery() методом,
# который создаст Subquery объект с FromClause.c коллекцией, на которую можно ссылаться во вложенном select():

u_subq = u.subquery()
stmt = (
    select(u_subq.c.name, address_table.c.email_address)
    .join_from(address_table, u_subq)
    .order_by(u_subq.c.name, address_table.c.email_address)
)
with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())
