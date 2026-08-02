from datetime import datetime

from pydantic import BaseModel, ConfigDict


class FieldCreate(BaseModel):
    name: str
    crop_type: str
    location: str | None = None


class FieldResponse(BaseModel):
    id: int
    name: str
    crop_type: str
    location: str | None
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )