from datetime import datetime
from uuid import UUID, uuid4
from pydantic import Field
from .common import DomainModel

class Assignment(DomainModel):
    id: UUID = Field(default_factory=uuid4)

    asset_id: UUID
    user_id: UUID

    assigned_at: datetime = Field(default_factory=datetime.utcnow)
    returned_at: datetime | None = None