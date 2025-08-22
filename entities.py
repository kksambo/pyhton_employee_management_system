from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from database_setup import DatabaseSetUp

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    title = Column(String)
    role = Column(String)
    employee_number = Column(String)
    organisation = Column(String)

async def on_startup(db_set_up :DatabaseSetUp):

    async with db_set_up.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
