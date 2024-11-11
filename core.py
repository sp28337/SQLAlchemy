from sqlalchemy import select
from sqlalchemy.orm import aliased

from database import get_db_engine
from orm_models import Address, User

engine = get_db_engine()


# Эквивалентом ORM метода FromClause.alias() является функция ORM aliased(), которая может быть применена к сущности,
# такой как User и Address. Это создает Alias объект внутри, который находится против исходного сопоставленного
# Table объекта, сохраняя при этом функциональность ORM. SELECT ниже выбирает из User сущности все объекты,
# которые включают два конкретных адреса электронной почты:

address_alias_1 = aliased(Address)
address_alias_2 = aliased(Address)
print(
    select(User)
    .join_from(User, address_alias_1)
    .where(address_alias_1.email_address == "patrick@aol.com")
    .join_from(User, address_alias_2)
    .where(address_alias_2.email_address == "patrick@gmail.com")
)
