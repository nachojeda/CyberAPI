import hashlib
import logging

from typing import Union
from fastapi import FastAPI
from adapters.connectors import create_connection_db


app = FastAPI()

@app.post("/users")
def create_user(user_id: Union[str, None], password: Union[str, None]):
    """
    Endpoint for new user insertion into MongoDB
    """
    # Create connection to MongoDB
    db = create_connection_db()
    # Hash password before inserting
    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # Inserting data in DB
    data = {
        "user_id": user_id,
        "password": hashed_pass
    }
    users = db.users
    insert_id = users.insert_one(data).inserted_id
    logging.info(f"Object inserted: {insert_id}")
    return {"User": user_id, "Hash": hashed_pass}

# @app.get("/users/{user_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}