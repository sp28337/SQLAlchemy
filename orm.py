from database import get_db_session
from orm_models import User

squidward = User(name="squidward", fullname="Squidward Tentacles")
krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")
session = get_db_session()
session.add(squidward)
print(squidward)
session.add(krabs)
session.flush()
print("-" * 60)

# Первичный ключевой идентификатор объектов имеет значение для Session, поскольку объекты теперь связаны с этим
# идентификатором в памяти с помощью функции, известной как Indentity Map (карта идентификаторов).
# Карта идентификаторов — это хранилище в памяти, которое связывает все объекты, загруженные в данный момент в память,
# с их первичным ключом идентификатора. Мы можем наблюдать это, извлекая один из указанных выше объектов с помощью
# Session.get() метода, который вернет запись из карты идентификаторов, если она присутствует локально,
# в противном случае выдавая SELECT:

some_squidward = session.get(User, 4)
print(some_squidward)

# Важно отметить, что карта идентичности поддерживает уникальный экземпляр конкретного объекта Python для конкретной
# идентичности базы данных в рамках конкретного Session объекта. Мы можем заметить, что some_squidward ссылается на
# тот же объект, что и squidward ранее:

print(some_squidward is squidward)

# Карта идентичности — это важнейшая функция, которая позволяет манипулировать сложными
# наборами объектов в рамках транзакции без нарушения синхронизации.
