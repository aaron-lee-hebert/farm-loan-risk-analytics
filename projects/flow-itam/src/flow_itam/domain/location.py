from uuid import UUID, uuid4
from pydantic import Field
from .common import DomainModel


class Location(DomainModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str | None = None