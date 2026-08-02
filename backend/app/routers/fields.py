from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models.field import Field
from schemas.field import FieldCreate, FieldResponse


router = APIRouter(
    prefix="/api/v1/fields",
    tags=["Fields"],
)


@router.post(
    "",
    response_model=FieldResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_field(
    field_data: FieldCreate,
    db: Session = Depends(get_db),
):
    field = Field(
        name=field_data.name,
        crop_type=field_data.crop_type,
        location=field_data.location,
    )

    db.add(field)
    db.commit()
    db.refresh(field)

    return field


@router.get(
    "",
    response_model=list[FieldResponse],
)
def get_fields(
    db: Session = Depends(get_db),
):
    statement = select(Field)

    result = db.execute(statement)

    fields = result.scalars().all()

    return fields