import os
from bson import ObjectId
from fastapi import Request, HTTPException, status
from typing import List, Dict, Optional

from app.api.repositories.base_repository import BaseRepository

class ProductRepository(BaseRepository):
    def __init__(self, request: Request):
        collection = request.app.state.mongo_client[os.environ.get("DB")][os.environ.get("PRODUCT_COLLECTION")]  # MongoDB collection
        super().__init__(collection)
    
    async def get_products_by_category_id(self, category_id: str) -> Dict:
        products = self.collection.find({"category_id": (category_id)})
        return [{"id": str(product["_id"]), **product} for product in products]
    
    async def get_stock(self, id: str) -> Optional[Dict]:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid product ID format")
        
        projection = {"quantity": 1, "_id": 0}

        result = self.collection.find_one({"_id": ObjectId(id)}, projection)
        
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        
        return result
    
    async def update_stock(self, id: str, data: Dict) -> Optional[Dict]:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid product ID format")

        result = self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": data},
            return_document=True)
        
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        
        result["id"] = str(result["_id"])  # Rename _id to id for JSON compatibility
        del result["_id"]                  # Remove the original _id key to avoid confusion

        return {"quantity": result["quantity"]}