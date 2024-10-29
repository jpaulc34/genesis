import os

from bson import ObjectId
from fastapi import Request
from typing import List, Dict

from app.repositories.base_repository import BaseRepository

class CategoryRepository(BaseRepository):
    def __init__(self, request: Request):
        collection = request.app.state.mongo_client[os.environ.get("DB")][os.environ.get("CATEGORY_COLLECTION")]  # MongoDB collection
        super().__init__(collection)
    
    async def get_categories_by_ids(self, category_ids: List[str]) -> Dict[str, Dict]:
        # Convert category IDs to ObjectIds for MongoDB and retrieve all matching categories
        object_ids = [ObjectId(category_id) for category_id in category_ids]
        categories = self.collection.find({"_id": {"$in": object_ids}})
        
        # Return a dictionary mapping each category's ID to its data for easy access
        return {str(category["_id"]): category for category in categories}