from sqlalchemy import select
from sqlalchemy.orm import Session

from core_models import *
from database import get_db_engine
from orm_models import User

engine = get_db_engine()

stmt = select(user_table).where(user_table.c.name == "spongebob")

print(stmt)
print()

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print()
        print(row)
        print()
# ---------------------------------------------------------------------------------------------------------------------
# При использовании ORM, особенно с select()конструкцией, составленной на основе сущностей ORM,
# нам нужно будет выполнить ее с помощью Session.execute()метода в Session; используя этот подход,
# мы продолжаем получать Row объекты из результата, однако эти строки теперь могут включать в себя полные сущности,
# такие как экземпляры класса User, как отдельные элементы в каждой строке:

stmt = select(User).where(User.name == "spongebob")
with Session(engine) as session:
    for row in session.execute(stmt):
        print()
        print(row)
        print()
