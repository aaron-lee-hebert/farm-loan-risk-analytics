from datetime import date
from uuid import UUID
from pydantic import Field
from .common import DomainModel

class Asset(DomainModel):
    id: UUID = Field(default_factory=UUID)
    name: str
    asset_type: str
    serial_number: str | None = None
    purchase_date: date | None = None