from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None

@app.get('/')
def get_server_msg():
    return {'Message':'Message from fast api server'}

@app.get('/health')
def health_check():
    return {'Health':'ok'}

@app.post('/items/')
def create_item(item: Item):
    return {"message": "Item created", "item": item}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {"message": f"Item {item_id} updated", "item": item}