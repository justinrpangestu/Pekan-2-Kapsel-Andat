from fastapi import FastAPI
from modules.items.routes import createItem, readItem, updateItem, deleteItem
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


app.include_router(createItem.router)
app.include_router(readItem.router)
app.include_router(updateItem.router)
app.include_router(deleteItem.router)


