from pymongo import MongoClient

def create_connection_db():
    client = MongoClient("mongodb://localhost:27017")
    db = client.AppDatabase
    return db