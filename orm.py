from database import get_db_session
from orm_models import User

squidward = User(name="squidward", fullname="Squidward Tentacles")
krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")

# Чтобы проиллюстрировать процесс добавления шаг за шагом, мы создадим Session без использования менеджера контекста
# (и поэтому мы должны убедиться, что мы закрыли его позже!):

session = get_db_session()
print(session)

# Затем объекты добавляются в Session с помощью Session.add() метода. Когда он вызывается, объекты
# находятся в состоянии, известном как ожидание, и еще не были вставлены:

session.add(squidward)
session.add(krabs)

print("-" * 60)
# Когда у нас есть ожидающие объекты, мы можем увидеть это состояние,
# посмотрев на коллекцию Session в вызываемом объекте Session.new:

print(session.new)

# Представление выше использует коллекцию, называемую IdentitySet, которая по сути является набором Python,
# который хэширует идентификатор объекта во всех случаях
# (т. е. использует встроенную id() функцию Python, а не hash() функцию Python).
