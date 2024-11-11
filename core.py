from sqlalchemy import select

from core_models import *
from database import get_db_engine

engine = get_db_engine()


# Оба метода Select.join() и Select.join_from() принимают аргументы-ключевые слова Select.join.isouter,
# Select.join.full которые отобразят LEFT OUTER JOIN и FULL OUTER JOIN соответственно:

print(select(user_table).join(address_table, isouter=True))
print("-" * 60)
print(select(user_table).join(address_table, full=True))

# Существует также метод Select.outerjoin(), эквивалентный использованию ..join(..., isouter=True)

# В SQL также есть «RIGHT OUTER JOIN». SQLAlchemy не отображает его напрямую;
# вместо этого измените порядок таблиц на обратный и используйте «LEFT OUTER JOIN».
