from sqlalchemy import select, and_, or_

from core_models import *
from database import get_db_engine
from orm_models import Address, User

engine = get_db_engine()


# SQLAlchemy позволяет нам составлять выражения SQL, такие как name = 'squidward' или user_id > 10,
# используя стандартные операторы Python в сочетании с Column и подобными объектами.
# Для булевых выражений большинство операторов Python, таких как ==, >=  >, и т. д.,
# генерируют новые объекты SQL Expression, а не простые булевы значения True/False:

print(user_table.c.name == "squidward")
print(address_table.c.user_id > 10)

print("-" * 60)
# Мы можем использовать подобные выражения для генерации предложения WHERE,
# передавая полученные объекты методу Select.where():

print(select(user_table).where(user_table.c.name == "squidward"))

print("-" * 60)
# Для создания нескольких выражений, объединенных с помощью AND,
# Select.where() метод можно вызывать любое количество раз:

print(
    select(address_table.c.email_address)
    .where(user_table.c.name == "squidward")
    .where(address_table.c.user_id == user_table.c.id)
)

print("-" * 60)
# Один вызов Select.where() также принимает несколько выражений с тем же эффектом:

print(
    select(address_table.c.email_address).where(
        user_table.c.name == "squidward",
        address_table.c.user_id == user_table.c.id,
    )
)

print("-" * 60)
# Союзы «И» и «ИЛИ» доступны напрямую с использованием функций and_()и or_(),
# как показано ниже в ORM:

print(
    select(Address.email_address).where(
        and_(
            or_(User.name == "squidward", User.name == "sandy"),
            Address.user_id == User.id,
        )
    )
)

print("-" * 60)
# Для простых сравнений «равенства» с одной сущностью также существует популярный метод, известный как
# Select.filter_by(), который принимает ключевые аргументы, соответствующие ключам столбцов или именам атрибутов ORM.
# Он будет фильтровать по самому левому выражению FROM или последней присоединенной сущности:

print(select(User).filter_by(name="spongebob", fullname="Spongebob Squarepants"))
