from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {
    1:{
        "name": "juice",
        "price": 2.99,
        "brand": "Juicy"
    }
}

@app.get("/")
def home():
    return{"Data": "Testing"}

@app.get("/about")
def about():
    return{"Data":"About"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.post("/create-item/{item_id}")
def create_iten(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}

    inventory[item_id] = item
    return inventory[item_id]