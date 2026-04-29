from uuid import UUID, uuid4
from pydantic import Field
from .common import DomainModel


class Vendor(DomainModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    contact_email: str | None = None