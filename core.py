from sqlalchemy import insert

from core_models import *
from database import engine

stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
print(f'{'\n [!]  '}{stmt}{'\n'}')
compiled = stmt.compile()
print(f'{'\n [!]  '}{compiled.params}{'\n'}')
