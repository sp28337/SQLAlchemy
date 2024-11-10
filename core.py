from sqlalchemy import insert, select, bindparam

from core_models import *
from database import get_db_engine

engine = get_db_engine()

insert_stmt = insert(address_table).returning(
    address_table.c.id, address_table.c.email_address
)
print(insert_stmt)

# Его также можно комбинировать с Insert.from_select(),
# как в примере ниже, который основан на примере, указанном в INSERT…FROM SELECT
#                                |
#                                V
# ------------------------------------------------------------------------
# Эта конструкция используется, когда требуется скопировать данные из какой-то другой части базы данных
# непосредственно в новый набор строк, без фактического извлечения и повторной отправки данных от клиента.
print('-----------------------------------------------------------------------')
select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
insert_stmt = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt
)
print(insert_stmt)
