import os

from bson import ObjectId
from fastapi import Request
from pymongo.collection import Collection
from typing import List, Dict


class CategoryRepository:
    def __init__(self, request: Request):
        self.collection: Collection = request.app.state.mongo_client[os.environ.get("DB")][os.environ.get("CATEGORY_COLLECTION")]  # MongoDB collection

    async def get_all_categories(self) -> List[Dict]:
        categories = self.collection.find()
        return [{"id": str(category["_id"]), "name": category["name"], "description": category["description"]} for category in categories]

    async def get_category_by_id(self, category_id: str) -> Dict:
        category = self.collection.find_one({"_id": ObjectId(category_id)})
        return {"id": str(category["_id"]), "name": category["name"], "description": category["description"]} if category else None

    async def create_category(self, category_data: Dict) -> str:
        result = self.collection.insert_one(category_data)
        return str(result.inserted_id)

    async def update_category(self, category_id: str, update_data: Dict):
        result = self.collection.find_one_and_update({"_id": ObjectId(category_id)}, {"$set": update_data}, return_document=True)
        return {"id": str(result["_id"]), "name": result["name"], "description": result["description"]} if result else None

    async def delete_category(self, category_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(category_id)})
        return result.deleted_count > 0
    
    async def get_categories_by_ids(self, category_ids: List[str]) -> Dict[str, Dict]:
        # Convert category IDs to ObjectIds for MongoDB and retrieve all matching categories
        object_ids = [ObjectId(category_id) for category_id in category_ids]
        categories = self.collection.find({"_id": {"$in": object_ids}})
        
        # Return a dictionary mapping each category's ID to its data for easy access
        return {str(category["_id"]): category for category in categories}