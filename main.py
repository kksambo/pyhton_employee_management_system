from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uvicorn
import entities
from database_setup import DatabaseSetUp
from entities import User, Employee
from pydantics_models import UserIn, EmployeeIn
from url_maker import Urlmaker


url = Urlmaker(
    host='localhost',
    port=5432,
    database_name='postgres',
    username='postgres',
    password='1234',
    driver='postgresql+asyncpg'
)
database_setup = DatabaseSetUp(url.get_url())




# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await entities.on_startup(database_setup)


@app.post("/users/")
async def create_user(user:UserIn, db: AsyncSession = Depends(database_setup.get_db)):
    new_user = User(name=user.name)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@app.get("/users/")
async def list_users(db: AsyncSession = Depends(database_setup.get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


@app.post("/employees/")
async def create_employee(employee: EmployeeIn,db: AsyncSession = Depends(database_setup.get_db)):
    try:
        new_employee = Employee(
                                first_name = employee.first_name,
                                last_name = employee.last_name,
                                email = employee.email,
                                title = employee.title,
                                role = employee.role,
                                employee_number = employee.employee_number,
                                organisation = employee.organisation
                                )

        db.add(new_employee)
        await db.commit()
        await db.refresh(new_employee)
        return new_employee

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app)