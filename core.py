from sqlalchemy import select

from core_models import *
from database import get_db_engine, get_db_session
from orm_models import User, Address

engine = get_db_engine()

print(select(User))
print()

with get_db_session() as session:
    #   При выполнении оператора, подобного приведенному выше, с использованием Session.execute() метода ORM,
    # есть важное отличие, когда мы выбираем из полной сущности, такой как User, в отличие от user_table,
    # которое заключается в том, что сама сущность возвращается как один элемент в каждой строке User.
    # То есть, когда мы извлекаем строки из приведенного выше оператора, поскольку в списке того, что нужно извлечь,
    # есть только сущность, мы получаем обратно Row объекты, которые имеют только один элемент,
    # которые содержат экземпляры класса User:

    row = session.execute(select(User)).first()
    print(row)

    # Выше приведенный пример Row содержит только один элемент, представляющий User сущность:

    print(row[0])

    # Настоятельно рекомендуемый удобный метод достижения того же результата, что и выше — это
    # использование Session.scalars() метода для непосредственного выполнения оператора;
    # этот метод вернет ScalarResult объект, который возвращает первый «столбец» каждой строки сразу,
    # в данном случае — экземпляры класса User:

    row = session.scalars(select(User)).first()
    print(row)

    # В качестве альтернативы мы можем выбрать отдельные столбцы сущности ORM как отдельные элементы
    # в строках результата, используя атрибуты, связанные с классом; когда они передаются в конструкцию,
    # такую как select(), они разрешаются в Column или другое выражение SQL, представленное каждым атрибутом:

    print(select(User.name, User.fullname))
    row = session.execute(select(User.name, User.fullname)).first()
    print(row)

    # Подходы также могут быть смешанными, как показано ниже, где мы ВЫБИРАЕМ name атрибут сущности User
    # в качестве первого элемента строки и объединяем его с полными Addressсущностями во втором элементе:

    print(
        session.execute(
            select(User.name, Address).where(User.id == Address.user_id).order_by(Address.id)
        ).all()
    )
