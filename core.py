from sqlalchemy import select, union_all
from sqlalchemy.orm import aliased
from database import get_db_session
from orm_models import User

# Предыдущие примеры иллюстрировали, как построить UNION для двух Tableо бъектов, чтобы затем
# вернуть строки базы данных. Если мы хотим использовать UNION или другую операцию над множествами для выбора строк,
# которые затем получаем как объекты ORM, есть два подхода, которые можно использовать.
# В обоих случаях мы сначала создаем объект select() or CompoundSelect, который представляет
# оператор SELECT / UNION / etc, который мы хотим выполнить; этот оператор должен быть составлен против
# целевых сущностей ORM или их базовых сопоставленных Tableо бъектов:

stmt1 = select(User).where(User.name == "sandy")
stmt2 = select(User).where(User.name == "spongebob")
u = union_all(stmt1, stmt2)

print(stmt1, stmt2, u, sep='\n\n')

print("-" * 60)
# Для простого SELECT с UNION, который еще не вложен в подзапрос, их часто можно использовать в контексте извлечения
# объектов ORM с помощью Select.from_statement() метода. При таком подходе оператор UNION представляет весь запрос;
# после Select.from_statement()использования не может быть добавлено никаких дополнительных критериев:

orm_stmt = select(User).from_statement(u)

print("-" * 60)
with get_db_session() as session:
    for obj in session.execute(orm_stmt).scalars():
        print(obj)

print("_" * 60)
# Чтобы использовать UNION или другую конструкцию, связанную с множеством, в качестве компонента,
# связанного с сущностью, более гибко, CompoundSelect конструкция может быть организована в подзапрос
# с использованием CompoundSelect.subquery(), который затем связывается с объектами ORM с помощью
# aliased() функции. Это работает так же, как представлено в ORM Entity Subqueries/CTE, чтобы
# сначала создать ad hoc «отображение» нашей желаемой сущности в подзапрос, а затем выбрать из этой новой сущности,
# как если бы это был любой другой отображенный класс. В примере ниже мы можем добавить дополнительные критерии,
# такие как ORDER BY, за пределами самого UNION, поскольку мы можем фильтровать или упорядочивать по столбцам,
# экспортированным подзапросом:

user_alias = aliased(User, u.subquery())
orm_stmt = select(user_alias).order_by(user_alias.id)
with get_db_session() as session:
    for obj in session.execute(orm_stmt).scalars():
        print(obj)
