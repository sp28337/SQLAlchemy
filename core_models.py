"""
Migration tools are usually appropriate

Overall, the CREATE / DROP feature of MetaData is useful for test suites, small and/or new applications,
and applications that use short-lived databases. For management of an application database schema over the long term
however, a schema management tool such as Alembic, which builds upon SQLAlchemy, is likely a better choice,
as it can manage and orchestrate the process of incrementally altering a fixed database schema over time
as the design of the application changes.

https://docs.sqlalchemy.org/en/20/tutorial/metadata.html
"""


from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

from database import get_db_engine


engine = get_db_engine()


metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)


metadata_obj.create_all(engine)
