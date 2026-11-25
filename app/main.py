from fastapi import FastAPI
from .api.v1 import items_router
from .db.database import Base, engine

app = FastAPI()

app.include_router(items_router, prefix="/api/v1/items", tags=["Items"])

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"welcome to FastAPI"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}