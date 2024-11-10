from sqlalchemy import insert

from core_models import *
from database import get_db_engine

# print()
# print(insert(user_table))
# print()

with get_db_engine().connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
        ],
    )
    # conn.commit()


