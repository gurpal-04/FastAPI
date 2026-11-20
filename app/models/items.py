from pydantic import BaseModel

class Item(BaseModel):
    title: str
    description: str
    completed: bool

class ItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class ResponseModel(BaseModel):
    message: str
    data: dict | None = None