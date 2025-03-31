import hashlib

from typing import Union
from fastapi import FastAPI


app = FastAPI()

@app.post("/users")
def create_user(user_id: Union[str, None], password: Union[str, None]):
    hashed_pass = hashlib.sha256(password).hexdigest()

@app.get("/users/{user_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}