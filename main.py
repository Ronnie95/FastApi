from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: str = None
    price: float = None
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

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"error": "item ID already exists"}
    
    inventory[item_id].update(item)
    return inventory[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"Error": "Id not working"}
    
    del inventory[item_id]