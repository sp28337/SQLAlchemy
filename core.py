from sqlalchemy import select, func

from core_models import *
from database import get_db_engine

engine = get_db_engine()


# Если мы выбираем один столбец из конкретной таблицы, то Table указывается после FROM:
print(select(user_table.c.name))

print("-" * 60)
# Если бы мы выбирали столбцы из двух таблиц, то получили бы предложение FROM, разделенное запятыми:

print(select(user_table.c.name, address_table.c.email_address))

print("." * 60)
# Для того, чтобы ОБЪЕДИНИТЬ эти две таблицы вместе, мы обычно используем один из двух методов Select.
# Первый — это Select.join_from() метод, который позволяет нам явно указать левую и правую сторону ОБЪЕДИНЕНИЯ:

print(
    select(user_table.c.name, address_table.c.email_address).join_from(
        user_table, address_table
    )
)

print("_" * 60)
# Другой метод Select.join() указывает только правую сторону JOIN, левая сторона выводится:

print(select(user_table.c.name, address_table.c.email_address).join(address_table))

print("*" * 60)
# У нас также есть возможность явно добавлять элементы в предложение FROM, если это не выводится так, как мы хотим,
# из предложения columns. Мы используем Select.select_from() метод, чтобы добиться того, как показано ниже,
# где мы устанавливаем user_table в качестве первого элемента в предложении FROM и Select.join() устанавливаем
# address_table в качестве второго:

print(select(address_table.c.email_address).select_from(user_table).join(address_table))

print("`" * 60)
# Другой пример, где мы могли бы захотеть использовать Select.select_from(), если в нашем предложении columns
# недостаточно информации для предоставления предложения FROM. Например, чтобы SELECT из общего выражения SQL count(*),
# мы используем элемент SQLAlchemy, известный как sqlalchemy.sql.expression.func для создания функции SQL count():

print(select(func.count("*")).select_from(user_table))
