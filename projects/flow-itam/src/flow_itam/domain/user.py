from uuid import UUID, uuid4
from pydantic import EmailStr, Field
from .common import DomainModel

class User(DomainModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: EmailStr