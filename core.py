from sqlalchemy import select
from sqlalchemy.orm import aliased
from database import get_db_session
from orm_models import Address, User


# В ORM aliased() конструкция может использоваться для связывания сущности ORM, такой как наш User или Address класс,
# с любой FromClause концепцией, которая представляет источник строк. Предыдущий раздел Псевдонимы сущностей ORM
# иллюстрирует использование aliased() для связывания сопоставленного класса с Alias его сопоставленным Table.
# Здесь мы иллюстрируем aliased() выполнение того же действия как против , Subquery так и CTE против
# сгенерированного против Select конструкции, которая в конечном итоге выводится из того же сопоставленного Table.
#
# Ниже приведен пример применения aliased() к Subquery конструкции, чтобы сущности ORM могли быть извлечены из ее строк.
# Результат показывает ряд объектов User и Address, где данные для каждого Address объекта в конечном итоге были
# получены из подзапроса к address таблице, а не из этой таблицы напрямую:

subq = select(Address).where(~Address.email_address.like("%@aol.com")).subquery()
address_subq = aliased(Address, subq)
stmt = (
    select(User, address_subq)
    .join_from(User, address_subq)
    .order_by(User.id, address_subq.id)
)
with get_db_session() as session:
    for user, address in session.execute(stmt):
        print(f"{user} {address}")

print("-" * 60)
# Далее следует еще один пример, который абсолютно такой же, за исключением того,
# что вместо этого используется конструкция CTE:

cte_obj = select(Address).where(~Address.email_address.like("%@aol.com")).cte()
address_cte = aliased(Address, cte_obj)
stmt = (
    select(User, address_cte)
    .join_from(User, address_cte)
    .order_by(User.id, address_cte.id)
)
with get_db_session() as session:
    for user, address in session.execute(stmt):
        print(f"{user} {address}")
