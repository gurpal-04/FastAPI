from fastapi import APIRouter, HTTPException, Depends
from uuid import UUID, uuid4
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db import read_db, write_db, get_db
from app.schemas import Item, ItemUpdate, ResponseModel
from app.models import Item as ItemModel

router = APIRouter()

@router.get("/")
def get_items(db=Depends(get_db)):
    return db.query(ItemModel).all()

@router.post("/", response_model=ResponseModel)
def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = ItemModel(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item created successfully", "data": db_item}
    

@router.get("/{item_id}")
def get_item(item_id: UUID, db: Session = Depends(get_db)):
    db_item = db.execute(
        select(ItemModel).where(ItemModel.id == item_id)
    ).scalar_one_or_none()   
    
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=ResponseModel)
def update_item(item_id: UUID, updated_item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.execute(
        select(ItemModel).where(ItemModel.id == item_id)
    ).scalar_one_or_none()  

    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in updated_item.model_dump(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item updated successfully", "data": db_item}

@router.delete("/{item_id}", response_model=ResponseModel)
def delete_item(item_id: UUID, db: Session = Depends(get_db)):

    db_item = db.execute(
        select(ItemModel).where(ItemModel.id == item_id)
    ).scalar_one_or_none()   

    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully", "data": db_item}