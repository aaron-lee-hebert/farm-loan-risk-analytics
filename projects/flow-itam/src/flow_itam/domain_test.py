from uuid import uuid4
from domain.user import User

u = User(id=uuid4(), name="Aaron Hebert", email="aaron.lee.hebert@gmail.com")
print(u)