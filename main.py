from fastapi import FastAPI


app = FastAPI()


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