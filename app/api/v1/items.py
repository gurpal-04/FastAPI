from fastapi import APIRouter
from uuid import UUID, uuid4

from ...db import read_db, write_db
from ...models import Item, ItemUpdate, ResponseModel

router = APIRouter()

@router.get("/")
def get_items():
    return read_db()

@router.post("/", response_model=ResponseModel)
def create_item(item: Item):
    tasks = read_db()

    new_task = {
        "id": str(uuid4()),
        **item.dict()
    }
    tasks.append(new_task)
    write_db(tasks)
    return {"message": "Item created successfully", "data": new_task}

@router.get("/{item_id}")
def get_item(item_id: UUID):
    tasks = read_db()
    for task in tasks:
        if task.get("id") == str(item_id):
            return task
    return {"message": "Item not found"}

@router.put("/{item_id}", response_model=ResponseModel)
def update_item(item_id: UUID, updated_item: ItemUpdate):
    tasks = read_db()
    for index, task in enumerate(tasks):
        if task.get("id") == str(item_id):
            tasks[index].update(updated_item.dict(exclude_unset=True))
            write_db(tasks)
            return {"message": "Item updated successfully", "data": tasks[index]}
    return {"message": "Item not found"}

@router.delete("/{item_id}", response_model=ResponseModel)
def delete_item(item_id: UUID):
    tasks = read_db()
    for index, task in enumerate(tasks):
        if task.get("id") == str(item_id):
            deleted_task = tasks.pop(index)
            write_db(tasks)
            return {"message": "Item deleted successfully", "data": deleted_task}
    return {"message": "Item not found"}