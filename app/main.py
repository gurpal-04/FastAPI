from fastapi import FastAPI
from .api.v1 import items_router

app = FastAPI()

app.include_router(items_router, prefix="/api/v1/items")

@app.get("/")
def root():
    return {"welcome to FastAPI"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}