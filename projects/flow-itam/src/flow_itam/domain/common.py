from pydantic import BaseModel, ConfigDict
from uuid import UUID

class DomainModel(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        validate_assignment=True,
        extra="forbid"
    )