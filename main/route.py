from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@router.get("/")
def root():
    return {"message": "Hello from FastAPI"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/items")
def create_item(item: Item):
    return item
