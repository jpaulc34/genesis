import os

from bson import ObjectId
from fastapi import Request
from pymongo.collection import Collection
from typing import List, Dict


class UserRepository:
    def __init__(self, request: Request):
        self.collection: Collection = request.app.state.mongo_client[os.environ.get("DB")][os.environ.get("USER_COLLECTION")]  # MongoDB collection

    async def get_all_users(self) -> List[Dict]:
        users = self.collection.find()
        return [{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]

    async def get_user_by_id(self, user_id: str) -> Dict:
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        return {"id": str(user["_id"]), "name": user["name"], "email": user["email"]} if user else None

    async def create_user(self, user_data: Dict) -> str:
        result = self.collection.insert_one(user_data)
        return str(result.inserted_id)

    async def update_user(self, user_id: str, update_data: Dict):
        result = self.collection.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": update_data}, return_document=True)
        return {"id": str(result["_id"]), "name": result["name"], "email": result["email"]} if result else None

    async def delete_user(self, user_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0