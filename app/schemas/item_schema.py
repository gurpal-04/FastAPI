from pydantic import BaseModel, ConfigDict
from uuid import UUID

class Item(BaseModel):
    title: str
    description: str
    completed: bool

class ItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class ItemResponse(BaseModel):
    id: UUID
    title: str
    description: str | None = None
    completed: bool

    model_config = ConfigDict(from_attributes=True)


class ResponseModel(BaseModel):
    message: str
    data: ItemResponse | None = None