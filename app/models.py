from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://mongodb:27017/')
db = client['inventory_db']

class Store:
    collection = db['stores']

    @classmethod
    def create_store(cls, store_id):
        cls.collection.insert_one({"_id": store_id, "report": []})

    @classmethod
    def get_store(cls, store_id):
        return cls.collection.find_one({"_id": store_id})

    @classmethod
    def update_store(cls, store_id, report):
        cls.collection.update_one({"_id": store_id}, {"$set": {"report": report}})

class Item:
    collection = db['items']

    @classmethod
    def create_item(cls, item_id, quantity):
        cls.collection.insert_one({"_id": item_id, "quantity": quantity})

    @classmethod
    def get_item(cls, item_id):
        return cls.collection.find_one({"_id": item_id})

    @classmethod
    def update_item(cls, item_id, quantity):
        cls.collection.update_one({"_id": item_id}, {"$set": {"quantity": quantity}})
