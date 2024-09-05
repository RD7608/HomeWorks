
from sqlalchemy.schema import CreateTable
from models.task import Task
from models.user import User

print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))
