import os

from bson import ObjectId
from fastapi import Request
from pymongo.collection import Collection
from typing import List, Dict


class ProductRepository:
    def __init__(self, request: Request):
        self.collection: Collection = request.app.state.mongo_client[os.environ.get("DB")][os.environ.get("PRODUCT_COLLECTION")]  # MongoDB collection

    async def get_all_products(self) -> List[Dict]:
        products = self.collection.find()
        return [{"id": str(product["_id"]), **product} for product in products]

    async def get_product_by_id(self, product_id: str) -> Dict:
        product = self.collection.find_one({"_id": ObjectId(product_id)})
        return {"id": str(product["_id"]), **product} if product else None

    async def create_product(self, product_data: Dict) -> str:
        result = self.collection.insert_one(product_data)
        return str(result.inserted_id)

    async def update_product(self, product_id: str, update_data: Dict):
        result = self.collection.find_one_and_update({"_id": ObjectId(product_id)}, {"$set": update_data}, return_document=True)
        return {"id": str(result["_id"]), **result} if result else None

    async def delete_product(self, product_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(product_id)})
        return result.deleted_count > 0
    
    async def get_products_by_category_id(self, category_id: str) -> Dict:
        products = self.collection.find({"category_id": (category_id)})
        return [{"id": str(product["_id"]), **product} for product in products]